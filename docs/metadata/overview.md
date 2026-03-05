# AQDx v3 Metadata Reference Guide

> **Download:** [AQDx_metadata_form_v3.yaml](../assets/AQDx_metadata_form_v3.yaml) (Template)

This document details the fields and definitions required for the AQDx Version 3 Metadata YAML form. Metadata provides essential context for air quality datasets, including project ownership, site locations, instrument specifications, and quality assurance procedures.

To streamline data submission, the metadata is organized into three distinct sections: Overview, Sites, and Instruments. This standardized structure avoids repetitive data entry by allowing submitters to define a monitoring site once, and then link multiple individual instruments to that location.

_(Note: Data submitters may fill out this information using either a standard three-tab spreadsheet (e.g. Microsoft Excel, Google Sheets) or editing the YAML file in a text editor. Please see the accompanying guide on **Using the AQDx Excel Template and Conversion Script** for step-by-step instructions on data entry.)_

## Metadata Organization

The schema relies on unique text identifiers to link data across the different sections:

- **Sites:** Each physical monitoring location is defined once and identified by a unique `site_name`. This section holds all geographic and location-based data.
- **Instruments:** Each instrument is identified by a combination of its `device_id` and the specific `parameter_code` it measures. This allows you to define different detection limits and calibrations for different pollutants measured by the _same_ physical sensor package.
- **The Link:** Every instrument entry must include a `site_name` that exactly matches a location defined in the Sites list.

## Data Quality Documentation

Data quality information is divided into two levels to accurately reflect different monitoring practices:

1. **Dataset-Level Quality:** Broad procedures that apply to the entire project (e.g., QAPP links, general data review workflows, project-wide automated QC).
2. **Instrument/Parameter-Level Quality:** Specific performance metrics (e.g., precision, bias, detection limits, and correction methods) that apply uniquely to a specific parameter measured by a specific device.

---

## 1. Dataset Header

These root-level fields define the entire submission package and ensure the metadata maps correctly to the accompanying row-level data file.

| Field                     | Type   | Description                                                                                                     |
| :------------------------ | :----- | :-------------------------------------------------------------------------------------------------------------- |
| **dataset_id**            | String | **Required.** Unique identifier for the dataset. Must exactly match the `dataset_id` in your tabular data file. |
| **aqdx_metadata_version** | String | **Required.** Version of the metadata schema used (e.g., "3.0").                                                |
| **aqdx_data_version**     | String | **Required.** Version of the attached tabular data format (e.g., "3.0").                                        |

## 2. Overview & Data Steward

This section provides context about the organization responsible for the data.

| Field                      | Type    | Description                                                                                                          |
| :------------------------- | :------ | :------------------------------------------------------------------------------------------------------------------- |
| **data_steward_name**      | String  | **Required.** Max 64 chars. Must exactly match `data_steward_name` in the tabular data.                              |
| **contact_name**           | String  | **Required.** First and Last name. Max 64 chars.                                                                     |
| **contact_email**          | String  | **Required.** Max 64 chars.                                                                                          |
| **contact_phone**          | String  | _Optional._ Phone number.                                                                                            |
| **organization_type**      | Integer | **Required.** `1`-Gov, `2`-NGO, `3`-Community, `4`-Academic, `5`-Industry, `6`-Consulting, `7`-Education, `8`-Other. |
| **organization_name_full** | String  | **Required.** Full name (e.g., Colorado Department of Public Health and Environment). Max 128 chars.                 |
| **address**                | String  | _Optional._ Physical address of the organization. Max 128 chars.                                                     |
| **last_update_date**       | Integer | **Required.** Date the metadata was last modified. Format: `YYYYMMDD`.                                               |
| **is_regulatory_data**     | Integer | **Required.** Is this dataset regulatory? `1` (Yes) or `0` (No).                                                     |
| **data_abstract**          | String  | _Optional._ Brief description of the dataset/project. Max 500 chars.                                                 |

## 3. Dataset-Level Quality

General quality assurance procedures applied to the dataset as a whole.

| Field                            | Type    | Description                                                                                                                                                                                                                                                                              |
| :------------------------------- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **automated_qc_applied**         | Boolean | **Required.** `true` or `false`. Should align with 'auto_qc' in the tabular data.                                                                                                                                                                                                        |
| **automated_qc_methods**         | String  | _Optional._ Comma-separated exact options: _bounds check, sticking values, comparison to other signals, low values check, high values check, completeness, comparison to co-located duplicate sensor or sample, automated bump checks, automated zero checks, other algorithmic checks_. |
| **automated_qc_description**     | String  | _Optional._ Free text summary of automated QC.                                                                                                                                                                                                                                           |
| **data_review_undergone**        | Boolean | **Required.** `true` or `false`. Should align with 'review_level_code' in the tabular data.                                                                                                                                                                                              |
| **data_review_methods**          | String  | _Optional._ Comma-separated options: _qualitative review, quantitative review, external party reviewing - [add here], based on established methods associated with an official Program - [add name here]_.                                                                               |
| **data_review_description**      | String  | _Optional._ Free text summary of the review process.                                                                                                                                                                                                                                     |
| **official_monitoring_programs** | String  | _Optional._ E.g., US EPA NATTS Program.                                                                                                                                                                                                                                                  |
| **other_processing_desc**        | String  | _Optional._ Any other processing users should be aware of.                                                                                                                                                                                                                               |
| **useful_links**                 | String  | _Optional._ Comma-separated URLs (e.g., project webpages, QAPPs, publications, procedures).                                                                                                                                                                                              |

## 4. Sites

Defines the physical locations of the monitoring stations. Provide one entry per site.

### Special Case: Handling Mobile and Wearable Data

AQDx fully supports mobile platforms (e.g., regulatory vans) and wearable sensors. Because the precise, second-by-second GPS coordinates for mobile data are recorded in your tabular data file, the `Sites` metadata entry is used to define the **General Study Area** or the **Mobile Platform** itself.

If your data is mobile or wearable, fill out the Sites section using these guidelines:

- **site_name:** Name the route, the bounding area, or the platform (e.g., "Denver Mobile Van 1", "I-25 Route", "Wearable Subject A").
- **latitude / longitude:** Enter the centroid (center point) of your study area, the starting point of your route, or the "home base" of the instrument.
- **surroundings_type:** Choose the code that best represents the overall area, or select `10` (Mixed) if the route covers diverse environments.

_(Note: When you set the `monitoring_approach` on the Instruments tab to `4` (Mobile) or `5` (Wearable), data users and databases will automatically know to look at your tabular data for the exact timestamps and moving coordinates.)_

| Field                            | Type    | Description                                                                                                                                         |
| :------------------------------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **site_name**                    | String  | **Required.** Unique identifier for the location. Max 64 chars.                                                                                     |
| **latitude** / **longitude**     | Decimal | **Required.** Coordinates in decimal degrees.                                                                                                       |
| **original_gis_datum**           | String  | **Required.** Expected coordinate system: `WGS84`. Use this field to indicate if the data was converted to WGS84.                                   |
| **address**                      | String  | _Optional._ Physical address of the site.                                                                                                           |
| **state_code** / **county_code** | Integer | **Required.** AQS state and county codes.                                                                                                           |
| **site_owner**                   | String  | **Required.** Person or organization owning the site. Max 128 chars.                                                                                |
| **site_photos_url**              | String  | _Optional._ Link to site imagery. Max 200 chars.                                                                                                    |
| **surroundings_type**            | Integer | **Required.** `1`-Urban, `2`-Rural, `3`-Suburban, `4`-Industrial, `5`-Residential, `6`-Ag, `7`-Natural, `8`-Rec, `9`-Water, `10`-Mixed, `11`-Other. |
| **nearby_sources**               | String  | _Optional._ Free text description of nearby pollution sources.                                                                                      |
| **reg_aqs_id**                   | Integer | **Required if regulatory.** 9-digit AQS monitoring location code.                                                                                   |
| **reg_monitoring_scale**         | Integer | **Required if regulatory.** `1`-Micro, `2`-Middle, `3`-Neighborhood, `4`-Urban, `5`-Regional, `6`-National, `7`-Global.                             |
| **reg_site_type**                | Integer | **Required if regulatory.** Objective category code.                                                                                                |
| **reg_groundcover**              | Integer | **Required if regulatory.** Dominant groundcover code.                                                                                              |

## 5. Instruments & Parameter-Level Quality

Defines the specific devices, configurations, and chemical/physical parameters measured. **Provide one entry per unique combination of `device_id` and `parameter_code`.**

| Field                        | Type    | Description                                                                                                    |
| :--------------------------- | :------ | :------------------------------------------------------------------------------------------------------------- |
| **device_id**                | String  | **Required.** The device identifier. Matches tabular data.                                                     |
| **parameter_code**           | String  | **Required.** 5-digit AQS parameter code. Matches tabular data.                                                |
| **site_name**                | String  | **Required.** Must exactly match a `site_name` defined in the Sites section.                                   |
| **manufacturer_name**        | String  | **Required.** Manufacturer of the instrument.                                                                  |
| **device_model**             | String  | **Required.** Model name assigned by `manufacturer_name`.                                                      |
| **firmware_version**         | String  | _Optional._ Instrument firmware version.                                                                       |
| **method_code**              | String  | **Required.** 3-digit method code. Matches tabular data.                                                       |
| **monitor_start_date**       | Integer | **Required.** Format: `YYYYMMDD`.                                                                              |
| **probe_height_m**           | Decimal | **Required.** Height above ground in meters.                                                                   |
| **monitoring_approach**      | Integer | **Required.** `1`-Stationary Cont, `2`-Stationary Integrated, `3`-Intermittent, `4`-Mobile, `5`-Wearable.      |
| **monitoring_objective**     | Integer | **Required.** `1`-Ambient, `2`-Near-source, `3`-Fenceline, `4`-Community, `5`-Personal, `6`-Indoor, `7`-Other. |
| **expanded_objective**       | String  | **Required.** Free text expanded objective.                                                                    |
| **sampling_frequency_sec**   | Decimal | **Required.** Frequency in seconds (e.g., 60, 3600).                                                           |
| **residence_time_sec**       | Decimal | _Optional._ Residence time for reactive parameters.                                                            |
| **airflow_arc_degrees**      | Integer | **Required.** Unrestricted airflow (0–360).                                                                    |
| **instrument_photos_url**    | String  | _Optional._ URL to instrument installation photos.                                                             |
| **dist_obstructions_m**      | Decimal | **Required.** Distance from obstructions not on roof (meters).                                                 |
| **dist_roof_obstructions_m** | Decimal | _Optional._ Distance from obstructions on roof (meters).                                                       |

### Instrument/Parameter-Specific Data Quality

These fields apply _only_ to the specific device and parameter defined in the row.

| Field                           | Type    | Description                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------ | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **corrections_applied**         | Boolean | **Required.** `true` or `false`. Matches tabular 'corr_code'.                                                                                                                                                                                                                                                                                                   |
| **corrections_methods**         | String  | _Optional._ Comma-separated options: _manual correction, automated correction, global correction model applied, unit/device-specific corrections applied, corrections derived from [frequency] co-locations, published model used [add name/description], corrections based on periodic calibration via standards, correction after re-processing/re-analysis_. |
| **corrections_description**     | String  | _Optional._ Free text including frequency.                                                                                                                                                                                                                                                                                                                      |
| **detection_limit_methods**     | String  | _Optional._ Comma-separated options: _method detection limit, instrument detection limit, determined empirically, taken from manufacturer specifications, method used - [add name/description]_.                                                                                                                                                                |
| **detection_limit_desc**        | String  | _Optional._ Free text limit description.                                                                                                                                                                                                                                                                                                                        |
| **precision_quantified**        | Boolean | _Optional._ `true` or `false`.                                                                                                                                                                                                                                                                                                                                  |
| **precision_desc**              | String  | _Optional._ Metrics (e.g., standard deviation, CV) and dataset used.                                                                                                                                                                                                                                                                                            |
| **bias_linearity_quantified**   | Boolean | _Optional._ `true` or `false`.                                                                                                                                                                                                                                                                                                                                  |
| **bias_linearity_desc**         | String  | _Optional._ Metrics (e.g., simple linear regression) and dataset used.                                                                                                                                                                                                                                                                                          |
| **accuracy_error_quantified**   | Boolean | _Optional._ `true` or `false`.                                                                                                                                                                                                                                                                                                                                  |
| **accuracy_error_desc**         | String  | _Optional._ Metrics (e.g., RMSE) and dataset used.                                                                                                                                                                                                                                                                                                              |
| **maintenance_procedures_desc** | String  | _Optional._ Frequency and date last performed for this device.                                                                                                                                                                                                                                                                                                  |

### Regulatory Fields

_Complete these fields only if `is_regulatory_data` is set to `1`. Otherwise, leave null or blank._

| Field                       | Type       | Description                                       |
| :-------------------------- | :--------- | :------------------------------------------------ |
| **reg_monitor_type**        | String/Int | _Optional._ AQS monitor type.                     |
| **reg_method_type**         | String/Int | _Optional._ AQS method type.                      |
| **reg_network_affiliation** | String     | _Optional._ Network affiliation. Max 64 chars.    |
| **reg_collecting_agency**   | String     | _Optional._ Collecting agency name. Max 64 chars. |
| **reg_agency_code**         | Integer    | _Optional._ Agency code.                          |
| **reg_analysis_method**     | String     | _Optional._ Analysis method used. Max 64 chars.   |
| **reg_analytical_lab**      | String     | _Optional._ Analytical lab name. Max 64 chars.    |
| **reg_probe_material**      | String     | _Optional._ Material of the probe. Max 64 chars.  |
