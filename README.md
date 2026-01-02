# Air Quality Data Exchange (AQDx) Standard

[![Documentation Status](https://readthedocs.org/projects/aqdx/badge/?version=latest)](https://aqdx.readthedocs.io/en/latest/?badge=latest)

**The standard for exchanging air quality and weather data.**

Air monitoring is fundamentally changing. With the emergence of new technologies, diverse organizations—from state agencies to community groups—are collecting vast amounts of air quality data. The **Air Quality Data Exchange (AQDx)** standard provides a universal language to harmonize, exchange, and aggregate these disparate datasets.

## Documentation

The full technical specification and user guides are hosted on ReadTheDocs:
👉 **[https://aqdx.readthedocs.io](https://aqdx.readthedocs.io)**

### Quick Links
*   **[Core Data Types](https://aqdx.readthedocs.io/en/latest/standard-format/data-types/)** – String, Integer, Decimal, and Date formats.
*   **[Field Dictionary](https://aqdx.readthedocs.io/en/latest/standard-format/field-dictionary/)** – Definitions for `parameter_code`, `device_id`, and more.
*   **[Tabular Format (CSV)](https://aqdx.readthedocs.io/en/latest/standard-format/tabular-format/)** – Structure for batch and historical data.
*   **[JSON Streaming](https://aqdx.readthedocs.io/en/latest/standard-format/json-format/)** – Structure for real-time data transmission.

## Purpose

AQDx aims to solve the "data silo" problem in air quality monitoring by providing:
1.  **Standardized Parameter Naming:** Consistent codes for pollutants (e.g., `44201` for Ozone).
2.  **Metadata Included:** Communicate experiment level info to describe datasets in the metadata form.
3.  **Data Quality Indicators:** Clear flags for QC status, processing levels, and data validity.
4.  **Flexible Formats:** Support for both bulk uploads (CSV) and real-time streams (JSON).
5.  **Unified Time Reporting:** Strict ISO 8601 formatting to eliminate timezone confusion.


## 🤝 Contributing

We welcome contributions from the air quality community! Whether you are a data steward, software developer, sensor manufacturor, or researcher, your feedback helps improve the AQDx standard.

### How to Contribute

 **Report Issues:**
    *   Found a typo, ambiguity, or error in the documentation?
    *   Have a question about how to map a specific parameter?
    *   👉 **[Open an Issue](https://github.com/your-org/aqdx/issues)** to start the discussion.

---
Developed by the Colorado Department of Public Health and Environment (CDPHE) Air Pollution Control Division with input from the U.S. EPA and community partners.
