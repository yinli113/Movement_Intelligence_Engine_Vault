---
id: midswing
type: Movement Function
preferred_name: "Midswing"
aliases: [mid-swing, mid swing phase]
short_definition: "The middle swing phase (~75-85% of the gait cycle), when the swinging limb passes the stance limb and the foot clears the ground."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis]
status: reviewed
reviewed_date: 2026-07-24
contains: []
connects_to: [swing_phase, gait_cycle, gait_observability_boundary]
directly_supported_claims:
  - "Midswing runs from the limbs being opposite to tibia vertical (~75-85% of the cycle)."
  - "The foot clears the ground as the limb passes the stance limb."
app_translation:
  - "A 2D app can report foot-clearance proxy (toe height) during midswing from a 2D side view."
  - "The app must not infer dorsiflexor activation or pathology from clearance alone."
---

# Midswing

## Definition

**Midswing** runs from the swinging limb being opposite the stance limb to tibia vertical (~75-85% of the [[gait_cycle]]). The foot clears the ground as the limb passes the stance limb (Chambers & Sutherland, p.2).

## Why it matters

Foot clearance during midswing is one of the most clinically salient and 2D-observable gait descriptors (e.g., foot drop shows here).

## Source-derived model

- Bounded by opposite-limb position (~75%) and tibia vertical (~85%).
- Ankle dorsiflexion holds the foot clear of the ground.

## Joint involvement

[[knee_joint]] extension begins, [[ankle_joint]] dorsiflexion for clearance, [[hip_joint]] flexion.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Middle phase of [[swing_phase]] (A); also Perry phase 7 (Mid Swing), cited via [[perry_burnfield_gait_analysis]] / [[chambers_sutherland_gait_analysis_2002]].

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Foot clearance (toe height), tibia verticality, knee angle from a 2D side view.

## What the app must not infer

- Dorsiflexor activation, foot-drop diagnosis, or causation.

## Related concepts

[[swing_phase]], [[gait_cycle]], [[initial_swing]], [[terminal_swing]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Phase bounds and clearance role — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[swing_phase]], [[gait_cycle]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
