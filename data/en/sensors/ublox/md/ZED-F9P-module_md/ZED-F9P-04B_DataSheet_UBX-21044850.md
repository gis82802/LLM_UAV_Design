

# **ZED-F9P-04B**

## **High precision GNSS module Professional grade**

**Data sheet**



#### **Abstract**

This data sheet describes the ZED-F9P high precision module with multiband GNSS receiver. The module provides multi-band RTK with fast convergence times, reliable performance and easy integration of RTK for fast time-to-market. It has a high update rate for highly dynamic applications and centimeter-level accuracy in a small and energy-efficient module.

**www.u-blox.com**



UBX-21044850 - R05 C1-Public



## **Document information**

| Title                  | ZED-F9P-04B                |             |
|------------------------|----------------------------|-------------|
| Subtitle               | High precision GNSS module |             |
| Document type          | Data sheet                 |             |
| Document number        | UBX-21044850               |             |
| Revision and date      | R05                        | 21-Mar-2024 |
| Disclosure restriction | C1-Public                  |             |

| Product status                   | Corresponding content status |                                                                                           |
|----------------------------------|------------------------------|-------------------------------------------------------------------------------------------|
| Functional sample                | Draft                        | For functional testing. Revised and supplementary data will be published<br>later.        |
| In development /<br>prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                    |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be<br>published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be<br>published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                        |

This document applies to the following products:

| Product name | Type number    | FW version | IN/PCN reference             | Product status  |
|--------------|----------------|------------|------------------------------|-----------------|
| ZED-F9P      | ZED-F9P-04B-01 | HPG 1.32   | UBX-23000084<br>UBX-23007382 | Mass production |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2024, u-blox AG.



| 1 Functional<br>description                                       | 4  |
|-------------------------------------------------------------------|----|
| 1.1 Overview 4                                                    |    |
| 1.2 Performance 4                                                 |    |
| 1.3 Supported GNSS constellations6                                |    |
| 1.4 Supported GNSS augmentation systems 7                         |    |
| 1.4.1 Quasi-Zenith Satellite System (QZSS)7                       |    |
| 1.4.2 Satellite-based augmentation system (SBAS)7                 |    |
| 1.4.3 Differential GNSS (DGNSS)7                                  |    |
| 1.4.4 Centimeter level augmentation service (CLAS)9               |    |
| 1.5 Broadcast navigation data and satellite signal measurements 9 |    |
| 1.5.1 Carrier-phase measurements9                                 |    |
| 1.6 Supported protocols9                                          |    |
| 2 System<br>description                                           | 10 |
| 2.1 Block diagram10                                               |    |
| 3 Pin<br>definition11                                             |    |
| 3.1 Pin assignment11                                              |    |
| 3.2 Pin states13                                                  |    |
|                                                                   |    |
| 4 Electrical<br>specification                                     | 14 |
| 4.1 Absolute maximum ratings14                                    |    |
| 4.2 Operating conditions14                                        |    |
| 4.3 Indicative power requirements15                               |    |
| 5 Communications<br>interfaces16                                  |    |
| 5.1 UART16                                                        |    |
| 5.2 SPI 16                                                        |    |
| 5.3 I2C 17                                                        |    |
| 5.4 USB 19                                                        |    |
| 5.5 Default interface settings19                                  |    |
| 6 Mechanical specification                                        | 20 |
| 7 Qualifications<br>and<br>approvals22                            |    |
| 8 Labeling<br>and<br>ordering<br>information23                    |    |
| 8.1 Product labeling 23                                           |    |
| 8.2 Explanation of product codes 23                               |    |
| 8.3 Ordering codes 23                                             |    |
| Related<br>documents                                              | 24 |
| Revision<br>history25                                             |    |



## <span id="page-3-0"></span>**1 Functional description**

### <span id="page-3-1"></span>**1.1 Overview**

The ZED-F9P-04B positioning module features the u-blox F9 receiver platform, which provides multi-band GNSS to high-volume industrial applications. The ZED-F9P-04B has integrated u-blox multi-band RTK and PPP-RTK [1](#page-3-3) technologies for centimeter-level accuracy. The module enables precise navigation and automation of moving machinery in industrial and consumer-grade products in a compact surface-mounted form factor of only 17.0 x 22.0 x 2.4 mm.

The ZED-F9P-04B includes moving base support, allowing both base and rover to move while computing the position between them. The moving base is ideal for UAV applications where the UAV is programmed to follow its owner or to land on a moving platform. It is also well suited to attitude sensing applications where both base and rover modules are mounted on the same moving platform and the relative position is used to derive attitude information for the vehicle or tool.

In this document, RTK refers to an OSR-based solution (using RTCM corrections), while PPP-RTK refers to an SSR-based solution (using SPARTN or CLAS corrections).

| Parameter                      | Specification                           |                   |
|--------------------------------|-----------------------------------------|-------------------|
| Receiver type                  | Multi-band GNSS high precision receiver |                   |
| Accuracy of time pulse signal  | RMS                                     | 30 ns             |
|                                | 99%                                     | 60 ns             |
| Frequency of time pulse signal |                                         | 0.25 Hz to 10 MHz |
|                                |                                         | (configurable)    |
| 2<br>Operational limits        | Dynamics                                | ≤ 4 g             |
|                                | Altitude                                | 80,000 m          |
|                                | Velocity                                | 500 m/s           |
| 3<br>Velocity accuracy         |                                         | 0.05 m/s          |
| 3<br>Dynamic heading accuracy  |                                         | 0.3 deg           |

### <span id="page-3-2"></span>**1.2 Performance**

**Table 1: ZED-F9P-04B specifications**

| GNSS4            |                  | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS   |
|------------------|------------------|-----------------|-------------|---------|---------|---------|-------|
| 5<br>Acquisition | Cold start       | 25 s            | 25 s        | 30 s    | 25 s    | 30 s    | 30 s  |
|                  | Hot start        | 2 s             | 2 s         | 2 s     | 2 s     | 2 s     | 2 s   |
|                  | 6<br>Aided start | 2 s             | 2 s         | 2 s     | 2 s     | 2 s     | 2 s   |
| Max navigation   | RTK              | 7 Hz            | 10 Hz       | 15 Hz   | 14 Hz   | 13 Hz   | 20 Hz |
| 7<br>update rate | PVT              | 9 Hz            | 10 Hz       | 20 Hz   | 20 Hz   | 16 Hz   | 25 Hz |
|                  | RAW              | 15 Hz           | 18 Hz       | 25 Hz   | 25 Hz   | 25 Hz   | 25 Hz |

<span id="page-3-3"></span>1 PPP-RTK position accuracy depends on the quality of the SSR service used, high-quality SSR services can perform similarly to RTK

<span id="page-3-4"></span>2 Assuming Airborne 4 g platform

<span id="page-3-5"></span>3 50% at 30 m/s for dynamic operation

<span id="page-3-6"></span>4 GPS used in combination with QZSS and SBAS

- <span id="page-3-7"></span>5 Commanded starts. All satellites at -130 dBm. Measured at room temperature.
- <span id="page-3-8"></span>6 Dependent on the speed and latency of the aiding data connection, commanded starts

<span id="page-3-9"></span>7 Measured with primary output only, secondary output disabled (default)



| GNSS4                |     | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS    |
|----------------------|-----|-----------------|-------------|---------|---------|---------|--------|
| Convergence<br>time8 | RTK | < 10 s          | < 10 s      | < 10 s  | < 10 s  | < 10 s  | < 30 s |

**Table 2: ZED-F9P-04B performance in different GNSS modes**

| GNSS                 |           | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS     |
|----------------------|-----------|-----------------|-------------|---------|---------|---------|---------|
| Horizontal<br>PVT9   | 1.5 m     | 1.5 m           | 1.5 m       | 1.5 m   | 1.5 m   | 1.5 m   |         |
| position<br>accuracy | 9<br>SBAS | 1.0 m           | 1.0 m       | 1.0 m   | 1.0 m   | 1.0 m   | 1.0 m   |
| (CEP)                | 10<br>RTK | 0.01 m          | 0.01 m      | 0.01 m  | 0.01 m  | 0.01 m  | 0.01 m  |
|                      |           | + 1 ppm         | + 1 ppm     | + 1 ppm | + 1 ppm | + 1 ppm | + 1 ppm |
| Vertical             | PVT9      | 2.0 m           | 2.0 m       | 2.0 m   | 2.0 m   | 2.0 m   | 2.0 m   |
| position<br>accuracy | 9<br>SBAS | 1.5 m           | 1.5 m       | 1.5 m   | 1.5 m   | 1.5 m   | 1.5 m   |
| (Median)             | 10<br>RTK | 0.01 m          | 0.01 m      | 0.01 m  | 0.01 m  | 0.01 m  | 0.01 m  |
|                      |           | + 1 ppm         | + 1 ppm     | + 1 ppm | + 1 ppm | + 1 ppm | + 1 ppm |

**Table 3: ZED-F9P-04B position accuracy in different GNSS modes**

| GNSS4                        |              | GPS+GLO+GAL+BDS | GPS+GLO+GAL |
|------------------------------|--------------|-----------------|-------------|
| Horizontal position accuracy | SPARTN       | < 0.06 m        | < 0.06 m    |
| (CEP)                        | CLAS         | 0.04 m          | 0.04 m      |
| Vertical position accuracy   | SPARTN       | < 0.12 m        | < 0.12 m    |
| (Median)                     | CLAS         | 0.08 m          | 0.08 m      |
| 8<br>Convergence time        | 11<br>SPARTN | < 45 s          | < 45 s      |
|                              | CLAS         | < 70 s          | < 70 s      |

**Table 4: ZED-F9P-04B performance for PPP-RTK in different GNSS modes**

PPP-RTK performancewithSPARTN 2.0.1protocol varies amongst service providers and service definitions. Performance has been validated with SPARTN correction stream available at the time of firmware release in April 2022.

| GNSS4             |                   | GPS+GLO+GAL+BDS |
|-------------------|-------------------|-----------------|
| 12<br>Sensitivity | Tracking and nav. | -167 dBm        |
|                   | Reacquisition     | -160 dBm        |
|                   | Cold start        | -148 dBm        |
|                   | Hot start         | -157 dBm        |

**Table 5: ZED-F9P-04B sensitivity**

| GNSS                          | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS    |
|-------------------------------|-----------------|-------------|---------|---------|---------|--------|
| Max navigation<br>update rate | 5 Hz            | 5 Hz        | 5 Hz    | 5 Hz    | 5 Hz    | 8 Hz   |
| Baseline<br>13<br>accuracy    | 0.01 m          | 0.01 m      | 0.01 m  | 0.01 m  | 0.01 m  | 0.01 m |

4 GPS used in combination with QZSS and SBAS

<span id="page-4-0"></span>8 Depends on atmospheric conditions, baseline length, GNSS antenna, multipath conditions, satellite visibility and geometry

<span id="page-4-1"></span>9 24 hours static

<span id="page-4-2"></span>10 Measured using 1 km baseline and patch antennas with good ground planes. Does not account for possible antenna phase center offset errors. ppm limited to baselines up to 20 km.

<span id="page-4-3"></span>11 Measured for IP data stream only with low-latency communication link

<span id="page-4-4"></span>12 Demonstrated with a good external LNA. Measured at room temperature.

<span id="page-4-5"></span>13 50%, measured with 1 m baseline and patch antennas with good ground plane



| GNSS             | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS     |
|------------------|-----------------|-------------|---------|---------|---------|---------|
| Heading accuracy | 0.4 deg         | 0.4 deg     | 0.4 deg | 0.4 deg | 0.4 deg | 0.4 deg |
|                  |                 |             |         |         |         |         |

**Table 6: ZED-F9P-04B moving base RTK performance in different GNSS modes**



**Figure 1: ZED-F9P-04B moving base RTK heading accuracy versus baseline length**

In a moving base application, and especially when the antennas are mounted on the same platform, it is recommended to use identical antennas. Furthermore it is recommended these antennas are mounted with identical orientation, as this will minimize effects of phase center variation.

#### <span id="page-5-0"></span>**1.3 Supported GNSS constellations**

The ZED-F9P-04B GNSSmodules are concurrent GNSSreceivers that can receive and trackmultiple GNSS constellations. Owing to the multi-band RF front-end architecture, all four major GNSS constellations (GPS, GLONASS, Galileo and BeiDou) plus SBAS and QZSS satellites can be received concurrently. All satellites in view can be processed to provide an RTK navigation solution when used with correction data. If power consumption is a key factor, the receiver can be configured for a subset of GNSS constellations.

The QZSS system shares the same frequency bands with GPS and can only be processed in conjunction with GPS.

To benefit from multi-band signal reception, dedicated hardware preparation must be made during the design-in phase. See the Integration manual [[1](#page-23-1)] for u-blox design recommendations.

<span id="page-5-1"></span>

| GPS / QZSS                            | GLONASS                 | Galileo                                  | BeiDou | NavIC |
|---------------------------------------|-------------------------|------------------------------------------|--------|-------|
| L1C/A (1575.420 MHz) L1OF (1602 MHz + | k*562.5 kHz, k = –7,,6) | E1-B/C (1575.420 MHz) B1I (1561.098 MHz) |        | -     |

The ZED-F9P-04B supports the GNSS and their signals as shown in [Table](#page-5-1) 7.



| GPS / QZSS         | GLONASS                                     | Galileo            | BeiDou             | NavIC |
|--------------------|---------------------------------------------|--------------------|--------------------|-------|
| L2C (1227.600 MHz) | L2OF (1246 MHz +<br>k*437.5 kHz, k = –7,,6) | E5b (1207.140 MHz) | B2I (1207.140 MHz) | -     |

**Table 7: Supported GNSS signals on ZED-F9P-04B**

The ZED-F9P-04B can use the u-blox AssistNow™ Online service which provides GNSS assistance information.

### <span id="page-6-0"></span>**1.4 Supported GNSS augmentation systems**

#### <span id="page-6-1"></span>**1.4.1 Quasi-Zenith Satellite System (QZSS)**

The Quasi-Zenith Satellite System (QZSS) is a regional navigation satellite system that provides positioning services for the Pacific region covering Japan and Australia. The ZED-F9P-04B is able to receive and track QZSS L1 C/A and L2C signals concurrently with GPS signals, resulting in better availability especially under challenging signal conditions, e.g. in urban canyons.

The ZED-F9P-04B is also able to receive the QZSS L1S signal in order to use the SLAS (Sub-meter Level Augmentation Service) which is an augmentation technology that provides correction data for pseudoranges. Ground monitoring stations positioned in Japan calculate separate corrections for each visible satellite and broadcast this data to the user via QZSS satellites. The correction stream is transmitted on the L1 frequency (1575.42 MHz).

QZSS can be enabled only if GPS operation is also configured.

#### <span id="page-6-2"></span>**1.4.2 Satellite-based augmentation system (SBAS)**

The ZED-F9P-04B supports SBAS (including WAAS in the US, EGNOS in Europe, L1Sb(QZSS SBAS) in Japan and GAGAN in India) to deliver improved location accuracy within the regions covered. However, the additional inter-standard time calibration step used during SBAS reception results in degraded time accuracy overall.

#### <span id="page-6-3"></span>**1.4.3 Differential GNSS (DGNSS)**

When operating in RTK mode, RTCM version 3 messages are required and the module supports DGNSS according to RTCM 10403.3.

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

A ZED-F9P-04B operating as a rover can decode the following RTCM 3.3 messages:



| Message type | Description                                             |
|--------------|---------------------------------------------------------|
| RTCM 1074    | GPS MSM4                                                |
| RTCM 1075    | GPS MSM5                                                |
| RTCM 1077    | GPS MSM7                                                |
| RTCM 1084    | GLONASS MSM4                                            |
| RTCM 1085    | GLONASS MSM5                                            |
| RTCM 1087    | GLONASS MSM7                                            |
| RTCM 1094    | Galileo MSM4                                            |
| RTCM 1095    | Galileo MSM5                                            |
| RTCM 1097    | Galileo MSM7                                            |
| RTCM 1124    | BeiDou MSM4                                             |
| RTCM 1125    | BeiDou MSM5                                             |
| RTCM 1127    | BeiDou MSM7                                             |
| RTCM 1230    | GLONASS code-phase biases                               |
| RTCM 4072.0  | Reference station PVT (u-blox proprietary RTCM Message) |

**Table 8: Supported input RTCM 3.3 messages**

A ZED-F9P-04B operating as a base station can generate the following RTCM 3.3 output messages:

| Message type | Description                                                                |
|--------------|----------------------------------------------------------------------------|
| RTCM 1005    | Stationary RTK reference station ARP                                       |
| RTCM 1074    | GPS MSM4                                                                   |
| RTCM 1077    | GPS MSM7                                                                   |
| RTCM 1084    | GLONASS MSM4                                                               |
| RTCM 1087    | GLONASS MSM7                                                               |
| RTCM 1094    | Galileo MSM4                                                               |
| RTCM 1097    | Galileo MSM7                                                               |
| RTCM 1124    | BeiDou MSM4                                                                |
| RTCM 1127    | BeiDou MSM7                                                                |
| RTCM 1230    | GLONASS code-phase biases                                                  |
| RTCM 4072.0  | Reference station PVT (u-blox proprietary RTCM Message)                    |
| RTCM 4072.1  | Additional reference station information (u-blox proprietary RTCM Message) |

**Table 9: Supported output RTCM 3.3 messages**

#### A ZED-F9P-04B operating as a rover can decode the following SPARTN 2.0.1 messages:

| Message type-subtype | Description                                         |
|----------------------|-----------------------------------------------------|
| SM 0-0               | GPS orbit, clock, bias (OCB)                        |
| SM 0-1               | GLONASS orbit, clock, bias (OCB)                    |
| SM 0-2               | Galileo orbit, clock, bias (OCB)                    |
| SM 1-0               | GPS high-precision atmosphere correction (HPAC)     |
| SM 1-1               | GLONASS high-precision atmosphere correction (HPAC) |
| SM 1-2               | Galileo high-precision atmosphere correction (HPAC) |



| Message type-subtype | Description                      |
|----------------------|----------------------------------|
| SM 2-0               | Geographic area definition (GAD) |

**Table 10: Supported input SPARTN version 2.0.1 messages**

#### <span id="page-8-0"></span>**1.4.4 Centimeter level augmentation service (CLAS)**

A ZED-F9P-04B operating as a rover can receive UBX-RXM-QZSSL6 message from a NEO-D9C on any communication interface. The message contains QZSS CLAS (centimeter-level augmentation service) corrections. The CLAS protocol provides corrections for in-view GPS, Galileo, and QZSS satellites in Japan.

### <span id="page-8-1"></span>**1.5 Broadcast navigation data and satellite signal measurements**

The ZED-F9P-04B can output all the GNSS broadcast data upon reception from tracked satellites. This includes all the supported GNSS signals as well as the QZSS and SBAS augmentation services. The UBX-RXM-SFRBX message provides this information, see the Interface description [\[2\]](#page-23-2) for the UBX-RXM-SFRBX message specification. The receiver can provide satellite signal information in a form compatible with the Radio Resource LCS Protocol (RRLP) [\[4\]](#page-23-3).

#### <span id="page-8-2"></span>**1.5.1 Carrier-phase measurements**

The ZED-F9P-04B modules provide raw carrier-phase data for all supported signals, along with pseudorange, Doppler and measurement quality information. The data contained in the UBX-RXM-RAWX message follows the conventions of a multi-GNSS RINEX 3 observation file. For the UBX-RXM-RAWX message specification, see Interface description [\[2\]](#page-23-2).

Raw measurement data are available once the receiver has established data bit synchronization and time-of-week.

### <span id="page-8-3"></span>**1.6 Supported protocols**

The ZED-F9P-04B supports the following protocols:

| Type                                     |
|------------------------------------------|
| Input/output, binary, u-blox proprietary |
| Input/output, ASCII                      |
| Input/output, binary                     |
| Input, binary                            |
|                                          |

**Table 11: Supported protocols**

For specification of the protocols, see the Interface description [[2](#page-23-2)].



## <span id="page-9-0"></span>**2 System description**

### <span id="page-9-1"></span>**2.1 Block diagram**



#### **Figure 2: ZED-F9P-04B block diagram**

An active antenna is mandatory with the ZED-F9P-04B. For more information, see the Integration manual [\[1\]](#page-23-1).



## <span id="page-10-0"></span>**3 Pin definition**

### <span id="page-10-1"></span>**3.1 Pin assignment**

The pin assignment of the ZED-F9P-04B module is shown in [Figure](#page-10-2) 3. The defined configuration of the PIOs is listed in [Table](#page-10-3) 12.

For detailed information on pin functions and characteristics, see the Integration manual [[1](#page-23-1)].

The ZED-F9P-04B is an LGA package with the I/O on the outside edge and central ground pads.

<span id="page-10-2"></span>

#### **Figure 3: ZED-F9P-04B pin assignment**

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



| Pin no. | Name           | I/O | Description                                                              |
|---------|----------------|-----|--------------------------------------------------------------------------|
| 10      | Reserved       | -   | Reserved                                                                 |
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
| 26      | RXD2           | I   | Correction UART input                                                    |
| 27      | TXD2           | O   | Correction UART output                                                   |
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
| 38      | V_USB          | I   | USB supply                                                               |
| 39      | USB_DM         | I/O | USB data                                                                 |
| 40      | USB_DP         | I/O | USB data                                                                 |
| 41      | GND            | -   | Ground                                                                   |
| 42      | TXD / SPI_SDO  | O   | Host UART output if D_SEL = 1(or open). SPI_SDO if D_SEL = 0             |
| 43      | RXD / SPI_SDI  | I   | Host UART input if D_SEL = 1(or open). SPI_SDI if D_SEL = 0              |
| 44      | SDA / SPI_CS_N | I/O | I2C Data if D_SEL = 1 (or open). SPI Chip Select if D_SEL = 0            |
| 45      | SCL / SPI_CLK  | I/O | I2C Clock if D_SEL = 1(or open). SPI Clock if D_SEL = 0                  |
| 46      | TX_READY       | O   | TX_Buffer full and ready for TX of data                                  |
| 47      | D_SEL          | I   | Interface select for pins 42-45                                          |
| 48      | GND            | -   | Ground                                                                   |
| 49      | RESET_N        | I   | RESET_N                                                                  |
| 50      | SAFEBOOT_N     | I   | SAFEBOOT_N (for future service, updates and reconfiguration, leave OPEN) |



| Pin no. | Name      | I/O | Description            |
|---------|-----------|-----|------------------------|
| 51      | EXTINT    | I   | External interrupt pin |
| 52      | Reserved  | -   | Reserved               |
| 53      | TIMEPULSE | O   | Time pulse             |
| 54      | Reserved  | -   | Reserved               |

**Table 12: ZED-F9P-04B pin assignment**

### <span id="page-12-0"></span>**3.2 Pin states**

[Table](#page-12-1) 13 defines the state of some ZED-F9P-04Bpins in differentmodes.The functions for the ZED-F9P-04B pins are as defined in the default configuration.

<span id="page-12-1"></span>

| Pin no. | Default function | Continuous mode        | Software backup mode | Safeboot mode          |
|---------|------------------|------------------------|----------------------|------------------------|
|         | D_SEL = open     | Input pull-up          | Input pull-up        | Input pull-up          |
| 47      | D_SEL = GND      | High-Z                 | Input pull-down      | High-Z                 |
|         | RXD              | Input pull-up          | Input pull-up        | Input pull-up          |
| 43      | SPI_SDO          | High-Z                 | Input pull-up        | Input pull-up          |
|         | TXD              | Output                 | Input pull-up        | Output                 |
| 42      | SPI_SDI          | 14<br>Output           | Input pull-up        | 14<br>Output           |
|         | SDA              | Input pull-up / Output | Input pull-up        | Input pull-up / Output |
| 44      | SPI_CS_N         | High-Z                 | High-Z               | High-Z                 |
|         | SCL              | Input pull-up          | Input pull-up        | Input pull-up          |
| 45      | SPI_SLK          | High-Z                 | High-Z               | High-Z                 |
| 53      | TIMEPULSE        | Output                 | Input pull-up        | Output low             |
| 50      | SAFEBOOT_N       | Input pull-up          | Input pull-up        | Input pull-up          |
| 51      | EXTINT           | Input pull-up          | Input pull-up        | Input pull-up          |
| 26      | RXD2             | Input pull-up          | Input pull-up        | Input pull-up          |
| 27      | TXD2             | Output                 | Input pull-up        | Output                 |
| 49      | RESET_N          | Input pull-up          | Input pull-up        | Input pull-up          |

**Table 13: ZED-F9P-04B pin states in different operational modes**

<span id="page-12-2"></span><sup>14</sup> If SPI CS = low. Otherwise it is configured as an input pull-up.



## <span id="page-13-0"></span>**4 Electrical specification**

### <span id="page-13-1"></span>**4.1 Absolute maximum ratings**

CAUTION. Risk of device damage. Exceeding the absolute maximum ratings may affect the lifetime and reliability of the device or permanently damage it. Do not exceed the absolute maximum ratings.

This product is not protected against overvoltage or reversed voltages. Use appropriate protection to avoid device damage from voltage spikes exceeding the specified boundaries.

| Parameter                    | Symbol            | Condition                                   | Min  | Max           | Units |
|------------------------------|-------------------|---------------------------------------------|------|---------------|-------|
| Power supply voltage         | VCC               |                                             | -0.5 | 3.6           | V     |
| 15<br>Voltage ramp on VCC    |                   |                                             | 20   | 8000          | µs/V  |
| Backup battery voltage       | V_BCKP            |                                             | -0.5 | 3.6           | V     |
| 15<br>Voltage ramp on V_BCKP |                   |                                             | 20   |               | µs/V  |
| Input pin voltage            | Vin               | VCC ≤ 3.1 V                                 | -0.5 | VCC + 0.5     | V     |
|                              |                   | VCC > 3.1 V                                 | -0.5 | 3.6           | V     |
| VCC_RF output current        | ICC_RF            |                                             |      | 300           | mA    |
| Supply voltage USB           | V_USB             |                                             | –0.5 | 3.6           | V     |
| USB signals                  | USB_DM,<br>USB_DP |                                             | -0.5 | V_USB + 0.5 V |       |
| Input power at RF_IN         | Prfin             | source impedance =<br>50 Ω, continuous wave |      | 10            | dBm   |
| Storage temperature          | Tstg              |                                             | -40  | +85           | °C    |
|                              |                   |                                             |      |               |       |

**Table 14: Absolute maximum ratings**

## <span id="page-13-2"></span>**4.2 Operating conditions**

Extreme operating temperatures can significantly impact the specified values. If an application operates near the min or max temperature limits, ensure the specified values are not exceeded.

| Parameter                                    | Symbol   | Min       | Typical | Max | Units | Condition                  |
|----------------------------------------------|----------|-----------|---------|-----|-------|----------------------------|
| Power supply voltage                         | VCC      | 2.7       | 3.0     | 3.6 | V     |                            |
| Backup battery voltage                       | V_BCKP   | 1.65      |         | 3.6 | V     |                            |
| 16, 17<br>Backup battery current             | I_BCKP   |           | 45      |     | µA    | V_BCKP = 3 V,<br>VCC = 0 V |
| 17<br>SW backup current                      | I_SWBCKP |           | 1.4     |     | mA    |                            |
| Input pin voltage range                      | Vin      | 0         |         | VCC | V     |                            |
| Digital IO pin low level input voltage       | Vil      |           |         | 0.4 | V     |                            |
| Digital IO pin high level input voltage      | Vih      | 0.8 * VCC |         |     | V     |                            |
| Digital IO pin low level output voltage      | Vol      |           |         | 0.4 | V     | Iol = 2 mA18               |
| Digital IO pin high level output voltage Voh |          | VCC – 0.4 |         |     | V     | Ioh = 2 mA18               |

<span id="page-13-3"></span><sup>15</sup> Exceeding the ramp speed may permanently damage the device

<span id="page-13-4"></span><sup>16</sup> To measure the I\_BCKP the receiver should first be switched on, i.e. VCC and V\_BCKP is available. Then set VCC to 0 V while the V\_BCKP remains available. Afterward measure the current consumption at the V\_BCKP.

<span id="page-13-5"></span><sup>17</sup> The value has been characterized at 25 °C ambient temperature.

<span id="page-13-6"></span><sup>18</sup> TIMEPULSE has 4 mA current drive/sink capability



| Parameter                                                     | Symbol   | Min | Typical   | Max   | Units | Condition |
|---------------------------------------------------------------|----------|-----|-----------|-------|-------|-----------|
| DC current through any digital I/O pin<br>(except supplies)   | Ipin     |     |           | 5     | mA    |           |
| Pull-up resistance for SCL, SDA                               | Rpu      | 7   | 15        | 30    | kΩ    |           |
| Pull-up resistance for D_SEL, RXD,<br>TXD, SAFEBOOT_N, EXTINT | Rpu      | 30  | 75        | 130   | kΩ    |           |
| Pull-up resistance for RESET_N                                | Rpu      | 7   | 10        | 13    | kΩ    |           |
| Voltage at USB pins                                           | V_USBIO  | 0   |           | V_USB | V     |           |
| VCC_RF voltage                                                | VCC_RF   |     | VCC - 0.1 |       | V     |           |
| VCC_RF output current                                         | ICC_RF   |     |           | 50    | mA    |           |
| 19<br>Receiver chain noise figure                             | NFtot    |     | 9.5       |       | dB    |           |
| External gain (at RF_IN)                                      | Ext_gain | 17  |           | 50    | dB    |           |
| Operating temperature                                         | Topr     | -40 | +25       | +85   | °C    |           |

**Table 15: Operating conditions**

#### <span id="page-14-0"></span>**4.3 Indicative power requirements**

[Table](#page-14-2) 16 provides examples of typical current requirements when using a cold start command. The given values are total system supply current for a possible application including RF and baseband sections.

All values in [Table](#page-14-2) 16 have been measured at 25 °C ambient temperature.

The actual power requirements vary depending on the FW version used, external circuitry, number of satellites tracked, signal strength, type and time of start, duration, and conditions of test.

<span id="page-14-2"></span>

| Symbol     | Parameter    | Conditions  | GPS+GLO<br>+GAL+BDS | GPS | Unit |
|------------|--------------|-------------|---------------------|-----|------|
| IPEAK      | Peak current | Acquisition | 130                 | 120 | mA   |
| 20<br>IVCC | VCC current  | Acquisition | 90                  | 75  | mA   |
| 20<br>IVCC | VCC current  | Tracking    | 85                  | 70  | mA   |

**Table 16: Currents to calculate the indicative power requirements**

<span id="page-14-1"></span><sup>19</sup> Only valid for GPS

<span id="page-14-3"></span><sup>20</sup> Simulated GNSS signal



## <span id="page-15-0"></span>**5 Communications interfaces**

The ZED-F9P-04B has several communications interfaces [21](#page-15-3) , including UART, SPI, I2C and USB.

All the inputs have internal pull-up resistors in normal operation and can be left open if not used. All the PIOs are supplied by VCC, therefore all the voltage levels of the PIO pins are related to VCC supply voltage.

### <span id="page-15-1"></span>**5.1 UART**

The UART interfaces support configurable baud rates. See the Integration manual [\[1\]](#page-23-1).

Hardware flow control is not supported.

The UART1 is enabled if D\_SEL pin of the module is left open or "high".

| Symbol | Parameter              | Min   | Max    | Unit  |
|--------|------------------------|-------|--------|-------|
| Ru     | Baud rate              | 9600  | 921600 | bit/s |
| ΔTx    | Tx baud rate accuracy  | -1%   | +1%    | -     |
| ΔRx    | Rx baud rate tolerance | -2.5% | +2.5%  | -     |

**Table 17: ZED-F9P-04B UART specifications**

### <span id="page-15-2"></span>**5.2 SPI**

The SPI interface is disabled by default. The SPI interface shares pins with UART and I2C and can be selected by setting D\_SEL = 0. The SPI interface can be operated in peripheral mode only. The maximum transfer rate using SPI is 125 kB/s and the maximum SPI clock frequency is 5.5 MHz.

The SPI timing parameters for peripheral operation are defined in [Figure](#page-15-4) 4. Default SPI configuration is CPOL = 0 and CPHA = 0.

<span id="page-15-4"></span>

**Figure 4: ZED-F9P-04B SPI specification mode 1: CPHA=0 SCK = 5.33 MHz**

<span id="page-15-3"></span><sup>21</sup> The signal names and related terms have been replaced with new terminology in this document.

#### ZED-F9P-04B - Data sheet



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

**Table 18: SPI peripheral input timing parameters 1 - 12**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 12  | 40  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 15  | 40  | ns   |
| C      | SDO data hold time                          | 100 | 140 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 0   | 5   | ns   |
| E      | SDO data disable lag time                   | 15  | 35  | ns   |
|        |                                             |     |     |      |

**Table 19: SPI peripheral timing parameters A - E, 2 pF load capacitance**

| Parameter                                   | Min | Max | Unit |
|---------------------------------------------|-----|-----|------|
| SDO data valid time (CS)                    | 16  | 55  | ns   |
| SDO data valid time (SCK), weak driver mode | 20  | 55  | ns   |
| SDO data hold time                          | 100 | 150 | ns   |
| SDO rise/fall time, weak driver mode        | 3   | 20  | ns   |
| SDO data disable lag time                   | 15  | 35  | ns   |
|                                             |     |     |      |

**Table 20: SPI peripheral timing parameters A - E, 20 pF load capacitance**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 26  | 85  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 30  | 85  | ns   |
| C      | SDO data hold time                          | 110 | 160 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 13  | 45  | ns   |
| E      | SDO data disable lag time                   | 15  | 35  | ns   |

**Table 21: SPI peripheral timing parameters A - E, 60 pF load capacitance**

### <span id="page-16-0"></span>**5.3 I2C**

An I2C interface is available for communication with an external host CPU in I2C Fast-mode. Backwards compatibility with Standard-mode I2C bus operation is not supported. The interface can be operated only in peripheral mode with a maximum bit rate of 400 kbit/s. The interface can make use of clock stretching by holding the SCL line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms.





#### **Figure 5: ZED-F9P-04B I2C peripheral specification**

|         |                                                     | I2C Fast-mode |                     |      |
|---------|-----------------------------------------------------|---------------|---------------------|------|
| Symbol  | Parameter                                           | Min           | Max                 | Unit |
| fSCL    | SCL clock frequency                                 | 0             | 400                 | kHz  |
| tHD;STA | Hold time (repeated) START condition                | 0.6           | -                   | µs   |
| tLOW    | Low period of the SCL clock                         | 1.3           | -                   | µs   |
| tHIGH   | High period of the SCL clock                        | 0.6           | -                   | µs   |
| tSU;STA | Setup time for a repeated START condition           | 0.6           | -                   | µs   |
| tHD;DAT | Data hold time                                      | 0 22          | 23<br>-             | µs   |
| tSU;DAT | Data setup time                                     | 100 24        |                     | ns   |
| tr      | Rise time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| tf      | Fall time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| tSU;STO | Setup time for STOP condition                       | 0.6           | -                   | µs   |
| tBUF    | Bus-free time between a STOP and START<br>condition | 1.3           | -                   | µs   |
| tVD;DAT | Data valid time                                     | -             | 0.9 23              | µs   |
| tVD;ACK | Data valid acknowledge time                         | -             | 0.9 23              | µs   |
| VnL     | Noise margin at the low level                       | 0.1 VCC       | -                   | V    |
| VnH     | Noise margin at the high level                      | 0.2 VCC       | -                   | V    |
|         |                                                     |               |                     |      |

**Table 22: ZED-F9P-04B I2C peripheral timings and specifications**

<span id="page-17-0"></span><sup>22</sup> External device must provide a hold time of at least one transition time (max 300 ns) for the SDA signal (with respect to the min Vih of the SCL signal) to bridge the undefined region of the falling edge of SCL.

<span id="page-17-1"></span><sup>23</sup> The maximum tHD;DAT must be less than the maximum tVD;DAT or tVD;ACK with a maximum of 0.9 µs by a transition time. This maximum must only be met if the device does not stretch the LOW period (tLOW) of the SCL signal. If the clock stretches the SCL, the data must be valid by the set-up time before it releases the clock.

<span id="page-17-2"></span><sup>24</sup> When the I2C peripheral is stretching the clock, the tSU;DAT of the first bit of the next byte is 62.5 ns.



The I2C interface is only available with the UART default mode. If the SPI interface is selected by using D\_SEL = 0, the I2C interface is not available.

### <span id="page-18-0"></span>**5.4 USB**

The USB 2.0 FS (full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface. The V\_USB pin supplies the USB interface.

| Interface    | Settings                                                                                                                                                                                                                                                                      |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART1 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output by default.                                                                                                                                                                                          |
|              | UBX and RTCM 3.3 protocols are enabled by default but no output messages are enabled by<br>default.                                                                                                                                                                           |
| UART1 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | UBX, NMEA and RTCM 3.3 input protocols are enabled by default.                                                                                                                                                                                                                |
|              | SPARTN input protocol is enabled by default.                                                                                                                                                                                                                                  |
| UART2 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | UBX protocol is disabled by default.                                                                                                                                                                                                                                          |
|              | RTCM 3.3 protocol is enabled by default but no output messages are enabled by default.                                                                                                                                                                                        |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                         |
| UART2 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                |
|              | UBX protocol is enabled by default.                                                                                                                                                                                                                                           |
|              | RTCM 3.3 protocol is enabled by default.                                                                                                                                                                                                                                      |
|              | SPARTN protocol is enabled by default.                                                                                                                                                                                                                                        |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                         |
| USB          | Default messages activated as in UART1. Input/output protocols available as in UART1.                                                                                                                                                                                         |
| I2C          | Available for communication in the Fast-mode with an external host CPU in peripheral mode<br>only. Default messages activated as in UART1. Input/output protocols available as in UART1.<br>Maximum bit rate 400 kb/s.                                                        |
| SPI          | Allow communication to a host CPU, operated in peripheral mode only. Default messages<br>activated as in UART1. Input/output protocols available as in UART1. SPI is not available unless<br>D_SEL pin is set to low (see section D_SEL interface in Integration manual [1]). |

#### <span id="page-18-1"></span>**5.5 Default interface settings**

**Table 23: Default interface settings**

- Refer to the applicable Interface description [[2](#page-23-2)] for information about further settings.
- By default, the ZED-F9P-04B outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.
- Do not use UART2 as the only one interface to the host. Not all UBX functionality is available on UART2, such as firmware upgrade, safeboot or backup modes functionalities. No start-up boot screen is sent out from UART2.



## <span id="page-19-0"></span>**6 Mechanical specification**







#### **Figure 6: ZED-F9P-04B mechanical drawing**

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

#### **Table 24: ZED-F9P-04B mechanical dimensions**

The mechanical picture of the de-paneling residual tabs (L) is an approximate representation. The shape and position may vary.

Take the size of the de-paneling residual tabs into account when designing the component keepout area.



## <span id="page-21-0"></span>**7 Qualifications and approvals**

| Quality and reliability                   |                                                                     |
|-------------------------------------------|---------------------------------------------------------------------|
| Product qualification                     | Qualified according to ISO 16750                                    |
| Chip qualification                        | Modules are based on AEC-Q100 qualified GNSS chips                  |
| Manufacturing                             | Manufactured at ISO/TS 16949 certified sites                        |
| Environmental                             |                                                                     |
| RoHS compliance                           | Yes                                                                 |
| 25 26<br>Moisture sensitivity level (MSL) | 4                                                                   |
| Type approvals                            |                                                                     |
| European RED certification (CE)           | Declaration of Conformity (DoC) is available on the u-blox website. |
| UK conformity assessment (UKCA)           | Yes                                                                 |

**Table 25: Qualifications and approvals**

<span id="page-21-1"></span><sup>25</sup> For the MSL standard, see IPC/JEDEC J-STD-020 and J-STD-033, available on [www.jedec.org](https://www.jedec.org/)

<span id="page-21-2"></span><sup>26</sup> For more information regarding moisture sensitivity levels, labelling, storage and drying, see the Product packaging reference guide [\[3](#page-23-4)]



## <span id="page-22-0"></span>**8 Labeling and ordering information**

This section provides information about product labeling and ordering. For information about moisture sensitivity level (MSL), product handling and soldering see the Integration manual [[1\]](#page-23-1).

### <span id="page-22-1"></span>**8.1 Product labeling**

The labeling of the ZED-F9P-04B modules provides product information and revision information. For more information contact u-blox sales.

### <span id="page-22-2"></span>**8.2 Explanation of product codes**

Three product code formats are used in the ZED-F9P-04B labels. The **Product name** used in documentation such as this data sheet identifies all u-blox products, independent of packaging and quality grade. The **Ordering code** includes options and quality, while the **Type number** includes the hardware and firmware versions.

<span id="page-22-4"></span>

| Format        | Structure      | Product code   |  |
|---------------|----------------|----------------|--|
| Product name  | PPP-TGV        | ZED-F9P        |  |
| Ordering code | PPP-TGV-NNQ    | ZED-F9P-04B    |  |
| Type number   | PPP-TGV-NNQ-XX | ZED-F9P-04B-01 |  |

[Table](#page-22-4) 26 below details these three formats.

**Table 26: Product code formats**

The parts of the product code are explained in [Table](#page-22-5) 27.

<span id="page-22-5"></span>

| Code | Meaning                | Example                                                         |
|------|------------------------|-----------------------------------------------------------------|
| PPP  | Product family         | ZED                                                             |
| TG   | Platform               | F9 = u-blox F9                                                  |
| V    | Variant                | P = High precision                                              |
| NNQ  | Option / Quality grade | NN: Option [0099]<br>Q: Grade, A = Automotive, B = Professional |
| XX   | Product detail         | Describes hardware and firmware versions                        |

**Table 27: Part identification code**

#### <span id="page-22-3"></span>**8.3 Ordering codes**

| Ordering code | Product | Remark                                 |
|---------------|---------|----------------------------------------|
| ZED-F9P-04B   | ZED-F9P | Shipped with firmware FW 1.00 HPG 1.32 |

**Table 28: Product ordering codes**

Product changes affecting form, fit or function are documented by u-blox. For a list of Product Change Notifications (PCNs) see our website at: <https://www.u-blox.com/en/product-resources>.



## <span id="page-23-0"></span>**Related documents**

- <span id="page-23-1"></span>**[1]** ZED-F9P Integration manual [UBX-18010802](https://www.u-blox.com/docs/UBX-18010802)
- <span id="page-23-2"></span>**[2]** HPG 1.32 Interface description [UBX-22008968](https://www.u-blox.com/docs/UBX-22008968)
- <span id="page-23-4"></span>**[3]** Product packaging reference guide [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-23-3"></span>**[4]** Radio Resource LCS Protocol (RRLP), (3GPP TS 44.031 version 11.0.0 Release 11)
- **[5]** ZED-F9P Moving Base application note, [UBX-19009093](https://www.u-blox.com/docs/UBX-19009093)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



## <span id="page-24-0"></span>**Revision history**

| Revision | Date        | Status / comments                                                                                                                    |
|----------|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 21-Dec-2021 | Advance information                                                                                                                  |
| R02      | 03-May-2022 | Early production information                                                                                                         |
|          |             | HPG 1.32 update. ZED-F9P-04B-01 update.                                                                                              |
|          |             | Overall text improvement and typo corrections plus:                                                                                  |
|          |             | 1.2 Performance section updated and vertical accuracy added                                                                          |
|          |             | 3.2 Pin states on operational modes table added                                                                                      |
|          |             | 4.2 Operating condition table updated with pull-up resistance values                                                                 |
|          |             | 5.5 Default interface setting table updated                                                                                          |
|          |             | 8.3 Ordering code section updated                                                                                                    |
|          |             | Related document section updated                                                                                                     |
| R03      | 24-Mar-2023 | Updated I2C and SPI timing specifications in section Communications interfaces                                                       |
|          |             | Updated VCC_RF output current in table Absolute maximum ratings                                                                      |
|          |             | Updated backup current in table Operating conditions                                                                                 |
|          |             | Added timepulse footnote in table Operating conditions                                                                               |
| R04      | 15-May-2023 | Changed product status to Mass production                                                                                            |
| R05      | 21-Mar-2024 | Updated sections:                                                                                                                    |
|          |             | •<br>Performance                                                                                                                     |
|          |             | •<br>Mechanical specifications updated with information on de-paneling residual tabs                                                 |
|          |             | •<br>Qualifications and approvals                                                                                                    |
|          |             | •<br>Information on moisture sensitivity level has been moved from the Integration manual<br>to chapter Qualifications and approvals |
|          |             | •<br>Editorial changes throughout the document                                                                                       |



## **Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).