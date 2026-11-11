---
id: trovato_postural_evaluation_2022
type: Evidence Source
preferred_name: "Postural Evaluation in Young Healthy Adults through a Digital and Reproducible Method"
aliases: [Trovato posture study, Apecs healthy adult posture reference, digital shoulder alignment reference]
short_definition: "Peer-reviewed digital-photogrammetry study of 100 healthy young adults reporting posterior-coronal shoulder alignment of 1.5° ± 1.2° and excellent inter-rater reproducibility (ICC 0.93)."
author: Bruno Trovato
contributors: [Federico Roggio, Martina Sortino, Marta Zanghì, Luca Petrigna, Rosario Giuffrida, Giuseppe Musumeci]
publication_year: 2022
publisher: Journal of Functional Morphology and Kinesiology
citation: "Trovato B, Roggio F, Sortino M, Zanghì M, Petrigna L, Giuffrida R, Musumeci G. Postural Evaluation in Young Healthy Adults through a Digital and Reproducible Method. J Funct Morphol Kinesiol. 2022;7(4):98. https://doi.org/10.3390/jfmk7040098"
format: open_access_journal_article
license: "CC BY 4.0"
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9680464/
pmid: 36412760
pmcid: PMC9680464
domain: static_posture
evidence_level: 4
source_role: applied_practice
relationships:
  connects_to: [bodyreading_static_posture, static_shoulder_alignment_measurement]
  relevant_to: [shoulder_height_difference, static_posture_app]
confidence: medium
review_status: source_reviewed_for_shoulder_reference
relationship_count: 4
hub_score: 12
centrality: 0.04
updated: 2026-11-11
---

# Trovato et al. — Digital Postural Evaluation in Healthy Young Adults

## Source role

This peer-reviewed applied digital-posture study provides a population reference for image-plane shoulder alignment. It does not establish a diagnostic cutoff. Its relevant contribution to the engine is a reproducible angular shoulder measure in a healthy young-adult sample.

## Study and method

- 100 healthy volunteers (50 male, 50 female), mean age 23.4 ± 6.2 years.
- Static anterior, posterior and sagittal photographs were assessed with the Apecs mobile app.
- Clinicians placed markers at the app's predefined anatomical landmarks.
- Three experienced operators performed the analysis; inter-rater agreement was assessed with ICC.

## Shoulder-alignment result used by the app

For the posterior coronal view, shoulder alignment was **1.5° ± 1.2°** across the full sample, with **ICC 0.93**. The study therefore supports measuring the line between the shoulder landmarks as an angle relative to horizontal and supports the reproducibility of that specific app-based observation.

The paper did **not** define normal/abnormal thresholds. The TillYes reporting bands in [[static_shoulder_alignment_measurement]] are an explicit Level 5 reference policy derived from the reported mean and standard deviation:

- below 2.7°: within the study-derived mean + 1 SD reference band;
- 2.7° to <3.9°: mild reportable difference;
- 3.9° to <5.1°: moderate reportable difference;
- 5.1° or more: significant reportable difference.

These bands determine display priority, not diagnosis.

## App implication

Use shoulder-line angle in degrees from horizontal, calculated in original-image pixel geometry. Do not use vertical landmark separation as a percentage of total photograph height: that quantity changes with framing and is not the metric reported by this study.

## Scope

The reference population was healthy young adults and the study did not compare Apecs with a gold-standard marker-based or rasterstereographic system. The metric remains an image-plane posture observation.

## Related concepts

- [[static_shoulder_alignment_measurement]]
- [[bodyreading_static_posture]]
- [[movement_reporting_standards]]

