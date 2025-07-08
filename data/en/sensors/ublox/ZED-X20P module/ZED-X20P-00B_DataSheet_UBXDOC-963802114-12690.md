

# **ZED-X20P-00B**

### **All-band high precision GNSS module Professional grade**

**Data sheet**



#### **Abstract**

This data sheet describes the ZED-X20P high precision module with all-band GNSS receiver. The module provides all-band RTK with fast convergence times, reliable performance and easy integration of RTK for fast time-to-market. It has a high update rate for highly dynamic applications and centimeter-level accuracy in a small and energy-efficient module.



### <span id="page-1-0"></span>**Document information**

| Title                  | ZED-X20P-00B                        |             |
|------------------------|-------------------------------------|-------------|
| Subtitle               | All-band high precision GNSS module |             |
| Document type          | Data sheet                          |             |
| Document number        | UBXDOC-963802114-12690              |             |
| Revision and date      | R03                                 | 23-May-2025 |
| Disclosure restriction | C1-Public                           |             |

| Product status                   | Corresponding content status |                                                                                           |
|----------------------------------|------------------------------|-------------------------------------------------------------------------------------------|
| Functional sample                | Draft                        | For functional testing. Revised and supplementary data will be published<br>later.        |
| In development /<br>prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                    |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be<br>published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be<br>published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                        |

This document applies to the following products:

| Product name | Type number     | FW version | IN/PCN reference | Product status     |
|--------------|-----------------|------------|------------------|--------------------|
| ZED-X20P     | ZED-X20P-00B-00 | HPG 2.00   | N/A              | Engineering sample |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents and product statuses, visit www.u-blox.com.

Copyright © 2025, u-blox AG.



<span id="page-2-0"></span>

| Document<br>information                                           | 2  |
|-------------------------------------------------------------------|----|
| Contents3                                                         |    |
| 1 Functional<br>description                                       | 4  |
| 1.1 Overview 4                                                    |    |
| 1.2 Performance 4                                                 |    |
| 1.3 Supported GNSS constellations5                                |    |
| 1.4 Supported assisted GNSS (A-GNSS) services6                    |    |
| 1.5 Supported augmentation systems 6                              |    |
| 1.6 Differential GNSS (DGNSS)7                                    |    |
| 1.7 Supported protocols8<br>1.8 Firmware features8                |    |
| 1.9 Broadcast navigation data and satellite signal measurements 8 |    |
| 1.9.1 Carrier-phase measurements9                                 |    |
| 2 Block<br>diagram10                                              |    |
| 3 Pin<br>definition11                                             |    |
| 3.1 Pin assignment11                                              |    |
| 3.2 Pin state13                                                   |    |
| 4 Electrical<br>specifications14                                  |    |
| 4.1 Absolute maximum ratings14                                    |    |
| 4.2 Operating conditions14                                        |    |
| 4.3 Indicative power requirements15                               |    |
| 5 Communications<br>interfaces16                                  |    |
| 5.1 UART16                                                        |    |
| 5.2 SPI 16                                                        |    |
| 5.3 I2C 18                                                        |    |
| 5.4 Default interface settings19                                  |    |
| 6 Mechanical specifications21                                     |    |
| 7 Qualifications<br>and<br>approvals23                            |    |
| 8 Packaging24                                                     |    |
| 8.1 Reels 24                                                      |    |
| 8.2 Tapes 24                                                      |    |
| 9 Soldering25                                                     |    |
| 10 Product<br>marking<br>and<br>ordering<br>information26         |    |
| 10.1 Product marking26                                            |    |
| 10.2 Product identifiers26                                        |    |
| 10.3 Ordering codes27                                             |    |
| Related<br>documents                                              | 28 |
| Revision<br>history29                                             |    |
| Contact30                                                         |    |



### <span id="page-3-0"></span>**1 Functional description**

#### <span id="page-3-1"></span>**1.1 Overview**

ZED-X20P is an innovative all-band receiver module designed to revolutionize positioning technology in industrial applications. Built upon the u-blox new generation receiver platform, this module offers multi-band Global Navigation Satellite System (GNSS) capability, supporting bands including L1, L2, L5 and L6. With its comprehensive coverage, ZED-X20P ensures precise and reliable positioning even in challenging environments, setting a new standard in accuracy.

Equipped with integrated u-blox multi-band real-time kinematic (RTK) and precise point positioning real-time kinematic (PPP-RTK) technologies, ZED-X20P achieves centimeter-level accuracy, enabling precise navigation and automation in industrial and consumer-grade products. Despite its advanced capabilities, ZED-X20P maintains a compact surface-mounted form factor, measuring only 17.0 x 22.0 x 2.4 mm, ensuring seamless integration into various applications without compromising performance.

In this document, RTK refers to an observation state representation (OSR) based solution utilizing radio technical commission for maritime services (RTCM) corrections, while PPP-RTK refers to state space representation (SSR) based solution using secure position augmentation for realtime navigation (SPARTN). With its comprehensive features and advanced technologies, ZED-X20P offers unparalleled accuracy and reliability, making it the ideal choice for applications requiring highperformance positioning solutions.

| Parameter                        | Specification | Value                                 |
|----------------------------------|---------------|---------------------------------------|
| Receiver type                    |               | All-band high precision GNSS receiver |
| Accuracy of time pulse signal    | RMS           | 20 ns                                 |
|                                  | 99%           | 60 ns                                 |
| Frequency of time pulse signal   |               | Default 1PPS                          |
|                                  |               | (0.25 Hz to 10 MHz configurable)      |
| 1<br>Operational limits          | Dynamics      | ≤ 4 g                                 |
|                                  | Altitude      | 80,000 m                              |
|                                  | Velocity      | 500 m/s                               |
| 2<br>Velocity accuracy           |               | 0.05 m/s                              |
| 2<br>Dynamic heading accuracy    |               | 0.3 deg                               |
| Table 1: ZED-X20P specifications |               |                                       |

#### <span id="page-3-2"></span>**1.2 Performance**

| GNSS             |                  | GPS+GAL+BDS |  |
|------------------|------------------|-------------|--|
| 3<br>Acquisition | Cold start       | 25 s        |  |
|                  | Hot start        | 2 s         |  |
|                  | 4<br>Aided start | 2 s         |  |

<span id="page-3-3"></span><sup>1</sup> Assuming Airborne 4 g platform.

<span id="page-3-4"></span><sup>2</sup> 50% at 30 m/s for dynamic operation.

<span id="page-3-5"></span><sup>3</sup> Commanded starts. All satellites at -130 dBm. Measured at room temperature. All band operation

<span id="page-3-6"></span><sup>4</sup> Dependent on the speed and latency of the aiding data connection, commanded starts



| GNSS                                      |                   | GPS+GAL+BDS |
|-------------------------------------------|-------------------|-------------|
| 5<br>Max navigation update rate           | RTK               | 25 Hz       |
|                                           | PVT               | 25 Hz       |
|                                           | RAW               | 25 Hz       |
| 6<br>Convergence time                     | RTK               | < 7 s       |
| Table 2: ZED-X20P performance             |                   |             |
| GNSS                                      |                   | GPS+GAL+BDS |
| Horizontal position accuracy (CEP)        | PVT7              | 1.2 m       |
|                                           | 7<br>SBAS         | 0.6 m       |
|                                           | 8                 | 0.006 m     |
|                                           | RTK               | + 1 ppm     |
| Vertical position accuracy (Median)       | PVT7              | 2.0 m       |
|                                           | 7<br>SBAS         | 1.0 m       |
|                                           | 8<br>RTK          | 0.01 m      |
|                                           |                   | + 1 ppm     |
| Table 3: ZED-X20P position accuracy       |                   |             |
| GNSS                                      |                   | GPS+GAL+BDS |
| Horizontal position accuracy (CEP)        | 9<br>SPARTN       | < 0.06 m    |
| Vertical position accuracy (Median)       | 9<br>SPARTN       | < 0.10 m    |
| 6<br>Convergence time                     | 9<br>SPARTN       | < 40 s      |
| Table 4: ZED-X20P performance for PPP-RTK |                   |             |
| GNSS                                      |                   | GPS+GAL+BDS |
| 10<br>Sensitivity                         | Tracking and nav. | -167 dBm    |
|                                           | Reacquisition     | -160 dBm    |
|                                           | Cold start        | -148 dBm    |
|                                           | Hot start         | -158 dBm    |

**Table 5: ZED-X20P sensitivity**

#### <span id="page-4-0"></span>**1.3 Supported GNSS constellations**

ZED-X20P is a concurrent GNSS receiver that can receive and track multiple GNSS constellations. Owing to the multi-band radio frequency (RF) front-end architecture, all major GNSS constellations (Global Positioning System (GPS), Galileo and BeiDou Navigation Satellite System (BDS)) plus Satellite-Based Augmentation System (SBAS), Quasi-Zenith Satellite System (QZSS), and Navigation with Indian Constellation (NavIC) satellites can be received concurrently on L1, L2 , L5 and L6 bands.

If power consumption is a key factor, the receiver can be configured for a subset of GNSS constellations.

<span id="page-4-1"></span><sup>5</sup> Measured with primary output only, secondary output disabled (default)

<span id="page-4-2"></span><sup>6</sup> Depends on atmospheric conditions, baseline length, GNSS antenna, multipath conditions, satellite visibility and geometry

<span id="page-4-3"></span><sup>7</sup> 24 hours static

<span id="page-4-4"></span><sup>8</sup> Measured using 1 km baseline and patch antennas with good ground planes. Does not account for possible antenna phase center offset errors. The ppm limited to baselines up to 20 km.

<span id="page-4-5"></span><sup>9</sup> PointPerfect Flex correction service based on the SPARTN format

<span id="page-4-6"></span><sup>10</sup> Demonstrated with a good external LNA. Measured at room temperature.



All satellites in view can be processed to provide an RTK navigation solution when used with correction data.

To benefit from multi-band signal reception, dedicated hardware preparation must be made during the design-in phase. The default configuration on ZED-X20P is concurrent reception of GPS, Galileo and BeiDou with QZSS and SBAS enabled.

| System  | Signal            | Frequency    |
|---------|-------------------|--------------|
| GPS     | L1C/A             | 1575.420 MHz |
|         | L2C               | 1227.600 MHz |
|         | L5                | 1176.450 MHz |
| Galileo | E1-B/C            | 1575.420 MHz |
|         | E5a               | 1176.450 MHz |
|         | E6                | 1278.750 MHz |
| BeiDou  | B1I               | 1561.098 MHz |
|         | B1C               | 1575.420 MHz |
|         | B2a               | 1176.450 MHz |
|         | B3I               | 1268.520 MHz |
| QZSS    | L1C/A, L1C/B11    | 1575.420 MHz |
|         | L2C               | 1227.600 MHz |
|         | L5                | 1176.450 MHz |
| NavIC   | 11<br>L1-SPS Data | 1575.420 MHz |
|         | L5-SPS            | 1176.450 MHz |

ZED-X20P supports the following GNSS constellations and their signals:

**Table 6: Supported GNSS constellations and signals on ZED-X20P**

#### <span id="page-5-0"></span>**1.4 Supported assisted GNSS (A-GNSS) services**

ZED-X20P supports the following GNSS assistance services:

| Service           | Signal     |
|-------------------|------------|
| AssistNow™ Online | GPS L1C/A  |
|                   | Galileo E1 |
|                   | QZSS L1C/A |
|                   | BeiDou B1I |

**Table 7: Supported assisted GNSS (A-GNSS) services**

#### <span id="page-5-1"></span>**1.5 Supported augmentation systems**

ZED-X20P supports the following augmentation systems:

| System | Signal           |
|--------|------------------|
| SBAS   | EGNOS            |
|        | GAGAN            |
|        | MSAS             |
|        | WAAS             |
|        | 11, 12<br>BDSBAS |

**Table 8: Supported augmentation systems**

<span id="page-5-2"></span><sup>11</sup> Currently in development phase.

<span id="page-5-3"></span><sup>12</sup> BDSBAS is not operational and is in the test phase.



The SBAS augmentation system can be enabled only if GPS operation is also enabled.

#### <span id="page-6-0"></span>**1.6 Differential GNSS (DGNSS)**

When operating in Real time kinematic (RTK) mode, RTCM version 3 messages are required and the module supports DGNSS according to RTCM 10403.4.

Operating as a rover, ZED-X20P can decode the following RTCM 3.4 messages:

| Message type | Description                                              |
|--------------|----------------------------------------------------------|
| RTCM 1001    | L1-only GPS RTK observables                              |
| RTCM 1002    | Extended L1-only GPS RTK observables                     |
| RTCM 1003    | L1/L2 GPS RTK observables                                |
| RTCM 1004    | Extended L1/L2 GPS RTK observables                       |
| RTCM 1005    | Stationary RTK reference station ARP                     |
| RTCM 1006    | Stationary RTK reference station ARP with antenna height |
| RTCM 1007    | Antenna descriptor                                       |
| RTCM 1033    | Receiver and antenna description                         |
| RTCM 1074    | GPS MSM4                                                 |
| RTCM 1075    | GPS MSM5                                                 |
| RTCM 1077    | GPS MSM7                                                 |
| RTCM 1094    | Galileo MSM4                                             |
| RTCM 1095    | Galileo MSM5                                             |
| RTCM 1097    | Galileo MSM7                                             |
| RTCM 1124    | BeiDou MSM4                                              |
| RTCM 1125    | BeiDou MSM5                                              |
| RTCM 1127    | BeiDou MSM7                                              |

**Table 9: Supported RTCM 3.4 input messages**

Operating as a base station, ZED-X20P can generate the following RTCM 3.4 output messages:

| Message type | Description                          |
|--------------|--------------------------------------|
| RTCM 1005    | Stationary RTK reference station ARP |
| RTCM 1074    | GPS MSM4                             |
| RTCM 1077    | GPS MSM7                             |
| RTCM 1094    | Galileo MSM4                         |
| RTCM 1097    | Galileo MSM7                         |
| RTCM 1124    | BeiDou MSM4                          |
| RTCM 1127    | BeiDou MSM7                          |

**Table 10: Supported RTCM 3.4 output messages**

Operating as a rover, ZED-X20P can decode the following SPARTN 2.0.2 messages:

| Message type-subtype | Description                                         |
|----------------------|-----------------------------------------------------|
| SM 0-0               | GPS orbit, clock, bias (OCB)                        |
| SM 0-2               | Galileo orbit, clock, bias (OCB)                    |
| SM 0-3               | BeiDou orbit, clock, bias (OCB)                     |
| SM 1-0               | GPS high-precision atmosphere correction (HPAC)     |
| SM 1-2               | Galileo high-precision atmosphere correction (HPAC) |
| SM 1-3               | BeiDou high-precision atmosphere correction (HPAC)  |



| Message type-subtype | Description                      |
|----------------------|----------------------------------|
| SM 2-0               | Geographic area definition (GAD) |

**Table 11: Supported SPARTN version 2.0.2 input messages**

#### <span id="page-7-0"></span>**1.7 Supported protocols**

ZED-X20P supports the following protocols:

| Type                                     |
|------------------------------------------|
| Input/output, binary, u-blox proprietary |
| Input/output, ASCII                      |
| Input/output, binary                     |
| Input, binary                            |
|                                          |

**Table 12: Supported protocols**

For specification of the protocols, see the Interface description [[2](#page-27-1)].

#### <span id="page-7-1"></span>**1.8 Firmware features**

| Feature                                | Description                                                                                                   |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 13<br>Antenna supervisor               | Antenna supervisor for active antenna control and short circuit detection                                     |
| RAW data                               | Provides carrier and code phase measurements of tracked signals                                               |
| Assisted GNSS                          | AssistNow Online                                                                                              |
| RTK support                            | High-precision positioning                                                                                    |
| Local base functionality               | Base station functionality with RTCM output                                                                   |
| Spectrum analyzer                      | Monitors RF environment for possible interference and anomalies                                               |
| Geofencing                             | Supports location-restriction and anti-theft functionality                                                    |
| Monitoring and management<br>functions | Extensive functions to monitor embedded system health such as I/O queues, pin<br>status and correction status |
| Personalization                        | Individualized identity to access high value features and subscriptions                                       |
| Backup modes                           | Hardware and software                                                                                         |
| Table 13: Firmware features            |                                                                                                               |

| Feature                    | Description                                                    |
|----------------------------|----------------------------------------------------------------|
| Anti-jamming               | RF interference and jamming detection and reporting            |
| Anti-spoofing              | Spoofing detection and reporting                               |
| Galileo OSNMA              | Galileo Open Service Navigation Message Authentication         |
| Configuration lockdown     | Receiver configuration can be locked by command                |
| Secure boot                | Only signed firmware images are executed                       |
| Secure storage             | Tamper-resistant secure storage with end-to-end security       |
| Navigation data validation | According to the DHS GPS Receiver Allow List Development Guide |

**Table 14: Security features**

### <span id="page-7-2"></span>**1.9 Broadcast navigation data and satellite signal measurements**

ZED-X20P uses UBX-RXM-SFRBX message to output all the GNSS broadcast data upon reception from tracked satellites. This includes all the supported GNSS signals as well as the QZSS and

<span id="page-7-3"></span><sup>13</sup> External components required, some pins need to be reconfigured.



SBAS augmentation services. See the Interface description[\[2](#page-27-1)] for the UBX-RXM-SFRBX message specification. The receiver can provide satellite signal information in a form compatible with the Radio Resource LCS Protocol (RRLP).

#### <span id="page-8-0"></span>**1.9.1 Carrier-phase measurements**

ZED-X20P provides raw carrier-phase data for all supported signals, along with pseudorange, Doppler and measurement quality information. The data contained in the UBX-RXM-RAWX message follows the conventions of a multi-GNSS RINEX3 observationfile. For the UBX-RXM-RAWX message specification, see Interface description[\[2\]](#page-27-1).

Raw measurement data is available once the receiver has established data bit synchronization and time-of-week.

UBXDOC-963802114-12690 - R03 1 Functional description Page 9 of 30 C1-Public



### <span id="page-9-0"></span>**2 Block diagram**



**Figure 1: ZED-X20P block diagram**





## <span id="page-10-0"></span>**3 Pin definition**

#### <span id="page-10-1"></span>**3.1 Pin assignment**

The pin assignment of the ZED-X20P module is shown in [Figure](#page-10-2) 2. The defined configuration of the programmable input/outputs (PIOs) is listed in [Table](#page-10-3) 15.

<span id="page-10-2"></span>

#### **Figure 2: ZED-X20P pin assignment**

<span id="page-10-3"></span>

| Pin no. | Name        | I/O | Description                                      |
|---------|-------------|-----|--------------------------------------------------|
| 1       | GND         | -   | Ground                                           |
| 2       | RF_IN       | I   | RF input                                         |
| 3       | GND         | -   | Ground                                           |
| 4       | ANT_DETECT  | I   | Active antenna detect - default active high      |
| 5       | ANT_OFF     | O   | External LNA disable - default active high       |
| 6       | ANT_SHORT_N | I   | Active antenna short detect - default active low |
| 7       | VCC_RF      | O   | Voltage for external LNA                         |
| 8       | Reserved    | -   | Reserved                                         |
| 9       | Reserved    | -   | Reserved                                         |
| 10      | Reserved    | -   | Reserved                                         |



| Pin no. | Name           | I/O | Description                                                              |
|---------|----------------|-----|--------------------------------------------------------------------------|
| 11      | Reserved       | -   | Reserved                                                                 |
| 12      | GND            | -   | Ground                                                                   |
| 13      | Reserved       | -   | Reserved                                                                 |
| 14      | GND            | -   | Ground                                                                   |
| 15      | Reserved       | -   | Reserved                                                                 |
| 16      | Reserved       | -   | Reserved                                                                 |
| 17      | Reserved       | -   | Reserved                                                                 |
| 18      | Reserved       | -   | Reserved                                                                 |
| 19      | GEOFENCE_STAT  | O   | Geofence status, user defined                                            |
| 20      | RTK_STAT       | O   | RTK status:                                                              |
|         |                |     | 0 = RTK/PPP-RTK fixed                                                    |
|         |                |     | blinking = receiving and using corrections                               |
|         |                |     | 1 = no corrections                                                       |
| 21      | Reserved       | -   | Reserved                                                                 |
| 22      | Reserved       | -   | Reserved                                                                 |
| 23      | Reserved       | -   | Reserved                                                                 |
| 24      | Reserved       | -   | Reserved                                                                 |
| 25      | Reserved       | -   | Reserved                                                                 |
| 26      | RXD2           | I   | UART2 input                                                              |
| 27      | TXD2           | O   | UART2 output                                                             |
| 28      | Reserved       | -   | Reserved                                                                 |
| 29      | Reserved       | -   | Reserved                                                                 |
| 30      | Reserved       | -   | Reserved                                                                 |
| 31      | Reserved       | -   | Reserved                                                                 |
| 32      | GND            | -   | Ground                                                                   |
| 33      | VCC            | I   | Voltage supply                                                           |
| 34      | VCC            | I   | Voltage supply                                                           |
| 35      | Reserved       | -   | Reserved                                                                 |
| 36      | V_BCKP         | I   | Backup supply voltage                                                    |
| 37      | GND            | -   | Ground                                                                   |
| 38      | Reserved       | -   | Connect to Ground                                                        |
| 39      | Reserved       | -   | Leave Open                                                               |
| 40      | Reserved       | -   | Leave Open                                                               |
| 41      | GND            | -   | Ground                                                                   |
| 42      | TXD / SPI_SDO  | O   | UART1 output if D_SEL = 1(or open). SPI_SDO if D_SEL = 0                 |
| 43      | RXD / SPI_SDI  | I   | UART1 input if D_SEL = 1(or open). SPI_SDI if D_SEL = 0                  |
| 44      | SDA / SPI_CS_N | I/O | I2C Data if D_SEL = 1 (or open). SPI Chip Select if D_SEL = 0            |
| 45      | SCL / SPI_CLK  | I/O | I2C Clock if D_SEL = 1(or open). SPI Clock if D_SEL = 0                  |
| 46      | TX_READY       | O   | TX_Buffer full and ready for TX of data                                  |
| 47      | D_SEL          | I   | Interface select for pins 42-45                                          |
| 48      | GND            | -   | Ground                                                                   |
| 49      | RESET_N        | I   | RESET_N                                                                  |
| 50      | SAFEBOOT_N     | I   | SAFEBOOT_N (for future service, updates and reconfiguration, leave OPEN) |
| 51      | EXTINT         | I   | External interrupt pin                                                   |



|           | I/O | Description |
|-----------|-----|-------------|
| Reserved  | -   | Reserved    |
| TIMEPULSE | O   | Time pulse  |
| Reserved  | -   | Reserved    |
|           |     |             |

**Table 15: ZED-X20P pin assignment**

#### <span id="page-12-0"></span>**3.2 Pin state**

[Table](#page-12-1) 16 defines the state of the PIOs and RESET\_N pins in different modes. The functions of the PIOs are as defined in the default configuration.

<span id="page-12-1"></span>

| D_SEL = open | Input pull-up          |                 |                        |
|--------------|------------------------|-----------------|------------------------|
|              |                        | Input pull-up   | Input pull-up          |
| D_SEL = GND  | High-Z                 | Input pull-down | High-Z                 |
| RXD          | Input pull-up          | Input pull-up   | Input pull-up          |
| SPI_SDO      | High-Z                 | Input pull-up   | Input pull-up          |
| TXD          | Output                 | Input pull-up   | Output                 |
| SPI_SDI      | 14<br>Output           | Input pull-up   | 14<br>Output           |
| SDA          | Input pull-up / Output | Input pull-up   | Input pull-up / Output |
| SPI_CS_N     | High-Z                 | High-Z          | High-Z                 |
| SCL          | Input pull-up          | Input pull-up   | Input pull-up          |
| SPI_SLK      | High-Z                 | High-Z          | High-Z                 |
| TIMEPULSE    | Output                 | Input pull-up   | Output low             |
| SAFEBOOT_N   | Input pull-up          | Input pull-up   | Input pull-up          |
| EXTINT       | Input pull-up          | Input pull-up   | Input pull-up          |
| RXD2         | Input pull-up          | Input pull-up   | Input pull-up          |
| TXD2         | Output                 | Input pull-up   | Output                 |
| RESET_N      | Input pull-up          | Input pull-up   | Input pull-up          |
|              |                        |                 |                        |

#### **Table 16: Pins state**

- In reset mode (RESET\_N = low), all PIOs are configured as input pull-up.
- In hardware backup mode (VCC = 0 V), PIOs must not be driven.

<span id="page-12-2"></span><sup>14</sup> If SPI CS = low. Otherwise it is configured as an input pull-up.



### <span id="page-13-0"></span>**4 Electrical specifications**

#### <span id="page-13-1"></span>**4.1 Absolute maximum ratings**

- CAUTION. Risk of device damage. Exceeding the absolute maximum ratings may affect the lifetime and reliability of the device or permanently damage it. Do not exceed the absolute maximum ratings.
- CAUTION. This product is not protected against overvoltage or reversed voltages. Use appropriate protection to avoid device damage from voltage spikes exceeding the specified boundaries.

| Symbol | Condition                                   | Min  | Max       | Units |
|--------|---------------------------------------------|------|-----------|-------|
| VCC    |                                             | -0.5 | 3.6       | V     |
|        |                                             | 20   | 8000      | µs/V  |
| V_BCKP |                                             | -0.5 | 3.6       | V     |
|        |                                             | 20   |           | µs/V  |
| Vin    | VCC ≤ 3.1 V                                 | -0.5 | VCC + 0.5 | V     |
|        | VCC > 3.1 V                                 | -0.5 | 3.6       | V     |
| ICC_RF |                                             |      | 300       | mA    |
| Prfin  | source impedance =<br>50 Ω, continuous wave |      | 10        | dBm   |
| Tstg   |                                             | -40  | +85       | °C    |
|        |                                             |      |           |       |

**Table 17: Absolute maximum ratings**

#### <span id="page-13-2"></span>**4.2 Operating conditions**

Extreme operating temperatures can significantly impact the specified values. If an application operates near the min or max temperature limits, ensure the specified values are not exceeded.

| Parameter                                                   | Symbol   | Condition    | Min       | Typical | Max | Units |
|-------------------------------------------------------------|----------|--------------|-----------|---------|-----|-------|
| Power supply voltage                                        | VCC      |              | 2.7       | 3.0     | 3.6 | V     |
| Backup battery voltage                                      | V_BCKP   |              | 1.65      |         | 3.6 | V     |
| 16, 17<br>Backup battery current                            | I_BCKP   |              |           | 32      |     | µA    |
| SW backup current                                           | I_SWBCKP |              |           | 93      |     | µA    |
| Input pin voltage range                                     | Vin      |              | 0         |         | VCC | V     |
| Digital IO pin low level input voltage                      | Vil      |              |           |         | 0.4 | V     |
| Digital IO pin high level input voltage                     | Vih      |              | 0.8 * VCC |         |     | V     |
| Digital IO pin low level output voltage                     | Vol      | Iol = 2 mA18 |           |         | 0.4 | V     |
| Digital IO pin high level output voltage                    | Voh      | Ioh = 2 mA18 | VCC – 0.4 |         |     | V     |
| DC current through any digital I/O pin<br>(except supplies) | Ipin     |              |           |         | 5   | mA    |
| Pull-down resistors on GPIOs                                | Rpd      |              | 34        | 62      | 142 | kΩ    |

<span id="page-13-3"></span><sup>15</sup> Exceeding the ramp speed may permanently damage the device

<span id="page-13-4"></span><sup>16</sup> To measure the I\_BCKP the receiver should first be switched on, i.e. VCC and V\_BCKP is available. Then set VCC to 0 V while the V\_BCKP remains available. Afterward measure the current consumption at the V\_BCKP.

<span id="page-13-5"></span><sup>17</sup> The value has been characterized at 25 °C ambient temperature.

<span id="page-13-6"></span><sup>18</sup> TIMEPULSE has 4 mA current drive/sink capability



| Parameter                                             | Symbol   | Condition                     | Min | Typical   | Max  | Units |
|-------------------------------------------------------|----------|-------------------------------|-----|-----------|------|-------|
| Pull-up resistance for SCL, SDA, EXTINT Rpu           |          |                               | 8   | 16        | 40   | kΩ    |
| Pull-up resistance for D_SEL, RXD, TXD,<br>SAFEBOOT_N | Rpu      |                               | 35  | 67        | 205  | kΩ    |
| Pull-up resistance for RESET_N                        | Rpu      |                               | 7   | 10        | 13   | kΩ    |
| VCC_RF voltage                                        | VCC_RF   |                               |     | VCC – 0.1 |      | V     |
| VCC_RF output current                                 | ICC_RF   |                               |     |           | 50   | mA    |
| Input impedance at RF_IN                              | Zin      |                               |     | 50        |      | Ω     |
| Receiver chain noise figure (L1\B1\E1)                | NFtot    |                               |     | 6.5       |      | dB    |
| Receiver chain noise figure (L2)                      | NFtot    |                               |     | 6         |      | dB    |
| Receiver chain noise figure (L5\E5a\B2a) NFtot        |          |                               |     | 5         |      | dB    |
| External gain (at RF_IN)                              | Ext_gain | Normal gain mode<br>(default) | 17  |           | 40   | dB    |
| External gain (at RF_IN)                              | Ext_gain | Low gain mode                 | 20  |           | 50   | dB    |
| Operating temperature                                 | Topr     |                               | –40 | +25       | +105 | °C    |

**Table 18: Operating conditions**

#### <span id="page-14-0"></span>**4.3 Indicative power requirements**

[Table](#page-14-1) 19 provides examples of typical current requirements. The given values are total system supply current for a possible application including RF and baseband sections. The values have been measured at 25 °C ambient temperature.

The actual power requirements vary depending on the firmware (FW) version used, external circuitry, number of satellites tracked, signal strength, type and time of start, duration, and conditions of test.

<span id="page-14-1"></span>

| Symbol | Parameter    | Conditions  | GPS+GAL<br>+BDS | GPS | Unit |
|--------|--------------|-------------|-----------------|-----|------|
| IPEAK  | Peak current | Acquisition | 80              | 70  | mA   |
| IVCC   | VCC current  | Acquisition | 68              | 55  | mA   |
| IVCC   | VCC current  | Tracking    | 64              | 55  | mA   |

**Table 19: Currents to calculate the indicative power requirements**



## <span id="page-15-0"></span>**5 Communications interfaces**

The ZED-X20P receiver support communication over UART, SPI and I2C.

All the inputs have internal pull-up resistors in normal operation and can be left open if not used. All the PIOs are supplied by V\_IO, therefore all the voltage levels of the PIO pins are related to V\_IO supply voltage.

#### <span id="page-15-1"></span>**5.1 UART**

The UART interfaces support configurable baud rates. Hardware flow control is not supported.

The UART1 is enabled if **D\_SEL** pin of the module is left open or "high".

| Symbol | Parameter              | Min   | Max     | Unit  |
|--------|------------------------|-------|---------|-------|
| Ru     | Baud rate              | 4800  | 8000000 | bit/s |
| ΔTx    | Tx baud rate accuracy  | -1%   | +1%     | -     |
| ΔRx    | Rx baud rate tolerance | -2.5% | +2.5%   | -     |

**Table 20: ZED-X20P UART specifications**

#### <span id="page-15-2"></span>**5.2 SPI**

The SPI interface is disabled by default. The SPI interface shares pins with UART1 and I2C and can be selected by setting **D\_SEL** = 0. The SPI interface can be operated in peripheral mode only. The SPI transfer rate based on load capacitance is shown in [Table](#page-15-3) 21.

<span id="page-15-3"></span>

| Load capacitance (pF) | Min transfer rate (kB/s) | Max transfer rate (kB/s) | Max clock frequency (MHz) |
|-----------------------|--------------------------|--------------------------|---------------------------|
| 2                     | 880                      | 950                      | 12.80                     |
| 20                    | 770                      | 920                      | 10.20                     |
| 60                    | 620                      | 880                      | 7.25                      |

**Table 21: SPI transfer rate based on load capacitance for ZED-X20P**

The SPI timing parameters for peripheral operation are defined in [Figure](#page-16-0) 3. Default SPI configuration is CPOL = 0 and CPHA = 0.



<span id="page-16-0"></span>



| Symbol | Parameter                                               | Min | Max | Unit |
|--------|---------------------------------------------------------|-----|-----|------|
| 1      | CS deassertion hold time                                | 8   | -   | ns   |
| 2      | Chip select time (CS to SCK)                            | 11  | -   | ns   |
| 3      | SCK rise/fall time                                      | -   | 5   | ns   |
| 4      | SCK high time                                           | 39  | -   | ns   |
| 5      | SCK low time                                            | 39  | -   | ns   |
| 6      | Chip deselect time (SCK falling to CS)                  | 3   | -   | ns   |
| 7      | Chip deselect time (CS to SCK)                          | 510 | -   | ns   |
| 9      | CS high time                                            | 511 | -   | ns   |
| 10     | SDI transition time                                     | -   | 5   | ns   |
| 11     | SDI setup time                                          | 6   | -   | ns   |
| 12     | SDI hold time                                           | 3   | -   | ns   |
|        | Table 22: SPI peripheral input timing parameters 1 - 12 |     |     |      |

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 15  | 31  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 15  | 29  | ns   |
| C      | SDO data hold time                          | 49  | 68  | ns   |
| D      | SDO rise/fall time, weak driver mode        | 3   | 8   | ns   |
| E      | SDO data disable lag time                   | 7   | 20  | ns   |

#### **Table 23: SPI peripheral timing parameters A - E, 2 pF load capacitance**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 17  | 42  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 16  | 39  | ns   |
| C      | SDO data hold time                          | 52  | 88  | ns   |
| D      | SDO rise/fall time, weak driver mode        | 2   | 21  | ns   |
| E      | SDO data disable lag time                   | 7   | 20  | ns   |

**Table 24: SPI peripheral timing parameters A - E, 20 pF load capacitance**



| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 20  | 62  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 19  | 59  | ns   |
| C      | SDO data hold time                          | 58  | 128 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 7   | 38  | ns   |
| E      | SDO data disable lag time                   | 7   | 20  | ns   |

**Table 25: SPI peripheral timing parameters A - E, 60 pF load capacitance**

### <span id="page-17-0"></span>**5.3 I2C**

An I2C interface is available for communication with an external host CPU in I2C standard mode, fast mode and fast mode plus. The interface can be operated only in peripheral mode with the maximum bit rate of 1000 kbit/s. The interface can make use of clock stretching by holding the SCL line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms. The I2C timing parameters are defined in [Figure](#page-17-1) 4 and specified in [Table](#page-17-2) 26.

<span id="page-17-1"></span>

**Figure 4: ZED-X20P I2C peripheral specification**

<span id="page-17-2"></span>

|         |                                              | Standard mode |     | Fast mode |     | Fast mode plus |      |      |
|---------|----------------------------------------------|---------------|-----|-----------|-----|----------------|------|------|
| Symbol  | Parameter                                    | Min           | Max | Min       | Max | Min            | Max  | Unit |
| fSCL    | SCL clock frequency                          | -             | 100 | -         | 400 | -              | 1000 | kHz  |
| tHD;STA | Hold time (repeated) START<br>condition      | 4.0           | -   | 0.6       | -   | 0.26           | -    | µs   |
| tLOW    | Low period of the SCL clock                  | 4.7           | -   | 1.3       | -   | 0.26           | -    | µs   |
| tHIGH   | High period of the SCL clock                 | 4.0           | -   | 0.6       | -   | 0.5            | -    | µs   |
| tSU;STA | Setup time for a repeated START<br>condition | 4.7           | -   | 0.6       | -   | 0.26           | -    | µs   |



| Parameter<br>19, 20 Data hold time<br>Data setup time<br>Rise time of both SDA and SCL | Min<br>0<br>250 | Max<br>-<br>- | Min<br>0<br>100 | Max<br>-<br>- | Min<br>0 | Max<br>- | Unit<br>µs |
|----------------------------------------------------------------------------------------|-----------------|---------------|-----------------|---------------|----------|----------|------------|
|                                                                                        |                 |               |                 |               |          |          |            |
|                                                                                        |                 |               |                 |               |          |          |            |
|                                                                                        |                 |               |                 |               | 50       | -        | ns         |
|                                                                                        | -               | 1000          | -               | 300           | -        | 120      | ns         |
| Fall time of both SDA and SCL<br>signals                                               | -               | 300           | -               | 300           | -        | 120      | ns         |
| Setup time for STOP condition                                                          | 4.0             | -             | 0.6             | -             | 0.26     | -        | µs         |
| Bus-free time between a STOP<br>and START condition                                    | 4.7             | -             | 1.3             | -             | 0.5      | -        | µs         |
| Data valid time                                                                        | -               | 3.45          | -               | 0.9           | -        | 0.45     | µs         |
| Data valid acknowledge time                                                            | -               | 3.45          | -               | 0.9           | -        | 0.45     | µs         |
| Noise margin at the low level                                                          | 0.1 VCC         | -             | 0.1 VCC         | -             | 0.1 VCC  | -        | V          |
| Noise margin at the high level                                                         | 0.2 VCC         | -             | 0.2 VCC         | -             | 0.2 VCC  | -        | V          |
| Capacitive load for each bus line                                                      | -               | 400           | -               | 400           | -        | 550      | pF         |
|                                                                                        | signals         |               |                 |               |          |          |            |

**Table 26: ZED-X20P I2C peripheral timings and specifications**

The I2C interface is only available with the UART default mode. If the SPI interface is selected by using **D\_SEL** = 0, the I2C interface is not available.

#### <span id="page-18-0"></span>**5.4 Default interface settings**

| Interface    | Settings                                                                                                                                                                                                                                                                     |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART1 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                               |
|              | NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output by default.                                                                                                                                                                                         |
|              | UBX and RTCM 3.4 protocols are enabled by default but no output messages are enabled by<br>default.                                                                                                                                                                          |
| UART1 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                               |
|              | UBX, NMEA and RTCM 3.4 input protocols are enabled by default.                                                                                                                                                                                                               |
| UART2 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                               |
|              | RTCM 3.4 protocol is enabled by default but no output messages are enabled by default.                                                                                                                                                                                       |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                        |
| UART2 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                               |
|              | RTCM 3.4 protocol is enabled by default.                                                                                                                                                                                                                                     |
|              | SPARTN protocol is enabled by default.                                                                                                                                                                                                                                       |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                        |
| I2C          | Available for communication in the Fast-mode with an external host CPU in peripheral mode<br>only. Default messages activated as in UART1. Input/output protocols available as in UART1.<br>Maximum bit rate 400 kb/s.                                                       |
| SPI          | Allow communication to a host CPU, operated in peripheral mode only. Default messages<br>activated as in UART1. Input/output protocols available as in UART1. SPI is not available unless<br>D_SEL pin is set to low (see section D_SEL interface in Integration manual[1]). |

**Table 27: Default interface settings**

<span id="page-18-1"></span><sup>19</sup> External device must provide a hold time of at least one transition time (max 300 ns) for the SDA signal (with respect to the min VIH of the SCL signal) to bridge the undefined region of the falling edge of SCL.

<span id="page-18-2"></span><sup>20</sup> The maximum tHD;DAT must be less than the maximum tVD;DAT or tVD;ACK with a maximum of 0.9 µs by a transition time. The maximum must only be met if the device does not stretch the low period tLOW of the SCL signal. If the clock stretches the SCL, the data must be valid by the set-up time before it releases the clock.



- Refer to the applicable Interface description for information about further settings.
- By default, ZED-X20P outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.



<span id="page-20-0"></span>



|  | — | $\overline{\phantom{0}}$ | ╼ |  |  |
|--|---|--------------------------|---|--|--|
|  |   |                          |   |  |  |

| Figure 5: ZED-X20P mechanical drawing |  |  |
|---------------------------------------|--|--|
|---------------------------------------|--|--|

| Symbol | Min (mm) | Typical (mm) | Max (mm) |
|--------|----------|--------------|----------|
| A      | 21.80    | 22.00        | 22.20    |
| B      | 16.80    | 17.00        | 17.20    |
| C      | 2.20     | 2.40         | 2.60     |
| D      | 3.65     | 3.85         | 4.05     |
| E      | 0.85     | 1.05         | 1.25     |
| F      | 1.70     | 1.90         | 2.10     |
| G      | 1.05     | 1.10         | 1.15     |
| H      | 0.70     | 0.80         | 0.96     |
| K      | 1.20     | 1.50         | 1.80     |
| M      | 3.45     | 3.65         | 3.85     |
| N      | 3.05     | 3.25         | 3.45     |
| P      | 2.05     | 2.10         | 2.15     |



| Symbol | Min (mm) | Typical (mm) | Max (mm) |
|--------|----------|--------------|----------|
| R      | 0.88     | 1.10         | 1.32     |
| L      | 0.00     |              | 0.30     |
| Weight |          | 1.6 g        |          |

#### **Table 28: ZED-X20P mechanical dimensions**

The mechanical picture of the de-paneling residual tabs (L) is an approximate representation. The shape and position may vary.

Take the size of the de-paneling residual tabs into account when designing the component keepout area.

## <span id="page-22-0"></span>**7 Qualifications and approvals**

| Type                                       | Description                                                                           |
|--------------------------------------------|---------------------------------------------------------------------------------------|
| Quality and reliability                    |                                                                                       |
| Product qualification                      | Qualified according to u-blox qualification policy, based on a subset of AEC<br>Q104. |
| Chip qualification                         | Modules are based on AEC-Q100 qualified GNSS chips.                                   |
| Manufacturing                              | Manufactured at ISO/TS 16949 certified sites.                                         |
| Environmental                              |                                                                                       |
| RoHS compliance                            | Yes                                                                                   |
| 21, 22<br>Moisture sensitivity level (MSL) | 4                                                                                     |
| Type approvals                             |                                                                                       |
| European RED certification (CE)            | 23<br>Yes                                                                             |
| UK conformity assessment (UKCA)            | 23<br>Yes                                                                             |

**Table 29: Qualifications and approvals**

<span id="page-22-1"></span><sup>21</sup> For the MSL standard, see IPC/JEDEC J-STD-020 and J-STD-033 [\[3\]](#page-27-3).

<span id="page-22-2"></span><sup>22</sup> For more information regarding moisture sensitivity levels, labeling, storage, and drying, see the Product packaging reference guide [\[4](#page-27-4)].

<span id="page-22-3"></span><sup>23</sup> The certification/conformity assessment process is ongoing.



### <span id="page-23-0"></span>**8 Packaging**

The ZED-X20P modules are delivered as hermetically sealed, reeled tapes in order to enable efficient production, production lot set-up and tear-down. For more information about packaging, see the Product packaging reference guide [[4](#page-27-4)].

#### <span id="page-23-1"></span>**8.1 Reels**

The ZED-X20P modules are deliverable in quantities of 250 pieces on a reel. They are shipped on reel type B, as specified in the Product packaging reference guide [\[4\]](#page-27-4).

| Package                                | Reel type | Delivery quantity |  |  |
|----------------------------------------|-----------|-------------------|--|--|
| SMD                                    | B2        | 250               |  |  |
| Table 30: Reel information for modules |           |                   |  |  |

#### <span id="page-23-2"></span>**8.2 Tapes**

[Figure](#page-23-3) 6 illustrates the feed direction, component orientation, and tape dimensions (mm). The tape feeds into the pick-and-place machine from the reel on the left side of the figure and moves to the right.

<span id="page-23-3"></span>





### <span id="page-24-0"></span>**9 Soldering**

For information on reflow soldering, see IPC/JEDEC J-STD-020 [[3\]](#page-27-3) and Integration manual[[1](#page-27-2)].



### <span id="page-25-0"></span>**10 Product marking and ordering information**

This section provides information about product marking and ordering.

#### <span id="page-25-1"></span>**10.1 Product marking**

The product marking provides information on ZED-X20P and its revision, as in [Figure](#page-25-3) 7. For a description of the product marking, see [Table](#page-25-4) 31

<span id="page-25-3"></span>

#### **Figure 7: Example of ZED-X20P marking**

<span id="page-25-4"></span>

| Code          | Meaning                    | Example                                   |
|---------------|----------------------------|-------------------------------------------|
| PPP           | Form factor                | ZED                                       |
| TG(G)         | Platform                   | X20 = u-blox X20                          |
| V             | Variant                    | P = High precision                        |
| NN            | Major product version      | 00, 01, , 99                              |
| Q             | Product grade              | A = Automotive                            |
|               |                            | B = Professional                          |
|               |                            | C = Standard                              |
| XX            | Revision                   | Hardware and firmware versions            |
| XXXXXXXXXXX   | Serial number              | Alphanumeric characters, e.g. BN600001181 |
| YY/WW or YYWW | Production date            | Year/week, e.g. 24/04 or 2404             |
| QR code       | For internal/technical use |                                           |

**Table 31: Description of product marking**

#### <span id="page-25-2"></span>**10.2 Product identifiers**

The ZED-X20P marking features three product identifiers: product name, ordering code and type number. The product name identifies all u-blox products, independent of packaging and product grade, and it is used in documentation such as this data sheet. The ordering code includes the major product version and product grade, while the type number additionally includes the hardware and firmware versions.

[Table](#page-25-5) 32 describes the three different product identifiers used in the ZED-X20P product marking.

<span id="page-25-5"></span>

| Identifier    | Format       | Example      |
|---------------|--------------|--------------|
| Product name  | PPP-TGGV     | ZED-X20P     |
| Ordering code | PPP-TGGV-NNQ | ZED-X20P-00B |



| Identifier  | Format          | Example         |  |  |
|-------------|-----------------|-----------------|--|--|
| Type number | PPP-TGGV-NNQ-XX | ZED-X20P-00B-00 |  |  |
|             |                 |                 |  |  |

**Table 32: Product identifiers**

#### <span id="page-26-0"></span>**10.3 Ordering codes**

| Ordering code                    | Product  | Remark                         |  |
|----------------------------------|----------|--------------------------------|--|
| ZED-X20P-00B                     | ZED-X20P | Shipped with firmware HPG 2.00 |  |
| Table 33: Product ordering codes |          |                                |  |

u-blox provides information on product changes affecting the form factor, size or function of the product. For the Product change notifications (PCNs), see our website at: [https://www.u-blox.com/](https://www.u-blox.com/en/product-resources) [en/product-resources.](https://www.u-blox.com/en/product-resources)



### <span id="page-27-0"></span>**Related documents**

- <span id="page-27-2"></span>**[1]** Integration manual, [UBXDOC-963802114-12901](https://www.u-blox.com/docs/UBXDOC-963802114-12901)
- <span id="page-27-1"></span>**[2]** Interface description, [UBXDOC-304424225-19888](https://www.u-blox.com/docs/UBXDOC-304424225-19888)
- <span id="page-27-3"></span>**[3]** MSL standard IPC/JEDEC J-STD-020, [www.jedec.org](http://www.jedec.org/)
- <span id="page-27-4"></span>**[4]** Product packaging reference guide [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)

For product change notifications and regular updates of u-blox documentation, register on our website, <https://www.u-blox.com>.





### <span id="page-28-0"></span>**Revision history**

| Revision | Date        | Comments                                                                                                                         |
|----------|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| R01      | 06-Sep-2024 | Initial revision.                                                                                                                |
| R02      | 04-Mar-2025 | Update on the supported GNSS constellations, communications interfaces, qualifications<br>and approvals, and packaging sections. |
|          |             | General text enhancement.                                                                                                        |
| R03      | 23-May-2025 | Updated sections:                                                                                                                |
|          |             | •<br>Performance                                                                                                                 |
|          |             | •<br>Firmware features                                                                                                           |
|          |             | •<br>Pin assignment                                                                                                              |
|          |             | •<br>Operating conditions                                                                                                        |
|          |             | •<br>Indicative power requirements                                                                                               |
|          |             | •<br>Communications interfaces                                                                                                   |



### <span id="page-29-0"></span>**Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).