---
id: trail_shoulder_external_rotation
type: Movement Pattern
preferred_name: Trail Shoulder External Rotation
aliases: [trail shoulder ER, trail arm external rotation, backswing shoulder load]
short_definition: "Golf-specific shoulder external rotation pattern of the trail arm during backswing completion and transition."
relationships:
  contains: []
  connects_to: [shoulder_joint, thoracic_spine, infraspinatus, teres_minor, deltoid, latissimus_dorsi, serratus_anterior]
  produces: [trail_arm_lag]
  assists: [golf_swing_transition]
  stabilizes: [shoulder_joint]
  limits: []
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [shoulder_external_rotation, planned_trail_shoulder_load_screen]
  improved_by: [planned_trail_shoulder_er_control_drill, planned_thoracic_rotation_breath_drill]
  supported_by: [statpearls_infraspinatus, statpearls_teres_minor, statpearls_rotator_cuff]
  relevant_to: [functional_lines, spiral_line, neck_tension, jaw_clenching, thoracic_rotation]
golf_relevance: "A key MVP traversal node: start here to reason from a visible shoulder pattern back to trunk rotation, fascial-line transfer, neck/jaw compensation, and foot/hip sequencing."
evidence:
  - source_id: statpearls_infraspinatus
    source_type: online_reference
    locator: "NCBI Bookshelf, Infraspinatus Muscle"
    supports: "Infraspinatus contributes to external rotation and shoulder stabilization."
  - source_id: statpearls_teres_minor
    source_type: online_reference
    locator: "NCBI Bookshelf, Teres Minor Muscle"
    supports: "Teres minor contributes to external rotation and rotator cuff stabilization."
  - source_id: statpearls_rotator_cuff
    source_type: online_reference
    locator: "NCBI Bookshelf, Anatomy Rotator Cuff"
    supports: "Rotator cuff muscles stabilize the glenohumeral joint; infraspinatus and teres minor externally rotate the shoulder."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 23
hub_score: 63
centrality: 0.397
updated: 2026-06-29
---

# Trail Shoulder External Rotation

## Relationships

- is_instance_of -> [[shoulder_external_rotation]]
- connects_to -> [[shoulder_joint]]
- connects_to -> [[thoracic_spine]]
- connects_to -> [[infraspinatus]]
- connects_to -> [[teres_minor]]
- connects_to -> [[latissimus_dorsi]]
- connects_to -> [[serratus_anterior]]
- supported_by -> [[functional_lines]]
- supported_by -> [[spiral_line]]
- limited_by -> [[neck_tension]]
- limited_by -> [[jaw_clenching]]
- active_during -> [[golf_swing_transition]]
- assessed_by -> [[shoulder_external_rotation]] as current proxy until a dedicated Assessment node exists
- improved_by -> planned `trail_shoulder_er_control_drill`

## Golf Reasoning

Start here when the visible problem is trail-arm load, shoulder hike, early arm throw, or loss of lag. Do not assume the shoulder is the root cause. Traverse:

[[trail_shoulder_external_rotation]] -> [[thoracic_rotation]] -> [[functional_lines]] -> [[hip_internal_rotation]] -> [[toe_loading]]

Then check compensation signals:

[[trail_shoulder_external_rotation]] -> [[neck_tension]] -> [[jaw_clenching]]

## Evidence Notes

Standard anatomy supports the external-rotation muscle relationships. The golf-specific sequence is a reasoning model that needs assessment and exercise nodes in the next conversion pass.

## Open Questions

- Create `trail_shoulder_load_screen` as an Assessment node.
- Create `trail_shoulder_er_control_drill` as an Exercise node.
