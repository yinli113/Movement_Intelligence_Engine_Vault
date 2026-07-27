---
id: swing_phase
type: Movement Function
preferred_name: "Swing Phase"
aliases: [swing, swing period]
short_definition: "The ~38% of the gait cycle when the foot is off the ground advancing forward, divided into initial swing, midswing, and terminal swing."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: [initial_swing, midswing, terminal_swing]
connects_to: [gait_cycle, stance_phase, observational_gait_analysis]
directly_supported_claims:
  - "Swing is the ~38% of the gait cycle when the foot is off the ground."
  - "Swing comprises three phases: initial swing, midswing, and terminal swing."
app_translation:
  - "Use swing boundaries (toe-off to next foot strike) as a 2D-observable phase marker."
  - "The app can mark swing duration and limb advancement but cannot measure the muscle activation that drives swing."
---

# Swing Phase

## Definition

**Swing** is the ~38% of the [[gait_cycle]] when the foot is off the ground, advancing the limb forward. It is divided into [[initial_swing]], [[midswing]], and [[terminal_swing]] (Chambers & Sutherland, p.2).

## Why it matters

Swing advances and positions the limb for the next strike; foot clearance during swing is a common 2D-observable gait descriptor.

## Source-derived model

- Toe-off (~62%) → next foot strike (100%) = swing.
- Three phases: initial swing (acceleration), midswing (clearance), terminal swing (deceleration/positioning).

## Joint involvement

[[hip_joint]] flexion, [[knee_joint]] flexion/extension, [[ankle_joint]] dorsiflexion for clearance.

## Muscle involvement

No muscle claims from this node; see [[gait_emg]].

## Movement or phase relationships

Second part of the [[gait_cycle]] (A); counterpart is [[stance_phase]] (A).

## Possible myofascial relationships

Engine synthesis (C) — see [[gait_myofascial_mapping]]. Swing-phase line engagement: [[superficial_front_line]] (drives limb advancement: hip flexion, knee extension, dorsiflexion), [[deep_front_line]] (psoas/iliacus initiates swing), [[front_functional_line]] (contralateral trunk counter-rotation). Short SFL here produces the classic stiff-knee swing compensations (hip hike, circumduction, vaulting). (Steppage gait is NOT an SFL-restriction compensation — steppage compensates for weak/inhibited dorsiflexors, the opposite problem.) Candidate-line map, not measured tissue loading.

## What a 2D app can observe

- Toe-off and foot-strike events, swing duration, foot clearance, knee/hip angles from a 2D side view.

## What the app must not infer

- Muscle activation driving swing, kinetics, or causation.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[initial_swing]], [[midswing]], [[terminal_swing]], [[observational_gait_analysis]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2.

## Evidence-separation rules

- **(A)** Swing definition, ~38%, three phases — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_cycle]], [[stance_phase]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
