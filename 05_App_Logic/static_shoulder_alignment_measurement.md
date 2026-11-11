---
id: static_shoulder_alignment_measurement
type: App Logic
preferred_name: Static Shoulder Alignment Measurement
aliases: [shoulder tilt angle, shoulder height asymmetry metric, coronal shoulder alignment]
category: App Logic
short_definition: "Original-image pixel angle between visible left and right shoulder landmarks and the horizontal, with study-derived reporting bands for static front and back views."
evidence_level: 5
evidence:
  - source_id: trovato_postural_evaluation_2022
    evidence_level: 4
    supports: "Angular shoulder alignment as an applied digital-posture measure; healthy young-adult posterior reference 1.5° ± 1.2° and ICC 0.93."
relationships:
  parent_concepts: [bodyreading_static_posture]
  related_concepts: [movement_reporting_standards, metric_evidence_classification]
confidence: medium
review_status: implemented_reference_policy
relationship_count: 4
hub_score: 12
centrality: 0.04
updated: 2026-11-11
---

# Static Shoulder Alignment Measurement

## Definition

For front and back static images, connect the visible left and right shoulder landmarks and calculate the acute angle between that line and image horizontal using the **original image width and height in pixels**.

$$\theta = \operatorname{atan2}(|\Delta y_{px}|, |\Delta x_{px}|)\times\frac{180}{\pi}$$

Direction is retained separately: positive means the left landmark is lower/right higher; negative means the left landmark is higher/right lower.

## Reporting bands

[[trovato_postural_evaluation_2022]] reported healthy young-adult posterior shoulder alignment of 1.5° ± 1.2°. TillYes uses the following Level 5 reporting policy:

| Absolute shoulder-line angle | App severity | Meaning |
|---:|---|---|
| <2.7° | normal | Within the study-derived mean + 1 SD reference band. |
| 2.7° to <3.9° | mild | Above mean + 1 SD; retain as a reportable observation. |
| 3.9° to <5.1° | moderate | Above mean + 2 SD; include in Measurement Details. |
| ≥5.1° | significant | Above mean + 3 SD; eligible for higher report priority. |

These are reporting bands, not diagnostic cutoffs. A 4.2° shoulder line is therefore a **moderate** reportable observation.

## Implementation contract

- Metric id remains `shoulder_height_difference` for report and knowledge compatibility.
- Unit is `degrees_from_horizontal`.
- Use original-image pixel geometry; never compute the angle in a stretched normalized unit square.
- Do not use `height_difference: 0.025` or another percentage of total image height for the shoulder metric.
- Front and back views use the same definition and bands.
- The overlay and the report engine must use the same angular geometry.

## Related concepts

- [[bodyreading_static_posture]]
- [[movement_reporting_standards]]
- [[trovato_postural_evaluation_2022]]

