# Field Dictionary

This page defines the standard vocabulary for the AQDx format. Regardless of whether you are using a tabular file (CSV/Excel) or a JSON stream, these field names and data types serve as the single source of truth.

## 1. Time & Measurement

These fields define _what_ was measured, _when_ it was measured, and _how much_ was found.

| Field Name                                | Data Type                 | Value Required | Description                                                                         |
| :---------------------------------------- | :------------------------ | :------------- | :---------------------------------------------------------------------------------- |
| [**datetime**](#datetime)                 | ISO 8601 <br> String (29) | Yes            | The date and time of the measurement (start of the sampling period).                |
| [**parameter_code**](#parameter_code)     | String (5)                | Yes            | The 5-digit AQS code identifying the pollutant or variable.                         |
| [**parameter_value**](#parameter_value)   | Decimal (12,5)            | No             | The actual measured value.                                                          |
| [**unit_code**](#unit_code)               | String (3)                | Yes            | The 3-digit AQS code identifying the unit of measure.                               |
| [**method_code**](#method_code)           | String (3)                | No             | The 3-digit code for the measurement method.                                        |
| [**duration**](#duration)                 | Decimal (12,3)            | Yes            | The duration of the sample in seconds.                                              |
| [**aggregation_code**](#aggregation_code) | Integer (1)               | Yes            | Indicates the mathematical or physical method used to represent the data over time. |

<br>

### datetime

**Format:** ISO 8601 String (29) &emsp;&emsp;
**Example:** `2008-10-08T12:00:43-06:00`

The date and time of the data value. It must follow the "Date and time with the offset" ISO 8601 format `YYYY-MM-DDThh:mm:ssTZD`, where `TZD` is the Time Zone Designator (offset from UTC). See also: <https://en.wikipedia.org/wiki/ISO_8601>

- **Precision:** For data reporting faster than 1Hz (less than one second), report seconds with a decimal (ss.sss). The maximum allowed precision is milliseconds, translating to a maximum allowed string length of 29 characters.
- **Timing:** The timestamp corresponds to the **beginning** of the averaging or sampling period.
- **Time Zone:** Must include the offset (e.g., `-06:00` for CST, `+00:00` for UTC). Do not use "Z" for UTC.
- see more details in [Data Types & Conventions](/aqdx-documentation/standard-format/data-types/#date-time-datetime)

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
- **Note:** Parameter code **cannot be blank**, if a parameter code or method_code is missing for your project, please open a [github issue](https://github.com/cdphe-atops/aqdx-documentation/issues) to have a code or codes added.

- [View Parameter Codes](/aqdx-documentation/code-lookup-tables/parameter-codes/)

### parameter_value

**Format:** Decimal (12,5) &emsp;&emsp;
**Example:** `35.5`

The actual data value of the specified parameter.

- **Precision:** Round data to the 5th decimal place if the measured value has larger precision than 5 decimal places.
- **Formatting:** Do not use commas (e.g., use `1500`, not `1,500`).
- **Can be blank:** Leave the field blank if the measurement could not be taken or is missing.
  - **Zero vs. Null:** distinct meanings must be preserved.
    - **`0.0`**: A valid measurement indicating zero concentration.
    - **Blank / Null**: The absence of a measurement (e.g., power failure, maintenance, sensor error).
  - **Validation Rules:**
    - If `parameter_value` is blank, the `validity_code` must be **9** (Invalid/Missing) for processed data or **0** (Not Validated) for raw data.
    - If `parameter_value` is blank, it is recommended to provide a `qualifier_code` (e.g., `AM` for Miscellaneous Void) to explain the missing data.

### unit_code

**Format:** String (3) &emsp;&emsp;
**Example:** `008` (ppb)

A 3-digit code associated with the units of the measurement.

- **Common Codes:**
  - `008`: Parts per billion (ppb)
  - `001`: Micrograms/cubic meter (µg/m³) at 25°C
  - `105`: Micrograms/cubic meter (µg/m³) at Local Conditions
  - `017`: Degrees Centigrade (°C)
  - [View Unit Codes](/aqdx-documentation/code-lookup-tables/unit-codes/)

### method_code

**Format:** String (3) &emsp;&emsp;
**Example:** `170` (Met One BAM-1020)

A 3-digit code associated with the reference method used to perform an EPA-designated FRM or FEM measurement.

- `Value Required` No
  - Regulatory Instruments (FRM/FEM): **Strongly Recommended.** If the instrument is an EPA Federal Reference Method (FRM), Federal Equivalent Method (FEM), or a Compendium Method, you should provide the specific 3-digit code defined by the EPA (e.g., `170` for BAM-1020).
  - Low-Cost Sensors / Non-Regulatory: Leave Blank. If the device is a low-cost sensor or has not been EPA-designated, leave this field blank.
- [View Method Codes](/aqdx-documentation/code-lookup-tables/method-codes/)

### duration

**Format:** Decimal (12,3) &emsp;&emsp;
**Example:** `3600` or `1.500`

The duration of the sampling period or mathematical aggregation window (see [`aggregation_code`](#aggregation_code) below) in seconds.

**General Guidelines**

- **Integers Preferred:** For standard intervals, use whole numbers without decimal padding (e.g., use `3600`, not `3600.000`).
- **Precision:** Fractional seconds are allowed up to milliseconds (3 digits after the decimal point) if high-precision timing is required.
- **Variable Duration:** If a sensor's physical sampling duration varies slightly row-to-row (e.g., fluctuating between 90 and 92 seconds), you should use a consistent, approximated nominal duration (e.g., `90`) for the entire dataset to reduce computational burden and make the data easier to query and compare.
- **Instantaneous / Unknown:** Use `0` to explicitly flag a measurement where the duration is near-instantaneous, highly inconsistent (sub-minute), or completely unknown. This specifically designates the data as coming from a low-cost sensor rather than a precision regulatory or research grade monitor.

For long-term aggregations (like months or years), **standard generalized timeframes are recommended** to maintain consistency across leap years and varying month lengths, unless the exact physical duration of a specific period is required.

**Common Duration Values:**

- `0` = Instantaneous / Unknown (Low-Cost Sensor flag)
- `60` = 1 Minute
- `3600` = 1 Hour
- `86400` = 1 Day (24 Hours)
- `604800` = 1 Week (7 Days)
- `2592000` = 1 Month (Standardized 30-Day Period)
- `31536000` = 1 Year (Standardized 365-Day Period)

### aggregation_code

**Format:** Integer (1) &emsp;&emsp;
**Example:** `1` (Mean)

Indicates the mathematical or physical method used to represent the data over the specified `duration`.

- `0`: **None / Native Resolution.** The data is reported at the instrument's native sampling frequency.
- `1`: **Mean (Average).** The mathematical average of measurements over the specified `duration`.
- `2`: **Time-Integrated (Physical).** A single physical sample accumulated over the `duration` (e.g., a 24-hour PM filter or VOC canister).
- `3`: **Maximum.** The highest single value recorded within the `duration`.
- `4`: **Median (50th Percentile).** The middle value of the measurements within the `duration`.
- `5`: **Rolling / Moving Average.** A mathematical average calculated over a moving window (e.g., an 8-hour rolling ozone average). Timestamp is assumed to be the beginning of the window unless specified in the metadata form.
- `6`: **Spatial Aggregation.** Data grouped by a geographic boundary rather than strictly by time (e.g., binning mobile data into 50-meter road segments).
  - Specific details of the method used must be documented in the accompanying AQDx metadata form.
  - For `duration`, report the total integration time (sum of durations) of all observations included in the spatial bin.
- `7`: **Other.** Any aggregation method not listed above, including specific statistical percentiles (e.g., 90th, 98th). Specific details of the method used must be documented in the accompanying AQDx metadata form.

## 2. Location

These fields define _where_ the measurement was taken.

| Field Name                  | Data Type     | Value Required | Description                         |
| :-------------------------- | :------------ | :------------- | :---------------------------------- |
| [**latitude**](#latitude)   | Decimal (9,5) | Conditional    | Latitude in WGS84 decimal degrees.  |
| [**longitude**](#longitude) | Decimal (9,5) | Conditional    | Longitude in WGS84 decimal degrees. |
| [**elevation**](#elevation) | Decimal (8,2) | No             | Elevation of the device in meters.  |

<br>

### latitude

**Format:** Decimal (9,5) &emsp;&emsp;
**Example:** `39.7392`

Latitude in decimal degrees (WGS84).

- **Positive:** North of the Equator.
- **Negative:** South of the Equator.
- **Precision:** Report to the 5th decimal point (~1 meter precision).
- **Conditional:** `latitude` is required except in the following circumstances:
  - **Mobile Monitoring Exception:** `latitude` may be left blank due to a temporary loss of GPS fix on a mobile platform, but you must include the `IG` (GPS invalid) code in the `qualifier_codes` field.

### longitude

**Format:** Decimal (9,5) &emsp;&emsp;
**Example:** `-104.9903`

Longitude in decimal degrees (WGS84).

- **Positive:** East of the Prime Meridian.
- **Negative:** West of the Prime Meridian (e.g., USA).
- **Precision:** Report to the 5th decimal point.
- **Conditional:** `longitude` is required except in the following circumstances:
  - **Mobile Monitoring Exception:** `longitude` may be left blank due to a temporary loss of GPS fix on a mobile platform, but you must include the `IG` (GPS invalid) code in the `qualifier_codes` field.

### elevation

**Format:** Decimal (8,2) &emsp;&emsp;
**Example:** `1609.3`

Elevation of the device in meters above mean sea level (MSL). Can be left blank.

---

## 3. Device & Organization

These fields define _who_ collected the data and _with what_ hardware.

| Field Name                                                      | Data Type    | Value Required | Description                                                       |
| :-------------------------------------------------------------- | :----------- | :------------- | :---------------------------------------------------------------- |
| [**data_steward_name**](#data_steward_name)                     | String (64)  | Yes            | The organization responsible for the data.                        |
| [**device_id**](#device_id)                                     | String (64)  | Yes            | An internal identifier used by the data steward.                  |
| [**measurement_technology_code**](#measurement_technology_code) | String (14)  | Yes            | categorizes the physical measurement technology of an instrument. |
| [**instrument_classification**](#instrument_classification)     | Integer (1)  | Yes            | Regulatory standing or operational tier of the instrument.        |
| [**dataset_id**](#dataset_id)                                   | String (128) | Yes            | Unique identifier to connect dataset to metadata form.            |

<br>

### data_steward_name

**Format:** String (64) &emsp;&emsp;
**Example:** `CityOfDenver` or `city_of_denver`

Name of the party responsible for data oversight.

- **Formatting:** Use PascalCase or snake_case to separate words.
- **Forbidden:** Do not use commas, spaces, or periods.

### device_id

**Format:** String (64) &emsp;&emsp;
**Example:** `A123-Sensor-01`

An internal identifier used by the data steward to uniquely distinguish this specific instrument within the dataset. Its primary purpose is to link the measurements in the data file to the instrument's details in the accompanying metadata form.

- **Internal Identification:** This is a localized text field to differentiate measurements. It is not intended to be a globally searchable, standardized hardware ID.
- **Recommended Convention:** We recommend using a combination of `[device model]-[ID#]-[sensor type or operating principle]`. The `ID#` can be an internal project number, a device serial number, or a device MAC address.
  - **Example:** `atmotube_pro_01_ls` (where "ls" stands for light scattering)
  - **Example:** `nodeA_macaddress_pms5003`
- **Other Valid Formats:** A simple hardware serial number, MAC address, or custom project ID (e.g., `Monitor_1`) are also acceptable.
- **Allowed Characters:** Spaces and hyphens.
- **Forbidden:** Do not use commas or periods.

### measurement_technology_code

**Format:** String (14) &emsp;&emsp;
**Examples:** `DA-00-SC`, `ICsu-GCca-MSpt`, `RS-00-OP`

A structured, hierarchical code that chronologically categorizes the physical journey of a sample from acquisition to the final signal.

- **Acquisition:** How the sample is acquired (e.g., in-situ, canister, remote sensing, etc.)
- **Conditioning:** The most significant physical or chemical treatment step applied to the sample (e.g., gas chromatography, de-humidification, thermal desorption, chemical ionization, etc.)
- **Detection:** The actual method of detection (e.g., mass spectrometry, PID sensor)

**Code Structure:** `[Acquisition]-[Conditioning]-[Detection]`
Each of the three steps requires a 2-character broad uppercase code (`XX`). You can optionally append two lowercase characters (`xx`) to designate a specific hardware subtype (e.g., `ICsu` for Integrated Canister, Summa). The blocks must be separated by hyphens.

**Key Rules:**

- **System Boundary:** The code describes the _end-to-end_ measurement system. For integrated or passive methods, it includes both the field acquisition AND the downstream laboratory analysis. Deep analytical nuances belong in the accompanying **AQDx Metadata Form (YAML)**.
- **The "00" Bright Line:** Use `00` for the Conditioning block ONLY if no intentional physical or chemical transformation occurred before the detector. If the system intentionally changes humidity, removes interferents, selects a size fraction, or chemically ionizes the sample, it is _not_ `00`.
- **Conditioning Priority:** If multiple conditioning steps exist, encode the one that most constrains what physically reaches the detector (e.g., a size cut or preconcentration) and document the rest in the YAML metadata form.

_Note: You must use approved vocabulary. Please refer to the [**Measurement Technology Codes Lookup Table**](/aqdx-documentation/code-lookup-tables/measurement-technology-codes/) in the code lookup tables to find the exact tokens permitted for your setup._

### instrument_classification

**Format:** Integer (1) &emsp;&emsp;
**Example:** `3`

Indicates the objective regulatory standing or operational tier of the instrument generating the data.

**Allowed Values:**

- `1` = **Regulatory Designated:** The instrument is operating under a formal, active designation from a recognized environmental authority (e.g., the US EPA) for the specific parameter being reported. _Note: If this code is used, the exact FRM/FEM designation should ideally be recorded in the `method_code` field if applicable._
- `2` = **Research-Grade Analytical Monitor:** High-fidelity instruments or methods that do not hold a formal regulatory designation but are widely accepted for rigorous scientific study. This includes advanced non-designated continuous monitors, as well as physical samples collected in the field and transported to a laboratory for discrete analytical analysis (e.g., GC/MS on canisters, XRF on filter tape).
- `3` = **Consumer-Grade Monitor:** Continuous monitors or indicative devices that actively measure ambient air but lack formal regulatory designation or research-grade analytical rigor. These devices are highly valuable for spatial mapping, identifying local trends, and supplemental public awareness.

### dataset_id

**Format:** String (128) &emsp;&emsp;
**Example:** `CDPHE_DowntownStation_20260213` or `123e4567-e89b-12d3-a456-426614174000`

A unique identifier that explicitly links this specific row of data to its corresponding AQDx dataset-level metadata file (e.g., `AQDx_metadata_form_v3.yaml`). This exact string must be present on every row of the tabular data file and must perfectly match the `dataset_id` field defined at the top of the accompanying metadata file.

- **Forbidden:** Do not use spaces, commas, or special characters other than hyphens (`-`), underscores (`_`), and periods (`.`).

To ensure global uniqueness across the AQDx ecosystem without relying on a central registry, data creators must generate this ID using one of the following three approved methods.

- **Method 1: Semantic Namespace (Recommended).** Create a self-documenting, human-readable string by combining your organization's metadata fields with high-resolution temporal or spatial identifiers.
  - _Formula:_ `[data_steward_name]_[project_or_device_id]_[YYYYMMDD]`
  - _Single Sensor Example:_ `CleanAirVision_A123-Sensor-01_20260213`
    - _note_: if you are submitting a dataset with multiple sensors, use project notation below.
  - _Network/Project Example:_ `CDPHE_WinterInversion_20260213`
- **Method 2: UUID v4.** Generate a standard Universally Unique Identifier. This is ideal for automated, programmatic data pipelines.
  - _Tooling:_ Specialists can generate these natively in Python (`import uuid; uuid.uuid4()`) or R (`uuid::UUIDgenerate()`).
  - _Web Generator:_ If generating manually, use a trusted standard generator such as <https://www.uuidgenerator.net/version4>.
  - _Example:_ `123e4567-e89b-12d3-a456-426614174000` **(do not use this uuid!)**
- **Method 3: External DOI / URI.** If the dataset is published to an academic or government repository (e.g., Zenodo, Dataverse), use its assigned permanent identifier (DOI) or record number.
  - _Example:_ `10.5281/zenodo.1234567`

---

## 4. Quality Control (QC)

These fields describe the quality and processing level of the data.

| Field Name                                  | Data Type      | Value Required | Description                                                                           |
| :------------------------------------------ | :------------- | :------------- | :------------------------------------------------------------------------------------ |
| [**validity_code**](#validity_code)         | Integer (1)    | Yes            | The assessed validity of the individual measurement.                                  |
| [**calibration_code**](#calibration_code)   | Integer (1)    | Yes            | Indicates whether the data has been corrected or calibrated against a known standard. |
| [**review_level_code**](#review_level_code) | Integer (1)    | Yes            | Indicates the level of human review the dataset has undergone.                        |
| [**detection_limit**](#detection_limit)     | Decimal (12,5) | No             | Detection limit for the method used to measure `parameter_value`.                     |
| [**qualifier_codes**](#qualifier_codes)     | String (254)   | No             | Space-separated codes explaining why data was flagged or describing specific events.  |

<br>

### validity_code

**Format:** Integer (1) &emsp;&emsp;
**Example:** `0` (Valid)

The assessed validity of the individual measurement. Validation extends beyond simple statistical outlier detection; it evaluates physical limits, hardware faults, "sticking" (unchanging) values, sensor degradation, and data completeness.

- `0`: **Validation not performed.** Raw data directly from the device. No QC checks have been applied to verify if a blank value is a true outage or a transmission error.
  - **Note:** Use this code for gaps in raw, real-time streams (`parameter_value` is blank) where no post-processing has occurred
- `1`: **Valid.** Data passed all QC checks and is considered accurate for analysis.
- `3`: **Estimated.** Data is considered valid, but the value was mathematically derived or interpolated rather than directly measured at this exact timestamp.
- `5`: **Suspect.** Data is physically possible but exhibits anomalous behavior (e.g., unexplained spikes, deviation from neighboring sensors, or operation during extreme weather). There is insufficient evidence to invalidate it entirely, but it should be used with caution.
- `8`: **QA/QC data.** Legitimate measurements taken during quality control procedures, such as zero/span checks, flow audits, or calibration events. While these values are "valid" representations of the instrument's response to a reference standard, they do not represent ambient air quality and **must be excluded** from environmental statistics (e.g., daily averages, AQI calculations).
- `9`: **Invalid or Missing.** Data that should not be used for analysis. Includes missing values (e.g., power failures, maintenance gaps, lost data), instrument malfunctions, failed range checks, or data failing completeness criteria (e.g., insufficient uptime for an hourly average).
  - If `parameter_value` is blank in a processed dataset, this code must be used.

### calibration_code

**Format:** Integer (1) &emsp;&emsp;
**Example:** `2` (Formally Verified)

Indicates the level of rigor and documentation of any post-processing corrections or calibrations applied by the Data Steward _after_ the data was output by the instrument. This field tracks human-applied adjustments to the `parameter_value`, distinct from any internal processing performed by the sensor firmware.

- `0`: **None / Factory Default.** The data is reported exactly as output by the device using the manufacturer's default factory calibration. No post-collection mathematical adjustments have been made.
- `1`: **Ad-Hoc / Project-Specific.** The data was mathematically adjusted using a custom, localized, or project-specific method. While the method may be highly effective for the specific project, it has not been formally vetted through a standardized regulatory or peer-review process.
- `2`: **Formally Verified (Math/Model).** The data was corrected using a robust, widely accepted methodology. To qualify for this code, the method must be explicitly documented in a Quality Assurance Project Plan (QAPP), derived from or available in a peer-reviewed scientific publication, or accepted for use by a government environmental agency (e.g., the US EPA's extended U.S.-wide correction for PurpleAir sensor data).
- `3`: **Physical Reference Standard.** The instrument was directly calibrated against a certified physical reference standard or secondary standard (e.g., physically adjusted using National Institute of Standards and Technology (NIST) traceable zero-air and span gas checks).

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
- This field should be left blank/omitted when a detection limit is unknown or not applicable.
- Please note the method used to determine the detection limit in the metadata form included with the submission.

### qualifier_codes

**Format:** String (254) &emsp;&emsp;
**Example:** `IM`

Space-separated codes explaining why data was flagged or describing specific events.

- **Examples:**
  - `IM` (Prescribed Fire)
  - `LJ` (High Winds)
  - `AA AG BG ND` (Multiple qualifier codes in one measurement)
  - ` ` (Can be blank)
- [View Qualifier Codes](/aqdx-documentation/code-lookup-tables/qualifier-codes/)
