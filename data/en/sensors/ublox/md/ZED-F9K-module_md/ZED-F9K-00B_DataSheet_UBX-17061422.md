

# **ZED-F9K-00B**

## **High precision automotive DR GNSS receiver Professional grade**

**Data sheet**



#### **Abstract**

This data sheet describes the ZED-F9K high precision module with 3D sensors and a multi-band GNSS receiver. The module provides laneaccurate positioning under the most challenging conditions, decimeterlevel accuracy for automotive mass markets, and it is ideal for ADAS, V2X and head-up display. It provides a low-risk multi-band RTK turnkey solution with built-in inertial sensors and lag-free displays with up to 30 Hz real-time position update rate.

**www.u-blox.com**



UBX-17061422 - R08 C1-Public



## **Document information**

| Title                  | ZED-F9K-00B                                |             |
|------------------------|--------------------------------------------|-------------|
| Subtitle               | High precision automotive DR GNSS receiver |             |
| Document type          | Data sheet                                 |             |
| Document number        | UBX-17061422                               |             |
| Revision and date      | R08                                        | 03-May-2024 |
| Disclosure restriction | C1-Public                                  |             |

| Product status                   | Corresponding content status |                                                                                           |
|----------------------------------|------------------------------|-------------------------------------------------------------------------------------------|
| Functional Sample                | Draft                        | For functional testing. Revised and supplementary data will be published<br>later.        |
| In development /<br>prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                    |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be<br>published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be<br>published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                        |

This document applies to the following products:

| Product name | Type number    | Firmware version | PCN reference | Product status  |
|--------------|----------------|------------------|---------------|-----------------|
| ZED-F9K      | ZED-F9K-00B-01 | LAP 1.20         | -             | Mass production |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2024, u-blox AG.



| 1.1 Overview 4<br>1.2 Performance 4<br>1.3 Supported GNSS constellations6<br>1.4 Supported GNSS augmentation systems 6<br>1.4.1 Quasi-Zenith Satellite System (QZSS)6<br>1.4.2 Satellite-based augmentation system (SBAS)7<br>1.4.3 Differential GNSS (DGNSS)7<br>1.5 Broadcast navigation data and satellite signal measurements 7<br>1.5.1 Carrier-phase measurements8<br>1.6 Supported protocols8<br>1.7 Automotive dead reckoning8<br>2 System<br>description<br>10<br>2.1 Block diagram10<br>3 Pin<br>definition11<br>3.1 Pin assignment11<br>4 Electrical<br>specifications14<br>4.1 Absolute maximum ratings14<br>4.2 Operating conditions14<br>4.3 Indicative power requirements15<br>5 Communications<br>interfaces16<br>5.1 UART16<br>5.2 SPI 16<br>5.3 I2C 18<br>5.4 USB 19<br>5.5 WT (wheel tick) and DIR (forward/reverse indication) 19<br>5.6 Default interface settings20<br>6 Mechanical specifications21<br>7 Qualifications<br>and<br>approvals23<br>8 Labeling<br>and<br>ordering<br>information24<br>8.1 Product labeling 24<br>8.2 Explanation of product codes 24<br>8.3 Ordering codes 25<br>Related<br>documents<br>26 | 1 Functional<br>description | 4 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|---|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                             |   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Revision<br>history27       |   |



# <span id="page-3-0"></span>**1 Functional description**

## <span id="page-3-1"></span>**1.1 Overview**

The ZED-F9K-00B module features the u-blox F9 multi-band L1/L2 GNSS receiver with rapid convergence time within seconds. This mass-market component provides decimeter-level positioning with high availability, while making use of all four GNSS constellations simultaneously.

It is the first dead reckoning module with an integrated Inertial Measurement Unit (IMU) capable of high precision positioning. The sophisticated built-in algorithms fuse the IMU data, GNSS measurements, wheel ticks, and vehicle dynamics model to provide lane-accurate positioning where GNSS alone would fail. The module operates under open-sky motorways, in the wooded countryside, in difficult urban environments, and even in tunnels and underground parking. In modern automotive applications, such as advanced driver assistance system (ADAS) where availability can improve the safety of our roads, ZED-F9K-00B is the ultimate solution.

The device is a turnkey solution eliminating the technical risk of integrating third-party libraries, precise positioning engines, and the multi-faceted hardware engineering aspects of radio frequency design and digital design. The u-blox approach provides a transparent evaluation of the positioning solution and clear lines of responsibility for design support while reducing supply chain complexity during production.

ZED-F9K-00B is ideal for innovative automotive architecture designs with limited space and power. The module provides accurate location services to the increasing number of intelligent electronic control units (ECU) such as telematics control unit, navigation system, infotainment and V2X safety systems.

In priority navigation mode the module reaches a navigation rate of up to 30 Hz. The on-board processor augments fused GNSS position with additional IMU-based position estimates. Drivers experience responsive, lag-free user interfaces. ZED-F9K-00B can output raw IMU and raw GNSS data for advanced applications.

ZED-F9K-00B modules are manufactured in ISO/TS 16949 certified sites and are fully tested on a system level. Qualification tests are performed as stipulated in the ISO 16750 standard: "Road vehicles–Environmental conditions and testing for electrical and electronic equipment".

| Parameter                            | Specification                              |                   |
|--------------------------------------|--------------------------------------------|-------------------|
| Receiver type                        | Multi-band high precision DR GNSS receiver |                   |
| Accuracy of time pulse signal        | RMS                                        | 30 ns             |
|                                      | 99%                                        | 60 ns             |
| Frequency of time pulse signal       |                                            | 0.25 Hz to 10 MHz |
|                                      |                                            | (configurable)    |
| 1<br>Operational limits              | Dynamics                                   | ≤ 4 g             |
|                                      | Altitude                                   | 80,000 m          |
|                                      | Velocity                                   | 500 m/s           |
| 2<br>Position error during GNSS loss | 3D Gyro + 3D accelerometer + speed pulse   | 1%                |
|                                      |                                            |                   |

## <span id="page-3-2"></span>**1.2 Performance**

<span id="page-3-3"></span><sup>1</sup> Assuming airborne 4 g platform, not supported by ADR

<span id="page-3-4"></span><sup>2</sup> 68% error incurred without GNSS as a percentage of distance of traveled 1000 m, applicable to four-wheel road vehicle



| Parameter                               | Specification                |          |
|-----------------------------------------|------------------------------|----------|
| 3 4<br>Max navigation update rate (RTK) | Priority navigation mode     | 30 Hz    |
|                                         | Non-priority navigation mode | 2 Hz     |
| 5<br>Velocity accuracy                  |                              | 0.05 m/s |
| 5<br>Dynamic attitude accuracy          | Heading                      | 0.2 deg  |
|                                         | Pitch                        | 0.3 deg  |
|                                         | Roll                         | 0.5 deg  |
| 5<br>Navigation latency                 | Priority navigation mode     | 15 ms    |
| Raw sensor (IMU) data output rate       |                              | 100 Hz   |

| GNSS                      |                   | GPS+GLO+GAL<br>+BDS | GPS+GLO+GAL | GPS+GAL  | GPS+BDS  | BDS      |
|---------------------------|-------------------|---------------------|-------------|----------|----------|----------|
| 6<br>Acquisition          | Cold start        | 26 s                | 25 s        | 30 s     | 25 s     | 28 s     |
|                           | Hot start         | 2 s                 | 2 s         | 2 s      | 2 s      | 2 s      |
|                           | 7<br>Aided starts | 3 s                 | 3 s         | 3 s      | 3 s      | 3 s      |
| Re-convergence<br>time8 9 | RTK               | ≤ 10 s              | ≤ 10 s      | ≤ 10 s   | ≤ 10 s   | ≤ 30 s   |
| 10 11<br>Sensitivity      | Tracking and nav. | -160 dBm            | -160 dBm    | -160 dBm | -160 dBm | -160 dBm |
|                           | Reacquisition     | -157 dBm            | -157 dBm    | -157 dBm | -157 dBm | -157 dBm |
|                           | Cold start        | -147 dBm            | -147 dBm    | -147 dBm | -147 dBm | -145 dBm |
|                           | Hot start         | -158 dBm            | -158 dBm    | -158 dBm | -158 dBm | -158 dBm |
| Position accuracy         | Along track       | 0.20 m              | 0.20 m      | 0.25 m   | 0.25 m   | 0.60 m   |
| 8 12<br>RTK               | Cross track       | 0.20 m              | 0.20 m      | 0.25 m   | 0.25 m   | 0.60 m   |
|                           | 2D CEP            | 0.30 m              | 0.30 m      | 0.40 m   | 0.40 m   | 0.85 m   |
|                           | Vertical          | 0.30 m              | 0.30 m      | 0.40 m   | 0.40 m   | 1.00 m   |

**Table 1: ZED-F9K-00B performance in different GNSS modes**

| GNSS                 |                   | GPS      | GLONASS  | BEIDOU   | GALILEO  |
|----------------------|-------------------|----------|----------|----------|----------|
| 6<br>Acquisition     | Cold start        | 30 s     | 28 s     | 40 s     | -        |
|                      | Hot start         | 2 s      | 2 s      | 2 s      | -        |
|                      | 7<br>Aided start  | 3 s      | 3 s      | 3 s      | -        |
| 10 11<br>Sensitivity | Tracking and nav. | -158 dBm | -158 dBm | -158 dBm | -156 dBm |
|                      | Reacquisition     | -157 dBm | -155 dBm | -157 dBm | -153 dBm |
|                      | Cold start        | -147 dBm | -147 dBm | -141 dBm | -137 dBm |
|                      | Hot start         | -158 dBm | -157 dBm | -158 dBm | -155 dBm |

<span id="page-4-0"></span>3 Rates with SBAS and QZSS enabled for > 98% fix report rate under typical conditions

<span id="page-4-1"></span>4 Update rate depends on the GNSS configuration

<span id="page-4-2"></span>5 68% at 30 m/s for dynamic operation

<span id="page-4-3"></span>6 All satellites at -130 dBm

<span id="page-4-4"></span>7 Dependent on the speed and latency of the aiding data connection, commanded starts

<span id="page-4-5"></span>8 68% depending on atmospheric conditions, baseline length, GNSS antenna, multipath conditions, satellite visibility and geometry

<span id="page-4-6"></span>9 Time to ambiguity fix after 20 s outage

<span id="page-4-7"></span>10 Demonstrated with a good external LNA

<span id="page-4-8"></span>11 Configured min C/N0 of 6 dB/Hz, limited by FW with min C/N0 of 20 dB/Hz for best performance

<span id="page-4-9"></span>12 Measured using 1 km baseline and patch antennas with good ground planes. Does not account for possible antenna phase center offset errors.



| GNSS                        |          | GPS    | GLONASS | BEIDOU | GALILEO |
|-----------------------------|----------|--------|---------|--------|---------|
| 12<br>Position accuracy RTK | 2D CEP   | 0.80 m | 1.00 m  | -      | 1.50 m  |
|                             | Vertical | 1.00 m | 1.50 m  | -      | 2.00 m  |

**Table 2: ZED-F9K-00B performance in single-GNSS modes**

## <span id="page-5-0"></span>**1.3 Supported GNSS constellations**

The ZED-F9K-00B GNSSmodules are concurrent GNSSreceivers that canreceive andtrackmultiple GNSS constellations. Owing to the multi-band RF front-end architecture, all four major GNSS constellations (GPS, GLONASS, Galileo and BeiDou) plus SBAS and QZSS satellites can be received concurrently. All satellites in view can be processed to provide an RTK navigation solution when used with correction data. If power consumption is a key factor, the receiver can be configured for a subset of GNSS constellations.

All satellites in view can be processed to provide an RTK navigation solution when used with correction data; the highest positioning accuracy will be achieved when the receiver is tracking signals on both bands from multiple satellites, and is provided with corresponding correction data.

The QZSS system shares the same frequency bands with GPS and can only be processed in conjunction with GPS.

To benefit from multi-band signal reception, dedicated hardware preparation must be made during the design-in phase. See the Integration manual [[1](#page-25-1)] for u-blox design recommendations.

| The ZED-F9K-00B supports the GNSS and their signals as shown in Table 3. |  |
|--------------------------------------------------------------------------|--|
|                                                                          |  |

<span id="page-5-3"></span>

| GPS / QZSS                            | GLONASS                                     | Galileo                                  | BeiDou             | NavIC |
|---------------------------------------|---------------------------------------------|------------------------------------------|--------------------|-------|
| L1C/A (1575.420 MHz) L1OF (1602 MHz + | k*562.5 kHz, k = –7,,6)                     | E1-B/C (1575.420 MHz) B1I (1561.098 MHz) |                    | -     |
| L2C (1227.600 MHz)                    | L2OF (1246 MHz +<br>k*437.5 kHz, k = –7,,6) | E5b (1207.140 MHz)                       | B2I (1207.140 MHz) | -     |
|                                       |                                             |                                          |                    |       |

**Table 3: Supported GNSS signals on ZED-F9K-00B**

The ZED-F9K-00B can use the u-blox AssistNow™ Online service which provides GNSS assistance information.

ZED-F9K-00B supports the following augmentation systems:

| SBAS                                  | QZSS      | IMES          | Differential GNSS |
|---------------------------------------|-----------|---------------|-------------------|
| EGNOS, GAGAN, WAAS and MSAS supported | Supported | Not supported | RTCM 3.3          |
|                                       |           |               |                   |

**Table 4: Supported augmentation systems of ZED-F9K-00B**

The augmentation systems SBAS and QZSS can be enabled only if GPS operation is also enabled.

#### <span id="page-5-1"></span>**1.4 Supported GNSS augmentation systems**

#### <span id="page-5-2"></span>**1.4.1 Quasi-Zenith Satellite System (QZSS)**

The Quasi-Zenith Satellite System (QZSS) is a regional navigation satellite system that provides positioning services for the Pacific region covering Japan and Australia. The ZED-F9K-00B is able to receive and track QZSS L1 C/A and L2C signals concurrently with GPS signals, resulting in better availability especially under challenging signal conditions, e.g. in urban canyons.



QZSS can be enabled only if GPS operation is also configured.

#### <span id="page-6-0"></span>**1.4.2 Satellite-based augmentation system (SBAS)**

The ZED-F9K-00B optionally supports SBAS (including WAAS in the US, EGNOS in Europe, MSAS in Japan and GAGAN in India) to deliver improved location accuracy within the regions covered. However, the additional inter-standard time calibration step used during SBAS reception results in degraded time accuracy overall.

SBAS reception is enabled by default in ZED-F9K-00B.

#### <span id="page-6-1"></span>**1.4.3 Differential GNSS (DGNSS)**

When operating in RTK mode, RTCM version 3.3 messages are required and the module supports DGNSS according to RTCM 10403.3. ZED-F9K-00B can decode the following RTCM 3.3 messages:

| Message type | Description                                              |
|--------------|----------------------------------------------------------|
| RTCM 1001    | L1-only GPS RTK observables                              |
| RTCM 1002    | Extended L1-only GPS RTK observables                     |
| RTCM 1003    | L1/L2 GPS RTK observables                                |
| RTCM 1004    | Extended L1/L2 GPS RTK observables                       |
| RTCM 1005    | Stationary RTK reference station ARP                     |
| RTCM 1006    | Stationary RTK reference station ARP with antenna height |
| RTCM 1007    | Antenna descriptor                                       |
| RTCM 1009    | L1-only GLONASS RTK observables                          |
| RTCM 1010    | Extended L1-only GLONASS RTK observables                 |
| RTCM 1011    | L1/L2 GLONASS RTK observables                            |
| RTCM 1012    | Extended L1/L2 GLONASS RTK observables                   |
| RTCM 1033    | Receiver and antenna description                         |
| RTCM 1074    | GPS MSM4                                                 |
| RTCM 1075    | GPS MSM5                                                 |
| RTCM 1077    | GPS MSM7                                                 |
| RTCM 1084    | GLONASS MSM4                                             |
| RTCM 1085    | GLONASS MSM5                                             |
| RTCM 1087    | GLONASS MSM7                                             |
| RTCM 1094    | Galileo MSM4                                             |
| RTCM 1095    | Galileo MSM5                                             |
| RTCM 1097    | Galileo MSM7                                             |
| RTCM 1124    | BeiDou MSM4                                              |
| RTCM 1125    | BeiDou MSM5                                              |
| RTCM 1127    | BeiDou MSM7                                              |
| RTCM 1230    | GLONASS code-phase biases                                |

**Table 5: Supported input RTCM 3.3 messages**

#### <span id="page-6-2"></span>**1.5 Broadcast navigation data and satellite signal measurements**

The ZED-F9K-00B can output all the GNSS broadcast data upon reception from tracked satellites. This includes all the supported GNSS signals as well as the QZSS augmentation service. The UBX-RXM-SFRBX message provides this information, see the Interface description [\[2\]](#page-25-2) for the UBX-



RXM-SFRBX message specification. The receiver can provide satellite signal information in a form compatible with the Radio Resource LCS Protocol (RRLP) [\[4\]](#page-25-3).

#### <span id="page-7-0"></span>**1.5.1 Carrier-phase measurements**

The ZED-F9K-00B modules provide raw carrier-phase data for all supported signals, along with pseudorange, Doppler and measurement quality information. The data contained in the UBX-RXM-RAWX message follows the conventions of a multi-GNSS RINEX 3 observation file. For the UBX-RXM-RAWX message specification, see Interface description [\[2\]](#page-25-2).

Raw measurement data are available once the receiver has established data bit synchronization and time-of-week.

Only available with an optional license for an additional cost.

#### <span id="page-7-1"></span>**1.6 Supported protocols**

The ZED-F9K-00B supports the following protocols:

| Protocol                                     | Type                                     |
|----------------------------------------------|------------------------------------------|
| UBX                                          | Input/output, binary, u-blox proprietary |
| NMEA 4.11, 4.10 (default), 4.0, 2.3, and 2.1 | Input/output, ASCII                      |
| RTCM 3.3                                     | Input, binary                            |

**Table 6: Supported protocols**

For specification of the protocols, see the Interface description [[2](#page-25-2)].

#### <span id="page-7-2"></span>**1.7 Automotive dead reckoning**

u-blox's proprietary automotive dead reckoning (ADR) solution uses a 3D inertial measurement unit (IMU) included within the module, and speed pulses from the vehicle's wheel tick (WT) sensor. Alternatively, the vehicle speed data can be provided as messages via a serial interface. Sensor data and GNSS signals are processed together, achieving 100% coverage, with highly accurate and continuous positioning even in GNSS-hostile environments (for example in urban canyons) or in case of GNSS signal absence (for example in tunnels and parking garages).

WT or speed sensor rate variations and the 3D IMU sensors are calibrated automatically and continuously by the module, accommodating automatically for example to vehicle tire wear.

For more details, see the integration manual [\[1\]](#page-25-1).

The ZED-F9K-00B combines GNSS and dead reckoning measurements and computes a position solution at rates of up to 5 Hz with the non-priority navigation mode. In the priority navigation mode, the navigation rate can be increased using IMU-only data to deliver accurate, low-latency position measurements at rates up to 30 Hz. These solutions are reported in standard NMEA, UBX-NAV-PVT and similar messages.

The priority navigation mode works optimally when the IMU and WT sensors have been calibrated, and the alignment angles are correct.

Dead reckoning allows navigation to commence as soon as power is applied to the module (that is, before a GNSS fix has been established) under the following conditions:

- The vehicle has not been moved while the module has been switched off.
- At least a dead reckoning fix was available when the vehicle was last used.
- A backup supply has been available for the module since the vehicle was last used.



The save-on-shutdown feature can be used when no backup supply is available. All necessary information is saved to the flash and read from the flash upon restart.



# <span id="page-9-0"></span>**2 System description**

## <span id="page-9-1"></span>**2.1 Block diagram**



**Figure 1: ZED-F9K-00B block diagram**



# <span id="page-10-0"></span>**3 Pin definition**

#### <span id="page-10-1"></span>**3.1 Pin assignment**

The pin assignment of the ZED-F9K-00B module is shown in [Figure](#page-10-2) 2. The defined configuration of the PIOs is listed in [Table](#page-10-3) 7.

The ZED-F9K-00B is an LGA package with the I/O on the outside edge and central ground pads.

<span id="page-10-2"></span>

#### **Figure 2: ZED-F9K-00B pin assignment**

<span id="page-10-3"></span>

| Pin no. | Name        | I/O | Description                 |
|---------|-------------|-----|-----------------------------|
| 1       | GND         | -   | Ground                      |
| 2       | RF_IN       | I   | RF input                    |
| 3       | GND         | -   | Ground                      |
| 4       | ANT_DETECT  | I   | Active antenna detect       |
| 5       | ANT_OFF     | O   | External LNA disable        |
| 6       | ANT_SHORT_N | I   | Active antenna short detect |
| 7       | VCC_RF      | O   | Voltage for external LNA    |
| 8       | Reserved    | -   | Reserved                    |
| 9       | Reserved    | -   | Reserved                    |



| Pin no. | Name           | I/O | Description                                                                             |
|---------|----------------|-----|-----------------------------------------------------------------------------------------|
| 10      | Reserved       | -   | Reserved                                                                                |
| 11      | Reserved       | -   | Reserved                                                                                |
| 12      | GND            | -   | Ground                                                                                  |
| 13      | Reserved       | -   | Reserved                                                                                |
| 14      | GND            | -   | Ground                                                                                  |
| 15      | Reserved       | -   | Reserved                                                                                |
| 16      | Reserved       | -   | Reserved                                                                                |
| 17      | Reserved       | -   | Reserved                                                                                |
| 18      | Reserved       | -   | Reserved                                                                                |
| 19      | GEOFENCE_STAT  | O   | Geofence status, user defined                                                           |
| 20      | RTK_STAT       | O   | RTK status 0 – fixed, blinking – receiving and using corrections, 1 – no<br>corrections |
| 21      | Reserved       | -   | Reserved                                                                                |
| 22      | WT             | I   | Wheel ticks                                                                             |
| 23      | DIR            | I   | Direction                                                                               |
| 24      | Reserved       | -   | Reserved                                                                                |
| 25      | Reserved       | -   | Reserved                                                                                |
| 26      | RXD2           | I   | Correction UART input                                                                   |
| 27      | TXD2           | O   | Correction UART output                                                                  |
| 28      | Reserved       | -   | Reserved                                                                                |
| 29      | Reserved       | -   | Reserved                                                                                |
| 30      | Reserved       | -   | Reserved                                                                                |
| 31      | Reserved       | -   | Reserved                                                                                |
| 32      | GND            | -   | Ground                                                                                  |
| 33      | VCC            | I   | Voltage supply                                                                          |
| 34      | VCC            | I   | Voltage supply                                                                          |
| 35      | Reserved       | -   | Reserved                                                                                |
| 36      | V_BCKP         | I   | Backup supply voltage                                                                   |
| 37      | GND            | -   | Ground                                                                                  |
| 38      | V_USB          | I   | USB power input                                                                         |
| 39      | USB_DM         | I/O | USB data                                                                                |
| 40      | USB_DP         | I/O | USB data                                                                                |
| 41      | GND            | -   | Ground                                                                                  |
| 42      | TXD / SPI_SDO  | O   | Serial port if D_SEL =1(or open). SPI SDO if D_SEL = 0                                  |
| 43      | RXD / SPI_SDI  | I   | Serial port if D_SEL =1(or open). SPI SDI if D_SEL = 0                                  |
| 44      | SDA / SPI_CS_N | I/O | I2C data if D_SEL =1 (or open). SPI chip select if D_SEL = 0                            |
| 45      | SCL / SPI_CLK  | I/O | I2C Clock if D_SEL =1(or open). SPI clock if D_SEL = 0                                  |
| 46      | TX_READY       | O   | TX_Buffer full and ready for TX of data                                                 |
| 47      | D_SEL          | I   | Interface select                                                                        |
| 48      | GND            | -   | Ground                                                                                  |
| 49      | RESET_N        | I   | RESET_N                                                                                 |
| 50      | SAFEBOOT_N     | I   | SAFEBOOT_N (for future service, updates and reconfiguration, leave OPEN)                |
| 51      | EXT_INT        | I   | External interrupt pin                                                                  |
| 52      | Reserved       | -   | Reserved                                                                                |



| Name      | I/O | Description |
|-----------|-----|-------------|
| TIMEPULSE | O   | Time pulse  |
| Reserved  | -   | Reserved    |
|           |     |             |

**Table 7: ZED-F9K-00B pin assignment**



# <span id="page-13-0"></span>**4 Electrical specifications**

#### <span id="page-13-1"></span>**4.1 Absolute maximum ratings**

CAUTION. Risk of device damage. Exceeding the absolute maximum ratings may affect the lifetime and reliability of the device or permanently damage it. Do not exceed the absolute maximum ratings.

This product is not protected against overvoltage or reversed voltages. Use appropriate protection to avoid device damage from voltage spikes exceeding the specified boundaries.

| Parameter                    | Symbol            | Condition                                   | Min  | Max           | Units |
|------------------------------|-------------------|---------------------------------------------|------|---------------|-------|
| Power supply voltage         | VCC               |                                             | -0.5 | 3.6           | V     |
| 13<br>Voltage ramp on VCC    |                   |                                             | 20   | 8000          | µs/V  |
| Backup battery voltage       | V_BCKP            |                                             | -0.5 | 3.6           | V     |
| 13<br>Voltage ramp on V_BCKP |                   |                                             | 20   |               | µs/V  |
| Input pin voltage            | Vin               | VCC ≤ 3.1 V                                 | -0.5 | VCC + 0.5     | V     |
|                              |                   | VCC > 3.1 V                                 | -0.5 | 3.6           | V     |
| VCC_RF output current        | ICC_RF            |                                             |      | 300           | mA    |
| Supply voltage USB           | V_USB             |                                             | –0.5 | 3.6           | V     |
| USB signals                  | USB_DM,<br>USB_DP |                                             | -0.5 | V_USB + 0.5 V |       |
| Input power at RF_IN         | Prfin             | source impedance =<br>50 Ω, continuous wave |      | 10            | dBm   |
| Storage temperature          | Tstg              |                                             | -40  | +85           | °C    |

**Table 8: Absolute maximum ratings**

## <span id="page-13-2"></span>**4.2 Operating conditions**

Extreme operating temperatures can significantly impact the specified values. If an application operates near the min or max temperature limits, ensure the specified values are not exceeded.

| Parameter                                    | Symbol   | Min       | Typical | Max | Units | Condition                  |
|----------------------------------------------|----------|-----------|---------|-----|-------|----------------------------|
| Power supply voltage                         | VCC      | 2.7       | 3.0     | 3.6 | V     |                            |
| Backup battery voltage                       | V_BCKP   | 1.65      |         | 3.6 | V     |                            |
| 14, 15<br>Backup battery current             | I_BCKP   |           | 45      |     | µA    | V_BCKP = 3 V,<br>VCC = 0 V |
| 15<br>SW backup current                      | I_SWBCKP |           | 1.5     |     | mA    |                            |
| Input pin voltage range                      | Vin      | 0         |         | VCC | V     |                            |
| Digital IO pin low level input voltage       | Vil      |           |         | 0.4 | V     |                            |
| Digital IO pin high level input voltage      | Vih      | 0.8 * VCC |         |     | V     |                            |
| Digital IO pin low level output voltage      | Vol      |           |         | 0.4 | V     | Iol = 2 mA16               |
| Digital IO pin high level output voltage Voh |          | VCC – 0.4 |         |     | V     | Ioh = 2 mA16               |

<span id="page-13-3"></span><sup>13</sup> Exceeding the ramp speed may permanently damage the device

<span id="page-13-4"></span><sup>14</sup> To measure the I\_BCKP the receiver should first be switched on, i.e. VCC and V\_BCKP is available. Then set VCC to 0 V while the V\_BCKP remains available. Afterward measure the current consumption at the V\_BCKP.

<span id="page-13-5"></span><sup>15</sup> The value has been characterized at 25 °C ambient temperature.

<span id="page-13-6"></span><sup>16</sup> TIMEPULSE has 4 mA current drive/sink capability



| Parameter                                                     | Symbol   | Min | Typical   | Max | Units | Condition |
|---------------------------------------------------------------|----------|-----|-----------|-----|-------|-----------|
| DC current through any digital I/O pin<br>(except supplies)   | Ipin     |     |           | 5   | mA    |           |
| Pull-up resistance for SCL, SDA                               | Rpu      | 7   | 15        | 30  | kΩ    |           |
| Pull-up resistance for D_SEL, RXD,<br>TXD, SAFEBOOT_N, EXTINT | Rpu      | 30  | 75        | 130 | kΩ    |           |
| Pull-up resistance for RESET_N                                | Rpu      | 7   | 10        | 13  | kΩ    |           |
| VCC_RF voltage                                                | VCC_RF   |     | VCC - 0.1 |     | V     |           |
| VCC_RF output current                                         | ICC_RF   |     |           | 50  | mA    |           |
| 17<br>Receiver chain noise figure                             | NFtot    |     | 9.5       |     | dB    |           |
| External gain (at RF_IN)                                      | Ext_gain | 17  |           | 50  | dB    |           |
| Operating temperature                                         | Topr     | -40 | +25       | +85 | °C    |           |

**Table 9: Operating conditions**

#### <span id="page-14-0"></span>**4.3 Indicative power requirements**

[Table](#page-14-2) 10 provides examples of typical current requirements when using a cold start command. The given values are total system supply current for a possible application including RF and baseband sections.

All values in [Table](#page-14-2) 10 have been measured at 25 °C ambient temperature.

The actual power requirements vary depending on the FW version used, external circuitry, number of satellites tracked, signal strength, type and time of start, duration, and conditions of test.

<span id="page-14-2"></span>

| Symbol     | Parameter    | Conditions  | GPS+GLO<br>+GAL+BDS | GPS | Unit |
|------------|--------------|-------------|---------------------|-----|------|
| IPEAK      | Peak current | Acquisition | 130                 | 120 | mA   |
| 18<br>IVCC | VCC current  | Acquisition | 90                  | 75  | mA   |
| 18<br>IVCC | VCC current  | Tracking    | 85                  | 70  | mA   |

**Table 10: Currents to calculate the indicative power requirements**

<span id="page-14-1"></span><sup>17</sup> Only valid for GPS

<span id="page-14-3"></span><sup>18</sup> Simulated GNSS signal



# <span id="page-15-0"></span>**5 Communications interfaces**

The ZED-F9K-00B has several communications interfaces [19](#page-15-3) , including UART, SPI, I2C and USB.

All the inputs have internal pull-up resistors in normal operation and can be left open if not used. All the PIOs are supplied by VCC, therefore all the voltage levels of the PIO pins are related to VCC supply voltage.

## <span id="page-15-1"></span>**5.1 UART**

The UART interfaces support configurable baud rates. See the Integration manual [\[1\]](#page-25-1).

Hardware flow control is not supported.

UART1 is the primary host communications interface while UART2 is dedicated for RTCM 3.3 corrections and NMEA. No UBX protocol is supported on UART 2.

The UART1 is enabled if D\_SEL pin of the module is left open or "high".

| Symbol | Parameter              | Min   | Max    | Unit  |
|--------|------------------------|-------|--------|-------|
| Ru     | Baud rate              | 9600  | 921600 | bit/s |
| ΔTx    | Tx baud rate accuracy  | -1%   | +1%    | -     |
| ΔRx    | Rx baud rate tolerance | -2.5% | +2.5%  | -     |

**Table 11: ZED-F9K-00B UART specifications**

## <span id="page-15-2"></span>**5.2 SPI**

The SPI interface is disabled by default. The SPI interface shares pins with UART and I2C and can be selected by setting D\_SEL = 0. The SPI interface can be operated in peripheral mode only. The maximum transfer rate using SPI is 125 kB/s and the maximum SPI clock frequency is 5.5 MHz.

The SPI timing parameters for peripheral operation are defined in [Figure](#page-16-0) 3. Default SPI configuration is CPOL = 0 and CPHA = 0.

<span id="page-15-3"></span><sup>19</sup> The signal names and related terms have been replaced with new terminology in this document.



<span id="page-16-0"></span>

**Figure 3: ZED-F9K-00B SPI specification mode 1: CPHA=0 SCK = 5.33 MHz**

| Symbol | Parameter                              | Min | Max | Unit |
|--------|----------------------------------------|-----|-----|------|
| 1      | CS deassertion hold time               | 23  | -   | ns   |
| 2      | Chip select time (CS to SCK)           | 20  | -   | ns   |
| 3      | SCK rise/fall time                     | -   | 7   | ns   |
| 4      | SCK high time                          | 24  | -   | ns   |
| 5      | SCK low time                           | 24  | -   | ns   |
| 6      | Chip deselect time (SCK falling to CS) | 30  | -   | ns   |
| 7      | Chip deselect time (CS to SCK)         | 30  | -   | ns   |
| 9      | CS high time                           | 32  | -   | ns   |
| 10     | SDI transition time                    | -   | 7   | ns   |
| 11     | SDI setup time                         | 16  | -   | ns   |
| 12     | SDI hold time                          | 24  | -   | ns   |
|        |                                        |     |     |      |

**Table 12: SPI peripheral input timing parameters 1 - 12**

| Parameter                                   | Min | Max | Unit |
|---------------------------------------------|-----|-----|------|
| SDO data valid time (CS)                    | 12  | 40  | ns   |
| SDO data valid time (SCK), weak driver mode | 15  | 40  | ns   |
| SDO data hold time                          | 100 | 140 | ns   |
| SDO rise/fall time, weak driver mode        | 0   | 5   | ns   |
| SDO data disable lag time                   | 15  | 35  | ns   |
|                                             |     |     |      |

**Table 13: SPI peripheral timing parameters A - E, 2 pF load capacitance**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 16  | 55  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 20  | 55  | ns   |
| C      | SDO data hold time                          | 100 | 150 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 3   | 20  | ns   |



| Symbol | Parameter                                                                | Min | Max | Unit |  |  |  |  |  |
|--------|--------------------------------------------------------------------------|-----|-----|------|--|--|--|--|--|
| E      | SDO data disable lag time                                                | 15  | 35  | ns   |  |  |  |  |  |
|        | Table 14: SPI peripheral timing parameters A - E, 20 pF load capacitance |     |     |      |  |  |  |  |  |
| Symbol | Parameter                                                                | Min | Max | Unit |  |  |  |  |  |
| A      | SDO data valid time (CS)                                                 | 26  | 85  | ns   |  |  |  |  |  |
| B      | SDO data valid time (SCK), weak driver mode                              | 30  | 85  | ns   |  |  |  |  |  |
| C      | SDO data hold time                                                       | 110 | 160 | ns   |  |  |  |  |  |
| D      | SDO rise/fall time, weak driver mode                                     | 13  | 45  | ns   |  |  |  |  |  |
| E      | SDO data disable lag time                                                | 15  | 35  | ns   |  |  |  |  |  |
|        |                                                                          |     |     |      |  |  |  |  |  |

**Table 15: SPI peripheral timing parameters A - E, 60 pF load capacitance**

### <span id="page-17-0"></span>**5.3 I2C**

An I2C interface is available for communication with an external host CPU in I2C Fast-mode. Backwards compatibility with Standard-mode I2C bus operation is not supported. The interface can be operated only in peripheral mode with a maximum bit rate of 400 kbit/s. The interface can make use of clock stretching by holding the SCL line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms.



| Figure 4: ZED-F9K-00B I2C peripheral specification |  |
|----------------------------------------------------|--|
|                                                    |  |

|         |                                           | I2C Fast-mode |     |      |
|---------|-------------------------------------------|---------------|-----|------|
| Symbol  | Parameter                                 | Min           | Max | Unit |
| fSCL    | SCL clock frequency                       | 0             | 400 | kHz  |
| tHD;STA | Hold time (repeated) START condition      | 0.6           | -   | µs   |
| tLOW    | Low period of the SCL clock               | 1.3           | -   | µs   |
| tHIGH   | High period of the SCL clock              | 0.6           | -   | µs   |
| tSU;STA | Setup time for a repeated START condition | 0.6           | -   | µs   |



|         |                                                     | I2C Fast-mode |                     |      |
|---------|-----------------------------------------------------|---------------|---------------------|------|
| Symbol  | Parameter                                           | Min           | Max                 | Unit |
| tHD;DAT | Data hold time                                      | 0 20          | 21<br>-             | µs   |
| tSU;DAT | Data setup time                                     | 100 22        |                     | ns   |
| tr      | Rise time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| tf      | Fall time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| tSU;STO | Setup time for STOP condition                       | 0.6           | -                   | µs   |
| tBUF    | Bus-free time between a STOP and START<br>condition | 1.3           | -                   | µs   |
| tVD;DAT | Data valid time                                     | -             | 0.9 21              | µs   |
| tVD;ACK | Data valid acknowledge time                         | -             | 0.9 21              | µs   |
| VnL     | Noise margin at the low level                       | 0.1 VCC       | -                   | V    |
| VnH     | Noise margin at the high level                      | 0.2 VCC       | -                   | V    |

**Table 16: ZED-F9K-00B I2C peripheral timings and specifications**

The I2C interface is only available with the UART default mode. If the SPI interface is selected by using D\_SEL = 0, the I2C interface is not available.

#### <span id="page-18-0"></span>**5.4 USB**

The USB 2.0 FS (full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface. The V\_USB pin supplies the USB interface.

### <span id="page-18-1"></span>**5.5 WT (wheel tick) and DIR (forward/reverse indication)**

ZED-F9K-00B pin 22(WT)is available as awheel-tick input.Thepin23(DIR)is available as adirection input (forward/reverse indication).

By default the wheel tick count is derived from the rising edges of the WT input.

For optimal performance the wheel tick resolution should be less than 5 cm. With the maximum supported wheel tick resolution is 40 cm.

The DIR input shall indicate whether the vehicle is moving forwards or backwards.

Alternatively, the vehicleWT(or speed) and DIR inputs can be provided via one of the communication interfaces with UBX-ESF-MEAS messages.

For more details, see the integration manual [\[1\]](#page-25-1).

<span id="page-18-2"></span><sup>20</sup> External device must provide a hold time of at least one transition time (max 300 ns) for the SDA signal (with respect to the min Vih of the SCL signal) to bridge the undefined region of the falling edge of SCL.

<span id="page-18-3"></span><sup>21</sup> The maximum tHD;DAT must be less than the maximum tVD;DAT or tVD;ACK with a maximum of 0.9 µs by a transition time. This maximum must only be met if the device does not stretch the LOW period (tLOW) of the SCL signal. If the clock stretches the SCL, the data must be valid by the set-up time before it releases the clock.

<span id="page-18-4"></span><sup>22</sup> When the I2C peripheral is stretching the clock, the tSU;DAT of the first bit of the next byte is 62.5 ns.



#### <span id="page-19-0"></span>**5.6 Default interface settings**

| Interface    | Settings                                                                                                                                                                                                                                                                      |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART1 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output by default.                                                                                                                                                                                          |
|              | UBX protocol is enabled by default but no output messages are enabled by default.                                                                                                                                                                                             |
|              | RTCM 3.3 protocol output is not supported.                                                                                                                                                                                                                                    |
| UART1 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | UBX, NMEA and RTCM 3.3 input protocols are enabled by default.                                                                                                                                                                                                                |
| UART2 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | UBX protocol cannot be enabled.                                                                                                                                                                                                                                               |
|              | RTCM 3.3 protocol output is not supported.                                                                                                                                                                                                                                    |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                         |
| UART2 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | UBX protocol cannot be enabled and will not receive UBX input messages.                                                                                                                                                                                                       |
|              | RTCM 3.3 protocol is enabled by default.                                                                                                                                                                                                                                      |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                         |
| USB          | Default messages activated as in UART1. Input/output protocols available as in UART1.                                                                                                                                                                                         |
| I2C          | Available for communication in the Fast-mode with an external host CPU in peripheral mode<br>only. Default messages activated as in UART1. Input/output protocols available as in UART1.<br>Maximum bit rate 400 kb/s.                                                        |
| SPI          | Allow communication to a host CPU, operated in peripheral mode only. Default messages<br>activated as in UART1. Input/output protocols available as in UART1. SPI is not available unless<br>D_SEL pin is set to low (see section D_SEL interface in Integration manual [1]). |

**Table 17: Default interface settings**

By default, the ZED-F9K-00B outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.



# <span id="page-20-0"></span>**6 Mechanical specifications**





#### **Figure 5: ZED-F9K-00B mechanical drawing**

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
| Weight |          | 1.8 g        |          |

#### **Table 18: ZED-F9K-00B mechanical dimensions**

The mechanical picture of the de-paneling residual tabs (L) is an approximate representation. The shape and position may vary.

Take the size of the de-paneling residual tabs into account when designing the component keepout area.



# <span id="page-22-0"></span>**7 Qualifications and approvals**

| Quality and reliability                   |                                                                                                                       |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Product qualification                     | Qualified according to u-blox qualification policy, based on a subset of AEC<br>Q104 Qualified according to ISO 16750 |
| Chip qualification                        | Modules are based on AEC-Q100 qualified GNSS chips                                                                    |
| Manufacturing                             | Manufactured at ISO/TS 16949 certified sites                                                                          |
| Environmental                             |                                                                                                                       |
| RoHS compliance                           | Yes                                                                                                                   |
| 23 24<br>Moisture sensitivity level (MSL) | 4                                                                                                                     |
| Type approvals                            |                                                                                                                       |
| European RED certification (CE)           | Declaration of Conformity (DoC) is available on the u-blox website.                                                   |
| UK conformity assessment (UKCA)           | Yes                                                                                                                   |
|                                           |                                                                                                                       |

**Table 19: Qualifications and approvals**

<span id="page-22-1"></span><sup>23</sup> For the MSL standard, see IPC/JEDEC J-STD-020 and J-STD-033, available on [www.jedec.org](https://www.jedec.org/)

<span id="page-22-2"></span><sup>24</sup> For more information regarding moisture sensitivity levels, labelling, storage and drying, see the Product packaging reference guide [\[3](#page-25-4)]



# <span id="page-23-0"></span>**8 Labeling and ordering information**

This section provides information about product labeling and ordering. For information about product handling and soldering see the Integration manual [\[1\]](#page-25-1).

#### <span id="page-23-1"></span>**8.1 Product labeling**

The labeling of the ZED-F9K-00B modules provides product information and revision information. For more information, contact u-blox sales.



**Figure 6: Example of ZED-F9K-00B label**

#### <span id="page-23-2"></span>**8.2 Explanation of product codes**

Three product code formats are used in the ZED-F9K-00B labels. The **Product name** used in documentation such as this data sheet identifies all u-blox products, independent of packaging and quality grade. The **Ordering code** includes options and quality, while the **Type number** includes the hardware and firmware versions.

[Table](#page-23-3) 20 below details these three formats.

<span id="page-23-3"></span>

| Format        | Structure      | Product code   |  |
|---------------|----------------|----------------|--|
| Product name  | PPP-TGV        | ZED-F9K        |  |
| Ordering code | PPP-TGV-NNQ    | ZED-F9K-00B    |  |
| Type number   | PPP-TGV-NNQ-XX | ZED-F9K-00B-01 |  |

#### **Table 20: Product code formats**

The parts of the product code are explained in [Table](#page-23-4) 21.

<span id="page-23-4"></span>

| Code | Meaning                | Example                                    |
|------|------------------------|--------------------------------------------|
| PPP  | Product family         | ZED                                        |
| TG   | Platform               | F9 = u-blox F9                             |
| V    | Variant                | K = High precision + ADR                   |
| NNQ  | Option / Quality grade | NN: Option [0099]                          |
|      |                        | Q: Grade, A = Automotive, B = Professional |
| XX   | Product detail         | Describes hardware and firmware versions   |

**Table 21: Part identification code**



#### <span id="page-24-0"></span>**8.3 Ordering codes**

| Ordering code | Product        | Remark                                 |
|---------------|----------------|----------------------------------------|
| ZED-F9K-00B   | u-blox ZED-F9K | Shipped with firmware FW 1.00 LAP 1.20 |
|               |                |                                        |

**Table 22: Product ordering codes**

Product changes affecting form, fit or function are documented by u-blox. For a list of Product Change Notifications (PCNs) see our website at: <https://www.u-blox.com/en/product-resources>.



## <span id="page-25-0"></span>**Related documents**

- <span id="page-25-1"></span>**[1]** ZED-F9K Integration manual, [UBX-20046189](https://www.u-blox.com/docs/UBX-20046189)
- <span id="page-25-2"></span>**[2]** LAP 1.20 Interface description, [UBX-20046191](https://www.u-blox.com/docs/UBX-20046191)
- <span id="page-25-4"></span>**[3]** Product packaging reference guide [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-25-3"></span>**[4]** Radio Resource LCS Protocol (RRLP), (3GPP TS 44.031 version 11.0.0 Release 11)

For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



## <span id="page-26-0"></span>**Revision history**

| Revision | Date        | Status / comments                                                                                                                                                                                                                                                                                                                                                 |
|----------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 19-Feb-2019 | Objective specification                                                                                                                                                                                                                                                                                                                                           |
| R02      | 24-Sep-2019 | Advance information<br>Priority/non-priority navigation mode                                                                                                                                                                                                                                                                                                      |
| R03      | 15-Jan-2020 | Early production information - optional license information for carrier-phase<br>measurements, aided starts performance numbers revised                                                                                                                                                                                                                           |
| R04      | 10-Sep-2020 | Advance information - LAP 1.20 update - ZED-F9K-00B-01 update<br>- Added ZED-F9K performance in different single GNSS modes<br>- Performance in different GNSS modes revised<br>- SBAS support added<br>- Communication interfaces section updated<br>- Re-convergence time performance numbers revised                                                           |
| R05      | 06-Nov-2020 | Early production information - ZED-F9K-00B-01 - Public                                                                                                                                                                                                                                                                                                            |
| R06      | 24-Aug-2021 | Advance information - ZED-F9K-00B-02                                                                                                                                                                                                                                                                                                                              |
| R07      | 23-Mar-2023 | Updated I2C and SPI timing specifications in section Communications interfaces<br>Updated VCC_RF output current in table Absolute maximum ratings<br>Updated backup current in table Operating conditions<br>Added timepulse details in table Operating conditions<br>Mechanical specification section updated<br>Mass production - ZED-F9K-00B-01 - Public       |
| R08      | 03-May-2024 | Updated sections:<br>•<br>Mechanical specifications updated with information on de-paneling residual tabs<br>•<br>Qualifications and approvals<br>•<br>Product labeling<br>•<br>Information on moisture sensitivity level has been moved from the Integration manual<br>to chapter Qualifications and approvals<br>•<br>Editorial changes throughout the document |



## **Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).