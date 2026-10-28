# M0 验收记录 · 2026-10-23

结论：**M0 三条指定链路通过，选型冻结为可继续开发的集成基线。** 这是同一主机上的 Ubuntu WSL 真实服务与独立浏览器自动验证，不是公网生产部署、校园真人试运营或物理多设备验收。

## 范围与证据

| 检查                                                                         | 结果                                  | 对应证据                                                                                  |
| ---------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------- |
| Keycloak 真实登录，Base 稳定用户，映射两种后端                               | PASS                                  | `integration.json`；浏览器授权码 PKCE 另见 `browser.json`                                 |
| 两校目录/场景/卡片/人物隔离，伪造票据和改签名拒绝                            | PASS                                  | `integration.json`                                                                        |
| 服务端存储人物配方、模型哈希；重试不多写；并发旧版本冲突、缺部件与旧目录拒绝 | PASS                                  | `integration.json`                                                                        |
| 人物实际预览、GLB 加载到原空间、第二浏览器上下文恢复                         | PASS                                  | `browser.json`；`avatar-editor.png`、`avatar-in-space.png`、`second-browser-restored.png` |
| OIDC 身份下 A2A 发现、留言任务、重复回执、跨用户任务拒绝                     | PASS                                  | `integration.json`                                                                        |
| 实际 NodeBB 待审、采纳发布、普通成员不能审核、待审不被他人读取               | PASS                                  | `integration.json`、`moderation-ranking.png`                                              |
| 源事件重复 10 次一次加分，规则版本可查，撤回一条冲正                         | PASS                                  | `integration.json`                                                                        |
| outbox 传输故障注入后保留待投递记录；从 PG 账本重建 Nakama 权威榜单          | PASS                                  | `integration.json`；客户端写分及私有存储越权均拒绝                                        |
| 撤销学校资格后，旧 Base JWT、Nakama 会话、NodeBB 会话均拒绝访问              | PASS                                  | `integration.json`                                                                        |
| 六个测试子服务重启前后，九张关键业务表行数和 SHA 一致                        | PASS                                  | `restart-before.json` 与 `restart-after.json`                                             |
| 业务库备份恢复到新的隔离数据库，九张表行数和 SHA 一致                        | PASS                                  | `backup-source.json` 与 `backup-restored.json`                                            |
| 原 Base 单元/A2A/pgvector等回归 13/13，空间构建与所有公开房间路径通过        | PASS                                  | 本次执行记录与 `base-regression.txt`                                                      |
| 原参考模式浏览器通行、换层、接待引用、刷新位置、返回入口，无 HTTP 或页面错误 | PASS                                  | `base-browser.json`                                                                       |
| 干净依赖目录，锁文件离线解析、811 个包安装、两校论坛/社交建库与构建          | PASS                                  | `installation.json`                                                                       |
| Base 与修补后的 NodeBB 生产依赖审计                                          | 0 项高风险、0 项严重，当前共 0 项公告 | `base-audit.json`、`nodebb-audit.json`；仅代表审计时点                                    |
| 50 次暖读取、5 并发，本机 P95 预算 500ms                                     | PASS，实际约 39.7ms                   | `metrics.json`；不外推生产并发或移动端帧率                                                |
| 既有 Base v0.2.1 完整包与图纸私有附加包                                      | SHA-256 不变                          | `protected-deliveries.json`                                                               |

## 本次解决的集成问题

- 原参考模式的公开读取权限不能直接用于校园私有部署。新增 `tenantBound` 校验，并保留参考模式原语义；跨校场景和卡片阴性用例通过。
- Nakama 的固定版本要求静态注册命名钩子；使用该版本实际支持的接口，未套用 master 声明中的新 API。
- WSL 的 Java IPv6 映射回环端口不能被 Windows 浏览器访问；加入 IPv4 配置后真实 PKCE 浏览器登录通过。
- NodeBB 上游锁定依赖存在安全公告；固定补丁版本并完成回归，未靠关闭审核或放宽断言通过。
- 论坛桥接插件原先是额外软链接，npm 安装会移除它。改为受锁文件管理的本地依赖；启动前检查必需插件，启动后核对真实原生拒绝结果。
- NodeBB 新人冷却期原先被桥接为通用错误。保留限流，映射成 429；自动测试准备阶段等待源服务既有冷却，不改变限流值。
- 原参考模式不应请求未启用的 M0 账号接口。通过目录能力字段控制人物扩展；原参考浏览器回归无 HTTP 错误。

## 本阶段没有证明的事项

- 任意时刻断电的跨服务原子性；NodeBB 原生发布与桥接事件持久化之间仍需 M1 增强对账。
- 六库、私有密钥、A2A 状态与其他外部服务的完整灾备，以及旧用户数据迁移。
- 账号找回、正式学校认证、组织/合作方角色全矩阵、私信/通知、背包、正式美术部件库、活动/奖励/商户业务。
- CharacterStudio 或 VRM 已集成：本次实际使用原创 glTF 编辑与导出方案。
- 独立新 Ubuntu 主机联网安装、生产 TLS/代理/服务账号与承载量。干净目录验证与同主机 WSL 不是第二台服务器验收。

继续开发的下一阶段是 M1，详细未完成清单见 `docs/M0.md`。本次结束在 M0，不恢复旧游戏开发。
