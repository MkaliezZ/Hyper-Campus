# v0.8.2 · Ubuntu全栈与Hermes部署技术验收

状态：**封装前部署技术验收 PASS**。本记录对应2026-10-24本机Ubuntu的实际运行；最终ZIP的CRC/SHA、源码一致性、归档镜像与追加模型调用记录随交付ZIP另存，不能用本记录替代归档后的复核。

## 环境与来源

- 从保留的v0.8.1 ZIP开始，校验其CRC和全部3819项文件SHA-256后解压。修复安装与容器配置后形成v0.8.2候选ZIP；当前候选再解压、校验、构建核心及Hermes镜像。
- WSL本地Ubuntu 26.04.1，容器Ubuntu 26.04/Linux amd64；全新Docker项目 `hd-zip082-20261024`，首次创建独立的七个数据库、卷、虚构学校及账号。没有复制旧应用状态、个人Hermes配置或用户数据库。
- Keycloak、双校NodeBB、双校Nakama、PostgreSQL/pgvector、Base按健康依赖启动。源码在镜像内，未从宿主机挂载应用源码。Base使用UID/GID 10001；仅Base挂载模型密钥。
- Hermes固定官方提交 `0a62610f10cc34d696b2239b2c69fa1ba0f1ca63`，版本0.19.1；固定Python 3.13.17，原uv.lock冻结核心依赖。实际回答调用联网DeepSeek，不是离线模型。
- 首次下载使用固定SHA-256校验的公开第三方缓存；后续构建复用本轮安装得到的可信依赖缓存。下载缓存不进入通用ZIP、用户卷或最终Hermes运行层。

## 实际通过的验证

| 范围 | 已观察结果 | 证据 |
| --- | --- | --- |
| 源码与空间 | doctor、双校场景构建和空间/导航契约校验通过；45项单元测试通过 | `unit-tests.txt` |
| 正式身份与权限 | 实际Keycloak浏览器登录、当前学校/组织隔离、受邀角色与撤权、消息双向同意及撤销 | `backend-contacts.json`、`backend-network.json`及浏览器报告 |
| 人物、背包和场景 | 保存、CAS冲突、重试、旧数据保留、欢迎包、到达门槛、非破坏性道具、独立浏览器恢复 | `backend-m2.json`、`browser-avatar.json` |
| 论坛、运营与计分 | 原生正文审核、修改/撤回、附件与点位、单次贡献、原额冲正、榜单冻结/重建 | `backend-community.json`、`backend-ledger.json`、`browser-community.json` |
| 校园连接与合作 | 自愿目录、学长预约、机会原生正文、负责人管理；入驻、发布、用户同意、取消和权益核销 | `backend-network.json`、`browser-network.json`、`browser-partners.json` |
| A2A与索引 | 官方SDK及独立Agent进程、最小委托、用户确认、重试/撤权；公开向量和私有审核历史自动更新、撤回即时失效 | `backend-a2a.json`、`backend-indexing.json` |
| 容器内真实Hermes | 8次真实调用、两名访客并发成功且不串会话、刷新恢复；实际重启Base容器后继续记忆 | `hermes-browser-before-restart.json`、`hermes-browser-after-restart.json` |
| 资料及记忆边界 | 已发布地点引用、未知学校事实不编造；本人JSON导出、删除、旧消息重放和旧context拒绝；当前PG快照与Hermes文件无被删除的测试口令 | 两份Hermes浏览器报告、`container-package-live.json` |
| 完整备份恢复 | 停止全部应用写入者后，七库及49项文件备份/校验并恢复至新命名空间；11张关键表逐行摘要一致，恢复的真实会话可导出，其他owner被拒绝 | `container-restore-live.json` |

机器可读汇总为 `SUMMARY.json`。其中67项命名检查与45项单元测试分别计数，不把重复调用当成新的功能验收。人物截图属于可运行占位样例；最新产品分工见 `docs/AVATAR-SCHOOL-ART.md`，学校自行提供美术，Base不继续扩充通用款式。

## 失败记录与修正

构建中遇到并修正了Python范围、旧uv锁解析、下载与重复npm安装问题；记录保存在 `BUILD-AND-TEST-NOTES.json`。旧M1专项脚本的早期通知格式/无联系人同意假设与当前校园契约不同，未把这些旧脚本标成全通过；使用当前社区、贡献账本与联系人测试完成对应验证，没有修改其断言或业务限时。合作办理使用明确启用的本地虚构适配器，默认部署仍拒绝未配置的外部办理。

## 验收边界

- 这是同一主机上的Ubuntu容器与独立浏览器上下文自动化，未进行真人、物理多设备或真实学校运营验收。
- 已验证七库完整存储恢复及会话管理器，不声称完成新生产服务器的域名/客户端切换。实际Ubuntu服务器、HTTPS/DNS、正式SMTP、目标并发/负载和商户接口仍需在目标环境配置复测。
- 模型密钥、真实学校图纸、运营原件、账号口令、浏览器cookie、对话导出和数据库备份不进入公开包。导出副本及历史备份的保留由其持有人管理，不声称删除在线会话能远程擦除副本或数据库历史介质。
- 保留所有旧交付包和用户数据。本版没有再创建独立接包子Agent，也没有恢复小游戏、重型捏脸或P2开发。
