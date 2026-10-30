---
id: rajagopal_opensim_model_2016
type: Evidence Source
preferred_name: "Rajagopal et al. Full-Body Musculoskeletal Model (OpenSim 2016)"
aliases: ['Rajagopal 2016', 'OpenSim Full-Body Model', 'Rajagopal OpenSim']
short_definition: "Full-body OpenSim musculoskeletal model with anatomical geometry and muscle parameters, tested in healthy walking and running."
author: "Apoorva Rajagopal; Christopher L. Dembia; Matthew S. DeMers; Denny D. Delp; Jennifer L. Hicks; Scott L. Delp"
publication_year: 2016
format: "computational_biomechanics_model"
domain: "gait"
evidence_level: 3
source_role: "domain_biomechanics"
confidence: high
review_status: source_checked_app_translation_unvalidated
relationships:
  cited_by: []
  connects_to: []
relationship_count: 0
hub_score: 0
centrality: 0.0
updated: 2026-10-28
---

# Rajagopal et al. (2016): Full-Body Model for Gait Simulation

## Citation and scope

Rajagopal A, Dembia CL, DeMers MS, Delp DD, Hicks JL, Delp SL. *Full-Body Musculoskeletal Model for Muscle-Driven Simulation of Human Gait.* IEEE Trans Biomed Eng. 2016;63(10):2068–2079. DOI [10.1109/TBME.2016.2586891](https://doi.org/10.1109/TBME.2016.2586891), [PMID 27392337](https://pubmed.ncbi.nlm.nih.gov/27392337/). Abstract and accessible full text checked 2026-10-28.

The model has 37 degrees of freedom, 80 lower-limb muscle-tendon units and 17 upper-body torque actuators. Its geometry and muscle parameters draw on anatomical measurements; the reported simulations and validation concern healthy walking and running.

## Allowed use and transfer boundary

Use as a computational musculoskeletal reference with explicit model, scaling, input and validation requirements. Model-derived forces are estimates under assumptions, not camera measurements. Applying this model to another task requires task-specific verification.

This paper does not validate bilateral-squat activation, patellofemoral shear from knee-to-toe excursion, or MediaPipe ground truth. Do not use its gait validation as evidence that TillYes squat kinematics or muscle-state inferences are accurate. [[bodyweight_squat]] and [[knee_to_toe_progression_boundary]] must cite squat-specific sources for their claims.
