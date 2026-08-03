# Six Phases Swing Graph Extraction

> **Historical project report (2026-07-13) — paths and the "missing concepts" list are superseded.** This is the provenance record for the one-time extraction of the 3D Golf Decoded six-phase model; the work it documents is complete and the nodes remain in the vault.
>
> **Folder mapping then → now:** `wiki/sources/` → `00_Spec/sources/`; `wiki/golf_phases/` → `04_Golf_Swing/phases/` and `04_Golf_Swing/positions/`; `wiki/movements/` → `04_Golf_Swing/`; `wiki/movement_patterns/` → `03_Movement_Functions/`.
>
> **"Missing Concepts to Add Later" — status update:** `Pelvis-Thorax Separation` now exists as [[x_factor]]; `Center of Mass` is covered as the COM proxy in [[golf_movement_sequence]] and [[segment_angle_metrics]]; `Deceleration` is covered in [[temporal_movement_metrics]]. `Clubhead Speed`, `Ball Flight`, `Pressure Shift`, and `Center of Pressure` remain intentionally uncreated (require instrumented data / not yet needed).
>
> The body below is kept as the original record and has **not** been rewritten.

## Source

- Evidence Source: [[golf_decoded_six_phases_swing]]
- Primary video: [On the Mark podcast / 3D Golf Decoded](https://www.youtube.com/watch?v=eDFQrVB2PXc&t=206s) (starts at 3:26)
- Supporting artifact: screenshot labeled "The 6 Phases of the Swing"
- Extraction goal: convert the phase model into reusable graph nodes, not a lecture summary.

## Placement in Vault

| Concept Type | Folder |
|---|---|
| Evidence source | `wiki/sources/` |
| Golf phase intervals | `wiki/golf_phases/` and existing `wiki/movements/golf_swing_transition.md` |
| Boundary events and reusable movement concepts | `wiki/movement_patterns/` |
| Parent movement | `wiki/movements/golf_swing.md` |

## Created or Updated Nodes

| Node | Category | Action |
|---|---|---|
| [[golf_decoded_six_phases_swing]] | Golf | Created evidence source |
| [[golf_swing]] | Golf | Updated parent movement |
| [[address_to_shaft_parallel]] | Movement Phase | Created |
| [[shaft_parallel_to_end_pelvis_rotation]] | Movement Phase | Created |
| [[end_pelvis_rotation_to_top_backswing]] | Movement Phase | Created |
| [[golf_swing_transition]] | Movement Phase | Updated and merged with Top Backswing -> Max Unweighting |
| [[max_unweighting_to_impact]] | Movement Phase | Created |
| [[impact_to_hands_chest_height]] | Movement Phase | Created |
| [[address_position]] | Golf | Created boundary event |
| [[shaft_parallel_position]] | Golf | Created boundary event |
| [[end_pelvis_rotation]] | Golf / Biomechanics | Created boundary event |
| [[top_backswing_position]] | Golf | Created boundary event |
| [[max_unweighting]] | Golf / Physics | Created boundary event |
| [[impact_position]] | Golf | Created boundary event |
| [[hands_chest_height_position]] | Golf | Created boundary event |
| [[movement_sequencing]] | Motor Control | Created reusable parent concept |
| [[force_transmission]] | Biomechanics | Created reusable parent concept |
| [[energy_transfer]] | Physics | Created reusable parent concept |
| [[ground_reaction_force]] | Physics | Created external-force concept |
| [[golf]] | Golf | Created domain parent |

## Phase Relationship Table

| Phase | Starts At | Ends At | Primary Reasoning Role | Next Phase |
|---|---|---|---|---|
| [[address_to_shaft_parallel]] | [[address_position]] | [[shaft_parallel_position]] | Establish setup and early pressure conditions | [[shaft_parallel_to_end_pelvis_rotation]] |
| [[shaft_parallel_to_end_pelvis_rotation]] | [[shaft_parallel_position]] | [[end_pelvis_rotation]] | Track early pelvis rotation timing | [[end_pelvis_rotation_to_top_backswing]] |
| [[end_pelvis_rotation_to_top_backswing]] | [[end_pelvis_rotation]] | [[top_backswing_position]] | Track upper-body loading after pelvis rotation ends | [[golf_swing_transition]] |
| [[golf_swing_transition]] | [[top_backswing_position]] | [[max_unweighting]] | Redirect backswing load into downswing sequencing | [[max_unweighting_to_impact]] |
| [[max_unweighting_to_impact]] | [[max_unweighting]] | [[impact_position]] | Transfer force and energy toward impact | [[impact_to_hands_chest_height]] |
| [[impact_to_hands_chest_height]] | [[impact_position]] | [[hands_chest_height_position]] | Early post-impact deceleration checkpoint | none in source |

## Concept Relationship Table

| Source Concept | Graph Category | Linked Concepts |
|---|---|---|
| Dynamic movement | Motor Control | [[movement_sequencing]], [[golf_swing]] |
| Pelvis rotation endpoint | Biomechanics | [[end_pelvis_rotation]], [[hip_joint]], [[hip_internal_rotation]], [[thoracic_rotation]] |
| Top backswing | Golf | [[top_backswing_position]], [[trail_shoulder_external_rotation]], [[thoracic_rotation]], [[neck_tension]] |
| Max unweighting | Physics / Golf | [[max_unweighting]], [[ground_reaction_force]], [[toe_loading]], [[plantar_fascia]] |
| Impact | Golf / Physics | [[impact_position]], [[force_transmission]], [[energy_transfer]] |
| Hands chest height | Golf | [[hands_chest_height_position]], [[impact_to_hands_chest_height]] |

## Inferred Relationships

These relationships are useful for AI reasoning but need future evidence beyond the screenshot.

| Inference | Confidence | Why It Was Added |
|---|---|---|
| [[max_unweighting]] relates to [[ground_reaction_force]] | Low | The term unweighting implies body-ground force interaction. |
| [[end_pelvis_rotation]] relates to [[hip_internal_rotation]] and [[hip_external_rotation]] | Medium | Pelvis rotation depends on hip rotation mechanics already represented in the graph. |
| [[top_backswing_position]] relates to [[trail_shoulder_external_rotation]] | Medium | Existing graph already models trail shoulder external rotation as a backswing/transition loading pattern. |
| [[golf_swing_transition]] maps to Top Backswing -> Max Unweighting | Medium | The screenshot labels that interval and the vault already had a transition node. |
| [[impact_to_hands_chest_height]] is an early deceleration checkpoint | Low | The source provides the boundary but not explicit deceleration language. |

## Missing Concepts to Add Later

Do not create these until they are needed by assessments or additional sources.

| Missing Concept | Category | Reason |
|---|---|---|
| Clubhead Speed | Physics / Golf | Output variable for force and energy transfer. |
| Ball Flight | Golf | Result of impact; useful for performance reasoning. |
| Pressure Shift | Biomechanics | Needed to analyze unweighting and ground interaction. |
| Center of Mass | Physics | Needed for unweighting and balance analysis. |
| Center of Pressure | Physics | Needed for pressure plate or force-plate style reasoning. |
| Pelvis-Thorax Separation | Biomechanics | Needed for backswing loading and transition reasoning. |
| Deceleration | Biomechanics | Needed for post-impact and follow-through analysis. |

## Graph Traversal Examples

```text
[[golf_swing]]
-> [[address_to_shaft_parallel]]
-> [[toe_loading]]
-> [[plantar_fascia]]
-> [[ground_reaction_force]]
```

```text
[[golf_swing]]
-> [[end_pelvis_rotation_to_top_backswing]]
-> [[top_backswing_position]]
-> [[trail_shoulder_external_rotation]]
-> [[functional_lines]]
-> [[thoracolumbar_fascia]]
```

```text
[[golf_swing_transition]]
-> [[max_unweighting]]
-> [[ground_reaction_force]]
-> [[force_transmission]]
-> [[impact_position]]
```
