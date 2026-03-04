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
4. **Column Order:** The exact order of the columns does not matter for machine parsing, provided all required headers are present and spelled correctly. However, for human readability, it is **strongly recommended** to group columns in the order shown in the field dictionary.
5. **One Record Per Row:** Each subsequent row represents one unique measurement (a specific parameter, at a specific time, from a specific device).
6. **Location Columns:** You must use separate columns for `latitude` and `longitude`.

## Format-Specific Rules

### 1. CSV Files (`.csv`)

- **Delimiter:** Fields must be separated by a comma (`,`).
- **Encoding:** UTF-8 encoding is required.
- **No Internal Commas:** Data fields like `data_steward_name` must not contain commas, as this breaks the parsing structure.
- **Handling Empty Fields:** If an optional field is blank (e.g., `method_code`), keep the comma placeholders.
  - _Correct:_ `...,44201,,45.2,...`
  - _Incorrect:_ `...,44201,45.2,...` (Skipping the column entirely shifts all subsequent data).
- **File Compression:** CSV files may be gzip compressed (e.g. `*.csv.gz`) to save storage space.

### 2. Excel Files (`.xlsx`)

- **First Sheet Only:** Data must be located on the **first sheet** (Worksheet 1) of the workbook. Data on subsequent sheets will be ignored.
- **No Metadata Headers:** Do not include "title rows" or merged cells above the header row. Row 1 must be the column headers.
- **Formulas:** Avoid formulas. Values must be stored as raw text or numbers.

### 3. Parquet Files (`.parquet`)

- **Schema Enforcement:** Ensure the column data types in the Parquet schema match the [AQDx Data Types](data-types.md) (e.g., `parameter_value` should be stored as a Float/Double, not a String).
- **Efficiency:** This format is recommended for datasets exceeding 1 million rows.

## Example file (`.csv`)

```csv
datetime,parameter_code,parameter_value,unit_code,method_code,duration,aggregation_code,latitude,longitude,elevation,data_steward_name,device_manufacturer_name,device_id,measurement_technology_code,instrument_classification,dataset_id,validity_code,calibration_code,review_level_code,detection_limit,qualifier_codes
2024-05-23T14:00:00-07:00,88101,12.50000,105,170,3600,1,39.75500,-105.01000,1580.0,CityOfDenver,MetOne,B2-Station,CF-SSvs-BA,1,CityOfDenver_B2_20240523,1,2,1,0.50000,
2024-05-23T15:00:00-07:00,88101,,105,170,3600,1,39.75500,-105.01000,1580.0,CityOfDenver,MetOne,B2-Station,CF-SSvs-BA,1,CityOfDenver_B2_20240523,9,2,1,0.50000,AB
```

| datetime                  | parameter_code | parameter_value | unit_code | method_code | duration | aggregation_code | latitude | longitude  | elevation | data_steward_name | device_manufacturer_name | device_id  | measurement_technology_code | instrument_classification | dataset_id               | validity_code | calibration_code | review_level_code | detection_limit | qualifier_codes |
| :------------------------ | :------------- | :-------------- | :-------- | :---------- | :------- | :--------------- | :------- | :--------- | :-------- | :---------------- | :----------------------- | :--------- | :-------------------------- | :------------------------ | :----------------------- | :------------ | :--------------- | :---------------- | :-------------- | :-------------- |
| 2024-05-23T14:00:00-07:00 | 88101          | 12.50000        | 105       | 170         | 3600     | 1                | 39.75500 | -105.01000 | 1580.0    | CityOfDenver      | MetOne                   | B2-Station | CF-SSvs-BA                  | 1                         | CityOfDenver_B2_20240523 | 1             | 2                | 1                 | 0.50000         |                 |
| 2024-05-23T15:00:00-07:00 | 88101          |                 | 105       | 170         | 3600     | 1                | 39.75500 | -105.01000 | 1580.0    | CityOfDenver      | MetOne                   | B2-Station | CF-SSvs-BA                  | 1                         | CityOfDenver_B2_20240523 | 9             | 2                | 1                 | 0.50000         | AB              |

> Note on Missing Data in CSV: Notice how missing or optional values are handled in the example above. For instance, the parameter_value is missing in the second row, and qualifier_codes is not used in the first row.
