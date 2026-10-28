# M2优先交付验收 · v0.4.0

## 前提与边界

仅使用独立的虚拟学校实例，设置 HD_M0_CONFIG、HD_M1_TEST_FIXTURE=1，拥有自己的 QA Chrome 路径。本轮环境是同一主机上的 Ubuntu WSL + Windows Chrome；两个干净浏览器会话不等于物理多设备，自动操作不是真人验收。不会对用户库造数据。旧交付包和旧服务实例保留。

## 不超过20分钟的操作卡

| 时间 | 操作 | 必须看到的结果 |
|---|---|---|
| 0–4分钟 | 登录两校账号，尝试越权；逐项换部件、配色和身高，预览站立/行走/挥手 | 24项原创部件可选择；不兼容搭配明确拒绝，未知版本/外部URL拒绝；不能跨学校/账号 |
| 4–7分钟 | 确认旧配方迁移、保存、重复请求、并发保存，再由第二个干净浏览器登录 | 原表保留，新历史存在；同请求仅一次；过时版本冲突；恢复相同配方与模型SHA-256 |
| 7–12分钟 | 欢迎包领取、装备、远程集章失败、真实寻路抵达后集章/明信片/记忆卡/挥手 | 数量服务端确认；仅一次欢迎包；重复集章不增量；每次明信片1张纸，重放不再扣；私人记忆未公开；不改几何/他人 |
| 12–15分钟 | 私人收藏、名片可见范围；记忆带到论坛编辑器 | 他人无法读取收藏；private字段不返回；论坛正文仅预填，必须主动提交审核；不自动计分/入知识库 |
| 15–20分钟 | 看完整备份摘要、启动独立恢复实例，登录后读取人物/背包/旧消息并重放旧道具请求 | 六库逐表摘要一致；模型与数量恢复；旧回执不再消耗；原M1私信仍可读且版主不能直读；新写入只在克隆 |

服务安装、受控备份与二进制绑定可提前准备；首次目标服务器安装尚未执行时，不能据此称目标部署验收完成，不另加一小时长测。

## 复做命令

```bash
export HD_M0_CONFIG=/srv/isolated-m2/private/config.json
export HD_M1_TEST_FIXTURE=1
npm run doctor
npm run build
npm test
npm run verify
node tests/m2-live.mjs
node tests/m2-negative.mjs
export HD_QA_CHROME=/opt/owned-qa/chrome
node tests/m2-browser.mjs
# 完整停止/启动该实例后，保留上一步的 qa/m2/browser.json：
node tests/m2-persistence.mjs
# 按docs/M1.md完整备份/恢复到新命名空间，逐表比对后：
export HD_M1_SOURCE_CONFIG=/srv/isolated-m2/private/config.json
export HD_M0_CONFIG=/srv/isolated-m2-clone/private/config.json
node tests/m2-restore.mjs
```

这些脚本会向虚拟账号发放道具、记录使用事件或修改存档；不能对实际学校库运行。重复演示需要由负责人通过审计发放材料或创建新的隔离实例，不重置用户背包、不降低数量/权限断言。测试之间顺序执行，避免共用角色状态冲突。

## 证据含义

- core-regression.json：18项测试，含原13项A2A/持久化/公开知识契约与5项新人物库检查。
- live.json：6组真实 Keycloak/PostgreSQL/原生服务集成链路。
- browser.json、avatar-studio.png、scene-backpack.png、mobile.png：4组独立浏览器自动验证，含VRM加载、第二会话恢复、场景道具与论坛草稿。
- negative.json：跨操作同requestId竞争、伪造位置和跨场景拒绝。
- restart.json：整套服务实际停止/启动后新登录恢复同一模型与背包收藏。
- backup-source/restored/comparison.json：六库199表、5026行逐表摘要一致，仅规范化显式变更的issuer；无原始账号凭据或私有正文。
- restore-live.json：独立恢复实例读取相同人物、背包、收藏、旧回执及M1原生消息；克隆的新写入不改变源库。
- foundation.json：8组既有M1账号/组织/审核/对账/A2A回归。
- protected-deliveries.json：既有封存包保持原SHA-256。

截图内的学校、人物与私有记忆文字都是本轮虚拟测试数据。初次浏览器测试曾因未等待装备响应而断言过早，改为等待实际装备状态后通过；没有放宽业务断言、发帖限制或到达条件。差异审查还统一了道具与其他操作的回执锁，防止同ID跨操作竞争变成数据库唯一键错误。

本轮完成用户指定的人物/存档/背包/轻道具优先范围。基础学校名片已接通；正式身份徽章、作品集、多人同步人物/表情、任意外部VRM导入、柔性衣物模拟和Agent长期记忆没有宣称完成。M3/M4运营与合作方业务保持后续阶段。
