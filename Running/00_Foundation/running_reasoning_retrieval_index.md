---
id: running_reasoning_retrieval_index
canonical_id: running.knowledge.reasoning_retrieval_index
type: App Logic
running_node_type: index
evidence_level: 5
domain: running
status: canonical
relationships:
  connects_to: [running_pelvis_thorax_rotation, running_arm_leg_coordination, running_cadence, running_head_trunk_pelvis_coordination, running_three_layer_rotation_model, running_running_economy, running_body_proportion_comparison, running_research_handoff_audit, running_measurement_limitations]
confidence: contextual
review_status: audited
relationship_count: 9
hub_score: 0
centrality: 0.0
updated: 2026-10-16
---

# Running observation-to-knowledge retrieval

Use the established graph traversal: measured observation → relationship node → source nodes/design → competing hypotheses → discriminating assessment. A link is navigation, not proof. Keep the observation separate from the explanation.

## Retrieval routes

| Query / observation terms | Primary relationship nodes | Supporting sources | Conditional limitations |
|---|---|---|---|
| Why might pelvic excursion differ between left and right stance? Pelvis tilt, shoulder symmetry, phase lag | [[running_pelvis_thorax_rotation]], [[running_cadence]] | [[running_preece_spine_pelvis_2016]], [[running_preece_speed_2016]], [[running_mesquita_step_frequency_pelvis_2024]] | timing, projection, coverage, tracking, confounding |
| How might arm swing relate to shoulder and pelvis coordination? Contralateral, compact arm, elbow | [[running_arm_leg_coordination]], [[running_pelvis_thorax_rotation]] | [[running_arellano_arm_swing_2014]], [[running_preece_spine_pelvis_2016]] | projection, timing, confounding, kinetics |
| How can the three rotational systems help investigate running asymmetry? Myers, outer, middle, inner | [[running_three_layer_rotation_model]] → [[running_functional_lines]], [[running_spiral_line]], [[running_deep_front_line]] | [[myers_three_rotational_systems_2024]], [[anatomy_trains_myofascial_thomas_w_myers]] | tissue, projection, timing |
| Head sway, shoulder translation, pelvic-center excursion, repeatability | [[running_head_trunk_pelvis_coordination]] | [[running_vellucci_sprint_coordination_2025]], [[running_morley_lumbar_restriction_2019]] | projection, kinetics, coverage, population |
| Economy, bounce, body proportions, unusually large motion | [[running_running_economy]], [[running_body_proportion_comparison]] | [[running_van_hooren_economy_2024]], [[running_halvorsen_vertical_frequency_2012]], [[running_steudel_limb_length_economy_2007]] | kinetics, confounding, population |

## Return contract for the retrieving agent
Return canonical relationship ID; measured inputs actually available; source ID + DOI/URL + evidence level + study design + verification depth; possible relationship; alternatives; missing synchronized measures; a testable question; a discriminating further assessment; only applicable limitations from [[running_measurement_limitations]]. Never return a bibliography without the reasoning bridge. Exact runtime IDs are distinct from proposed derived comparisons. Do not claim the app already computes an unimplemented lag/arm-relative metric.

## Continuous windows and outliers
Foot events are needed for phase-labelled claims, not continuous co-variation. With uncertain contacts, return valid same-camera time-window observations and withhold stance labels. A high value alone is not an outlier: check geometry, tracking, identity and camera changes. Keep raw values and exclusion reasons; robust medians and sensitivity comparisons can assess influence without inventing physiological thresholds. This is a knowledge rule, not a change to app filtering.

## Validation: three requested queries
The three first table rows were traversed to their relationship, source and limitation nodes on 2026-10-16. Result payloads:

1. Pelvic asymmetry → `running.rotation.pelvis_thorax` and `running.rhythm.cadence`; R02/R03 observational/group evidence and R05 experimental evidence (Level 3); app explanation Level 5. Return synchronized shoulder/pelvis curves, reliable stance boundaries, speed/cadence context, visibility and sample counts. Alternatives: different segment strategy, arm task, cadence, camera yaw, unequal sampling. Do not return hip weakness as a finding.
2. Arm query → `running.rotation.arm_leg_coordination`; R01 Level 3 controlled restriction experiment; altered torso/pelvis motion as experimentally supported relationship, individual compensation as hypothesis. Request separate upper-arm excursion and elbow posture plus matched synchronized signals. No “compact arms cause inefficiency” conclusion.
3. Three-system query → `running.myofascial.three_layer_rotation_model`; R14/R15 applied anatomical framework and foundational Anatomy Trains, running application Level 5. Return outer contralateral timing, middle segment relationship, inner alignment questions with tissue limitation. No measured fascial function score.

## Demonstrated observation-to-knowledge example
Input (hypothetical, not a new result from the user's video): greater pelvic-line excursion in right stance, similar shoulder-line excursions on both sides.

Retrieved: [[running_pelvis_thorax_rotation]] → [[running_preece_spine_pelvis_2016]] (DOI 10.1016/j.humov.2015.11.014, Level 3 observational kinematics); secondary [[running_cadence]] → [[running_mesquita_step_frequency_pelvis_2024]] (DOI 10.1123/jab.2024-0016, Level 3 manipulation experiment).

Reasoning: similar shoulder amplitudes do not establish identical shoulder timing or a rigid torso. Ask whether simultaneous signed shoulder/pelvis curves and relative offsets differ reproducibly, after checking right/left event validity, speed, coverage and camera projection. Segmental redistribution is one hypothesis; arm strategy, cadence, camera yaw and tracking imbalance are alternatives. Repeat matched-camera observations; use 3D multi-segment measurements if testing spinal motion specifically. Neither spinal damping, hip weakness, fascial tension nor economy follows from the amplitude difference alone.

Validation scope: graph-level retrieval by an agent using the existing navigation convention, not an end-to-end runtime AI-engine benchmark. No callable runtime retriever was found in the active vault; no new architecture was installed.

[[running_research_handoff_audit]], [[running_canonical_knowledge_index]].


## Claim-level applicability contract — 2026-10-19
Every research-backed output statement must return a claim-level chain:
**Measured observation → proposed mechanism → applicable study → evidence limitations.**
Use additive `evidence_paths` records on existing relationship nodes. Required fields: claim_id, measured_observation (metric, phase/view and provenance in the actual response), proposed_mechanism, applicable_study (resolvable source ID), study_design, evidence_scope, app_measurement_validation, athlete_specific_conclusion, evidence_limitations.

A general-principle paper does not validate the app's algorithm. App-measurement validation requires an explicit comparison of this measurement/version against a reference method and applicable conditions. An athlete-specific conclusion requires this athlete's relevant evidence; a citation alone cannot supply it. Preserve experimental findings, observational associations, review synthesis and hypotheses as different claim classes. If no applicable source is found, label the mechanism unsupported or omit it; do not borrow a nearby citation. Source evidence level and app claim level remain separate.

| Retrieval question | Relationship → source | Required boundary |
|---|---|---|
| Does recovery-knee folding lower swing-leg inertia? | [[running_swing_knee_inertia]] → [[running_van_oeveren_running_styles_synthesis]] | General synthesis; no individual effort or app validation |
| Does restricting arm swing alter shoulder/pelvis motion? | [[running_arm_leg_coordination]] → [[running_arellano_arm_swing_2014]] | Controlled axial-rotation experiment; frontal tilt is a different measurement |
| Does leg length relate to running economy? | [[running_body_proportion_comparison]] → [[running_steudel_limb_length_economy_2007]] | Anthropometry/economy association; not a knee-flexion experiment |

Migration scope: these three chains are populated and checked. Other legacy claims must satisfy this contract when retrieved; this is not a claim that every source in the vault has been re-audited.

## Running literature audit — 2026-10-19
All 35 Running literature nodes reviewed for source identity and claim scope: [[running_literature_claim_audit_2026_10_19]]. Source-specific `claim_audit` records distinguish verification depth, applicability and unestablished app validation.
