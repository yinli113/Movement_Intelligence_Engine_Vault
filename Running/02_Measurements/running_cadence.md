---
id: running_cadence
canonical_id: running.rhythm.cadence
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: "Running - Cadence and Step Frequency Dynamics"
aliases: [Cadence, Step rate, Step frequency, Stride frequency]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_mesquita_step_frequency_pelvis_2024, running_schubert_stride_frequency_2014, running_anderson_step_rate_2022, running_goss_step_rate_training_2026]
relationships:
  required_events: [running_initial_contact, running_running_cycle]
  supports: [running_pelvis_rotation, running_variability, running_fatigue_drift, running_longer_landing_strategy, running_altered_rotational_coordination]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: high
review_status: evidence_audited_2026_10_16
relationship_count: 18
hub_score: 28
centrality: 0.14
updated: 2026-10-16
reasoning_contract:
  relationship_id: running.rhythm.cadence
  anatomical_segments: ["pelvis", "thigh", "hip_joint"]
  measurable_metrics: ["running.rhythm.cadence", "running.swing.thigh", "running.frontal.pelvis_tilt"]
  observation_scope: [continuous_window, reviewed_stance, reviewed_stride]
  limitation_keys: [projection, timing, tracking, coverage, confounding, kinetics, population, reliability]
  literature_sources: ["running_mesquita_step_frequency_pelvis_2024"]
  claim_class: evidence_informed_hypothesis
---

# Cadence–pelvis–thigh coordination

## Canonical relationship
`running.rhythm.cadence` (existing ID preserved).

## Biomechanical principle
Step frequency and speed are conditions that can change segment coordination; cadence is a whole sequence rate, not an inferred property of one pelvic excursion.

## Evidence and claim separation
Experimental finding: R05 manipulated frequency/speed. The observed pelvic-roll response is sample-specific; explanations involving hip flexor stretch or gravity are interpretations.
Sources: [[running_mesquita_step_frequency_pelvis_2024]]. Follow source nodes for DOI/URL, design and audit depth. Experimental effects, observational associations and proposed mechanisms must retain their separate labels.

## Measurable inputs and camera views
- Anatomical segments: pelvis, thigh, hip_joint.
- Canonical metric IDs: `running.rhythm.cadence`, `running.swing.thigh`, `running.frontal.pelvis_tilt`.
- Supported views: side, front, back. Each metric retains its own view: frontal line angles/offsets use front or back, sagittal limb/trunk angles use side. These views are not interchangeable.
- Continuous valid windows need no foot event. Stance-specific comparisons require reviewed contact/toe-off boundaries; stride-specific comparisons require reliable same-foot contacts. Timing/lag is an investigation requirement, not a declaration that it is already implemented.

## Expected or possible relationships
Step frequency and speed are conditions that can change segment coordination; cadence is a whole sequence rate, not an inferred property of one pelvic excursion. A co-occurrence is a descriptive pattern until compatible evidence supports a mechanism; no required ideal amplitude, sign or phase is imposed.

## Analysis questions
Are cadence and speed independently known? Does pelvic excursion change within the runner at matched speed? Is the thigh response consistent or participant-specific?

## Alternative explanations
Speed, step length, curve, fatigue, individual coordination and camera changes; a longer right stance need not imply a lower right cadence.

## Testable hypotheses and further assessment
Use validated cadence or externally counted steps. Compare matched-speed trials; retain observed responses rather than impose a target. Frontal thigh offset is not sagittal hip ROM. Synchronize separate views if investigating cross-plane relationships.

## Structured uncertainty
Resolve `reasoning_contract.limitation_keys` in [[running_measurement_limitations]] only when applicable. Missing synchronized signals block that comparison, not unrelated usable observations. No numerical thresholds are introduced.

## Anatomical and graph links
[[hip_joint]], [[psoas_major]], [[gluteus_medius]], [[running_pelvis_rotation]], [[running_step_time]], [[running_stride_time]].
Navigation: [[running_reasoning_retrieval_index]], [[running_research_handoff_audit]].

## Recovery-leg mechanism routing
For knee flexion, swing-leg inertia and step-frequency questions, retrieve [[running_swing_knee_inertia]] → [[running_van_oeveren_running_styles_synthesis]]. Do not substitute [[running_steudel_limb_length_economy_2007]] as direct support. General mechanism support is separate from validated cadence measurement and from an athlete-specific explanation.
