# Data Quality Details

The **Data Quality** section of the metadata file provides critical context on how the data was processed, cleaned, and verified. In AQDx Version 3, this replaces the "Data Quality Questionnaire" from the Version 2 Excel form with a structured object that is machine-readable.

These fields allow data users to instantly filter datasets based on their quality needs (e.g., "Show me only data that has passed automated QC").

## Field Summary

| Field Key                                                     | Data Type    | Required | Description                                       |
| :------------------------------------------------------------ | :----------- | :------- | :------------------------------------------------ |
| **[automated_qc](#automated_qc)**                             | Object       | **Yes**  | Details on automated scripts/algorithms applied.  |
| **[corrections](#corrections)**                               | Object       | **Yes**  | Details on calibrations or formulaic adjustments. |
| **[data_review](#data_review)**                               | Object       | **Yes**  | Details on human review processes.                |
| **[precision_quantified](#precision_quantified)**             | Object       | No       | Metrics on instrument precision.                  |
| **[bias_linearity_quantified](#bias_linearity_quantified)**   | Object       | No       | Metrics on bias/linearity.                        |
| **[accuracy_error_quantified](#accuracy_error_quantified)**   | Object       | No       | Metrics on accuracy/error.                        |
| **[detection_limit_quantified](#detection_limit_quantified)** | Object       | No       | Details on the Minimum Detection Limit (MDL).     |
| **[qapp_link](#qapp_link)**                                   | String (URL) | No       | Link to the Quality Assurance Project Plan.       |

---

## Field Definitions

### automated_qc

Describes whether automated algorithms were used to flag or remove bad data.

- **applied** (Boolean): `true` if scripts were run (e.g., range checks, sticking checks). This should align with the `autoqc_code` column in your data file (where 1 = true).
- **description** (String): A brief summary of the checks used.
  - _Example:_ "Removed negative values and flat-lined data > 2 hours."

### corrections

Describes whether the raw sensor outputs were adjusted based on a reference standard or formula.

- **applied** (Boolean): `true` if data was modified from the original raw output. This should align with the `correction_code` column in your data file.
- **description** (String): Summary of the correction method.
  - _Example:_ "Adjusted using the EPA's national correction factor for PurpleAir PM2.5."

### data_review

Describes the level of human oversight applied to the dataset.

- **undergone_review** (Boolean): `true` if a human has looked at and approved the data. This aligns with the `review_level_code` in the data file.
- **description** (String): Who reviewed it and what was the criteria?
  - _Example:_ "Quarterly review by data manager to remove maintenance periods."

### qapp_link

**Format:** String (URL)
**Example:** `https://example.org/docs/project-qapp-v1.pdf`

A direct link to the Quality Assurance Project Plan (QAPP) or Standard Operating Procedure (SOP) document. This is highly recommended for regulatory or academic datasets to establish credibility.

---

## Quantitative Metrics (Optional)

These optional sections allow you to provide specific performance numbers if you have characterized your instruments (e.g., through co-location).

### precision_quantified

- **value** (Boolean): Have you calculated precision?
- **metrics_description** (String): "CV = 5% based on 2-week co-location with BAM-1020."

### bias_linearity_quantified

- **value** (Boolean): Have you calculated bias?
- **metrics_description** (String): "Slope = 0.92, Intercept = 1.5 µg/m³."

### accuracy_error_quantified

- **value** (Boolean): Have you calculated overall error?
- **metrics_description** (String): "RMSE = 2.5 µg/m³ compared to reference."

### detection_limit_quantified

- **value** (Boolean): Do you know the lower limit of detection?
- **description** (String): "MDL < 1 ppb for Ozone."
