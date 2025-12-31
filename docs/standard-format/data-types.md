# Data Types & Valid Values

This page defines the specific data formats used across the AQDx standard. Strict adherence to these types ensures data can be parsed correctly by any system, regardless of whether it is transmitted via CSV, Excel, or JSON.

## Core Data Types

| Data Type | Definition | Tabular Example | JSON Example |
| :--- | :--- | :--- | :--- |
| **String(n)** | Alphanumeric text with a maximum length of *n* characters. No commas allowed in CSV. | `PurpleAir` | `"PurpleAir"` |
| **Integer(n)** | Whole number with a maximum length of *n* digits. No decimals. | `44201` | `44201` |
| **Decimal** | A real number. Unless otherwise specified, use up to 5 decimal places of precision. | `45.231` | `45.231` |
| **ISO 8601** | Specific timestamp string format. See "Date & Time" below. | `2024-05-23...` | `"2024-05-23..."` |

## Date & Time (`datetime`)
All timestamps must follow the **ISO 8601** extended format.

*   **Format:** `YYYY-MM-DDThh:mm:ssTZD`
*   **Time Zone:** You must include a Time Zone Designator (TZD).
    *   **UTC:** Ends in `Z` or `+00:00`.
    *   **Offset:** `+hh:mm` or `-hh:mm` (e.g., `-07:00` for MST).
*   **Precision:** Seconds are required. Decimals for partial seconds (`ss.s`) are allowed but not required.
*   **24-Hour Clock:** Use `14:00`, not `2:00 PM`.

**Examples:**
*   ✅ `2024-05-23T14:30:00-07:00` (Local time with offset)
*   ✅ `2024-05-23T21:30:00Z` (UTC)
*   ❌ `2024-05-23 14:30:00` (Missing "T" and Time Zone)

## Null / Missing Values
How to represent missing data depends on the file format.

*   **Tabular (CSV):** Leave the field empty between commas.
    *   Example: `44201,,45.2` (Missing method code)
*   **Tabular (Excel):** Leave the cell empty.
*   **JSON:** Omit the key entirely OR use `null`.
    *   Preferred: `{"parameter": "44201", "value": 45.2}` (Key omitted)
    *   Allowed: `{"method_code": null}`

## Valid Value Lists
Certain fields restrict values to a specific code list.

### Quality Control Codes (`qc_code`)
Used to indicate the validity of a single measurement.

| Code | Meaning |
| :--- | :--- |
| **`0`** | **Valid.** Data is good. |
| **`1`** | **Estimated.** Data is valid but estimated (e.g., interpolated). |
| **`7`** | **Suspect.** Data looks weird but hasn't been proven invalid. |
| **`8`** | **Invalid.** Known bad data (e.g., instrument malfunction). |
| **`9`** | **Missing.** No value recorded. |

### Processing Levels (`review_level_code`)
Indicates the maturity of the dataset.

| Code | Meaning |
| :--- | :--- |
| **`0`** | **Raw.** Direct from device, no human review. |
| **`1`** | **Internal.** Reviewed by the data creator. |
| **`2`** | **External.** Audited by a third party. |
| **`3`** | **Certified.** Legally certified for regulatory use (rare). |

### Boolean Flags (`autoqc_check`, `corr_code`)
Simple flags for yes/no states.

| Code | Meaning |
| :--- | :--- |
| **`0`** | **No** / False |
| **`1`** | **Yes** / True |
