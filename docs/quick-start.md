# Quick Start Guide

Ready to format your data? A valid AQDx data package consists of exactly **two** files that work together. This guide provides the minimum requirements to get started.

## The Two Components

To be compliant with AQDx, you must produce:

1. **The Data File** (CSV, Parquet, or JSON) containing the actual measurements.
2. **The Metadata File** (YAML) containing context about who you are, where the site is, and how the data was collected.

> These two files are linked together by a unique **`dataset_id`**. You must generate this ID and place it in _every row_ of your data file and at the _top_ of your metadata file.

---

## Step 1: Create the Data File

Most users start with the **Tabular (CSV)** format. Your file must adhere to these strict rules:

### 1. Headers are Mandatory

Your file **must** include every single column header listed in the [Field Dictionary](../standard-format/field-dictionary.md), even if you don't have data for that field.

- _Example:_ If you don't measure `elevation`, you must still have an `elevation` column header, and leave the cells below it empty.

### 2. Exact Naming

Column headers must match the standard **exactly** (case-sensitive).

- ✅ `device_id`
- ❌ `Device ID`, `deviceID`, `Serial_Number`

### 3. Strict Data Types

Values must match the defined [Data Types](../standard-format/data-types.md):

- **Dates:** Must be ISO 8601 with time zone offsets (e.g., `2024-05-23T14:00:00-07:00`).
- **Numbers:** No commas or units in the cell (e.g., `1500`, not `1,500` or `1500ppb`).
- **Missing Data:** Leave the cell empty. Do not use `-999`, `NA`, or `Null` strings.

---

## Step 2: Create the Metadata File

The metadata provides the context that makes your numbers meaningful.

1. **Download the Template:** [AQDx_metadata_form_v3.yaml](assets/AQDx_metadata_form_v3.yaml).
2. **Edit in Text Editor:** Open the file in a text editor (e.g., VS Code, Notepad++, or standard Notepad).
3. **Fill Required Fields:**
   - **Data Steward:** Contact info and the `dataset_id` (must match your CSV).
   - **Site Info:** Location name and coordinates.
   - **Instrument Info:** Details on the hardware (nested under the Site).
4. **Save:** Save as a `.yaml` file alongside your data.

---

## Checklist Before Submission

| Check | Requirement                                                                                   |
| :---- | :-------------------------------------------------------------------------------------------- |
| ☐     | **Matching IDs:** Does the `dataset_id` in the YAML match the `dataset_id` column in the CSV? |
| ☐     | **Headers:** Does the CSV contain _all_ required column headers from the dictionary?          |
| ☐     | **Time Format:** Are all timestamps in ISO 8601 format with a timezone offset?                |
| ☐     | **Codes:** Are you using the correct AQS codes for parameters and units?                      |
| ☐     | **Metadata:** Is the YAML file valid and complete?                                            |

[View the Full Field Dictionary →](standard-format/field-dictionary.md)
