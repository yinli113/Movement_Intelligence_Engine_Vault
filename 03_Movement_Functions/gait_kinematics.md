---
id: gait_kinematics
type: Movement Function
preferred_name: "Gait Kinematics"
aliases: [gait kinematic analysis, motion analysis]
short_definition: "The measurement of gait motion (joint angles, segment positions) over the cycle, typically via 3D marker-based motion capture; one of the five instrumented gait measurement categories."
domain: gait
evidence_level: 3
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis, kadaba_lower_extremity_kinematics_1990, fukuchi_walking_kinematics_dataset_2018, stenum_video_gait_pose_estimation_2021, yang_park_mediapipe_gait_camera_location_2024, bergamini_walking_symmetry_2024]
status: reviewed
reviewed_date: 2026-11-14
contains: []
connects_to: [gait_cycle, gait_kinetics, gait_observability_boundary, observational_gait_analysis]
directly_supported_claims:
  - "Gait kinematics is the measurement of joint angles and segment positions over the gait cycle."
  - "Lab kinematics uses 3D marker-based motion capture; 2D pose estimation provides projected image-plane angle curves."
  - "Kinematics describes motion, not the forces that cause it."
  - "Each of the eight gait phases has a characteristic sagittal progression at the ankle, knee, and hip in 3D motion capture, while 2D video angles require coordinate-aware interpretation (curve direction, within-phase excursion, and left-right matching-phase comparison rather than raw 3D degree cutoffs)."
app_translation:
  - "A 2D app produces projected kinematic proxies (2D joint angles), NOT lab-grade 3D anatomical joint angles."
  - "Evaluate phase-by-phase movement using expected directional progressions, within-phase excursion, and left-vs-right matching-phase comparison; display 3D literature phase values only as educational reference context."
confidence: high
review_status: reviewed
relationship_count: 9
hub_score: 13
centrality: 0.08
---

# Gait Kinematics

## Definition

**Gait kinematics** is the measurement of gait motion — joint angles and segment positions over the [[gait_cycle]] — typically via 3D marker-based motion capture. It is one of the five instrumented gait measurement categories (Chambers & Sutherland, p.4-5). Kinematics describes **motion, not the forces that cause it**.

## Why it matters

Kinematics is the closest instrumented category to what a 2D app observes, so the distinction between validated 3D anatomical joint angles and 2D camera-projected proxies is essential for scientifically accurate phase-by-phase insights.

## Source-derived model

- 3D marker-based motion capture produces normalized joint-angle curves (0–100% gait cycle) across the eight phases (Kadaba et al., 1990; Perry & Burnfield, 2010; Fukuchi et al., 2018).
- Kinematics = geometry of motion (position, angle, excursion, timing), independent of force.

### Eight-phase 3D reference progression vs. 2D camera proxy translation

| Phase (% of cycle) | 3D Ankle Reference (Kadaba 1990; Perry & Burnfield; Fukuchi 2018) | 3D Knee Reference | 3D Hip Reference | Valid 2D Camera Insight Strategy (`gait_observability_boundary`) |
|---|---|---|---|---|
| **1. Initial Contact (0%)** | ~0° neutral | ~0–5° flexion (near full extension) | ~20–30° flexion | Single contact frame snapshot; compare L vs R contact posture and knee bend proxy. |
| **2. Loading Response (0–12%)** | Plantarflexes ~5–10° (first rocker / foot-flat lowering) | Flexes to ~15–20° (loading knee bend) | Holds ~20–25° flexion, begins extending | Check whether **knee bend proxy increases** during weight acceptance and **foot–shank included angle opens**; compare L vs R loading excursion. |
| **3. Midstance (12–31%)** | Dorsiflexes to ~5° as tibia advances (second rocker) | Extends from ~15° back toward ~0–5° | Extends from ~20° toward ~0° neutral | Check whether **knee bend proxy decreases** (straightens) and **foot–shank angle closes** as the tibia progresses over the planted foot. |
| **4. Terminal Stance (31–50%)** | Dorsiflexes to ~10° peak as heel rises (third rocker) | Remains near ~0–5° extension, begins flexing late | Reaches ~10–20° hyperextension (trailing thigh) | Check continued ankle closure prior to heel rise and trailing-limb progression; note that unsigned 2D trunk–thigh angle increases again as the thigh trails behind vertical. |
| **5. Pre-Swing (50–62%)** | Rapidly plantarflexes to ~15–20° at toe-off | Rapidly flexes to ~35–40° (unloading for swing) | Moves from extension back toward ~0° neutral | Check rapid **knee bend proxy increase** (~30–40°) and **foot–shank angle opening** during unloading. |
| **6. Initial Swing (62–75%)** | Plantarflexion reduces from ~20° toward ~5–10° | Reaches peak swing flexion (~60°; 55–65°) for toe clearance | Flexes to ~15–20° | Check **peak swing knee bend proxy** (typically ~50–65° in 2D side view) and L vs R swing-peak symmetry. |
| **7. Midswing (75–87%)** | Reaches ~0° neutral dorsiflexion for foot clearance | Begins extending from ~60° toward ~25–30° | Flexes to ~25° (near peak advancement) | Check **knee straightening progression** and **foot–shank angle closure** for midswing foot clearance. |
| **8. Terminal Swing (87–100%)** | Holds ~0° neutral (or slight plantarflexion) for contact | Extends to ~0–5° in preparation for heel strike | Holds ~20–25° flexion | Check **terminal knee extension** (knee bend proxy returning near minimum before contact) and L vs R terminal reach. |

## Joint involvement

[[hip_joint]], [[knee_joint]], [[ankle_joint]], pelvis, trunk — all measured as angle-time curves across [[initial_contact]], [[loading_response]], [[mid_stance]], [[terminal_stance]], [[preswing]], [[initial_swing]], [[midswing]], and [[terminal_swing]].

## Muscle involvement

No muscle claims from this node; muscle activity is [[gait_emg]].

## Movement or phase relationships

Measured over the [[gait_cycle]] (A); paired with [[gait_kinetics]] (A) to compute joint moments; bounded by [[gait_observability_boundary]] (A).

## Possible myofascial relationships

None directly. Fascial-line mapping is an engine synthesis (C).

## What a 2D app can observe

- **Knee (`left/right_knee_flexion_proxy`)**: `180° - jointAngle(hip, knee, ankle)` in side view tracks sagittal knee-bend direction and excursion closely (loading bend in `loading_response`, straightening in `mid_stance`, rapid bend in `preswing`, peak bend in `initial_swing`, and straightening in `terminal_swing`), though perspective and clothing affect absolute degrees (Stenum et al., 2021; Yang & Park, 2024).
- **Hip (`left/right_hip_flexion_proxy`)**: `180° - jointAngle(shoulder, hip, knee)` measures **unsigned** trunk–thigh deviation from straight alignment. Because both anterior thigh flexion (at `initial_contact` / `midswing`) and posterior thigh extension (at `terminal_stance`) produce positive unsigned angles, phase insights must evaluate within-phase direction, excursion range, and L-vs-R matching-phase symmetry rather than treating raw degrees as signed 3D hip flexion/extension.
- **Ankle (`left/right_ankle_flexion_proxy`)**: `jointAngle(knee, ankle, footIndex)` measures the raw 2D included angle between shank and foot (typically ~100–130° in shoes), not calibrated anatomical neutral (0° at 90°). Therefore, phase insights must evaluate **within-phase opening/closing** (rocker progression) and **L-vs-R matching-phase excursion**, never comparing the raw ~110° included angle directly against a 3D `0°–10°` dorsiflexion threshold.
- **Frontal plane (`front` / `back` views)**: Apparent pelvic obliquity (`hip-line tilt`), lateral trunk lean, shoulder-line tilt, and horizontal ankle separation.

## What the app must not infer

- Calibrated 3D anatomical ROM pass/fail cutoffs from uncalibrated 2D included angles.
- Kinetics, joint moments, EMG, or clinical pathology from 2D proxies.

## Related concepts

[[gait_cycle]], [[gait_kinetics]], [[gait_observability_boundary]], [[observational_gait_analysis]], [[gait_emg]], [[initial_contact]], [[loading_response]], [[mid_stance]], [[terminal_stance]], [[preswing]], [[initial_swing]], [[midswing]], [[terminal_swing]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.4-5.
- [[perry_burnfield_gait_analysis]] — Ch. 1–9 (eight-phase functional tasks, critical events, and joint progressions).
- [[kadaba_lower_extremity_kinematics_1990]] — Repeatability and normative 3D lower-extremity angle waveforms across the gait cycle.
- [[fukuchi_walking_kinematics_dataset_2018]] — Normative overground and treadmill 3D walking kinematics across speeds.
- [[stenum_video_gait_pose_estimation_2021]] — Comparison of 2D pose-estimation sagittal joint angles and temporal events against 3D motion capture.
- [[yang_park_mediapipe_gait_camera_location_2024]] — Camera-view sensitivity and systematic offset/projection effects of MediaPipe Pose 2D joint angles.
- [[bergamini_walking_symmetry_2024]] — Bilateral symmetry across walking speeds.

## Evidence-separation rules

- **(A)** Kinematics definition, 3D eight-phase progressions, and 2D camera projection properties — directly from the cited Level 1 and Level 3 sources.
- **(B)** Cross-links to [[gait_cycle]], [[gait_observability_boundary]], and the eight phase nodes.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
