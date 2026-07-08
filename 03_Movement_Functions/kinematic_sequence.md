---
id: kinematic_sequence
type: Movement Pattern
preferred_name: Kinematic Sequence
aliases: [rotational sequence, swing sequencing, kinematic sequence timing]
category: Biomechanics
short_definition: "The sequential acceleration and deceleration of body segments from the ground up (Pelvis → Thorax → Lead Arm → Club) to transfer energy and maximize endpoint velocity."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Explains how the ground reaction moment initiates the pelvic rotation that begins the kinematic sequence."
  - source_id: golf_decoded_six_phases_swing
    evidence_level: 4
    supports: "Identifies sequence phases and transition timing in the golf swing."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [ground_reaction_moment, torque, angular_momentum, energy_transfer, force_transmission, functional_lines]
confidence: high
review_status: active_spec
relationship_count: 9
hub_score: 20
centrality: 0.18
updated: 2026-07-08
---

# Kinematic Sequence

## Definition

The **Kinematic Sequence** is a biomechanical model describing the coordination and timing of body segments during high-velocity rotational activities. In a powerful, efficient golf swing, the kinematic sequence progress from the ground up, following a specific order of peak angular velocity and subsequent deceleration:

$$\text{Pelvis} \rightarrow \text{Thorax (Rib Cage)} \rightarrow \text{Lead Arm} \rightarrow \text{Club}$$

Each segment accelerates and reaches its peak velocity, then decelerates rapidly, transferring its momentum to the next adjacent segment, which reaches a higher peak velocity.

---

## Why It Matters

The kinematic sequence is the execution phase of the movement chain. Pushing off the ground generates torque, which is sequentially transmitted through the segments to multiply velocity. If the sequence is out of order (e.g., the upper body rotates before the lower body, known as an *over-the-top* move), energy is lost, velocity is reduced, and compensations occur.

---

## Biomechanical Mechanics (Level 3 Evidence)

An efficient kinematic sequence relies on two mechanical factors:

### 1. Proximal-to-Distal Acceleration
- **Pelvic Start**: Lower body ground reaction moments initiate pelvic rotation.
- **Segment Lag**: The upper body (thorax) initially lags behind the pelvis, creating eccentric stretch in the core and [[functional_lines]] (abdominal obliques and thoracolumbar fascia).
- **Core Stretch**: This stretch triggers the stretch-shortening cycle, allowing the thorax to accelerate rapidly, overtaking the pelvis.
- **Shoulder Release**: The lead arm similarly lags behind the thorax, stretching the chest/shoulder fascia before whipping forward.

### 2. Segment Deceleration (Momentum Transfer)
- A segment must decelerate to transfer its momentum. When the pelvis stops or slows down target-ward, its kinetic energy is not lost; it is transferred up to the thorax.
- This requires strong stability and joint deceleration capabilities (e.g., lead hip internal rotation stability, lead leg bracing).
- If the lower body continues to slide or spin without decelerating, the energy is "bled off," reducing the final speed of the clubhead.

---

## App Hypotheses & App Logic (Level 5 Evidence)

### Metrics Integration
The kinematic sequence is monitored via **Energy Transmission Efficiency (ETE)**. ETE rates:
- The order of segment peaks.
- The time delays (lag) between segment peaks (ideally 20–40ms between pelvis and thorax).
- The deceleration rate (slope) of the pelvic and thoracic curves.

### MediaPipe Proxies
Kinematic sequence timing is tracked in the app using:
- **Pelvic Rotation Angle Velocity**: Derived from the left-right hip line.
- **Thorax Rotation Angle Velocity**: Derived from the left-right shoulder line.
- **Lead Arm Angular Velocity**: Derived from the lead shoulder-to-wrist line.
- **Timing Analysis**: Detecting the timestamps of peak angular velocities for these three lines to verify if they occur in the correct order.

---

## Relationships

| Relationship | Target | Description |
| :--- | :--- | :--- |
| connects_to | [[energy_transfer]] | Kinematic sequence is the temporal map of energy transfer. |
| connects_to | [[ground_reaction_moment]] | GRM is the initiator of the sequence's first link (pelvis). |
| connects_to | [[functional_lines]] | The fascial lines stretch and recoil to transfer the speed between segments. |
| active_during | [[golf_swing_transition]] | The sequence begins and is set during the transition. |

---

## Open Questions

- What is the difference in sequence timing profiles between male and female golfers due to differences in baseline joint laxity?
- How much does a restriction in lead ankle dorsiflexion alter the timing of peak pelvic deceleration?
