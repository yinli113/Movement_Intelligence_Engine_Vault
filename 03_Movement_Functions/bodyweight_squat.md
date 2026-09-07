---
id: bodyweight_squat
type: Movement Function
preferred_name: Bodyweight Squat
aliases: [bilateral bodyweight squat, unloaded squat, air squat]
short_definition: "A bilateral unloaded squat performed without an overhead mobility requirement and analysed as a time-series movement strategy."
domain: squat
evidence_level: 2
source_role: domain_movement_definition
supported_by: [gray_cook_movement_2010, straub_powers_squat_biomechanics_2024]
status: reviewed_for_app_v1
reviewed_date: 2026-08-27
connects_to: [deep_squat, movement_pattern, squat_joint_muscle_mapping, squat_myofascial_mapping, squat_observability_boundary, squat_cross_view_synthesis]
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 10
hub_score: 17
centrality: 0.09
---

# Bodyweight Squat

## Definition

The bodyweight squat is a bilateral, unloaded squat performed without the overhead
shoulder-mobility requirement of the FMS [[deep_squat]]. The first app protocol uses
continuous video and analyses descent, bottom, ascent, and completion across repeated
repetitions.

It is a movement-strategy assessment, not a test of one ideal or normal squat.
Stance width, foot rotation, arm position, selected depth, tempo, and symptoms are
part of the protocol context because each can change the observed mechanics.

## V1.1 Protocol

- A side-view video, front-view video, or both may be analysed.
- Three unloaded repetitions are requested in each selected recording.
- Side-only and front-only reports remain valid view-bounded observations.
- Cross-view synthesis is an explicit user choice and requires both recordings.
- The user selects a comfortable stance and depth and keeps both consistent.
- No overhead arm position is required.
- Stop if pain, dizziness, or loss of balance occurs.
- Results describe the recorded strategy and are not a diagnosis or treatment plan.
- When cross-view is selected, each recording is analysed independently before
  [[squat_cross_view_synthesis]]. The repetitions are not synchronized or treated as
  the same movement trial.

## Movement Phases

1. Standing baseline.
2. Descent onset to peak knee-flexion proxy.
3. Bottom transition.
4. Ascent to standing completion.

## Primary App Metrics

- repetition count;
- descent and ascent duration;
- peak knee-flexion proxy;
- peak hip-flexion proxy;
- trunk inclination;
- tibia inclination;
- trunk-tibia angle;
- depth and timing consistency;
- heel-rise proxy when foot landmarks are reliable;
- front-view knee-to-foot tracking, pelvic shift, trunk shift, stance-width, and
  left-right asymmetry proxies;
- cross-view complementary-pattern and recording-agreement summaries.

## Interpretation Boundary

Metrics may identify a hip-biased, neutral, or knee-biased strategy and may surface
joints or muscle regions worth reviewing. They cannot establish joint restriction,
muscle weakness, activation, pathology, pain source, or fascial tension. See
[[squat_observability_boundary]].

## Sources

- [[gray_cook_movement_2010]] - whole-pattern and screen-versus-diagnosis framework.
- [[straub_powers_squat_biomechanics_2024]] - modifiable squat parameters and applied
  biomechanical interpretation.

## Evidence Grounding
```yaml
evidence:
  - source_id: rajagopal_opensim_model_2016
    level: domain_biomechanics
    evidence_tier: Level 3
    description: "Lower extremity joint kinematics, moments, and multi-joint muscle activations during bilateral squatting."
  - source_id: openstax_anatomy_physiology_2e
    level: foundational_anatomical_framework
    evidence_tier: Level 1
    description: "Triple flexion/extension articulation of ankle, knee, and hip joints."
```
