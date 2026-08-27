---
id: squat_cross_view_synthesis
type: App Logic
preferred_name: Squat Cross-View Synthesis
aliases: [multi-view squat synthesis, side-front squat report]
domain: squat
evidence_level: 5
source_role: app_synthesis_policy
supported_by: [straub_powers_squat_biomechanics_2024, gray_cook_movement_2010]
status: active_spec
reviewed_date: 2026-08-27
connects_to: [bodyweight_squat, squat_observability_boundary, squat_joint_muscle_mapping, squat_myofascial_mapping, movement_reporting_standards]
---

# Squat Cross-View Synthesis

## Purpose

Combine independently analysed side and front squat recordings into one movement
story while preserving view-specific evidence. The synthesis does not re-run pose
detection and does not align separately recorded repetitions.

## Relationship Types

- `complementary`: different planes contribute distinct observations to one
  anatomical theme;
- `corroborating`: both recordings support a genuinely comparable protocol or
  repeatability observation;
- `conflicting`: recordings differ enough that setup, effort, tracking, or natural
  variability should be reviewed;
- `limited`: one view lacks sufficient quality or complete repetitions.

## V1.1 Themes

| Theme | Side evidence | Front evidence | Allowed synthesis |
|---|---|---|---|
| Depth and frontal control | selected depth, sagittal segment strategy | knee-to-foot excursion, frontal asymmetry | Multi-plane strategy at the selected depth; not movement quality or pathology. |
| Ankle-foot strategy | heel-rise and tibia proxies | knee-to-foot excursion, stance width | Ankle-foot contribution may warrant direct review; no dorsiflexion or pronation diagnosis. |
| Trunk-pelvis organization | trunk inclination and trunk-tibia relationship | pelvic and trunk lateral shift | Complementary sagittal/frontal trunk-pelvis organization; no spinal or hip diagnosis. |
| Repeatability | depth and timing variability | pelvic-descent and frontal variability | Whether both recordings were similarly repeatable; recordings remain separate trials. |

## Quality Gates

- Retain side and front reliability independently.
- Mark synthesis `limited` when either view has low reliability or no complete rep.
- Do not average angles or timestamps across views.
- Do not call absence in one view proof that a pattern is absent.
- Report differences as possible protocol or movement variability, not contradiction
  by the person.

## Interpretation Boundary

Cross-view evidence can prioritize a region or question for direct assessment. It
cannot diagnose pathology, select a weak/tight muscle, measure joint mobility, infer
pain source, or detect fascial tension, restriction, or loading.
