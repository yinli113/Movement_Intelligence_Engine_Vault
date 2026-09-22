---
id: running_fatigue_drift
canonical_id: running.variability.fatigue_drift
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: Running - Fatigue Drift
aliases: [Fatigue Drift]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_zandbergen_fatigue_2023, running_trowell_fatigue_2025, running_winter_fatigue_2017]
relationships:
  required_inputs: [running_variability, running_running_cycle, running_cadence, running_contact_time, running_vertical_oscillation]
  supports: [running_different_load_distribution_strategy, running_altered_rotational_coordination]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_definition
relationship_count: 32
hub_score: 57
centrality: 0.286
updated: 2026-09-09
---

# Running - Fatigue Drift

## Definition

An early-to-late within-trial trend in a named metric, described as fatigue-related only when the protocol establishes fatigue context.

## Why It Matters

This node makes the transition from measurements to a repeatable movement pattern explicit.

## Required Inputs

- [[running_variability]]
- [[running_running_cycle]]
- [[running_cadence]]
- [[running_contact_time]]
- [[running_vertical_oscillation]]

## Evidence Gate

Apply [[running_evidence_gate]]. Use multiple valid cycles and retain mean, median, variability, side difference, trend, valid count, and confidence.

## Camera Boundary

side or front or back view under the declared setup. Apply [[running_measurement_limitations]].

## What It Can Support

- [[running_different_load_distribution_strategy]]
- [[running_altered_rotational_coordination]]

## What It Cannot Prove

Time trend alone does not prove physiological fatigue or identify its cause.

## Literature Evidence

- [[running_zandbergen_fatigue_2023]]
- [[running_trowell_fatigue_2025]]
- [[running_winter_fatigue_2017]]

## Reporting Language

Permitted: "Contact-time proxy increased from early to late trial; the recording protocol did not independently measure fatigue."

## Forbidden Claims

Do not convert this node into a force, injury, diagnosis, tissue-state, universal-good/bad, or treatment claim. See [[running_reporting_guardrails]].

## Open Questions

- What validation dataset and minimum repeat count are required before this definition becomes executable app logic?
