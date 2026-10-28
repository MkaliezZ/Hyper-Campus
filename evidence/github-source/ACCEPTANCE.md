# Hyper Campus Git 源码首版验收

2026-10-28，Windows/Node 24.22.1。本次为独立私有代码仓库整理，不改原 Base 工作目录和封存包，不包含学校用户项目、原图纸、运行配置、数据库或模型密钥。

已实际执行：根目录锁定 `npm ci --ignore-scripts`、`npm run setup`、doctor、示例空间 verify/build；45 项 Node 测试全部通过。后台依赖从同锁的既有开发目录复用；其中 Windows esbuild 二进制异常，已从锁定 npm 官方包获取并核对 SHA-512 后修复，本目录 React-admin 构建成功。再次运行完整测试验证新构建。

完整打包测试需要模型、Hermes 固定归档、管理台及生产依赖。此次使用已封存来源对应的公开模型/固定源码作为忽略的本地输入，未向 Git 提交这些生成物；`prepare-hermes-source.py --check` 验证它们与原固定 SHA-256 一致。新准备脚本的联网重建分支本次未重新下载完整 Hermes；不能把本地输入核验说成新网络安装/真实模型验证。

`evidence/ubuntu-hermes/` 与其他旧证据继承原版本范围。本轮没有新运行 Ubuntu 全栈、真实 Hermes/模型调用、真实学校运营或实体多设备验收。Git 源码需要按 README 和 SOURCE-CHECKOUT 准备依赖后运行，不是旧完整 ZIP 的离线替代物。

库内不保存 ZIP 或其他依赖归档，也不创建 Release 附件。仓库名称为 Hyper Campus，协议/包名保持兼容。
