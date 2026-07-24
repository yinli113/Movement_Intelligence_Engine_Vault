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

[[ankle_joint]] plantarflexion, [[knee_joint]] flexion (shock absorption), [[hip_joint]] extension moment.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Second phase of [[stance_phase]] (A); follows [[initial_contact]] (A); maps to the coarser [[initial_double_limb_support]] period (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Period bounds (initial contact to opposite toe-off), knee-flexion proxy, foot contact pattern from a 2D side view.

## What the app must not infer

- Shock-absorption kinetics, joint moments, or muscle activation.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[initial_contact]], [[mid_stance]], [[initial_double_limb_support]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).

## Evidence-separation rules

- **(A)** Phase definition, ~0-10%, weight-acceptance role — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[initial_double_limb_support]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
