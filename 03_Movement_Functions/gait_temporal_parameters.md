---
id: gait_temporal_parameters
type: Movement Function
preferred_name: "Gait Temporal Parameters"
aliases: [temporal-spatial gait parameters, gait temporal-spatial]
short_definition: "The measurable time-and-distance descriptors of gait: velocity, cadence, step length, stride length, and cycle time."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [gait_cycle, observational_gait_analysis, gait_observability_boundary]
directly_supported_claims:
  - "Temporal-spatial gait parameters are velocity, cadence, step length, stride length, and cycle time."
  - "Step length is one foot strike to the contralateral foot strike; stride length is one foot strike to the next same-foot strike."
  - "Normal values are age-dependent."
app_translation:
  - "A 2D app can estimate step/stride length (scaled to a known reference) and cadence from timed foot strikes."
  - "Velocity from a 2D recording is a proxy; lab-grade velocity requires instrumented timing. Label app-derived values as proxies."
---

# Gait Temporal Parameters

## Definition

**Gait temporal-spatial parameters** are velocity, cadence, step length, stride length, and cycle time. Step length = one foot strike to the contralateral foot strike; stride length = one foot strike to the next same-foot strike. Normal values are age-dependent (Chambers & Sutherland, p.2-3).

## Why it matters

These are the most reportable gait descriptors and the natural output of an observational/2D gait app — they describe gait without claiming kinetics.

## Source-derived model

- Velocity (m/s), cadence (steps/min), step length, stride length, cycle time.
- Age-specific normal ranges provided in the source.

## Joint involvement

Whole-limb; these are whole-body output parameters, not joint-specific.

## Muscle involvement

No muscle claims from this node.

## Movement or phase relationships

Derived from the [[gait_cycle]] (A); observable via [[observational_gait_analysis]] (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Step/stride count and timing (cadence, cycle time); step/stride length scaled to a known reference; velocity proxy.

## What the app must not infer

- Lab-grade instrumented velocity/precision.
- Kinetics, EMG, or causation.

## Related concepts

[[gait_cycle]], [[observational_gait_analysis]], [[gait_observability_boundary]], [[determinants_of_gait]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2-3.

## Evidence-separation rules

- **(A)** Parameter definitions and age-dependence — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_cycle]], [[observational_gait_analysis]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
