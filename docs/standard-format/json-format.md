# JSON Data Format

The JSON (JavaScript Object Notation) format is the standard AQDx method for **real-time data transmission**, API responses, and streaming data. Unlike the Tabular format, which is optimized for human readability and bulk history, JSON is optimized for machine-to-machine communication in real time.

AQDx supports two common JSON structures:

1. **Single Record / Stream (NDJSON):** A continuous stream of individual objects, separated by newlines. Ideal for live feeds.
2. **Batch Array:** A list of record objects wrapped in brackets `[...]`. Ideal for API responses containing a short history.

## General Requirements

To ensure your JSON data can be parsed by AQDx systems, you must follow these rules:

1. **Field Names:** JSON keys must **exactly match** the field names defined in the [Field Dictionary](field-dictionary.md).
   - _Correct:_ `"device_id": "A1"`
   - _Incorrect:_ `"DeviceID": "A1"` or `"deviceId": "A1"`
2. **Data Types:** You must respect the strict data types (String vs. Number).
   - **Strings:** Must be wrapped in double quotes (e.g., `"unit_code": "008"`).
   - **Numbers:** Must **not** be wrapped in quotes (e.g., `"parameter_value": 45.2`, `"validity_code": 1`).
3. **Required Fields:** All fields marked **"Value Required : Yes"** in the Field Dictionary must be present in every JSON object.
4. **File Termination:** All multi-line JSON files must end with a single newline character (`\n`).

## Handling Optional & Missing Values

Unlike CSV files where you must leave an empty space between commas, JSON allows flexibility for optional fields (like `elevation` or `method_code`).

If you do not have data for an optional field, you have two valid choices:

1. **Omit the Key (Preferred):** Simply do not include the field in the JSON object. This reduces file size.
2. **Send Null:** Include the key with a `null` value.

**Example:**

```json
// Option 1: Key Omitted (Preferred)
{
  "parameter_code": "44201",
  "parameter_value": 45.2
}

// Option 2: Explicit Null
{
  "parameter_code": "44201",
  "parameter_value": 45.2,
  "method_code": null
}
```

## Structure 1: Newline Delimited JSON (Streaming)

For real-time applications, use Newline Delimited JSON (NDJSON). Each line represents one complete measurement record. There are no commas between lines and no enclosing brackets.

**Format:**

```text
{record_1}\n
{record_2}\n
{record_3}\n
```

### Example stream

```json
{"dataset_id": "City_PM_Live", "device_id": "A1", "datetime": "2024-05-23T14:00:00-07:00", "parameter_code": "44201", "parameter_value": 45.2, "unit_code": "008", "duration": 60, "aggregation_code": 0, "validity_code": 0, "latitude": 39.739, "longitude": -104.990, "data_steward_name": "CityOfDenver", "device_manufacturer_name": "PurpleAir", "calibration_code": 0, "review_level_code": 0}
{"dataset_id": "City_PM_Live", "device_id": "A1", "datetime": "2024-05-23T14:01:00-07:00", "parameter_code": "44201", "parameter_value": 46.1, "unit_code": "008", "duration": 60, "aggregation_code": 0, "validity_code": 0, "latitude": 39.739, "longitude": -104.990, "data_steward_name": "CityOfDenver", "device_manufacturer_name": "PurpleAir", "calibration_code": 0, "review_level_code": 0}
```

## Structure 2: Standard JSON File (Batch)

For archival files or API responses, wrap the records in a standard JSON Array [...]. Note that this example has been indented and formatted for visualization purposes.

### Example file

```json
[
  {
    "dataset_id": "City_PM_2024",
    "data_steward_name": "CityOfDenver",
    "device_id": "B2-Station",
    "device_manufacturer_name": "MetOne",
    "datetime": "2024-05-23T14:00:00-07:00",
    "latitude": 39.755,
    "longitude": -105.01,
    "elevation": 1580.0,
    "parameter_code": "88101",
    "parameter_value": 12.5,
    "unit_code": "105",
    "method_code": "170",
    "duration": 3600,
    "aggregation_code": 1,
    "validity_code": 0,
    "calibration_code": 2,
    "review_level_code": 1,
    "detection_limit": 0.5
  },
  {
    "dataset_id": "City_PM_2024",
    "data_steward_name": "CityOfDenver",
    "device_id": "B2-Station",
    "device_manufacturer_name": "MetOne",
    "datetime": "2024-05-23T15:00:00-07:00",
    "latitude": 39.755,
    "longitude": -105.01,
    "elevation": 1580.0,
    "parameter_code": "88101",
    "parameter_value": null,
    "unit_code": "105",
    "method_code": "170",
    "duration": 3600,
    "aggregation_code": 1,
    "validity_code": 9,
    "calibration_code": 2,
    "review_level_code": 1,
    "qualifier_codes": "AM"
  }
]
```
