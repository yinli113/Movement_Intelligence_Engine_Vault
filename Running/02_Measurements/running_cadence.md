---
id: running_cadence
canonical_id: running.rhythm.cadence
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Cadence
aliases: [Cadence]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_anderson_step_rate_2022, running_goss_step_rate_training_2026]
relationships:
  required_events: [running_initial_contact]
  supports: [running_variability, running_fatigue_drift, running_longer_landing_strategy]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 13
hub_score: 21
centrality: 0.116
updated: 2026-09-09
---

# Running - Cadence

## Definition

A Level A camera-derived measurement or named proxy. Cadence averaged 168 steps/min across 12 valid steps at the recorded trial speed.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

Reliable bilateral foot or ankle trajectories sufficient to detect successive steps.

## Calculation Concept

Count valid left and right step events over elapsed analysed time and convert to steps per minute.

## Normalisation

No geometric normalisation; retain speed, trial duration, and step count as context.

## Recommended Camera View

- side
- front
- back

## Confidence / Quality Gate

Require stable frame timing, at least six valid steps, and high-confidence step-event assignment. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_variability]]
- [[running_fatigue_drift]]
- [[running_longer_landing_strategy]]

## What It Cannot Prove

Cadence does not establish correctness, injury risk, economy, or an ideal target. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_anderson_step_rate_2022]]
- [[running_goss_step_rate_training_2026]]

## Reporting Language

Permitted: "Cadence averaged 168 steps/min across 12 valid steps at the recorded trial speed."

## Forbidden Claims

- Do not report: "Cadence below 180 is poor."
- Do not report: "Cadence detected an injury risk."
