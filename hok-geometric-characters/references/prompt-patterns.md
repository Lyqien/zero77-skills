# 提示词模式

按原图填写人物内容，不依赖对话记忆。固定风格要求与角色信息分开，以便局部调整。

## 基础生成

```text
Use case: stylized-concept.
Input 1 official hero image: identity, costume, props, original hue families and gesture ONLY.
Inputs 2 and 3 First-Refer sheets: primary angular geometric flat illustration language.
Inputs 4 and 5 approved Zhuang Zhou I and Xiao Qiao L: accepted compact chibi anatomy, plane density and soft color treatment. Borrow style ONLY, not character design or props.
Input 6 Erin and input 5 Xiao Qiao L: eye-plane references, supported by the bundled Daji example. Match their few BROAD flat color patches. NO added distinct pupil or anatomical iris/pupil segmentation. This does NOT mean one uniform eye-color fill. Preserve hero-specific eye hue.
Output unit: [one hero / matched male-female variants together / human controller and puppet together].
Subject and identifying features: [hero-specific details].
Pose: [readable short-limb adaptation of the source action]. Preserve the action's character; do not automatically replace dynamic poses with neutral standing.
Big head, small short torso, short limbs and minimal neck. Angular silhouette, broad matte flat color shapes with deliberate structural polygon planes. Keep the detail level of the approved samples, not fine triangular noise and not overly smooth round anime art. Simplify repeated feathers, locks and ornaments into groups. Face simpler than costume.
Eyes use a few BROAD flat geometric color planes like the Xiao Qiao L, Erin and Daji examples: darker upper areas and lighter lower or diagonal patches with clear boundaries. Do not reduce eyes to a single uniform fill. Do not add a separate pupil, central dot, slit or concentric ring, and do not arrange patches radially around an implied pupil. A broad dark plane is a graphic shape, not a reason to invent pupil anatomy. Preserve eye whites, simple upper eyelid, hero-specific color and expression. No tiny iris mosaic, optical texture, continuous gradient, white catchlights, wet shine or glass reflections. Closed or winking eyes remain as intended.
Palette: [hero-specific colors], gentle moderate saturation, neither neon nor washed gray. Preserve character-specific warm/cool differences.
Soft localized aura comparable to approved samples is acceptable, without strengthening it into dominant atmospheric effects. No scene background, base, text or watermark.
Entire figure and all major props in frame with comfortable margins. Target landscape 1536x1024, 3:2 PNG with transparent surroundings; preserve native alpha.
```

使用内置图像生成工具的透明背景选项。不要把白底中间图和抠图添加为默认流程。工具实际尺寸仍须检查，提示词中的数字不保证精确执行。

默认只保存最终 PNG。工具完成后在聊天中简述必要信息，不自动向输出目录写说明 Markdown、TXT、JSON、提示词或生成记录。只有用户明确要求时才另存报告。此规则约束交付行为，不需要画到图片上。

## 关系片段

- 元流之子：two distinct gender designs of ONE hero together, male left female right, equal apparent height hair-crown to soles, soles same baseline and comparable head scale. If necessary scale the whole female uniformly rather than lengthening her legs.
- 云中君：ONLY left silver-haired male and his wings, exclude pink-haired woman, antlers, animal ears and staff.
- 瑶：ONLY right pink-haired female with antlers, animal ears, cape and staff, exclude male and bird wings.
- 元歌：TWO distinct figures in ONE hero-unit image; short-gray-haired blue/teal human controller, long-white-haired purple/white articulated puppet, a few control strings visibly connecting them. Never fuse bodies or swap roles.

## 单项修改

眼睛跑偏：Eye-rendering correction ONLY. Preserve eye outline, gaze, hue, expression and every non-eye part. Match the few broad flat dark/light patches in the approved Xiao Qiao L, Erin and Daji references. Keep broad upper, lower or diagonal planes rather than one uniform fill. Do not add an independent pupil or radial/concentric anatomical segmentation. No tiny central inset, optical texture, continuous gradient or bright reflection dots. Do not shrink eyes, alter the face or restyle the whole image.

颜色偏鲜：slightly lower saturation in [specific accents], preserve hue, brightness, value separation and all geometry. Keep colors recognizable, never washed gray. Percentages are visual guidance, not a deterministic measurement.

切面过碎：merge minor internal triangles into fewer broad directional planes, preserving the current silhouette, pose, palette and identity. Do not erase all faceting or turn hair into smooth rounded shapes.

动作别扭：identify the exact wrist, knee, foot direction or prop contact that needs correction, retain the existing dynamic gesture and short anatomy. Do not redesign the entire pose unless the user asks.

已认可图只需规格检查时：不调用图像生成重画，不重新着色、不抠图、不移除光雾。检查尺寸、比例、模式、文件名与版本。
