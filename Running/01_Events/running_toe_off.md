---
id: running_toe_off
canonical_id: running.events.toe_off
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Toe Off
aliases: [Toe Off]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [till_yes_running_literature_foundation]
relationships:
  parent_concepts: [running_event_detection, running_running_cycle]
  child_concepts: [running_contact_time, running_flight_time, running_compression_and_rebound]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 10
hub_score: 17
centrality: 0.089
updated: 2026-09-09
---

# Running - Toe Off

## Definition

The estimated frame when the support foot ends ground contact.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Toe/forefoot/ankle trajectory relative to the ground across neighbouring frames.

## Camera and Quality Gate

Side view is preferred. Require a visible support foot and a consistent departure transition; label as estimated. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_contact_time]]
- [[running_flight_time]]
- [[running_compression_and_rebound]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Right toe-off was estimated at 2.58 s with medium confidence."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
