---
id: metric_evidence_classification
type: App Logic
preferred_name: Metric Evidence Classification
aliases: [metric typing rules, evidence-typed metrics, claim-strength classification]
category: App Logic
short_definition: "Rule that every metric or interpretation must declare what kind of claim it is — from directly measured landmark to interpretive hypothesis — together with its source, view and landmark requirements, confidence limits, and error modes."
evidence_level: 5
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Instrumented quantities define the measured end of the classification and its instrumentation requirements."
relationships:
  parent_concepts: [evidence_levels]
  child_concepts: []
  related_concepts: [golf_kinetics_observability_boundary, movement_reporting_standards, temporal_movement_metrics, personalised_movement_intelligence]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 9
hub_score: 19
centrality: 0.081
updated: 2026-07-27
---

# Metric Evidence Classification

## Definition

Every metric or interpretation the engine emits must carry an explicit **claim type** and its evidentiary context. A number without a declared type invites over-claiming; the type tells downstream reports how strong a statement may be.

## Claim-Type Vocabulary

| Type | Meaning |
| :--- | :--- |
| directly measured from landmarks | a landmark coordinate or distance read from the capture |
| calculated from landmarks | geometry computed from landmark coordinates (angle, line, separation) |
| temporal derivative | a rate, timing, or sequence derived from the time series |
| biomechanical proxy | a descriptor standing in for a construct that is not directly measured |
| interpretive hypothesis | a proposed meaning, explicitly labelled as inference |
| domain-specific coaching concept | an applied coaching idea, never promoted to measured fact |

## Required Metadata per Metric

Where possible, each metric records:

- **source** (which capture, algorithm version);
- **evidence level** (per [[evidence_levels]]);
- **camera-view requirement**;
- **landmark requirement** (which landmarks must be visible);
- **confidence limitations**;
- **likely sources of error** (occlusion, oblique view, smoothing, frame rate);
- **dimensionality validity** — valid for 2-D description, or requires 3-D / force-plate data.

## Governing Rule

The classification applies the vault's Kinetic Proxy Non-Upgrade Rule (see [[evidence_levels]] §4): a Level 3 relationship never upgrades a linked Level 5 proxy into a measured kinetic variable. Applied coaching theory is never promoted to the certainty of peer-reviewed biomechanics.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[evidence_levels]] | Applies the five-level hierarchy and non-upgrade rule. |
| enforced_with | [[golf_kinetics_observability_boundary]] | Golf allow-list and prohibited inferences. |
| consumed_by | [[movement_reporting_standards]] | Reports inherit each metric's type and limits. |
| applied_to | [[temporal_movement_metrics]] | Temporal descriptors carry view/frame-rate limits. |
| applied_to | [[personalised_movement_intelligence]] | Baselines keep provenance and confidence. |

## Parent Concepts

- [[evidence_levels]]

## Child Concepts

- None currently.

## Related Concepts

- [[movement_reporting_standards]]
- [[golf_kinetics_observability_boundary]]

## Evidence Level

Level 5 app policy, grounded in the Level 1–4 hierarchy it enforces.

## App Use

Reject any report payload whose metrics lack a declared claim type, evidence level, view/landmark context, and confidence limits. Return `unavailable` rather than a plausible-looking value when requirements are unmet.

## Open Questions

- Should the claim-type vocabulary be a closed enum in the report schema, versioned alongside the algorithm?
- What minimum metadata makes a Level 5 proxy eligible for future validation-promotion review?
