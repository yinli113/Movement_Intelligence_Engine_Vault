---
id: running_maximum_compression
canonical_id: running.events.maximum_compression
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Maximum Compression
aliases: [Maximum Compression]
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
  child_concepts: [running_leg_compression_proxy, running_compression_and_rebound]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 8
hub_score: 13
centrality: 0.071
updated: 2026-09-09
---

# Running - Maximum Compression

## Definition

The stance frame with the minimum declared leg-length proxy or lowest declared body-centre proxy, depending on the algorithm.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Continuous stance-side hip/foot geometry and body-centre proxy.

## Camera and Quality Gate

Side view is preferred. Declare the algorithm, require an interior stance minimum, and reject flat/noisy minima. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_leg_compression_proxy]]
- [[running_compression_and_rebound]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Minimum hip-to-foot distance occurred 112 ms after left contact."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
