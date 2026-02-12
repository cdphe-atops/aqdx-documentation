# Metadata Overview

## Purpose

While the data files (CSV or JSON) contain the _measurements_ (the "what" and "when"), the Metadata Form provides the essential context (the "who," "where," and "how"). Without this context, air quality data is often unusable by third parties.

The **AQDx Metadata Form** is designed to:

1. **Harmonize descriptions** of monitoring sites and instruments.
2. **Enable data discovery** by documenting ownership and contact information.
3. **Clarify data quality** by detailing Quality Control (QC) procedures and instrument limitations.

## Format: Moving to YAML

In AQDx Version 3, metadata is exchanged via a **YAML** file (`.yaml`) rather than the spreadsheet used in Version 2. This shift allows for:

- **Better Hierarchy:** Instruments can be properly nested under specific Sites.
- **Machine Readability:** YAML is easily parsed by software while remaining human-readable.
- **Version Control:** Text-based metadata files can be tracked in Git repositories alongside code and data.

> **Download:** [AQDx_metadata_form_v3.yaml](../assets/AQDx_metadata_form_v3.yaml) (Template)

## Metadata Scope & Structure

The metadata is organized into three primary sections. Fields within these sections are designated as either:

**Applicable to All** (required for everyone)
**Applicable to Regulatory** (required only for compliance monitoring).

### 1. Data Steward Details

**Who is responsible?**

- Contains contact information for the organization or individual managing the dataset.
- Defines the `aqdx_data_version` and whether the dataset is considered `regulatory`.

### 2. Sites & Instruments

**Where was it measured?**

- Site location (Lat/Lon), surroundings (Urban/Rural), and physical environment.

**What was used?**

- Instruments are nested **within** the Site they belong to.
- Includes `device_id`, `parameter_code`, sampling frequency, and inlet details (e.g., probe height, airflow).

### 3. Data Quality Details

**How good is the data?**

- Describes the Quality Assurance (QA) and Quality Control (QC) processes.
- Documents if the data has been corrected, reviewed, or audited.

## "All" vs. "Regulatory" Data

AQDx distinguishes between general monitoring (e.g., community science, research) and regulatory monitoring (e.g., compliance with EPA NAAQS).

**All Instruments (Base Requirements):** Fields in the YAML marked "Applicable to All" must be completed by every user. These cover the basics needed to plot and interpret the data physically.

**Regulatory Instruments (Extended Requirements):** If the `is_regulatory_data` field is set to `1` (Yes), additional fields become required. These include AQS codes, monitoring scales, and specific audit details necessary for government reporting.

## Completing the Form

1. **Download** the [AQDx_metadata_form_v3.yaml](../assets/AQDx_metadata_form_v3.yaml) template.
2. **Edit** the file using a text editor (e.g., VS Code, Notepad++, or standard Notepad).
3. **Fill** in values after the colons.
    - Use quotes for text strings: `site_name: "Downtown Station"`
    - Use `null` for unknown values: `contact_phone: null`
    - Do not change the field keys (the text before the colon).
4. **Save** the file alongside your data distribution.
