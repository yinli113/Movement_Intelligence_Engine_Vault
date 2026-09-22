---
id: running_foot_strike
canonical_id: running.landing.foot_strike
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Foot Strike
aliases: [Foot Strike]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_anderson_foot_strike_2020, running_burke_foot_strike_injury_2021, running_bovalino_foot_strike_2021, running_almeida_foot_strike_2015]
relationships:
  required_events: [running_initial_contact]
  supports: [running_landing_relationship, running_tibial_inclination, running_knee_flexion_at_contact]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 16
hub_score: 24
centrality: 0.143
updated: 2026-09-09
---

# Running - Foot Strike

## Definition

A Level A camera-derived measurement or named proxy. An estimated rearfoot contact pattern was observed with medium confidence; this is a strategy descriptor.

## Why It Matters

It contributes a bounded observation to the running coordination graph; it must be interpreted with speed, view, repeated strides, and related measurements.

## Required Events

- [[running_initial_contact]]

## Required Landmarks

Heel, forefoot/toe, ankle, and a visible ground reference near contact.

## Calculation Concept

Estimate rearfoot, midfoot, or forefoot contact from foot-segment orientation and which region first approaches the ground at the contact frame.

## Normalisation

No universal score; retain footwear, frame rate, side, and confidence.

## Recommended Camera View

- side

## Confidence / Quality Gate

Require adequate frame rate, an unoccluded foot, and a defensible exact contact frame; otherwise return indeterminate. Apply [[running_evidence_gate]] and return unavailable when the gate fails.

## What It Can Support

- [[running_landing_relationship]]
- [[running_tibial_inclination]]
- [[running_knee_flexion_at_contact]]

## What It Cannot Prove

Foot-strike category alone cannot determine correctness, injury, or running economy. See [[running_kinematics_are_not_kinetics]].

## Related Patterns

See [[running_variability]], [[running_left_right_asymmetry]], and the supported nodes above.

## Multi-Stride Aggregation

Before interpretation, aggregate multiple valid strides where possible: mean, median, standard deviation, valid stride count, left/right difference, early-trial mean, late-trial mean, trend, and confidence. See [[running_variability]] and [[running_fatigue_drift]].

## Literature Evidence

- [[running_anderson_foot_strike_2020]]
- [[running_burke_foot_strike_injury_2021]]
- [[running_bovalino_foot_strike_2021]]
- [[running_almeida_foot_strike_2015]]

## Reporting Language

Permitted: "An estimated rearfoot contact pattern was observed with medium confidence; this is a strategy descriptor."

## Forbidden Claims

- Do not report: "Rearfoot strike is bad."
- Do not report: "Forefoot strike is universally superior."
