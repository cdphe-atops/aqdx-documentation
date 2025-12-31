# Field Dictionary

This page defines the standard vocabulary for the AQDx format. Regardless of whether you are using a tabular file (CSV/Excel) or a JSON stream, these field names and data types serve as the single source of truth.

## 1. Time & Measurement
These fields define *what* was measured, *when* it was measured, and *how much* was found.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **`datetime`** | ISO 8601 String | **Yes** | The date and time of the measurement (start of the sampling period).<br>Format: `YYYY-MM-DDThh:mm:ssTZD`<br>Example: `2024-05-23T14:30:00-07:00` |
| **`parameter_code`** | Integer (5) | **Yes** | The 5-digit AQS code identifying the pollutant or variable (e.g., `44201` for Ozone). See [Parameter Codes](../appendices/parameter-codes.md). |
| **`value`** | Decimal | **Yes** | The actual measured number. <br>Example: `45.2` |
| **`unitcode`** | Integer (3) | **Yes** | The 3-digit AQS code identifying the unit of measure (e.g., `008` for ppb). |
| **`duration`** | Decimal | **Yes** | The duration of the sample in seconds.<br>Example: `3600` (1 hour), `60` (1 minute). |
| **`methodcode`** | Integer (3) | **Yes*** | The 3-digit code for the measurement method. <br>*Required for FRM/FEM instruments; leave blank for sensors.* |

## 2. Location
These fields define *where* the measurement was taken.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **`lat`** | Decimal (9,5) | **Yes** | Latitude in decimal degrees (WGS84). Positive is North, Negative is South.<br>Example: `39.7392` |
| **`lon`** | Decimal (9,5) | **Yes** | Longitude in decimal degrees (WGS84). Positive is East, Negative is West.<br>Example: `-104.9903` |
| **`elev`** | Decimal | No | Elevation of the device in meters above mean sea level (MSL). |

## 3. Device & Organization
These fields define *who* collected the data and *with what* hardware.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **`deviceid`** | String (64) | **Yes** | Unique serial number or ID of the specific device.<br>Example: `A123-Sensor-01` |
| **`datastewardname`** | String (64) | **Yes** | The organization responsible for the data. Use PascalCase or snake_case.<br>Example: `CityOfDenver` or `city_of_denver` |
| **`devicemanufacturername`** | String (64) | **Yes** | The maker of the instrument. <br>Example: `PurpleAir`, `TeledyneAPI` |

## 4. Quality Control (QC)
These fields describe the quality and processing level of the data.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **`qccode`** | Integer (1) | **Yes** | The validity of the measurement.<br>`0`: Valid, `1`: Estimated, `7`: Suspect, `8`: Invalid, `9`: Missing. |
| **`autoqccheck`** | Integer (1) | **Yes** | Has automated QC been applied? <br>`0`: No (Raw), `1`: Yes. |
| **`corrcode`** | Integer (1) | **Yes** | Has the data been corrected or calibrated?<br>`0`: No, `1`: Yes. |
| **`reviewlevelcode`** | Integer (1) | **Yes** | What level of human review has occurred?<br>`0`: None, `1`: Internal, `2`: External, `3`: Certified. |
| **`qualifiercodes`** | String (254) | No | Space-separated codes explaining why data was flagged (e.g., `IM` for Prescribed Fire). |

## 5. Metadata & Implementation
Additional fields for licensing and specific implementation details.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **`datalicensecode`** | Integer (1) | No | The license governing data reuse. `0`: None, `1`: ODbL, `2`: CC-BY-4.0. |
| **`samplehash`** | String (64) | No | **(Streaming Only)** A unique ID to link simultaneous measurements (e.g., PM2.5 and PM10) that might have slightly different timestamps due to transmission lag. |

---

### Note on GeoJSON
In the **JSON implementation** of this standard, the `lat` and `lon` fields are often combined into a GeoJSON `coordinates` array for compatibility with mapping software.
- **Tabular:** Use separate columns `lat` and `lon`.
- **JSON:** You may use `lat`/`lon` keys OR a `coordinates: [lon, lat]` array. Both are valid as long as the values are decimal degrees.
