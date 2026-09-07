---
id: length_tension_postural_relationship
type: Concept
subtype: Biomechanics
preferred_name: Length-Tension Postural Relationship
aliases: [Agonist-Antagonist Postural Balance, Reciprocal Inhibition Postural Model, Kendall Tone Model]
short_definition: "Clinical framework describing how persistent postural alignments and movement compensations correlate with shortened/overactive movers and lengthened/underactive stabilizers."
category: Biomechanics
evidence_level: 4
source_role: applied_clinical_practice
evidence_sources: [kendall_muscles_testing_function, sahrmann_movement_impairment_syndromes]
relationships:
  defined_by: [kendall_muscles_testing_function]
  connects_to: [apparent_shortness_vs_structural_shortening, sagittal_plumb_line_alignment, coronal_plumb_line_alignment]
  part_of: [movement_observation_framework]
confidence: high
review_status: reviewed
relationship_count: 5
hub_score: 6
centrality: 0.045
updated: 2026-09-01
---

# Length-Tension Postural Relationship

## Clinical Foundations

Florence Kendall established the clinical paradigm linking joint positioning to muscle tone balance:
* When a joint is held persistently in an offset position, the agonist muscles adaptively shorten while the antagonist muscles are held in a lengthened state.
* **Locked Short (Hypothesized Overactive)**: Muscles held in shortened ranges develop hypertonicity, increased resting stiffness, and neural dominance. In movement, they tend to over-recruit as prime movers.
* **Locked Long (Hypothesized Underactive)**: Muscles held in lengthened ranges suffer from stretch weakness, mechanical disadvantage, and neural inhibition. In movement, they struggle to contribute as local dynamic stabilizers.

## Integration with Modern Movement Intelligence

In the TillYes engine, Kendall's single-muscle model is synthesized with:
1. **Thomas Myers (Anatomy Trains)**: Muscles operate within continuous fascial meridians; tension or slack in one station propagates throughout the entire myofascial line.
2. **Shirley Sahrmann (Movement Impairment Syndromes)**: The body follows the path of least resistance (directional susceptibility to movement).
3. **Non-Diagnostic Framing**: Camera-based kinematic tracking generates **observational hypotheses** (e.g. 🔴 *Hypothesized Overactive* vs. 🔵 *Hypothesized Underactive*), which serve as prioritized palpation targets and testing cues for in-person practitioners rather than definitive diagnoses.

## Related Nodes

- [[kendall_muscles_testing_function]]
- [[sagittal_plumb_line_alignment]]
- [[apparent_shortness_vs_structural_shortening]]
- [[czaprowski_nonstructural_posture_2018]]

## Evidence Grounding
```yaml
evidence:
  - source_id: kendall_muscles_testing_function
    level: foundational_anatomical_framework
    evidence_tier: Level 2
    description: "Sarcomere length-tension curves, stretch weakness, and positional tightness."
  - source_id: anatomy_trains_myers_2009
    level: foundational_anatomical_framework
    evidence_tier: Level 2
    description: "Postural tone adaptation across continuous myofascial meridians."
```
