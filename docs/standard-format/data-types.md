# Data Types, Formats, and Conventions

This page defines the specific data formats used across the AQDx standard. Strict adherence to these types ensures data can be parsed correctly by any system, regardless of whether it is transmitted via CSV, Excel, or JSON.

## Core Data Types

| Data Type | Definition | Tabular CSV Example | JSON Example |
| :--- | :--- | :--- | :--- |
| [**String (n)**](#string-n)  | Alphanumeric or numeric only text with a maximum length of *n* characters. | `...,PurpleAir,...` <br> `...,008,...` | `{"device_manufacturer_name"="PurpleAir"}` <br> `{"unit_code":"008"}` |
| [**Integer (n)**](#integer-n) | Whole number with a maximum length of *n* digits. No decimals. | `...,1,...` | `{"autoqc_check":1}` |
| [**Decimal (p,s)**](#decimal-ps) | A fixed-point number with precision *p* and scale *s*. Example: (5,3)| `...,45.231,...` | `{"parameter_value":45.231}` |

<br>

### String (n)

**Format:** `String (n)`  
**Definition:** A text value with a maximum length of *n* characters. Strings may contain letters, digits, and selected punctuation as allowed by the field definition (see Field Dictionary).  

**Numeric string (important):** A “numeric string” is a String that consists only of digits `0–9` but MUST still be represented as a String because leading zeros are meaningful.  
- Example: unit codes like `008` must be transmitted/stored as `"008"` (a String) and not as `8` (an Integer), otherwise the code changes meaning.  

**Allowed**
- Any value whose character length is `<= n`.
- Digit-only values (numeric strings) such as `008`, `000`, `01234`, when the field definition requires a String (common for codes).

**Not allowed**
- Values longer than *n* characters.
- Automatically converting digit-only code strings into numbers (e.g., turning `008` into `8`).
- Using Strings to store true numeric measurements when the Field Dictionary specifies `Decimal (p,s)` (e.g., `value="45.2"` is not allowed when `value` is Decimal).

<br>

### Integer (n)

**Format:** `Integer (n)` &emsp;&emsp; 
**Definition:** A whole number with up to *n* digits. Integers do not have a decimal point.  

**Allowed**
- `0` through the maximum value representable with *n* digits (e.g., `Integer (1)` allows `0..9`).
- JSON numbers without decimals (e.g., `{"autoqc_check":1}`).

**Not allowed**
- Decimal points (e.g., `1.0`, `3.14`).
- Thousands separators or commas (e.g., `1,000`).
- Using Integer when the Field Dictionary defines a code as `String (n)` (for example, codes that may have leading zeros).

<br>

### Decimal (p, s)

**Format:** `Decimal (p, s)`  &emsp;&emsp;
**Definition:** A fixed-point decimal number with:

- **precision (p):** the total number of digits allowed (left + right of the decimal point, excluding sign and decimal point)
- **scale (s):** the number of digits to the right of the decimal point  

This is used for measured quantities and other numeric values where fractional values may occur (e.g., `value`, `lat`, `lon`, `duration`).  

**How to determine (p,s) (examples)**  
1. **If you know the maximum digits left of the decimal (m) and required fractional digits (s):**  
   - Then `p = m + s` and `Decimal (p,s)` allows up to `m` digits before the decimal and exactly/at-most `s` digits after (depending on implementation).  
   - Example: Want to allow up to `9999999.999` (7 digits left, 3 right) → `m=7`, `s=3`, so `p=10` → `Decimal (10,3)`.

2. **From a concrete maximum value and required decimal places:**  
   - Take the largest magnitude value you must support, count digits to the left of the decimal (m), choose required decimal places (s), then compute `p=m+s`.  
   - Example: Duration in seconds up to 24 hours with milliseconds: max `86400.000` → `m=5` (86400), `s=3` → `p=8` → `Decimal (8,3)`.

3. **Latitude/Longitude style constraints:**  
   - Latitude ranges `-90` to `90`. If AQDx requires 5 decimal places (meter-scale), max looks like `-90.00000`.  
   - Digits left of decimal for 90 is `2` (`90`), digits right `5`, so `p=2+5=7` → `Decimal (7,5)` would cover that numeric range; AQDx fields may specify a different `p` to accommodate formatting or consistency across systems (e.g., `Decimal (9,5)` in the Field Dictionary).  

4. **AQDx example from the Field Dictionary (`Decimal (12,5)`):**  
   - This allows up to `p-s = 7` digits left of the decimal and `5` digits right.  
   - So values up to `9999999.99999` (and corresponding negatives) fit within `Decimal (12,5)`.

**Allowed**
- Optional leading sign (`-`).
- Digits with an optional decimal point.
- Up to *s* digits to the right of the decimal point.
- No thousands separators (use `1500.0`, not `1,500.0`).

**Not allowed**
- More than *p* total digits (excluding sign and decimal point).
- More than *s* digits after the decimal point (must be rounded or truncated to conform).
- Commas or other digit grouping characters (e.g., `1,500.25`).
- Scientific notation (e.g., `1e-6`) unless explicitly allowed by a specific AQDx implementation profile (default AQDx expects plain fixed-point text/number representation).



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
    *   Preferred: `{"parameter": "44201", "parameter_value": 45.2}` (Key omitted)
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
