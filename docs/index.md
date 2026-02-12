# Air Quality Data Exchange (AQDx) Standard Format Guidance

Version 3.0 - January 2026

[Download the Full Specification (PDF)](pdf/document.pdf)

![Figure 1. Data exchange using AQDx between different organizations and agencies.](images/fig1_DataExchange.jpg)

_Figure 1. Data exchange using AQDx between different organizations and agencies._

## Introduction

Air monitoring is fundamentally changing. With new technology emerging, a wide range of organizations and individuals can now measure air pollution. Additionally, more organizations want to collect and aggregate these new datasets. With all these advances, the potential exists for organizations to integrate and harness these data to create transformative and systemic change. Many challenges exist for organizations collecting air quality data such as exchanging, integrating, harmonizing, and using these new data sources. There are too many data formats and ways to name parameters, little consistency in time formatting, various ways to indicate data quality, and more. This results in data that are more expensive to manage, harder to exchange, and not fully utilized. Universal methods are urgently needed for describing and exchanging data between organizations and their data management systems. Establishing standard parameter names, conventions for time reporting, and data quality levels will make it easier for organizations to collect and exchange data with many other organizations. Figure 1 shows how data exchange between organizations/systems needs a common format that describes the data, its collection, and its quality.

### Purpose and intended use

The AQ Data Exchange (AQDx) format is intended for:

- Enabling the exchange of air quality and weather data between organizations
- Exchanging of real-time and recent data (last couple of days)
- Establishing common ways to name parameters, units, etc.
- Documenting data so it is self-describing with location, device, organization, and quality levels
- Enabling open and public exchange of air quality data

### What AQDx is (and is not intended for)

This data format is voluminous and meant for exchanging smaller amounts of data. It is not intended to exchange large amounts of data (e.g., 200 sites of hourly data for five years), nor is it meant to serve as an archive or data analysis format.

The remainder of this document describes all aspects of the Air Quality Data Exchange (AQDx) format. This format is made flexible to accommodate different types of monitoring, sampling methods, devices, and user groups. Much of the information is based on the extensive libraries provided by EPA’s Air Quality System (AQS). There are two versions of the format. The first is a Comma-Separated Value (CSV) version, which is a simple text record with comma delimiters (,) between each field. Each record contains one data value for a given device, time, and parameter. Other supporting fields in the record describe the units, measurement methods, location, and other information associated with the data value. Additional details about the data format are contained in this document. The second version is a JavaScript Object Notation (JSON) version. This version is intended to support real-time or streaming data. It includes all of the same parameters as the CSV version.

AQDx format was built upon the successful AirNow Air Quality Comma Separated Values (AQCSV) format and has been developed by the Colorado Department of Public Health and Environment (CDPHE) with input from the U.S. Environmental Protection Agency (EPA) and other industry, academic, and community-based organizations.
