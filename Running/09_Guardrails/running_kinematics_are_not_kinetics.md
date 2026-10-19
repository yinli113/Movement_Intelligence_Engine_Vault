---
id: running_kinematics_are_not_kinetics
canonical_id: running.guardrail.kinematics_not_kinetics
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Kinematics Are Not Kinetics
aliases: [kinematics are not kinetics]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  governs: [running_landing_relationship, running_leg_compression_proxy, running_spring_mass_model, running_running_economy]
  connects_to: [running_measurement_limitations, evidence_levels, ground_reaction_force]
confidence: high
review_status: canonical
relationship_count: 47
hub_score: 92
centrality: 0.42
updated: 2026-09-09
---

# Running - Kinematics Are Not Kinetics

## Rule

Ordinary monocular pose video may describe landmark geometry and timing. It does not directly measure ground-reaction force, braking or propulsive force, joint moments, tendon force, tissue stiffness, metabolic cost, muscle activation, or fascial loading.

## Permitted Language

- "The contacting foot landed farther ahead of the body-centre proxy in this trial."
- "Late-stance hip and ankle landmark geometry showed less extension on the right."

## Forbidden Claims

- "Excessive braking force detected."
- "Propulsive force is low."
- "Achilles tendon stiffness is poor."
- "The Spiral Line is tight."

Return `unavailable_without_kinetic_instrumentation` when a requested quantity is kinetic.

## Relationships

This rule constrains [[running_landing_relationship]], [[running_leg_compression_proxy]], [[running_spring_mass_model]], [[running_running_economy]], and every Level C/D output.
