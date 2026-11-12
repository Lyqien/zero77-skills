# 生成的画风 Skill 结构

在不与现有目录冲突的新目录中创建：

```text
<style-slug>-png/
  SKILL.md
  references/
    style-profile.json
    shared-style.md
    negative.md
    router.md
    convert-subject.md
    subject-completeness.md
    output-delivery.md
    sources/                 原始风格图，实际可读文件
    subjects/                face/full_body/environment/object 的 PNG 与 .md 规则
    materials/               十六种材质的 PNG 与 .md 规则
    validation/
      report.json
      iterations/            两轮及以上的实际生成图片
      transfer-input.png
      transfer-output.png
      transfer-output.alpha.json
      transfer-output.subject-qa.json
  scripts/
    check_png.py
```

`SKILL.md` 从工厂的 `assets/generated-SKILL.md` 生成，替换名称占位符。`shared-style.md` 保存已验证的通用画风及其证据、`negative.md` 保存实际负面偏差；不要只写“参考上次对话”。从工厂复制转换流程、subject-completeness.md、output-delivery.md 和 Alpha 脚本，引用不得指向工厂。子 Skill 的入口与转换流程都必须读取单图交付规则，避免只在工厂写默认数量却没有传给子 Skill。路由按交付范围选择：默认完整人物读 full_body，即使上传图本来是半身；明确头像请求才读 face。所有主体规则和 prompt 不得残留“默认保留输入裁切”的旧规则。

`router.md` 将 face、full_body、environment、object 路由到实际文件，将 mixed 路由到实际涉及的类型；environment 在这里表示独立建筑或环境部件，默认不能把整幅风景当成透明素材。将材质名称路由到实际规则与图片，只读与上传主体相关的材质。无人物的物品不加载人物比例规则。

`style-profile.json` 保存实际数据，至少包括：

- `name`、`label`、`status`（`draft` 或 `validated`）、`macro_medium`。
- `source_images`：包内相对路径及源文件 SHA-256。
- `observed_traits`、`inferred_traits`：证据支持与推演内容分开。
- `supported_subjects`、`limitations`：适用范围，不能因生成了锚点就宣布所有主体都经过源图实证验证。
- `validation_report`：指向 `validation/report.json`。
- `output_contract`：PNG、实际 Alpha、默认移除背景与地面投影、保留主体内明暗与可辨识特征、默认 complete_subject、自动补全输入截断处、尊重用户明确的局部范围、默认 requested_output_count=1 和 delivered_image_count=1、首张合格即停止、内部检查预览不交付、不重复嵌入已展示成品。

`validation/report.json` 记录每轮 prompt、实际图片路径、各风格维度的证据和结果、真实材质锚点检查、端到端测试结果、输入截断位置、补全计划、推演部位、实际主体完整性检查、修复次数和 Alpha 报告。`subject_completeness_pass` 必须基于生成后逐部位读图检查。裁腿人物默认完整输出与明确头像范围这两种行为均须在新 Skill 的验证记录中交代；未执行不能沿用旧通过结论。转换 QA 还需记录初始候选是否通过、实际修复原因、所选最终文件和交付图数；不得把模型分析用预览与实际成品混算，也不能把截图中的人数当成输出图片数。未执行项用 `not_run`，无证据项用 `unknown`。`validated` 要求默认蒸馏测试与端到端测试均完成并通过；不得用空记录、占位路径或人工预填分数替代验证。

草稿只保存真实存在的文件与已完成记录，不创建假 PNG 或伪造成功报告。交付前逐一解析包内链接、打开图像，检查没有遗漏占位符或绝对机器路径；对外回复的文件链接按宿主要求使用实际路径。
