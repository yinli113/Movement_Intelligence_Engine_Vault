---
id: running_altered_rotational_coordination
canonical_id: running.interpretation.altered_rotational_coordination
type: App Logic
running_node_type: biomechanical_interpretation
evidence_level: 5
running_claim_level: C
status: canonical
preferred_name: "Running - Altered Rotational Coordination and Biomechanical Hypotheses"
aliases: [Altered Rotational Coordination, Rotational asymmetry interpretation, Pelvis-shoulder decoupling]
domain: running
directly_measured: false
camera_views: [front, back, side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_arellano_arm_swing_2014, running_mesquita_step_frequency_pelvis_2024, running_morley_lumbar_restriction_2019, running_reinking_2d_reliability_2018, gruenke_kiptum_running_analysis_2023]
relationships:
  required_inputs: [running_pelvis_rotation, running_shoulder_rotation, running_pelvis_thorax_rotation, running_rotational_coupling, running_arm_leg_coordination, running_cadence, running_step_time, running_variability, running_left_right_asymmetry]
  supports: [running_cross_body_myofascial_hypothesis, running_three_layer_rotation_model, running_spiral_line, running_functional_lines, running_deep_front_line]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_measurement_limitations, running_kinematics_are_not_kinetics]
confidence: high
review_status: canonical_definition
relationship_count: 24
hub_score: 48
centrality: 0.24
updated: 2026-10-15
---

# Running - Altered Rotational Coordination and Biomechanical Hypotheses

## Definition

A structured Level C biomechanical interpretation node that evaluates repeated, high-confidence differences in multi-segment proxy timing, excursion amplitudes, or relative phase between left and right stance cycles.

## Why It Matters

When TillYes Running measures an asymmetry (for example, greater pelvic-line tilt excursion during right stance while shoulder-line excursion remains symmetric between sides), an AI reasoning agent must not default to generic disclaimers or diagnose muscle weakness. This node maps observed kinematic asymmetries to **testable biomechanical hypotheses, required synchronized measurements, and supporting literature**.

## Required Synchronized Measurements

Before generating a Level C interpretation, the reasoning engine requires:
1. `running.frontal.pelvis_tilt` (`pelvic_line_excursion_deg_projected`) evaluated separately for `LEFT_STANCE` and `RIGHT_STANCE`.
2. `running.frontal.shoulder_tilt` (`shoulder_line_excursion_deg_projected`) evaluated separately for `LEFT_STANCE` and `RIGHT_STANCE`.
3. `running.rhythm.step_time` and `running.rhythm.cadence` for each side.
4. Shoulder-pelvis continuous phase lag (`shoulder_pelvis_lag_pct_stride`).
5. Valid cycle sample count ($n \ge 7$ per side per [[running_dingenen_2d_reliability_2018]]).
6. Camera view stability and heading drift checks ([[running_reinking_2d_reliability_2018]]).

## The 6 Biomechanical Explanations for Asymmetric Pelvis-Shoulder Coordination

When a runner shows greater pelvic-line tilt excursion on one side while shoulder-line excursion is relatively similar between sides:

```
                                 OBSERVED PATTERN
        ┌─────────────────────────────────────────────────────────────────┐
        │ Right stance: Large pelvic-line tilt excursion (e.g. 14.5°)     │
        │ Left stance:  Moderate pelvic-line tilt excursion (e.g. 9.2°)   │
        │ Shoulder-line: Symmetrical excursion between sides (e.g. 8.1°)  │
        └────────────────────────────────┬────────────────────────────────┘
                                         ▼
                            INVESTIGATE 6 RELATIONSHIPS
 ┌───────────────────────────────────────┼───────────────────────────────────────┐
 ▼                                       ▼                                       ▼
1. SPINAL DAMPING                       2. CADENCE & STANCE TIME                3. HIP ABDUCTOR CAPACITY
Thoraco-lumbar lateral flexion          Longer right step time allows           Right gluteus medius/minimus
absorbs pelvic roll before              gravity to induce more pelvic           eccentric control vs contralateral
reaching shoulder girdle                drop per Mesquita et al. (2024)         quadratus lumborum
(Preece et al., 2016)                   ([[running_cadence]])                   ([[gluteus_medius]])
 ┌───────────────────────────────────────┼───────────────────────────────────────┐
 ▼                                       ▼                                       ▼
4. LATERAL SPRING RECOIL                5. CONTRALATERAL ARM SWING              6. PERSPECTIVE ARTIFACT
Shoulder tipping & stance-hip hike      Contralateral (left) arm adjusts        Out-of-plane axial yaw or track
loads Spiral Line for passive recoil    excursion to balance pelvic moment      curve projects false 2D tilt
(Gruenke, 2023; [[running_spiral_line]]) (Arellano & Kram, 2014)                 (Reinking et al., 2018)
```

### 1. Spinal Lateral Flexion Damping (Thoraco-Pelvic Decoupling)
- **Mechanism**: The multi-segmental spine ([[thoracic_spine]], [[lumbar_spine]]) absorbs pelvic tilt through asymmetric lateral flexion, preserving a level shoulder girdle and horizontal gaze.
- **Evidence**: 3D motion capture demonstrates that the spine and thorax actively decouple from the pelvis in the frontal plane ([[running_preece_spine_pelvis_2016]]). Restricting spinal mobility raises metabolic cost ([[running_morley_lumbar_restriction_2019]]).

### 2. Cadence and Stance Duration Differences
- **Mechanism**: If right step time is longer than left step time, the body remains in single-leg support longer. Gravitational torque naturally produces greater cumulative pelvic roll excursion during longer contact periods.
- Frequency and speed may alter coordination under specific conditions; consult [[running_mesquita_step_frequency_pelvis_2024]] and [[running_preece_speed_2016]] rather than infer a deterministic individual response.

### 3. Stance-Phase Hip Abductor Capacity vs. Quadratus Lumborum
- **Mechanism**: Greater pelvic drop (contralateral hip depression) indicates higher demand on the stance-side hip abductor complex ([[gluteus_medius]], [[gluteus_minimus]], [[tensor_fasciae_latae]]) and ipsilateral lateral core stabilizers ([[quadratus_lumborum]], [[internal_oblique]]).
- **Evidence**: Classic biomechanical stance mechanics; warrants clinical assessment of hip abductor endurance without claiming diagnostic weakness from video.

### 4. Dynamic Lateral Elastic Spring Recoil (Spiral Line Recruitment)
- Elastic recoil, head stabilization and individual economy mechanisms are hypotheses here; see [[running_pelvis_thorax_rotation]] and [[running_running_economy]] for the evidence boundary.

### 5. Arm Swing Counterbalancing
- **Mechanism**: The contralateral arm swing (left arm during right stance) may provide sufficient counter-torque around the vertical axis to stabilize the upper trunk, isolating the shoulder girdle from pelvic movement ([[running_arellano_arm_swing_2014]]).

### 6. Camera Perspective and Yaw Cross-talk
- **Mechanism**: Frontal-plane 2D angles are highly sensitive to out-of-plane rotation ([[running_reinking_2d_reliability_2018]]). If the athlete exhibits an axial yaw bias or the camera is slightly oblique, transverse pelvic rotation will project geometrically as an apparent difference in pelvic-line tilt.

## Downstream Hypothesis Connections (Level D)

This Level C interpretation provides the required evidence bridge to Thomas Myers' three rotational systems:
- Contralateral arm-leg momentum differences $\rightarrow$ [[running_functional_lines]] (Outer System).
- Thoraco-pelvic decoupling, lateral spring recoil, and stirrup control $\rightarrow$ [[running_spiral_line]] (Middle System).
- Single-leg axial plumb-line centration and pelvic levelness $\rightarrow$ [[running_deep_front_line]] (Inner System).
- Synthesized model $\rightarrow$ [[running_three_layer_rotation_model]].

## Limitations and Evidence Boundaries

- Camera 2D video outputs are kinematic descriptors; they do not establish ground reaction force, joint torque, muscle activation (EMG), or fascial tension in Newtons ([[running_kinematics_are_not_kinetics]]).
- An observed asymmetry is an individual movement characteristic, not an automatic diagnosis of injury or inefficiency.
- Sampling uncertainty is metric-specific; [[running_dingenen_2d_reliability_2018]] does not validate a universal stride-count threshold for coordination.

## Reporting Language

- *Permitted*: "The runner demonstrated greater pelvic-line tilt excursion during right stance (14.2°) than left stance (9.8°) while shoulder excursion remained symmetric (8.5° bilateral), supporting a hypothesis of thoraco-lumbar lateral flexion damping."
- *Permitted*: "This asymmetry coexisted with a 30 ms longer right step time, consistent with cadence-dependent stance mechanics (Mesquita et al., 2024)."
- *Forbidden*: "Right gluteus medius is weak, causing pelvic collapse."
- *Forbidden*: "Runner has functional line pathology."

## Review Status

`canonical_definition`. Full-text evidence integration complete.

## Audited reasoning route (2026-10-16)
Use [[running_reasoning_retrieval_index]] and its relationship nodes for evidence-separated interpretation. An anatomical or clinical explanation is a hypothesis until independently assessed.
