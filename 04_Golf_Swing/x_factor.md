---
id: x_factor
type: Movement Pattern
preferred_name: X-Factor (Pelvis-Thorax Dissociation)
aliases: [x-factor, xfactor, pelvis-thorax separation, pelvis-thorax dissociation, x-factor stretch]
category: Golf
short_definition: "The rotational dissociation between pelvis and thorax during the golf swing, represented as a time-varying curve — not simply 'shoulder turn minus hip turn' — whose value, timing, stretch, and release are all interpreted within the individual's own pattern."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Anchors the kinematics/kinetics boundary and the torsional-separation sequence context; dissociation timing is kinematics, not measured tissue loading."
  - source_id: bourgain_golf_swing_biomechanics_2022
    evidence_level: 3
    supports: "Systematic review confirming the pelvis-thorax dissociation definition, the X-factor-stretch timing variant, and the methodological non-consensus that requires the app to record its own operational definition."
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Provides the fascial-line anatomy through which dissociation is cautiously interpreted; it does not measure dissociation."
relationships:
  parent_concepts: [golf_swing, temporal_movement_metrics]
  child_concepts: []
  related_concepts: [stretch_shortening_cycle, kinematic_sequence, golf_swing_events, golf_movement_sequence, functional_lines, personalised_movement_intelligence, golf_kinetics_observability_boundary]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 14
hub_score: 42
centrality: 0.126
updated: 2026-07-27
---

# X-Factor (Pelvis-Thorax Dissociation)

## Definition

The **X-factor** is represented as **pelvis-thorax rotational dissociation** — the changing rotational offset between the pelvis and the thorax over the swing. It is a **time-varying curve**, not the single static difference "shoulder turn minus hip turn" sampled at one position.

## Why It Matters

Treating the X-factor as one angle at the top of the backswing discards the timing that determines whether the dissociation is doing useful work. The engine tracks the whole curve and its events.

## Temporal Descriptor Set

| Descriptor | Meaning |
| :--- | :--- |
| X-factor at top of backswing | dissociation value at the TB event |
| maximum X-factor | largest dissociation value in the curve |
| time of maximum X-factor | when the maximum occurs (normalised time) |
| X-factor stretch | transition-period increase in dissociation |
| rate of increase / decrease | how quickly dissociation builds and releases |
| pelvis and thorax angular velocities | the segment rates underlying the curve |
| pelvis vs thorax reversal order | whether pelvis reversal precedes thorax reversal |
| pelvis-initiation to thorax-acceleration duration | the inter-segment delay |

## The Transition Principle

Maximum pelvis-thorax dissociation may occur **just after the top of backswing, during early transition**, because the pelvis may begin rotating toward the target while the thorax remains relatively fixed or briefly continues in the opposite direction. This transition increase may be described as **X-factor stretch**.

**X-factor stretch is not automatically better when larger.** Interpretation focuses on whether the dissociation is:

- **dynamically created** (produced by the movement, not forced);
- **appropriately timed** (placed well within the person's sequence);
- **smoothly released** (transferred without abrupt loss);
- **coordinated with the rest of the movement**;
- **compatible with the person's structure and capacity**.

Users must not be coached to forcibly restrict the pelvis or to maximise separation.

## Interpretation Layers

### Measured Mechanics — Level 3

With calibrated 3-D capture, pelvis and thorax orientations and their rates are legitimate kinematics; dissociation timing and reversal order are descriptive sequence features, not measured energy or tissue loading.

### Fascial Interpretation — Levels 1–2 plus explicit inference

A well-timed dissociation-and-release *may be consistent with* elastic load sharing across [[functional_lines]] and related lines; the association is interpretive and never a measured fascial claim.

### App Hypothesis — Level 5

Single-camera dissociation is the `image-plane shoulder-line minus hip-line angle descriptor` tracked over time; see [[golf_kinetics_observability_boundary]]. It is not 3-D torsional separation, stored energy, X-factor efficacy, muscle activation, or fascial loading.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[golf_swing]] | Dissociation is a golf-swing pattern. |
| parent | [[temporal_movement_metrics]] | Interpreted as a curve, not a snapshot. |
| golf_expression_of | [[stretch_shortening_cycle]] | Dissociation-then-release is the golf SSC proxy. |
| timed_by | [[golf_swing_events]] | Maximum may fall in early transition. |
| sequenced_with | [[kinematic_sequence]] | Pelvis-thorax reversal order is a sequence feature. |
| interpreted_within | [[personalised_movement_intelligence]] | Judged against the individual's own pattern. |
| bounded_by | [[golf_kinetics_observability_boundary]] | 2-D descriptor limits. |

## Parent Concepts

- [[golf_swing]]
- [[temporal_movement_metrics]]

## Child Concepts

- None currently.

## Related Concepts

- [[golf_movement_sequence]]
- [[functional_lines]]
- [[energy_flow]]

## Evidence Level

Instrumented dissociation kinematics are Level 3; fascial interpretation is Level 1–2 plus inference; single-camera dissociation descriptors are Level 5.

## App Use

Report the dissociation curve: value at TB, maximum and its timing, transition stretch, rates, segment velocities, and reversal order — each as a camera descriptor with confidence. Never coach "increase your X-factor" or present a larger value as superior by default.

## Open Questions

- What reversal-order and timing bands distinguish smooth from forced dissociation on 2-D video?
- How does dissociation timing covary with a person's anthropometrics and mobility, and can that normal variation be modelled without pathologising it?
