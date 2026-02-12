# Version Changelog

This document tracks major changes to the AQDx standard, including updates to the metadata schema, file formats, and documentation structure.

## Version 3.0 (January 2025)

**Focus:** Machine Readability, Version Control, and Developer Experience.

### 1. Metadata Restructuring (Major Change)

The metadata submission process has been completely overhauled to support modern data engineering workflows.

- **Format Change:** Switched from **Excel (`.xlsx`)** to **YAML (`.yaml`)**.
  - _Why?_ YAML allows for nested structures (Instruments nested under Sites), is human-readable, and allows metadata to be tracked in version control systems like Git.
- **Schema Updates:**
  - **Nesting:** Instruments are no longer flat rows; they are now children of specific Site objects.
  - **Field Standardization:** Field names in the metadata now exactly match the field names in the data files (e.g., `data_steward_name` is consistent across both).
  - **Data Quality:** The "Quality Questionnaire" has been replaced by a structured `data_quality` object with boolean flags (`automated_qc`, `corrections`) and explicit description fields.

### 2. Documentation Architecture

- **Migration to MkDocs:** Documentation has moved from static **PDFs** to a live **ReadTheDocs** website generated from Markdown.
- **Searchability:** Users can now search for specific field definitions or error codes instantly across the entire standard.
- **Versioning:** Documentation is now versioned alongside the schema, allowing users to view guidance for previous versions if needed.

### 3. Data Format Enhancements

- **Parquet Support:** Added Apache Parquet (`.parquet`) as a supported format for high-volume, archival datasets.

---

## Version 2.0 (July 2024)
