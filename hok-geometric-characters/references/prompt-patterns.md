# 提示词模式

按原图填写人物内容，不依赖对话记忆。固定风格要求与角色信息分开，以便局部调整。

## 基础生成

```text
Use case: stylized-concept.
Input 1 official hero image: identity, costume, props, original hue families and gesture ONLY.
Inputs 2 and 3 First-Refer sheets: primary angular geometric flat illustration language.
Inputs 4 and 5 approved Zhuang Zhou I and Xiao Qiao L: accepted compact chibi anatomy, plane density and soft color treatment. Borrow style ONLY, not character design or props.
Input 6 Erin: authoritative reference for FLAT GRAPHIC EYES ONLY. For eye rendering it overrides glossy eyes in all other references. Do not copy Erin's purple eye color, hair or costume to another hero.
Output unit: [one hero / matched male-female variants together / human controller and puppet together].
Subject and identifying features: [hero-specific details].
Pose: [readable short-limb adaptation of the source action]. Preserve the action's character; do not automatically replace dynamic poses with neutral standing.
Big head, small short torso, short limbs and minimal neck. Angular silhouette, broad matte flat color shapes with deliberate structural polygon planes. Keep the detail level of the approved samples, not fine triangular noise and not overly smooth round anime art. Simplify repeated feathers, locks and ornaments into groups. Face simpler than costume.
Eyes are matte flat graphic shapes matching input 6: simple upper eye edge and iris built from two or three broad SOLID color shapes with hard boundaries. Preserve the hero's eye hue and intended expression. No white catchlight dots, sparkle, glossy corneal reflection, wet shine, spherical eyeball modeling, continuous iris gradients, detailed iris texture or concentric pupil rings. Avoid separately modeled realistic black pupils. Do not substitute smaller glossy anime eyes for flat eyes. Closed and winking eyes remain simple solid graphic strokes; do not force them open.
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

眼睛跑偏：Eye-rendering correction ONLY. Preserve the existing eye outline, gaze, eye hue, wink or closed-eye expression, face, anatomy, pose, costume, palette, background effects and composition. Replace glossy iris shading with two or three broad solid flat color shapes matching the Erin reference. Remove white catchlight dots, corneal reflections, sparkle, continuous iris gradients, ring textures and realistic separate black pupils. Keep eyes expressive through shape and simple graphic eyelid, not shine. Do not shrink the eyes or change the character to imitate Erin's identity.

颜色偏鲜：slightly lower saturation in [specific accents], preserve hue, brightness, value separation and all geometry. Keep colors recognizable, never washed gray. Percentages are visual guidance, not a deterministic measurement.

切面过碎：merge minor internal triangles into fewer broad directional planes, preserving the current silhouette, pose, palette and identity. Do not erase all faceting or turn hair into smooth rounded shapes.

动作别扭：identify the exact wrist, knee, foot direction or prop contact that needs correction, retain the existing dynamic gesture and short anatomy. Do not redesign the entire pose unless the user asks.

已认可图只需规格检查时：不调用图像生成重画，不重新着色、不抠图、不移除光雾。检查尺寸、比例、模式、文件名与版本。
