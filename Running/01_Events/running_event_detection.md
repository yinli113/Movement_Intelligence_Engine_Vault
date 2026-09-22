---
id: running_event_detection
canonical_id: running.events.detection
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Event Detection
aliases: [Event Detection]
domain: running
directly_measured: true
proxy_measurement: true
camera_views: [side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [till_yes_running_literature_foundation]
relationships:
  parent_concepts: []
  child_concepts: [running_initial_contact, running_midstance, running_maximum_compression, running_toe_off, running_flight_phase]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 10
hub_score: 19
centrality: 0.089
updated: 2026-09-09
---

# Running - Event Detection

## Definition

The quality-gated process that identifies running-cycle event frames from pose/video signals.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Foot/ankle trajectories, body-centre-proxy motion, ground-plane relationship, and monotonic timestamps.

## Camera and Quality Gate

Side view is preferred. Require event-order plausibility, temporal separation, side assignment, and confidence; retain manual-review and unavailable states. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_initial_contact]]
- [[running_midstance]]
- [[running_maximum_compression]]
- [[running_toe_off]]
- [[running_flight_phase]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Seven valid right contacts and six valid left contacts were detected; one uncertain event was excluded."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
