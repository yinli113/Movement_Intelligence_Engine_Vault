---
id: running_flight_phase
canonical_id: running.events.flight_phase
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Flight Phase
aliases: [Flight Phase]
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
  child_concepts: [running_flight_time]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 7
hub_score: 10
centrality: 0.062
updated: 2026-09-09
---

# Running - Flight Phase

## Definition

The interval in running when neither foot is classified in ground contact.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Bilateral foot trajectories and valid toe-off/contact boundaries.

## Camera and Quality Gate

Side view is preferred. Require visible feet and stable ground reference; otherwise flight status is unavailable. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_flight_time]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "A flight interval of 78 ms was estimated between right toe-off and left contact."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
