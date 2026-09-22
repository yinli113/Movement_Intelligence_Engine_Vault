---
id: running_running_economy
canonical_id: running.interpretation.running_economy
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Running Economy
aliases: [Running Economy]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_van_hooren_economy_2024]
relationships:
  required_inputs: [running_kinematics_are_not_kinetics]
  supports: [running_till_yes_progression_ratio]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 11
hub_score: 18
centrality: 0.098
updated: 2026-09-09
---

# Running - Running Economy

## Definition

A physiological construct describing energy or oxygen cost at a standardised submaximal running speed.

## Why It Matters

This node makes the transition from observed patterns to a bounded biomechanical interpretation explicit.

## Required Inputs

- [[running_kinematics_are_not_kinetics]]

## Evidence Gate

Apply [[running_evidence_gate]]. Require mutually supporting inputs, matched literature, sufficient confidence, and contextual wording.

## Camera Boundary

No camera directly measures this construct. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_till_yes_progression_ratio]]

## What It Cannot Prove

Running economy cannot be directly measured or scored from pose video alone.

## Literature Evidence

- [[running_van_hooren_economy_2024]]

## Reporting Language

Permitted: "TillYes reports a kinematic profile; metabolic running economy was not measured."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
