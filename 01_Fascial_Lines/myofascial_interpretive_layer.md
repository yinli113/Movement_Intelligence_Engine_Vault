---
id: myofascial_interpretive_layer
type: Spec
preferred_name: Myofascial Interpretive Layer
aliases: [myofascial interpretation rules, fascial-line interpretation layer, cautious fascial language]
category: Fascial Line
short_definition: "Interpretive layer that associates coordinated movement patterns with relevant anatomical continuities using cautious, non-causal language — never treating MediaPipe landmarks as proof of activation, fascial force, tissue stiffness, or energy storage."
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Defines the myofascial continuities (Functional, Spiral, Superficial Front/Back, Deep Front, Lateral, and Arm Lines) used as the interpretive anatomy."
relationships:
  parent_concepts: [functional_lines]
  child_concepts: []
  related_concepts: [functional_lines, spiral_line, deep_front_line, lateral_line, superficial_front_line, superficial_back_line, x_factor, stretch_shortening_cycle, metric_evidence_classification, movement_reporting_standards]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 12
hub_score: 0
centrality: 0.0
updated: 2026-07-27
---

# Myofascial Interpretive Layer

## Definition

Myofascial concepts are used as an **interpretive layer**, not as directly measured facts. The engine may associate a coordinated movement pattern with relevant anatomical continuities, but the association is always a labelled interpretation sitting on top of the kinematics — never a measurement of tissue behaviour.

## Relevant Anatomical Continuities

Depending on the pattern, interpretation may reference:

- [[functional_lines]] (Back, Front, Ipsilateral);
- [[spiral_line]];
- [[superficial_front_line]] and [[superficial_back_line]];
- [[deep_front_line]];
- [[lateral_line]];
- the Arm Lines.

For rotational sports such as golf, particular attention goes to **contralateral connections** between the pelvis, trunk, shoulder girdle, and upper limbs — the pathways that cross the body during rotation.

## Required Cautious Language

Reports and interpretations use phrasing such as:

- "may be consistent with";
- "could reflect";
- "is associated with";
- "suggests a possible loading strategy";
- "is an indirect proxy for".

## Hard Boundary

MediaPipe landmarks do **not** prove muscle activation, fascial force, tissue stiffness, or energy storage. This layer never converts a camera observation into a tissue-level claim, and it never creates a deterministic path from one landmark measurement to one muscle diagnosis. It sits under [[metric_evidence_classification]] and the Kinetic Proxy Non-Upgrade Rule.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[functional_lines]] | Uses the Anatomy Trains line model as interpretive anatomy. |
| interprets | [[x_factor]] | Dissociation-release may be consistent with line loading. |
| interprets | [[stretch_shortening_cycle]] | Smooth SSC may be associated with elastic line sharing. |
| governed_by | [[metric_evidence_classification]] | Every association keeps its interpretive type. |
| expressed_through | [[movement_reporting_standards]] | Cautious wording is enforced in reports. |

## Parent Concepts

- [[functional_lines]]

## Child Concepts

- None currently.

## Related Concepts

- [[functional_lines]]
- [[spiral_line]]
- [[energy_flow]]

## Evidence Level

The interpretive anatomy is Level 1; each specific association is a separately labelled vault interpretation (Level 4–5), never a measured tissue fact.

## App Use

Attach myofascial associations to patterns only with cautious wording and an explicit interpretive-hypothesis type. Where camera data cannot support the association, omit it rather than soften it into an implication.

## Open Questions

- Which minimal evidence would let a specific pattern-to-line association graduate from interpretation to a testable hypothesis?
- How should the layer handle patterns consistent with several competing line explanations?
