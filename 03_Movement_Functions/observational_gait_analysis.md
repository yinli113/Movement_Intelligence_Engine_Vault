---
id: observational_gait_analysis
type: Movement Function
preferred_name: "Observational Gait Analysis"
aliases: [visual gait analysis, 2D gait observation]
short_definition: "Systematic visual observation of gait by plane (coronal, sagittal, transverse), often with video, producing descriptors of gait appearance — explicitly unable to determine biomechanical cause."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [gait_cycle, gait_temporal_parameters, gait_observability_boundary, gait_kinematics]
directly_supported_claims:
  - "Observational gait analysis is a systematic visual assessment by plane (coronal, sagittal, transverse), often aided by videotape for rotational abnormalities."
  - "Observational gait analysis cannot determine the biomechanical causes of an abnormal gait; causation requires kinetics or EMG."
app_translation:
  - "This is the app's native method: 2D video observation by plane, producing descriptors and temporal-spatial proxies."
  - "The app must report descriptors (what is seen), not causes (why it happens); cause is reserved for instrumented analysis."
---

# Observational Gait Analysis

## Definition

**Observational gait analysis** is a systematic visual assessment of gait by plane — coronal, sagittal, transverse — often aided by videotape for rotational abnormalities. It produces **descriptors** of gait appearance. It explicitly **cannot determine the biomechanical causes** of an abnormal gait (Chambers & Sutherland, p.4).

## Why it matters

This is the app's native method and the source of the gait-domain observability boundary. It defines what a 2D app may legitimately produce (descriptors) and what it may not (causes).

## Source-derived model

- Observe by plane: sagittal (front-back motion), coronal (side-to-side), transverse (rotational, via video).
- Output = descriptors (e.g., "reduced knee flexion at mid-stance"), not causes.

## Joint involvement

All visible joints by plane; the method, not a single joint.

## Muscle involvement

No muscle claims from this node; muscle activity requires [[gait_emg]].

## Movement or phase relationships

Operates on the [[gait_cycle]] (A); produces [[gait_temporal_parameters]] (A); bounded by [[gait_observability_boundary]] (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Joint angles and alignments by plane, phase timing, asymmetries, rotational proxies from video.

## What the app must not infer

- Biomechanical cause, kinetics, EMG, foot pressure, or diagnosis.

## Related concepts

[[gait_cycle]], [[gait_temporal_parameters]], [[gait_observability_boundary]], [[gait_kinematics]], [[gait_kinetics]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.4.

## Evidence-separation rules

- **(A)** By-plane method and the cannot-determine-cause statement — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_cycle]], [[gait_observability_boundary]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
