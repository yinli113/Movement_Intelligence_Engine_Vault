---
id: running_thorax_rotation
canonical_id: running.rotation.thorax
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Thorax Rotation
aliases: [Thorax Rotation]
domain: running
directly_measured: true
proxy_measurement: true
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_lumbar_bone_pins_2014]
relationships:
  required_events: [running_running_cycle]
  supports: [running_pelvis_thorax_rotation, running_rotational_coupling, running_rotational_reversal]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 14
hub_score: 22
centrality: 0.125
updated: 2026-09-09
---

# Running - Thorax Rotation

## Definition

A Level A camera-derived measurement or named proxy. The shoulder-line thorax proxy showed smaller rightward excursion in comparable half-cycles.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

Bilateral shoulders, with torso landmarks used to reject foreshortened geometry.

## Calculation Concept

Estimate an image-derived shoulder/thorax orientation signal from bilateral shoulder geometry.

## Normalisation

Normalise time to the stride cycle and compare only like-for-like views.

## Recommended Camera View

- front
- back

## Confidence / Quality Gate

Contextual: require visible shoulders, adequate left-right separation, and no major occlusion. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_pelvis_thorax_rotation]]
- [[running_rotational_coupling]]
- [[running_rotational_reversal]]

## What It Cannot Prove

The proxy cannot measure vertebral rotation, true 3D thorax rotation, muscle action, or fascial tension. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_preece_spine_pelvis_2016]]
- [[running_lumbar_bone_pins_2014]]

## Reporting Language

Permitted: "The shoulder-line thorax proxy showed smaller rightward excursion in comparable half-cycles."

## Forbidden Claims

- Do not report: "Thoracic rotation restriction was diagnosed."
- Do not report: "Spinal rotation was directly measured."
