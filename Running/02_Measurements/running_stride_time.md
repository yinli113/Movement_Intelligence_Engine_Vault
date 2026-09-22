---
id: running_stride_time
canonical_id: running.rhythm.stride_time
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Stride Time
aliases: [Stride Time]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: high
related_nodes: []
source_nodes: [running_anderson_step_rate_2022]
relationships:
  required_events: [running_initial_contact]
  supports: [running_running_cycle, running_variability, running_fatigue_drift]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 11
hub_score: 13
centrality: 0.098
updated: 2026-09-09
---

# Running - Stride Time

## Definition

A Level A camera-derived measurement or named proxy. Left stride time median was 704 ms across five valid cycles.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

A tracked foot or ankle across two reliable same-side initial contacts.

## Calculation Concept

Elapsed time from initial contact of one foot to the next initial contact of the same foot.

## Normalisation

Report milliseconds and side; retain speed and trial context.

## Recommended Camera View

- side
- front
- back

## Confidence / Quality Gate

Require two successive valid same-side contacts and no tracking discontinuity. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_running_cycle]]
- [[running_variability]]
- [[running_fatigue_drift]]

## What It Cannot Prove

Stride time alone does not quantify stride length, economy, or tissue state. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_anderson_step_rate_2022]]

## Reporting Language

Permitted: "Left stride time median was 704 ms across five valid cycles."

## Forbidden Claims

- Do not report: "Slow stride time means inefficient running."
