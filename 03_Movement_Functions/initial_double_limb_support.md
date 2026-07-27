---
id: initial_double_limb_support
type: Movement Function
preferred_name: "Initial Double-Limb Support"
aliases: [loading response, initial double support]
short_definition: "The first stance period, from foot strike to opposite toe-off (~0-10% of the gait cycle), when both feet are on the ground and weight is transferred onto the new stance limb."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [stance_phase, gait_cycle, gait_observability_boundary]
directly_supported_claims:
  - "Initial double-limb support runs from foot strike to opposite toe-off (~0-10% of the cycle)."
  - "Both feet are on the ground and weight is transferred onto the new stance limb."
app_translation:
  - "A 2D app can bound this period by the foot-strike and opposite toe-off events."
  - "The app must not infer shock-absorption kinetics or muscle activation from the visible period alone."
---

# Initial Double-Limb Support

## Definition

**Initial double-limb support** is the first stance period, from foot strike to opposite toe-off (~0-10% of the [[gait_cycle]]), when both feet are on the ground and weight is transferred onto the new stance limb (Chambers & Sutherland, p.2).

## Why it matters

It is the weight-acceptance / shock-absorption window. Its duration is a 2D-observable descriptor of loading symmetry.

## Source-derived model

- Bounded by foot strike (0%) and opposite toe-off (~10%).
- Both limbs loaded; transition of weight to the new stance limb.

## Joint involvement

[[ankle_joint]] plantarflexion to foot-flat, [[knee_joint]] flexion for shock absorption, [[hip_joint]] extension moment.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

First period of [[stance_phase]] (A). In the Perry eight-phase taxonomy (cited via [[perry_burnfield_gait_analysis]]), this period corresponds to [[initial_contact]] + [[loading_response]].

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]]. Initial double-limb support (heel strike to opposite toe-off) loads [[spiral_line]] and [[back_functional_line]] for rotational/flexion braking, and [[superficial_front_line]] anterior tissues lengthen / elastically load for shock absorption (muscle action often isometric per Earls' SSC framing, not eccentric). Candidate-line map, not measured tissue loading.

## What a 2D app can observe

- Foot-strike and opposite toe-off events bounding the period; knee flexion proxy.

## What the app must not infer

- Shock-absorption kinetics, joint moments, or muscle activation.

## Related concepts

[[stance_phase]], [[gait_cycle]], [[single_limb_stance]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Period bounds and weight-transfer role — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[stance_phase]], [[gait_cycle]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
