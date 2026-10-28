# Hyper Campus

校园空间开发底座：学生会提供图纸、公开信息、运营规则和美术，人类开发者或 Agent 在共同协议、权限和服务上搭建自己的校园。

这是**私有源码仓库**，不是 ZIP 附件库。代码采用 Hyper Dimension Base v0.8.2 运行时与 v0.8.3 统一开发文档，核心协议 v0.2.1。品牌为 Hyper Campus；现有 `hyper-dimension` 包名、协议和接口 ID 保留兼容。

## 四个 Base

| 模块 | 功能 | 实现 |
| --- | --- | --- |
| Base-1 空间与接待 | 建模、导航、protocol、A2A、接待 Agent、资料检索、隔离会话及导出删除 | Three.js、官方 A2A SDK、Hermes 适配、PostgreSQL/pgvector |
| Base-2 人物与互动 | 简单部件搭配、动作、存档、背包轻道具、联系人、私信与聊天 | Base 服务端权限/状态、Nakama；学校提供正式美术 |
| Base-3 论坛与运营 | 论坛、地点记忆、审核申诉、活动、年度运营、贡献排行、奖励与历史索引 | NodeBB、pg-boss、Base 事件与账本 |
| Base-4 校外合作 | 入驻审核、合作目录、工单、授权转交、权益核销及业务 A2A | Base 委托、权限、回执及合作方适配器 |

共同能力包括 Keycloak 身份、学校/组织隔离、负责人/管理员后台、审计、事件对账与七库备份恢复。正式学校资料、邮件、域名/TLS、模型、真实合作方和美术由部署者配置；未配置的服务不可冒充已接通。

## 阅读入口

- Agent：[AGENTS.md](AGENTS.md) → [AGENT-START.md](AGENT-START.md) → [统一开发手册](DEVELOPMENT-MANUAL.md)。用户问“这是做什么用的？怎么用？”时先解释，再引导看示例、建校或部署。
- 人类开发者：[统一开发手册](DEVELOPMENT-MANUAL.md) → [当前功能](docs/CURRENT-FEATURES.md)及模块说明。
- 部署维护者：[源码准备](docs/SOURCE-CHECKOUT.md) → [Ubuntu 容器部署](docs/DEPLOYMENT-CONTAINERS.md)。前端为浏览器。
- 搭建学校：[建校流程](prompts/00-BUILD-SCHOOL.md) → [美术深化](prompts/04-VISUAL-POLISH.md)。图纸中的尺寸与推定须记录，不要停留在通用方盒。

## 轻量示例

需要 Node.js 22.13+，建议 Node 24。Git 检出需要安装依赖，与已含依赖的旧完整 ZIP 不同。

```sh
git clone https://github.com/MkaliezZ/Hyper-Campus.git
cd Hyper-Campus
npm ci --ignore-scripts
npm run setup
npm start
```

访问 `http://127.0.0.1:4180`，Ctrl+C 停止。轻量模式提供空间、A2A 与资料接待；完整账号、论坛、聊天、后台使用全栈部署。

## 开发与验证

```sh
npm --prefix admin ci --ignore-scripts
npm --prefix admin run build
node tools/verify-docs.mjs
```

向量检索先执行 `python3 tools/fetch-embedding-model.py` 并配置 PostgreSQL/pgvector。Hermes 容器先执行 `python3 tools/prepare-hermes-source.py` 准备固定上游源码和 uv 安装器，再遵循容器部署手册。生成归档、模型、依赖和构建产物不提交 Git。

完成上述模型、Hermes 输入、根/后台依赖和后台构建后，执行 `npm test`（45项，含完整打包前置检查）。只开发空间时可先执行 `node --test tests/core.test.mjs tests/http.test.mjs tests/a2a-sdk.test.mjs`；完整包测试缺输入应补齐，不应降低断言或把源代码检出宣称为完整离线包。

Hermes 是服务器接待选项；访客本机 Agent 不限品牌，只需兼容 A2A、身份与授权规则。公开接待只读取已发布资料；Base 管理隔离会话，默认30天、学校可配置、本人可导出/删除。不提供个人 Agent 长期记忆。

## 目录

```text
src/          协议、空间、A2A、接待、知识、人物及校园业务
public/       浏览器界面；vendor 脚本由 npm run setup 生成
admin/        React-admin 后台源码和独立依赖锁
database/     PostgreSQL 结构与不可变迁移
deploy/       Ubuntu/Docker Compose、配置生成及恢复
integrations/ 开源适配器、固定版本与来源说明
assets/       原创人物占位部件和素材接口
examples/     可运行虚拟学校示例
schemas/      空间、资料及业务契约
tools/ tests/ 开发、验证、备份恢复与打包
docs/ prompts/模块参考、Agent 工作流程与建校提示词
evidence/     有版本边界的历史技术验收
```

## 数据与版本

学校内容放 `projects/<school>/`，原件放 `.private-inputs/`，运行配置和密钥放私有目录，均不提交 Git。原有本地交付包和用户数据保留。示例与历史自动检查不等于真实学校运营、真实商家履约或物理多设备验收。

来源见 [SOURCE-PROVENANCE.json](SOURCE-PROVENANCE.json)，本轮源码检出验证见 [验收记录](evidence/github-source/ACCEPTANCE.md)。历史 Ubuntu/Hermes 证据保留原时间和范围，不冒充本次新部署。
