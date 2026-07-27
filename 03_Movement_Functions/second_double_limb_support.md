---
id: second_double_limb_support
type: Movement Function
preferred_name: "Second Double-Limb Support (Preswing)"
aliases: [preswing, terminal double support, second double support]
short_definition: "The final stance period (~50-62% of the gait cycle), from opposite foot strike to toe-off, when both feet are again on the ground and the limb prepares to swing."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [stance_phase, swing_phase, gait_cycle, gait_observability_boundary]
directly_supported_claims:
  - "Second double-limb support (preswing) runs from opposite foot strike to toe-off (~50-62% of the cycle)."
  - "Both feet are on the ground and the limb unloads in preparation for swing."
app_translation:
  - "A 2D app can bound this period by opposite foot strike and toe-off."
  - "The app must not infer push-off kinetics or muscle activation from the visible period alone."
---

# Second Double-Limb Support (Preswing)

## Definition

**Second double-limb support (preswing)** runs from opposite foot strike to toe-off (~50-62% of the [[gait_cycle]]), when both feet are again on the ground and the limb unloads to prepare for [[swing_phase]] (Chambers & Sutherland, p.2).

## Why it matters

It is the weight-transfer-off / propulsion-preparation window. Its duration is a 2D-observable descriptor of push-off symmetry.

## Source-derived model

- Bounded by opposite foot strike (~50%) and toe-off (~62%).
- Both limbs loaded; weight transfers off the soon-to-swing limb.

## Joint involvement

[[ankle_joint]] plantarflexion (toe-off), [[knee_joint]] flexion, [[hip_joint]] extension for propulsion.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Final period of [[stance_phase]] (A); transitions into [[swing_phase]] (A). In the Perry eight-phase taxonomy (cited via [[perry_burnfield_gait_analysis]]), this period corresponds to [[preswing]].

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]]. Second double-limb support (opposite foot strike to toe-off) loads [[superficial_back_line]] for the propulsive catapult, [[spiral_line]] for foot re-supination, and [[superficial_front_line]] for the pre-swing elastic pre-stretch. Candidate-line map, not measured tissue loading.

## What a 2D app can observe

- Opposite foot strike and toe-off events bounding the period; ankle/knee angle proxies.

## What the app must not infer

- Push-off kinetics, joint moments, or muscle activation.

## Related concepts

[[stance_phase]], [[swing_phase]], [[gait_cycle]], [[initial_double_limb_support]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Period bounds and unload/propulsion-prep role — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[stance_phase]], [[swing_phase]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
