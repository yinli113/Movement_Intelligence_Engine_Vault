---
id: terminal_swing
type: Movement Function
preferred_name: "Terminal Swing"
aliases: [deceleration phase, terminal swing phase]
short_definition: "The final swing phase (~85-100% of the gait cycle), from tibia vertical to the next foot strike, decelerating the limb and positioning it for stance."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [swing_phase, gait_cycle, stance_phase, gait_observability_boundary]
directly_supported_claims:
  - "Terminal swing runs from tibia vertical to the next foot strike (~85-100% of the cycle)."
  - "The limb decelerates and extends to position the foot for the next stance."
app_translation:
  - "A 2D app can bound terminal swing by tibia vertical and foot strike, and report knee extension / heel-strike preparation proxies."
  - "The app must not infer the hamstring deceleration kinetics from the visible limb position alone."
---

# Terminal Swing

## Definition

**Terminal swing** runs from tibia vertical to the next foot strike (~85-100% of the [[gait_cycle]]). The limb decelerates and extends to position the foot for the next stance (Chambers & Sutherland, p.2).

## Why it matters

It sets up foot strike and stance; the limb's deceleration and extension here determine initial contact posture (heel strike vs flat foot).

## Source-derived model

- Bounded by tibia vertical (~85%) and next foot strike (100%).
- Knee extends; hip extends toward neutral; limb decelerates for controlled contact.

## Joint involvement

[[knee_joint]] extension, [[hip_joint]] extension, [[ankle_joint]] positioning for contact.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Final phase of [[swing_phase]] (A); transitions into [[stance_phase]] (A); also Perry phase 8 (Terminal Swing), cited via [[perry_burnfield_gait_analysis]] / [[chambers_sutherland_gait_analysis_2002]].

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Tibia-vertical and foot-strike events, knee extension, foot-contact posture from a 2D side view.

## What the app must not infer

- Hamstring deceleration kinetics, muscle activation, or causation.

## Related concepts

[[swing_phase]], [[gait_cycle]], [[stance_phase]], [[initial_swing]], [[midswing]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Phase bounds and deceleration/positioning role — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[swing_phase]], [[gait_cycle]], [[stance_phase]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
