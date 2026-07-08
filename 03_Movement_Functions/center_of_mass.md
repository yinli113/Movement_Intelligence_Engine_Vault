---
id: center_of_mass
type: Movement Pattern
preferred_name: Center of Mass
aliases: [COM, center of gravity, COG, body center]
category: Physics
short_definition: "The unique point in space where the weighted relative position of the distributed mass of the body sums to zero; the body's balance point."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Uses the body's COM as the central coordinate point around which external moments (GRMs) act to rotate the body."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, ground_reaction_moment, torque, moment_arm, center_of_pressure]
confidence: high
review_status: active_spec
relationship_count: 9
hub_score: 17
centrality: 0.18
updated: 2026-07-08
---

# Center of Mass

## Definition

The **Center of Mass (COM)** is the point at which the entire mass of the human body is concentrated for mechanical calculations. In a static, upright standing position, the COM is typically located within the pelvis, just anterior to the second sacral vertebra (S2). However, because the human body is segmented and dynamic, the COM moves in response to changes in body posture and segment alignment.

---

## Why It Matters

All external forces (such as gravity and ground reaction forces) act on the body's Center of Mass to determine linear acceleration, and generate moments about the COM to determine rotational acceleration. In golf, the body's COM must move in a controlled, coordinated pattern to maintain balance, dynamic stability, and maximize the moment arm of ground reaction forces.

---

## Biomechanical Relevance (Level 3 Evidence)

In the golf swing, the COM exhibits a specific 3D trajectory:

### 1. Lateral (Target-Ward) Shift
- During the backswing, the COM shifts slightly towards the trail side (roughly 4–5 cm).
- Before the backswing is complete (during the transition phase), the COM shifts back towards the target, moving forward into the lead side.
- **Moments Coupling**: This target-ward shift of the COM relative to a wide lead foot placement increases the horizontal distance (moment arm) between the COM and the lead foot's Center of Pressure (COP).

### 2. Vertical (Downward-Upward) Shift
- **Pelvic Drop**: In the early downswing, the golfer lowers their COM (squatting) to prepare for force generation.
- **Vertical Thrust**: Through impact, the golfer dynamically extends their legs, pushing their COM upward. This vertical acceleration corresponds to the peak vertical Ground Reaction Force ($F_z$).

---

## App Hypotheses & App Logic (Level 5 Evidence)

### Metrics Integration
The relationship between the COM and the foot pressure center is represented by the **COM–COP Separation Score (CCS)** in the app.

### MediaPipe Proxies
Since skeletal tracking cannot measure body mass density, the app uses geometric proxies to calculate the COM:
- **Pelvic Center Proxy**: The midpoint between the left and right hip joint landmarks is the primary proxy for the lower-body COM.
- **Torso Center Proxy**: The midpoint of the pelvis and shoulder centers is used to estimate whole-body COM shifts.
- **Sway and Slide Detectors**: Tracking lateral deviations of this pelvic center proxy relative to the feet boundaries allows the app to detect excessive sway (backswing COM shift beyond trail foot) or slide (downswing COM shift beyond lead foot).

---

## Relationships

| Relationship | Target | Description |
| :--- | :--- | :--- |
| connects_to | [[ground_reaction_moment]] | GRM is calculated as the force acting around the COM axis. |
| connects_to | [[moment_arm]] | The moment arm is the distance from the COM to the line of action. |
| connects_to | [[center_of_pressure]] | The separation between COM and COP determines horizontal force leverage. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Base reference for COM-related torque calculations. |

---

## Open Questions

- How accurately does a simple pelvic midpoint proxy correlate with 3D force-plate-calculated COM in golfers of different body compositions?
