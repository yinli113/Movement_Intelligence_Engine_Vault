---
id: angular_momentum
type: Movement Pattern
preferred_name: Angular Momentum
aliases: [rotational momentum, system angular momentum, L]
category: Physics
short_definition: "The quantity of rotation of a body, which is the product of its moment of inertia and its angular velocity."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Focuses on how external moments acting on the golfer are required to alter the system's angular momentum during the swing."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [ground_reaction_moment, torque, center_of_mass, kinematic_sequence]
confidence: high
review_status: active_spec
relationship_count: 6
hub_score: 10
centrality: 0.12
updated: 2026-07-08
---

# Angular Momentum

## Definition

**Angular Momentum** ($L$) is the measure of the amount of rotation a body has, relative to a specific axis. For a rigid body rotating about a fixed axis, it is the product of the body's **Moment of Inertia** ($I$, its resistance to rotational acceleration) and its **Angular Velocity** ($\omega$):

$$L = I \omega$$

For a dynamic, multi-segment system like the human body and golf club, the total angular momentum is the sum of the angular momenta of all individual segments. 

According to Newton's Second Law for rotation, the rate of change of angular momentum of a system is equal to the net external torque ($\tau$) acting on it:

$$\tau = \frac{dL}{dt}$$

---

## Why It Matters

To swing a golf club at high speeds, the golfer must rapidly increase the angular momentum of the golfer-club system. Since the only way to change the angular momentum is through external torque, the golfer must generate a large net **Ground Reaction Moment (GRM)**. Once generated, this angular momentum is transferred sequentially from the large segments (pelvis, torso) to the smaller segments (arms, hands) and finally to the club.

---

## Biomechanical Relevance (Level 3 Evidence)

The management of angular momentum during the downswing involves two main phases:

### 1. Generation Phase (Transition to Early Downswing)
- Golfer applies force into the ground to create Ground Reaction Moments.
- The net external torque causes a rapid increase in the body's angular momentum, rotating the pelvis and trunk target-ward.

### 2. Transfer Phase (Late Downswing to Impact)
- **Moment of Inertia Manipulation**: By keeping the arms tucked close to the body in the early downswing, the golfer keeps their Moment of Inertia ($I$) low, allowing the body to rotate with a high Angular Velocity ($\omega$).
- **Deceleration & Release**: As the lead arm extends and the club releases, the golfer's body decelerates. Because the total angular momentum of the system must be conserved (or continued via ongoing external forces), decelerating the body causes a massive transfer of angular momentum to the club, resulting in maximum clubhead speed at impact.

---

## App Hypotheses & App Logic (Level 5 Evidence)

### Metrics Integration
The efficiency of momentum transfer is quantified by the **Energy Transmission Efficiency (ETE)** metric in the app.

### MediaPipe Proxies
The app estimates angular velocity and momentum transfer using:
- **Segment Rotational Velocities**: Tracking the peak angular velocity of the pelvis, thorax, and lead arm landmarks.
- **Deceleration Profiling**: Observing the rate at which the pelvis and thorax decelerate before impact. A sharp deceleration profile indicates efficient momentum transfer to the club.

---

## Relationships

| Relationship | Target | Description |
| :--- | :--- | :--- |
| connects_to | [[torque]] | Torque is the rate of change of angular momentum. |
| connects_to | [[ground_reaction_moment]] | GRM is the external torque that changes the system's angular momentum. |
| connects_to | [[kinematic_sequence]] | Kinematic sequence describes the sequential transfer of angular velocity. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Authoritative source for golf system momentum analysis. |

---

## Open Questions

- What is the mathematical correlation between pelvis deceleration rate and final clubhead velocity in amateur versus professional golfers?
