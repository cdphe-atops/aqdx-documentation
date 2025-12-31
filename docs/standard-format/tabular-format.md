# Tabular Data Files (CSV, Excel, Parquet)

The Tabular format is the standard method for exchanging historical datasets, batch uploads, and archival data. In this format, every record is a row, and every field is a column.

AQDx supports the following file types:
*   **CSV** (`.csv`): Comma-Separated Values (Universal standard).
*   **Excel** (`.xlsx`): Microsoft Excel Open XML Spreadsheet.
*   **Parquet** (`.parquet`): Columnar storage format for large datasets.

## General Requirements
Regardless of the file type, all tabular files must adhere to these structure rules:

1.  **Header Row:** The first row of the file must contain the field names.
2.  **Exact Naming:** Column headers must **exactly match** the field names defined in the [Field Dictionary](field-dictionary.md) (e.g., use `device_id`, not `Device ID`).
3.  **One Record Per Row:** Each subsequent row represents one unique measurement (a specific parameter, at a specific time, from a specific device).
4.  **Location Columns:** You must use separate columns for `lat` and `lon`. (The nested `coordinates` object used in JSON is not supported in tabular files).

## Format-Specific Rules

### 1. CSV Files (`.csv`)
*   **Delimiter:** Fields must be separated by a comma (`,`).
*   **Encoding:** UTF-8 encoding is strongly recommended.
*   **No Internal Commas:** Data fields like `data_steward_name` must not contain commas, as this breaks the parsing structure.

### 2. Excel Files (`.xlsx`)
*   **First Sheet Only:** Data must be located on the **first sheet** (Worksheet 1) of the workbook. Data on subsequent sheets will be ignored by most AQDx parsers.
*   **No Metadata Headers:** Do not include "title rows" or merged cells above the header row. Row 1 must be the column headers.
*   **Formulas:** Avoid formulas. Values should be stored as raw text or numbers.

### 3. Parquet Files (`.parquet`)
*   **Schema Enforcement:** Ensure the column data types in the Parquet schema match the [AQDx Data Types](data-types.md) (e.g., `value` should be stored as a Float/Double, not a String).
*   **Efficiency:** This format is recommended for datasets exceeding 1 million rows.

## Example Table

Below is a visualization of a valid AQDx tabular structure.

| data_steward_name | device_id | datetime | lat | lon | parameter_code | value | unit_code | qc_code |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CityOfDenver | A1-Sensor | 2024-05-23T14:00:00-07:00 | 39.739 | -104.990 | 44201 | 45.2 | 008 | 0 |
| CityOfDenver | A1-Sensor | 2024-05-23T15:00:00-07:00 | 39.739 | -104.990 | 44201 | 42.1 | 008 | 0 |
| CityOfDenver | B2-Station | 2024-05-23T14:00:00-07:00 | 39.755 | -105.010 | 88101 | 12.5 | 105 | 0 |

> **Note:** The order of columns does not strictly matter, but keeping core fields (Who, What, When, Where) to the left makes manual review easier.