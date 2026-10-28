# M1 通信验收 · v0.3.0

## 运行前提

只在全新的虚拟学校测试命名空间运行。设置 `HD_M0_CONFIG` 为该实例私有配置，`HD_M1_TEST_FIXTURE=1`。测试依赖真实 PostgreSQL、Keycloak、NodeBB 和 Nakama；浏览器使用独立 QA Chrome，不读取用户浏览器配置。原 M1 的交付包与数据不得覆盖。

## 不超过20分钟的验收卡

| 时段      | 操作                                                        | 通过标准                                                                              |
| --------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0–3分钟   | 两校账号登录、组织权限与现有令牌撤权                        | 不跨校/组织；最后负责人保护、交接和审计有效                                           |
| 3–7分钟   | 两位虚拟账号发送私信、断线重连、编辑/撤回、已读、屏蔽和举报 | 一次写入；改输入/旧版本冲突；第三人和普通版主不能直读；明确举报的单条审查有理由与审计 |
| 7–10分钟  | 学校/组织实时讨论，已打开流期间撤权                         | 事件流重新鉴权、停止交付；原生 storage/RPC/频道无旁路                                 |
| 10–14分钟 | NodeBB 主题/回复修订、审核、撤回及故障恢复                  | 审核前旧正文不变，审核后保留 pid/tid；修订不增分；撤回按源记录冲正；丢响应不重复发布  |
| 14–17分钟 | 到期预览/处理、保留锁、公开知识回归                         | 过期正文不再展示，锁定证据保留；聊天不进公开知识库；原 A2A 与接待契约不退化           |
| 17–20分钟 | 检查六库备份恢复报告、启动恢复实例、旧消息读取及新消息发送  | 表摘要一致，稳定 ID 保留；权限仍生效，新写入只在恢复实例                              |

完整备份必须停写，备份/恢复工具与固定版本服务安装可以提前准备。若目标服务器首次安装尚未就绪，不把安装等待或未执行的恢复算作这张20分钟卡已通过；不另外启动一小时长测。

## 可复做命令

```bash
export HD_M0_CONFIG=/srv/hd-fixture/private/config.json
export HD_M1_TEST_FIXTURE=1
node tests/m1-live.mjs
node tests/m1-permission-regression.mjs
node tests/m1-social.mjs
node tests/m1-social-governance.mjs
# 独立 QA Chrome 路径；在 Windows 运行时使用自己的 Windows Chrome 绝对路径
export HD_QA_CHROME=/opt/owned-qa/chrome
node tests/m1-social-browser.mjs
node tools/m1-status.mjs
npm run doctor
npm run build
npm test
npm run verify
```

顺序执行共享账号的测试，避免彼此撤权/改写同一虚拟记录。NodeBB 原生新账号与发帖间隔仍生效；测试查询实际等待时间，不清掉限流、不自动重复投稿。测试会创建虚拟组织、消息、帖子、举报和角色记录，不能对实际用户库运行。

恢复验证先按 docs/M1.md 建立独立备份/恢复实例，使用 `m1-snapshot.mjs` 比对停止写入时的六库表摘要。恢复环境另设 `HD_M1_SOURCE_CONFIG` 指向原测试实例只读对照配置，再运行 `tests/m1-social-restore.mjs`。私有快照、凭据、原始消息正文不能放入公开源码包。

## 本轮证据的含义

- integration.json：5组通信与编辑链路。
- governance.json：4组到期、源提交/回执恢复、编辑丢响应、原生回复与父主题撤回隔离。
- browser.json、chat.png、editor.png：3组独立浏览器自动验收及截图。
- foundation.json：原 M1 的8组账号、组织、撤权、A2A、账本与 outbox 回归。
- permission-regression.json：现有成员邀请保护及当前 IdP 邮箱回归。
- migration.json：事务迁移、原 JSON 保留、PG 持久化与单写者检查。
- backup-source.json、backup-restored.json、backup-comparison.json：六库192表、4924行逐表摘要一致，只规范化明确迁移的 issuer。
- restore-live.json：恢复后实际登录、旧私信、权限及独立新写入。
- core-regression.json、spatial.json：13项既有核心测试与两套示例通行检查。
- protected-deliveries.json：旧交付文件哈希；credentials-exclusion.json：公开变更未含私有生成凭据。

这些证据属于同机 WSL Ubuntu + QA Chrome 的自动验证，不是实际学校用户、物理多设备、真实 SMTP、公网生产或承载验收。历史 M1 证据在 evidence/m1 中保留，并不覆盖成新的测试日期。
