---
id: running_midstance
canonical_id: running.events.midstance
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Midstance
aliases: [Midstance]
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
  child_concepts: [running_com_progression, running_trunk_lean]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 8
hub_score: 11
centrality: 0.071
updated: 2026-09-09
---

# Running - Midstance

## Definition

A stance interval/event proxy when the body-centre proxy progresses over or nearest the support relationship; it is not assumed to equal maximum compression.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Support-foot identity, body-centre-proxy trajectory, and stance boundaries.

## Camera and Quality Gate

Side view is preferred. Require valid stance events and stable side-view geometry; do not infer force crossover. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_com_progression]]
- [[running_trunk_lean]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Midstance proxy occurred 94 ms after right contact."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
