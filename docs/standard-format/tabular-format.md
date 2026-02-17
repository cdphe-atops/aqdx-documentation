# Tabular Data Files (CSV, Excel, Parquet)

The Tabular format is the standard method for exchanging historical datasets, batch uploads, and archival data. In this format, every record is a row, and every field is a column.

AQDx supports the following file types:

- **CSV** (`.csv`): Comma-Separated Values (Universal standard).
- **Excel** (`.xlsx`): Microsoft Excel Open XML Spreadsheet.
- **Parquet** (`.parquet`): Columnar storage format for large datasets.

## General Requirements

Regardless of the file type, all tabular files must adhere to these structure rules:

1. **Header Row:** The first row of the file must contain the field names.
2. **All Columns Required:** You must include **every column** listed in the [Field Dictionary](field-dictionary.md) as a header, even if you do not have data for that field (e.g., `elevation` or `qualifier_codes`). If a column is missing, the file will be rejected.
3. **Exact Naming:** Column headers must **exactly match** the field names defined in the Field Dictionary (e.g., use `device_id`, not `Device ID`).
4. **One Record Per Row:** Each subsequent row represents one unique measurement (a specific parameter, at a specific time, from a specific device).
5. **Location Columns:** You must use separate columns for `latitude` and `longitude`.

## Format-Specific Rules

### 1. CSV Files (`.csv`)

- **Delimiter:** Fields must be separated by a comma (`,`).
- **Encoding:** UTF-8 encoding is required.
- **No Internal Commas:** Data fields like `data_steward_name` must not contain commas, as this breaks the parsing structure.
- **Handling Empty Fields:** If an optional field is blank (e.g., `method_code`), keep the comma placeholders.
  - _Correct:_ `...,44201,,45.2,...`
  - _Incorrect:_ `...,44201,45.2,...` (Skipping the column entirely shifts all subsequent data).

### 2. Excel Files (`.xlsx`)

- **First Sheet Only:** Data must be located on the **first sheet** (Worksheet 1) of the workbook. Data on subsequent sheets will be ignored.
- **No Metadata Headers:** Do not include "title rows" or merged cells above the header row. Row 1 must be the column headers.
- **Formulas:** Avoid formulas. Values must be stored as raw text or numbers.

### 3. Parquet Files (`.parquet`)

- **Schema Enforcement:** Ensure the column data types in the Parquet schema match the [AQDx Data Types](data-types.md) (e.g., `parameter_value` should be stored as a Float/Double, not a String).
- **Efficiency:** This format is recommended for datasets exceeding 1 million rows.

## Required Column Checklist

Before submitting, verify your file contains headers for **all** of the following fields.

**Time & Measurement**

- `datetime`
- `parameter_code`
- `parameter_value`
- `unit_code`
- `method_code` (Can be empty)
- `duration`
- `aggregation_code`

**Location**

- `latitude`
- `longitude`
- `elevation` (Can be empty)

**Device & Identity**

- `device_id`
- `data_steward_name`
- `device_manufacturer_name`
- `dataset_id` (Required on every row)

**Quality Control**

- `validity_code`
- `calibration_code`
- `review_level_code`
- `detection_limit` (Can be empty)
- `qualifier_codes` (Can be empty)

## Example Table

Below is a visualization of a valid AQDx tabular structure with all required columns. Note that **optional** fields (like `qualifier_codes`) are included as headers, even if the cells are empty.

> **Scroll right to view all columns.**

| dataset_id   | data_steward_name | device_id  | datetime                  | latitude | longitude | elevation | parameter_code | parameter_value | unit_code | method_code | duration | aggregation_code | validity_code | calibration_code | review_level_code | detection_limit | qualifier_codes |
| :----------- | :---------------- | :--------- | :------------------------ | :------- | :-------- | :-------- | :------------- | :-------------- | :-------- | :---------- | :------- | :--------------- | :------------ | :--------------- | :---------------- | :-------------- | :-------------- |
| City_PM_2024 | CityOfDenver      | A1-Sensor  | 2024-05-23T14:00:00-07:00 | 39.739   | -104.990  | 1609.3    | 44201          | 45.2            | 008       |             | 3600     | 1                | 0             | 0                | 0                 |                 |                 |
| City_PM_2024 | CityOfDenver      | A1-Sensor  | 2024-05-23T15:00:00-07:00 | 39.739   | -104.990  | 1609.3    | 44201          | 42.1            | 008       |             | 3600     | 1                | 0             | 0                | 0                 |                 |                 |
| City_PM_2024 | CityOfDenver      | B2-Station | 2024-05-23T14:00:00-07:00 | 39.755   | -105.010  | 1580.0    | 88101          | 12.5            | 105       | 170         | 3600     | 1                | 0             | 0                | 0                 | 0.5             |                 |
| City_PM_2024 | CityOfDenver      | B2-Station | 2024-05-23T15:00:00-07:00 | 39.755   | -105.010  | 1580.0    | 88101          |                 | 105       | 170         | 3600     | 1                | 9             | 0                | 0                 | 0.5             | AM              |

**Note on Missing Values:**
In the last row above, the `parameter_value` is missing (empty). Therefore, the `validity_code` is set to `9` (Invalid/Missing), and a `qualifier_code` (`AM`) is provided to explain the missing data.
