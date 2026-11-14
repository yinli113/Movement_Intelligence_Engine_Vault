---
id: loading_response
type: Movement Function
preferred_name: "Loading Response (Perry Phase 2)"
aliases: [loading response, weight acceptance]
short_definition: "The ~0-10% stance phase of weight acceptance and shock absorption, with both feet on the ground; Perry & Burnfield phase 2, cited via Chambers & Sutherland."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [perry_burnfield_gait_analysis, chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [gait_cycle, stance_phase, initial_contact, mid_stance, initial_double_limb_support, gait_observability_boundary]
directly_supported_claims:
  - "Loading response is the ~0-10% stance phase of weight acceptance and shock absorption with both feet on the ground."
  - "It is phase 2 of the Perry eight-phase model (cited via Chambers & Sutherland)."
app_translation:
  - "A 2D app bounds loading response by initial contact and opposite toe-off and reports a knee-flexion shock-absorption proxy."
  - "The app must not infer shock-absorption kinetics or muscle activation from the visible period alone."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 19
hub_score: 43
centrality: 0.17
---

# Loading Response (Perry Phase 2)

## Definition

**Loading response** is the ~0-10% stance phase of weight acceptance and shock absorption, with both feet on the ground. It is phase 2 of the Perry eight-phase model, cited via [[chambers_sutherland_gait_analysis_2002]] (p.2, Table 2). Full Perry & Burnfield text not yet in vault (see [[perry_burnfield_gait_analysis]] caveat).

## Why it matters

It is the weight-acceptance / shock-absorption window. Its duration is a 2D-observable descriptor of loading symmetry.

## Source-derived model

- ~0-10% of the cycle; both limbs loaded; transition of weight onto the new stance limb.
- Knee flexion absorbs shock; ankle plantarflexes to foot-flat.

## Joint involvement

- **Sagittal (3D instrumented reference):** [[ankle_joint]] rapidly [[ankle_plantarflexion|plantarflexes]] (~5°–10°) to foot-flat ("heel rocker"), [[knee_joint]] flexes (~15°–20° [[knee_flexion]]) for shock absorption, [[hip_joint]] stabilizes at ~20° flexion moving toward extension ([[kadaba_lower_extremity_kinematics_1990]], [[fukuchi_walking_kinematics_dataset_2018]]).
- **Frontal/Triplanar (3D instrumented reference):** [[subtalar_joint]] rapidly **pronates** (calcaneal [[ankle_eversion]], ~4°–8° excursion), unlocking the midtarsal joint to act as a flexible shock absorber and terrain adapter ([[leardini_multisegment_foot_kinematics_2007]]).

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Second phase of [[stance_phase]] (A); follows [[initial_contact]] (A); maps to the coarser [[initial_double_limb_support]] period (A).

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]] for the full mapping. During loading response the primary loaded lines are:

- [[superficial_front_line]] — anterior tissues lengthen / elastically load (quadriceps take up the ~15° knee-flexion shock absorption; muscle action often isometric per Earls' SSC framing, not eccentric). Short SFL restricts this knee flexion.
- [[spiral_line]] — continues decelerating pronation/IR via the anterior SPL; the upper gluteus max sling brakes hip flexion.
- [[back_functional_line]] — posterior sling braking continues.
- [[superficial_back_line]] — begins taking over as the leg engages into hip extension and plantarflexion.

These are candidate line roles, not measured tissue loading.

## What a 2D app can observe

- Period bounds (initial contact to opposite toe-off), sagittal knee-flexion shock-absorption proxy, sagittal ankle plantarflexion toward foot-flat, and foot contact pattern from a 2D side view.
- Subtalar pronation (calcaneal eversion) is triplanar and **cannot** be measured from a 2D side view; posterior/anterior views can only observe coarse rearfoot eversion or arch-drop proxies ([[leardini_multisegment_foot_kinematics_2007]], [[kadaba_lower_extremity_kinematics_1990]]).

## What the app must not infer

- Shock-absorption kinetics, joint moments, muscle activation, or triplanar subtalar pronation from 2D side-view landmarks.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[initial_contact]], [[mid_stance]], [[initial_double_limb_support]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).
- [[kadaba_lower_extremity_kinematics_1990]] — normative 3D sagittal lower-limb kinematics during loading response (Level 3).
- [[fukuchi_walking_kinematics_dataset_2018]] — normative walking kinematics dataset (Level 3).
- [[leardini_multisegment_foot_kinematics_2007]] — multi-segment rearfoot eversion / pronation during early stance (Level 3).

## Evidence-separation rules

- **(A)** Phase definition, ~0-10%, weight-acceptance role — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[initial_double_limb_support]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
