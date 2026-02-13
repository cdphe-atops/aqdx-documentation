# Field Dictionary

This page defines the standard vocabulary for the AQDx format. Regardless of whether you are using a tabular file (CSV/Excel) or a JSON stream, these field names and data types serve as the single source of truth.

## 1. Time & Measurement

These fields define _what_ was measured, _when_ it was measured, and _how much_ was found.

| Field Name                                | Data Type                 | Required | Description                                                                         |
| :---------------------------------------- | :------------------------ | :------- | :---------------------------------------------------------------------------------- |
| [**datetime**](#datetime)                 | ISO 8601 <br> String (29) | **Yes**  | The date and time of the measurement (start of the sampling period).                |
| [**parameter_code**](#parameter_code)     | String (5)                | **Yes**  | The 5-digit AQS code identifying the pollutant or variable.                         |
| [**parameter_value**](#parameter_value)   | Decimal (12,5)            | **Yes**  | The actual measured value.                                                          |
| [**unit_code**](#unit_code)               | String (3)                | **Yes**  | The 3-digit AQS code identifying the unit of measure.                               |
| [**method_code**](#method_code)           | String (3)                | **Yes**  | The 3-digit code for the measurement method.                                        |
| [**duration**](#duration)                 | Decimal (12,3)            | **Yes**  | The duration of the sample in seconds.                                              |
| [**aggregation_code**](#aggregation_code) | Integer (1)               | **Yes**  | Indicates the mathematical or physical method used to represent the data over time. |

<br>

### datetime

**Format:** ISO 8601 String (29) &emsp;&emsp;
**Example:** `2008-10-08T12:00:43-06:00`

The date and time of the data value. It must follow the "Date and time with the offset" ISO 8601 format `YYYY-MM-DDThh:mm:ssTZD`, where `TZD` is the Time Zone Designator (offset from UTC). See also: <https://en.wikipedia.org/wiki/ISO_8601>

- **Precision:** For data reporting faster than 1Hz (less than one second), report seconds with a decimal (ss.sss). The maximum allowed precision is milliseconds, translating to a maximum allowed string length of 29 characters.
- **Timing:** The timestamp corresponds to the **beginning** of the averaging or sampling period.
- **Time Zone:** Must include the offset (e.g., `-06:00` for CST, `+00:00` for UTC). Do not use "Z" for UTC.

---

### parameter_code

**Format:** String (5) &emsp;&emsp;
**Example:** `44201` (Ozone)

A 5-digit numerical code that identifies the parameter being measured. These codes are based on the EPA's Air Quality System (AQS) parameter library.

- **Common Codes:**
  - `44201`: Ozone (O3)
  - `88101`: PM2.5 - Local Conditions
  - `61101`: Wind Speed
- **Note:** Only list one parameter code per data record.
<!-- *   [View Parameter Codes](../appendices/parameter-codes.md) -->

### parameter_value

**Format:** Decimal (12,5) &emsp;&emsp;
**Example:** `35.5`

The actual data value of the specified parameter.

- **Precision:** Round data to the 5th decimal place if the measured value has larger precision than 5 decimal places.
- **Formatting:** Do not use commas (e.g., use `1500`, not `1,500`).
- **Missing Data:** Leave the field blank (CSV: `,,`) if the data is missing. Do not use a fill value such as `-999`. Do not use empty string "".
- **Whole Numbers:** Always include a decimal point (e.g., `85.0` instead of `85`).

### unit_code

**Format:** String (3) &emsp;&emsp;
**Example:** `008` (ppb)

A 3-digit code associated with the units of the measurement.

- **Common Codes:**
  - `008`: Parts per billion (ppb)
  - `001`: Micrograms/cubic meter (µg/m³) at 25°C
  - `105`: Micrograms/cubic meter (µg/m³) at Local Conditions
  - `017`: Degrees Centigrade (°C)

### method_code

**Format:** String (3) &emsp;&emsp;
**Example:** `170` (Met One BAM-1020)

A 3-digit code associated with the method used to perform an EPA-designated FRM or FEM measurement.

- **Sensors:** Leave this field null (`,,` for csv) if the device is a low-cost sensor or has not been EPA-designated.
- **Regulatory:** Required for FRM/FEM instruments.

### duration

**Format:** Decimal (12,3) &emsp;&emsp;
**Example:** `3600.000`

The duration of the sampling period or aggregation window in seconds. Fractional seconds are allowed up to milliseconds (3 digits after the decimal point).

For long-term aggregations (like months or years), standard generalized timeframes are recommended to maintain consistency across leap years and varying month lengths, unless the exact physical duration of a specific period is required.

**Common Duration Values:**

- `60` = 1 Minute (decimal point is not strictly required)
- `900.000` = 15 Minutes
- `3600.000` = 1 Hour
- `86400` = 1 Day (24 Hours)
- `604800` = 1 Week (7 Days)
- `2592000` = 1 Month (Standardized 30-Day Period)
- `31536000` = 1 Year (Standardized 365-Day Period)

### aggregation_code

**Format:** Integer &emsp;&emsp;
**Example:** `1` (Mean)

Indicates the mathematical or physical method used to represent the data over the specified `duration`.

- `0`: **None / Native Resolution.** The data is reported at the instrument's native sampling frequency.
- `1`: **Mean (Average).** The mathematical average of measurements over the specified `duration`.
- `2`: **Time-Integrated (Physical).** A single physical sample accumulated over the `duration` (e.g., a 24-hour PM filter or VOC canister).
- `3`: **Maximum.** The highest single value recorded within the `duration`.
- `4`: **Median (50th Percentile).** The middle value of the measurements within the `duration`.
- `5`: **Rolling / Moving Average.** A mathematical average calculated over a moving look-back window (e.g., an 8-hour rolling ozone average).
- `6`: **Spatial Aggregation.** Data grouped by a geographic boundary rather than strictly by time (e.g., binning mobile data into 50-meter road segments).
- `7`: **Other.** Any aggregation method not listed above, including specific statistical percentiles (e.g., 90th, 98th). Specific details of the method used must be documented in the accompanying AQDx metadata form.

---

## 2. Location

These fields define _where_ the measurement was taken.

| Field Name                  | Data Type     | Required | Description                         |
| :-------------------------- | :------------ | :------- | :---------------------------------- |
| [**latitude**](#latitude)   | Decimal (9,5) | **Yes**  | Latitude in WGS84 decimal degrees.  |
| [**longitude**](#longitude) | Decimal (9,5) | **Yes**  | Longitude in WGS84 decimal degrees. |
| [**elevation**](#elevation) | Decimal (8,2) | No       | Elevation of the device in meters.  |

<br>

### latitude

**Format:** Decimal (9,5) &emsp;&emsp;
**Example:** `39.7392`

Latitude in decimal degrees (WGS84).

- **Positive:** North of the Equator.
- **Negative:** South of the Equator.
- **Precision:** Report to the 5th decimal point (~1 meter precision).

### longitude

**Format:** Decimal (9,5) &emsp;&emsp;
**Example:** `-104.9903`

Longitude in decimal degrees (WGS84).

- **Positive:** East of the Prime Meridian.
- **Negative:** West of the Prime Meridian (e.g., USA).
- **Precision:** Report to the 5th decimal point.

### elevation

**Format:** Decimal (8,2) &emsp;&emsp;
**Example:** `1609.3`

Elevation of the device in meters above mean sea level (MSL).

---

## 3. Device & Organization

These fields define _who_ collected the data and _with what_ hardware.

| Field Name                                                | Data Type   | Required | Description                                |
| :-------------------------------------------------------- | :---------- | :------- | :----------------------------------------- |
| [**device_id**](#device_id)                               | String (64) | **Yes**  | Unique serial number or ID of the device.  |
| [**data_steward_name**](#data_steward_name)               | String (64) | **Yes**  | The organization responsible for the data. |
| [**device_manufacturer_name**](#device_manufacturer_name) | String (64) | **Yes**  | The maker of the instrument.               |

<br>

### device_id

**Format:** String (64) &emsp;&emsp;
**Example:** `A123-Sensor-01`

Serial number of the device performing the measurement.

- **Allowed Characters:** Spaces and hyphens.
- **Forbidden:** Do not use commas or periods.

### data_steward_name

**Format:** String (64) &emsp;&emsp;
**Example:** `CityOfDenver` or `city_of_denver`

Name of the party responsible for data oversight.

- **Formatting:** Use PascalCase or snake_case to separate words.
- **Forbidden:** Do not use commas, spaces, or periods.

### device_manufacturer_name

**Format:** String (64) &emsp;&emsp;
**Example:** `PurpleAir`, `Teledyne`

Name of the manufacturer associated with the device.

- **Formatting:** Use PascalCase or snake_case.
- **Forbidden:** Do not use commas, spaces, or periods.

---

## 4. Quality Control (QC)

These fields describe the quality and processing level of the data.

| Field Name                                  | Data Type      | Required | Description                                                                           |
| :------------------------------------------ | :------------- | :------- | :------------------------------------------------------------------------------------ |
| [**validity_code**](#validity_code)         | Integer        | **Yes**  | The assessed validity of the individual measurement.                                  |
| [**correction_code**](#correction_code)     | Integer (1)    | **Yes**  | Indicates whether the data has been corrected or calibrated against a known standard. |
| [**review_level_code**](#review_level_code) | Integer (1)    | **Yes**  | Indicates the level of human review the dataset has undergone.                        |
| [**detection_limit**](#detection_limit)     | Decimal (12,5) | No       | Detection limit for the method used to measure `parameter_value`.                     |
| [**qualifier_codes**](#qualifier_codes)     | String (254)   | No       | Space-separated codes explaining why data was flagged or describing specific events.  |

<br>

### validity_code

**Format:** Integer &emsp;&emsp;
**Example:** `0` (Valid)

The assessed validity of the individual measurement. Validation extends beyond simple statistical outlier detection; it evaluates physical limits, hardware faults, "sticking" (unchanging) values, sensor degradation, and data completeness.

- `0`: **Validation not performed.** Raw data directly from the device. No automated or manual quality control (QC) checks have been applied.
- `1`: **Valid.** Data passed all QC checks and is considered accurate for analysis.
- `3`: **Estimated.** Data is considered valid, but the value was mathematically derived or interpolated rather than directly measured at this exact timestamp.
- `5`: **Suspect.** Data is physically possible but exhibits anomalous behavior (e.g., unexplained spikes, deviation from neighboring sensors, or operation during extreme weather). There is insufficient evidence to invalidate it entirely, but it should be used with caution.
- `9`: **Invalid.** Known bad data that should not be used. Includes instrument malfunctions, failed range checks, or data failing completeness criteria (e.g., insufficient uptime for an hourly average).

### correction_code

**Format:** Integer &emsp;&emsp;
**Example:** `1` (Global / Generic)

Indicates whether a mathematical correction or calibration model was applied to the data to improve its accuracy. While `validity_code` identifies _if_ a measurement is trustworthy (identifying faults or outliers), `correction_code` tracks if the numerical `parameter_value` was actively adjusted to account for known biases (e.g., humidity interference, sensor drift, or collocation offsets).

- `0`: **None / As Measured.** The data is reported exactly as output by the device (using the manufacturer's default factory calibration). No post-collection adjustments have been made.
- `1`: **Global / Generic.** The data was adjusted using a broad, universal equation applicable to all sensors of this type (e.g., applying a generic relative humidity correction, or using the national EPA correction equation for PurpleAir data).
- `2`: **Local / Collocated.** The data was adjusted using a site-specific or region-specific model. This is typically derived by collocating the sensor with a nearby regulatory reference monitor and adjusting the data based on the resulting comparison (e.g., applying a linear regression slope and intercept).
- `3`: **Reference Standard.** The data was calibrated directly against a certified physical reference standard (e.g., adjusted using known span gas or zero-air checks).

### review_level_code

**Format:** Integer (1) &emsp;&emsp;
**Example:** `1` (Internal Review)

Indicates the level of human review the dataset has undergone.

- `0`: **Raw.** Direct from device, no human review.
- `1`: **Internal.** Reviewed by the data creator/project team.
- `2`: **External.** Audited by an independent third party.
- `3`: **Certified.** Legally certified for regulatory use (requires FRM/FEM).

### detection_limit

**Format:** Decimal (12,5) &emsp;&emsp;
**Example:** `0.50000`

- The detection limit for the measurement, expressed in the same units as `parameter_value` (i.e., the record’s `unit_code`).
- This field is optional and should be left blank/omitted when a detection limit is unknown, not applicable, or only documented at a higher (instrument/project) level.
- Please note the method used to determine the detection limit in the metadata form included with the submission

### qualifier_codes

**Format:** String (254) &emsp;&emsp;
**Example:** `IM`

Space-separated codes explaining why data was flagged or describing specific events.

- **Examples:**
  - `IM` (Prescribed Fire)
  - `LJ` (High Winds)
  - `AA AG BG ND` (Multiple qualifier codes in one measurement)
- See the full list of AQS Qualifier Codes: <https://aqs.epa.gov/aqsweb/documents/codetables/qualifiers.html>
