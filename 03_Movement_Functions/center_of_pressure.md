---
id: center_of_pressure
type: Movement Pattern
preferred_name: Center of Pressure
aliases: [COP, pressure center, foot pressure, weight distribution]
category: Physics
short_definition: "The point on the ground through which the net vertical ground reaction force vector acts; represents the average location of all contact pressures."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Analyses how the Center of Pressure (COP) location under the feet serves as the application point for the net Ground Reaction Force vector."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [ground_reaction_force, ground_reaction_moment, torque, moment_arm, center_of_mass]
confidence: high
review_status: active_spec
relationship_count: 8
hub_score: 14
centrality: 0.16
updated: 2026-07-08
---

# Center of Pressure

## Definition

The **Center of Pressure (COP)** is the point location of the vertical ground reaction force vector's net application. It represents the spatial average of all pressures acting on the contact surface (the soles of the feet). 

While the **Center of Mass (COM)** is a physical balance point inside the body, the COP is an external point of contact on the ground. When both feet are on the ground, the net COP is a combined point situated somewhere between the two feet.

---

## Why It Matters

The COP is the steering wheel of the golf swing. A golfer shifts their pressure (COP) to manipulate the ground reaction force vectors, directing the forces to generate torque. The relationship between where the pressure is applied (COP) and where the body's weight is balanced (COM) determines the magnitude of the moment arm that drives rotation.

---

## Biomechanical Relevance (Level 3 Evidence)

The trajectory of the COP during a high-velocity golf swing is highly coordinated:

### 1. Address to Backswing
- At address, the net COP is centered between the feet.
- During the backswing, the COP shifts towards the trail heel, representing a transfer of pressure to the trail side (reaching roughly 70–80% trail-foot pressure).

### 2. Transition and Downswing
- **Early Shift**: Before the backswing is complete, the COP shifts rapidly target-ward, moving towards the lead toe (lateral pressure shift).
- **Heel Target**: As the downswing progresses, the COP under the lead foot moves from the toe/midfoot back towards the lead heel, facilitating pelvic clearance and rotation.

### 3. COP-COM Contrast
- **COM** represents the displacement of body mass.
- **COP** represents the application of contact force.
- The COP shifts first, acting as the driver that pushes the body to shift the COM. In a proper downswing sequence, the COP shifts to the lead side well before the COM arrives.

---

## App Hypotheses & App Logic (Level 5 Evidence)

### Metrics Integration
The spatial relationship and timing sequence between the COM and COP are evaluated by the **COM–COP Separation Score (CCS)**.

### MediaPipe Proxies
Because standard cameras cannot measure contact pressure, the app estimates COP activity using:
- **Joint Flexion and Weight Distribution Hypotheses**: If the lead knee is flexed and the lead ankle is directly under the pelvis, the app assumes a lead midfoot/toe COP. If the lead leg is extended and the hips are clearing backward, the app infers the COP has shifted to the lead heel.
- **Dynamic Posture Foot Loading**: Tracking ankle and knee joint angles serves as a proxy to model whether pressure is loaded in the toes or heels.

---

## Relationships

| Relationship | Target | Description |
| :--- | :--- | :--- |
| connects_to | [[ground_reaction_moment]] | COP is the starting point of the GRF vector that generates the moment. |
| connects_to | [[moment_arm]] | The distance between the COP and the vertical line of COM defines the moment arm. |
| connects_to | [[center_of_mass]] | The spatial delta between COM and COP determines rotational leverage. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Authoritative source for golfer-ground contact pressure analysis. |

---

## Open Questions

- Can consumer-grade smart insoles (measuring pressure) be integrated with skeletal tracking to provide real-time, high-accuracy COP data to the AI engine?
