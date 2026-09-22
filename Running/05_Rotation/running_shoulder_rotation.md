---
id: running_shoulder_rotation
canonical_id: running.rotation.shoulder
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Shoulder Rotation
aliases: [Shoulder Rotation]
domain: running
directly_measured: true
proxy_measurement: true
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_arellano_arm_swing_2014, running_pontzer_arm_swing_2009]
relationships:
  required_events: [running_running_cycle]
  supports: [running_arm_leg_coordination, running_pelvis_thorax_rotation, running_cross_body_coordination]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 16
hub_score: 22
centrality: 0.143
updated: 2026-09-09
---

# Running - Shoulder Rotation

## Definition

A Level A camera-derived measurement or named proxy. Shoulder-line rotational excursion differed between comparable left and right half-cycles.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

Bilateral shoulder landmarks; arm landmarks provide context but do not redefine thorax orientation.

## Calculation Concept

Track shoulder-line orientation and excursion as an image-plane rotational proxy across the stride.

## Normalisation

Normalise to stride phase and report peak-to-peak excursion in declared proxy units/degrees.

## Recommended Camera View

- front
- back

## Confidence / Quality Gate

Contextual: require both shoulders, stable view, and adequate landmark separation. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_arm_leg_coordination]]
- [[running_pelvis_thorax_rotation]]
- [[running_cross_body_coordination]]

## What It Cannot Prove

Shoulder-line rotation is not glenohumeral rotation, true 3D thorax rotation, angular momentum, or energy cost. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_arellano_arm_swing_2014]]
- [[running_pontzer_arm_swing_2009]]

## Reporting Language

Permitted: "Shoulder-line rotational excursion differed between comparable left and right half-cycles."

## Forbidden Claims

- Do not report: "Arm swing generated this measured metabolic cost."
- Do not report: "Shoulder rotation is deficient."
