---
id: running_compression_and_rebound
canonical_id: running.pattern.compression_rebound
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Compression and Rebound
aliases: [Compression and Rebound]
domain: running
directly_measured: false
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_meyer_stiffness_2023, running_masson_stiffness_2026]
relationships:
  required_inputs: [running_initial_contact, running_maximum_compression, running_toe_off, running_leg_compression_proxy, running_vertical_oscillation, running_contact_time]
  supports: [running_different_load_distribution_strategy, running_spring_mass_model]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 18
hub_score: 29
centrality: 0.161
updated: 2026-09-09
---

# Running - Compression and Rebound

## Definition

A multi-measurement pattern describing descent/shortening after contact and rise/re-extension toward toe-off.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_initial_contact]]
- [[running_maximum_compression]]
- [[running_toe_off]]
- [[running_leg_compression_proxy]]
- [[running_vertical_oscillation]]
- [[running_contact_time]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

side view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_different_load_distribution_strategy]]
- [[running_spring_mass_model]]

## What It Cannot Prove

It cannot establish stiffness, force, elastic energy, muscle action, or tissue loading.

## Literature Evidence

- [[running_meyer_stiffness_2023]]
- [[running_masson_stiffness_2026]]

## Reporting Language

Permitted: "Right stance showed greater kinematic compression and a later transition from maximum compression toward toe-off."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
