# v0.7.1 完整实际材料的前后端验证

状态：PASS。仅限本轮材料补全的工程范围；旧交付、数据库和历史证据保留。

## 本轮新增证据

- `source-fidelity.json`：独立只读核对来源。82 条非空渠道记录、432 条年历情境、9 年级、20 引用、38 条背景口径、324 条逐项评级条件及 6 类分支均保留，未执行 HTML。
- `full-materials-tests.json`：两份完整实际转换稿在回环地址的虚构组织测试。真实 PostgreSQL/OIDC 后端全量预览、不可覆盖导入、启用和精确读回；表格稿通过浏览器文件上传、预览、导入和启用。
- 浏览器遍历 18 页，432 个条目全部可达且每页最多 24 卡片；跨页选择产生分工，公开指南和合作服务路由可用。测试日期由负责人另行确认后只创建一条活动草稿，贡献值无增加。
- 普通成员筛选、学生/可选家庭需求独立展示、客观事件不评级、本人选择等级、刷新恢复、完成解除评级与管理员代查拒绝通过。390px 界面无横向溢出，专用 Chrome 无 pageerror；实际材料截图在私有附包，已查看。
- `tests/annual-conversion.test.mjs` 用原创小型源文件验证转换不执行脚本、不补造空白、拒绝覆盖、支持新版本；来源核对会拒绝缺失的逐项评级条件。根单元套件 41 项通过。

## 复做

使用 Python 标准库运行 `tools/prepare-annual-materials.py`，再用 `tools/annual-validate.mjs` 和独立的 `tools/verify-annual-materials.py` 校验。实际材料完整流程入口为 `tests/annual-materials-live-browser.mjs`；需要专用隔离服务配置、虚构账号、`HD_M1_TEST_FIXTURE=1`、`HD_ACTUAL_MATERIALS_TEST=1`、`HD_MATERIALS_DIR` 和 `HD_QA_CHROME`。具体环境变量在脚本开头，切勿指向真实学校。

此前七组年度 API、七库停写恢复、合作业务 A2A、索引与撤权、Ubuntu 编排证据分别保留在 `evidence/annual` 和 `evidence/integrations`。本补丁不修改后端、SQL 或原数据库，仅调整转换、界面、验证工具与文档。v0.7.0 的结构和原创小样证据不能代替本次实际全量材料流程。

## 边界与资源

真实校历、学校批准、实际学生运营、目标服务器、正式 SMTP、真实商家履约和物理多设备没有在本机验证。未新增 P2、重型捏脸或个人模型长期记忆；ABC 不进入贡献排名。没有复用旧 v0.5 独立 Agent 接包结果作为本版证据。

原件只读、私有转换稿不进入通用源码或镜像。测试完成已关闭本轮专属浏览器、应用及容器，并停止 Docker/socket/containerd 后台；停止后的隔离卷和备份保留。新 ZIP 解压启动结果与摘要由交付目录另外记录。
