

# **NEO-F9P-15B**

### **High precision GNSS module Professional grade**

**Data sheet**



#### **Abstract**

This data sheet describes the NEO-F9P high precision module with multiband GNSS receiver. The module provides multi-band RTK with fast convergence times, reliable performance and easy integration of RTK for fast time-to-market. It has a high update rate for highly dynamic applications and centimeter-level accuracy in a small and energy-efficient module.

> **Note!** GPS L5 signals are pre-operational and not used by default. Refer to the Overview section for more information.

**www.u-blox.com**

UBX-22021920 - R04 C1-Public





## **Document information**

| Title                  | NEO-F9P-15B                |             |
|------------------------|----------------------------|-------------|
| Subtitle               | High precision GNSS module |             |
| Document type          | Data sheet                 |             |
| Document number        | UBX-22021920               |             |
| Revision and date      | R04                        | 06-Jun-2024 |
| Disclosure restriction | C1-Public                  |             |

| Product status                   | Corresponding content status |                                                                                           |
|----------------------------------|------------------------------|-------------------------------------------------------------------------------------------|
| Functional sample                | Draft                        | For functional testing. Revised and supplementary data will be published<br>later.        |
| In development /<br>prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                    |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be<br>published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be<br>published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                        |

This document applies to the following products:

| Product name | Type number    | FW version    | IN/PCN reference       | Product status  |
|--------------|----------------|---------------|------------------------|-----------------|
| NEO-F9P      | NEO-F9P-15B-00 | HPG L1L5 1.40 | UBXDOC-963802114-12773 | Mass production |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2024, u-blox AG.



| 1 Functional<br>description                                       | 4  |
|-------------------------------------------------------------------|----|
| 1.1 Overview 4                                                    |    |
| 1.2 Performance 4                                                 |    |
| 1.3 Supported GNSS constellations6                                |    |
| 1.4 Supported GNSS augmentation systems 6                         |    |
| 1.4.1 Quasi-Zenith Satellite System (QZSS)6                       |    |
| 1.4.2 Satellite-based augmentation system (SBAS)6                 |    |
| 1.4.3 Differential GNSS (DGNSS)6                                  |    |
| 1.4.4 Centimeter level augmentation service (CLAS)8               |    |
| 1.5 Broadcast navigation data and satellite signal measurements 8 |    |
| 1.5.1 Carrier-phase measurements8                                 |    |
| 1.6 Supported protocols8                                          |    |
| 2 System<br>description9                                          |    |
| 2.1 Block diagram 9                                               |    |
| 3 Pin<br>definition10                                             |    |
| 3.1 Pin assignment10                                              |    |
| 3.2 Pin states11                                                  |    |
|                                                                   |    |
| 4 Electrical<br>specifications12                                  |    |
| 4.1 Absolute maximum ratings12                                    |    |
| 4.2 Operating conditions12<br>4.3 Indicative power requirements13 |    |
|                                                                   |    |
| 5 Communications<br>interfaces14                                  |    |
| 5.1 UART14                                                        |    |
| 5.2 SPI 14                                                        |    |
| 5.3 I2C 15                                                        |    |
| 5.4 USB 17                                                        |    |
| 5.5 Default interface settings17                                  |    |
| 6 Mechanical specifications18                                     |    |
| 7 Qualifications<br>and<br>approvals20                            |    |
| 8 Labeling<br>and<br>ordering<br>information21                    |    |
| 8.1 Product labeling 21                                           |    |
| 8.2 Explanation of product codes 21                               |    |
| 8.3 Ordering codes 22                                             |    |
| Related<br>documents                                              | 23 |
| Revision<br>history24                                             |    |



## <span id="page-3-0"></span>**1 Functional description**

### <span id="page-3-1"></span>**1.1 Overview**

The NEO-F9P-15B positioning module features the u-blox F9 receiver platform, which provides multi-band GNSS to high-volume industrial applications. NEO-F9P-15B has integrated u-blox multi-

band RTK and PPP-RTK [1](#page-3-3) technologies for centimeter-level accuracy. The module enables precise navigation and automation of moving machinery in industrial and consumer-grade products in a compact surface-mounted form factor of only 16.0 x 12.2 x 3.4 mm.

In this document, RTK refers to an OSR-based solution (using RTCM corrections), while PPP-RTK refers to an SSR-based solution (using SPARTN or CLAS corrections).

At the time of writing, the GPS L5 signals remain pre-operational and are set as unhealthy until sufficient monitoring capability is established. This is an operational issue concerning the satellites / space segment and not a limitation of u-blox products.

It is the responsibility of the designer to decide whether the application may use the GPS L5 signals and make the tradeoff between performance and application suitability. Alternatively, the designer may assess the performance in the future when the L5 signals are deemed healthy. Both of these goals can be achieved by configuring the receiver to apply the health status of L1 signals to L5 signals. For details on u-blox GPS L5 configuration, see the Application note [\[5](#page-22-1)] for u-blox GPS L5 configuration.

| Parameter                           | Specification                           |                   |
|-------------------------------------|-----------------------------------------|-------------------|
| Receiver type                       | Multi-band GNSS high precision receiver |                   |
| Accuracy of time pulse signal       | RMS                                     | 30 ns             |
|                                     | 99%                                     | 60 ns             |
| Frequency of time pulse signal      |                                         | 0.25 Hz to 10 MHz |
|                                     |                                         | (configurable)    |
| 2<br>Operational limits             | Dynamics                                | ≤ 4 g             |
|                                     | Altitude                                | 80,000 m          |
|                                     | Velocity                                | 500 m/s           |
| 3<br>Velocity accuracy              |                                         | 0.05 m/s          |
| 3<br>Dynamic heading accuracy       |                                         | 0.3 deg           |
| Table 1: NEO-F9P-15B specifications |                                         |                   |

### <span id="page-3-2"></span>**1.2 Performance**

| GNSS4            |                  | GPS+GLO+GAL+BDS | GPS+BDS+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS  |
|------------------|------------------|-----------------|-------------|---------|---------|---------|------|
| 5<br>Acquisition | Cold start       | 27 s            | 28 s        | 29 s    | 30 s    | 27 s    | 37 s |
|                  | Hot start        | 3 s             | 3 s         | 3 s     | 3 s     | 3 s     | 3 s  |
|                  | 6<br>Aided start | 4 s             | 4 s         | 4 s     | 4 s     | 4 s     | 5 s  |

<span id="page-3-3"></span><sup>1</sup> PPP-RTK position accuracy depends on the quality of the SSR service used, high-quality SSR services can perform similarly to RTK

<span id="page-3-4"></span><sup>2</sup> Assuming Airborne 4 g platform

<span id="page-3-5"></span><sup>3</sup> 50% at 30 m/s for dynamic operation

<span id="page-3-6"></span><sup>4</sup> GPS used in combination with QZSS and SBAS

<span id="page-3-7"></span><sup>5</sup> Commanded starts. All satellites at -130 dBm. Measured at room temperature.

<span id="page-3-8"></span><sup>6</sup> Dependent on the speed and latency of the aiding data connection, commanded starts



| GNSS4                |     | GPS+GLO+GAL+BDS | GPS+BDS+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS    |
|----------------------|-----|-----------------|-------------|---------|---------|---------|--------|
| Max navigation       | RTK | 7 Hz            | 8 Hz        | 14 Hz   | 15 Hz   | 10 Hz   | 25 Hz  |
| 7<br>update rate     | PVT | 7 Hz            | 8 Hz        | 14 Hz   | 20 Hz   | 11 Hz   | 25 Hz  |
|                      | RAW | 10 Hz           | 10 Hz       | 20 Hz   | 25 Hz   | 20 Hz   | 25 Hz  |
| Convergence<br>time8 | RTK | < 12 s          | < 12 s      | < 12 s  | < 12 s  | < 12 s  | < 30 s |

**Table 2: NEO-F9P-15B performance in different GNSS modes**

| GNSS                 |           | GPS+GLO+GAL+BDS | GPS+BDS+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS     |
|----------------------|-----------|-----------------|-------------|---------|---------|---------|---------|
| Horizontal           | PVT9      | 1.5 m           | 1.5 m       | 1.5 m   | 1.5 m   | 1.5 m   | 1.5 m   |
| position<br>accuracy | 9<br>SBAS | 1.0 m           | 1.0 m       | 1.0 m   | 1.0 m   | 1.0 m   | 1.0 m   |
| (CEP)                | 10<br>RTK | 0.01 m          | 0.01 m      | 0.01 m  | 0.01 m  | 0.01 m  | 0.01 m  |
|                      |           | + 1 ppm         | + 1 ppm     | + 1 ppm | + 1 ppm | + 1 ppm | + 1 ppm |
| Vertical             | PVT9      | 2.0 m           | 2.0 m       | 2.0 m   | 2.0 m   | 2.0 m   | 2.0 m   |
| position<br>accuracy | 9<br>SBAS | 1.5 m           | 1.5 m       | 1.5 m   | 1.5 m   | 1.5 m   | 1.5 m   |
| (Median)             | 10<br>RTK | 0.01 m          | 0.01 m      | 0.01 m  | 0.01 m  | 0.01 m  | 0.01 m  |
|                      |           | + 1 ppm         | + 1 ppm     | + 1 ppm | + 1 ppm | + 1 ppm | + 1 ppm |

**Table 3: NEO-F9P-15B position accuracy in different GNSS modes**

| GNSS4                                  |              | GPS+GLO+GAL+BDS | GPS+BDS+GAL |
|----------------------------------------|--------------|-----------------|-------------|
| Horizontal position accuracy           | SPARTN       | < 0.10 m        | < 0.10 m    |
| (CEP)                                  | CLAS         | 0.04 m          | 0.04 m      |
| Vertical position accuracy<br>(Median) | SPARTN       | < 0.20 m        | < 0.20 m    |
|                                        | CLAS         | 0.08 m          | 0.08 m      |
| 8<br>Convergence time                  | 11<br>SPARTN | < 65 s          | < 65 s      |
|                                        | CLAS         | < 90 s          | < 90 s      |

**Table 4: NEO-F9P-15B performance for PPP-RTK in different GNSS modes**

| GNSS4             |                   | GPS+GLO+GAL+BDS |
|-------------------|-------------------|-----------------|
| 12<br>Sensitivity | Tracking and nav. | -167 dBm        |
|                   | Reacquisition     | -160 dBm        |
|                   | Cold start        | -148 dBm        |
|                   | Hot start         | -157 dBm        |

**Table 5: NEO-F9P-15B sensitivity**

Performance values include the use of GPS L5 signals. Refer to the Application Note [UBX-21038688](https://www.u-blox.com/docs/UBX-21038688) for u-blox GPS L5 configuration details.

<sup>4</sup> GPS used in combination with QZSS and SBAS

<span id="page-4-0"></span><sup>7</sup> Measured with primary output only, secondary output disabled (default)

<span id="page-4-1"></span><sup>8</sup> Depends on atmospheric conditions, baseline length, GNSS antenna, multipath conditions, satellite visibility and geometry

<span id="page-4-2"></span><sup>9</sup> 24 hours static

<span id="page-4-3"></span><sup>10</sup> Measured using 1 km baseline and patch antennas with good ground planes. Does not account for possible antenna phase center offset errors. ppm limited to baselines up to 20 km.

<span id="page-4-4"></span><sup>11</sup> Measured for IP data stream only with low-latency communication link

<span id="page-4-5"></span><sup>12</sup> Demonstrated with a good external LNA. Measured at room temperature.



### <span id="page-5-0"></span>**1.3 Supported GNSS constellations**

The NEO-F9P-15B GNSS modules are concurrent GNSS receivers that can receive and track multiple GNSS constellations. Owing to the multi-band RF front-end architecture, all four major GNSS constellations (GPS, GLONASS, Galileo and BeiDou) plus SBAS and QZSS satellites can be received concurrently. All satellites in view can be processed to provide an RTK navigation solution when used with correction data. If power consumption is a key factor, the receiver can be configured for a subset of GNSS constellations.

The QZSS system shares the same frequency bands with GPS and can only be processed in conjunction with GPS.

To benefit from multi-band signal reception, dedicated hardware preparation must be made during the design-in phase. See the Integration manual [[1](#page-22-2)] for u-blox design recommendations.

NEO-F9P-15B supports the GNSS and their signals as shown in [Table](#page-5-5) 6.

<span id="page-5-5"></span>

| GPS / QZSS                            | GLONASS                 | Galileo                                  | BeiDou             | NavIC                    |
|---------------------------------------|-------------------------|------------------------------------------|--------------------|--------------------------|
| L1C/A (1575.420 MHz) L1OF (1602 MHz + | k*562.5 kHz, k = –7,,6) | E1-B/C (1575.420 MHz) B1I (1561.098 MHz) |                    | -                        |
| L5 (1176.450 MHz)                     | -                       | E5a (1176.450 MHz)                       | B2a (1176.450 MHz) | SPS-L5 (1176.450<br>MHz) |

**Table 6: Supported GNSS signals on NEO-F9P-15B**

NEO-F9P-15B can use the u-blox AssistNow™ Online service which provides GNSS assistance information.

#### <span id="page-5-1"></span>**1.4 Supported GNSS augmentation systems**

#### <span id="page-5-2"></span>**1.4.1 Quasi-Zenith Satellite System (QZSS)**

The Quasi-Zenith Satellite System (QZSS) is a regional navigation satellite system that provides positioning services for the Pacific region covering Japan and Australia. NEO-F9P-15B is able to receive and track QZSS L1 C/A and L5 signals concurrently with GPS signals, resulting in better availability especially under challenging signal conditions, e.g. in urban canyons.

NEO-F9P-15B is also able to receive the QZSS L1S signal in order to use the SLAS (Sub-meter Level Augmentation Service) which is an augmentation technology that provides correction data for pseudoranges. Ground monitoring stations positioned in Japan calculate separate corrections for each visible satellite and broadcast this data to the user via QZSS satellites. The correction stream is transmitted on the L1 frequency (1575.42 MHz).

QZSS can be enabled only if GPS operation is also configured.

#### <span id="page-5-3"></span>**1.4.2 Satellite-based augmentation system (SBAS)**

NEO-F9P-15B supports SBAS (including WAAS in the US, EGNOS in Europe, L1Sb(QZSS SBAS) in Japan and GAGAN in India) to deliver improved location accuracy within the regions covered. However, the additional inter-standard time calibration step used during SBAS reception results in degraded time accuracy overall.

#### <span id="page-5-4"></span>**1.4.3 Differential GNSS (DGNSS)**

When operating in the RTK mode, RTCM version 3 messages are required and the module supports DGNSS according to RTCM 10403.3.



#### Operating as a rover, NEO-F9P-15B can decode the following RTCM 3.3 messages:

| Message type | Description                                              |
|--------------|----------------------------------------------------------|
| RTCM 1005    | Stationary RTK reference station ARP                     |
| RTCM 1006    | Stationary RTK reference station ARP with antenna height |
| RTCM 1007    | Antenna descriptor                                       |
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

#### **Table 7: Supported input RTCM 3.3 messages**

#### Operating as a base station, NEO-F9P-15B can generate the following RTCM 3.3 output messages:

| Message type | Description                          |
|--------------|--------------------------------------|
| RTCM 1005    | Stationary RTK reference station ARP |
| RTCM 1074    | GPS MSM4                             |
| RTCM 1077    | GPS MSM7                             |
| RTCM 1084    | GLONASS MSM4                         |
| RTCM 1087    | GLONASS MSM7                         |
| RTCM 1094    | Galileo MSM4                         |
| RTCM 1097    | Galileo MSM7                         |
| RTCM 1124    | BeiDou MSM4                          |
| RTCM 1127    | BeiDou MSM7                          |
| RTCM 1230    | GLONASS code-phase biases            |

**Table 8: Supported output RTCM 3.3 messages**

#### Operating as a rover, NEO-F9P-15B can decode the following SPARTN 2.0.1 messages:

| Message type-subtype | Description                                         |
|----------------------|-----------------------------------------------------|
| SM 0-0               | GPS orbit, clock, bias (OCB)                        |
| SM 0-1               | GLONASS orbit, clock, bias (OCB)                    |
| SM 0-2               | Galileo orbit, clock, bias (OCB)                    |
| SM 0-3               | BeiDou orbit, clock, bias (OCB)                     |
| SM 1-0               | GPS high-precision atmosphere correction (HPAC)     |
| SM 1-1               | GLONASS high-precision atmosphere correction (HPAC) |
| SM 1-2               | Galileo high-precision atmosphere correction (HPAC) |
| SM 1-3               | BeiDou high-precision atmosphere correction (HPAC)  |



| Message type-subtype | Description                      |
|----------------------|----------------------------------|
| SM 2-0               | Geographic area definition (GAD) |

**Table 9: Supported input SPARTN version 2.0.1 messages**

#### <span id="page-7-0"></span>**1.4.4 Centimeter level augmentation service (CLAS)**

Operating as a rover, NEO-F9P-15B can receive UBX-RXM-QZSSL6 message from a NEO-D9C on any communication interface. The message contains QZSS CLAS (centimeter-level augmentation service) corrections. The CLAS protocol provides corrections for in-view GPS, Galileo, and QZSS satellites in Japan.

#### <span id="page-7-1"></span>**1.5 Broadcast navigation data and satellite signal measurements**

The NEO-F9P-15B can output all the GNSS broadcast data upon reception from tracked satellites. This includes all the supported GNSS signals as well as the QZSS and SBAS augmentation services. The UBX-RXM-SFRBX message provides this information. For the UBX-RXM-SFRBX message specification, see the Interface description [\[2\]](#page-22-3) for the UBX-RXM-SFRBX message specification. The receiver can provide satellite signal information in a form compatible with the Radio Resource LCS Protocol (RRLP) [[4](#page-22-4)].

#### <span id="page-7-2"></span>**1.5.1 Carrier-phase measurements**

The NEO-F9P-15B modules provide raw carrier-phase data for all supported signals, along with pseudorange, Doppler and measurement quality information. The data contained in the UBX-RXM-RAWX message follows the conventions of a multi-GNSS RINEX 3 observation file. For the UBX-RXM-RAWX message specification, see Interface description [\[2\]](#page-22-3).

Raw measurement data is available once the receiver has established data bit synchronization and time-of-week.

#### <span id="page-7-3"></span>**1.6 Supported protocols**

NEO-F9P-15B supports the following protocols:

| Protocol                                     | Type                                     |
|----------------------------------------------|------------------------------------------|
| UBX                                          | Input/output, binary, u-blox proprietary |
| NMEA 4.11 (default), 4.10, 4.0, 2.3, and 2.1 | Input/output, ASCII                      |
| RTCM 3.3                                     | Input/output, binary                     |
| SPARTN 2.0.1                                 | Input, binary                            |

**Table 10: Supported protocols**

For specification of the protocols, see the Interface description [[2](#page-22-3)].



## <span id="page-8-0"></span>**2 System description**

### <span id="page-8-1"></span>**2.1 Block diagram**



**Figure 1: NEO-F9P-15B block diagram**



## <span id="page-9-0"></span>**3 Pin definition**

### <span id="page-9-1"></span>**3.1 Pin assignment**

The pin assignment of the NEO-F9P-15B module is shown in [Figure](#page-9-2) 2. The defined configuration of the PIOs is listed in [Table](#page-9-3) 11.

<span id="page-9-2"></span>

|  |  | Figure 2: NEO-F9P-15B pin assignment |
|--|--|--------------------------------------|

<span id="page-9-3"></span>

| Pin no. | Name       | I/O | Description                                                      |
|---------|------------|-----|------------------------------------------------------------------|
| 1       | SAFEBOOT_N | I   | SAFEBOOT_N (used for FW updates and reconfiguration, leave open) |
| 2       | D_SEL      | I   | Interface select (open or VCC = UART + I2C; GND = SPI)           |
| 3       | TIMEPULSE  | O   | TIMEPULSE (1 PPS)                                                |
| 4       | EXTINT     | I   | EXTINT (PIO 7)                                                   |
| 5       | USB_DM     | I/O | USB data (DM)                                                    |
| 6       | USB_DP     | I/O | USB data (DP)                                                    |
| 7       | V_USB      | I   | USB supply                                                       |
| 8       | RESET_N    | I   | RESET (active low)                                               |
| 9       | VCC_RF     | O   | Voltage for external LNA                                         |
| 10      | GND        | I   | Ground                                                           |
| 11      | RF_IN      | I   | GNSS signal input                                                |
| 12      | GND        | I   | Ground                                                           |
| 13      | GND        | I   | Ground                                                           |
| 14      | LNA_EN     | O   | Antenna/LNA control                                              |



| Pin no. | Name           | I/O | Description                                                       |
|---------|----------------|-----|-------------------------------------------------------------------|
| 15      | RTK_STAT       | O   | RTK status:                                                       |
|         |                |     | 0 = RTK/PPP-RTK fixed                                             |
|         |                |     | blinking = receiving and using corrections                        |
|         |                |     | 1 = no corrections                                                |
| 16      | TXD2           | O   | UART 2 TXD                                                        |
| 17      | RXD2           | I   | UART 2 RXD                                                        |
| 18      | SDA / SPI CS_N | I/O | I2C data if D_SEL = VCC (or open); SPI chip select if D_SEL = GND |
| 19      | SCL / SPI SLK  | I/O | I2C clock if D_SEL = VCC (or open); SPI clock if D_SEL = GND      |
| 20      | TXD / SPI SDO  | O   | UART1 output if D_SEL = VCC (or open); SPI SDO if D_SEL = GND     |
| 21      | RXD / SPI SDI  | I   | UART1 input if D_SEL = VCC (or open); SPI SDI if D_SEL = GND      |
| 22      | V_BCKP         | I   | Backup voltage supply                                             |
| 23      | VCC            | I   | Supply voltage                                                    |
| 24      | GND            | I   | Ground                                                            |

**Table 11: NEO-F9P-15B pin assignment**

#### <span id="page-10-0"></span>**3.2 Pin states**

[Table](#page-10-1) 12 defines the state of some NEO-F9P-15B pins in different modes. The functions for the NEO-F9P-15B pins are as defined in the default configuration.

<span id="page-10-1"></span>

| Pin no. | Default function | Continuous mode        | Software backup mode | Safeboot mode          |
|---------|------------------|------------------------|----------------------|------------------------|
| 2       | D_SEL = open     | Input pull-up          | Input pull-up        | Input pull-up          |
|         | D_SEL = GND      | High-Z                 | Input pull-down      | High-Z                 |
| 21      | RXD              | Input pull-up          | Input pull-up        | Input pull-up          |
|         | SPI_SDO          | High-Z                 | Input pull-up        | Input pull-up          |
| 20      | TXD              | Output                 | Input pull-up        | Output                 |
|         | SPI_SDI          | 13<br>Output           | Input pull-up        | 13<br>Output           |
| 18      | SDA              | Input pull-up / Output | Input pull-up        | Input pull-up / Output |
|         | SPI_CS_N         | High-Z                 | High-Z               | High-Z                 |
|         | SCL              | Input pull-up          | Input pull-up        | Input pull-up          |
| 19      | SPI_SLK          | High-Z                 | High-Z               | High-Z                 |
| 3       | TIMEPULSE        | Output                 | Input pull-up        | Output low             |
| 14      | LNA_EN           | Output                 | Input pull-down      | Input pull-up          |
| 15      | RTK_STAT         | Output                 | Input pull-up        | Input pull-up          |
| 1       | SAFEBOOT_N       | Input pull-up          | Input pull-up        | Input pull-up          |
| 4       | EXTINT           | Input pull-up          | Input pull-up        | Input pull-up          |
| 17      | RXD2             | Input pull-up          | Input pull-up        | Input pull-up          |
| 16      | TXD2             | Output                 | Input pull-up        | Output                 |
| 8       | RESET_N          | Input pull-up          | Input pull-up        | Input pull-up          |

**Table 12: NEO-F9P-15B pin states in different operational modes**

<span id="page-10-2"></span><sup>13</sup> If SPI CS = low. Otherwise it is configured as an input pull-up.



## <span id="page-11-0"></span>**4 Electrical specifications**

#### <span id="page-11-1"></span>**4.1 Absolute maximum ratings**

CAUTION. Risk of device damage. Exceeding the absolute maximum ratings may affect the lifetime and reliability of the device or permanently damage it. Do not exceed the absolute maximum ratings.

This product is not protected against overvoltage or reversed voltages. Use appropriate protection to avoid device damage from voltage spikes exceeding the specified boundaries.

| Parameter                    | Symbol            | Condition                                   | Min  | Max           | Units |
|------------------------------|-------------------|---------------------------------------------|------|---------------|-------|
| Power supply voltage         | VCC               |                                             | –0.5 | 3.6           | V     |
| 14<br>Voltage ramp on VCC    |                   |                                             | 20   | 8000          | µs/V  |
| Backup battery voltage       | V_BCKP            |                                             | –0.5 | 3.6           | V     |
| 14<br>Voltage ramp on V_BCKP |                   |                                             | 20   |               | µs/V  |
| Input pin voltage            | Vin               | VCC ≤ 3.1 V                                 | –0.5 | VCC + 0.5     | V     |
|                              |                   | VCC > 3.1 V                                 | –0.5 | 3.6           | V     |
| VCC_RF output current        | ICC_RF            |                                             |      | 300           | mA    |
| Supply voltage USB           | V_USB             |                                             | –0.5 | 3.6           | V     |
| USB signals                  | USB_DM,<br>USB_DP |                                             | –0.5 | V_USB + 0.5 V |       |
| Input power at RF_IN         | Prfin             | source impedance =<br>50 Ω, continuous wave |      | 10            | dBm   |
| Storage temperature          | Tstg              |                                             | –40  | +85           | °C    |
|                              |                   |                                             |      |               |       |

**Table 13: Absolute maximum ratings**

### <span id="page-11-2"></span>**4.2 Operating conditions**

Extreme operating temperatures can significantly impact the specified values. If an application operates near the min or max temperature limits, ensure the specified values are not exceeded.

| Parameter                                    | Symbol   | Min       | Typical | Max | Units | Condition                  |
|----------------------------------------------|----------|-----------|---------|-----|-------|----------------------------|
| Power supply voltage                         | VCC      | 2.7       | 3.0     | 3.6 | V     |                            |
| Backup battery voltage                       | V_BCKP   | 1.65      |         | 3.6 | V     |                            |
| 15, 16<br>Backup battery current             | I_BCKP   |           | 45      |     | µA    | V_BCKP = 3 V,<br>VCC = 0 V |
| 16<br>SW backup current                      | I_SWBCKP |           | 0.8     |     | mA    |                            |
| Input pin voltage range                      | Vin      | 0         |         | VCC | V     |                            |
| Digital IO pin low level input voltage       | Vil      |           |         | 0.4 | V     |                            |
| Digital IO pin high level input voltage      | Vih      | 0.8 * VCC |         |     | V     |                            |
| Digital IO pin low level output voltage      | Vol      |           |         | 0.4 | V     | Iol = 2 mA17               |
| Digital IO pin high level output voltage Voh |          | VCC – 0.4 |         |     | V     | Ioh = 2 mA17               |

<span id="page-11-3"></span><sup>14</sup> Exceeding the ramp speed may permanently damage the device

<span id="page-11-4"></span><sup>15</sup> To measure the I\_BCKP the receiver should first be switched on, i.e. VCC and V\_BCKP is available. Then set VCC to 0 V while the V\_BCKP remains available. Afterward measure the current consumption at the V\_BCKP.

<span id="page-11-5"></span><sup>16</sup> The value has been characterized at 25 °C ambient temperature.

<span id="page-11-6"></span><sup>17</sup> TIMEPULSE has 4 mA current drive/sink capability



| Parameter                                                     | Symbol   | Min | Typical   | Max   | Units | Condition |
|---------------------------------------------------------------|----------|-----|-----------|-------|-------|-----------|
| DC current through any digital I/O pin<br>(except supplies)   | Ipin     |     |           | 5     | mA    |           |
| Pull-up resistance for SCL, SDA                               | Rpu      | 7   | 15        | 30    | kΩ    |           |
| Pull-up resistance for D_SEL, RXD,<br>TXD, SAFEBOOT_N, EXTINT | Rpu      | 30  | 75        | 130   | kΩ    |           |
| Pull-up resistance for RESET_N                                | Rpu      | 7   | 10        | 13    | kΩ    |           |
| Voltage at USB pins                                           | V_USBIO  | 0   |           | V_USB | V     |           |
| VCC_RF voltage                                                | VCC_RF   |     | VCC – 0.1 |       | V     |           |
| VCC_RF output current                                         | ICC_RF   |     |           | 50    | mA    |           |
| 18<br>Receiver chain noise figure                             | NFtot    |     | 3         |       | dB    |           |
| External gain (at RF_IN)                                      | Ext_gain | 0   |           | 30    | dB    |           |
| Operating temperature                                         | Topr     | –40 | +25       | +85   | °C    |           |

**Table 14: Operating conditions**

#### <span id="page-12-0"></span>**4.3 Indicative power requirements**

[Table](#page-12-2) 15 provides examples of typical current requirements when using a cold start command. The given values are total system supply current for a possible application including RF and baseband sections.

All values in [Table](#page-12-2) 15 have been measured at 25 °C ambient temperature.

The actual power requirements vary depending on the FW version used, external circuitry, number of satellites tracked, signal strength, type and time of start, duration, and conditions of test.

<span id="page-12-2"></span>

| Symbol     | Parameter    | Conditions  | GPS+GLO<br>+GAL+BDS | GPS | Unit |
|------------|--------------|-------------|---------------------|-----|------|
| IPEAK      | Peak current | Acquisition | 135                 | 125 | mA   |
| 19<br>IVCC | VCC current  | Acquisition | 98                  | 80  | mA   |
| 19<br>IVCC | VCC current  | Tracking    | 95                  | 78  | mA   |

**Table 15: Currents to calculate the indicative power requirements**

<span id="page-12-1"></span><sup>18</sup> Only valid for GPS

<span id="page-12-3"></span><sup>19</sup> Simulated GNSS signal



## <span id="page-13-0"></span>**5 Communications interfaces**

The NEO-F9P-15B has several communications interfaces [20](#page-13-3) , including UART, SPI, I2C and USB.

All the inputs have internal pull-up resistors in normal operation and can be left open if not used. All the PIOs are supplied by VCC, therefore all the voltage levels of the PIO pins are related to VCC supply voltage.

### <span id="page-13-1"></span>**5.1 UART**

The UART interfaces support configurable baud rates. For further information, see the Integration manual [[1](#page-22-2)].

Hardware flow control is not supported.

The UART1 is enabled if D\_SEL pin of the module is left open or "high".

| Symbol | Parameter              | Min   | Max    | Unit  |
|--------|------------------------|-------|--------|-------|
| Ru     | Baud rate              | 9600  | 921600 | bit/s |
| ΔTx    | Tx baud rate accuracy  | -1%   | +1%    | -     |
| ΔRx    | Rx baud rate tolerance | -2.5% | +2.5%  | -     |

**Table 16: NEO-F9P-15B UART specifications**

### <span id="page-13-2"></span>**5.2 SPI**

The SPI interface is disabled by default. The SPI interface shares pins with UART and I2C and can be selected by setting D\_SEL = 0. The SPI interface can be operated in peripheral mode only. The maximum transfer rate using SPI is 125 kB/s and the maximum SPI clock frequency is 5.5 MHz.

The SPI timing parameters for peripheral operation are defined in [Figure](#page-13-4) 3. Default SPI configuration is CPOL = 0 and CPHA = 0.

<span id="page-13-4"></span>

**Figure 3: NEO-F9P-15B SPI specification mode 1: CPHA=0 SCK = 5.33 MHz**

<span id="page-13-3"></span><sup>20</sup> The signal names and related terms have been replaced with new terminology in this document.

#### NEO-F9P-15B - Data sheet



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

**Table 17: SPI peripheral input timing parameters 1 - 12**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 12  | 40  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 15  | 40  | ns   |
| C      | SDO data hold time                          | 100 | 140 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 0   | 5   | ns   |
| E      | SDO data disable lag time                   | 15  | 35  | ns   |
|        |                                             |     |     |      |

**Table 18: SPI peripheral timing parameters A - E, 2 pF load capacitance**

| Parameter                                   | Min | Max | Unit |
|---------------------------------------------|-----|-----|------|
| SDO data valid time (CS)                    | 16  | 55  | ns   |
| SDO data valid time (SCK), weak driver mode | 20  | 55  | ns   |
| SDO data hold time                          | 100 | 150 | ns   |
| SDO rise/fall time, weak driver mode        | 3   | 20  | ns   |
| SDO data disable lag time                   | 15  | 35  | ns   |
|                                             |     |     |      |

**Table 19: SPI peripheral timing parameters A - E, 20 pF load capacitance**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 26  | 85  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 30  | 85  | ns   |
| C      | SDO data hold time                          | 110 | 160 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 13  | 45  | ns   |
| E      | SDO data disable lag time                   | 15  | 35  | ns   |

**Table 20: SPI peripheral timing parameters A - E, 60 pF load capacitance**

### <span id="page-14-0"></span>**5.3 I2C**

An I2C interface is available for communication with an external host CPU in I2C Fast-mode. Backwards compatibility with Standard-mode I2C bus operation is not supported. The interface can be operated only in peripheral mode with a maximum bit rate of 400 kbit/s. The interface can make use of clock stretching by holding the SCL line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms.





**Figure 4: NEO-F9P-15B I2C peripheral specification**

|         |                                                     | I2C Fast-mode |                     |      |  |
|---------|-----------------------------------------------------|---------------|---------------------|------|--|
| Symbol  | Parameter                                           | Min           | Max                 | Unit |  |
| fSCL    | SCL clock frequency                                 | 0             | 400                 | kHz  |  |
| tHD;STA | Hold time (repeated) START condition                | 0.6           | -                   | µs   |  |
| tLOW    | Low period of the SCL clock                         | 1.3           | -                   | µs   |  |
| tHIGH   | High period of the SCL clock                        | 0.6           | -                   | µs   |  |
| tSU;STA | Setup time for a repeated START condition           | 0.6           | -                   | µs   |  |
| tHD;DAT | Data hold time                                      | 0 21          | 22<br>-             | µs   |  |
| tSU;DAT | Data setup time                                     | 100 23        |                     | ns   |  |
| tr      | Rise time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |  |
| tf      | Fall time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |  |
| tSU;STO | Setup time for STOP condition                       | 0.6           | -                   | µs   |  |
| tBUF    | Bus-free time between a STOP and START<br>condition | 1.3           | -                   | µs   |  |
| tVD;DAT | Data valid time                                     | -             | 0.9 22              | µs   |  |
| tVD;ACK | Data valid acknowledge time                         | -             | 0.9 22              | µs   |  |
| VnL     | Noise margin at the low level                       | 0.1 VCC       | -                   | V    |  |

<span id="page-15-0"></span><sup>21</sup> External device must provide a hold time of at least one transition time (max 300 ns) for the SDA signal (with respect to the min Vih of the SCL signal) to bridge the undefined region of the falling edge of SCL.

<span id="page-15-1"></span><sup>22</sup> The maximum tHD;DAT must be less than the maximum tVD;DAT or tVD;ACK with a maximum of 0.9 µs by a transition time. This maximum must only be met if the device does not stretch the LOW period (tLOW) of the SCL signal. If the clock stretches the SCL, the data must be valid by the set-up time before it releases the clock.

<span id="page-15-2"></span><sup>23</sup> When the I2C peripheral is stretching the clock, the tSU;DAT of the first bit of the next byte is 62.5 ns.





|        |                                | I2C Fast-mode |     |      |
|--------|--------------------------------|---------------|-----|------|
| Symbol | Parameter                      | Min           | Max | Unit |
| VnH    | Noise margin at the high level | 0.2 VCC       | -   | V    |

**Table 21: NEO-F9P-15B I2C peripheral timings and specifications**

The I2C interface is only available with the UART default mode. If the SPI interface is selected by using D\_SEL = 0, the I2C interface is not available.

### <span id="page-16-0"></span>**5.4 USB**

The USB 2.0 FS (full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface. The V\_USB pin supplies the USB interface.

### <span id="page-16-1"></span>**5.5 Default interface settings**

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

#### **Table 22: Default interface settings**

Refer to the applicable Interface description [[2](#page-22-3)] for information about further settings.

- By default, NEO-F9P-15B outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.
- Do not use UART2 as the only one interface to the host. Not all UBX functionality is available on UART2, such as firmware upgrade, safeboot or backup modes functionalities. No start-up boot screen is sent out from UART2.



## <span id="page-17-0"></span>**6 Mechanical specifications**







#### **Figure 5: NEO-F9P-15B mechanical drawing**

| Symbol | Min (mm) | Typical (mm) | Max (mm) |                                                                                         |
|--------|----------|--------------|----------|-----------------------------------------------------------------------------------------|
| A      | 15.9     | 16.0         | 16.1     |                                                                                         |
| B      | 12.1     | 12.2         | 12.4     |                                                                                         |
| C      | 3.40     | 3.58         | 3.76     |                                                                                         |
| D      | 0.9      | 1.0          | 1.1      |                                                                                         |
| E      | 1.0      | 1.1          | 1.2      |                                                                                         |
| F      | 2.9      | 3.0          | 3.1      |                                                                                         |
| G      | 0.9      | 1.0          | 1.1      |                                                                                         |
| H1     | 1.22     | 1.32         | 1.42     |                                                                                         |
| H2     | 0.6      | 0.7          | 0.8      |                                                                                         |
| K      | 0.7      | 0.8          | 0.9      |                                                                                         |
| M      | 0.8      | 0.9          | 1.0      |                                                                                         |
| N      | 0.4      | 0.5          | 0.6      |                                                                                         |
| P*     | 0.0      | -            | 0.5      | There are 2 de-paneling residual tabs on the left<br>and 1 on the right, or vice versa. |
| Weight |          | 1.25 g       |          |                                                                                         |

**Table 23: NEO-F9P-15B mechanical dimensions**



The mechanical picture of the de-paneling residual tabs (P\*) is an approximate representation. The shape and position may vary.

Take the size of the de-paneling residual tabs into account when designing the component keepout area.



## <span id="page-19-0"></span>**7 Qualifications and approvals**

| Quality and reliability                   |                                                                                      |  |
|-------------------------------------------|--------------------------------------------------------------------------------------|--|
| Product qualification                     | Qualified according to u-blox qualification policy, based on a subset of AEC<br>Q104 |  |
| Chip qualification                        | Modules are based on AEC-Q100 qualified GNSS chips                                   |  |
| Manufacturing                             | Manufactured at ISO/TS 16949 certified sites                                         |  |
| Environmental                             |                                                                                      |  |
| RoHS compliance                           | Yes                                                                                  |  |
| 24 25<br>Moisture sensitivity level (MSL) | 4                                                                                    |  |
| Type approvals                            |                                                                                      |  |
| European RED certification (CE)           | Declaration of Conformity (DoC) is available on the u-blox website.                  |  |
| UK conformity assessment (UKCA)           | Yes                                                                                  |  |
|                                           |                                                                                      |  |

**Table 24: Qualifications and approvals**

<span id="page-19-1"></span><sup>24</sup> For the MSL standard, see IPC/JEDEC J-STD-020 and J-STD-033, available on [www.jedec.org](https://www.jedec.org/)

<span id="page-19-2"></span><sup>25</sup> For more information regarding moisture sensitivity levels, labelling, storage and drying, see the Product packaging reference guide [\[3](#page-22-5)]



## <span id="page-20-0"></span>**8 Labeling and ordering information**

This section provides information about product labeling and ordering. For information about product handling and soldering, see the Integration manual [[1](#page-22-2)].

#### <span id="page-20-1"></span>**8.1 Product labeling**

The labeling of the NEO-F9P-15B modules provides product information and revision information. For more information, contact u-blox sales.



**Figure 6: Example of NEO-F9P-15B label**

### <span id="page-20-2"></span>**8.2 Explanation of product codes**

Three product code formats are used in the NEO-F9P-15B labels. The **Product name** used in documentation such as this data sheet identifies all u-blox products, independent of packaging and quality grade. The **Ordering code** includes options and quality, while the **Type number** includes the hardware and firmware versions.

[Table](#page-20-3) 25 below details these three formats.

<span id="page-20-3"></span>

| Format        | Structure      | Product code   |  |
|---------------|----------------|----------------|--|
| Product name  | PPP-TGV        | NEO-F9P        |  |
| Ordering code | PPP-TGV-NNQ    | NEO-F9P-15B    |  |
| Type number   | PPP-TGV-NNQ-XX | NEO-F9P-15B-00 |  |

#### **Table 25: Product code formats**

The parts of the product code are explained in [Table](#page-20-4) 26.

<span id="page-20-4"></span>

| Code | Meaning                | Example                                    |
|------|------------------------|--------------------------------------------|
| PPP  | Product family         | NEO                                        |
| TG   | Platform               | F9 = u-blox F9                             |
| V    | Variant                | P = High precision                         |
| NNQ  | Option / Quality grade | NN: Option [0099]                          |
|      |                        | Q: Grade, A = Automotive, B = Professional |
| XX   | Product detail         | Describes hardware and firmware versions   |
|      |                        |                                            |

**Table 26: Part identification code**



#### <span id="page-21-0"></span>**8.3 Ordering codes**

| Ordering code | Product | Remark                                         |
|---------------|---------|------------------------------------------------|
| NEO-F9P-15B   | NEO-F9P | Shipped with firmware FW 1.00 HPG L1L5<br>1.40 |

#### **Table 27: Product ordering codes**

Product changes affecting form, fit or function are documented by u-blox. For a list of Product Change Notifications (PCNs) see our website at: <https://www.u-blox.com/en/product-resources>.



## <span id="page-22-0"></span>**Related documents**

- <span id="page-22-2"></span>**[1]** NEO-F9P Integration manual [UBX-22028362](https://www.u-blox.com/docs/UBX-22028362)
- <span id="page-22-3"></span>**[2]** HPG L1L5 1.40 Interface description [UBX-23006991](https://www.u-blox.com/docs/UBX-23006991)
- <span id="page-22-5"></span>**[3]** Product packaging reference guide [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-22-4"></span>**[4]** Radio Resource LCS Protocol (RRLP), (3GPP TS 44.031 version 11.0.0 Release 11)
- <span id="page-22-1"></span>**[5]** GPS L5 configuration, Application note, [UBX-21038688](https://www.u-blox.com/docs/UBX-21038688)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



## <span id="page-23-0"></span>**Revision history**

| Revision | Date        | Status / comments                                                                                                                            |
|----------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 14-Oct-2022 | Objective specification                                                                                                                      |
| R02      | 21-Jun-2023 | Advance information                                                                                                                          |
| R03      | 19-Sep-2023 | Early production information<br>Update in mechanical dimensions table and the performance section                                            |
| R04      | 06-Jun-2024 | Mass production<br>Change in document structure<br>•<br>Moisture sensitivity level (MSL) is included in chapter Qualifications and approvals |



## **Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).