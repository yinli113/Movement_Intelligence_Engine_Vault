---
id: mid_stance
type: Movement Function
preferred_name: "Mid Stance (Perry Phase 3)"
aliases: [mid-stance, midstance]
short_definition: "The ~10-30% stance phase of single-limb support when the body passes over the stationary foot; Perry & Burnfield phase 3, cited via Chambers & Sutherland."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [perry_burnfield_gait_analysis, chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [gait_cycle, stance_phase, loading_response, terminal_stance, single_limb_stance, gait_observability_boundary]
directly_supported_claims:
  - "Mid stance is the ~10-30% stance phase of single-limb support when the body passes over the stationary foot."
  - "It is phase 3 of the Perry eight-phase model (cited via Chambers & Sutherland)."
app_translation:
  - "A 2D app bounds mid stance by opposite toe-off and heel-rise and reports single-leg balance proxies (pelvic level, trunk sway)."
  - "The app must not infer single-leg stability as a measured kinetic or muscle-activation variable."
---

# Mid Stance (Perry Phase 3)

## Definition

**Mid stance** is the ~10-30% stance phase of single-limb support when the body passes over the stationary foot. It is phase 3 of the Perry eight-phase model, cited via [[chambers_sutherland_gait_analysis_2002]] (p.2, Table 2). Full Perry & Burnfield text not yet in vault (see [[perry_burnfield_gait_analysis]] caveat).

## Why it matters

It is the first half of single-limb support — the gait analogue of single-leg balance. Its 2D proxies (pelvic level, trunk sway) are directly observable.

## Source-derived model

- ~10-30% of the cycle; only the stance foot is on the ground; the body progresses over the foot.
- Ankle moves from foot-flat to neutral dorsiflexion over the stationary foot.

## Joint involvement

[[ankle_joint]] dorsiflexion (over stationary foot), [[knee_joint]] stable, [[hip_joint]] extension, pelvis and trunk control.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Third phase of [[stance_phase]] (A); follows [[loading_response]] (A); precedes [[terminal_stance]] (A); maps to the first part of the coarser [[single_limb_stance]] period (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Period bounds (opposite toe-off to heel-rise), pelvic levelness, trunk sway, knee tracking from a 2D front/side view.

## What the app must not infer

- Single-leg stability as a measured kinetic or muscle-activation variable; diagnosis or causation.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[loading_response]], [[terminal_stance]], [[single_limb_stance]], [[gait_observability_boundary]], [[perry_burnfield_gait_analysis]].

## Sources

- [[perry_burnfield_gait_analysis]] — eight-phase model (framework-cited via Chambers & Sutherland).
- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2).

## Evidence-separation rules

- **(A)** Phase definition, ~10-30%, single-limb-over-foot role — cited via Chambers & Sutherland (read in full).
- **(B)** Cross-links to [[stance_phase]], [[single_limb_stance]] — same Level 1 domain.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
