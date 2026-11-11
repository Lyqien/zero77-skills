# 主体完整性与自动补全

在图像生成前和每次生成后都读本文件。完整性是视觉与语义检查，Alpha 脚本只能检查透明结构，不能判断是否缺腿、缺脚或缺少物品部件。

## 先确定交付范围

- 用户未指定局部范围、只是要求“转画风 / 透明素材”时，默认输出完整的选定主体。人物默认完整全身，动物包含完整身体与尾翼等适用部位，物品包含完整功能结构。
- 用户明确要求头像、胸像、半身、局部特写或保持裁切范围时，按指定范围输出；不能把有意的局部构图误判成缺失，也不自动扩展为全身。
- 先确定输入中选定主体的类别与数量。不因为看到两条腿便为蛇、轮椅、义肢或特殊设计主体添加“标准人体”部件。保留角色固有的生理或机械结构。

## 生成前检查与补全计划

打开 SUBJECT，逐区查看头顶/头饰、躯干、左右手臂和手、骨盆、腿、膝、踝、脚/鞋，以及实际涉及的尾巴、翅膀、道具和服饰末端。分别判断：完整可见、自然遮挡、在输入边缘被截断、疑似缺失、无法判断。不把自然遮挡自动等同于截肢，不为显示隐藏部位破坏原姿态或服装。

完整主体模式下，对明确截断的部位自动制定补全计划并执行，不再要求用户额外说“补腿”或重复确认。补全被画框裁掉的小腿和脚、衣摆与发梢等，沿已有关节方向和衣物结构自然延续；适当扩大画布并缩小主体占画面比例，而不是拉伸、贴边或只在截断处加一个封口。

保持已观察到的身份特征、上身姿态、朝向、配色、衣服、配件与主体数量。未展示部位按现有服装和目标风格做最少必要推演，选择简单一致的腿部与鞋履，不擅加武器、花纹、装饰或额外肢体。推演不是原始设计的真实还原，交付时简短注明补全了哪些部位。

输入被其他物体遮挡时，保持有依据的遮挡关系；移除背景后，对必须露出的主体轮廓合理补全。若服装或自身姿势仍自然遮住某些关节，只检查结构连续与遮挡合理，不强迫每个关节外露。

人物有裁切而默认要求完整素材时，路由到 full_body 加实际材质，不能因为上传图是半身就选 face 并沿用头像裁切。明确头像请求才走 face。

把下列实际决策写入生成 prompt，而非只写“完整主体”：

```text
OUTPUT_SCOPE: complete_subject, unless the user explicitly requested a crop.
OBSERVED_SUBJECT: identity, visible pose, colors, clothing, parts and count.
INPUT_CROP: the actual edges and parts cut off in the uploaded image.
COMPLETION_PLAN: enumerate each truncated part to reconstruct, its joint
continuation, pose, clothing coverage and simplest consistent inferred design.
Extend the canvas and reframe the subject. Do not copy the input crop.
Show the whole intended subject including completed limbs and terminal parts,
with transparent padding beyond the head, hands, feet and other extremities.
For people: continue each applicable leg through a plausible knee and ankle
to a complete foot/shoe; maintain connected anatomy and target-style proportions.
Preserve natural occlusions, actual body differences and the selected pose.
No stumps, floating shoes, extra limbs, duplicate feet, dislocated joints or
invented accessories. Inferred regions must match the same style and lighting.
```

## 生成后检查与自动修复

打开实际生成文件，并与输入和补全计划对比。不能只看工具成功状态或生成 prompt。完整模式逐项检查：

1. 选定主体数量和身份特征仍然一致。
2. 输入截断处已经延续成合理结构，而非把截断边缘平移到透明画布中央。人物即使距边缘很远，若仍在大腿处平切，仍判失败。
3. 每条适用肢体连接合理，腿/足与姿态和服饰一致；没有多手、多脚、断关节、悬浮鞋或复制部件。自然遮挡有明确解释。
4. 头饰、发梢、手指、衣摆、脚底等可见轮廓完整，并位于透明留边内。
5. 新补部位与原有主体在比例、切面/线条、材质、明暗和细节频率上统一。

发现缺失、截断或错误补全时自动调用图像编辑工具扩图或修复；将原始 SUBJECT、当前候选及 STYLE 的角色标清，保留已正确的身份与部位，针对失败位置修复。默认每次转换最多两次修正（完整性、风格与透明修复共用此上限）。每次修复后重新做完整性、风格、主体保持和 Alpha/黑白底检查。

修正到限仍失败时标为未完成，报告具体缺失部位，不把截断素材当作最终成品。不能用 Alpha 有透明边框来抵消主体不完整。

## 留存真实检查结果

每次转换保存 `<output-stem>.subject-qa.json`，至少包含 `output_scope`、`input_crop_findings`、`completion_plan`、`inferred_parts`、`output_image`、逐部位 `checks`（状态和可见证据）、`subject_completeness_pass`、`identity_preservation_pass`、`style_match_pass`、`alpha_report`、`repair_attempts` 和 `overall_pass`。范围外或自然遮挡部位记录 `not_applicable` / `naturally_occluded` 与理由；未查看记为 `not_checked`，不能预填通过。

只有实际完成的范围内完整性、身份、风格、透明结构和黑白底视觉检查均通过，`overall_pass` 才可为 true。JSON 是已执行视觉检查的记录，不是自动识别器，也不能替代打开图片。
