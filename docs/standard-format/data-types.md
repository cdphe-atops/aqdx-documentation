# Data Types & Conventions

This page defines the specific data formats used across the AQDx standard. Strict adherence to these types ensures data can be parsed correctly by any system, regardless of whether it is transmitted via CSV, Excel, or JSON.

## Core Data Types

| Data Type                         | Definition                                                                 | Tabular CSV Example                    | JSON Example                                                          |
| :-------------------------------- | :------------------------------------------------------------------------- | :------------------------------------- | :-------------------------------------------------------------------- |
| [**String (n)**](#string-n)       | Alphanumeric or numeric only text with a maximum length of _n_ characters. | `...,PurpleAir,...` <br> `...,008,...` | `{"device_manufacturer_name"="PurpleAir"}` <br> `{"unit_code":"008"}` |
| [**Integer (n)**](#integer-n)     | Whole number with a maximum length of _n_ digits. No decimals.             | `...,1,...`                            | `{"aggregation_code":1}`                                              |
| [**Decimal (p,s)**](#decimal-p-s) | A fixed-point number with precision _p_ and scale _s_. Example: (5,3)      | `...,45.231,...`                       | `{"parameter_value":45.231}`                                          |

<br>

### String (n)

**Format:** `String (n)` &emsp;&emsp;
**Definition:** A text value with a maximum length of _n_ characters.

**Numeric string:** A “numeric string” is a String that consists only of digits `0–9` but MUST still be represented as a String because leading zeros are meaningful.

- Example: unit codes like `008` must be transmitted/stored as `"008"` (a String) and not as `8` (an Integer), otherwise the code changes meaning.

**Allowed**

- Any value whose character length is `<= n`.
- Digit-only values (numeric strings) such as `008`, `000`, `01234`, when the field definition requires a String (common for codes).

**Not allowed**

- Values longer than _n_ characters.
- Automatically converting digit-only code strings into numbers (e.g., turning `008` into `8`).
- Using Strings to store true numeric measurements when the Field Dictionary specifies `Decimal (p,s)` (e.g., `value="45.2"` is not allowed when `value` is Decimal).

<br>

### Integer (n)

**Format:** `Integer (n)` &emsp;&emsp;
**Definition:** Zero or a positive whole number with up to _n_ digits. Integers do not have a decimal point.

**Note on Codes:** Fields defined as `Integer (1)` (like `validity_code`) are categorical flags. Even though they look like numbers (0, 1, 2), they must be treated as exact integers. `1.0` is not a valid status code; `1` is.

**Allowed**

- `0` through the maximum value representable with _n_ digits (e.g., `Integer (1)` allows `0..9`).
- JSON numbers without decimals (e.g., `{"aggregation_code":1}`).

**Not allowed**

- Decimal points (e.g., `1.0`, `3.14`).
- Thousands separators or commas (e.g., `1,000`).
- Using Integer when the Field Dictionary defines a code as `String (n)` (for example, codes that may have leading zeros).

<br>

### Decimal (p, s)

**Format:** `Decimal (p, s)` &emsp;&emsp;
**Definition:** A fixed-point number where:

- **p (precision):** The total number of digits allowed (left + right of the decimal).
- **s (scale):** The number of digits allowed to the right of the decimal.

This type is used for all measured quantities (e.g., `parameter_value`, `latitude`, `duration`).

#### Checking your Data against Decimal (p, s)

The notation `Decimal (p, s)` defines the exact space available for your number. To ensure your data fits, perform these two checks:

**1. The "Left Side" Check (Magnitude)**
Ensure your number isn't too large. The maximum number of digits allowed to the _left_ of the decimal point is **`p - s`**.

- **Example:** For `Decimal (8, 3)`, you have `8 - 3 = 5` allowed digits to the left.
  - _Fits:_ `12345.123` (5 digits left).
  - _Too Large:_ `123456.123` (6 digits left).

**2. The "Right Side" Check (Precision)**
Ensure your number isn't too precise. The `s` value defines the maximum number of digits allowed to the _right_ of the decimal point.

- **Rule:** If your instrument reports more decimal places than `s`, you must round the value.
- **Example:** For `Decimal (12, 5)`, if you have `45.123456`:
  - _Action:_ Round to the 5th decimal place.
  - _Result:_ Submit `45.12346`.

**Common AQDx Scenarios:**

- **Coordinates (`Decimal (9, 5)`):**
  - _Left Side:_ `9 - 5 = 4` digits allowed. This comfortably fits Longitude (e.g., `-180` uses 3 digits).
  - _Right Side:_ Round long GPS decimals (e.g., `-105.1234567`) to 5 places (`-105.12346`).
- **Measurements (`Decimal (12, 5)`):**
  - _Left Side:_ `12 - 5 = 7` digits allowed. This fits values up to `9,999,999`.
  - _Right Side:_ Round high-precision sensor readings to 5 decimal places.

#### Syntax & Formatting Rules

- **No Commas:** Never use thousands separators (e.g., use `1500.0`, not `1,500.0`).
- **No Scientific Notation:** Use plain fixed-point notation (e.g., use `0.00015`, not `1.5e-4`).
- **Optional Signs:** A negative sign (`-`) is allowed and does _not_ count toward precision (`p`).
- **Optional Decimal Point:** Whole numbers are valid (e.g., `85` is accepted as `85.0`).

## Data Formats & Conventions

### Date & Time (`datetime`)

All timestamps are stored as Strings but must follow the **ISO 8601** extended format.

- **Format:** `YYYY-MM-DDThh:mm:ssTZD`
- **Time Zone:** You must include a Time Zone Designator (TZD).
  - **UTC:** Ends in `+00:00`. "Z" Notation is not allowed.
  - **Offset:** `+hh:mm` or `-hh:mm` (e.g., `-07:00` for MST).
    - Note: Unlike AQS, local standard time is not a requirement (daylight time may be used), but you must use the correct TZD
- **Precision:** Seconds are required. Decimals for partial seconds (`ss.sss`) are allowed up to milliseconds but not required.
- **24-Hour Clock:** Use `14:00`, not `2:00 PM`.

**Examples:**

- ✅ `2024-05-23T14:30:00-07:00` (Local time with offset)
- ✅ `2024-05-23T14:30:00.343-07:00` (Local time with offset - up to milliseconds are allowed)
- ❌ `2024-05-23T21:30:00Z` (UTC using "Z" notation is not allowed - use `2024-05-23T21:30:00+00:00` instead)
- ❌ `2024-05-23 14:30:00` (Missing "T" and Time Zone)

### Required vs. Optional Fields ("Can be blank?")

The Field Dictionary specifies whether a field **"Can be blank?"**. This rule dictates whether a valid value is required for the record to be accepted.

#### 1. Required Fields (`Can be blank? : No`)

These fields define the core identity of the record (e.g., `datetime`, `device_id`, `dataset_id`).

- **Tabular (CSV):** The cell **must** contain a value. It cannot be empty between commas.
- **JSON:** The key **must** exist, and the value **cannot** be `null`.

#### 2. Optional Fields (`Can be blank? : Yes`)

These fields provide extra context that may not always be available (e.g., `method_code` for low-cost sensors, or `elevation`).

- **Tabular (CSV):** The column header **must still exist**. Do not delete the column. Leave the cell completely empty between the commas.
  - _Correct:_ `44201,,45.2`
  - _Incorrect:_ `44201,NA,45.2` (See "Forbidden Placeholders" below)
- **JSON:** You may omit the key entirely, or send the key with a `null` value.
  - _Preferred:_ `{"parameter": "44201", "value": 45.2}` (Key omitted)
  - _Allowed:_ `{"method_code": null}`

#### Forbidden Placeholders (Null Values)

Air quality researchers often use specific codes to indicate missing data. **Do not use these in AQDx.** The only valid representation of a missing value is an empty cell (CSV) or `null` (JSON).

| Format            | ❌ **Invalid (Do Not Use)**            | ✅ **Valid** |
| :---------------- | :------------------------------------- | :----------- |
| **Text**          | `"NA"`, `"N/A"`, `"null"`, `"Missing"` | ` ` (Empty)  |
| **Numeric**       | `-999`, `-9999`, `NaN`                 | ` ` (Empty)  |
| **Empty Strings** | `""`, `" "`                            | ` ` (Empty)  |

### Quotation Marks

Strict adherence to quotation rules ensures compatibility across parsers.

- **Double Quotes (`"`)**
  - **JSON:** **Required.** All keys and string values _must_ be wrapped in standard double quotes (e.g., `{"parameter": "44201"}`).
    - Note that numeric values do not need quotes `{"parameter_value": 0.00232}`
  - **CSV:** **Allowed.** Use standard double quotes to enclose fields if necessary.
- **Single Quotes (`'`)**
  - **Not Allowed.** Do not use single quotes to wrap strings or keys in either format.
- **Smart / Curly Quotes (`“` `”`)**
  - **Not Allowed.** These characters (often auto-formatted by text editors like Word) will cause parsing errors. Always use standard "straight" Double Quotes.
