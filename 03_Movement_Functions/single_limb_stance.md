---
id: single_limb_stance
type: Movement Function
preferred_name: "Single-Limb Stance"
aliases: [single limb support, mid-stance support]
short_definition: "The middle stance period (~10-50% of the gait cycle) when only the stance foot is on the ground and the body passes over it; the longest stance period."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [stance_phase, gait_cycle, gait_observability_boundary]
directly_supported_claims:
  - "Single-limb stance runs from opposite toe-off to opposite foot strike (~10-50% of the cycle)."
  - "Only the stance foot is on the ground while the body passes over it; it is the longest stance period."
app_translation:
  - "A 2D app can bound this period and report single-leg balance proxies (pelvic level, trunk sway)."
  - "The app must not infer single-leg stability as a kinetic/muscle-activation measurement."
---

# Single-Limb Stance

## Definition

**Single-limb stance** runs from opposite toe-off to opposite foot strike (~10-50% of the [[gait_cycle]]), when only the stance foot is on the ground and the body passes over it. It is the longest stance period (Chambers & Sutherland, p.2).

## Why it matters

It is the single-leg balance window — the gait analogue of the FMS [[hurdle_step]] / [[inline_lunge]] single-leg control. Its 2D proxies (pelvic level, trunk sway) are directly observable.

## Source-derived model

- Bounded by opposite toe-off (~10%) and opposite foot strike (~50%).
- Single foot supports body weight; contralateral limb is in swing.

## Joint involvement

[[ankle_joint]], [[knee_joint]], [[hip_joint]] stability; pelvis and trunk control.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Middle period of [[stance_phase]] (A); gait analogue of single-leg screen patterns (C). In the Perry eight-phase taxonomy (cited via [[perry_burnfield_gait_analysis]]), this period corresponds to [[mid_stance]] + [[terminal_stance]].

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]]. Single-limb stance relies most on [[lateral_line]] (frontal-plane stability, preventing hip adduction/Trendelenburg) and [[deep_front_line]] (inner-leg stability and medial arch support). [[superficial_back_line]] and [[superficial_front_line]] manage the sagittal progression over the stationary foot. Candidate-line map, not measured tissue loading.

## What a 2D app can observe

- Period bounds, pelvic levelness, trunk sway, knee tracking from a 2D front/side view.

## What the app must not infer

- Single-leg stability as a measured kinetic or muscle-activation variable.
- Diagnosis or causation.

## Related concepts

[[stance_phase]], [[gait_cycle]], [[initial_double_limb_support]], [[second_double_limb_support]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Period bounds and single-limb role — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[stance_phase]], [[gait_cycle]] — same Level 1 source.
- **(C)** FMS single-leg analogy and any fascial mapping are `engine_synthesis`.
