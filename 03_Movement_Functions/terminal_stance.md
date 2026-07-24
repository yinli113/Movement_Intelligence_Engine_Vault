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

[[ankle_joint]] dorsiflexion over forefoot, [[knee_joint]] extension, [[hip_joint]] extension, metatarsophalangeal (toe) joint loading.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Fourth phase of [[stance_phase]] (A); follows [[mid_stance]] (A); precedes [[preswing]] (A); maps to the second part of the coarser [[single_limb_stance]] period (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Period bounds (heel-rise to opposite foot strike), heel-rise event, ankle/ knee angle proxies from a 2D side view.

## What the app must not infer

- Propulsion kinetics, joint moments, or muscle activation.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[mid_stance]], [[preswing]], [[single_limb_stance]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).

## Evidence-separation rules

- **(A)** Phase definition, ~30-50%, roll-over role — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[single_limb_stance]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
