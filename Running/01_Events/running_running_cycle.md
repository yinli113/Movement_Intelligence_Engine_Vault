---
id: running_running_cycle
canonical_id: running.events.cycle
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Running Cycle
aliases: [Running Cycle]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [till_yes_running_literature_foundation]
relationships:
  parent_concepts: [running_event_detection]
  child_concepts: [running_initial_contact, running_midstance, running_maximum_compression, running_toe_off, running_flight_phase]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 27
hub_score: 50
centrality: 0.241
updated: 2026-09-09
---

# Running - Running Cycle

## Definition

One same-side initial contact to the next same-side initial contact, containing stance and flight/swing intervals.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Successive same-side contacts and all intervening valid events.

## Camera and Quality Gate

Side view is preferred. Require valid start and end contacts with no unresolved side switch or tracking discontinuity. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_initial_contact]]
- [[running_midstance]]
- [[running_maximum_compression]]
- [[running_toe_off]]
- [[running_flight_phase]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Five complete right running cycles passed the event-quality gate."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
