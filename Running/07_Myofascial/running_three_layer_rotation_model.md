---
id: running_three_layer_rotation_model
canonical_id: running.myofascial.three_layer_rotation_model
type: App Logic
running_node_type: myofascial_hypothesis
evidence_level: 5
running_claim_level: D
status: canonical
preferred_name: "Running - Thomas Myers' Three Rotational Systems Model"
aliases: [Three-Layer Rotation Model, Myers 3 Spirals Running, Three Rotational Muscle Systems, Fascial rotational layers]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: true
confidence_required: contextual
related_nodes: []
source_nodes: [myers_three_rotational_systems_2024, anatomy_trains_myofascial_thomas_w_myers, gruenke_kiptum_running_analysis_2023]
relationships:
  required_inputs: [running_altered_rotational_coordination, running_pelvis_thorax_rotation, running_rotational_coupling, running_arm_leg_coordination, running_rotational_reversal, running_left_right_asymmetry]
  supports: [running_functional_lines, running_spiral_line, running_deep_front_line, running_cross_body_myofascial_hypothesis]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_measurement_limitations, running_kinematics_are_not_kinetics]
confidence: medium
review_status: evidence_audited_2026_10_16
relationship_count: 24
hub_score: 46
centrality: 0.22
updated: 2026-10-16
reasoning_contract:
  relationship_id: running.myofascial.three_layer_rotation_model
  anatomical_segments: ["upper_limb", "trunk", "pelvis", "spine", "lower_limb"]
  measurable_metrics: ["running.swing.arm", "running.swing.thigh", "running.frontal.shoulder_tilt", "running.frontal.pelvis_tilt", "running.frontal.head_pelvis_offset"]
  observation_scope: [continuous_window, reviewed_stance, reviewed_stride]
  limitation_keys: [projection, timing, tracking, coverage, confounding, kinetics, population, reliability, tissue]
  literature_sources: ["myers_three_rotational_systems_2024", "anatomy_trains_myofascial_thomas_w_myers"]
  claim_class: theoretical_hypothesis
---

# Myers three rotational systems

## Canonical relationship
`running.myofascial.three_layer_rotation_model` (existing ID preserved).

## Biomechanical principle
Use the outer Functional Lines, middle Spiral Line and inner Deep Front Line as anatomical question-organizing frameworks, not measured functional subsystems.

## Evidence and claim separation
Theoretical anatomical framework: Myers article/course (Level 4 applied exposition; underlying Anatomy Trains Level 1 framework). Running-specific mapping is a Level 5 interpretive hypothesis, not empirical validation.
Sources: [[myers_three_rotational_systems_2024]], [[anatomy_trains_myofascial_thomas_w_myers]]. Follow source nodes for DOI/URL, design and audit depth. Experimental effects, observational associations and proposed mechanisms must retain their separate labels.

## Measurable inputs and camera views
- Anatomical segments: upper_limb, trunk, pelvis, spine, lower_limb.
- Canonical metric IDs: `running.swing.arm`, `running.swing.thigh`, `running.frontal.shoulder_tilt`, `running.frontal.pelvis_tilt`, `running.frontal.head_pelvis_offset`.
- Supported views: side, front, back. Each metric retains its own view: frontal line angles/offsets use front or back, sagittal limb/trunk angles use side. These views are not interchangeable.
- Continuous valid windows need no foot event. Stance-specific comparisons require reviewed contact/toe-off boundaries; stride-specific comparisons require reliable same-foot contacts. Timing/lag is an investigation requirement, not a declaration that it is already implemented.

## Expected or possible relationships
Use the outer Functional Lines, middle Spiral Line and inner Deep Front Line as anatomical question-organizing frameworks, not measured functional subsystems. A co-occurrence is a descriptive pattern until compatible evidence supports a mechanism; no required ideal amplitude, sign or phase is imposed.

## Analysis questions
Outer: does contralateral limb timing differ? Middle: do shoulder/pelvis projected directions and timing differ? Inner: is head/trunk/pelvis relative alignment repeatable? Which independent assessment could distinguish the explanations?

## Alternative explanations
Ordinary individual strategy, speed, camera projection, limb task and tracking failure may explain the same observations without a tissue abnormality.

## Testable hypotheses and further assessment
Start with measured curves; retrieve the corresponding line and muscle nodes as anatomical context. Repeat a matched task or obtain clinical assessment if relevant to the person’s concern. Do not grade fascial function or prescribe tissue treatment from the video.

## Structured uncertainty
Resolve `reasoning_contract.limitation_keys` in [[running_measurement_limitations]] only when applicable. Missing synchronized signals block that comparison, not unrelated usable observations. No numerical thresholds are introduced.

## Anatomical and graph links
[[running_functional_lines]], [[running_spiral_line]], [[running_deep_front_line]], [[functional_lines]], [[spiral_line]], [[deep_front_line]], [[latissimus_dorsi]], [[gluteus_maximus]], [[internal_oblique]], [[external_oblique]], [[psoas_major]], [[multifidus]].
Navigation: [[running_reasoning_retrieval_index]], [[running_research_handoff_audit]].
