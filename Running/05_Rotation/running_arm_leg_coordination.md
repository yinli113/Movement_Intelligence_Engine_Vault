---
id: running_arm_leg_coordination
canonical_id: running.rotation.arm_leg_coordination
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: "Running - Arm Leg Coordination and Pendulum Dynamics"
aliases: [Arm Leg Coordination, Contralateral arm swing, Arm-trunk-pelvis coordination, Elbow flexion and arm swing]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_arellano_arm_swing_2014, running_movaia_kiptum_running_form_2023, running_pontzer_arm_swing_2009]
relationships:
  required_inputs: [running_shoulder_rotation, running_running_cycle, running_initial_contact, running_toe_off, running_variability]
  supports: [running_cross_body_coordination, running_altered_rotational_coordination, running_functional_lines]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_measurement_limitations, running_kinematics_are_not_kinetics]
confidence: high
review_status: evidence_audited_2026_10_16
relationship_count: 18
hub_score: 32
centrality: 0.16
updated: 2026-10-16
reasoning_contract:
  relationship_id: running.rotation.arm_leg_coordination
  anatomical_segments: ["upper_arm", "forearm", "thorax", "pelvis", "thigh"]
  measurable_metrics: ["running.swing.arm", "running.swing.thigh", "running.trunk.lean", "running.frontal.shoulder_tilt", "running.frontal.pelvis_tilt"]
  observation_scope: [continuous_window, reviewed_stance, reviewed_stride]
  limitation_keys: [projection, timing, tracking, coverage, confounding, kinetics, population, reliability]
  literature_sources: ["running_arellano_arm_swing_2014", "running_movaia_kiptum_running_form_2023"]
  claim_class: evidence_informed_hypothesis
evidence_paths: [{"claim_id": "running.rotation.arm_leg_coordination", "measured_observation": "Synchronized arm and opposite-leg motion; shoulder/pelvis motion in its measured plane", "proposed_mechanism": "Arm task may alter torso/pelvis coordination", "applicable_study": "running_arellano_arm_swing_2014", "study_design": "controlled_restriction_experiment", "evidence_scope": "general_biomechanical_principle", "app_measurement_validation": "not_established_by_this_source", "athlete_specific_conclusion": "hypothesis_only", "evidence_limitations": ["Artificial restriction differs from natural arm swing", "Axial rotation is not frontal tilt", "Compensation is an interpretation; individual causation is not demonstrated"]}]

---

# Arm–trunk–pelvis coordination

## Canonical relationship
`running.rotation.arm_leg_coordination` (existing ID preserved).

## Biomechanical principle
Upper-limb task and torso/pelvis motion can interact; elbow flexion and upper-arm excursion are separate quantities.

## Evidence and claim separation
Experimental finding: artificial arm restrictions altered axial motion and metabolic cost. A compensation mechanism in an unrestrained individual remains a testable hypothesis. Movaia is Level 4 case commentary.
Sources: [[running_arellano_arm_swing_2014]], [[running_movaia_kiptum_running_form_2023]]. Follow source nodes for DOI/URL, design and audit depth. Experimental effects, observational associations and proposed mechanisms must retain their separate labels.

## Measurable inputs and camera views
- Anatomical segments: upper_arm, forearm, thorax, pelvis, thigh.
- Canonical metric IDs: `running.swing.arm`, `running.swing.thigh`, `running.trunk.lean`, `running.frontal.shoulder_tilt`, `running.frontal.pelvis_tilt`.
- Supported views: side, front, back. Each metric retains its own view: frontal line angles/offsets use front or back, sagittal limb/trunk angles use side. These views are not interchangeable.
- Continuous valid windows need no foot event. Stance-specific comparisons require reviewed contact/toe-off boundaries; stride-specific comparisons require reliable same-foot contacts. Timing/lag is an investigation requirement, not a declaration that it is already implemented.

## Expected or possible relationships
Upper-limb task and torso/pelvis motion can interact; elbow flexion and upper-arm excursion are separate quantities. A co-occurrence is a descriptive pattern until compatible evidence supports a mechanism; no required ideal amplitude, sign or phase is imposed.

## Analysis questions
Does contralateral upper-arm/thigh timing repeat? Is apparent compactness elbow posture or reduced upper-arm excursion? Do torso and pelvis changes coincide with arm changes in synchronized observations?

## Alternative explanations
Elbow posture, carrying objects, speed, preferred arm strategy, unequal visibility, perspective and contralateral leg timing. Natural compact swing is not equivalent to experimental restraint.

## Testable hypotheses and further assessment
Inspect both arms at matched speed, with side footage for sagittal swing and synchronized front/back footage for line tilts. Current upper-arm metric is referenced to vertical, not automatically trunk-relative; derive an explicit aligned difference only if supported. Elbow angle and wrist-path channels are additional assessment needs, not asserted implemented metrics.

## Structured uncertainty
Resolve `reasoning_contract.limitation_keys` in [[running_measurement_limitations]] only when applicable. Missing synchronized signals block that comparison, not unrelated usable observations. No numerical thresholds are introduced.

## Anatomical and graph links
[[shoulder_joint]], [[latissimus_dorsi]], [[pectoralis_major]], [[gluteus_maximus]], [[running_functional_lines]], [[running_cross_body_coordination]].
Navigation: [[running_reasoning_retrieval_index]], [[running_research_handoff_audit]].
