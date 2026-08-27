---
id: squat_observability_boundary
type: App Logic
preferred_name: Squat Observability Boundary
aliases: [squat camera boundary, squat inference limits]
domain: squat
evidence_level: 5
source_role: app_observability_policy
supported_by: [straub_powers_squat_biomechanics_2024, gray_cook_movement_2010]
status: active_spec
reviewed_date: 2026-08-27
connects_to: [bodyweight_squat, squat_joint_muscle_mapping, squat_myofascial_mapping, squat_cross_view_synthesis, metric_evidence_classification, movement_reporting_standards]
---

# Squat Observability Boundary

## Side View Allow-List

- 2D knee-flexion and hip-flexion proxies;
- trunk and tibia inclination in the image plane;
- trunk-tibia angle proxy;
- selected depth and phase timing;
- repetition count and repeatability;
- heel-rise proxy when heel and forefoot landmarks remain reliable.

## Front View Allow-List

- knee-to-foot tracking proxy;
- pelvis midpoint lateral displacement relative to standing baseline;
- shoulder-midpoint relative to pelvis-midpoint lateral displacement;
- left-right timing/depth contribution;
- stance-width descriptor when landmarks are adequate;
- repetition count and repeatability from pelvis-descent timing.

## Cross-View Allow-List

- combine independently produced side and front findings by anatomical theme;
- identify complementary multi-plane observations without claiming that they are
  the same repetition;
- describe corroboration only when both views measure a genuinely comparable theme;
- identify conflict or limited synthesis when view quality, repetition count, or
  protocol setup differs;
- preserve each view's metric, reliability, and competing explanations.

Cross-view synthesis must never average side and front angles, align events across
separate recordings, or upgrade two proxies into a diagnosis. See
[[squat_cross_view_synthesis]].

## Unavailable Without Additional Instrumentation

- joint moments, force, pressure, COM, COP, kinetics, and tissue loading;
- muscle activation, weakness, length, fatigue, or inhibition;
- passive ankle, knee, hip, or spinal mobility;
- lumbar segment position from MediaPipe landmarks;
- reliable pronation/supination or tibial rotation from a single ordinary view;
- pathology, pain source, injury risk, or diagnosis;
- fascial tension, restriction, line loading, or energy storage.

## Finding Contract

Every finding must include:

1. measured observation and phase;
2. reliability and view;
3. movement-strategy interpretation;
4. joints and candidate regions to review;
5. competing explanations;
6. optional myofascial hypothesis labelled `engine_synthesis`;
7. explicit conclusions that cannot be made.
