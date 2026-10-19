---
id: running_trunk_lean
canonical_id: running.trunk.lean
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Trunk Lean
aliases: [Trunk Lean]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_trunk_lean_loading_2024]
relationships:
  required_events: [running_running_cycle]
  supports: [running_different_load_distribution_strategy, running_variability, running_fatigue_drift]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 12
hub_score: 17
centrality: 0.107
updated: 2026-09-09
---

# Running - Trunk Lean

## Definition

A Level A camera-derived measurement or named proxy. Forward trunk-inclination proxy averaged 7 degrees during midstance at this speed.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

Shoulder midpoint and pelvis/hip midpoint.

## Calculation Concept

Angle of the shoulder-centre to pelvis-centre vector relative to image vertical.

## Normalisation

Report signed degrees with the documented forward direction and stride phase.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require visible bilateral shoulder and hip landmarks and a near-orthogonal side view. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_different_load_distribution_strategy]]
- [[running_variability]]
- [[running_fatigue_drift]]

## What It Cannot Prove

Trunk lean does not directly measure hip/knee loads, force redistribution, or a universally correct posture. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_trunk_lean_loading_2024]]

## Reporting Language

Permitted: "Forward trunk-inclination proxy averaged 7 degrees during midstance at this speed."

## Forbidden Claims

- Do not report: "More forward lean is better."
- Do not report: "Hip loading increased by this measured amount."
