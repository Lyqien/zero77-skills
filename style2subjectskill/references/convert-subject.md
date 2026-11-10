# 上传主体图 → 目标风格透明 PNG

## 识别输入

打开 SUBJECT 与本 Skill 保存的 STYLE 参考图。SUBJECT 只提供要转换的主体，STYLE 只提供美术处理。不要把 STYLE 的人物、配饰、服装或背景移植进来，也不要把 SUBJECT 原有画风当作目标画风。

有多个主体且用户未选定时，画面存在明确主角则默认主角；存在多个同等主角才澄清。完整群组是用户指定主体时保留其相对关系。背景内可独立使用的建筑、植物也可作为主体提取；无法确定主体的整幅风景需先明确保留对象。

记录主体锁定项：类别、身份特征、辨识色、服装与道具种类、数量、朝向、姿态及部件关系。按目标风格调整比例、线条、明暗和纹理；不随意更换身份、产品型号或配件。不保证生物识别意义的身份一致，应逐项视觉检查。

默认保留输入可见范围，不能声称还原被遮挡部分。需要补全到全身或完整物件时，仅在用户提出或确认后进行；如输入本来完整，则确保边缘不裁切。画布保留合理透明留边，不贴边或人为改变长宽。

## 读取与生成

读取 `shared-style.md`、`negative.md`、`router.md`，再读实际涉及的主体与材质文件，避免全量加载。使用原始 STYLE 加已通过的相应类型锚点，减少生成图反复作为唯一参照造成的漂移。

向图像工具明确各输入的角色，提交类似如下的分层要求，并填入实际风格规则：

```text
Task: style-transfer of the SUBJECT, delivered as one reusable cutout asset.
Inputs: enumerate each actual input image and label SUBJECT or STYLE.
SUBJECT invariants: identity cues, category, count, pose, orientation,
costume/parts, defining colors and relationships recorded from the upload.
STYLE: the saved style invariants plus the relevant subject/material rules.
Change the visual rendering according to STYLE; retain SUBJECT invariants.
Composition: preserve the visible framing, keep the complete visible silhouette
inside the canvas with clear transparent padding.
Output: actual transparent background, PNG with alpha. Preserve intentional
holes between limbs, handles and accessories. Retain fine silhouette details.
No backdrop, ground plane, frame, watermark, added label or painted checkerboard.
No ground shadow unless specifically requested; retain shading on the subject.
```

启用工具的真实透明参数。当前内置工具使用 `transparent_background: true`；所有输入有本地路径时用 `referenced_image_paths`；若有无本地路径的会话图片，用覆盖全部目标的最小 `num_last_images_to_include`（最多 5），两种方式不可同时传。无法覆盖全部输入时请用户重传缺失图。实际工具接口变化时以当前 schema 为准。不同工具不共享这些参数名。

没有适用图像工具或透明能力时明确说明缺项，不把文字 prompt 当图片交付，不擅自改用 API。文件应保存到用户要求位置或工作区输出目录，保留原件。

## 文件与视觉双重验收

对实际输出文件运行（需要 Python 3 与 Pillow）：

```text
python scripts/check_png.py path/to/result.png --report path/to/result.alpha.json
```

脚本以 PNG 文件签名、实际解码格式、原始 Alpha 能力、透明/可见像素及透明边框为依据；不修改图像。`RGBA` 且全部 Alpha=255 仍失败，全透明空文件同样失败。索引色 PNG 的 tRNS 透明信息也可正常验收。

脚本通过只说明基本透明结构合格。还必须查看原图以及黑、白背景上的临时合成预览：是否仍有被画进图里的棋盘格、残余背景块、白边/黑边、杂散像素；发丝和细部是否被吞；应镂空的位置是否通透；主体内部是否意外变透明；玻璃、薄纱、辉光是否保留合理半透明。临时合成预览只用于检查，不作为透明 PNG 交付。

风格匹配和主体锁定项也要逐项检查。若工具生成了假透明或错误边缘，使用图像编辑工具针对问题重试，不用“删除全部白色像素”来抠图，不用格式转换把不透明 RGB 假装成合格 RGBA。实际修复必须重新验收。

默认最多两次有针对性的修正。仍失败则报告问题和未完成状态，不把失败图标为最终素材。交付真实 PNG 文件与简短验证结论；链接指向文件本身，不能仅交付棋盘格预览截图。
