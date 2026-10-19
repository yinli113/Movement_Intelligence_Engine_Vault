---
id: running_body_proportion_comparison
canonical_id: running.knowledge.body_proportion_comparison
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
domain: running
status: canonical
relationships:
  connects_to: [running_steudel_limb_length_economy_2007, running_larsen_kenyan_danish_anthropometry_2026, running_spataro_kenyan_european_anthropometry_2026, running_reasoning_retrieval_index]
confidence: contextual
review_status: audited
relationship_count: 4
hub_score: 0
centrality: 0.0
updated: 2026-10-16
evidence_paths: [{"claim_id": "running.body_proportion_comparison.limb_length", "measured_observation": "Measured limb proportions, not apparent uncalibrated image length", "proposed_mechanism": "Anthropometry can relate to locomotor economy", "applicable_study": "running_steudel_limb_length_economy_2007", "study_design": "observational_anthropometry_economy", "evidence_scope": "general_biomechanical_principle", "app_measurement_validation": "not_established_by_this_source", "athlete_specific_conclusion": "hypothesis_only", "evidence_limitations": ["Does not test recovery-knee flexion", "Does not establish individual economy from video"]}]

---

# Body proportions as comparison context

## Canonical relationship
`running.knowledge.body_proportion_comparison`.

## Principle and evidence
Relative segment dimensions can be associated with locomotor cost and alter geometric displacement at a given angle; they do not determine an individual's coordination. Observational Level 3 sources: [[running_steudel_limb_length_economy_2007]] (R11), [[running_larsen_kenyan_danish_anthropometry_2026]] (R12), [[running_spataro_kenyan_european_anthropometry_2026]] (R13). Source nodes retain DOI/URLs; audit depth is in [[running_research_handoff_audit]].

## Inputs, segments, phases and views
Segments: thigh, shank, pelvis, trunk. Existing TillYes `running.swing.thigh`, `running.frontal.left_ankle_offset`, `running.frontal.right_ankle_offset` and projected line metrics are descriptive inputs, not direct anthropometry. Actual stature, segment lengths, mass and metabolic cost require independent measurements. Same-view continuous windows can be compared; phase comparisons need reliable events. Side angles and front/back offsets cannot substitute for one another.

## Relationships and questions
Could an apparent displacement difference reflect scale, geometry, speed or body proportions? Does within-runner comparison persist under matched imaging? Lower-leg length alone does not guarantee longer strides or lower cost.

## Alternatives and assessment
Training, selection, speed, shoes, mass distribution, camera yaw and scale can confound between-runner differences. Prefer repeated within-runner recordings; measure anthropometry directly if it is relevant. Ethnicity does not establish individual anatomy or explain an observed asymmetry.

## Structured uncertainty
limitation_keys: [projection, confounding, population, kinetics, coverage]. Resolve in [[running_measurement_limitations]]. Clinical and causal interpretation is not established by the group associations.

Anatomical navigation: [[hip_joint]], [[gluteus_maximus]], [[psoas_major]], [[running_functional_lines]]. Reasoning: [[running_reasoning_retrieval_index]].

