---
id: squat_myofascial_mapping
type: Movement Function
preferred_name: Squat Myofascial Mapping
aliases: [squat fascial-line interpretation, Anatomy Trains squat mapping, squat switch failure taxonomy]
domain: squat
evidence_level: 5
source_role: engine_synthesis
supported_by: [anatomy_trains_myofascial_thomas_w_myers, straub_powers_squat_biomechanics_2024, kuljian_gmoneymvmt_hip_ir_squat_correlation]
status: reviewed_engine_synthesis
reviewed_date: 2026-08-29
connects_to: [bodyweight_squat, myofascial_interpretive_layer, superficial_back_line, superficial_front_line, deep_front_line, lateral_line, spiral_line, squat_switch_failure_modes]
relationships:
  parent_concepts: [bodyweight_squat]
  child_concepts: [superficial_back_line, superficial_front_line, deep_front_line, lateral_line, spiral_line, squat_switch_failure_modes]
  related_concepts: [squat_joint_muscle_mapping, squat_observability_boundary, gluteus_maximus, gluteus_medius, adductor_magnus, tensor_fasciae_latae, serratus_anterior, tibialis_posterior]
confidence: medium
review_status: source_checked_app_translation_unvalidated
relationship_count: 23
hub_score: 88
centrality: 0.205
---

# Squat Myofascial Mapping: Assessment Hypotheses

## Evidence status

Anatomy Trains supplies an anatomical continuity framework. Every squat-pattern-to-line association here is Level 5 `engine_synthesis`, not a validated tissue-state classifier. The former 21-misalignment matrix and deterministic express/local failure explanations are withdrawn. Their replacement preserves regional assessment questions without declaring inhibition, overactivity, restriction or a treatment requirement.

Read [[squat_joint_muscle_mapping]], [[squat_observability_boundary]], [[squat_article_app_contract]] and [[squat_switch_failure_modes]] before translating these relationships into a report. [[wilke_myofascial_chains_review_2016]] concerns anatomical continuity, not validation of these squat hypotheses.

## Structured relationship blocks

Each row follows observed pattern → why a line is considered → muscle-to-line relationship → potential clinical issues → direct assessment/retest → camera boundary. Candidate lines are overlapping alternatives, never a count of damaged lines.

| Observed pattern | Why consider a line | Muscle-to-line relationship | Questions/competing explanations | Direct assessment/retest | Camera boundary |
|---|---|---|---|---|---|
| Visible heel rise | SBL / DFL | calf and deep lower-leg regions | ankle task strategy, footwear, depth and tracking | Compare directly assessed ankle motion and comfortable recorded heel conditions | Heel rise does not identify a short calf or Achilles block. |
| Knee moves toward/away from foot in front view | DFL / LL / SPL | adductor, gluteal, lateral thigh and foot regions | stance, camera yaw, active control and available joint motion | Review the original front trajectory; compare comfortable stance trials | Projected knee-to-foot excursion is not a valgus angle, activation or hip IR measurement. |
| Pelvis shifts laterally | LL / DFL | hip abductor/adductor, lateral trunk and pelvic regions | whole-body translation, stance, symptoms and tracking | Compare supported and original tasks at similar depth/tempo if appropriate | No weak glute, QL overactivity or unilateral tissue cause is established. |
| Trunk shifts relative to pelvis | LL / SPL | oblique and shoulder-girdle continuities | relative trunk/pelvis strategy and camera movement | Inspect simultaneous common-reference trajectories before comparing directions | Independent peaks cannot establish simultaneous counter-shift or rotation. |
| Trunk–tibia relation at selected depth | SBL / SFL | hip/knee extensor and trunk regions | segment proportions, depth, stance and load | Review same-frame projected angles and recorded task conditions | Apparent strategy is not joint moment, shear, muscle dominance or injury risk. |
| Head/shoulder translation | SBL / DFL / SPL | neck-region and shoulder-girdle continuities | gaze, arm task, trunk travel and tracking | Review relative trajectories and examine the region directly if relevant | Landmarks do not isolate cervical motion, thoracic curvature or scapular winging. |
| Foot arch, pelvic tilt or axial rotation question | Direct examination first | region selected by clinical history and examination | anatomy, task strategy and symptoms | Use an appropriate direct assessment before choosing a line hypothesis | Ordinary front/side landmarks do not establish these 3D or segmental states. |

These regional relationships guide questions only. Passive mobility, muscle strength/activity, tissue state and symptoms require their own assessment. A comfortable wedge, load, support or stance comparison records a task response; it does not confirm a line-specific cause. No fixed release/activate prescription follows from a camera trigger. Preserve raw trajectories and uncertainty rather than using a hypothesis to replace a measurement.

## Export contract — 2026-10-28

`squat_knowledge.v1.json` v1.4.0 retains regional rationale, competing explanations and bounded retest prompts. It removes deterministic switch-failure, inhibited/overactive muscle lists, automatic palpation targets and release/activate/integrate prescriptions from camera-generated notes. Existing saved reports are not rewritten. The clinical display and report JSON must use the same current contract.

## Repeated multiregion squat translation — 2026-09-30

This app policy is Level 5 `engine_synthesis`, not an anatomical-source claim that
a squat shift diagnoses any line. In a single phase of a repetition, head, pelvis
and at least one named foot must simultaneously exceed their own noise-adjusted
displacement thresholds in the same screen direction for at least 150 ms, with
no missing data or gaps over 200 ms in that interval. Match the same foot, direction
and phase across at least two repetitions and at least half of all completed
repetitions. Report the supporting repetition numbers and absolute timestamps.
Unavailable recordings are not negative evidence; counts use all completed reps
conservatively and disclose tracking limitations. Do not combine independent peaks
or separate camera views to invent a chain.

The result can surface Lateral Line, Deep Front Line and Spiral Line as concurrent
assessment candidates. Lateral translation provides the closest descriptive context
for LL. DFL is a deep-medial support differential, not limited to medial knee motion.
SPL is a less-specific cross-body differential: translation alone does not establish
rotation. Seek independent rotational evidence before a rotation-specific account.
Whole-body translation, camera movement, stance strategy and tracking artefacts remain
competing explanations. None of these observations measures line damage, restriction,
weakness, activation, tension, causality, or a need for treatment.

Clinical display must connect observations to candidate rationale, muscle-to-line
relationships, assessment questions, retest and camera limits. Untriggered lines
are not confirmed balanced or normal. No synthetic score, inhibited/overactive
label, or fixed treatment prescription may substitute for measured evidence.
The synchronized JSON `multiRegionClinicalContract` owns the app wording.
