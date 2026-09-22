---
id: running_initial_contact
canonical_id: running.events.initial_contact
type: Movement Pattern
running_node_type: event
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: Running - Initial Contact
aliases: [Initial Contact]
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
  child_concepts: [running_landing_relationship, running_foot_strike, running_tibial_inclination, running_knee_flexion_at_contact, running_contact_time]
  constrained_by: [running_measurement_limitations, running_evidence_gate]
confidence: medium
review_status: canonical_definition
relationship_count: 18
hub_score: 33
centrality: 0.161
updated: 2026-09-09
---

# Running - Initial Contact

## Definition

The estimated frame at which a foot first establishes ground contact and begins stance.

## Why It Matters

Reliable event boundaries are prerequisites for downstream timing, landing, compression, and multi-stride calculations.

## Observable Inputs

Foot/heel/toe trajectory relative to a stable ground reference and neighbouring frames.

## Camera and Quality Gate

Side view is preferred. Require an unoccluded contact foot, adequate frame rate, and consistent kinematic transition; label as estimated. Apply [[running_measurement_limitations]] and [[running_evidence_gate]].

## Supports

- [[running_landing_relationship]]
- [[running_foot_strike]]
- [[running_tibial_inclination]]
- [[running_knee_flexion_at_contact]]
- [[running_contact_time]]

## What It Cannot Prove

An event frame does not measure force, pressure, impulse, tissue loading, or injury risk.

## Reporting Language

Permitted: "Right initial contact was estimated at 2.34 s with high event confidence."

## Forbidden Claims

Do not describe ground reaction, braking, propulsion, or tissue state as measured from the event alone.

## Literature Evidence

- [[till_yes_running_literature_foundation]]
