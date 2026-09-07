---
id: stance_phase
type: Movement Function
preferred_name: "Stance Phase"
aliases: [stance, stance period]
short_definition: "The ~62% of the gait cycle when the foot is on the ground, divided into initial double-limb support, single-limb stance, and second double-limb support (preswing)."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: [initial_double_limb_support, single_limb_stance, second_double_limb_support]
connects_to: [gait_cycle, swing_phase, observational_gait_analysis]
directly_supported_claims:
  - "Stance is the ~62% of the gait cycle when the foot is on the ground."
  - "Stance comprises three periods: initial double-limb support, single-limb stance, and second double-limb support (preswing)."
app_translation:
  - "Use stance boundaries (foot strike to toe-off) as the primary 2D-observable phase marker."
  - "The app can mark stance duration but cannot measure the ground reaction force that defines loading."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 26
hub_score: 59
centrality: 0.234
---

# Stance Phase

## Definition

**Stance** is the ~62% of the [[gait_cycle]] when the foot is on the ground. It is divided into three periods: [[initial_double_limb_support]], [[single_limb_stance]], and [[second_double_limb_support]] (preswing) (Chambers & Sutherland, p.2).

## Why it matters

Stance is where weight is accepted and advanced; it is the phase a 2D camera can most reliably bound (foot on/off ground), making it the anchor for observational timing.

## Source-derived model

- Foot strike (0%) → toe-off (~62%) = stance.
- Three periods: initial double-limb support, single-limb stance, second double-limb support.

## Joint involvement

[[ankle_joint]], [[knee_joint]], [[hip_joint]] across shock absorption, mid-stance, and propulsion.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

First half of the [[gait_cycle]] (A); counterpart is [[swing_phase]] (A).

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]]. Stance-phase line engagement: [[superficial_back_line]] (hip extension/plantarflexion), [[lateral_line]] (frontal-plane stability), [[spiral_line]] (rotational deceleration at heel strike and re-supination before toe-off), [[back_functional_line]] (posterior sling braking), [[superficial_front_line]] (anterior tissues lengthen / elastically load for shock absorption and pre-stretch for swing recoil; muscle action often isometric per Earls' SSC framing, not eccentric), [[deep_front_line]] (inner-leg stability and swing initiation). Candidate-line map, not measured tissue loading.

## What a 2D app can observe

- Foot contact intervals and stance duration from a 2D side/front view.

## What the app must not infer

- Ground reaction force, joint moments, muscle activation, or causation.

## Related concepts

[[gait_cycle]], [[swing_phase]], [[initial_double_limb_support]], [[single_limb_stance]], [[second_double_limb_support]], [[observational_gait_analysis]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Stance definition, ~62%, three periods — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_cycle]], [[swing_phase]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
