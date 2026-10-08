---
id: squat_trunk_tibia_relationship
type: Movement Pattern
preferred_name: "Squat Trunk–Tibia Relationship"
domain: squat
evidence_level: 4
source_role: applied_clinical_biomechanics_commentary
relationships:
  supported_by: [straub_powers_squat_biomechanics_2024]
  connects_to: [bodyweight_squat, hip_joint, knee_joint, squat_depth_context, squat_article_app_contract, squat_observability_boundary]
confidence: medium
review_status: source_checked_app_translation_unvalidated
relationship_count: 8
hub_score: 12
centrality: 0.071
updated: 2026-10-08
---

# Squat Trunk–Tibia Relationship

## Source-grounded concept

[[straub_powers_squat_biomechanics_2024]], “Knee vs. Hip Extensor Biased Squatting,” Figure 5: trunk inclination minus tibia inclination gives the proposed categories >10° hip bias, −10° to +10° neutral, and <−10° knee bias. The cited regression crosses equal moments at −8°; this is distinct from the commentary’s practical bands. Its predictor is measured at peak knee flexion, with the outcome averaged over descent.

## App translation — Level 5 engine synthesis

Use a common vertical reference, same frame, same tracked side, and aspect-corrected coordinates. Subtract tibia inclination from trunk inclination; never subtract a horizontal-reference angle from a vertical-reference angle. Direction and camera orientation must be declared before interpreting unusual backward lean. An unsigned angle is insufficient to distinguish all postures.

Retain the measured value, timestamp, quality flags, selected depth and protocol. Do not independently select peak trunk and peak shin angles from different frames. At either boundary, the source figure places the value in the neutral category; uncertain measurements near boundaries should remain uncertain instead of implying a meaningful biological transition.

Report an apparent strategy consistent with the commentary, never an observed hip/knee moment ratio or equal muscle effort. Primary instrumented evidence and markerless validation must be reviewed before treating this as a quantitative kinetic estimator. The categories supply no pass/fail score.

## Relationships

| Node | Relationship | Evidence boundary |
|---|---|---|
| [[bodyweight_squat]] | Movement context | Unloaded, non-overhead protocol |
| [[hip_joint]] / [[knee_joint]] | Anatomical interpretation | Joint moments remain unavailable |
| [[squat_depth_context]] | Depth changes the comparison | Compare equivalent tasks |
| [[squat_article_app_contract]] | Consumer policy | Level 5 translation |
| [[squat_observability_boundary]] | Measurement boundary | 2D geometry is not kinetics |
