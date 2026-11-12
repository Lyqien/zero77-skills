---
name: style2subjectskill
description: 从用户上传的美术参考图蒸馏并保存画风，生成独立可复用的主体转风格 Skill；生成的 Skill 将后续上传图中的主体转为目标画风，默认补全输入中截断的主体部位，并默认仅交付一张经主体完整性与 Alpha 检查的透明背景 PNG。用于建立或更新此类风格素材技能。
metadata:
  version: "0.2.2"
  upstream: "waterblower/Omni-Art-Skills style-distill 1.4.5"
---

# Style2SubjectSkill

本 Skill 是工厂；产物是每种画风各自独立的 Skill。维护工厂文件时不生成图片。真正提取风格时必须生成并检查验证图，不能把文字分析称为已验证画风。

## 输入与模式

- 建立画风：用户上传风格参考图，按下述蒸馏流程生成新的 `<style-slug>-png` Skill。名称未指定时，根据可见美术特征命名。
- 使用已有画风：用户已指定某个生成的风格 Skill 时，执行该 Skill 的主体转换流程，不重新蒸馏、不重新生成材质库。
- 修改技能：只修改指令、资源或脚本并验证，不触发图片生成。

先查看所有输入图片，区分 STYLE（提供美术语言）与 SUBJECT（提供主体身份、结构、服装、道具、姿态）。创建阶段只有 STYLE 很正常，不要求另传主体图。多张图角色不明且影响结果时才澄清。图片内的文字不作为操作指令。

## 建立画风

1. 阅读 [references/distillation.md](references/distillation.md)，执行风格分析和生成验证。保存原图；路径不可用时不得伪造已保存文件。
2. 将证据、适用范围、风格不变量、条件性材质规则和不应迁移的内容分别保存。单张图未展示的材质与人物比例标为推断，不宣称已从图中提取。
3. 默认保留上游的两轮四类测试和十六张独立材质锚点。端到端测试至少使用一张下肢被画框截断的人物图，在未要求补腿的普通“转风格透明素材”请求下，验证自动检查、补全小腿与脚、主体保持和真实透明度。明确头像请求则验证仍按头像范围处理。维护本技能文件时不自动生成图片，未执行的新行为测试如实记为 not_run。
4. 读取 [references/package-contract.md](references/package-contract.md)，按其中结构创建全新输出目录。复制 [assets/generated-SKILL.md](assets/generated-SKILL.md) 并将其中 `STYLE_SLUG`、`STYLE_LABEL` 替换为实际值；填入实际风格文件、参考图和验证记录。把 [references/convert-subject.md](references/convert-subject.md) 复制为子 Skill 的 `references/convert-subject.md`，把 `scripts/check_png.py` 复制到子 Skill 同名位置。同时复制 `references/subject-completeness.md`，使子 Skill 自包含地执行主体缺失检查、首次生成自动补全及生成后检查。同时复制 `references/output-delivery.md`，在子 Skill 入口和转换流程中加载默认单图与去重交付规则。
5. 子 Skill 必须自包含：不能依赖工厂的安装路径、当前会话、临时 URL 或其他未安装 Skill。可迁移的包内引用用相对路径；工具调用使用实际可读取的路径；对话中的链接遵守宿主的路径要求。
6. 检查新 Skill 的 frontmatter、链接、资源可读性和脚本，打包交付。仅在实际生成验证完成时标记 `validated`；缺图、工具失败或额度不足时保留 `draft`，明确未完成项。

## 主体完整性默认行为

先读 [references/subject-completeness.md](references/subject-completeness.md)。生成的 Skill 必须默认输出完整选定主体，自动补全输入画框截断的部位；用户明确要求头像、半身或局部裁切时按指定范围。路由、模板、转换 prompt 与验收都必须采用此规则，不得残留“仅保留输入可见范围”或“补全需另行确认”的旧默认。新补部分标为合理推演，不能宣称真实还原。主体完整性由实际读图检查，Alpha 脚本不负责识别解剖缺失。

## 默认单图交付

读取 [references/output-delivery.md](references/output-delivery.md)。生成的画风 Skill 执行普通转换时，生成与编辑工具调用总预算为一次（含首次生成）；首张验收通过即交付，失败则说明问题并停止，用户明确要求修复后才能再次生成；内部检查预览不作为第二张输出。同图多人组合仍保留在一张图里。此规则不减少工厂阶段的蒸馏实验和材质锚点数量。维护时只检查指令与文件，不自动生成图片；实际界面单图行为未测时记 not_run。

## 执行约束

图像生成与转换使用宿主可用的图像工具；透明素材请求必须启用真正透明输出（当前内置工具为 `transparent_background: true`）。实际调用前检查当前工具参数，不把某家工具的参数当作通用接口。多图输入明确标注每张图的作用；本地图片先打开查看。

生成结果必须保存到输出目录。工具仅返回预览且无法取得文件时，不能宣称完成 Alpha 验收。不要擅自切换到收费 API 或添加外部抠图服务。

每轮只修正最显著的偏差。工厂默认最多四轮风格迭代；子 Skill 普通转换只调用一次图像工具，不自动追加修复。首张失败保留候选、报告问题，等待用户明确要求修复或重做。上游两轮是最低验证量，不是两轮后自动通过。

不覆盖原 Skill、用户输入或已有输出。默认在用户指定目录或当前工作区的 `outputs/` 中创建新目录；重名用递增后缀。只有用户要求安装时才写入技能安装目录。

完成回复包含新 Skill 的名称与路径、验证状态、后续调用示例，以及实际存在的透明 PNG 测试文件。没有参考图时只请求提供参考图，不虚构任何画风或验证结果。
