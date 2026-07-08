---
id: ground_reaction_force
type: Movement Pattern
preferred_name: Ground Reaction Force
aliases: [GRF, ground forces, ground reaction forces, vertical force]
category: Physics
short_definition: "The 3D external force exerted by the ground on the body's feet in response to the body pushing into the ground."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Analyses how 3D GRF vectors act through the Center of Pressure to create rotational moments about the Center of Mass."
  - source_id: golf_decoded_six_phases_swing
    evidence_level: 4
    supports: "Details the role of unweighting and force application during the swing transition and downswing."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: [toe_loading]
  related_concepts: [ground_reaction_moment, center_of_mass, center_of_pressure, energy_transfer, force_transmission, plantar_fascia]
  stable_anatomy: [plantar_fascia, ankle_joint, knee_joint, hip_joint]
  golf_interpretation: [golf_swing_transition, max_unweighting_to_impact]
  app_hypotheses: [torque_generation_score]
confidence: high
review_status: active_spec
relationship_count: 21
hub_score: 50
centrality: 0.42
updated: 2026-07-08
---

# Ground Reaction Force

## Definition

**Ground Reaction Force (GRF)** is the force exerted by the ground on a body in contact with it. According to Newton's Third Law of Motion, when the body applies a force to the ground, the ground simultaneously applies an equal and opposite force back onto the body.

GRF is a 3D vector resolved into three components:
1. **Vertical GRF ($F_z$)**: The upward force perpendicular to the ground.
2. **Anteroposterior (AP) GRF ($F_y$)**: The forward-backward shear force.
3. **Mediolateral (ML) GRF ($F_x$)**: The side-to-side shear force.

---

## Why It Matters

The human body cannot create movement out of nothing. To accelerate its Center of Mass (COM), the body must interact with an external object. The ground is the only external object available to a golfer. Muscular contractions internally pull bones together, but to translate that internal work into external acceleration and rotation, the feet must push against the ground. GRFs are the raw material of the swing's kinetic chain.

---

## Biomechanical Breakdown (Level 3 Evidence)

In the golf swing, the 3D components of GRF serve distinct roles:

### 1. Vertical Force ($F_z$)
- **Action**: Golfer squats or pushes down into the ground, and the ground pushes up.
- **Golf Role**: Reaches peaks of 1.5 to 2.0+ times the golfer's body weight in the lead foot during the early downswing.
- **Moments Link**: If the vertical force vector is offset from the COM (which is typical for the lead foot), it generates a powerful rotational moment around the COM, accelerating pelvic rotation. As Dr. Kwon notes, pushing down vertically generates rotational moments about the COM, contributing directly to clubhead speed (see [Dr. Kwon's Biomechanics: FGMOM](http://drkwongolf.info/biom/fgmom.html#:~:text=One%20thing%20clearly%20shown%20in,contributes%20to%20the%20clubhead%20speed.)).

### 2. Anteroposterior (AP) Shear Force ($F_y$)
- **Action**: Pushing the lead foot forward (towards the target) and the trail foot backward (away from the target).
- **Golf Role**: Pushing the lead foot forward generates a backward deceleration force, which acts as a "brake" to stall lateral slide and convert linear speed into rotational speed.

### 3. Mediolateral (ML) Shear Force ($F_x$)
- **Action**: Pushing the feet outward or squeezing them inward relative to the target line.
- **Golf Role**: Controls lateral sway and slide, helping stabilize the Center of Mass within the golfer's stance width.

---

## Stable Anatomy (Level 1 & 2 Evidence)
Ground Reaction Forces enter the body through the soles of the feet. The primary structures responsible for absorbing, adapting, and transmitting these forces are:
- **Plantar Fascia**: Undergoes elastic loading (windlass mechanism) when the foot is loaded, transferring force directly into the [[superficial_back_line]] and [[deep_front_line]].
- **Foot & Ankle Complex**: Dynamic pronation and supination distribute shear forces.
- **Lower Limb Joints**: The ankle, knee, and hip joints act in series to transmit the forces upward into the pelvis.

---

## App Hypotheses & App Logic (Level 5 Evidence)

### Metrics Integration
GRF magnitudes and direction efficiency contribute directly to the **Torque Generation Score (TGS)** and the **Energy Transmission Efficiency (ETE)**.

### MediaPipe-Observable Proxies
Without force plates, the app estimates GRF activity via:
- **Pelvic Vertical Drop & Lift**: A dynamic squatting motion during transition (Phase 4 to 5) followed by explosive leg extension indicates high vertical force ($F_z$) application.
- **Lead Knee Extension Velocity**: Rapid extension of the lead knee during the downswing indicates the lead side is bracing and pushing hard against the ground (high AP/vertical GRF).

---

## Relationships

| Relationship | Target | Description |
| :--- | :--- | :--- |
| parent_of | [[movement_chain_model]] | The primary input of the movement chain. |
| connects_to | [[ground_reaction_moment]] | GRF vectors generate the Ground Reaction Moments. |
| connects_to | [[plantar_fascia]] | Absorbs and transfers GRF from the sole of the foot. |
| active_during | [[golf_swing_transition]] | Reaches critical lateral and shear force thresholds. |
| assessed_by | [[planned_pressure_shift_screen]] | Assessment for ground loading. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Authoritative biomechanical source. |

---

## Open Questions

- What is the relationship between footwear friction coefficients (spikeless vs. spiked golf shoes) and horizontal shear GRF generation?
- Can we train amateur golfers to increase vertical GRF without causing premature hip extension (early extension)?
