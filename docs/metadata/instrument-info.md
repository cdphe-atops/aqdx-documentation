# Instrument & Monitor Details

This section of the metadata defines the specific hardware or method used to generate the data. In the AQDx V3 YAML structure, `instruments` are listed as a list **nested under** the specific site where they are located.

If a site has multiple sensors (e.g., a particulate monitor and a weather station), each should be listed as a separate entry under that site.

## Field Summary

| Field Key                                                     | Data Type    | Required | Description                                       |
| :------------------------------------------------------------ | :----------- | :------- | :------------------------------------------------ |
| **[device_id](#device_id)**                                   | String (64)  | **Yes**  | Unique serial number of the device.               |
| **[manufacturer_name](#manufacturer_name)**                   | String (64)  | **Yes**  | Name of the device manufacturer.                  |
| **[parameter_code](#parameter_code)**                         | Integer (5)  | **Yes**  | AQS code for the parameter measured.              |
| **[method_code](#method_code)**                               | Integer (3)  | **Yes**  | AQS code for the measurement method.              |
| **[firmware_version](#firmware_version)**                     | String (32)  | No       | Version of the firmware running on the device.    |
| **[monitor_start_date](#monitor_start_date)**                 | Date (8)     | **Yes**  | Date monitoring began (YYYYMMDD).                 |
| **[probe_height_m](#probe_height_m)**                         | Decimal      | **Yes**  | Height of the inlet above ground (meters).        |
| **[monitoring_approach](#monitoring_approach)**               | Integer      | **Yes**  | Coded approach (e.g., Stationary, Mobile).        |
| **[monitoring_objective](#monitoring_objective)**             | Integer      | **Yes**  | Coded objective (e.g., Community, Ambient).       |
| **[expanded_objective](#expanded_objective)**                 | String (128) | **Yes**  | Brief text description of the goal.               |
| **[sampling_frequency_seconds](#sampling_frequency_seconds)** | Decimal      | **Yes**  | How often a sample is taken (seconds).            |
| **[residence_time_seconds](#residence_time_seconds)**         | Decimal      | No       | Time for sample to transfer from inlet to sensor. |
| **[airflow_arc_degrees](#airflow_arc_degrees)**               | Integer      | **Yes**  | Unrestricted airflow around the probe (0-360).    |
| **[instrument_photos_url](#instrument_photos_url)**           | String (200) | No       | Link to photos of the installation.               |
| **[dist_obstructions_m](#dist_obstructions_m)**               | Decimal      | **Yes**  | Distance to nearest obstruction (meters).         |

---

## Field Definitions

### device_id

**Format:** String (64)  
**Example:** `A123-Sensor-01`

The unique serial number or identifier of the device performing the measurement. This **must match** the `device_id` found in the data files (CSV/JSON).

### manufacturer_name

**Format:** String (64)  
**Example:** `PurpleAir`, `Teledyne`

The name of the manufacturer. Use TitleCase (PascalCase) to separate words. Do not use underscores or special characters.

### parameter_code

**Format:** Integer (5)  
**Example:** `88101` (PM2.5 Local Conditions)

The five-digit AQS numerical code identifying the parameter being measured. This must match the `parameter_code` in the data files.

### method_code

**Format:** Integer (3)  
**Example:** `000` (for generic sensors) or `170` (for BAM-1020)

The three-digit AQS numerical code identifying the method/technology used.

- **Sensors:** If no specific AQS method exists, use `000` or a supplemental AQDx code.
- **Regulatory:** Must use the specific FRM/FEM code from the AQS library.

### firmware_version

**Format:** String (32)  
**Example:** `6.02`

The version of the firmware installed on the device during the monitoring period. If the firmware changed, note the current version or the version used for the majority of the dataset.

### monitor_start_date

**Format:** String (YYYYMMDD)  
**Example:** `20240101`

The date on which this specific instrument began collecting data at this location.

### probe_height_m

**Format:** Decimal  
**Example:** `2.5`

The vertical distance from the ground to the instrument's inlet probe, measured in meters.

### monitoring_approach

**Format:** Integer  
**Example:** `1` (Stationary Continuous)

The basic operational approach of the monitoring. Select the integer code that applies:

1. **Stationary Continuous:** Fixed location, recording continuously.
2. **Stationary Integrated:** Fixed location, filter-based/integrated samples (e.g., 24-hour filter).
3. **Stationary Intermittent:** Fixed location, but does not run continuously.
4. **Mobile:** Moving platform (vehicle, bike).
5. **Wearable:** On a person.

### monitoring_objective

**Format:** Integer  
**Example:** `4` (Community)

The primary reason for the monitoring. Select the integer code that applies:

1. **Ambient:** General background air quality.
2. **Near-source:** Targeted at a specific emission source.
3. **Fenceline:** Boundary of a facility.
4. **Community:** Community-led or neighborhood-scale monitoring.
5. **Personal:** Exposure monitoring for an individual.
6. **Indoor:** Inside a building.
7. **Other/Mixed:** Objectives not listed above.

### expanded_objective

**Format:** String (128)  
**Example:** `Wildfire smoke impact study`

A short text description clarifying the specific goal. Examples: "Early warning system," "Trend analysis," "Baseline collection," or "School zone safety."

### sampling_frequency_seconds

**Format:** Decimal  
**Example:** `60` (1 minute)

The frequency at which the instrument takes a sample, in seconds.

- **1 Hour:** `3600`
- **1 Minute:** `60`
- **Instantaneous:** `1`

### airflow_arc_degrees

**Format:** Integer (0–360)  
**Example:** `360`

The number of degrees of unrestricted airflow around the probe inlet.

- **360:** Free-standing probe (unobstructed on all sides).
- **180:** Mounted directly against a wall.
- **90:** Mounted in a corner.

### dist_obstructions_m

**Format:** Decimal  
**Example:** `3.6`

The distance in meters from the inlet to the nearest obstruction (e.g., a wall, chimney, or sign) that is _not_ the roof surface itself. If there are no nearby obstructions, use `null` or a large value (e.g., `999`).

### dist_roof_obstructions_m

**Format:** Decimal  
**Example:** `2.0`

If the instrument is on a roof, the distance in meters to the nearest obstruction _on_ that roof.

---

## Regulatory Info (Conditional)

These fields are nested under `regulatory_info` in the YAML. They are **required** only if `is_regulatory_data` is set to `1` (Yes) in the Data Steward section.

| Field Key               | Type    | Description                                                         |
| :---------------------- | :------ | :------------------------------------------------------------------ |
| **monitor_type**        | String  | EPA Monitor Type (e.g., "SLAMS", "SPM", "Industrial").              |
| **method_type**         | String  | The designation (e.g., "FRM", "FEM", "ARM").                        |
| **network_affiliation** | String  | Network name (e.g., "CASTNET", "NCORE", "CSN").                     |
| **collecting_agency**   | String  | Name of the agency collecting the data.                             |
| **agency_code**         | Integer | AQS Agency Code (e.g., `0329`).                                     |
| **probe_material**      | String  | Material of the inlet (e.g., "Stainless Steel", "Teflon", "Glass"). |
