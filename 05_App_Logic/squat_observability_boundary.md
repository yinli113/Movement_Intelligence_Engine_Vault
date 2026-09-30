---
id: squat_observability_boundary
type: App Logic
preferred_name: Squat Observability Boundary
aliases: [squat camera boundary, squat inference limits]
domain: squat
evidence_level: 5
source_role: app_observability_policy
supported_by: [straub_powers_squat_biomechanics_2024, gray_cook_movement_2010]
status: active_spec
reviewed_date: 2026-08-27
connects_to: [bodyweight_squat, squat_joint_muscle_mapping, squat_myofascial_mapping, squat_cross_view_synthesis, metric_evidence_classification, movement_reporting_standards]
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 5
hub_score: 9
centrality: 0.045
---

# Squat Observability Boundary

## Side View Allow-List

- 2D knee-flexion and hip-flexion proxies;
- trunk and tibia inclination in the image plane;
- trunk-tibia angle proxy;
- selected depth and phase timing;
- repetition count and repeatability;
- heel-rise proxy when heel and forefoot landmarks remain reliable.

## Front View Allow-List

- knee-to-foot tracking proxy;
- pelvis midpoint lateral displacement relative to standing baseline;
- shoulder-midpoint relative to pelvis-midpoint lateral displacement;
- left-right timing/depth contribution;
- stance-width descriptor when landmarks are adequate;
- repetition count and repeatability from pelvis-descent timing.

## Cross-View Allow-List

- combine independently produced side and front findings by anatomical theme;
- identify complementary multi-plane observations without claiming that they are
  the same repetition;
- describe corroboration only when both views measure a genuinely comparable theme;
- identify conflict or limited synthesis when view quality, repetition count, or
  protocol setup differs;
- preserve each view's metric, reliability, and competing explanations.

Cross-view synthesis must never average side and front angles, align events across
separate recordings, or upgrade two proxies into a diagnosis. See
[[squat_cross_view_synthesis]].

## Unavailable Without Additional Instrumentation

- joint moments, force, pressure, COM, COP, kinetics, and tissue loading;
- muscle activation, weakness, length, fatigue, or inhibition;
- passive ankle, knee, hip, or spinal mobility;
- lumbar segment position from MediaPipe landmarks;
- reliable pronation/supination or tibial rotation from a single ordinary view;
- pathology, pain source, injury risk, or diagnosis;
- fascial tension, restriction, line loading, or energy storage.

## Finding Contract

Every finding must include:

1. measured observation and phase;
2. reliability and view;
3. movement-strategy interpretation;
4. joints and candidate regions to review;
5. competing explanations;
6. optional myofascial hypothesis labelled `engine_synthesis`;
7. explicit conclusions that cannot be made.

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

## Repeated multiregion squat translation — 2026-09-30

This app policy is Level 5 `engine_synthesis`, not an anatomical-source claim that
a squat shift diagnoses any line. In a single phase of a repetition, head, pelvis
and at least one named foot must simultaneously exceed their own noise-adjusted
displacement thresholds in the same screen direction for at least 150 ms, with
no missing data or gaps over 200 ms in that interval. Match the same foot, direction
and phase across at least two repetitions and at least half of all completed
repetitions. Report the supporting repetition numbers and absolute timestamps.
Unavailable recordings are not negative evidence; counts use all completed reps
conservatively and disclose tracking limitations. Do not combine independent peaks
or separate camera views to invent a chain.

The result can surface Lateral Line, Deep Front Line and Spiral Line as concurrent
assessment candidates. Lateral translation provides the closest descriptive context
for LL. DFL is a deep-medial support differential, not limited to medial knee motion.
SPL is a less-specific cross-body differential: translation alone does not establish
rotation. Seek independent rotational evidence before a rotation-specific account.
Whole-body translation, camera movement, stance strategy and tracking artefacts remain
competing explanations. None of these observations measures line damage, restriction,
weakness, activation, tension, causality, or a need for treatment.

Clinical display must connect observations to candidate rationale, muscle-to-line
relationships, assessment questions, retest and camera limits. Untriggered lines
are not confirmed balanced or normal. No synthetic score, inhibited/overactive
label, or fixed treatment prescription may substitute for measured evidence.
The synchronized JSON `multiRegionClinicalContract` owns the app wording.

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
