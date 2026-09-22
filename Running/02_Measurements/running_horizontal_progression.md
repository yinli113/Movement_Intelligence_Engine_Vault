---
id: running_horizontal_progression
canonical_id: running.body_centre.horizontal_progression
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Horizontal Progression
aliases: [Horizontal Progression]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_van_hooren_economy_2024]
relationships:
  required_events: [running_running_cycle]
  supports: [running_com_progression, running_till_yes_progression_ratio, running_longer_landing_strategy]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 14
hub_score: 20
centrality: 0.125
updated: 2026-09-09
---

# Running - Horizontal Progression

## Definition

A Level A camera-derived measurement or named proxy. Horizontal body-centre-proxy progression remained consistent across the analysed overground strides.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_running_cycle]]

## Required Landmarks

A valid body-centre proxy trajectory and a stable/calibrated horizontal image frame.

## Calculation Concept

Horizontal displacement or velocity of the body-centre proxy across a defined time or stride interval.

## Normalisation

Use body height, calibrated distance, or explicitly label pixel-space values; retain treadmill versus overground context.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require camera stabilisation and sufficient track length; treadmill recordings need a distinct relative-motion interpretation. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_com_progression]]
- [[running_till_yes_progression_ratio]]
- [[running_longer_landing_strategy]]

## What It Cannot Prove

Horizontal progression is not propulsive force, impulse, or metabolic efficiency. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_van_hooren_economy_2024]]

## Reporting Language

Permitted: "Horizontal body-centre-proxy progression remained consistent across the analysed overground strides."

## Forbidden Claims

- Do not report: "Propulsion was strong because horizontal progression was high."
