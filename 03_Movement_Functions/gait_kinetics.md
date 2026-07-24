---
id: gait_kinetics
type: Movement Function
preferred_name: "Gait Kinetics"
aliases: [gait kinetic analysis, joint moments gait]
short_definition: "The measurement of forces and joint moments during gait, typically via force plates, yielding ground reaction forces and internal/external joint moments; an instrumented category not available from 2D observation."
domain: gait
evidence_level: 3
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [gait_cycle, gait_kinematics, ground_reaction_force, gait_observability_boundary]
directly_supported_claims:
  - "Gait kinetics is the measurement of forces and joint moments during gait."
  - "Lab kinetics uses force plates to derive ground reaction forces and internal vs external joint moments."
  - "Kinetics describes forces, which observation cannot measure."
app_translation:
  - "A 2D app CANNOT measure gait kinetics; force-plate data is required."
  - "The app must never report a joint moment, ground reaction force, or loading value as if measured from video."
---

# Gait Kinetics

## Definition

**Gait kinetics** is the measurement of forces and joint moments during gait, typically via force plates, yielding [[ground_reaction_force]] and internal/external joint moments (Chambers & Sutherland, p.4-5). It is an instrumented category **not available from 2D observation**.

## Why it matters

Kinetics is the force layer that, combined with [[gait_kinematics]], explains *why* gait looks the way it does. Because it requires force plates, it is the clearest example of what a 2D app must never claim.

## Source-derived model

- Force plates measure ground reaction force (vertical, fore-aft, mediolateral).
- Joint moments computed from force + kinematics; internal vs external moments distinguished.

## Joint involvement

[[hip_joint]], [[knee_joint]], [[ankle_joint]] moments; whole-body ground reaction.

## Muscle involvement

Moments reflect net muscle + ligament action, but specific muscle activation requires [[gait_emg]].

## Movement or phase relationships

Measured over the [[gait_cycle]] (A); paired with [[gait_kinematics]] (A); bounded by [[gait_observability_boundary]] (A).

## Possible myofascial relationships

None directly. Inferring fascial loading from kinetics is an engine synthesis (C) and must be labelled.

## What a 2D app can observe

- Nothing kinetic directly. Only kinematic proxies that *suggest* loading patterns as hypotheses.

## What the app must not infer

- Joint moments, ground reaction force magnitude/direction, loading, or any kinetic value from 2D.
- Causation or diagnosis.

## Related concepts

[[gait_cycle]], [[gait_kinematics]], [[ground_reaction_force]], [[gait_observability_boundary]], [[gait_emg]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.4-5.

## Evidence-separation rules

- **(A)** Kinetics definition, force-plate method, forces-not-observable — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_cycle]], [[gait_observability_boundary]] — same Level 1 source.
- **(C)** Any fascial-loading inference is `engine_synthesis` and must be labelled.
