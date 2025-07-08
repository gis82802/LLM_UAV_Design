

# **ZED-F9H-01B**

## **Module for heading applications Professional grade**

**Data sheet**



#### **Abstract**

This data sheet describes the ZED-F9H module for heading applications. The ZED-F9H module is designed to provide best possible heading information to applications where precise attitude is of greatest importance. It is suitable for UAV, trucks, heavy vehicles and antenna alignment applications and provides heading accuracy independent of vehicle motion and calibration.

**www.u-blox.com**



UBX-21025012 - R05 C1-Public



## **Document information**

| Title                  | ZED-F9H-01B                     |             |  |
|------------------------|---------------------------------|-------------|--|
| Subtitle               | Module for heading applications |             |  |
| Document type          | Data sheet                      |             |  |
| Document number        | UBX-21025012                    |             |  |
| Revision and date      | R05                             | 21-Mar-2024 |  |
| Disclosure restriction | C1-Public                       |             |  |

| Product status                   | Corresponding content status |                                                                                           |
|----------------------------------|------------------------------|-------------------------------------------------------------------------------------------|
| Functional sample                | Draft                        | For functional testing. Revised and supplementary data will be published<br>later.        |
| In development /<br>prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                    |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be<br>published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be<br>published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                        |

This document applies to the following products:

| Product name | Type number    | FW version | IN/PCN reference | Product status  |
|--------------|----------------|------------|------------------|-----------------|
| ZED-F9H      | ZED-F9H-01B-00 | HDG 1.13   | UBX-23000084     | Mass production |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2024, u-blox AG.



| 1 Functional<br>description                                       | 4  |
|-------------------------------------------------------------------|----|
| 1.1 Overview 4                                                    |    |
| 1.2 Performance 4                                                 |    |
| 1.3 Supported GNSS constellations5                                |    |
| 1.4 Supported GNSS augmentation systems 6                         |    |
| 1.4.1 Quasi-Zenith Satellite System (QZSS)6                       |    |
| 1.4.2 Satellite-based augmentation system (SBAS)6                 |    |
| 1.4.3 Differential GNSS (DGNSS)6                                  |    |
| 1.5 Broadcast navigation data and satellite signal measurements 7 |    |
| 1.6 Supported protocols7                                          |    |
| 2 System<br>description8                                          |    |
| 2.1 Block diagram 8                                               |    |
| 3 Pin<br>definition                                               | 9  |
| 3.1 Pin assignment9                                               |    |
| 4 Electrical<br>specification                                     | 12 |
| 4.1 Absolute maximum ratings12                                    |    |
| 4.2 Operating conditions12                                        |    |
| 4.3 Indicative power requirements13                               |    |
| 5 Communications<br>interfaces14                                  |    |
| 5.1 UART14                                                        |    |
| 5.2 SPI 14                                                        |    |
| 5.3 I2C 15                                                        |    |
| 5.4 USB 17                                                        |    |
| 5.5 Default interface settings17                                  |    |
| 6 Mechanical specification                                        | 18 |
| 7 Qualifications<br>and<br>approvals20                            |    |
| 8 Labeling<br>and<br>ordering<br>information21                    |    |
| 8.1 Product labeling 21                                           |    |
| 8.2 Explanation of product codes 21                               |    |
| 8.3 Ordering codes 21                                             |    |
| Related<br>documents                                              | 22 |
| Revision<br>history23                                             |    |



## <span id="page-3-0"></span>**1 Functional description**

### <span id="page-3-1"></span>**1.1 Overview**

The ZED-F9H-01B positioning module features the u-blox F9 receiver platform, which provides multi-band GNSS to high-volume industrial applications. The ZED-F9H-01B has integrated ublox multi-band moving-base RTK technology for high GNSS-based heading accuracy. The ZED-F9H-01Bcan only be used in combination with a ZED-F9Pbase in amoving base with afixed baseline application to derive accurate heading information.

No absolute position information is output in any UBX or NMEA message.

Moving base allows both base and rover to move while computing a centimeter-level accurate position between them. It is well suited to attitude-sensing applications where both base and rover modules are mounted on the same moving platform and the relative position is used to derive attitude information for the platform.

See the ZED-F9P Moving Base application note [[5](#page-21-1)] for more information on designing in and using moving base.

### <span id="page-3-2"></span>**1.2 Performance**

| Parameter                           | Specification                           |                                     |  |
|-------------------------------------|-----------------------------------------|-------------------------------------|--|
| Receiver type                       | Multi-band GNSS high precision receiver |                                     |  |
| Frequency of time pulse signal      |                                         | 0.25 Hz to 10 MHz<br>(configurable) |  |
| 1<br>Operational limits             | Dynamics                                | ≤ 4 g                               |  |
|                                     | Altitude                                | 80,000 m                            |  |
|                                     | Velocity                                | 500 m/s                             |  |
| 2<br>Velocity accuracy              |                                         | 0.05 m/s                            |  |
| 2<br>Dynamic heading accuracy       |                                         | 0.3 deg                             |  |
| Table 1: ZED-F9H-01B specifications |                                         |                                     |  |

| GNSS3            |                  | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS  |
|------------------|------------------|-----------------|-------------|---------|---------|---------|------|
| 4<br>Acquisition | Cold start       | 25 s            | 25 s        | 30 s    | 26 s    | 28 s    | 30 s |
|                  | Hot start        | 2 s             | 2 s         | 2 s     | 2 s     | 2 s     | 2 s  |
|                  | 5<br>Aided start | 2 s             | 2 s         | 2 s     | 2 s     | 2 s     | 2 s  |

**Table 2: ZED-F9H-01B performance in different GNSS modes**

<span id="page-3-3"></span><sup>1</sup> Assuming Airborne 4 g platform

<span id="page-3-4"></span><sup>2</sup> 50% at 30 m/s for dynamic operation

<span id="page-3-5"></span><sup>3</sup> GPS used in combination with QZSS and SBAS

<span id="page-3-6"></span><sup>4</sup> Commanded starts. All satellites at -130 dBm. Measured at room temperature.

<span id="page-3-7"></span><sup>5</sup> Dependent on the speed and latency of the aiding data connection, commanded starts



| GNSS3            |                   | GPS+GLO+GAL+BDS |
|------------------|-------------------|-----------------|
| 6<br>Sensitivity | Tracking and nav. | -167 dBm        |
|                  | Reacquisition     | -160 dBm        |
|                  | Cold start        | -148 dBm        |
|                  | Hot start         | -157 dBm        |

**Table 3: ZED-F9H-01B sensitivity**

| GNSS                          | GPS+GLO+GAL+BDS | GPS+GLO+GAL | GPS+GAL | GPS+GLO | GPS+BDS | GPS     |
|-------------------------------|-----------------|-------------|---------|---------|---------|---------|
| Max navigation<br>update rate | 8 Hz            | 8 Hz        | 10 Hz   | 10 Hz   | 10 Hz   | 10 Hz   |
| Convergence<br>time7          | < 10 s          | < 10 s      | < 10 s  | < 10 s  | < 10 s  | < 30 s  |
| Heading accuracy              | 0.4 deg         | 0.4 deg     | 0.4 deg | 0.4 deg | 0.4 deg | 0.4 deg |

**Table 4: ZED-F9H-01B moving base RTK performance in different GNSS modes**



**Figure 1: ZED-F9H-01B moving base RTK heading accuracy versus baseline length**

In a moving base application, and especially when the antennas are mounted on the same platform, it is recommended to use identical antennas. Furthermore it is recommended these antennas are mounted with identical orientation, as this will minimize effects of phase center variation.

### <span id="page-4-0"></span>**1.3 Supported GNSS constellations**

The ZED-F9H-01B GNSS modules are concurrent GNSS receivers that can receive and track multiple GNSS constellations. Owing to the multi-band RF front-end architecture, all four major GNSS constellations (GPS, GLONASS, Galileo and BeiDou) plus SBAS and QZSS satellites can be

<span id="page-4-1"></span><sup>6</sup> Demonstrated with a good external LNA. Measured at room temperature.

<span id="page-4-2"></span><sup>7</sup> Depends on atmospheric conditions, baseline length, GNSS antenna, multipath conditions, satellite visibility and geometry



received concurrently. All satellites in view can be processed to derive accurate heading information when used with correction data. If power consumption is a key factor, the receiver can be configured for a subset of GNSS constellations.

The QZSS system shares the same frequency bands with GPS and can only be processed in conjunction with GPS.

To benefit from multi-band signal reception, dedicated hardware preparation must be made during the design-in phase. See the Integration manual [[1](#page-21-2)] for u-blox design recommendations.

The ZED-F9H-01B supports the GNSS and their signals as shown in [Table](#page-5-4) 5.

<span id="page-5-4"></span>

| GPS / QZSS                            | GLONASS                                     | Galileo                                  | BeiDou             | NavIC |
|---------------------------------------|---------------------------------------------|------------------------------------------|--------------------|-------|
| L1C/A (1575.420 MHz) L1OF (1602 MHz + | k*562.5 kHz, k = –7,,6)                     | E1-B/C (1575.420 MHz) B1I (1561.098 MHz) |                    | -     |
| L2C (1227.600 MHz)                    | L2OF (1246 MHz +<br>k*437.5 kHz, k = –7,,6) | E5b (1207.140 MHz)                       | B2I (1207.140 MHz) | -     |

**Table 5: Supported GNSS signals on ZED-F9H-01B**

The ZED-F9H-01B can use the u-blox AssistNow™ Online service which provides GNSS assistance information.

### <span id="page-5-0"></span>**1.4 Supported GNSS augmentation systems**

#### <span id="page-5-1"></span>**1.4.1 Quasi-Zenith Satellite System (QZSS)**

The Quasi-Zenith Satellite System (QZSS) is a regional navigation satellite system that provides positioning services for the Pacific region covering Japan and Australia. The ZED-F9H-01B is able to receive and track QZSS L1 C/A and L2C signals concurrently with GPS signals, resulting in better availability especially under challenging signal conditions, e.g. in urban canyons.

The ZED-F9H-01B is also able to receive the QZSS L1S signal in order to use the SLAS (Sub-meter Level Augmentation Service) which is an augmentation technology that provides correction data for pseudoranges. Ground monitoring stations positioned in Japan calculate separate corrections for each visible satellite and broadcast this data to the user via QZSS satellites. The correction stream is transmitted on the L1 frequency (1575.42 MHz).

QZSS can be enabled only if GPS operation is also configured.

#### <span id="page-5-2"></span>**1.4.2 Satellite-based augmentation system (SBAS)**

The ZED-F9H-01B supports SBAS (including WAAS in the US, EGNOS in Europe, L1Sb(QZSS SBAS) in Japan and GAGAN in India) to deliver improved location accuracy within the regions covered. However, the additional inter-standard time calibration step used during SBAS reception results in degraded time accuracy overall.

### <span id="page-5-3"></span>**1.4.3 Differential GNSS (DGNSS)**

A ZED-F9H-01B operating in moving base rover mode can decode the following RTCM messages provided by a ZED-F9P moving base:

| Message type | Description  |  |
|--------------|--------------|--|
| RTCM 1074    | GPS MSM4     |  |
| RTCM 1077    | GPS MSM7     |  |
| RTCM 1084    | GLONASS MSM4 |  |



| Message type | Description                                             |
|--------------|---------------------------------------------------------|
| RTCM 1087    | GLONASS MSM7                                            |
| RTCM 1094    | Galileo MSM4                                            |
| RTCM 1097    | Galileo MSM7                                            |
| RTCM 1124    | BeiDou MSM4                                             |
| RTCM 1127    | BeiDou MSM7                                             |
| RTCM 1230    | GLONASS code-phase biases                               |
| RTCM 4072.0  | Reference station PVT (u-blox proprietary RTCM Message) |

**Table 6: Supported ZED-F9H input RTCM messages**

### <span id="page-6-0"></span>**1.5 Broadcast navigation data and satellite signal measurements**

The ZED-F9H-01B can output all the GNSS broadcast data upon reception from tracked satellites. This includes all the supported GNSS signals as well as the QZSS and SBAS augmentation services. The UBX-RXM-SFRBX message provides this information, see the Interface description [\[2\]](#page-21-3) for the UBX-RXM-SFRBX message specification. The receiver can provide satellite signal information in a form compatible with the Radio Resource LCS Protocol (RRLP) [\[4\]](#page-21-4).

### <span id="page-6-1"></span>**1.6 Supported protocols**

The ZED-F9H-01B supports the following protocols:

| Protocol                                     | Type                                     |
|----------------------------------------------|------------------------------------------|
| UBX                                          | Input/output, binary, u-blox proprietary |
| NMEA 4.11, 4.10 (default), 4.0, 2.3, and 2.1 | Input/output, ASCII                      |
| RTCM 3.3                                     | Input, binary                            |

**Table 7: Supported protocols**

For specification of the protocols, see the Interface description [[2](#page-21-3)].



## <span id="page-7-0"></span>**2 System description**

### <span id="page-7-1"></span>**2.1 Block diagram**



#### **Figure 2: ZED-F9H-01B block diagram**

An active antenna is mandatory with the ZED-F9H-01B. For more information, see the Integration manual [\[1\]](#page-21-2).



## <span id="page-8-0"></span>**3 Pin definition**

### <span id="page-8-1"></span>**3.1 Pin assignment**

The pin assignment of the ZED-F9H-01B module is shown in [Figure](#page-8-2) 3. The defined configuration of the PIOs is listed in [Table](#page-8-3) 8.

For detailed information on pin functions and characteristics, see the Integration manual [[1](#page-21-2)].

The ZED-F9H-01B is an LGA package with the I/O on the outside edge and central ground pads.

<span id="page-8-2"></span>

#### **Figure 3: ZED-F9H-01B pin assignment**

<span id="page-8-3"></span>

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
|         |                |     | 0 = RTK fixed                                                            |
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

**Table 8: ZED-F9H-01B pin assignment**



## <span id="page-11-0"></span>**4 Electrical specification**

### <span id="page-11-1"></span>**4.1 Absolute maximum ratings**

- CAUTION. Risk of device damage. Exceeding the absolute maximum ratings may affect the lifetime and reliability of the device or permanently damage it. Do not exceed the absolute maximum ratings.
- This product is not protected against overvoltage or reversed voltages. Use appropriate protection to avoid device damage from voltage spikes exceeding the specified boundaries.

| Parameter                   | Symbol            | Condition                                   | Min  | Max           | Units |
|-----------------------------|-------------------|---------------------------------------------|------|---------------|-------|
| Power supply voltage        | VCC               |                                             | -0.5 | 3.6           | V     |
| 8<br>Voltage ramp on VCC    |                   |                                             | 20   | 8000          | µs/V  |
| Backup battery voltage      | V_BCKP            |                                             | -0.5 | 3.6           | V     |
| 8<br>Voltage ramp on V_BCKP |                   |                                             | 20   |               | µs/V  |
| Input pin voltage           | Vin               | VCC ≤ 3.1 V                                 | -0.5 | VCC + 0.5     | V     |
|                             |                   | VCC > 3.1 V                                 | -0.5 | 3.6           | V     |
| VCC_RF output current       | ICC_RF            |                                             |      | 200           | mA    |
| Supply voltage USB          | V_USB             |                                             | –0.5 | 3.6           | V     |
| USB signals                 | USB_DM,<br>USB_DP |                                             | -0.5 | V_USB + 0.5 V |       |
| Input power at RF_IN        | Prfin             | source impedance =<br>50 Ω, continuous wave |      | 10            | dBm   |
| Storage temperature         | Tstg              |                                             | -40  | +85           | °C    |
|                             |                   |                                             |      |               |       |

**Table 9: Absolute maximum ratings**

### <span id="page-11-2"></span>**4.2 Operating conditions**

Extreme operating temperatures can significantly impact the specified values. If an application operates near the min or max temperature limits, ensure the specified values are not exceeded.

| Parameter                                    | Symbol   | Min       | Typical | Max | Units | Condition                  |
|----------------------------------------------|----------|-----------|---------|-----|-------|----------------------------|
| Power supply voltage                         | VCC      | 2.7       | 3.0     | 3.6 | V     |                            |
| Backup battery voltage                       | V_BCKP   | 1.65      |         | 3.6 | V     |                            |
| 9, 10<br>Backup battery current              | I_BCKP   |           | 45      |     | µA    | V_BCKP = 3 V,<br>VCC = 0 V |
| 10<br>SW backup current                      | I_SWBCKP |           | 1.4     |     | mA    |                            |
| Input pin voltage range                      | Vin      | 0         |         | VCC | V     |                            |
| Digital IO pin low level input voltage       | Vil      |           |         | 0.4 | V     |                            |
| Digital IO pin high level input voltage      | Vih      | 0.8 * VCC |         |     | V     |                            |
| Digital IO pin low level output voltage      | Vol      |           |         | 0.4 | V     | Iol = 2 mA11               |
| Digital IO pin high level output voltage Voh |          | VCC – 0.4 |         |     | V     | Ioh = 2 mA11               |

<span id="page-11-3"></span><sup>8</sup> Exceeding the ramp speed may permanently damage the device

<span id="page-11-4"></span><sup>9</sup> To measure the I\_BCKP the receiver should first be switched on, i.e. VCC and V\_BCKP is available. Then set VCC to 0 V while the V\_BCKP remains available. Afterward measure the current consumption at the V\_BCKP.

<span id="page-11-5"></span><sup>10</sup> The value has been characterized at 25 °C ambient temperature.

<span id="page-11-6"></span><sup>11</sup> TIMEPULSE has 4 mA current drive/sink capability



| Parameter                                                   | Symbol   | Min | Typical   | Max | Units | Condition |
|-------------------------------------------------------------|----------|-----|-----------|-----|-------|-----------|
| DC current through any digital I/O pin<br>(except supplies) | Ipin     |     |           | 5   | mA    |           |
| VCC_RF voltage                                              | VCC_RF   |     | VCC - 0.1 |     | V     |           |
| VCC_RF output current                                       | ICC_RF   |     |           | 50  | mA    |           |
| 12<br>Receiver chain noise figure                           | NFtot    |     | 9.5       |     | dB    |           |
| External gain (at RF_IN)                                    | Ext_gain | 17  |           | 50  | dB    |           |
| Operating temperature                                       | Topr     | -40 | +25       | +85 | °C    |           |

**Table 10: Operating conditions**

### <span id="page-12-0"></span>**4.3 Indicative power requirements**

[Table](#page-12-2) 11 provides examples of typical current requirements when using a cold start command. The given values are total system supply current for a possible application including RF and baseband sections.

All values in [Table](#page-12-2) 11 have been measured at 25 °C ambient temperature.

The actual power requirements vary depending on the FW version used, external circuitry, number of satellites tracked, signal strength, type and time of start, duration, and conditions of test.

<span id="page-12-2"></span>

| Symbol     | Parameter    | Conditions  | GPS+GLO<br>+GAL+BDS | GPS | Unit |
|------------|--------------|-------------|---------------------|-----|------|
| IPEAK      | Peak current | Acquisition | 130                 | 120 | mA   |
| 13<br>IVCC | VCC current  | Acquisition | 90                  | 75  | mA   |
| 13<br>IVCC | VCC current  | Tracking    | 85                  | 70  | mA   |

**Table 11: Currents to calculate the indicative power requirements**

<span id="page-12-1"></span><sup>12</sup> Only valid for GPS

<span id="page-12-3"></span><sup>13</sup> Simulated GNSS signal

## <span id="page-13-0"></span>**5 Communications interfaces**

The ZED-F9H-01B has several communications interfaces [14](#page-13-3) , including UART, SPI, I2C and USB.

All the inputs have internal pull-up resistors in normal operation and can be left open if not used. All the PIOs are supplied by VCC, therefore all the voltage levels of the PIO pins are related to VCC supply voltage.

### <span id="page-13-1"></span>**5.1 UART**

The UART interfaces support configurable baud rates. See the Integration manual [\[1\]](#page-21-2).

Hardware flow control is not supported.

The UART1 is enabled if D\_SEL pin of the module is left open or "high".

| Symbol | Parameter              | Min   | Max    | Unit  |
|--------|------------------------|-------|--------|-------|
| Ru     | Baud rate              | 9600  | 921600 | bit/s |
| ΔTx    | Tx baud rate accuracy  | -1%   | +1%    | -     |
| ΔRx    | Rx baud rate tolerance | -2.5% | +2.5%  | -     |

**Table 12: ZED-F9H-01B UART specifications**

### <span id="page-13-2"></span>**5.2 SPI**

The SPI interface is disabled by default. The SPI interface shares pins with UART and I2C and can be selected by setting D\_SEL = 0. The SPI interface can be operated in peripheral mode only. The maximum transfer rate using SPI is 125 kB/s and the maximum SPI clock frequency is 5.5 MHz.

The SPI timing parameters for peripheral operation are defined in [Figure](#page-13-4) 4. Default SPI configuration is CPOL = 0 and CPHA = 0.

<span id="page-13-4"></span>



<span id="page-13-3"></span><sup>14</sup> The signal names and related terms have been replaced with new terminology in this document.

#### ZED-F9H-01B - Data sheet



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

**Table 13: SPI peripheral input timing parameters 1 - 12**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 12  | 40  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 15  | 40  | ns   |
| C      | SDO data hold time                          | 100 | 140 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 0   | 5   | ns   |
| E      | SDO data disable lag time                   | 15  | 35  | ns   |
|        |                                             |     |     |      |

**Table 14: SPI peripheral timing parameters A - E, 2 pF load capacitance**

| Parameter                                   | Min | Max | Unit |
|---------------------------------------------|-----|-----|------|
| SDO data valid time (CS)                    | 16  | 55  | ns   |
| SDO data valid time (SCK), weak driver mode | 20  | 55  | ns   |
| SDO data hold time                          | 100 | 150 | ns   |
| SDO rise/fall time, weak driver mode        | 3   | 20  | ns   |
| SDO data disable lag time                   | 15  | 35  | ns   |
|                                             |     |     |      |

**Table 15: SPI peripheral timing parameters A - E, 20 pF load capacitance**

| Symbol | Parameter                                   | Min | Max | Unit |
|--------|---------------------------------------------|-----|-----|------|
| A      | SDO data valid time (CS)                    | 26  | 85  | ns   |
| B      | SDO data valid time (SCK), weak driver mode | 30  | 85  | ns   |
| C      | SDO data hold time                          | 110 | 160 | ns   |
| D      | SDO rise/fall time, weak driver mode        | 13  | 45  | ns   |
| E      | SDO data disable lag time                   | 15  | 35  | ns   |

**Table 16: SPI peripheral timing parameters A - E, 60 pF load capacitance**

### <span id="page-14-0"></span>**5.3 I2C**

An I2C interface is available for communication with an external host CPU in I2C Fast-mode. Backwards compatibility with Standard-mode I2C bus operation is not supported. The interface can be operated only in peripheral mode with a maximum bit rate of 400 kbit/s. The interface can make use of clock stretching by holding the SCL line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms.





#### **Figure 5: ZED-F9H-01B I2C peripheral specification**

|                                                     | I2C Fast-mode |                     |      |
|-----------------------------------------------------|---------------|---------------------|------|
| Parameter                                           | Min           | Max                 | Unit |
| SCL clock frequency                                 | 0             | 400                 | kHz  |
| Hold time (repeated) START condition                | 0.6           | -                   | µs   |
| Low period of the SCL clock                         | 1.3           | -                   | µs   |
| High period of the SCL clock                        | 0.6           | -                   | µs   |
| Setup time for a repeated START condition           | 0.6           | -                   | µs   |
| Data hold time                                      | 0 15          | 16<br>-             | µs   |
| Data setup time                                     | 100 17        |                     | ns   |
| Rise time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| Fall time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| Setup time for STOP condition                       | 0.6           | -                   | µs   |
| Bus-free time between a STOP and START<br>condition | 1.3           | -                   | µs   |
| Data valid time                                     | -             | 0.9 16              | µs   |
| Data valid acknowledge time                         | -             | 0.9 16              | µs   |
| Noise margin at the low level                       | 0.1 VCC       | -                   | V    |
| Noise margin at the high level                      | 0.2 VCC       | -                   | V    |
|                                                     |               |                     |      |

**Table 17: ZED-F9H-01B I2C peripheral timings and specifications**

<span id="page-15-0"></span><sup>15</sup> External device must provide a hold time of at least one transition time (max 300 ns) for the SDA signal (with respect to the min Vih of the SCL signal) to bridge the undefined region of the falling edge of SCL.

<span id="page-15-1"></span><sup>16</sup> The maximum tHD;DAT must be less than the maximum tVD;DAT or tVD;ACK with a maximum of 0.9 µs by a transition time. This maximum must only be met if the device does not stretch the LOW period (tLOW) of the SCL signal. If the clock stretches the SCL, the data must be valid by the set-up time before it releases the clock.

<span id="page-15-2"></span><sup>17</sup> When the I2C peripheral is stretching the clock, the tSU;DAT of the first bit of the next byte is 62.5 ns.



The I2C interface is only available with the UART default mode. If the SPI interface is selected by using D\_SEL = 0, the I2C interface is not available.

### <span id="page-16-0"></span>**5.4 USB**

The USB 2.0 FS (full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface. The V\_USB pin supplies the USB interface.

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

### <span id="page-16-1"></span>**5.5 Default interface settings**

#### **Table 18: Default interface settings**

Refer to the applicable Interface description [[2](#page-21-3)] for information about further settings.

By default, the ZED-F9H-01B outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.



## <span id="page-17-0"></span>**6 Mechanical specification**







#### **Figure 6: ZED-F9H-01B mechanical drawing**

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

#### **Table 19: ZED-F9H-01B mechanical dimensions**

The mechanical picture of the de-paneling residual tabs (L) is an approximate representation. The shape and position may vary.

Take the size of the de-paneling residual tabs into account when designing the component keepout area.



## <span id="page-19-0"></span>**7 Qualifications and approvals**

| Quality and reliability                   |                                                                     |
|-------------------------------------------|---------------------------------------------------------------------|
| Product qualification                     | Qualified according to ISO 16750                                    |
| Chip qualification                        | Modules are based on AEC-Q100 qualified GNSS chips                  |
| Manufacturing                             | Manufactured at ISO/TS 16949 certified sites                        |
| Environmental                             |                                                                     |
| RoHS compliance                           | Yes                                                                 |
| 18 19<br>Moisture sensitivity level (MSL) | 4                                                                   |
| Type approvals                            |                                                                     |
| European RED certification (CE)           | Declaration of Conformity (DoC) is available on the u-blox website. |
| UK conformity assessment (UKCA)           | Yes                                                                 |
|                                           |                                                                     |

**Table 20: Qualifications and approvals**

<span id="page-19-1"></span><sup>18</sup> For the MSL standard, see IPC/JEDEC J-STD-020 and J-STD-033, available on [www.jedec.org](https://www.jedec.org/)

<span id="page-19-2"></span><sup>19</sup> For more information regarding moisture sensitivity levels, labelling, storage and drying, see the Product packaging reference guide [\[3](#page-21-5)]



## <span id="page-20-0"></span>**8 Labeling and ordering information**

This section provides information about product labeling and ordering. For information about moisture sensitivity level (MSL), product handling and soldering see the Integration manual [[1\]](#page-21-2).

### <span id="page-20-1"></span>**8.1 Product labeling**

The labeling of the ZED-F9H-01B modules provides product information and revision information. For more information contact u-blox sales.

### <span id="page-20-2"></span>**8.2 Explanation of product codes**

Three product code formats are used in the ZED-F9H-01B labels. The **Product name** used in documentation such as this data sheet identifies all u-blox products, independent of packaging and quality grade. The **Ordering code** includes options and quality, while the **Type number** includes the hardware and firmware versions.

<span id="page-20-4"></span>

| Format        | Structure      | Product code   |  |
|---------------|----------------|----------------|--|
| Product name  | PPP-TGV        | ZED-F9H        |  |
| Ordering code | PPP-TGV-NNQ    | ZED-F9H-01B    |  |
| Type number   | PPP-TGV-NNQ-XX | ZED-F9H-01B-00 |  |

[Table](#page-20-4) 21 below details these three formats.

**Table 21: Product code formats**

The parts of the product code are explained in [Table](#page-20-5) 22.

<span id="page-20-5"></span>

| Code | Meaning                | Example                                                         |
|------|------------------------|-----------------------------------------------------------------|
| PPP  | Product family         | ZED                                                             |
| TG   | Platform               | F9 = u-blox F9                                                  |
| V    | Variant                | H = Heading                                                     |
| NNQ  | Option / Quality grade | NN: Option [0099]<br>Q: Grade, A = Automotive, B = Professional |
| XX   | Product detail         | Describes hardware and firmware versions                        |

**Table 22: Part identification code**

### <span id="page-20-3"></span>**8.3 Ordering codes**

| Ordering code | Product | Remark                                 |
|---------------|---------|----------------------------------------|
| ZED-F9H-01B   | ZED-F9H | Shipped with firmware FW 1.00 HDG 1.13 |

**Table 23: Product ordering codes**

Product changes affecting form, fit or function are documented by u-blox. For a list of Product Change Notifications (PCNs) see our website at: <https://www.u-blox.com/en/product-resources>.



## <span id="page-21-0"></span>**Related documents**

- <span id="page-21-2"></span>**[1]** ZED-F9H Integration manual [UBX-19030120](https://www.u-blox.com/docs/UBX-19030120)
- <span id="page-21-3"></span>**[2]** HDG 1.13 Interface description [UBX-21025013](https://www.u-blox.com/docs/UBX-21025013)
- <span id="page-21-5"></span>**[3]** Product packaging reference guide [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-21-4"></span>**[4]** Radio Resource LCS Protocol (RRLP), (3GPP TS 44.031 version 11.0.0 Release 11)
- <span id="page-21-1"></span>**[5]** ZED-F9P Moving Base application note, [UBX-19009093](https://www.u-blox.com/docs/UBX-19009093)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



## <span id="page-22-0"></span>**Revision history**

| Revision | Date        | Status / comments                                                                                                                                                                                                                                                                                                                                            |  |
|----------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| R01      | 02-Jun-2020 | Early production information<br>For document legacy revisions see UBX-19027170                                                                                                                                                                                                                                                                               |  |
| R02      | 18-Jun-2021 | Production information                                                                                                                                                                                                                                                                                                                                       |  |
| R03      | 16-Feb-2022 | Voltage ramp on VCC value added in Absolute maximum ratings table. V_BCKP general<br>update. Related documents update                                                                                                                                                                                                                                        |  |
| R04      | 24-Mar-2023 | Updated I2C and SPI timing specifications in section Communications interfaces<br>Updated VCC_RF output current in table Absolute maximum ratings<br>Updated backup current in table Operating conditions<br>Added timepulse footnote in table Operating conditions                                                                                          |  |
| R05      | 21-Mar-2024 | Updated sections:<br>•<br>Performance<br>•<br>Mechanical specifications updated with information on de-paneling residual tabs<br>•<br>Qualifications and approvals<br>•<br>Information on moisture sensitivity level has been moved from the Integration manual<br>to chapter Qualifications and approvals<br>•<br>Editorial changes throughout the document |  |



## **Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).