---
id: movement_chain_model
type: Movement Pattern
preferred_name: Biomechanical Movement Chain Model
aliases: [movement chain, force flow, kinetic chain, movement_chain]
category: Biomechanics
short_definition: "A complete framework tracing movement generation from ground-reaction forces through internal fascial line loading to joint motion, performance, and compensations."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Validates the transition from Ground Reaction Forces and Center of Pressure shifts to Ground Reaction Moments and external torque generation."
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Provides the model for how myofascial lines distribute force and transmit energy across multiple joints."
relationships:
  parent_concepts: []
  child_concepts: [ground_reaction_force, ground_reaction_moment, torque, functional_lines]
  related_concepts: [energy_transfer, force_transmission, kinematic_sequence]
confidence: high
review_status: active_spec
relationship_count: 16
hub_score: 34
centrality: 0.32
updated: 2026-07-08
---

# Biomechanical Movement Chain Model

## Definition

The **Biomechanical Movement Chain Model** is a unified framework modeling how human movement is generated, transmitted, and expressed. It describes the sequential propagation of mechanical energy and forces through the body, defined by the following path:

$$\text{Ground Reaction Forces (GRF)} \rightarrow \text{Ground Reaction Moments (GRM)} \rightarrow \text{External Torque} \rightarrow \text{Body Loading} \rightarrow \text{Myofascial Line Loading} \rightarrow \text{Energy Transmission} \rightarrow \text{Joint Motion} \rightarrow \text{Functional Movement} \rightarrow \text{Performance / Compensation}$$

---

## The Movement Chain Breakdown

### 1. Ground Reaction Forces (GRF)
The golfer initiates movement by applying force into the ground. The ground pushes back with equal and opposite force vectors ($F_{\text{GRF}}$), acting through the **Center of Pressure (COP)**.
*(Evidence Level: 2 - Physics/General Biomechanics)*

### 2. Ground Reaction Moments (GRM)
If the GRF vector does not pass directly through the body's **Center of Mass (COM)**, it generates a moment (rotational effect) around the COM. The magnitude of this moment is the force multiplied by the perpendicular distance (moment arm) from the vector to the COM.
*(Evidence Level: 3 - Golf Biomechanics)*

### 3. External Torque
The net sum of all GRMs (frontal, sagittal, and horizontal planes) and foot pivoting moments creates the net **External Torque** acting to rotate the golfer's body skeleton.
*(Evidence Level: 2 - Physics)*

### 4. Body Loading
To absorb and redirect this external torque, the body undergoes mechanical loading. The skeleton, joints, and soft tissues act as a suspension system to brace against or yield to these forces.
*(Evidence Level: 2 - General Biomechanics)*

### 5. Myofascial Line Loading
As the bones move and joints resist the external torque, tension is distributed along continuous anatomical pathways. The **Fascial Lines** (such as the Functional Lines or Spiral Line) act as tension-sharing cables, stretching eccentrically (elastic loading) to store mechanical energy.
*(Evidence Level: 1 - Anatomy Trains)*

### 6. Energy Transmission
The stored elastic energy in the fascial system is transmitted rapidly along the kinetic chain. As the muscles contract and the fascia recoils, energy is transferred sequentially from the lower extremity, through the core/pelvic hubs, and into the upper body.
*(Evidence Level: 2 - General Biomechanics)*

### 7. Joint Motion
The transmission of energy and local muscle contractions result in angular displacement at individual joints (e.g., hip internal rotation, thoracic rotation, shoulder external rotation).
*(Evidence Level: 2 - Stable Anatomy)*

### 8. Functional Movement
The coordinated, multi-joint actions combine to produce complex functional patterns (e.g., the golf downswing transition and release).
*(Evidence Level: 4 - Applied Coaching)*

### 9. Performance / Compensation
- **Performance**: High energy transmission efficiency, correct timing sequence, and maximum endpoint velocity (e.g., clubhead speed).
- **Compensation**: If any link in the chain is restricted (e.g., limited ankle dorsiflexion or poor lead hip rotation), the force cannot transmit smoothly. The body creates compensatory patterns (e.g., pelvic sway, early arm release, neck/jaw bracing) to generate speed or maintain balance, leading to inefficiency and injury risk.
*(Evidence Level: 5 - App-Logic Hypotheses)*

---

## Why It Matters for AI Movement Reasoning

Traditional movement assessment apps report joint angles or posture in isolation. This model allows the AI reasoning engine to analyze **why** a movement pattern or compensation occurs by tracing it back to its root cause in the chain:
- If a client has an *early release (casting)* at joint motion, the AI does not just flag the arms.
- It traces backward: Casting $\rightarrow$ Poor Energy Transmission $\rightarrow$ Decreased Elastic Loading in the Front Functional Line $\rightarrow$ Lack of lead hip deceleration (Body Loading) $\rightarrow$ Insufficient Ground Reaction Moment $\rightarrow$ Failure to push off the lead foot (GRF).
- The root cause is a foot-ground interaction issue, not an arm issue.

---

## Relationships

| Node in Chain | Canonical Note | Role in Golf Swing |
| :--- | :--- | :--- |
| **GRF** | [[ground_reaction_force]] | Pushing into the lead foot during transition. |
| **GRM** | [[ground_reaction_moment]] | Converting lead foot push into pelvic rotation. |
| **Torque** | [[torque]] | Axial torque rotating the pelvis and torso. |
| **Fascial Loading** | [[functional_lines]] | Stretching the Back Functional Line to store elastic energy. |
| **Energy Trans.** | [[energy_transfer]] | Transmitting power up the core and through the shoulder complex. |
| **Joint Motion** | [[hip_internal_rotation]] / [[thoracic_rotation]] | Coordinated joint rotations delivering the club. |
| **Compensation** | [[neck_tension]] / [[jaw_clenching]] | Bracing due to poor force transfer. |

---

## Open Questions

- What is the mathematical decay rate of force transmission across the lumbodorsal fascia crossing?
- Can 2D video analysis accurately identify the breakdown point in this chain, or does it require inertial sensors/force plates?
