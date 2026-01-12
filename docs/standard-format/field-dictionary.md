# Field Dictionary

This page defines the standard vocabulary for the AQDx format. Regardless of whether you are using a tabular file (CSV/Excel) or a JSON stream, these field names and data types serve as the single source of truth.

## 1. Time & Measurement
These fields define *what* was measured, *when* it was measured, and *how much* was found.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| [**datetime**](#datetime) | ISO 8601 <br> String (29) | **Yes** | The date and time of the measurement (start of the sampling period). |
| [**parameter_code**](#parameter_code) | String (5) | **Yes** | The 5-digit AQS code identifying the pollutant or variable. |
| [**parameter_value**](#parameter_value) | Decimal (12,5) | **Yes** | The actual measured value. |
| [**unit_code**](#unit_code) | String (3) | **Yes** | The 3-digit AQS code identifying the unit of measure. |
| [**duration**](#duration) | Decimal (9,3) | **Yes** | The duration of the sample in seconds. |
| [**method_code**](#method_code) | String (3) | **Yes** | The 3-digit code for the measurement method. |

<br>

### datetime
**Format:** ISO 8601 String (29) &emsp;&emsp;
**Example:** `2008-10-08T12:00:43-06:00`

The date and time of the data value. It must follow the "Date and time with the offset" ISO 8601 format `YYYY-MM-DDThh:mm:ssTZD`, where `TZD` is the Time Zone Designator (offset from UTC). See also: https://en.wikipedia.org/wiki/ISO_8601

*   **Precision:** For data reporting faster than 1Hz (less than one second), report seconds with a decimal (ss.sss). The maximum allowed precision is milliseconds, translating to a maximum allowed string length of 29 characters.
*   **Timing:** The timestamp corresponds to the **beginning** of the averaging or sampling period.
*   **Time Zone:** Must include the offset (e.g., `-06:00` for CST, `+00:00` for UTC). Do not use "Z" for UTC.
****
### parameter_code
**Format:** String (5) &emsp;&emsp;
**Example:** `44201` (Ozone)

A 5-digit numerical code that identifies the parameter being measured. These codes are based on the EPA's Air Quality System (AQS) parameter library.

*   **Common Codes:**
    *   `44201`: Ozone (O3)
    *   `88101`: PM2.5 - Local Conditions
    *   `61101`: Wind Speed
*   **Note:** Only list one parameter code per data record.
*   [View Parameter Codes](../appendices/parameter-codes.md)

### parameter_value
**Format:** Decimal (12,5) &emsp;&emsp;
**Example:** `35.5`

The actual data value of the specified parameter.

*   **Precision:** Round data to the 5th decimal place if the measured value has larger precision than 5 decimal places.
*   **Formatting:** Do not use commas (e.g., use `1500`, not `1,500`).
*   **Missing Data:** Leave the field blank (CSV: `,,`) if the data is missing. Do not use a fill value such as `-999`. Do not use empty string "".
*   **Whole Numbers:** Always include a decimal point (e.g., `85.0` instead of `85`).

### unit_code
**Format:** String (3) &emsp;&emsp;
**Example:** `008` (ppb)

A 3-digit code associated with the units of the measurement.

*   **Common Codes:**
    *   `008`: Parts per billion (ppb)
    *   `001`: Micrograms/cubic meter (µg/m³) at 25°C
    *   `105`: Micrograms/cubic meter (µg/m³) at Local Conditions
    *   `017`: Degrees Centigrade (°C)

### duration
**Format:** Decimal &emsp;&emsp;
**Example:** `3600.0`

The duration of the sampling period in seconds.

*   `3600.0` = 1 Hour
*   `60.0` = 1 Minute
*   `900.0` = 15 Minutes

### method_code
**Format:** String (3) &emsp;&emsp;
**Example:** `170` (Met One BAM-1020)

A 3-digit code associated with the method used to perform an EPA-designated FRM or FEM measurement.

*   **Sensors:** Leave this field blank (`,,`) if the device is a low-cost sensor or has not been EPA-designated.
*   **Regulatory:** Required for FRM/FEM instruments.

---

## 2. Location
These fields define *where* the measurement was taken.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| [**lat**](#lat) | Decimal (9,5) | **Yes** | Latitude in WGS84 decimal degrees. |
| [**lon**](#lon) | Decimal (9,5) | **Yes** | Longitude in WGS84 decimal degrees. |
| [**elev**](#elev) | Decimal (8,2) | No | Elevation of the device in meters. |
| [**coordinates**](#coordinates) | Array | No | (JSON Only) GeoJSON array: **[lon, lat]**. <br> *note:* This is swapped from typical lat, lon |

<br>

### lat
**Format:** Decimal (9,5) &emsp;&emsp;
**Example:** `39.7392`

Latitude in decimal degrees (WGS84).

*   **Positive:** North of the Equator.
*   **Negative:** South of the Equator.
*   **Precision:** Report to the 5th decimal point (~1 meter precision).

### lon
**Format:** Decimal (9,5) &emsp;&emsp;
**Example:** `-104.9903`

Longitude in decimal degrees (WGS84).

*   **Positive:** East of the Prime Meridian.
*   **Negative:** West of the Prime Meridian (e.g., USA).
*   **Precision:** Report to the 5th decimal point.

### elev
**Format:** Decimal (8,2) &emsp;&emsp;
**Example:** `1609.3`

Elevation of the device in meters above mean sea level (MSL).

### coordinates
**Format:** Array of Decimals [**lon**, **lat**] &emsp;&emsp;
**Example:** `[-104.9903, 39.7392]`

**(JSON Only)** To comply with GeoJSON, the longitude and latitude are included as a list under the `location.coordinates` key.

*   **Order:** Always `[lon, lat]` (Longitude first).

---

## 3. Device & Organization
These fields define *who* collected the data and *with what* hardware.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| [**device_id**](#device_id) | String (64) | **Yes** | Unique serial number or ID of the device. |
| [**data_steward_name**](#data_steward_name) | String (64) | **Yes** | The organization responsible for the data. |
| [**device_manufacturer_name**](#device_manufacturer_name) | String (64) | **Yes** | The maker of the instrument. |

<br>

### device_id
**Format:** String (64) &emsp;&emsp;
**Example:** `A123-Sensor-01`

Serial number of the device performing the measurement.

*   **Allowed Characters:** Spaces and hyphens.
*   **Forbidden:** Do not use commas or periods.

### data_steward_name
**Format:** String (64) &emsp;&emsp;
**Example:** `CityOfDenver` or `city_of_denver`

Name of the party responsible for data oversight.

*   **Formatting:** Use PascalCase or snake_case to separate words.
*   **Forbidden:** Do not use commas, spaces, or periods.

### device_manufacturer_name
**Format:** String (64) &emsp;&emsp;
**Example:** `PurpleAir`, `Teledyne`

Name of the manufacturer associated with the device.

*   **Formatting:** Use PascalCase or snake_case.
*   **Forbidden:** Do not use commas, spaces, or periods.

---

## 4. Quality Control (QC)
These fields describe the quality and processing level of the data.

| Field Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| [**autoqc_check**](#autoqc_check) | Integer (1) | **Yes** | Has automated QC been applied? (0=No, 1=Yes) |
| [**corr_code**](#corr_code) | Integer (1) | **Yes** | Has the data been corrected or calibrated? (0=No, 1=Yes) |
| [**review_level_code**](#review_level_code) | Integer (1) | **Yes** | What level of human review has occurred? |
| [**qc_code**](#qc_code) | Integer (1) | **Yes** | The assessed validity of the measurement. |
| [**qualifier_codes**](#qualifier_codes) | String (254) | No | Space-separated codes explaining flags. |

<br>

### autoqc_check
**Format:** Integer (1) &emsp;&emsp;
**Example:** `1` (Yes)

Indicates whether automated quality control (QC) tools/algorithms have been applied to the data (e.g., range checks, sticking checks).

*   `0`: **No.** Raw, unprocessed data.
*   `1`: **Yes.** Automated checks have been applied.

### corr_code
**Format:** Integer (1) &emsp;&emsp;
**Example:** `1` (Yes)

Indicates whether the data has been corrected or calibrated against a known standard.

*   `0`: **No.** Initial, unprocessed data.
*   `1`: **Yes.** Data has been adjusted/aligned using a documented method.

### review_level_code
**Format:** Integer (1) &emsp;&emsp;
**Example:** `1` (Internal Review)

Indicates the level of human review the dataset has undergone.

*   `0`: **Raw.** Direct from device, no human review.
*   `1`: **Internal.** Reviewed by the data creator/project team.
*   `2`: **External.** Audited by an independent third party.
*   `3`: **Certified.** Legally certified for regulatory use (requires FRM/FEM).

### qc_code
**Format:** Integer (1) &emsp;&emsp;
**Example:** `0` (Valid)

The validity status of the individual measurement.

*   `0`: **Valid.** Data is good.
*   `1`: **Estimated.** Valid but estimated (e.g., interpolated).
*   `7`: **Suspect.** Data looks weird but hasn't been proven invalid.
*   `8`: **Invalid.** Known bad data (e.g., malfunction).
*   `9`: **Missing.** No value recorded.

### qualifier_codes
**Format:** String (254) &emsp;&emsp;
**Example:** `IM`

Space-separated codes explaining why data was flagged or describing specific events.

*   **Examples:** 
    *   `IM` (Prescribed Fire)
    *    `LJ` (High Winds)
    *    `AA AG BG ND` (Multiple qualifier codes in one measurement)
*   See the full list of AQS Qualifier Codes: https://aqs.epa.gov/aqsweb/documents/codetables/qualifiers.html