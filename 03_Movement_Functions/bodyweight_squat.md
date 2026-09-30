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
centrality: 0.089
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

## Stance and temporal descriptors — 2026-09-30

Level 5 `engine_synthesis`, provisional engineering thresholds only. Front stance
is ankle separation / standing shoulder separation in the image x direction:
wide when the ratio is greater than 1.0; otherwise not wide, per the user-defined
stance convention. There is no classification uncertainty band. Require a stable upright baseline before descent.
Stance describes task context and never adds or subtracts movement-quality points;
performance across different stances is not an equivalent-task comparison.

Within each complete front repetition, use its preceding upright baseline and
fixed shoulder-width scale. Track signed image-x displacement of foot midpoints,
ankles, knees relative to their ankles, pelvis midpoint, shoulder midpoint (upper
trunk proxy), and ear midpoint (head proxy). Positive means screen-right; mirror
orientation is not inferred. Foot translation is not inversion or pressure;
hip IR, lumbar motion, true thoracic motion, COM and millimetres are unavailable.

Report sustained onset, signed peak and time, velocity, acceleration, reversal,
and increase in outward slope. Percentages refer to the detected descent window
(start threshold to bottom), not the full cycle or true first movement. Gate each
channel independently: visibility >= 0.65, finite in-frame coordinates, gaps <=
200 ms, >=150 ms persistence. Motion threshold is 0.05 shoulder widths, raised
by baseline noise. Suppress sequencing when a channel starts already displaced,
has missing coverage, or timing windows overlap. Slope changes compare 200 ms
windows; preceding events are candidates for association only. Same-direction
and counter-shift comparisons use simultaneous common-reference trajectories,
not independent peaks. Report each repetition separately; do not turn one event
into a persistent clinical finding. JSON retains the deterministic evidence for
future typed judgments; no external model or confidence probability is implied.

## Movement-first report refinement — 2026-09-30

Report displacement independently from sustained onset. A failed onset threshold
is not evidence of no movement. Retain observed peaks when tracking is partial,
but suppress sequence, derivative and full-phase peak claims across gaps.
Analyse descent and ascent separately against the same standing baseline.
Add individual hip and shoulder horizontal landmark trajectories, shoulder-midpoint
relative to pelvis, and ear-midpoint relative to shoulders (neck-region proxy).
The latter is not cervical joint motion; no tilt, rotation or spinal alignment is
inferred. All observations remain image-plane descriptors, not clinical deviations.
Default dashboard: one repetition and phase at a time, plain-language regional
observations and visible uncertainty reasons; raw rates and clinical context are
collapsed. Show no causal initiator wording in the primary summary.

## Side-view temporal story — 2026-09-30
Use the engine-selected tracked side for horizontal foot/ankle travel, knee relative
to ankle, hip and shoulder travel, shoulder relative to hip, and ear relative to
shoulder. Normalize horizontal offsets by preceding standing heel-to-toe image-x
length; heel-minus-forefoot vertical change uses standing shoulder-to-ankle image-y
height. Keep their units separate in charts. A stable upright baseline, finite
landmarks, visibility >=0.65, <=200 ms gaps and >=150 ms persistence are required
for events; missing channels remain explicitly unavailable. Provisional thresholds:
0.1 projected foot lengths horizontal, 0.01 standing heights heel change, rate
increases 0.3 foot lengths/s and 0.03 standing heights/s. Baseline noise can raise
thresholds. These are engineering gates, not normal/pathological boundaries.
Analyse descent and ascent separately; both use the same preceding upright baseline.
Phase-start displacement has unknown earlier onset but may still amplify later.
Sequence is temporal association only; knee/hip travel is expected in a squat and
is not automatically a fault. Do not claim pelvic tilt, lumbar/cervical joint
kinematics, stance width or causal fascial impairment. Replay uses only this side
recording; never synchronize independent front and side trials.

## Side-view coordination and literature boundary — 2026-09-30

[[schurr_2d_3d_movement_assessment_2017]] supplies method-comparison context;
[[straub_powers_squat_biomechanics_2024]] supplies trunk/shin interpretation context.
Neither validates this app. The following contract is Level 5 `engine_synthesis`.

Use selected-side, finite in-frame landmarks with visibility >=0.65 and recorded
image width/height ratio to calculate projected knee/hip flexion and unsigned
shin/trunk inclination from vertical. Correct x by image aspect ratio before
angle calculation. Missing aspect metadata makes these new angular channels
unavailable; never assume a square image. Degenerate segments are unavailable.
Standing-baseline angle changes use a 5-degree onset gate and 15 degrees/s rate
increase gate, raised by baseline noise. These are motion descriptors, not faults.
Keep degrees, horizontal foot-length offsets and vertical standing-height offsets
on separate charts. Preserve phase-relative percentages and absolute replay times.

Descent candidate: over a 300 ms window shin inclination changes <=1 degree,
after >=2 degrees increase in the preceding window, while trunk inclination
increases >=3 degrees and hip y continues downward >=0.015 standing heights.
Ascent candidates use common-time hip/shoulder y travel over 300 ms: hip rise
>=0.015 standing heights, shoulder not falling, and hip-minus-shoulder rise
>=0.01 heights means hips rise faster; reverse the comparison for shoulders.
Both rising >=0.015 with difference <0.01 indicates similar vertical travel in
that interval, not global coordination or a normal score. Sustained flags require
150 ms. Timings label the start of the qualifying comparison window, not true
movement onset. Report measured interval changes and knee-flexion depth proxy.
Suppress relationship events for missing samples, >200 ms gaps, missing baseline
or inconsistent image aspect ratio. Require continuous baseline-to-phase coverage.
No candidate does not mean no movement. Per-repetition observations do not become
persistent clinical/fascial triggers; no new line assignment or treatment follows.

New video processing retains image aspect metadata; existing side summary angles and new angular trajectories use the same corrected geometry. Older imported frames retain legacy normalized-coordinate summary calculations for compatibility, but new angular timing remains unavailable. Reanalysis is required for the updated geometry.
