# 单次生成与单图交付

适用于画风 Skill 的普通主体转换；工厂蒸馏阶段的多轮实验与材质库不受此数量规则影响。

## 默认调用预算

普通转换任务默认 `generation_call_budget = 1`，含首次生成在内，总共只调用一次生成/编辑工具。每次工具请求只要一张；工具有 count/n/variants 时按实际 schema 设为 1，没有则在 prompt 中写明一张，不能捏造参数。

这一限制同时覆盖透明修复、补腿扩图、清边、调整留白、尺寸变体、备用方案和超时后的盲目重试。把同一任务拆到另一个函数或称为“后处理”也不能增加调用。单图默认优先于旧的“最多两次自动修复”约定；调用次数和最终文件数分别记录，不能写 delivered_image_count=1 就把两次实际生成当成单次。

图像数量不等于人物数量。保持选定的多人、人物与傀儡/坐骑组合在同一张 PNG 内。明确批量任务按每个输入分别计算；用户明确要求多方案或继续修复时，才按该请求增加相应调用预算。

## 在第一次生成中完成要求

生成前充分查看输入、风格与相关锚点，把实际截断位置、补全计划、姿态、服装、完整脚/鞋、透明背景和留白全部写入第一次 prompt。补全输入裁切仍是自动行为；生成后的再生成修复不再默认自动执行。

```text
OUTPUT_COUNT: exactly one transparent PNG image for this task.
Complete the identified missing parts and preserve identity in this first result.
Keep the selected subject/group together on one canvas, with full silhouette,
clear transparent padding, alpha-zero background and no outside haze or glow.
No alternate image, duplicate, comparison panel, contact sheet or extra preview.
```

## 检查后停止

生成后仍须执行主体完整性、身份、画风、Alpha 和黑白底检查。首张通过即交付该文件并结束。首张有缺失、背景残留或边缘失败时，保留这张候选并说明具体问题、将对应 QA 记为未通过；停止，不再次调用图像工具，不擅自降低检查门槛或把失败图称为合格成品。只有用户明确要求“修复 / 重做 / 继续生成”后，才在该后续授权范围内生成。

工具失败或返回状态不明时也不能盲目追加生成；先确认既有任务状态，无法确认则如实报告。一次调用本身可能失败，不能保证每次首张都通过。

## 展示去重

同一结果最多展示一次。宿主已展示时不再用 Markdown 图片重复嵌入；下载链接指向同一 PNG，不复制一份或再生成缩小版。检查用黑白底预览、缩略图、Alpha/主体 QA 记录只用于内部检查，不作为第二张成品或图片入口。

单次请求中已经发生的工具展示无法靠 Skill 撤回。可以控制的是不再追加图像调用、不重复嵌入已有成品，不声称能隐藏宿主不可控的历史展示。

QA 记录实际 `generation_call_budget`、`generation_calls_used`、`requested_output_count`、`initial_candidate_pass`、`selected_final_image`（未通过时为 null）、`candidate_image`、`delivered_image_count`、`repair_requires_user_request` 和 `overall_pass`。单图模式未通过时合格交付数量为 0，不能因界面显示过候选而伪记成功。维护技能未生成图片时记 not_run。
