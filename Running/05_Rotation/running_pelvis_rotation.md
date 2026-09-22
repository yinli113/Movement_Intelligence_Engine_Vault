---
id: running_pelvis_rotation
canonical_id: running.rotation.pelvis
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Pelvis Rotation
aliases: [Pelvis Rotation]
domain: running
directly_measured: true
proxy_measurement: true
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_schache_lumbopelvic_1999]
relationships:
  required_events: [running_running_cycle]
  supports: [running_pelvis_thorax_rotation, running_rotational_coupling, running_rotational_reversal]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 15
hub_score: 24
centrality: 0.134
updated: 2026-09-09
---

# Running - Pelvis Rotation

## Definition

A Level A camera-derived measurement or named proxy. The front-view pelvis-orientation proxy reversed later in right stance.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

Bilateral hip landmarks and, where available, additional pelvis-orientation landmarks.

## Calculation Concept

Estimate an image-derived pelvis-orientation signal from left-right hip geometry; document the algorithm and sign convention.

## Normalisation

Normalise time to the stride cycle; compare within the same view and setup.

## Recommended Camera View

- front
- back

## Confidence / Quality Gate

Contextual: suppress with hip occlusion, severe foreshortening, low left-right separation, or unstable camera geometry. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_pelvis_thorax_rotation]]
- [[running_rotational_coupling]]
- [[running_rotational_reversal]]

## What It Cannot Prove

True 3D transverse pelvis rotation, angular momentum, torque, or fascial loading cannot be recovered from this proxy. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_preece_spine_pelvis_2016]]
- [[running_schache_lumbopelvic_1999]]

## Reporting Language

Permitted: "The front-view pelvis-orientation proxy reversed later in right stance."

## Forbidden Claims

- Do not report: "Pelvis rotation torque was high."
- Do not report: "True transverse rotation measured."
