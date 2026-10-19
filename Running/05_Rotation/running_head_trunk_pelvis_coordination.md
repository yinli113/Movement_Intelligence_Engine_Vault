---
id: running_head_trunk_pelvis_coordination
canonical_id: running.rotation.head_trunk_pelvis_coordination
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: "Running - Head Trunk Pelvis Coordination and Repeatability"
aliases: [Head Trunk Pelvis Coordination, Head lateral translation, CoM counterbalancing]
domain: running
directly_measured: false
camera_views: [front, back, side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_vellucci_sprint_coordination_2025, running_morley_lumbar_restriction_2019, running_dingenen_2d_reliability_2018, running_reinking_2d_reliability_2018, gruenke_kiptum_running_analysis_2023]
relationships:
  required_inputs: [running_body_centre_proxy, running_pelvis_rotation, running_shoulder_rotation, running_pelvis_thorax_rotation, running_running_cycle, running_variability]
  supports: [running_altered_rotational_coordination, running_rotational_coupling, running_left_right_asymmetry]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_measurement_limitations, running_kinematics_are_not_kinetics]
confidence: high
review_status: evidence_audited_2026_10_16
relationship_count: 14
hub_score: 30
centrality: 0.15
updated: 2026-10-16
reasoning_contract:
  relationship_id: running.rotation.head_trunk_pelvis_coordination
  anatomical_segments: ["head", "thorax", "pelvis"]
  measurable_metrics: ["running.frontal.head_pelvis_offset", "running.frontal.shoulder_centre_offset", "running.frontal.pelvis_tilt", "running.frontal.shoulder_tilt"]
  observation_scope: [continuous_window, reviewed_stance, reviewed_stride]
  limitation_keys: [projection, timing, tracking, coverage, confounding, kinetics, population, reliability]
  literature_sources: ["running_vellucci_sprint_coordination_2025", "running_morley_lumbar_restriction_2019", "running_preece_spine_pelvis_2016"]
  claim_class: evidence_informed_hypothesis
---

# Head–trunk–pelvis coordination

## Canonical relationship
`running.rotation.head_trunk_pelvis_coordination` (existing ID preserved).

## Biomechanical principle
Relative head and shoulder displacement can be examined alongside pelvis-line motion without assuming the body moves as a rigid block.

## Evidence and claim separation
Observational association: R08 relates limb/trunk coordination to CoM displacement in maximal sprinting. It does not directly establish marathon head stabilization. R07 is a restriction experiment, not a head-control test. The proposed head–pelvis explanation is Level 5.
Sources: [[running_vellucci_sprint_coordination_2025]], [[running_morley_lumbar_restriction_2019]], [[running_preece_spine_pelvis_2016]]. Follow source nodes for DOI/URL, design and audit depth. Experimental effects, observational associations and proposed mechanisms must retain their separate labels.

## Measurable inputs and camera views
- Anatomical segments: head, thorax, pelvis.
- Canonical metric IDs: `running.frontal.head_pelvis_offset`, `running.frontal.shoulder_centre_offset`, `running.frontal.pelvis_tilt`, `running.frontal.shoulder_tilt`.
- Supported views: front, back. Each metric retains its own view: frontal line angles/offsets use front or back, sagittal limb/trunk angles use side. These views are not interchangeable.
- Continuous valid windows need no foot event. Stance-specific comparisons require reviewed contact/toe-off boundaries; stride-specific comparisons require reliable same-foot contacts. Timing/lag is an investigation requirement, not a declaration that it is already implemented.

## Expected or possible relationships
Relative head and shoulder displacement can be examined alongside pelvis-line motion without assuming the body moves as a rigid block. A co-occurrence is a descriptive pattern until compatible evidence supports a mechanism; no required ideal amplitude, sign or phase is imposed.

## Analysis questions
Does head-to-pelvis excursion repeat in valid windows? Does head-to-shoulder relative motion change when shoulder and pelvis motions diverge? Are repeated patterns preserved across comparable portions?

## Alternative explanations
Gaze direction, head turning, camera pan, nose tracking error, torso translation, body scale and curve running. Small pelvis-center translation cannot prove small whole-body CoM displacement.

## Testable hypotheses and further assessment
Compare synchronized head and shoulder offsets sharing the same pelvis reference. Inspect the source and visibility, especially a hidden nose in back view. Where head landmarks are unavailable, retain shoulder/pelvis observations independently. Direct gaze or CoM questions require additional instrumentation.

## Structured uncertainty
Resolve `reasoning_contract.limitation_keys` in [[running_measurement_limitations]] only when applicable. Missing synchronized signals block that comparison, not unrelated usable observations. No numerical thresholds are introduced.

## Anatomical and graph links
[[cervical_spine]], [[thoracic_spine]], [[hip_joint]], [[trapezius]], [[running_body_centre_proxy]], [[running_spiral_line]].
Navigation: [[running_reasoning_retrieval_index]], [[running_research_handoff_audit]].
