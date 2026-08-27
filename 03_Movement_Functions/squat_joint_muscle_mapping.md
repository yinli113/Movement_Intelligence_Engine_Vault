---
id: squat_joint_muscle_mapping
type: Movement Function
preferred_name: Squat Joint and Muscle Mapping
aliases: [squat anatomical mapping, squat regional contributors]
domain: squat
evidence_level: 4
source_role: engine_synthesis
supported_by: [straub_powers_squat_biomechanics_2024, gray_cook_movement_2010]
status: reviewed_for_app_v1
reviewed_date: 2026-08-27
connects_to: [bodyweight_squat, hip_joint, knee_joint, ankle_joint, lumbar_spine, squat_observability_boundary]
---

# Squat Joint and Muscle Mapping

## Purpose

This node maps camera-observable squat metrics to involved joints and candidate
muscle regions. A candidate region is a question for further assessment, not a
camera-detected impairment.

| Metric or pattern | Primary joints | Candidate muscle regions | Allowed interpretation |
|---|---|---|---|
| Squat depth / peak knee flexion | ankle, knee, hip, pelvis | quadriceps region, gluteus maximus, adductor magnus, hamstrings, soleus, gastrocnemius | Combined lower-limb depth strategy; no single limiting structure can be selected from video. |
| Trunk-tibia angle | hip, knee, trunk | hip extensors, quadriceps region, spinal extensors, abdominal wall | Relative hip-biased, neutral, or knee-biased strategy. |
| Forward trunk inclination | hip and trunk with knee interaction | gluteus maximus, hamstrings, adductor magnus, spinal extensors, abdominal wall | Increased hip/trunk contribution or support demand; not trunk dysfunction. |
| Tibia inclination / heel rise | ankle and knee | soleus, gastrocnemius, tibialis anterior, foot stabilizer regions | Ankle-foot strategy may warrant direct dorsiflexion and foot-position review. |
| Medial knee-to-foot tracking | hip, knee, ankle-foot | gluteal region, adductors, tensor fasciae latae/IT region, deep lower-leg and foot stabilizers | Multi-region frontal-plane strategy; never a weak-glute diagnosis. |
| Pelvic lateral shift | pelvis/hip and bilateral lower limb | gluteus medius region, adductors, quadratus lumborum, obliques | Asymmetric lateral strategy; causal region remains unknown. |
| Trunk lateral shift relative to pelvis | trunk, pelvis, bilateral hip | lateral abdominal wall, quadratus lumborum region, hip abductor/adductor regions | Frontal trunk-pelvis organization; not spinal or hip dysfunction. |
| Left-right frontal contribution difference | bilateral hip, knee, ankle-foot | bilateral quadriceps, gluteal, adductor and calf regions | Side-to-side movement contribution differs in this recording; no weaker side is identified. |
| Repetition variability | whole kinetic chain | none assigned | Repeatability descriptor only; no fatigue or weakness inference. |

## Cross-View Themes

Side and front metrics may be grouped into ankle-foot, trunk-pelvis, depth/frontal
control, and repeatability themes. These are complementary anatomical stories rather
than synchronized kinematic chains. Cross-view agreement raises a question for direct
assessment; it does not identify the responsible joint or muscle.

## Evidence Boundary

- Muscle lists describe anatomical actions and candidate regions involved in the task.
- MediaPipe does not measure activation, force, length, stiffness, or weakness.
- A joint-angle proxy does not establish passive joint range or tissue extensibility.
- Multiple competing contributors must remain visible in the report.

## Vault Quality Note

Several current muscle and joint-action pages are `generated_legacy_needs_review`.
They may support graph navigation, but the squat app export uses region-level language
until standard anatomy and instrumented squat sources are added for each claim.
