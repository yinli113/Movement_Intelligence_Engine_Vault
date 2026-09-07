---
id: personalised_movement_intelligence
type: Movement Function
preferred_name: Personalised Movement Intelligence
aliases: [individual movement baseline, personal pattern discovery, individualised movement analysis]
category: Motor Control
short_definition: "Framework for helping each user discover their most effective repeatable movement pattern from their own longitudinal data, rather than comparing them against an elite athlete or a fixed ideal position."
evidence_level: 2
evidence:
  - source_id: czaprowski_nonstructural_posture_2018
    evidence_level: 1
    supports: "Posture and movement are questions about individual organisation and adaptability, not deviations from one ideal."
  - source_id: gray_cook_movement_2010
    evidence_level: 1
    supports: "Screening respects individual variation; patterns are interpreted before parts."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [temporal_movement_metrics, energy_flow, movement_reporting_standards, metric_evidence_classification, x_factor, stretch_shortening_cycle]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 11
hub_score: 24
centrality: 0.099
updated: 2026-07-27
---

# Personalised Movement Intelligence

## Definition

The engine helps each user discover **their own most effective repeatable pattern** — it does not coach them to copy another person's movement or a fixed ideal position. People differ in anatomy, proportions, mobility, injury history, and coordination strategies; effectiveness is judged within the individual.

## Why It Matters

This is the core TillYes principle: the aim is not to maximise one angle or reproduce one ideal movement, but to understand how **each person** loads, coordinates, transfers, and releases movement so they can find a powerful, fluent, and sustainable pattern that works for their own body.

## Conceptual Distinctions

| Concept | Meaning |
| :--- | :--- |
| population reference range | broad context from many people; background, not a target |
| individual baseline | the person's own established pattern |
| session-to-session change | drift of the baseline across days or weeks |
| trial-to-trial consistency | repeatability within a session |
| personal best pattern | the person's own most effective observed organisation |
| fatigue-related change | pattern shift under accumulating fatigue |
| pain-limited / injury-modified strategy | an adapted pattern respecting symptoms or injury |
| adaptive variation | a useful, context-appropriate change |
| potentially inefficient compensation | a change that may cost fluency or sustainability |

Where sufficient longitudinal data exists, **the individual's own historical data outweighs population averages** in interpreting any new observation.

## Future Machine-Learning Direction

Future models may seek relationships between movement patterns and outcomes such as **speed, accuracy, balance, comfort, consistency, fatigue, pain response, and performance under different tasks**. They must not manufacture unsupported claims of a single "optimal movement"; personal pattern discovery stays descriptive and outcome-referenced.

## Interpretation Layers

### Measured Mechanics — Levels 2–3

Longitudinal kinematic tracking with declared methods can support within-person change detection.

### Fascial Interpretation — Levels 1–2 plus explicit inference

A person's stable strategy *may be associated with* characteristic line-loading preferences; interpretive only.

### App Hypothesis — Level 5

Baselines, consistency bands, and change alerts computed from camera descriptors are Level 5 and must carry provenance and confidence.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[movement_chain_model]] | Personal patterns are chain organisations. |
| built_from | [[temporal_movement_metrics]] | Consistency and change are temporal descriptors. |
| governs_interpretation_of | [[energy_flow]] | Flow judged against the person's own structure. |
| reported_through | [[movement_reporting_standards]] | Non-judgmental, individual-referenced language. |
| evidenced_by | [[metric_evidence_classification]] | Every personal metric keeps its evidence type. |
| golf_application | [[x_factor]] | Dissociation interpreted within the individual. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[movement_reporting_standards]]
- [[stretch_shortening_cycle]]
- [[segment_angle_metrics]]

## Evidence Level

The framework philosophy is Level 2 (grounded in Level 1 clinical philosophy); instrumented longitudinal tracking is Level 3; camera-derived personal metrics are Level 5.

## App Use

Prefer within-person comparisons: report change relative to the individual baseline and trial consistency, with population ranges only as loose context. Never rank a user against an elite template.

## Open Questions

- How many sessions establish a stable individual baseline for a given descriptor?
- How should fatigue- and pain-related changes be separated from skill drift in the same longitudinal record?
