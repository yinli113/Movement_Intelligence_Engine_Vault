---
id: running_longer_landing_strategy
canonical_id: running.interpretation.longer_landing_strategy
type: App Logic
running_node_type: biomechanical_interpretation
evidence_level: 5
running_claim_level: C
status: canonical
preferred_name: Running - Longer Landing Strategy
aliases: [Longer Landing Strategy]
domain: running
directly_measured: false
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_anderson_step_rate_2022, running_schubert_stride_frequency_2014]
relationships:
  required_inputs: [running_long_forward_landing_pattern, running_cadence, running_contact_time, running_horizontal_progression]
  supports: [running_cross_body_myofascial_hypothesis]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 14
hub_score: 23
centrality: 0.125
updated: 2026-09-09
---

# Running - Longer Landing Strategy

## Definition

A cautious interpretation that the runner used a relatively longer forward landing organisation in the observed trial.

## Why It Matters

This node makes the transition from observed patterns to a bounded biomechanical interpretation explicit.

## Required Inputs

- [[running_long_forward_landing_pattern]]
- [[running_cadence]]
- [[running_contact_time]]
- [[running_horizontal_progression]]

## Evidence Gate

Apply [[running_evidence_gate]]. Require mutually supporting inputs, matched literature, sufficient confidence, and contextual wording.

## Camera Boundary

side view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_cross_body_myofascial_hypothesis]]

## What It Cannot Prove

It cannot quantify braking impulse or establish cause, injury risk, or a universal need to change cadence.

## Literature Evidence

- [[running_anderson_step_rate_2022]]
- [[running_schubert_stride_frequency_2014]]

## Reporting Language

Permitted: "The combined landing-offset, timing, and progression findings may reflect a longer landing strategy on the right."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
