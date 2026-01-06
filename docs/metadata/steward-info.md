# Data Steward Details

The **Data Steward** section appears at the very top of the AQDx metadata file. It serves two critical functions:

1.  **Accountability:** Identifies who is responsible for the data collection and processing.
2.  **Dataset Scope:** Defines the AQDx version, update frequency, and regulatory status for the entire file.

## Field Summary

| Field Key | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **[aqdx_metadata_version](#aqdx_metadata_version)** | String | **Yes** | Version of the metadata template used. |
| **[data_steward_name](#data_steward_name)** | String (64) | **Yes** | The party responsible for data oversight. |
| **[contact_name](#contact_name)** | String (64) | **Yes** | Primary individual contact. |
| **[contact_email](#contact_email)** | String (64) | **Yes** | Primary contact email. |
| **[contact_phone](#contact_phone)** | String | No | Primary contact phone number. |
| **[organization_type](#organization_type)** | Integer | **Yes** | Coded type of organization (e.g., Gov, Academic). |
| **[organization_name_full](#organization_name_full)** | String (128) | **Yes** | Full legal name of the organization. |
| **[address](#address)** | String (128) | No | Organization's physical or mailing address. |
| **[last_update_date](#last_update_date)** | Date (8) | **Yes** | Date the metadata was last modified (YYYYMMDD). |
| **[aqdx_data_version](#aqdx_data_version)** | String | **Yes** | AQDx Standard version of the data files (e.g., "3.0"). |
| **[is_regulatory_data](#is_regulatory_data)** | Integer (0/1) | **Yes** | Flag indicating if data is for regulatory compliance. |
| **[data_abstract](#data_abstract)** | String (500) | No | Brief summary of the project goals. |

---

## Field Definitions

### aqdx_metadata_version
**Format:** String  
**Example:** `3.0`

The version of the AQDx Metadata Form schema being used. This ensures software parsers know which fields to expect.

### data_steward_name
**Format:** String (64)  
**Example:** `CleanAirVision`, `CDPHE`

The short-code or ID of the party responsible for the data.
*   **Important:** This string must **exactly match** the `data_steward_name` field found in every row of your AQDx data files (CSV/JSON).
*   **Style:** Use PascalCase or snake_case. Avoid spaces or special characters.

### contact_name
**Format:** String (64)  
**Example:** `Jane Doe`

The name of the individual who can answer questions regarding the dataset. This may be the Principal Investigator (PI), the technical lead, or a project manager.

### contact_email
**Format:** String (64)  
**Example:** `jane.doe@example.org`

The best email address for reaching the contact person.

### contact_phone
**Format:** String  
**Example:** `(001)(303) 555-0100`

The phone number that may be called regarding data oversight.
*   **Format:** `(CCC)(AAA) NXX-XXXX`
    *   `CCC` = Country Code (e.g., 001 for USA)
    *   `AAA` = Area Code
    *   `NXX-XXXX` = Local Number
*   **Privacy Note:** Since metadata files are often public, consider using an office line or a project-specific Google Voice number rather than a personal cell phone.


### organization_type
**Format:** Integer  
**Example:** `3` (Community-Based Organization)

A numerical code representing the type of organization managing the data.
1.  **Government**
2.  **Non-Governmental Organization (NGO)**
3.  **Community-Based Organization (CBO)**
4.  **Research/Academic Institution**
5.  **Industry**
6.  **Consulting**
7.  **Education** (e.g., public school, library)
8.  **Other**

### organization_name_full
**Format:** String (128)  
**Example:** `Colorado Department of Public Health and Environment`

The full, human-readable name of the organization. Unlike `data_steward_name`, this field may contain spaces and commas.

### address
**Format:** String (128)  
**Example:** `4300 Cherry Creek S Dr, Denver, CO 80246`

The mailing address for the organization. This is optional but recommended for formal data exchanges.

### last_update_date
**Format:** String (YYYYMMDD)  
**Example:** `20260105`

The date on which this metadata file was last edited. This helps data users determine if they are looking at the most recent site/instrument configuration.

### aqdx_data_version
**Format:** String  
**Example:** `3.0`

The version of the AQDx Data Standard used to format the actual measurement files (CSV/JSON).

### is_regulatory_data
**Format:** Integer (0 or 1)  
**Example:** `0` (No)

Indicates whether the dataset is collected for regulatory compliance purposes (e.g., NAAQS comparison).
*   `0`: **No.** (Community science, research, informational monitoring).
*   `1`: **Yes.** (Data collected following strict EPA requirements).
    *   **Note:** Setting this to `1` triggers additional required fields in the Site and Instrument sections (e.g., AQS IDs, Method Codes).

### data_abstract
**Format:** String (500)  
**Example:** `This dataset provides daily PM2.5 concentrations for the Berkeley neighborhood to study seasonal changes.`

A short paragraph describing the project. This is the place to include context that does not fit into specific fields, such as the hypothesis being tested, specific events captured (e.g., "captured the 2024 wildfire season"), or funding source