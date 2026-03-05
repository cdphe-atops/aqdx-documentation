# Air Quality Data Exchange (AQDx) Standard Format Guidance

Version 3.0 - February 2026

[Download the Full Specification (PDF)](pdf/document.pdf)

![Figure 1. Data exchange using AQDx between different organizations and agencies.](images/fig1_DataExchange.jpg)

_Figure 1. Data exchange using AQDx between different organizations and agencies._

## Introduction

Air monitoring is fundamentally changing. With new technology emerging, a wide range of organizations and individuals can now measure air pollution. Additionally, more organizations want to collect and aggregate these new datasets. With all these advances, the potential exists for organizations to integrate and harness these data to create transformative and systemic change. Many challenges exist for organizations collecting air quality data such as exchanging, integrating, harmonizing, and using these new data sources. There are too many data formats and ways to name parameters, little consistency in time formatting, various ways to indicate data quality, and more. This results in data that are more expensive to manage, harder to exchange, and not fully utilized. Universal methods are urgently needed for describing and exchanging data between organizations and their data management systems. Establishing standard parameter names, conventions for time reporting, and data quality levels will make it easier for organizations to collect and exchange data with many other organizations. Figure 1 shows how data exchange between organizations/systems needs a common format that describes the data, its collection, and its quality.

### Purpose and intended use

The Air Quality Data eXchange (AQDx) format is intended for:

- Enabling the exchange of air quality and weather data between organizations
- Exchanging of both historical and real-time data
- Establishing standardized naming conventions for parameters, units, etc.
- Documenting data so it is self-describing with location, device, organization, and quality levels
- Enabling open and public exchange of air quality data

## What is AQDx?

AQDx is not a piece of software, a database, or a specific file format. **It is a schema.**

By adhering to this schema, data becomes self-describing. Any person or software program that understands AQDx can instantly read, map, and visualize air quality data without needing to ask for the experimental specifics of an individual dataset.

### The Two Components of the Standard

AQDx splits information into two distinct files to handle different types of information efficiently. To ensure clarity across all documentation, we use the following controlled vocabulary:

1. **AQDx data (The Measurements)**
   Strict, structured files that hold the actual numbers, dates, and codes. Each record contains a single air quality measurement paired with a timestamp and location.
   - **AQDx datasheet:** Measurements formatted as a static table (e.g., CSV, Parquet).
   - **AQDx datastream:** Measurements formatted as a continuous flow (e.g., JSON).

2. **AQDx metadata (The Context)**
   The experiment-level details that accompany the data. This is a structured YAML document (typically generated from a 3-tab spreadsheet) that captures the "who, where, and how" such as project ownership, site configurations, and instrument QA/QC procedures.

### What AQDx Specifies

- **Identity:** Who collected the data (`data_steward_name`) and with what device (`device_id`).
- **Time:** When it happened, using strict ISO 8601 formatting to eliminate timezone confusion.
- **Location:** Where it happened (`latitude`, `longitude`).
- **Measurement:** What was found (`parameter_value`) and the unit used (`unit_code`).
- **Quality:** How reliable the data is (`validity_code`, `review_level_code`).

### What AQDx Does Not Specify

- **Storage Technology:** You can store AQDx data in SQL, NoSQL, data lakes, or simple spreadsheets. The schema is technology-agnostic.
- **File Size:** Whether you have ten rows of data or ten billion, the rules for naming your columns remain the same.

## Implementations

While the core AQDx schema is format-agnostic, we provide strict specifications for how to apply it to common file formats used in the real world:

- **Tabular (CSV, Excel, Parquet):** For historical data, bulk uploads, and archives.
- **JSON:** For real-time streaming, APIs, and web applications.

---

<small>The AQDx format was built upon the successful AirNow Air Quality Comma Separated Values (AQCSV) format. It is developed and maintained by the Colorado Department of Public Health and Environment (CDPHE) with input from the U.S. Environmental Protection Agency (EPA) and partners in the academic and community science sectors.
