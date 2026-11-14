---
id: gait_temporal_parameters
type: Movement Function
preferred_name: "Gait Temporal Parameters"
aliases: [temporal-spatial gait parameters, gait temporal-spatial]
short_definition: "The measurable time-and-distance descriptors of gait: velocity, cadence, step length, stride length, and cycle time."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis, fukuchi_walking_kinematics_dataset_2018, stenum_video_gait_pose_estimation_2021, hii_mediapipe_gait_validation_2023, bergamini_walking_symmetry_2024]
status: reviewed
reviewed_date: 2026-11-14
contains: []
connects_to: [gait_cycle, observational_gait_analysis, gait_observability_boundary]
directly_supported_claims:
  - "Temporal-spatial gait parameters are velocity, cadence, step length, stride length, and cycle time."
  - "Step length is one foot strike to the contralateral foot strike; stride length is one foot strike to the next same-foot strike."
  - "Normal values are age- and walking-speed-dependent; at comfortable adult walking speed, stance is ~60-62% and swing is ~38-40% of the gait cycle."
  - "2D markerless pose estimation (OpenPose, MediaPipe Pose) can estimate temporal parameters (stance time, swing time, step time, stride time, double support, cadence) from detected contact and toe-off events."
  - "Bilateral walking symmetry indices vary systematically with walking speed and parameter choice rather than obeying a single fixed cutoff."
app_translation:
  - "A 2D app can estimate step/stride timing, stance/swing durations and percentages, bilateral step-time/stance-time symmetry, and cadence from timed foot strikes and toe-offs."
  - "Velocity and step/stride length from uncalibrated 2D video are proxies or unavailable without spatial calibration; label app-derived values accurately and interpret temporal/symmetry values in the context of walking speed and stride-to-stride consistency."
confidence: high
review_status: reviewed
relationship_count: 5
hub_score: 8
centrality: 0.045
---

# Gait Temporal Parameters

## Definition

**Gait temporal-spatial parameters** are velocity, cadence, step length, stride length, step time, cycle (stride) time, and stance/swing phase durations. Step length and step time are measured from one foot strike to the contralateral foot strike; stride length and cycle time are measured from one foot strike to the next same-foot strike. Reference values are age- and speed-dependent (Chambers & Sutherland, p.2-3; Perry & Burnfield, Ch. 1; Fukuchi et al., 2018).

## Why it matters

Temporal parameters and bilateral stance/swing comparisons are among the highest-reliability outputs of an observational or 2D video gait assessment because they depend on contact and toe-off event timing rather than calibrated 3D depth or force plates (Stenum et al., 2021; Hii et al., 2023).

## Source-derived model

- **Cycle time (stride time)**: Elapsed time from initial contact to next initial contact of the same foot (100% gait cycle; typically ~1.0–1.2 s in comfortable adult walking).
- **Step time**: Elapsed time from initial contact of one foot to initial contact of the opposite foot (typically ~0.5–0.6 s at comfortable adult walking speed).
- **Cadence (steps/min)**: Step rate calculated as `60 / mean_step_time_sec` or `120 / mean_cycle_time_sec`. Comfortable adult walking typically averages ~100–120 steps/min, scaling upward with faster walking speeds and varying with stature and age (Chambers & Sutherland, 2002; Fukuchi et al., 2018).
- **Stance vs. swing split (% of cycle)**:
  - **Stance phase**: ~60–62% of the cycle at comfortable walking speed (`loading_response` ~0–10/12%, `mid_stance` ~10/12–30/31%, `terminal_stance` ~30/31–50%, `preswing` ~50–60/62%).
  - **Swing phase**: ~38–40% of the cycle at comfortable walking speed (`initial_swing` ~60/62–73/75%, `midswing` ~73/75–87%, `terminal_swing` ~87–100%).
  - **Double-limb support**: Initial double support (`loading_response`) + terminal double support (`preswing`), totaling ~20–24% of the cycle at comfortable speed and decreasing as walking speed increases.
  - **Single-limb support**: `mid_stance` + `terminal_stance` (~38–40% of the cycle), equal to the opposite limb's swing duration.
- **Left-right temporal symmetry**:
  - Comparing left vs. right stance duration (s), swing duration (s), stance:swing ratio (`% : %`), and step time (s) identifies whether one limb unloads early (shorter stance %, longer contralateral double support) or prolongs stance.
  - Symmetry indices vary across walking speeds and across parameter types (Bergamini et al., 2024), so bilateral differences should be reported descriptively alongside per-side durations, percentages, and stride-to-stride variability rather than as a standalone diagnostic cutoff.

## Joint involvement

Whole-limb; these are whole-body output parameters, not joint-specific.

## Muscle involvement

No muscle claims from this node.

## Movement or phase relationships

Derived from the [[gait_cycle]] (A); observable via [[observational_gait_analysis]] (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- Per-side cycle time (stride duration), stance duration (s and % of cycle), swing duration (s and % of cycle), step time (s), cadence (steps/min), and stride-to-stride cycle variability from detected initial-contact and toe-off events (Stenum et al., 2021; Hii et al., 2023).
- Left-vs-right comparisons of stance time, swing time, stance:swing percentage split, and step time.
- Step/stride length and walking speed only as image-plane proxies unless a spatial calibration reference is provided.

## What the app must not infer

- Lab-grade instrumented velocity or spatial step length (m) without scene calibration.
- Kinetics, ground reaction forces, EMG, or clinical pathology from temporal asymmetry alone.

## Related concepts

[[gait_cycle]], [[observational_gait_analysis]], [[gait_observability_boundary]], [[determinants_of_gait]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2-3 (temporal-spatial definitions, ~60% stance / ~40% swing split, age-dependent norms).
- [[perry_burnfield_gait_analysis]] — Ch. 1 (eight-phase stance/swing subdivisions, ~60–62% stance / ~38–40% swing, single and double support intervals).
- [[fukuchi_walking_kinematics_dataset_2018]] — Overground and treadmill normative kinematics/spatiotemporal dataset across walking speeds.
- [[stenum_video_gait_pose_estimation_2021]] — Validation of 2D video pose estimation for temporal gait parameters (step time, stance time, swing time, double support) against 3D motion capture.
- [[hii_mediapipe_gait_validation_2023]] — Markerless MediaPipe Pose temporal gait detection (heel-strike, toe-off, cadence, stance/swing, double support).
- [[bergamini_walking_symmetry_2024]] — Speed-dependence and index sensitivity of bilateral walking symmetry metrics.

## Evidence-separation rules

- **(A)** Parameter definitions, stance/swing percentages, 2D video temporal validation, and symmetry speed-dependence — directly from the cited Level 1 and Level 3 sources.
- **(B)** Cross-links to [[gait_cycle]], [[observational_gait_analysis]], and [[gait_observability_boundary]].
- **(C)** Any fascial-line mapping is `engine_synthesis`.
