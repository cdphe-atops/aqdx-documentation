# Glossary & Acronyms

This glossary defines common terms and acronyms used throughout the AQDx standard, particularly those derived from US EPA regulatory programs.

## Acronyms

| Acronym     | Definition                                                  | Context                                                                                                                                |
| :---------- | :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| **AQDx**    | **Air Quality Data Exchange**                               | The standard data format defined in this documentation.                                                                                |
| **AQCSV**   | **Air Quality Comma Separated Values**                      | The precursor format to AQDx, originally developed for the EPA's AirNow program.                                                       |
| **AQS**     | **Air Quality System**                                      | The EPA's repository of ambient air quality data. AQDx uses AQS codes for parameters and methods.                                      |
| **ARM**     | **Approved Regional Method**                                | A method for measuring PM2.5 that has been approved for use within a specific geographic area.                                         |
| **CASTNET** | **Clean Air Status and Trends Network**                     | A long-term monitoring network designed to assess trends in air quality and deposition.                                                |
| **CSN**     | **Chemical Speciation Network**                             | A network that monitors the chemical composition of PM2.5.                                                                             |
| **EPA**     | **Environmental Protection Agency**                         | The US federal agency responsible for protecting human health and the environment.                                                     |
| **FEM**     | **Federal Equivalent Method**                               | A monitoring method designated by the EPA as equivalent to a Federal Reference Method (FRM) for regulatory compliance.                 |
| **FRM**     | **Federal Reference Method**                                | The "gold standard" method for measuring a pollutant, as defined in the Code of Federal Regulations (CFR).                             |
| **IMPROVE** | **Interagency Monitoring of Protected Visual Environments** | A monitoring network established to protect visibility in Class I areas (national parks and wilderness areas).                         |
| **NAAQS**   | **National Ambient Air Quality Standards**                  | Limits on atmospheric concentration of six common pollutants ($O_3$, PM, CO, $SO_2$, $NO_2$, Pb) set by the EPA.                       |
| **NATTS**   | **National Air Toxics Trends Stations**                     | A network designed to provide long-term monitoring data for certain air toxics.                                                        |
| **NCore**   | **National Core Network**                                   | A multi-pollutant network that integrates several advanced measurement systems.                                                        |
| **PAMS**    | **Photochemical Assessment Monitoring Stations**            | Stations that monitor ozone precursors (volatile organic compounds, oxides of nitrogen) in serious ozone nonattainment areas.          |
| **QAPP**    | **Quality Assurance Project Plan**                          | A formal document describing in detail the necessary quality assurance, quality control, and other technical activities for a project. |
| **QC**      | **Quality Control**                                         | Operational techniques and activities used to fulfill requirements for quality (e.g., sticking checks, zero checks).                   |
| **SLAMS**   | **State or Local Air Monitoring Stations**                  | The primary network of monitoring stations used by state and local agencies for NAAQS compliance.                                      |
| **SPM**     | **Special Purpose Monitor**                                 | A monitor used for special studies or short-term objectives, often not strictly for regulatory compliance.                             |
| **STN**     | **Speciation Trends Network**                               | A component of the Chemical Speciation Network (CSN).                                                                                  |
| **UTC**     | **Coordinated Universal Time**                              | The primary time standard by which the world regulates clocks and time. AQDx requires time zone offsets relative to UTC.               |
| **WGS84**   | **World Geodetic System 1984**                              | The standard coordinate system for Earth, used by GPS. AQDx requires latitude/longitude in WGS84.                                      |

## Terminology

### Data Steward

The organization or individual responsible for the oversight, collection, processing, and distribution of the dataset. The Data Steward is the primary contact for any questions regarding the data.

### Method Code

A 3-digit integer from the AQS library that identifies the specific technology or analysis method used (e.g., `170` for a specific BAM-1020 setup). For low-cost sensors without a regulatory designation, this is often left blank or set to a generic code.

### Parameter Code

A 5-digit integer from the AQS library that identifies the pollutant or variable being measured (e.g., `44201` for Ozone, `88101` for PM2.5).

### Regulatory Data

Data collected with the specific intent of comparing it against National Ambient Air Quality Standards (NAAQS). This data must meet strict quality assurance requirements, typically using FRM or FEM instruments.

### ISO 8601

The international standard for date and time formatting. AQDx uses the extended format with time zone offsets: `YYYY-MM-DDThh:mm:ssTZD` (e.g., `2024-01-01T14:30:00-07:00`).
