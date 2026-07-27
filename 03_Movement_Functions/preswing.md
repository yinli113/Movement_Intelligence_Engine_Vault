---
id: preswing
type: Movement Function
preferred_name: "Preswing (Perry Phase 5)"
aliases: [preswing, pre-swing, toe-off preparation]
short_definition: "The ~50-60% stance phase from opposite foot strike to toe-off, when the limb unloads in preparation for swing; Perry & Burnfield phase 5, cited via Chambers & Sutherland."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [perry_burnfield_gait_analysis, chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [gait_cycle, stance_phase, terminal_stance, initial_swing, second_double_limb_support, gait_observability_boundary]
directly_supported_claims:
  - "Preswing is the ~50-60% stance phase from opposite foot strike to toe-off, when the limb unloads in preparation for swing."
  - "It is phase 5 of the Perry eight-phase model (cited via Chambers & Sutherland)."
app_translation:
  - "A 2D app bounds preswing by opposite foot strike and toe-off and reports an unload/propulsion-prep proxy."
  - "The app must not infer push-off kinetics or muscle activation from the visible period alone."
---

# Preswing (Perry Phase 5)

## Definition

**Preswing** is the ~50-60% stance phase from opposite foot strike to toe-off, when the limb unloads in preparation for [[swing_phase]]. It is phase 5 of the Perry eight-phase model, cited via [[chambers_sutherland_gait_analysis_2002]] (p.2, Table 2). Full Perry & Burnfield text not yet in vault (see [[perry_burnfield_gait_analysis]] caveat).

## Why it matters

It is the weight-transfer-off / propulsion-preparation window, ending stance and beginning swing. Its duration is a 2D-observable descriptor of push-off symmetry.

## Source-derived model

- ~50-60% of the cycle; both feet again on the ground; weight transfers off the soon-to-swing limb.
- Ankle plantarflexes toward toe-off; knee flexion begins.

## Joint involvement

[[ankle_joint]] plantarflexion (toe-off), [[knee_joint]] flexion, [[hip_joint]] extension for propulsion.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Fifth/final phase of [[stance_phase]] (A); follows [[terminal_stance]] (A); transitions into [[initial_swing]] (A); maps to the coarser [[second_double_limb_support]] period (A).

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]] for the full mapping. During preswing the primary loaded lines are:

- [[superficial_back_line]] — plantarflexors of the SBL **plus LL and DFL** complete the catapult (Earls — catapult is multi-line, not SBL-only); toe-off releases the stored elastic energy.
- [[superficial_front_line]] — anterior tissues recoil to assist **hip flexion** into swing (recoil assists hip flexion; it does NOT assist knee flexion — knee flexion in swing is active hamstring + popliteus, not SFL recoil). Short SFL restricts this recoil → stiff-knee swing.
- [[spiral_line]] — anterior SPL assists foot supination prior to toe-off; contralateral arm swing tensions the upper SPL.
- [[deep_front_line]] — psoas/iliacus initiates the swing phase.

These are candidate line roles, not measured tissue loading.

## What a 2D app can observe

- Period bounds (opposite foot strike to toe-off), ankle/knee angle proxies, toe-off event from a 2D side view.

## What the app must not infer

- Push-off kinetics, joint moments, or muscle activation.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[terminal_stance]], [[initial_swing]], [[second_double_limb_support]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).

## Evidence-separation rules

- **(A)** Phase definition, ~50-60%, unload/propulsion-prep role — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[second_double_limb_support]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
