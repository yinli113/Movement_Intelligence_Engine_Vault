---
id: terminal_stance
type: Movement Function
preferred_name: "Terminal Stance (Perry Phase 4)"
aliases: [terminal stance, heel-rise phase]
short_definition: "The ~30-50% stance phase from heel-rise to opposite foot strike, when the body rolls over the forefoot and prepares to unload; Perry & Burnfield phase 4, cited via Chambers & Sutherland."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [perry_burnfield_gait_analysis, chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [gait_cycle, stance_phase, mid_stance, preswing, single_limb_stance, gait_observability_boundary]
directly_supported_claims:
  - "Terminal stance is the ~30-50% stance phase from heel-rise to opposite foot strike, when the body rolls over the forefoot."
  - "It is phase 4 of the Perry eight-phase model (cited via Chambers & Sutherland)."
app_translation:
  - "A 2D app bounds terminal stance by heel-rise and opposite foot strike and reports a heel-rise/roll-over proxy."
  - "The app must not infer propulsion kinetics or muscle activation from the visible period alone."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 18
hub_score: 40
centrality: 0.161
---

# Terminal Stance (Perry Phase 4)

## Definition

**Terminal stance** is the ~30-50% stance phase from heel-rise to opposite foot strike, when the body rolls over the forefoot and prepares to unload. It is phase 4 of the Perry eight-phase model, cited via [[chambers_sutherland_gait_analysis_2002]] (p.2, Table 2). Full Perry & Burnfield text not yet in vault (see [[perry_burnfield_gait_analysis]] caveat).

## Why it matters

It is the roll-over / propulsion-preparation window. Heel-rise is a clean 2D-observable event bounding this phase.

## Source-derived model

- ~30-50% of the cycle; heel rises; body advances over the forefoot; the contralateral limb begins its contact.
- Ankle dorsiflexion increases over the forefoot; the knee extends.

## Joint involvement

- **Sagittal (3D instrumented reference):** [[ankle_joint]] reaches peak [[ankle_dorsiflexion]] (~10°) before heel-rise ("forefoot rocker"), [[knee_joint]] reaches full extension (~0°), [[hip_joint]] extends to ~10°–20° [[hip_extension]] behind the pelvis, with metatarsophalangeal extension ([[kadaba_lower_extremity_kinematics_1990]], [[fukuchi_walking_kinematics_dataset_2018]]).
- **Frontal/Triplanar (3D instrumented reference):** [[subtalar_joint]] continues **supinating** (calcaneal [[ankle_inversion]]), locking the midtarsal joint into a rigid propulsive lever prior to push-off ([[leardini_multisegment_foot_kinematics_2007]]).

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Fourth phase of [[stance_phase]] (A); follows [[mid_stance]] (A); precedes [[preswing]] (A); maps to the second part of the coarser [[single_limb_stance]] period (A).

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]] for the full mapping. During terminal stance the primary loaded lines are:

- [[superficial_back_line]] — plantarflexors load the "catapult" as the body rolls over the forefoot and the heel rises.
- [[superficial_front_line]] — anterior tissues are pre-stretched as the hip comes into extension, loading elastic energy for the upcoming swing recoil.
- [[deep_front_line]] — ideally tensions through its entire length (toe extension + ankle DF + knee extension + hip extension/IR/abduction + thoracic extension).
- [[spiral_line]] — anterior portion (TFL/ITB → tibialis anterior) begins assisting foot re-supination prior to toe-off.

These are candidate line roles, not measured tissue loading.

## What a 2D app can observe

- Period bounds (heel-rise to opposite foot strike), heel-rise event, ankle/ knee angle proxies from a 2D side view.

## What the app must not infer

- Propulsion kinetics, joint moments, or muscle activation.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[mid_stance]], [[preswing]], [[single_limb_stance]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).
- [[kadaba_lower_extremity_kinematics_1990]] — normative 3D lower-limb kinematics during terminal stance (Level 3).
- [[fukuchi_walking_kinematics_dataset_2018]] — normative walking kinematics dataset (Level 3).
- [[leardini_multisegment_foot_kinematics_2007]] — multi-segment rearfoot re-supination / rigid-lever mechanics in late stance (Level 3).

## Evidence-separation rules

- **(A)** Phase definition, ~30-50%, roll-over role — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[single_limb_stance]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
