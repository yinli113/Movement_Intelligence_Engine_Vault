---
id: running_measurement_limitations
canonical_id: running.guardrail.measurement_limitations
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Measurement Limitations
aliases: [running camera limitations]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  governs: [running_event_detection, running_body_centre_proxy, running_pelvis_rotation, running_thorax_rotation, running_foot_strike]
  connects_to: [running_kinematics_are_not_kinetics, running_reporting_guardrails, running_evidence_gate]
confidence: high
review_status: canonical
relationship_count: 49
hub_score: 97
centrality: 0.438
updated: 2026-09-09
---

# Running - Measurement Limitations

## Camera Contract

- Side view is preferred for sagittal timing, landing, progression, trunk lean, and compression proxies.
- Front/back views are preferred for frontal asymmetry and selected rotation proxies.
- Monocular transverse rotation is a proxy: `is_rotation_proxy: true`, `true_3d_rotation: false`.
- Suppress outputs affected by occlusion, foreshortening, an uncertain contact frame, poor calibration, or unreliable landmark confidence.
- Never invent or interpolate across a quality-gate failure without retaining that failure in provenance.

## Terminology

A hip midpoint is a [[running_body_centre_proxy|body-centre proxy]], not whole-body COM. Foot-strike classification is estimated and view/frame-rate dependent.

## Required Output Fields

`value, unit, view, valid_samples, confidence, quality_flags, algorithm_version`.

## Relationships

Applies to all measurements in [[running_canonical_measurement_contract]] and is enforced by [[running_evidence_gate]].


## Conditional reasoning limitations (2026-10-16)
Apply only the rows whose conditions are present. Retrieve these alongside a relationship's `limitation_keys`; do not append the entire list to every answer.

| Key | Applies when | Consequence / further assessment |
|---|---|---|
| projection | A relationship uses 2D angles or lateral offsets | Yaw, perspective, camera roll and landmark definition can alter the signal. Check source frames and same-camera segments; 3D axial motion needs compatible instrumentation. |
| timing | A claim names stance, toe-off, contact or phase lag | Require reliable, synchronized boundaries for phase labels. Continuous windows remain eligible for descriptive co-variation; lag needs an explicit method, sampling and uncertainty. |
| tracking | Missing, swapped, low-visibility or unresolved landmarks; suspected spikes | Flag technical failures with reasons, retain raw data and compare robust summaries. Do not delete genuine extremes or invent a universal cutoff. Do not bridge gaps. |
| coverage | Partial recording or unequal usable samples | Report time coverage and each side's counts; conclusions apply only to those portions. |
| confounding | Comparing sides, speeds, athletes or sessions | Check speed, surface/curve, fatigue, camera, arm task and body proportions; association does not isolate a cause. |
| kinetics | Explanation invokes force, work, economy, activation or CoM | Pose geometry does not measure those quantities. Obtain the corresponding force, metabolic, EMG or validated whole-body measurements. |
| tissue | A myofascial or muscle-state interpretation is requested | Anatomical model is an interpretive hypothesis; movement alone cannot identify tissue tension, weakness or dysfunction. |
| population | Sprint, small cohort, elite youth or anthropometric group study is transferred | Preserve study context; no universal norms or ancestry-based predictions. |
| reliability | A sample-size or repeatability claim is made | R09 studied means of seven steps for specific variables, not a universal seven-strides-per-side rule or phase-lag validation. |
