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
- [[kuljian_gmoneymvmt_hip_ir_squat_correlation]] - pelvifemoral clearance, superficial hip flexor and anterior pelvic tilt interactions with hip internal rotation, and individualized squat equilibrium.

## Evidence Grounding

Squat descriptors are supported by the squat-specific sources above. The Rajagopal gait model does not establish bilateral-squat activation or validate this app.
```yaml
evidence:
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


## Schematic replay overlay — 2026-10-28

Replay paths are optional educational drawings with fixed neutral styling and default off. Landmark displacement must never produce a fascial tension score, slack/balanced/high-strain classification, activation state or tissue-loading color. Paths are schematic, not localized patient anatomy. Omit paths with unsupported landmarks. The pose, angle and measurement layers retain their own evidence and units.


## Optional same-set recording alignment — 2026-10-28

Separate trials remain independent and cannot be aligned by repetition index. A phone and computer may instead record the same physical squat set with overlapping footage. Start either device first; make the same visible gesture before and after the set in both views. This is a manually reviewed alignment workflow, not hardware synchronization.

The user must confirm the same set, mark both matching events in each original video, enter positive per-camera marker-time uncertainty estimates and review the correspondence. Preserve SHA-256 file identities, durations, filmed side, marker intervals and method/version. Any source, duration, filmed-side or marker/uncertainty change invalidates the review. Never infer anatomical left/right from mirroring.

Two marker pairs define a linear side-to-front media-time mapping. Use interpolation only inside the marker intervals; do not extrapolate. The difference between start/end offsets is reported as an observed offset change, not a calibrated clock-drift measurement. Propagate marker intervals through the mapping; these are user-estimated bounds and exclude unknown nonlinear drift, dropped-frame and event-detection errors. Linked playback follows the side media clock and cannot alter measurement evidence.

Alignment metadata uses `video-alignment/1.0.0`. A future cross-view event comparison must include event-time uncertainty, use the same source pair and withhold order when intervals overlap or events lie outside the reviewed span. This workflow does not match repetitions automatically, validate joint sequences or change existing per-view numerical summaries. Existing cross-view synthesis and DuckDB ETL retain `synchronized: false`; manually reviewed metadata is separate from that legacy contract.


## Phase 3: shift-centered regional sequence — 2026-10-28

Level 5 engineering policy, not a literature-validated abnormality detector. The existing browser trajectory engine owns the numerical event detection. Its versioned `within-squat-sequence/1.0.0` export carries phase windows, preceding baseline evidence, per-channel status, signed peaks, threshold, samples, native onset time and uncertainty interval. Silver validates and retains these browser-derived facts; it does not invent onset from per-repetition peaks or silently recompute a second detector. Older exports lacking this contract require reanalysis for sequence evidence; peaks remain usable.

Use descent and ascent separately with the same pre-repetition standing baseline. Require continuous baseline-to-phase coverage, reliable channel landmarks, stable scale, finite monotonic timestamps, at least five phase samples and 500 ms, maximum 200 ms gaps, and 150 ms sustained threshold crossing. Angular channels also require stable image aspect metadata. A channel gap before the selected phase withholds that channel's onset. Missing head tracking must not suppress reliable knees/pelvis. Keep partial observed peaks with a reason; never call them confirmed full-phase peaks. Do not create a new ascent onset for a displacement already present at the bottom.

For each front phase, use pelvis translation as the shift anchor. Compare other measured regions with it using interval bounds: earlier, later, timing overlaps/order uncertain, already changed/unknown onset, no sustained onset, or unavailable. Onset uncertainty is a provisional engineering interval of at least ±150 ms or the largest phase sample interval, covering sample selection/smoothing conservatively; it is not calibrated measurement accuracy. Show signed offset and before-to-after change around the shift (±200 ms) only when the complete interval is observed. These are observed threshold changes, not clinical deviations. Report the interval at the native camera clock and allow replay.

Gold retains every channel/phase status and counts ordered/uncertain relationships with the denominator of all Silver-included repetitions, separating phase, view, region and direction. A repeated review candidate requires at least two supporting repetitions and at least 50% of included repetitions. This is descriptive persistence, not proof of a fault. The optional peak magnitude/direction filter never filters trajectory/event evidence.

Cross-view shift comparisons are optional. Require matching SHA-256 source identities/durations and reviewed same-set alignment; do not join repetition indices. Select side event windows by mapped media-time overlap with the selected front phase, preserving both original repetition numbers. Include event intervals and propagated marker intervals; withhold order outside the reviewed span or when intervals overlap. A side phase already displaced has unknown onset. Unmapped or missing evidence remains visible. Alignment never upgrades these observations into causes, abnormal joint states, force, activation or fascial restriction. Legacy cross-view summary and ETL `synchronized: false` remain unchanged; aligned event associations are an explicitly separate layer.


## Consumer report contract — 2026-10-29

`movement-reporting/1.0.0` in squat knowledge v1.7.0 defines metric-specific
meaning, summary basis, limits and vault references. Present front and side
findings as independent recordings. Show reliable available values with their
measured-repetition counts; withhold unsupported findings. Missing onset does
not remove a valid displacement. If the pelvis anchor lacks a reliable onset,
replace the empty relation table with one explanation and retain the full audit
inside details. No new clinical thresholds, algorithms or charts are introduced.

Keep timing intervals, raw metrics, exclusions and ETL counts in optional review.
Literature may support a concept without validating the app's detector or its
thresholds. Baseline offsets are image descriptors, not normative posture labels.
The main result includes front pelvis/trunk and knee-foot descriptors alongside
side heel/shin/trunk observations. SCD2 task context remains separate.


## Visual consumer dashboard — 2026-10-29

The movement-focus dashboard leads with charts and at most two supported repeated
observations per view, following Running's findings-first reporting ladder. It
does not turn any nonzero offset into a clinical issue. Headlines retain browser
consistency flags and require at least two and half of all Silver-included
repetitions to support the observation after exclusions. A missing headline is
not a negative test. Raw evidence, failed tracking and numerical audits remain
accessible outside the primary focus.

`data/video_average_profiles.py` owns display-only average curves. Accepted
continuous channel evidence is mapped to 51 equally spaced positions per phase:
descent 0–50%, ascent 50–100%, with one shared bottom point. Interpolate only
between finite observed samples at most 200 ms apart; never extrapolate or bridge
missing samples/phases. Include a region's repetition only when its entire
101-point curve is available in compatible units. At least two repetitions are
required for an average. Each point uses the same contributing repetitions;
counts can differ between channels. Comparison overlays use those identical
resampled curves and never change the average. This is a shape comparison, not
real-time synchronisation, a new onset detector or a clinical norm. Peak review
filtering does not trim continuous trajectory evidence.

Front panels group hips/upper body and the two knees relative to ankles. Side
view uses one figure with separate heel, shin and trunk scales. All colors are
region/comparison identifiers, never tissue states or pass/fail scores. Remove
the generic onset interval plot from primary focus. Numerical details and
methods are optional. All public evidence is grouped behind one disclosure and
names literature title, author, year and source role; internal knowledge paths
and Obsidian links are not public app content. The knowledge vault remains the
source of truth behind the app.

Running workflow references: `running_reporting_guardrails` findings-first and
optional Gemini sections. Future requested LLM explanations must retain metric
IDs, view, counts, source provenance and known availability; explain only supplied
facts and retrieved compatible knowledge, reject invented numbers/causes, and
keep local reports usable without an LLM. Adding or calling an external LLM is
not part of this dashboard change.


## Plain-language chart summaries and competing explanations — 2026-10-29

Consumer dashboard contract v1.1.0 (knowledge v1.9.0) adds short descriptions of
complete average curves. Describe start/bottom/finish relationships or the phase
containing the largest absolute departure from standing. These are coarse shape
descriptions, not monotonicity, sustained-onset, repetition-persistence, abnormality
or anatomical left/right claims. Zero curves do not generate movement claims.

Optional explanations require an existing gated persistent finding in the same
view. For a trunk-lean finding, consider a hip-oriented strategy using
[[squat_trunk_tibia_relationship]], with ankle–foot/setup as a competing assessment
question using [[squat_stance_foot_context]]. Keep the observed relationship,
source mechanism, personal hypothesis and distinguishing assessment separate.
The source is [[straub_powers_squat_biomechanics_2024]], particularly Tibia
Inclination and Knee vs. Hip Extensor Biased Squatting; application to the person
is Level 5 engine synthesis. Do not rank causes, infer calf tightness, assign
measured loading, infer symptoms or generate treatment. A wedge response alone
cannot identify restricted tissue. No front hypothesis is generated merely from
an average sideways offset. Public evidence names literature, not vault paths.
No external LLM calls or new measurements are introduced.


## Optional Squat Gemini explanation — 2026-10-29

Knowledge v1.10.0 adds `squat-explanation/1.0.0` as an opt-in Streamlit explanation
layer. Reuse Running's allowlisted evidence, curated retrieval and provider
separation, with squat-specific gates. A local packet reconstructs only
average-shape anchors/counts, supported repeated findings and their eligible
curated hypotheses/source reasoning. Independent views remain separate. No
video, raw landmarks, capture/person identifiers, timestamps, SCD2 screens or
user notes are sent. A preview shows the exact packet before explicit Generate.

Generated prose references supplied observation and eligible hypothesis IDs.
Attach original observations, public literature metadata and curated
distinguishing checks independently of model wording. Format, reference and
conservative language checks are not semantic or clinical validation. Reject
unknown references, numerical/causal/tissue/prescription claims, links and HTML.
Retain model, prompt/evidence/knowledge provenance and label output unverified.
Errors never replace the deterministic report. A password key stays in local
Streamlit session memory or server environment (`SQUATS_GEMINI_API`), never ETL,
files, model prompts or exports. No call on page load or key entry. This release
uses a mocked provider for verification; no real credential or live generation
is required. No deployment or chat agent is part of this addition.


## Detailed average-curve movement story — 2026-11-02

Knowledge v1.12.0 / visual-movement-summary v1.2.0 adds a deterministic
`squat-curve-story/1.0.0` presentation contract. Movement focus provides detailed descriptions of complete 101-point averages: each phase's largest absolute
average offset, bottom and finish, with native signs, units and contributing
counts. Start/bottom/finish or phase extrema describe sampled average shape;
they do not establish monotonic movement, sustained onset, repetition persistence
or a clinical fault. Nonfinite, partial, all-zero and fewer-than-two contributor
curves do not produce movement narratives. Small nonzero values remain explicitly
below display precision rather than becoming zero. Opposite knee signs do not
establish an imbalance. Upper-body-relative-to-hips is not absolute trunk travel.

The primary story precedes a separate peak/filter review. Distinguish the
per-repetition preceding-standing/shoulder-width average contract from legacy
recording-reference/body-scale peak summaries, and disclose original sign counts
and excluded repetitions. The peak filter does not trim continuous curves.
Both views offer individual overlays while preserving the fixed average.
Supporting research retains task/population and source roles from
[[schurr_2d_3d_movement_assessment_2017]] and
[[straub_powers_squat_biomechanics_2024]]. Optional hypotheses retain their
existing same-view persistent-finding gates. No new detector, clinical rule,
external LLM request or personal assessment record is introduced.


### 2026-11-02 — Shared concise squat overview

The canonical overview contract supplies number-free wording selected from complete average trajectories. The ETL read model owns selection and evidence provenance; Streamlit My summary and the web Gold Medallion summary render the same payload. One overview includes supported observations across available recordings without claiming synchronization. Detailed anchors, values and research remain in Movement focus and closed evidence disclosures. This is local curated wording, not free-form LLM inference.


### 2026-11-02 — Compact context guidance

The contextGuidance contract supplies one closed optional assessment question in Setup & context. It requires an existing reviewed persistent pelvis-shift or side trunk-lean finding; an average offset alone cannot trigger it. Matching-view saved ankle measurements choose missing-both, missing-one or already-recorded wording. The action opens the existing editor without saving or inferring results. [[crowe_unilateral_ankle_dorsiflexion_squat_asymmetry_2020]] supports experimental force asymmetry, not visible hip-shift causation; [[straub_powers_squat_biomechanics_2024]] supplies setup context. Personal applicability remains engine synthesis.
