---
id: initial_contact
type: Movement Function
preferred_name: "Initial Contact (Perry Phase 1)"
aliases: [initial contact, foot strike, heel strike]
short_definition: "The instant of foot strike at 0% of the gait cycle that begins the stance phase; Perry & Burnfield phase 1, cited via Chambers & Sutherland."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [perry_burnfield_gait_analysis, chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [gait_cycle, stance_phase, loading_response, initial_double_limb_support, gait_observability_boundary]
directly_supported_claims:
  - "Initial contact is the instant of foot strike at 0% of the gait cycle that begins stance."
  - "It is phase 1 of the Perry eight-phase model (cited via Chambers & Sutherland, which presents Perry's phase nomenclature)."
app_translation:
  - "A 2D app marks initial contact as the foot-strike event that starts the cycle and stance."
  - "The app must not infer heel-strike kinetics or muscle activation from the visible contact event."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 16
hub_score: 32
centrality: 0.143
---

# Initial Contact (Perry Phase 1)

## Definition

**Initial contact** is the instant of foot strike at 0% of the [[gait_cycle]] that begins the [[stance_phase]]. It is phase 1 of the Perry eight-phase model, cited via [[chambers_sutherland_gait_analysis_2002]] (p.2, Table 2), which presents Perry's phase nomenclature. The full Perry & Burnfield text is not yet in the vault (see [[perry_burnfield_gait_analysis]] caveat).

## Why it matters

It is the cycle's zero-point and the start of weight acceptance. Its 2D-observable event (foot down) is the primary anchor for cycle normalisation.

## Source-derived model

- Instant at 0%; the foot meets the ground.
- Begins stance and the loading that follows in [[loading_response]].

## Joint involvement

- **Sagittal (3D instrumented reference):** [[ankle_joint]] near neutral (~0° [[ankle_dorsiflexion]]/plantarflexion), [[knee_joint]] near full extension (~0°–5° [[knee_flexion]]), [[hip_joint]] flexed (~20°–25° [[hip_flexion]]) ([[kadaba_lower_extremity_kinematics_1990]], [[fukuchi_walking_kinematics_dataset_2018]]). Contact can initiate at the heel, midfoot, or forefoot depending on gait pattern.
- **Frontal/Triplanar (3D instrumented reference):** [[subtalar_joint]] typically contacts slightly inverted/supinated (~2°–4° [[ankle_inversion]]) before transitioning into loading pronation ([[leardini_multisegment_foot_kinematics_2007]]).

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

First phase of [[stance_phase]] (A); precedes [[loading_response]] (A); maps to the start of the coarser [[initial_double_limb_support]] period (A).

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]] for the full mapping. At initial contact the primary loaded lines are:

- [[spiral_line]] — anterior portion (tibialis anterior → ITB → upper gluteus max) decelerates the pronation + hip flexion + tibial IR initiated at heel strike.
- [[back_functional_line]] — posterior pelvic sling (glute max → thoracolumbar fascia → contralateral lat) brakes hip flexion/IR.
- [[superficial_back_line]] — begins to engage as the back of the leg takes over into hip extension and plantarflexion.

These are candidate line roles, not measured tissue loading.

## What a 2D app can observe

- The foot-strike event and contact posture (heel, midfoot, or forefoot contact) plus sagittal ankle/knee/hip descriptor proxies from a 2D side view.
- Subtalar pronation/supination is triplanar and **cannot** be measured from a 2D side view ([[leardini_multisegment_foot_kinematics_2007]], [[kadaba_lower_extremity_kinematics_1990]]).

## What the app must not infer

- Heel-strike kinetics, impact force, muscle activation, or triplanar subtalar pronation/supination from 2D side-view landmarks.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[loading_response]], [[initial_double_limb_support]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).
- [[kadaba_lower_extremity_kinematics_1990]] — normative 3D sagittal lower-limb kinematics at initial contact (Level 3).
- [[fukuchi_walking_kinematics_dataset_2018]] — normative walking kinematics dataset (Level 3).
- [[leardini_multisegment_foot_kinematics_2007]] — multi-segment foot / rearfoot alignment at stance onset (Level 3).

## Evidence-separation rules

- **(A)** Phase definition and 0% placement — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[initial_double_limb_support]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
