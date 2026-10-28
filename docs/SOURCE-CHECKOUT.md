# Hyper Campus 源码检出

Git 是可继续开发的源码；旧 ZIP 是封存快照。不要将旧 `PACKAGE-MANIFEST.json` 复制到修改后的源码检出，也不要为通过旧清单覆盖开发改动。

1. `npm ci --ignore-scripts`、`npm run setup` 安装锁定依赖并生成浏览器库。
2. 修改管理台前执行 `npm --prefix admin ci --ignore-scripts`，之后 `npm --prefix admin run build`。
3. 向量模型：`python3 tools/fetch-embedding-model.py`；Python 依赖在 `requirements-embedding.txt`。
4. Hermes 容器：`python3 tools/prepare-hermes-source.py`。它在忽略目录获取官方固定提交，通过 `git archive` 重建并校验 `SOURCE.json` 中的原 SHA-256，再从 PyPI 下载并核验固定 uv 轮子。不运行 Agent、不读取用户密钥或对话。重复执行先校验；已有冲突文件保留并停止。
5. 之后遵循 `DEPLOYMENT-CONTAINERS.md`。核心 Dockerfile 的源码分支安装依赖/生成前端，Hermes 层消费步骤4准备的输入。`--check` 仅检查现有输入，不联网。
6. 完整打包前准备必需模型、固定源码、许可证、生产依赖、管理台和实际验收，再运行原打包器。Git 本身不是离线整机镜像。

文档中的“完整ZIP已经包含依赖/模型”只适用于历史交付快照，不适用于本 Git 源码。既有验收仍按原版本归属，本次代码仓库检查只看 `evidence/github-source/`。不要提交真实学校原图、运营材料、数据库或私人配置。
