---
id: gait_kinematics
type: Movement Function
preferred_name: "Gait Kinematics"
aliases: [gait kinematic analysis, motion analysis]
short_definition: "The measurement of gait motion (joint angles, segment positions) over the cycle, typically via 3D marker-based motion capture; one of the five instrumented gait measurement categories."
domain: gait
evidence_level: 3
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [gait_cycle, gait_kinetics, gait_observability_boundary, observational_gait_analysis]
directly_supported_claims:
  - "Gait kinematics is the measurement of joint angles and segment positions over the gait cycle."
  - "Lab kinematics uses 3D marker-based motion capture."
  - "Kinematics describes motion, not the forces that cause it."
app_translation:
  - "A 2D app produces a kinematic proxy (2D joint angles), NOT lab-grade 3D kinematics."
  - "Report app-derived angles as 2D proxies; do not present them as validated 3D kinematic measurements."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 9
hub_score: 13
centrality: 0.081
---

# Gait Kinematics

## Definition

**Gait kinematics** is the measurement of gait motion — joint angles and segment positions over the [[gait_cycle]] — typically via 3D marker-based motion capture. It is one of the five instrumented gait measurement categories (Chambers & Sutherland, p.4-5). Kinematics describes **motion, not the forces that cause it**.

## Why it matters

Kinematics is the closest instrumented category to what a 2D app observes, so the distinction between validated 3D kinematics and a 2D proxy is critical for honest reporting.

## Source-derived model

- 3D marker-based motion capture produces joint-angle curves over the cycle.
- Kinematics = geometry of motion (position, angle, velocity), independent of force.

## Joint involvement

[[hip_joint]], [[knee_joint]], [[ankle_joint]], pelvis, trunk — all measured as angle-time curves.

## Muscle involvement

No muscle claims from this node; muscle activity is [[gait_emg]].

## Movement or phase relationships

Measured over the [[gait_cycle]] (A); paired with [[gait_kinetics]] (A) to compute joint moments; bounded by [[gait_observability_boundary]] (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- 2D joint-angle proxies over the cycle (sagittal-plane angles are most reliable; transverse is least reliable from 2D).

## What the app must not infer

- Validated 3D kinematics, kinetics, EMG, or causation from 2D proxies.

## Related concepts

[[gait_cycle]], [[gait_kinetics]], [[gait_observability_boundary]], [[observational_gait_analysis]], [[gait_emg]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.4-5.

## Evidence-separation rules

- **(A)** Kinematics definition, 3D marker method, motion-not-force — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_cycle]], [[gait_observability_boundary]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
