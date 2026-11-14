---
id: gait_observability_boundary
type: Movement Function
preferred_name: "Gait Observability Boundary"
aliases: [gait observational-vs-instrumented boundary, gait observability rule]
short_definition: "The gait-domain rule that observational/2D gait yields descriptors only; kinetics, EMG, foot pressure, and energetics each require specific instrumentation, and causation cannot be inferred from observation alone."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: []
connects_to: [observational_gait_analysis, gait_kinematics, gait_kinetics, gait_emg, foot_pressure, gait_energetics]
directly_supported_claims:
  - "Observational gait analysis cannot determine the biomechanical causes of an abnormal gait."
  - "Without measurements of kinetics or muscular activity (EMG), one can rarely be sure of the etiology of a gait problem."
  - "Kinematics, kinetics, EMG, foot pressure, and energetics each require specific instrumentation."
app_translation:
  - "A camera-derived gait descriptor (e.g., a knee-flexion proxy) is a camera-observable descriptor, NOT a measured kinetic, EMG, pressure, or energetic variable."
  - "The app must never upgrade a 2D proxy into a kinetic, EMG, or causal claim, nor diagnose gait etiology or direct treatment."
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 23
hub_score: 42
centrality: 0.205
---

# Gait Observability Boundary

## Definition

The **gait observability boundary** is the gait-domain rule that observational/2D gait yields **descriptors only**; kinetics, EMG, foot pressure, and energetics each require specific instrumentation, and **causation cannot be inferred from observation alone**. It is the gait analogue of the golf [[golf_kinetics_observability_boundary]].

## Source quote

> "Observational gait analysis is limited because it cannot determine the biomechanical causes of an abnormal gait. Although one can infer causation, without measurements of kinetics or of muscular activity by dynamic electromyography (EMG), one can rarely be sure of the etiology of a problem." (Chambers & Sutherland, p.4)

## Why it matters

This boundary governs gait-app reporting exactly as the golf boundary governs golf-app reporting. It is the single most important rule for keeping gait reports scientifically honest.

## Source-derived model

- Observation → descriptors (what is seen).
- Kinetics / EMG / pressure / energetics → require instrumentation (not available from 2D).
- Causation → requires instrumented kinetics or EMG; not inferable from observation.

## Joint involvement

Applies to all joints; it is a reporting rule, not a joint model.

## Muscle involvement

Muscle activity is explicitly out of observational reach; it requires [[gait_emg]].

## Movement or phase relationships

Binds [[observational_gait_analysis]] (A) and separates it from [[gait_kinematics]] (A), [[gait_kinetics]] (A), [[gait_emg]] (A), [[foot_pressure]] (A), [[gait_energetics]] (A).

## Possible myofascial relationships

Inferring fascial tension/shortening from gait observation is forbidden by this boundary. The engine synthesis in [[gait_myofascial_mapping]] provides candidate-line mappings (line→phase, line→restriction pattern, line→compensation) for follow-up assessment only — it must not be reported as measured tissue loading, fascial tension, or causal diagnosis from 2D observation.

## What a 2D app can observe

- Descriptors: joint angles, alignments, phase timing, asymmetries, temporal-spatial proxies.

## What the app must not infer

- Kinetics, EMG, foot pressure, energetics, causation, etiology, diagnosis, or treatment.

## Related concepts

[[observational_gait_analysis]], [[gait_kinematics]], [[gait_kinetics]], [[gait_emg]], [[foot_pressure]], [[gait_energetics]], [[golf_kinetics_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.4-6.
- [[yang_park_mediapipe_gait_camera_location_2024]] — 2D MediaPipe camera-placement sensitivity for ankle/knee/hip angles (Level 3).
- [[hii_mediapipe_gait_validation_2023]] — MediaPipe vs. Vicon temporal/spatial gait validation boundary (Level 3).

## Evidence-separation rules

- **(A)** The boundary statement and the instrumentation requirement — directly from Chambers & Sutherland.
- **(B)** Cross-link to [[golf_kinetics_observability_boundary]] — same principle, golf domain (Level 1 Kwon source).
- **(C)** None; this node is a rule, not a synthesis.


## Phase-aware gait reporting — 13 November 2026

Canonical app reporting contract: `gait_reporting.v1.json` (engine synthesis). It owns honest projected-angle labels, phase-functional context, view gates and nonclinical display gates. Primary method sources: [[stenum_video_gait_pose_estimation_2021]], [[yang_park_mediapipe_gait_camera_location_2024]] and [[bergamini_walking_symmetry_2024]]. Compare matching phases for left/right descriptions; simultaneous traces describe coordination. No normative band or tissue cause is inferred.


Report geometry clarification (13 November 2026): fresh workbench metrics use a hip-line tilt projection with anatomical-right-lower positive and a shoulder/pelvis-midpoint trunk lean with image-right positive. These use normalized image coordinates, not calibrated physical angles. Legacy shoulder-line tilt is not trunk lean; old wrapped pelvic angles are not reused as the new levelness metric. Unsigned hip bend and raw knee–ankle–toe angle are relabelled rather than treated as clinical flexion/extension or neutral dorsiflexion. Toe y is image position, not ground clearance.


### Phase-specific interpretation refinement — 13 November 2026

`gait_reporting.v1.json` v1.1 adds eight phase-specific observation questions and functional context. Actual tracked curve extrema, plateau spans and phase-specific shapes support descriptive summaries; visible little knee change does not establish poor shock absorption, toe image position does not establish ground clearance or foot drop, and knee extension does not measure hamstring eccentric control. Side-view horizontal pelvic travel remains chart context, not a highlighted deficit. Contact pattern, heel-rise/forefoot contact and foot–ground clearance remain explicitly labelled visual-review questions unless measured by an eligible dedicated method. Reference ratios/3D angles are never individual timing or clinical pass/fail rules.
