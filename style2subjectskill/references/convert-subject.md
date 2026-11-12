# 上传主体图 → 目标风格透明 PNG

## 识别输入

打开 SUBJECT 与本 Skill 保存的 STYLE 参考图。SUBJECT 只提供要转换的主体，STYLE 只提供美术处理。不要把 STYLE 的人物、配饰、服装或背景移植进来，也不要把 SUBJECT 原有画风当作目标画风。

有多个主体且用户未选定时，画面存在明确主角则默认主角；存在多个同等主角才澄清。完整群组是用户指定主体时保留其相对关系。背景内可独立使用的建筑、植物也可作为主体提取；无法确定主体的整幅风景需先明确保留对象。

记录主体锁定项：类别、身份特征、辨识色、服装与道具种类、数量、朝向、姿态及部件关系。按目标风格调整比例、线条、明暗和纹理；不随意更换身份、产品型号或配件。不保证生物识别意义的身份一致，应逐项视觉检查。

先读取 [subject-completeness.md](subject-completeness.md)，确定交付范围并检查输入截断。默认完整主体模式下自动补全缺失肢体或部件；明确头像、半身或局部请求时尊重指定范围。保留可见身份与姿态，扩展画布自然补全输入未展示部位，并将其记录为推演。生成后必须逐部位检查，发现截断自动修复；不能只扩大透明边框而保留断腿。

## 读取与生成

先读 [output-delivery.md](output-delivery.md)。默认一个初始候选、一个最终 PNG；首张验收通过即停止。工具有数量参数时设为 1，无此参数时只在 prompt 中写明单图，不擅自追加第二次生成。

读取 `shared-style.md`、`negative.md`、`router.md`，再读实际涉及的主体与材质文件，避免全量加载。使用原始 STYLE 加已通过的相应类型锚点，减少生成图反复作为唯一参照造成的漂移。

向图像工具明确各输入的角色，提交类似如下的分层要求，并填入实际风格规则：

```text
Task: style-transfer of the SUBJECT, delivered as one reusable cutout asset.
OUTPUT_COUNT: exactly one final transparent PNG asset for this task.
Keep the selected subject or subject group together on one canvas.
No alternate version, duplicate, comparison panel, contact sheet or extra preview.
Inputs: enumerate each actual input image and label SUBJECT or STYLE.
SUBJECT invariants: identity cues, category, count, pose, orientation,
costume/parts, defining colors and relationships recorded from the upload.
STYLE: the saved style invariants plus the relevant subject/material rules.
Change the visual rendering according to STYLE; retain SUBJECT invariants.
OUTPUT_SCOPE: complete_subject unless an explicit user crop was requested.
INPUT_CROP and COMPLETION_PLAN: name the actual truncated parts and how each
will be continued in the same pose, clothing and target style. Reconstruct
missing legs through knees and ankles to complete feet/shoes where applicable.
Composition: extend the canvas and reframe to show the complete intended subject,
with clear transparent padding beyond all extremities. Do not copy source cropping.
Preserve natural occlusions and actual anatomical/mechanical differences.
Output: actual transparent background, PNG with alpha. Preserve intentional
holes between limbs, handles and accessories. Retain fine silhouette details.
No backdrop, ground plane, frame, watermark, added label or painted checkerboard.
No ground shadow unless specifically requested; retain shading on the subject.
```

启用工具的真实透明参数。当前内置工具使用 `transparent_background: true`；所有输入有本地路径时用 `referenced_image_paths`；若有无本地路径的会话图片，用覆盖全部目标的最小 `num_last_images_to_include`（最多 5），两种方式不可同时传。无法覆盖全部输入时请用户重传缺失图。实际工具接口变化时以当前 schema 为准。不同工具不共享这些参数名。

没有适用图像工具或透明能力时明确说明缺项，不把文字 prompt 当图片交付，不擅自改用 API。文件应保存到用户要求位置或工作区输出目录，保留原件。

## 先检查主体完整性

按 `subject-completeness.md` 打开实际输出与原始输入逐项对比，保存 `<output-stem>.subject-qa.json`。默认人物素材不能在大腿或膝部平切；需有合理连接的腿与脚，或有依据的自然遮挡。完整性、身份、风格和透明度任一失败均不交付。发现缺失自动编辑补全，每次修改后重新检查全部门槛。完整性与透明修复共用每次转换最多两次修正的上限。

## 文件与视觉双重验收

对实际输出文件运行（需要 Python 3 与 Pillow）：

```text
python scripts/check_png.py path/to/result.png --report path/to/result.alpha.json
```

脚本以 PNG 文件签名、实际解码格式、原始 Alpha 能力、透明/可见像素及透明边框为依据；不修改图像。`RGBA` 且全部 Alpha=255 仍失败，全透明空文件同样失败。索引色 PNG 的 tRNS 透明信息也可正常验收。

脚本通过只说明基本透明结构合格。还必须查看原图以及黑、白背景上的临时合成预览：是否仍有被画进图里的棋盘格、残余背景块、白边/黑边、杂散像素；发丝和细部是否被吞；应镂空的位置是否通透；主体内部是否意外变透明；玻璃、薄纱、辉光是否保留合理半透明。临时合成预览只用于内部检查，不展示为第二张输出、不附带交付；首张已合格的原始 PNG 不额外制作缩小版或重复重导出版本。

风格匹配和主体锁定项也要逐项检查。若工具生成了假透明或错误边缘，使用图像编辑工具针对问题重试，不用“删除全部白色像素”来抠图，不用格式转换把不透明 RGB 假装成合格 RGBA。实际修复必须重新验收。

默认最多两次有针对性的修正。仍失败则报告问题和未完成状态，不把失败图标为最终素材。仅交付一个选定的真实 PNG 与简短验证结论；首张通过便交付首张，不额外生成备用图。必要修复后只选一个通过的版本交付，检查记录留存内部。工具已展示同一成品时不再嵌入同一图片；下载链接指向该同一文件。
