---
id: running_leg_compression_proxy
canonical_id: running.compression.leg_compression_proxy
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Leg Compression Proxy
aliases: [Leg Compression Proxy]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: medium
related_nodes: []
source_nodes: [running_meyer_stiffness_2023, running_masson_stiffness_2026]
relationships:
  required_events: [running_initial_contact, running_maximum_compression]
  supports: [running_compression_and_rebound, running_different_load_distribution_strategy, running_left_right_asymmetry]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 16
hub_score: 27
centrality: 0.143
updated: 2026-09-09
---

# Running - Leg Compression Proxy

## Definition

A Level A camera-derived measurement or named proxy. Right stance showed a larger kinematic leg-compression proxy than left.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]
- [[running_maximum_compression]]

## Required Landmarks

Stance-side hip and ankle/foot reference points through stance.

## Calculation Concept

Compare hip-to-contact-foot distance at initial contact with the minimum distance during stance: (contact length - minimum length) / contact length.

## Normalisation

Report as a percentage and retain the landmark pair, view, and contact-foot reference.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require a stable side view, continuous stance-side tracking, valid contact, and valid maximum-compression event. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_compression_and_rebound]]
- [[running_different_load_distribution_strategy]]
- [[running_left_right_asymmetry]]

## What It Cannot Prove

This kinematic ratio is not leg stiffness, tendon stiffness, force, or stored elastic energy. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_meyer_stiffness_2023]]
- [[running_masson_stiffness_2026]]

## Reporting Language

Permitted: "Right stance showed a larger kinematic leg-compression proxy than left."

## Forbidden Claims

- Do not report: "Leg stiffness was low."
- Do not report: "Elastic energy storage was poor."
