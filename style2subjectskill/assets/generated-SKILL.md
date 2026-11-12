---
name: STYLE_SLUG-png
description: 将用户上传图片中的主体转换为STYLE_LABEL画风，保留主体身份与关键特征，默认自动补全截断部位，默认只输出一张经完整性、Alpha 与视觉检查的透明背景 PNG 素材。用户调用此画风或要求按此画风转换主体图时使用。
---

# STYLE_LABEL透明素材

先读取 `references/style-profile.json`。仅当状态为 `validated` 且相关主体在适用范围内时，使用已验证声明；草稿必须说明尚未完成的验证。

执行 [references/convert-subject.md](references/convert-subject.md)。读取 `references/router.md` 路由到实际所需的主体、材质规则与参考图；将上传图绑定为 SUBJECT，将本 Skill 保存的原始风格图与适用锚点绑定为 STYLE。

先读取 [references/output-delivery.md](references/output-delivery.md)。默认生成/编辑工具总共只调用一次，首张通过即交付。首张未通过则如实说明失败并停止，不自动再生成；只有用户明确要求修复或重做才继续。不额外交付缩小版、规格版、黑白底检查图或重复预览。工具已展示同一成品时不再次嵌入图片。同图主体组合保持完整，不拆图。

默认直接转换上传主体，不重新提取风格。保持身份、结构、数量、姿态、服装/部件和辨识特征，按画风规则调整渲染与比例。未上传主体图时请求提供图片；不要把本 Skill 的风格参考图误用为待转换主体。

先读取 [references/subject-completeness.md](references/subject-completeness.md)。普通转风格素材请求默认完整主体：生成前识别裁切，自动补全截断肢体与部件，并扩展画布；明确头像、半身、局部请求则按指定范围。生成后读图逐部位检查，失败则说明问题并停止，记录推演部位与 `<output-stem>.subject-qa.json`。不能将有透明留边但仍缺腿的图判为通过。

必须请求实际透明背景，保存 PNG，并运行 `scripts/check_png.py`，再完成黑白背景视觉检查、风格匹配和主体保持检查。主体完整性也必须通过后才交付为最终素材。无法获取实际文件时报告未完成验证，不能仅凭工具预览宣称透明。

本 Skill 自包含；引用均相对此目录，不依赖创建它的工厂或原会话。
