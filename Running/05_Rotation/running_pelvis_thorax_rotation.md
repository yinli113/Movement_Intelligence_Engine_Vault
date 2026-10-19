---
id: running_pelvis_thorax_rotation
canonical_id: running.rotation.pelvis_thorax
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: "Running - Pelvis Thorax Rotation and Dissociation"
aliases: [Pelvis Thorax Rotation, Shoulder-pelvis coordination, Thoraco-pelvic dissociation, Pelvis-thorax phase lag]
domain: running
directly_measured: false
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_morley_lumbar_restriction_2019, running_mesquita_step_frequency_pelvis_2024, gruenke_kiptum_running_analysis_2023]
relationships:
  required_inputs: [running_pelvis_rotation, running_shoulder_rotation, running_running_cycle, running_initial_contact, running_toe_off]
  supports: [running_rotational_coupling, running_altered_rotational_coordination, running_head_trunk_pelvis_coordination, running_spiral_line]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics, running_measurement_limitations]
confidence: high
review_status: evidence_audited_2026_10_16
relationship_count: 20
hub_score: 36
centrality: 0.18
updated: 2026-10-16
reasoning_contract:
  relationship_id: running.rotation.pelvis_thorax
  anatomical_segments: ["thorax", "lumbar_spine", "pelvis", "shoulder_girdle"]
  measurable_metrics: ["running.frontal.shoulder_tilt", "running.frontal.pelvis_tilt", "running.frontal.shoulder_centre_offset"]
  observation_scope: [continuous_window, reviewed_stance, reviewed_stride]
  limitation_keys: [projection, timing, tracking, coverage, confounding, kinetics, population, reliability]
  literature_sources: ["running_preece_spine_pelvis_2016", "running_preece_speed_2016"]
  claim_class: evidence_informed_hypothesis
---

# Shoulder–pelvis coordination

## Canonical relationship
`running.rotation.pelvis_thorax` (existing ID preserved).

## Biomechanical principle
Different segment excursions can coexist; amplitude similarity does not establish timing similarity. Investigate the synchronized relationship before assigning a mechanism.

## Evidence and claim separation
Observational association: Preece reports segment coordination. Acceleration management is the authors’ theoretical explanation, not measured fascia or head control.
Sources: [[running_preece_spine_pelvis_2016]], [[running_preece_speed_2016]]. Follow source nodes for DOI/URL, design and audit depth. Experimental effects, observational associations and proposed mechanisms must retain their separate labels.

## Measurable inputs and camera views
- Anatomical segments: thorax, lumbar_spine, pelvis, shoulder_girdle.
- Canonical metric IDs: `running.frontal.shoulder_tilt`, `running.frontal.pelvis_tilt`, `running.frontal.shoulder_centre_offset`.
- Supported views: front, back. Each metric retains its own view: frontal line angles/offsets use front or back, sagittal limb/trunk angles use side. These views are not interchangeable.
- Continuous valid windows need no foot event. Stance-specific comparisons require reviewed contact/toe-off boundaries; stride-specific comparisons require reliable same-foot contacts. Timing/lag is an investigation requirement, not a declaration that it is already implemented.

## Expected or possible relationships
Different segment excursions can coexist; amplitude similarity does not establish timing similarity. Investigate the synchronized relationship before assigning a mechanism. A co-occurrence is a descriptive pattern until compatible evidence supports a mechanism; no required ideal amplitude, sign or phase is imposed.

## Analysis questions
Do shoulder and pelvis tilt move in the same or opposing directions in matched windows? Does the signed lag repeat? Does a side difference remain when duration, coverage and speed are matched?

## Alternative explanations
Possible segmental redistribution; arm strategy; cadence/speed change; curve running; camera yaw; landmark occlusion; unequal sampling. Spine damping is a hypothesis, not a finding from shoulder/pelvis amplitude alone.

## Testable hypotheses and further assessment
Compare paired curves in the same timestamps; then repeat at matched speed/view. If naming right stance, review its contact and toe-off. Test the redistribution hypothesis with multi-segment 3D motion rather than diagnosing spinal dysfunction.

## Structured uncertainty
Resolve `reasoning_contract.limitation_keys` in [[running_measurement_limitations]] only when applicable. Missing synchronized signals block that comparison, not unrelated usable observations. No numerical thresholds are introduced.

## Anatomical and graph links
[[thoracic_spine]], [[lumbar_spine]], [[hip_joint]], [[internal_oblique]], [[external_oblique]], [[running_spiral_line]], [[running_cadence]].
Navigation: [[running_reasoning_retrieval_index]], [[running_research_handoff_audit]].
