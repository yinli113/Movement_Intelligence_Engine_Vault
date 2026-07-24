---
id: initial_swing
type: Movement Function
preferred_name: "Initial Swing"
aliases: [acceleration phase, initial swing phase]
short_definition: "The first swing phase (~62-75% of the gait cycle), from toe-off to when the swinging limb is opposite the stance limb, accelerating the limb forward."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [swing_phase, gait_cycle, gait_observability_boundary]
directly_supported_claims:
  - "Initial swing runs from toe-off to the swinging limb being opposite the stance limb (~62-75% of the cycle)."
  - "The limb accelerates forward and the knee flexes to shorten the limb for advancement."
app_translation:
  - "A 2D app can bound initial swing by toe-off and the mid-swing limb position and report knee-flexion proxy."
  - "The app must not infer the muscle activation that accelerates the limb."
---

# Initial Swing

## Definition

**Initial swing** runs from toe-off to the swinging limb being opposite the stance limb (~62-75% of the [[gait_cycle]]). The limb accelerates forward and the knee flexes to shorten the limb for advancement (Chambers & Sutherland, p.2).

## Why it matters

It is the limb-acceleration window; knee flexion here is a clean 2D-observable descriptor of swing initiation.

## Source-derived model

- Bounded by toe-off (~62%) and the limbs being opposite (~75%).
- Knee flexion peaks to reduce the limb's moment of inertia.

## Joint involvement

[[hip_joint]] flexion, [[knee_joint]] flexion, [[ankle_joint]] dorsiflexion begins.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

First phase of [[swing_phase]] (A); also Perry phase 6 (Initial Swing), cited via [[perry_burnfield_gait_analysis]] / [[chambers_sutherland_gait_analysis_2002]].

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Toe-off and opposite-limb events, knee-flexion angle, limb advancement from a 2D side view.

## What the app must not infer

- Muscle activation driving acceleration, kinetics, or causation.

## Related concepts

[[swing_phase]], [[gait_cycle]], [[midswing]], [[terminal_swing]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Phase bounds and acceleration role — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[swing_phase]], [[gait_cycle]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
