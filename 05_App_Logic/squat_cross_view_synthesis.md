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
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 2
hub_score: 4
centrality: 0.018
---

# Squat Cross-View Synthesis

## Purpose

Combine independently analysed side and front squat recordings into one movement
story while preserving view-specific evidence. The synthesis does not re-run pose
detection and does not align separately recorded repetitions.

Cross-view synthesis is optional and must be explicitly selected. Uploading both
views does not replace or suppress either single-view report pathway.

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
