# Site & Location Details

In the AQDx metadata structure, a **Site** represents the physical location where monitoring takes place. A single Site may contain multiple **Instruments** (e.g., a PM2.5 sensor and a wind sensor at the same location).

In the YAML file, the `sites` key accepts a list of site entries. If your project spans multiple locations, you will copy and paste the entire site block for each new location.

## Field Summary

| Field Key | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **[site_name](#site_name)** | String (64) | **Yes** | Human-readable name of the site. |
| **[latitude](#latitude)** | Decimal | **Yes** | Latitude in decimal degrees. |
| **[longitude](#longitude)** | Decimal | **Yes** | Longitude in decimal degrees. |
| **[gis_datum](#gis_datum)** | String (10) | **Yes** | Coordinate datum (default: "WGS84"). |
| **[address](#address)** | String (128) | No | Physical address of the site. |
| **[state_code](#state_code)** | Integer (2) | **Yes** | AQS State Code. |
| **[county_code](#county_code)** | Integer (3) | **Yes** | AQS County Code. |
| **[site_owner](#site_owner)** | String (128) | **Yes** | Owner of the site/property. |
| **[site_photos_url](#site_photos_url)** | String (200) | No | Link to photos of the site context. |
| **[surroundings_type](#surroundings_type)** | Integer | **Yes** | Coded description of land use (e.g., Urban). |
| **[nearby_sources](#nearby_sources)** | String (200) | No | Text description of pollution sources. |

---

## Field Definitions

### site_name
**Format:** String (64)  
**Example:** `Downtown Station`, `Smith Residence`

The human-readable name of the site. This should match the name used in reports, newsletters, or publications.

### latitude
**Format:** Decimal  
**Example:** `39.74204`

Latitude in decimal degrees. Positive values are North of the Equator; negative values are South. Report to at least 5 decimal places (~1 meter precision) where possible.

### longitude
**Format:** Decimal  
**Example:** `-104.99153`

Longitude in decimal degrees. Positive values are East of the Prime Meridian; negative values are West (e.g., US longitudes are negative).

### gis_datum
**Format:** String (10)  
**Default:** `WGS84`

The coordinate system used for the latitude and longitude. AQDx expects `WGS84`.

### address
**Format:** String (128)  
**Example:** `4300 Cherry Creek S Dr, Denver, CO`

If the site has a physical mailing address or is located at a specific facility, enter it here. Otherwise, leave as `null`.

### state_code
**Format:** Integer (2)  
**Example:** `08` (Colorado)

The two-digit Federal Information Processing Standards (FIPS) code for the state.
*   [Lookup EPA State Codes](https://aqs.epa.gov/aqsweb/documents/codetables/states.html)

### county_code
**Format:** Integer (3)  
**Example:** `031` (Denver County)

The three-digit FIPS code for the county.
*   [Lookup EPA County Codes](https://aqs.epa.gov/aqsweb/documents/codetables/counties.html)

### site_owner
**Format:** String (128)  
**Example:** `Jane Doe`, `City of Denver`

The name of the person or organization that owns the property where the monitor is located. If it is a private home, you may list "Private Residence" if privacy is a concern, though specific ownership is preferred for QA tracking.

### site_photos_url
**Format:** String (200)  
**Example:** `https://example.com/photos/site1`

A publicly accessible URL linking to photos of the site. Photos should show the surroundings (N, S, E, W) to help data users understand potential local influences (e.g., trees, buildings, roads).

### surroundings_type
**Format:** Integer  
**Example:** `1` (Urban)

A numerical code describing the primary land use surrounding the site. Select the integer that best fits:

1.  **Urban**
2.  **Suburban**
3.  **Rural**
4.  **Industrial**
5.  **Residential**
6.  **Agricultural**
7.  **Natural**
8.  **Recreational**
9.  **Waterfront**
10. **Mixed-use**
11. **Other**

### nearby_sources
**Format:** String (200)  
**Example:** `Wastewater treatment plant ~500m North; Highway I-25 ~1km East`

A free-text description of major pollution sources that might affect measurements. Examples include roadways, factories, dry cleaners, or frequent barbecues.

---

## Regulatory Info (Conditional)

These fields are nested under `regulatory_info` in the YAML. They are **required** only if `is_regulatory_data` is set to `1` (Yes) in the Data Steward section.

| Field Key | Type | Description |
| :--- | :--- | :--- |
| **aqs_id** | Integer (9) | The unique 9-digit AQS monitoring location code. |
| **[monitoring_scale](#monitoring_scale)** | Integer | Coded spatial scale of representativeness. |
| **[site_type](#site_type)** | Integer | Coded general monitoring objective. |
| **[groundcover](#groundcover)** | Integer | Coded surface material under the site. |

### monitoring_scale
**Format:** Integer  
**Example:** `3` (Neighborhood)

The spatial scale for which the concentrations are expected to be similar.
1.  **Micro** (Several meters - e.g., street canyon)
2.  **Middle** (100 m to 0.5 km)
3.  **Neighborhood** (0.5 to 4 km)
4.  **Urban** (4 to 50 km)
5.  **Regional** (Tens to hundreds of km)
6.  **National**
7.  **Global**

### site_type
**Format:** Integer  
**Example:** `2` (Population Oriented)

The primary reason for monitoring at this specific location (Regulatory objective).
1.  **Highest Concentration**
2.  **Population Oriented**
3.  **Source Impact**
4.  **General/Background & Regional Transport**
5.  **Welfare-Related Impacts**
6.  **Other**

### groundcover
**Format:** Integer  
**Example:** `1` (Grass)

The dominant material covering the ground beneath the monitoring site.
1.  **Grass**
2.  **Shrub**
3.  **Trees**
4.  **Flowers**
5.  **Moss**
6.  **Groundcovers** (generic)
7.  **Mulch**
8.  **Rocks**
9.  **Sand**
10. **Gravel**
11. **Pavement**
12. **Bare Soil**
13. **Water**
14. **Other**
