---
id: running_spring_mass_model
canonical_id: running.biomechanics.spring_mass_model
type: App Logic
running_node_type: biomechanical_interpretation
evidence_level: 5
running_claim_level: C
status: canonical
preferred_name: Running - Spring Mass Model
aliases: [Spring Mass Model]
domain: running
directly_measured: false
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_meyer_stiffness_2023, running_stiffness_overview_2021, running_masson_stiffness_2026, running_mass_spring_damper_2012]
relationships:
  required_inputs: [running_contact_time, running_flight_time, running_leg_compression_proxy, running_vertical_oscillation]
  supports: [running_compression_and_rebound]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 14
hub_score: 21
centrality: 0.125
updated: 2026-09-09
---

# Running - Spring Mass Model

## Definition

A simplified conceptual model in which the body's mass and support leg show compression and rebound during running.

## Why It Matters

This node makes the transition from observed patterns to a bounded biomechanical interpretation explicit.

## Required Inputs

- [[running_contact_time]]
- [[running_flight_time]]
- [[running_leg_compression_proxy]]
- [[running_vertical_oscillation]]

## Evidence Gate

Apply [[running_evidence_gate]]. Require mutually supporting inputs, matched literature, sufficient confidence, and contextual wording.

## Camera Boundary

side view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_compression_and_rebound]]

## What It Cannot Prove

It does not prove tissue stiffness, tendon energy storage, force, or an optimal stiffness value.

## Literature Evidence

- [[running_meyer_stiffness_2023]]
- [[running_stiffness_overview_2021]]
- [[running_masson_stiffness_2026]]
- [[running_mass_spring_damper_2012]]

## Reporting Language

Permitted: "Observed stance kinematics can be described with a spring-mass analogy, while stiffness remains unmeasured without force data."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
