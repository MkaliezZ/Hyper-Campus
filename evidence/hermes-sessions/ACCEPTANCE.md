# 本地 Hermes 与接待会话生命周期 · v0.8.1

2026-10-24，本机 Windows / Node 24.19.0 / Python 3.11.15。安装的 Hermes 源码版本 `0a62610f10cc34d696b2239b2c69fa1ba0f1ca63`。调用真实本地 `AIAgent` 与联网 DeepSeek Flash；不是离线模型、固定回答或模拟 provider。虚构 north/south 学校与两个全新浏览器上下文，未读取用户浏览器、个人 Hermes 配置或聊天库。

| 验证 | 结果与证据 |
| --- | --- |
| 真实通用对话、计算与追问 | PASS，8次真实模型调用，均 `transport=local-hermes`、`toolCount=0`；`hermes-sessions-live.json` |
| 独立访客隔离 | PASS，其他访客列表没有原会话，不能复用/导出/删除；真实回答不含另一访客的测试口令 |
| 学校与Agent边界 | PASS，跨学校或不同Agent复用原context拒绝，不增加模型调用 |
| 页面刷新和服务重启 | PASS，同一签名HttpOnly Cookie与数据目录恢复原会话；新Hermes进程能用Base提供的有限历史继续回答 |
| 学校事实与通用智能 | PASS，一般交流可直接回答，已发布房间信息引用真实来源；未提供的校长姓名/电话号码明确未知 |
| 浏览器导出 | PASS，下载JSON包含本人3轮原问题/答案，没有模型密钥；`conversation-samples.json`保留虚构样本 |
| 删除与再次提问 | PASS，删除后旧会话不在列表，导出/复用/原messageId重放被拒绝；Base与Hermes运行目录全部文件不含测试口令，新会话真实回答无法召回 |
| 进程收尾 | PASS，自有浏览器/Base已关闭，8个Hermes调用进程exit 0；`process-cleanup.json` |

浏览器界面证据：`hermes-session-before-delete.png`，仅虚构对话。测试源码：`tests/hermes-sessions-live.mjs`。学校默认30天/可配置、到期清理、删除进行中的晚到结果、CAS冲突等非计时条件另由 `tests/reception-sessions.test.mjs` 检查，不声称实际等待30天。

## 本轮改动与诊断

桥接器在原有零工具、skip_memory、session_db=None的基础上，显式启用Hermes的持久化隔离开关并关闭JSON会话快照。会话的保留、恢复、导出与删除统一由Base管理，模型回复不授予权限，不将私人对话送入公共RAG。

首个完整流程的首轮调用触发既有60秒超时，返回失败并退出；同一配置的独立诊断与全新目录的冷启动诊断随后均真实返回。未取得足以确定该单次超时上游原因的证据，因此不将其描述为已定位的网络故障或已修复的启动缺陷，也未扩大生产时限。第二轮因测试脚本把原生隐藏option当可见元素等待而停止；已改为等待DOM挂载。第三轮完成全部9组检查，8次模型调用均成功。保留此诊断说明，不通过隐瞒历史失败宣称服务永不超时。

## 验证边界

本轮是本机浏览器自动检查，身份模式是独立示例的签名Cookie；Ubuntu/Keycloak/PostgreSQL与七库恢复沿用分别标注的v0.8.0证据，没有假称本轮重跑全部外部服务。未重新创建独立接包Agent，也未证明真人、物理多设备、目标服务器、生产负载或离线模型可用。

Hermes安装及Python环境、真实模型密钥不进入通用ZIP。删除不会远程擦除用户已导出的副本、WAL或历史离线备份；学校须另设备份保留政策。保留全部已有交付包、原数据库和用户数据。
