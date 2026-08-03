---
id: golf_movement_sequence
type: Golf Phase
preferred_name: Golf Full-Body Movement Sequence
aliases: [golf sequence, full-body golf sequence, golf segment sequence]
category: Golf
short_definition: "The full observable golf-swing sequence from feet and ankles through knees, pelvis, COM proxy, thorax, shoulders, elbows, wrists, and hands to the head — analysed as a coordinated whole rather than only hips and knees."
evidence_level: 4
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Grounds pelvis translation/rotation and golfer-ground interaction in instrumented mechanics."
  - source_id: golf_decoded_six_phases_swing
    evidence_level: 4
    supports: "Provides the applied whole-swing context the sequence is read within."
relationships:
  parent_concepts: [golf_swing]
  child_concepts: []
  related_concepts: [x_factor, golf_swing_events, segment_angle_metrics, kinematic_sequence, energy_flow, stretch_shortening_cycle, personalised_movement_intelligence]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 9
hub_score: 0
centrality: 0.0
updated: 2026-07-27
---

# Golf Full-Body Movement Sequence

## Definition

The golf module analyses the **whole observable sequence**, not only the hips and knees. The segments considered, in chain order, are: feet and ankles → knees → pelvis → COM proxy → thorax → shoulders → elbows → wrists → hands → head.

## Why It Matters

Restricting analysis to hips and knees misses where most sequencing information lives: ground contact, trunk organisation, and upper-limb timing. The full chain is read as one coordinated organisation, judged against the person's own pattern ([[personalised_movement_intelligence]]).

## Analysis Priorities

In approximate priority order for whole-body sequencing:

1. pelvis translation toward the target;
2. pelvis rotation;
3. thorax rotation;
4. pelvis-thorax dissociation (see [[x_factor]]);
5. transition timing;
6. lead-side organisation;
7. trail-side unloading;
8. upper-limb sequencing;
9. wrist and hand timing;
10. radius (hand-path) changes;
11. head stability — **without** assuming the head must remain perfectly still.

## Role of Hip and Knee

Hip (pelvis) rotation is generally more central to whole-body sequencing than isolated knee flexion. Knee behaviour remains useful: it contributes to support, force redirection posture, pelvis motion, and individual compensation strategies — see [[segment_angle_metrics]] for shank/thigh organisation relative to the ground.

## Interpretation Layers

### Measured Mechanics — Levels 3–4

Instrumented pelvis translation/rotation and segment sequencing are Level 3; the applied whole-swing reading is Level 4.

### Fascial Interpretation — Levels 1–2 plus explicit inference

Lead-side organisation and trail-side unloading *may be associated with* lateral-, spiral-, and functional-line behaviour; interpretive only.

### App Hypothesis — Level 5

Per-segment camera descriptors (positions, orientations, timings) are Level 5 and carry the view/landmark/confidence context required by [[metric_evidence_classification]].

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[golf_swing]] | The sequence is the swing read as a whole. |
| timed_by | [[golf_swing_events]] | Segment timing is event-referenced. |
| includes | [[x_factor]] | Pelvis-thorax dissociation is one element. |
| measured_with | [[segment_angle_metrics]] | Support organisation via segment orientation. |
| sequenced_with | [[kinematic_sequence]] | Segment peak/reversal order. |
| expresses | [[energy_flow]] | Whole-sequence continuity is the flow signal. |

## Parent Concepts

- [[golf_swing]]

## Child Concepts

- None currently.

## Related Concepts

- [[golf_swing_transition]]
- [[stretch_shortening_cycle]]
- [[personalised_movement_intelligence]]

## Evidence Level

Sequence structure is Level 4; instrumented segment mechanics are Level 3; camera sequence descriptors are Level 5.

## App Use

Describe each segment's timing and organisation, then their coordination — never a single joint's verdict. Head motion is reported descriptively; stillness is not treated as a correctness criterion.

## Open Questions

- Which segment-timing panel is most robust to the oblique camera views typical of consumer golf video?
- How should upper-limb sequencing be described when the hands or club leave the frame?
