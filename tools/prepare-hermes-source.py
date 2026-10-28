"""Prepare pinned third-party build inputs without committing archives or private data."""
from pathlib import Path
import argparse, hashlib, json, subprocess, urllib.request
ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'integrations/hermes'
META = json.loads((DEST / 'SOURCE.json').read_text(encoding='utf-8'))
WHEEL = 'uv-0.12.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl'
WHEEL_SHA = '27211df9b277f440dea438a4e525ba40250fb721ad39b8927eefc2d91f9aea15'

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''): h.update(chunk)
    return h.hexdigest()

def verified(path, digest):
    if not path.exists(): return False
    if sha(path) != digest: raise RuntimeError('Existing mismatched input preserved: ' + str(path))
    return True

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    archive = DEST / META['archive']; wheel = DEST / WHEEL
    archive_ok = verified(archive, META['archiveSha256']); wheel_ok = verified(wheel, WHEEL_SHA)
    if args.check:
        print(json.dumps({'archiveReady': archive_ok, 'uvReady': wheel_ok, 'commit': META['commit']})); return
    if not archive_ok:
        upstream = DEST / 'upstream'
        if not upstream.exists():
            subprocess.run(['git', 'init', str(upstream)], check=True)
            subprocess.run(['git', '-C', str(upstream), 'remote', 'add', 'origin', META['repository']], check=True)
        remote = subprocess.check_output(['git', '-C', str(upstream), 'remote', 'get-url', 'origin'], text=True).strip()
        if remote != META['repository']: raise RuntimeError('Unexpected upstream remote; preserved')
        subprocess.run(['git', '-C', str(upstream), 'fetch', '--depth=1', 'origin', META['commit']], check=True)
        staged = DEST / 'source-preparing.tar.gz'
        if staged.exists(): raise RuntimeError('Previous partial preparation preserved: ' + str(staged))
        subprocess.run(['git', '-C', str(upstream), 'archive', '--format=tar.gz', '--prefix=hermes/',
                        '--output=' + str(staged), META['commit']], check=True)
        if sha(staged) != META['archiveSha256']: raise RuntimeError('Archive digest mismatch; partial output preserved')
        staged.rename(archive)
    if not wheel_ok:
        with urllib.request.urlopen('https://pypi.org/pypi/uv/0.12.1/json', timeout=45) as response: index = json.load(response)
        row = next(r for r in index['urls'] if r['filename'] == WHEEL)
        if row['digests']['sha256'] != WHEEL_SHA or not row['url'].startswith('https://files.pythonhosted.org/'):
            raise RuntimeError('Unexpected wheel source')
        staged = DEST / (WHEEL + '.partial')
        if staged.exists(): raise RuntimeError('Previous partial wheel preserved: ' + str(staged))
        with urllib.request.urlopen(row['url'], timeout=60) as source, staged.open('xb') as dest:
            for chunk in iter(lambda: source.read(1024 * 1024), b''): dest.write(chunk)
        if sha(staged) != WHEEL_SHA: raise RuntimeError('Wheel digest mismatch')
        staged.rename(wheel)
    print(json.dumps({'status': 'READY', 'commit': META['commit'], 'archiveSha256': sha(archive), 'uvSha256': sha(wheel)}))
if __name__ == '__main__': main()
