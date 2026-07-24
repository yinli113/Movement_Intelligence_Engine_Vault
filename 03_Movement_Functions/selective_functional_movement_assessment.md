---
id: selective_functional_movement_assessment
type: Movement Function
preferred_name: "Selective Functional Movement Assessment (SFMA)"
aliases: [SFMA, SFMA top-tier, SFMA breakouts]
short_definition: "A clinical, pain-present movement assessment using FN/FP/DP/DN classification and mobility-vs-stability breakouts; the clinical counterpart to the FMS screen."
domain: general_movement
evidence_level: 2
source_role: foundational_movement_framework
supported_by: [gray_cook_movement_2010]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [functional_movement_screen, joint_by_joint_concept, mobility_stability_relationship, regional_interdependence]
directly_supported_claims:
  - "SFMA is a clinical assessment used when pain is present, distinct from the non-clinical FMS screen."
  - "Each top-tier test is classified FN, FP, DP, or DN (Functional/Non-functional x Painful/Non-painful)."
  - "DN and DP findings are broken out to separate mobility problems from stability/motor-control problems."
app_translation:
  - "Use SFMA's FN/FP/DP/DN logic as the clinical-redirect model: a 2D app can flag a painful or non-functional pattern but must hand off to a clinician for breakouts."
  - "The app must not perform SFMA breakouts or assign mobility-vs-stability diagnoses from video."
---

# Selective Functional Movement Assessment (SFMA)

## Definition

The Selective Functional Movement Assessment is a **clinical, pain-present** movement assessment. Each top-tier test is classified **FN / FP / DP / DN** (Functional or Non-functional x Painful or Non-painful), and DN/DP findings are broken out to separate **mobility** problems from **stability / motor-control** problems (Gray Cook, *Movement*, Ch. 7-8).

## Why it matters

SFMA is the clinical counterpart to the [[functional_movement_screen]]. It defines the engine's **screen-vs-assessment** boundary: a screen sorts and flags; an assessment diagnoses and breaks out. This boundary governs when the app must redirect to a qualified clinician rather than continue.

## Source-derived model

- Seven top-tier assessments: cervical, upper extremity, multi-segmental flexion, multi-segmental extension, multi-segmental rotation, single-leg stance, overhead deep squat.
- Four-result classification: FN, FP, DP, DN.
- Breakouts separate mobility (tissue extensibility / joint range) from stability (motor control).

## Joint involvement

Cervical, shoulder, [[lumbar_spine]], [[thoracic_spine]], [[hip_joint]], [[knee_joint]], [[ankle_joint]] across the top-tier tests.

## Muscle involvement

SFMA breakouts identify mobility vs motor-control problems, not specific muscle diagnoses. Muscle-level conclusions are clinical and out of scope for a 2D app.

## Movement or phase relationships

SFMA operationalises the [[mobility_stability_relationship]] (A) and [[regional_interdependence]] (A) principles: a deficit in one region is probed via breakouts elsewhere.

## Possible myofascial relationships

None directly from this source. Linking SFMA breakouts to fascial lines is an engine synthesis (C).

## What a 2D app can observe

- Whether a top-tier pattern is functional or non-functional from a 2D view.
- A pain flag if the user reports pain.

## What the app must not infer

- The FN/FP/DP/DN breakout itself (requires hands-on clinical assessment).
- Mobility-vs-stability diagnosis.
- Pain source, pathology, or treatment.

## Related concepts

[[functional_movement_screen]], [[mobility_stability_relationship]], [[regional_interdependence]], [[joint_by_joint_concept]], [[performance_pyramid]].

## Sources

- [[gray_cook_movement_2010]] — Ch. 7-8.

## Evidence-separation rules

- **(A)** FN/FP/DP/DN classification, top-tier list, mobility-vs-stability breakouts — directly from Gray Cook.
- **(B)** Cross-links to [[mobility_stability_relationship]], [[regional_interdependence]] — same Level 1 source.
- **(C)** Any fascial-line mapping of an SFMA breakout is `engine_synthesis` and must be labelled.
