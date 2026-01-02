# Data Types, Formats, and Conventions

This page defines the specific data formats used across the AQDx standard. Strict adherence to these types ensures data can be parsed correctly by any system, regardless of whether it is transmitted via CSV, Excel, or JSON.

## Core Data Types

| Data Type | Definition | Tabular Example | JSON Example |
| :--- | :--- | :--- | :--- |
| **String (n)** | Alphanumeric or numeric only text with a maximum length of *n* characters. | `...,PurpleAir,...` <br> `...,008,...` | `{"device_manufacturer_name"="PurpleAir"}` <br> `{"unit_code":"008"}` |
| **Integer (n)** | Whole number with a maximum length of *n* digits. No decimals. | `...,1,...` | `{"autoqc_check":1}` |
| **Decimal (p,s)** | A fixed-point number with precision *p* and scale *s*. Example: (5,3)| `...,45.231,...` | `{"value":45.231}` |


## Data Formats & Conventions
### Date & Time (`datetime`)
All timestamps are stored as Strings but must follow the **ISO 8601** extended format.

*   **Format:** `YYYY-MM-DDThh:mm:ssTZD`
*   **Time Zone:** You must include a Time Zone Designator (TZD).
    *   **UTC:** Ends in `Z` or `+00:00`.
    *   **Offset:** `+hh:mm` or `-hh:mm` (e.g., `-07:00` for MST).
*   **Precision:** Seconds are required. Decimals for partial seconds (`ss.sss`) are allowed up to milliseconds but not required.
*   **24-Hour Clock:** Use `14:00`, not `2:00 PM`.

**Examples:**

*   ✅ `2024-05-23T14:30:00-07:00` (Local time with offset)
*   ❌ `2024-05-23T21:30:00Z` (UTC using "Z" notation is not allowed)
*   ❌ `2024-05-23 14:30:00` (Missing "T" and Time Zone)

### Null / Missing Values
How to represent missing data depends on the file format. Do not use empty string `""` or fill values such as `-999`.

*   **Tabular (CSV):** Leave the field empty between commas.
    *   Allowed: `44201,,45.2` (Missing method code)
*   **Tabular (Excel):** Leave the cell empty.
*   **JSON:** Omit the key entirely OR use `null`.
    *   Preferred: `{"parameter": "44201", "value": 45.2}` (Key omitted)
    *   Allowed: `{"method_code": null}`
    *   Not Allowed: `{"method_code": ""}` (Empty strings are not nulls)

### Quotation Marks
Strict adherence to quotation rules ensures compatibility across parsers.

*   **Double Quotes (`"`)**
    *   **JSON:** **Required.** All keys and string values *must* be wrapped in standard double quotes (e.g., `{"parameter": "44201"}`).
    *   **CSV:** **Allowed.** Use standard double quotes to enclose fields if necessary.
*   **Single Quotes (`'`)**
    *   **Not Allowed.** Do not use single quotes to wrap strings or keys in either format.
*   **Smart / Curly Quotes (`“` `”`)**
*   **Not Allowed.** These characters (often auto-formatted by text editors like Word) will cause parsing errors. Always use standard "straight" Double Quotes.
