

# <span id="page-0-0"></span>**ZED-X20P**

## **All-band high precision GNSS module Professional grade**

**Integration manual**



#### **Abstract**

This document describes the ZED-X20P high precision module with all-band GNSS receiver. The module provides all-band RTK with fast convergence times, reliable performance and easy integration of RTK for fast time-to-market. It has a high update rate for highly dynamic applications and centimeter-level accuracy in a small and energy-efficient module.

**www.u-blox.com**



UBXDOC-963802114-12901 - R01 C1-Public



## **Document information**

| Title                  | ZED-X20P                            |             |
|------------------------|-------------------------------------|-------------|
| Subtitle               | All-band high precision GNSS module |             |
| Document type          | Integration manual                  |             |
| Document number        | UBXDOC-963802114-12901              |             |
| Revision and date      | R01                                 | 19-May-2025 |
| Disclosure restriction | C1-Public                           |             |

This document applies to the following products:

| Product name | Type number     | FW version | IN/PCN reference | RN reference               |
|--------------|-----------------|------------|------------------|----------------------------|
| ZED-X20P     | ZED-X20P-00B-00 | HPG 2.00   | -                | UBXDOC-304424225<br>-19895 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents and product statuses, visit www.u-blox.com.

Copyright © 2025, u-blox AG.



| 1 System<br>description6                                         |  |
|------------------------------------------------------------------|--|
| 1.1 Overview 6                                                   |  |
| 1.2 Real time kinematic6                                         |  |
| 1.2.1 RTK modes of operation7                                    |  |
| 1.2.2 PPP-RTK modes of operation 7                               |  |
| 1.2.3 NTRIP - networked transport of RTCM via internet protocol7 |  |
| 1.3 Typical ZED-X20P application setups8                         |  |
| 1.4 Block diagram 9                                              |  |
| 1.5 Pin assignment9                                              |  |
| 2 Receiver<br>configuration12                                    |  |
| 2.1 Storing configuration in different memory layers12           |  |
| 2.2 Basic receiver configuration 12                              |  |
| 2.2.1 Basic hardware configuration12                             |  |
| 2.2.2 Internal LNA mode configuration12                          |  |
| 2.2.3 GNSS signal configuration13                                |  |
| 2.2.4 GPS L5 signal health status configuration 14               |  |
| 2.2.5 Communication interface configuration15                    |  |
| 2.2.6 Message output configuration16                             |  |
| 2.2.7 Antenna supervisor configuration16                         |  |
| 2.3 Navigation configuration17                                   |  |
| 2.3.1 Dynamic platform 17                                        |  |
| 2.3.2 Navigation input filters18                                 |  |
| 2.3.3 Navigation output filters 18                               |  |
| 2.4 RTK configuration19                                          |  |
| 2.4.1 RTCM corrections 19                                        |  |
| 2.4.2 List of supported RTCM input messages20                    |  |
| 2.4.3 List of supported RTCM output messages20                   |  |
| 2.4.4 Rover operation 20                                         |  |
| 2.4.5 Stationary base operation 22                               |  |
| 2.5 PPP-RTK configuration24                                      |  |
| 2.5.1 SPARTN corrections24                                       |  |
| 2.5.2 Multiple SPARTN sources 25                                 |  |
| 2.5.3 Encrypted SPARTN support 26                                |  |
| 2.5.4 Rover operation 27                                         |  |
| 2.6 OTP memory configuration 27                                  |  |
| 3 Receiver<br>functionality28                                    |  |
| 3.1 Augmentation systems28                                       |  |
| 3.1.1 SBAS 28                                                    |  |
| 3.1.2 BeiDou SBAS configuration 29                               |  |
| 3.2 Communication interfaces and PIOs30                          |  |
| 3.2.1 UART30                                                     |  |
| 3.2.2 I2C31                                                      |  |
| 3.2.3 SPI34                                                      |  |
| 3.2.4 Predefined PIOs 35                                         |  |
|                                                                  |  |



| 3.3 Antenna supervisor 37                                                     |  |
|-------------------------------------------------------------------------------|--|
| 3.3.1 Antenna voltage control (ANT_OFF)38                                     |  |
| 3.3.2 Antenna short detection (ANT_SHORT_N) 38                                |  |
| 3.3.3 Antenna short detection auto-recovery38                                 |  |
| 3.3.4 Antenna open circuit detection (ANT_DETECT) 38                          |  |
| 3.3.5 Antenna status reporting 38                                             |  |
| 3.4 Receiver reset and startup40                                              |  |
| 3.4.1 Reset types 40                                                          |  |
| 3.4.2 Startup modes40                                                         |  |
| 3.5 Time 41                                                                   |  |
| 3.5.1 Receiver local time41                                                   |  |
| 3.5.2 GNSS time bases41                                                       |  |
| 3.5.3 Navigation epochs 42                                                    |  |
| 3.5.4 iTOW timestamps43                                                       |  |
| 3.5.5 Time validity43                                                         |  |
| 3.5.6 UTC representation 44                                                   |  |
| 3.5.7 Leap seconds 44                                                         |  |
| 3.5.8 Date ambiguity 45                                                       |  |
| 3.6 Time mark 46                                                              |  |
| 3.7 Time pulse47                                                              |  |
| 3.7.1 Recommendations47                                                       |  |
| 3.7.2 Time pulse configuration48                                              |  |
| 3.8 Security 49                                                               |  |
| 3.8.1 Over-the-air signal integrity and security50                            |  |
| 3.8.2 GNSS receiver integrity and security 52                                 |  |
| 3.9 Multiple GNSS assistance (MGA) 53                                         |  |
| 3.9.1 Authorization 53                                                        |  |
| 3.9.2 Preserving MGA and operational data during power-off 53                 |  |
| 3.10 u-blox protocol feature descriptions53                                   |  |
| 3.10.1 Broadcast navigation data 53                                           |  |
| 3.11 Firmware update55                                                        |  |
|                                                                               |  |
| 4 Hardware<br>integration56                                                   |  |
| 4.1 Power supply56                                                            |  |
| 4.1.1 VCC56                                                                   |  |
| 4.1.2 V_BCKP56                                                                |  |
|                                                                               |  |
| 4.1.3 ZED-X20P power supply57                                                 |  |
| 4.2 RF interference57                                                         |  |
| 4.2.1 In-band interference58                                                  |  |
| 4.2.2 Out-of-band interference 58                                             |  |
| 4.2.3 Spectrum analyzer58                                                     |  |
| 4.3 RF front-end60                                                            |  |
| 4.3.1 Internal LNA modes60                                                    |  |
| 4.3.2 Out-of-band blocking immunity60                                         |  |
| 4.3.3 Interference coupling 60                                                |  |
| 4.4 Antenna61                                                                 |  |
| 4.4.1 Active Antenna Power Supply62                                           |  |
| 4.4.2 Antenna supervisor circuit65                                            |  |
| 4.5 I2C design recommendations 67                                             |  |
| 4.5.1 I2C pull up calculation67<br>4.5.2 EMI/EMC considerations for I2C bus67 |  |



| 4.6 Layout68                                              |    |
|-----------------------------------------------------------|----|
| 4.6.1 Placement68                                         |    |
| 4.6.2 Thermal and mechanical considerations68             |    |
| 4.6.3 Package footprint, copper and paste mask 68         |    |
| 4.6.4 Layout guidance 70                                  |    |
| 5 Production<br>test73                                    |    |
| 5.1 Connected sensitivity test73                          |    |
| 5.2 Go/no go tests for integrated devices 73              |    |
| 6 Product<br>handling                                     | 74 |
| 6.1 ESD precautions74                                     |    |
| 6.2 Safety precautions 75                                 |    |
| 6.3 Soldering75                                           |    |
| 6.4 Safe handling of modules77                            |    |
| Appendix                                                  | 79 |
| A Migration79                                             |    |
| A.1 Hardware functionality79                              |    |
| B Reference Design 79                                     |    |
| C Reference frames80                                      |    |
| D Creating RTK configuration with u-center 281            |    |
| D.1 Creating static base configuration with u-center 2 81 |    |
| D.2 Creating rover configuration with u-center 282        |    |
| Related<br>documents                                      | 84 |
|                                                           |    |



## <span id="page-5-0"></span>**1 System description**

This document is an important source of information for all aspects of ZED-X20P software and hardware design. The purpose of this document is to provide guidelines for a successful integration of the receiver with the customer's end product.

## <span id="page-5-1"></span>**1.1 Overview**

ZED-X20P is an innovative all-band receiver module designed to revolutionize positioning technology in industrial applications. Built upon the u-blox new generation receiver platform, this module offers multi-band Global Navigation Satellite System (GNSS) capability, supporting bands including L1, L2, L5 and L6. With its comprehensive coverage, ZED-X20P ensures precise and reliable positioning even in challenging environments, setting a new standard in accuracy.

Equipped with integrated u-blox multi-band real-time kinematic (RTK) and precise point positioning real-time kinematic (PPP-RTK) technologies, ZED-X20P achieves centimeter-level accuracy, enabling precise navigation and automation in industrial and consumer-grade products. Despite its advanced capabilities, ZED-X20P maintains a compact surface-mounted form factor, measuring only 17.0 x 22.0 x 2.4 mm, ensuring seamless integration into various applications without compromising performance.

In this document, RTK refers to an observation state representation (OSR) based solution utilizing radio technical commission for maritime services (RTCM) corrections, while PPP-RTK refers to state space representation (SSR) based solution using secure position augmentation for realtime navigation (SPARTN). With its comprehensive features and advanced technologies, ZED-X20P offers unparalleled accuracy and reliability, making it the ideal choice for applications requiring highperformance positioning solutions.

## <span id="page-5-2"></span>**1.2 Real time kinematic**

u-blox ZED-X20P high precision receiver takes GNSS precision to the next level:

- Delivers accuracy down to the millimeter level: 0.006 m + 1 ppm CEP.
- Fast time to first fix and robust performance with multi-band, multi-constellation reception.
- Compatible with leading correction services for global coverage and versatility.

Some typical applications for the ZED-X20P are shown below:







**Figure 1: Typical applications for the ZED-X20P**

#### <span id="page-6-0"></span>**1.2.1 RTK modes of operation**

The ZED-X20P supports the following modes of operation:

- **1.** ZED-X20P operating as a base: It provides RTCM correction data to a rover, or to a network of rovers.
- **2.** ZED-X20P operating as a rover: It receives RTCM correction data from a ZED-X20P operating as a base, or from a VRS service provider operating a network of base receivers.

#### <span id="page-6-1"></span>**1.2.2 PPP-RTK modes of operation**

The ZED-X20P operating as a rover supports the following additional operation modes:

• It can receive SPARTN correction data via internet from the service provider

#### <span id="page-6-2"></span>**1.2.3 NTRIP - networked transport of RTCM via internet protocol**

Networked Transport of RTCM via internet protocol, or NTRIP, is an open standard protocol for streaming differential data and other kinds of GNSS streaming data over the internet in accordance with specifications published by RTCM.

The NTRIP protocol is also used by SSR correction service providers to stream SSR correction data over the internet (e.g. SPARTN corrections).

There are three major parts to the NTRIP system: The NTRIP client, the NTRIP server, and the NTRIP caster:

- **1.** The NTRIP server is a PC or an on-board computer running NTRIP server software communicating directly with a GNSS reference station. The NTRIP server serves as the intermediary between the GNSS receiver (NTRIP Source) streaming correction data and the NTRIP caster.
- **2.** The NTRIP caster is an HTTP server which receives streaming correction data from one or more NTRIP servers and in turn streams the correction data to one or more NTRIP clients via the internet.
- **3.** The NTRIP client receives streaming correction data from the NTRIP caster to apply as realtime corrections to a GNSS receiver.

u-center 2 GNSS [evaluation](https://www.u-blox.com/en/product/u-center) software provides a NTRIP client and server application that can be used to easily evaluate a ZED-X20P base or rover. Typically a u-center 2 NTRIP client connects to an NTRIP service provider over the internet. The u-center 2 NTRIP client then provides the corrections



to a ZED-X20P rover connected to the local u-center 2 application. VRS service is also supported by the u-center 2 NTRIP client.

## <span id="page-7-0"></span>**1.3 Typical ZED-X20P application setups**

Two application examples are illustrated below as typical system implementations. Both are representative of a simple "short baseline" setup in which the base and rover receivers are within a few hundred meters of each other. In [Figure](#page-7-1) 2 and [Figure](#page-8-2) 3 ZED-X20P is used as a base station providing corrections to a ZED-X20P rover receiver.

Alternatively, the rover can use corrections provided over longer baselines from a correction stream distributed as a subscription service. This method can use a single fixed reference source which is local to the rover receiver or via a VRS service in which corrections are synthesized based on the rover's location.

<span id="page-7-1"></span>

**Figure 2: ZED-X20P base and rover in a short baseline drone application**



<span id="page-8-2"></span>

**Figure 3: ZED-X20P base and rover in a short baseline robotic mower application**

## <span id="page-8-0"></span>**1.4 Block diagram**



**Figure 4: ZED-X20P block diagram**

## <span id="page-8-1"></span>**1.5 Pin assignment**

The pin assignment of the ZED-X20P module is shown in [Figure](#page-9-0) 5. The defined configuration of the programmable input/outputs (PIOs) is listed in [Table](#page-9-1) 1.



<span id="page-9-0"></span>

<span id="page-9-1"></span>

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
| 11      | Reserved    | -   | Reserved                                         |
| 12      | GND         | -   | Ground                                           |
| 13      | Reserved    | -   | Reserved                                         |
| 14      | GND         | -   | Ground                                           |
| 15      | Reserved    | -   | Reserved                                         |
| 16      | Reserved    | -   | Reserved                                         |
| 17      | Reserved    | -   | Reserved                                         |

#### **Figure 5: ZED-X20P pin assignment**



| Pin no. | Name           | I/O | Description                                                              |
|---------|----------------|-----|--------------------------------------------------------------------------|
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
| 52      | Reserved       | -   | Reserved                                                                 |
| 53      | TIMEPULSE      | O   | Time pulse                                                               |
| 54      | Reserved       | -   | Reserved                                                                 |

**Table 1: ZED-X20P pin assignment**



## <span id="page-11-0"></span>**2 Receiver configuration**

The ZED-X20P receiver is highly customizable using the UBX configuration interface. Its settings are stored in a configuration database located in the receiver's RAM, which is loaded during startup from multiple sources as discussed in section *Configuration layers* in the Interface description [\[2\]](#page-83-1). These settings are applied during operation and can be adjusted as needed.

The configuration interface settings are stored in a database. Each item is made up of a configuration key ID and value pair. Related items are grouped together and identified under a common group name: CFG-GROUP; a convention used in u-center 2 and within this document.

In the u-center 2 *Device configuration* window, the configuration group is identified as *Group name* and the configuration item as the *Item name*.

The UBX messages available to change or poll the configurations are the UBX-CFG-VALSET, UBX-CFG-VALGET, and UBX-CFG-VALDEL messages. For more information about these messages and the configuration keys, see the configuration interface section in the Interface description [\[2\]](#page-83-1).

## <span id="page-11-1"></span>**2.1 Storing configuration in different memory layers**

Store the basic receiver [configuration](#page-11-2) and the navigation [configuration](#page-16-0) in the memory layers described in [Table](#page-11-5) 2. For further details, see the Interface description section *Configuration layers* [\[2](#page-83-1)]. For more details of the permanence of the RAM and BBR layer configurations, see section [Receiver](#page-39-0) reset and startup.

<span id="page-11-5"></span>

| Memory                      | Remarks                                                                                                                               |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| RAM                         | •<br>Contains the current runtime configuration.<br>•<br>Receiver power-down or entering backup mode clears the configuration in RAM. |
| Battery-backed RAM<br>(BBR) | •<br>Retains the settings as long as the backup power supply remains.<br>•<br>Can also be cleared with the UBX-CFG-CFG message.       |
| Flash                       | •<br>Permanent storage of the configuration settings.<br>•<br>Can be cleared with the UBX-CFG-CFG message.                            |

**Table 2: Applicable memory storage layers**

In addition to RAM, it is recommended to apply the runtime configuration also on BBR or flash memory layers.

## <span id="page-11-2"></span>**2.2 Basic receiver configuration**

This section summarizes the most commonly used, basic receiver configurations.

#### <span id="page-11-3"></span>**2.2.1 Basic hardware configuration**

The ZED-X20P receiver is configured with the default settings during the module production. The receiver starts up and is fully operational as soon as proper power supply, communication interfaces and antenna signal from the host application device are connected.

#### <span id="page-11-4"></span>**2.2.2 Internal LNA mode configuration**

ZED-X20P provides three independently configurable [internal](#page-59-1) LNAs, one for each RF block. The internal LNA modes are configurable in all memory layers of the receiver.

| Configuration key           | Normal gain<br>(default) | Low gain | Description                     |
|-----------------------------|--------------------------|----------|---------------------------------|
| CFG-HW-RF1_LNA_MODE_LOWGAIN | 0                        | 1        | Internal LNA mode of RF block 1 |





| Configuration key           | Normal gain<br>(default) | Low gain | Description                     |
|-----------------------------|--------------------------|----------|---------------------------------|
| CFG-HW-RF2_LNA_MODE_LOWGAIN | 0                        | 1        | Internal LNA mode of RF block 2 |
| CFG-HW-RF3_LNA_MODE_LOWGAIN | 0                        | 1        | Internal LNA mode of RF block 3 |

**Table 3: Internal LNA mode configuration keys**

#### <span id="page-12-0"></span>**2.2.3 GNSS signal configuration**

The GNSS constellations and signal bands are selected using keys from the CFG-SIGNAL. configuration group. ZED-X20P is an all-band receiver that can concurrently select signals of all GNSS bands. Each GNSS constellation can be enabled or disabled independently except for QZSS [1](#page-12-1) and SBAS [2](#page-12-2) . A GNSS constellation is considered to be enabled when the constellation enable key is set and at least one of the constellation's band keys is enabled.

ZED-X20Ponly supports certaincombinations of constellations andbands.For all constellations,L1 band is mandatory, a combination of L1 and L2 or L1 and L5 or L1,L2 and L5 must either be enabled or disabled. The receiver rejects unsupported combinations with the UBX-ACK-NAK message and sends the "inv sig cfg" warning via the UBX-INF and NMEA-TXT messages if they are enabled.

| Constellation key  | Band key   | Band key    | Band key   | Constellation enabled? |
|--------------------|------------|-------------|------------|------------------------|
| CFG-SIGNAL-GAL_ENA | CFG-SIGNAL | CFG-SIGNAL  | CFG-SIGNAL |                        |
|                    | GAL_E1_ENA | GAL_E5A_ENA | GAL_E6_ENA |                        |
| true (1)           | true (1)   | true (1)    | true (1)   | yes                    |
| true (1)           | true (1)   | true (1)    | false (0)  | yes                    |
| true (1)           | true (1)   | false (0)   | true (1)   | yes                    |
| true (1)           | true (1)   | false (0)   | false (0)  | yes                    |
| true (1)           | false (0)  | true (1)    | true (1)   | no                     |
| true (1)           | false (0)  | false (0)   | true (1)   | no                     |
| true (1)           | false (0)  | true (1)    | false (0)  | no                     |
| true (1)           | false (0)  | false (0)   | false (0)  | no                     |
| false (0)          | true (1)   | true (1)    | true (1)   | no                     |
| false (0)          | true (1)   | true (1)    | false (0)  | no                     |
| false (0)          | true (1)   | false (0)   | true (1)   | no                     |
| false (0)          | false (0)  | true (1)    | true (1)   | no                     |
| false (0)          | false (0)  | false (0)   | true (1)   | no                     |
| false (0)          | false (0)  | true (1)    | false (0)  | no                     |
| false (0)          | true (1)   | false (0)   | false (0)  | no                     |
| false (0)          | false (0)  | false (0)   | false (0)  | no                     |
|                    |            |             |            |                        |

The following table shows possible configuration key combinations for the Galileo constellation.

**Table 4: Examples of possible values of configuration items for the Galileo constellation**

#### **2.2.3.1 Default GNSS configuration**

The ZED-X20P default GNSS configuration is set as follows:

#### **ZED-X20P-00B:**

<span id="page-12-1"></span><sup>1</sup> QZSS can be enabled only if GPS is selected

<span id="page-12-2"></span><sup>2</sup> SBAS can only be enabled with at least one of GPS, GAL and BDS



- GPS: L1C/A, L2C, L5 [3](#page-13-1)
- Galileo: E1B/C, E5a, E6
- BeiDou: B1C, B2a, B3I
- QZSS: L1C/A
- SBAS: L1C/A

For more information about the default configuration, see the applicable Interface description [\[2](#page-83-1)].

#### <span id="page-13-0"></span>**2.2.4 GPS L5 signal health status configuration**

ZED-X20P supports GPS L1 C/A, L2C and L5 signals. Broadcasting of Civil Navigation (CNAV) messages on the L5 signal began in April 2014. At the time of writing, GPS L5 signals remain [pre](https://www.gps.gov/systems/gps/modernization/civilsignals/)[operational](https://www.gps.gov/systems/gps/modernization/civilsignals/) which are set unhealthy until sufficient monitoring capability is established.

To evaluate GPS L5 signals before they become fully operational, the receiver can be configured to ignore the GPS L5 health status by overriding it with the respective GPS L1 C/A signal status.

Do not use unhealthy, pre-operational GPSL5 signals for safety-of-life or other critical purposes. This is an operational issue concerning the satellites / space segment and not a limitation or specific configuration of u-blox products.

To ignore the GPS L5 signal health status and override it with the respective GPS L1 signal health status, send the configuration string given in [Table](#page-13-2) 5. The configuration can be stored in RAM, battery-backed RAM (BBR), and flash layers. Stored in the RAM layer, the device returns the UBX-ACK-ACK message if the configuration is sent successfully and it is applied immediately without a configuration reset. To apply the configuration stored in the BBR and flash layers, send the UBX-CFG-RST message with resetMode 0x01.

To revert back to the default configuration, send the configuration string given in [Table](#page-13-3) 6. The device returns the UBX-ACK-ACK message if the configuration is sent successfully and it is applied immediately without a reset in the RAM layer. To apply the configuration stored in the BBR and flash layers, send the UBX-CFG-RST message with resetMode 0x01.

Customers who choose to ignore the GPS L5 signal health status in their production system do so at their own risk and must be fully aware of the implications. The system should also include a mechanism to revert to the mode where the L5 signal health status is respected when the GPS Operational Control System (OCX) upgrade is complete.

<span id="page-13-2"></span>

| Configuration layer                                                                          | Configuration string                               |  |
|----------------------------------------------------------------------------------------------|----------------------------------------------------|--|
| RAM                                                                                          | B5 62 06 8A 09 00 01 01 00 00 01 00 32 10 01 DF F6 |  |
| BBR                                                                                          | B5 62 06 8A 09 00 01 02 00 00 01 00 32 10 01 E0 FE |  |
| FLASH                                                                                        | B5 62 06 8A 09 00 01 04 00 00 01 00 32 10 01 E2 0E |  |
| Table 5: UBX binary string to override GPS L5 signal health status with GPS L1 health status |                                                    |  |

<span id="page-13-3"></span>

| Configuration layer | Configuration string                               |
|---------------------|----------------------------------------------------|
| RAM                 | B5 62 06 8A 09 00 01 01 00 00 01 00 32 10 00 DE F5 |
| BBR                 | B5 62 06 8A 09 00 01 02 00 00 01 00 32 10 00 DF FD |

<span id="page-13-1"></span><sup>3</sup> GPS L5 is tracked but not used in navigation by default





| Configuration layer | Configuration string                               |
|---------------------|----------------------------------------------------|
| FLASH               | B5 62 06 8A 09 00 01 04 00 00 01 00 32 10 00 E1 0D |
|                     |                                                    |

**Table 6: UBX binary strings to revert the GPS L5 signal health status monitoring to default**

#### <span id="page-14-0"></span>**2.2.5 Communication interface configuration**

Several configuration groups allow operation mode configuration of the various communication interfaces. These include parameters for the data framing, transfer rate and enabled input/output protocols. The configuration groups available for each interface are:

| Interface | Configuration groups |
|-----------|----------------------|
| UART1     | CFG-UART1,           |
|           | CFG-UART1INPROT,     |
|           | CFG-UART1OUTPROT     |
| UART2     | CFG-UART2,           |
|           | CFG-UART2INPROT,     |
|           | CFG-UART2OUTPROT     |
| I2C       | CFG-I2C,             |
|           | CFG-I2CINPROT,       |
|           | CFG-I2COUTPROT       |
| SPI       | CFG-SPI,             |
|           | CFG-SPIINPROT,       |
|           | CFG-SPIOUTPROT       |
|           |                      |

**Table 7: Interface configurations**

#### **2.2.5.1 Default interface settings**

| Interface    | Settings                                                                                                                                                                                                               |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART1 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                         |
|              | NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output by default.                                                                                                                                   |
|              | UBX and RTCM 3.4 protocols are enabled by default but no output messages are enabled by<br>default.                                                                                                                    |
| UART1 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                         |
|              | UBX, NMEA and RTCM 3.4 input protocols are enabled by default.                                                                                                                                                         |
| UART2 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                         |
|              | RTCM 3.4 protocol is enabled by default but no output messages are enabled by default.                                                                                                                                 |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                  |
| UART2 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                         |
|              | RTCM 3.4 protocol is enabled by default.                                                                                                                                                                               |
|              | SPARTN protocol is enabled by default.                                                                                                                                                                                 |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                  |
| I2C          | Available for communication in the Fast-mode with an external host CPU in peripheral mode<br>only. Default messages activated as in UART1. Input/output protocols available as in UART1.<br>Maximum bit rate 400 kb/s. |
| SPI          | Allow communication to a host CPU, operated in peripheral mode only. Default messages<br>activated as in UART1. Input/output protocols available as in UART1. SPI is not available unless<br>D_SEL pin is set to low   |

#### **Table 8: Default interface settings**

Refer to the applicable Interface description for information about further settings.



By default, ZED-X20P outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period.

#### <span id="page-15-0"></span>**2.2.6 Message output configuration**

The receiver supports two protocols for output messages: industry-standard NMEA and u-blox UBX. Any message type can be enabled or disabled individually and the output rate is configurable.

The message output rate is related to the frequency of an event. For example, the output message UBX-NAV-PVT (position, velocity, and time solution) is related to the navigation event, which generates a navigation epoch. In this case, the rate for each navigation epoch is defined by the configuration keys CFG-RATE-MEAS and CFG-RATE-NAV. For example, a value of 1000 ms in CFG-RATE-MEAS indicates that a measurement is done every second. If CFG-RATE-NAV is set to one (1), the solution is calculated for every measurement. This means that a navigation epoch is calculated every 1000 ms. If the rate is set to two (2), only the second measurement is used and the navigation epoch is calculated every two seconds. The same result is obtained if CFG-RATE-MEAS is set to 2000 ms, and CFG-RATE-NAV is set to one (1). Every 2000 ms a measurement is done, and in every measurement, a navigation epoch is calculated. However, this second option demands fewer resources and is the correct procedure when the navigation rate is changed. Setting a navigation rate value higher than one (1) is only needed when it is required that the raw measurement data is output at a higher rate than the navigation data.

The output rate for each message is defined in the CFG-MSGOUT configuration group. If the output rate of the message is set to one (1) on the UART interface, CFG-MSGOUT-UBX\_NAV\_PVT\_UART1 = 1, the message is output for every navigation epoch. If the rate is set to two (2), the message is output for every other navigation epoch. If the rate is zero (0), then corresponding message is not output. As seen in this example, the rates of the output messages are individually configurable per communication interface.

Some messages, such as UBX-MON-VER, are non-periodic and are only output as an answer to a poll request.

The UBX-INF and NMEA-Standard-TXT information messages are non-periodic output messages that do not have a message rate configuration. Instead they can be enabled for each communication interface via the CFG-INFMSG configuration group.

All message output is additionally subject to the protocol configuration of the communication interfaces. Messages of a given protocol are not output unless the protocol is enabled for output on the interface. See [Communication](#page-14-0) interface configuration for details.

#### <span id="page-15-1"></span>**2.2.7 Antenna supervisor configuration**

Configure the antenna [supervisor](#page-36-0) with the configuration items in [Table](#page-15-2) 9. The antenna supervisor is configurable in runtime in the RAM, BBR and flash layers. However, applying the configurations from the BBR and flash layers requires a suitable [receiver](#page-39-1) reset. Furthermore, consider the [pin](#page-0-0) [assignment](#page-0-0) when reconfiguring the PIOs as antenna supervisor pins. The receiver provides the antenna supervisor status as discussed in section Antenna status [reporting.](#page-37-4)

<span id="page-15-2"></span>

| Configuration item         | Description                              | Remarks                                                                           |
|----------------------------|------------------------------------------|-----------------------------------------------------------------------------------|
| CFG-HW<br>ANT_CFG_VOLTCTRL | Enable active antenna voltage<br>control | See section Antenna voltage control (ANT_OFF).                                    |
| CFG-HW<br>ANT_CFG_SHORTDET |                                          | Enable short circuit detection See section Antenna short detection (ANT_SHORT_N). |



| Configuration item             | Description                                                                                                       | Remarks                                                                                                                                                                  |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFG-HW<br>ANT_CFG_SHORTDET_POL | Short antenna detection<br>polarity                                                                               | Default: 1 (true), the required logic polarity is active-low.                                                                                                            |
| CFG-HW<br>ANT_CFG_OPENDET      | Enable open circuit detection                                                                                     | See section Antenna open circuit detection (ANT_DETECT) .                                                                                                                |
| CFG-HW<br>ANT_CFG_OPENDET_POL  | Open antenna detection<br>polarity                                                                                | Default: 1 (true), the required logic polarity is active-low.                                                                                                            |
| CFG-HW<br>ANT_CFG_PWRDOWN      | Power down antenna supply if<br>short circuit is detected                                                         | Can be enabled only if CFG-HW-ANT_CFG_VOLTCTRL and CFG<br>HW-ANT_CFG_SHORTDET are enabled.                                                                               |
| CFG-HW<br>ANT_CFG_PWRDOWN_POL  | Power down antenna logic<br>polarity                                                                              | Default: 1 (true), the required logic polarity is active-high.                                                                                                           |
| CFG-HW<br>ANT_CFG_RECOVER      | Enables auto-recovery in the<br>event of a short circuit                                                          | Can be enabled only if CFG-HW-ANT_CFG_PWRDOWN is enabled.<br>See section Antenna short detection auto-recovery.                                                          |
| CFG-HW<br>ANT_SUP_SWITCH_PIN   | Antenna switch pin number                                                                                         | Default: pin 5. Uses the LNA_EN signal to control the external<br>LNA in case of antenna short detection.                                                                |
| CFG-HW<br>ANT_ON_SHORT_US      | Delay in µs between turning<br>the antenna power supply<br>on and enabling the antenna<br>short circuit detection | Increase the time delay to avoid a short circuit to be<br>detected before the antenna supply voltage has stabilized.<br>Recommended values: 500 µs (default) to 5000 µs. |

**Table 9: Antenna supervisor configuration**

## <span id="page-16-0"></span>**2.3 Navigation configuration**

This section presents various configuration options related to the navigation engine. These options can be configured with the CFG-NAVSPG configuration group.

#### <span id="page-16-1"></span>**2.3.1 Dynamic platform**

Configure the dynamic platform model for the application with the CFG-NAVSPG-DYNMODEL configuration item. For the supported dynamic platform models and their details, see [Table](#page-16-2) 10 and [Table](#page-17-2) 11.

The receiver checks the sanity of the navigation solution against the dynamic platform model limits as described in [Table](#page-17-2) 11. If the sanity check fails, the receiver sets the navigation solution invalid.

<span id="page-16-2"></span>

| Platform     | Description                                                                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Portable     | Applications with low acceleration, e.g. portable devices. Suitable for most situations.                                                           |
| Stationary   | Used in timing applications (antenna must be stationary) or other stationary applications.<br>Velocity restricted to 0 m/s. Zero dynamics assumed. |
| Pedestrian   | Applications with low acceleration and speed, e.g. how a pedestrian would move. Low<br>acceleration assumed.                                       |
| Automotive   | Used for applications with equivalent dynamics to those of a passenger car. Low vertical<br>acceleration assumed.                                  |
| At sea       | Recommended for applications at sea. Zero vertical velocity and sea level assumed.                                                                 |
| Airborne <1g | Used for applications with a higher dynamic range and greater vertical acceleration than a<br>passenger car. No 2D position fix supported.         |
| Airborne <2g | Recommended for typical airborne environments. No 2D position fix supported.                                                                       |
| Airborne <4g | Only recommended for extremely dynamic environments. No 2D position fix supported.                                                                 |
| Wrist        | Only recommended for wrist-worn applications. Receiver filters out arm motion.                                                                     |

**Table 10: Dynamic platform models**



<span id="page-17-2"></span>

| Platform     | Max altitude [m] | Max horizontal<br>velocity [m/s] | Max vertical velocity<br>[m/s] | Sanity check type     | Max<br>position<br>deviation |
|--------------|------------------|----------------------------------|--------------------------------|-----------------------|------------------------------|
| Portable     | 12,000           | 310                              | 50                             | Altitude and velocity | Medium                       |
| Stationary   | 9,000            | 10                               | 6                              | Altitude and velocity | Small                        |
| Pedestrian   | 9,000            | 30                               | 20                             | Altitude and velocity | Small                        |
| Automotive   | 6,000            | 100                              | 15                             | Altitude and velocity | Medium                       |
| At sea       | 500              | 25                               | 5                              | Altitude and velocity | Medium                       |
| Airborne <1g | 80,000           | 100                              | 6,400                          | Altitude              | Large                        |
| Airborne <2g | 80,000           | 250                              | 10,000                         | Altitude              | Large                        |
| Airborne <4g | 80,000           | 500                              | 20,000                         | Altitude              | Large                        |
| Wrist        | 9,000            | 30                               | 20                             | Altitude and velocity | Medium                       |
|              |                  |                                  |                                |                       |                              |

**Table 11: Dynamic platform model details**

Applying dynamic platform models designed for high acceleration systems, such as airborne <2g, can result in a higher standard deviation in the reported position.

#### <span id="page-17-0"></span>**2.3.2 Navigation input filters**

The navigation input filters control how the navigation engine handles the input data that comes from the satellite signal. For the applicable navigation input filter configurations, see [Table](#page-17-3) 12.

If the receiver has only three satellites for calculating a position, the navigation algorithm uses a constant altitude to compensate for the missing fourth satellite.This is called a 2D fix.The constant altitude value is taken from the last successful 3D fix using a minimum of four available satellites.

<span id="page-17-3"></span>

| Configuration item        | Description                                                                                                                                                                                                                    |  |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| CFG-NAVSPG-FIXMODE        | By default, the receiver calculates a 3D position fix if possible but it reverts to 2D<br>position if necessary (auto 2D/3D). The receiver can also be configured to calculate<br>only 2D (2D only) or 3D (3D only) positions. |  |
| CFG-NAVSPG-CONSTR_ALT     | The fixed altitude is used if fixMode is set to 2D only. Supply a variance greater than                                                                                                                                        |  |
| CFG-NAVSPG-CONSTR_ALTVAR  | zero.                                                                                                                                                                                                                          |  |
| CFG-NAVSPG-INFIL_MINELEV  | The minimum elevation of a satellite above the horizon to be used in the navigation<br>solution. Low-elevation satellites may provide degraded accuracy due to the long<br>signal path through the atmosphere.                 |  |
| CFG-NAVSPG-INFIL_MINSVS   | The minimum and maximum number of satellites to use in the navigation solution.                                                                                                                                                |  |
| CFG-NAVSPG-INFIL_MAXSVS   | There is an absolute maximum limit of 32 satellites that can be used for navigation.                                                                                                                                           |  |
| CFG-NAVSPG-INFIL_NCNOTHRS | A navigation solution will only be attempted if there is at least the given number of                                                                                                                                          |  |
| CFG-NAVSPG-INFIL_CNOTHRS  | satellites with signals at least as strong as the given threshold.                                                                                                                                                             |  |

**Table 12: Navigation input filter parameters**

#### <span id="page-17-1"></span>**2.3.3 Navigation output filters**

The receiver initially classifies the navigation solution by the fix type, as in the fixType field of the UBX-NAV-PVT message. However, the fix type doesn't provide any validity information. Therefore, the receiver checks the validity of every position fix with the navigation output filters. That is, the receiver sets the fix as valid if the navigation solution is above all the navigation output filter masks (thresholds) described in [Table](#page-18-2) 13. The receiver reports the fix validity in the message fields listed in [Table](#page-18-3) 14.

Don't use fixes that are not marked valid.



<span id="page-18-2"></span>

| Configuration item     | Description                                                |
|------------------------|------------------------------------------------------------|
| CFG-NAVSPG-OUTFIL_PDOP | The position dilution of precision (PDOP) mask (threshold) |
| CFG-NAVSPG-OUTFIL_TDOP | The time dilution of precision (TDOP) mask (threshold)     |
| CFG-NAVSPG-OUTFIL_PACC | Output filter position accuracy mask (threshold)           |
| CFG-NAVSPG-OUTFIL_TACC | Output filter time accuracy mask (threshold)               |
| CFG-NAVSPG-OUTFIL_FACC | Output filter frequency accuracy mask (threshold)          |

**Table 13: Navigation output filter parameters**

<span id="page-18-3"></span>

| Message        | Field     | Description and remarks                                                                                                     |
|----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| UBX-NAV-PVT    | gnssFixOK | 1 = valid fix                                                                                                               |
| UBX-NAV-STATUS | gpsFixOK  | This message is only retained for backwards compatibility, and it is<br>recommended to use the UBX-NAV-PVT message instead. |
| NMEA-GLL       | status    | Data validity status                                                                                                        |
| NMEA-RMC       | status    | Data validity status                                                                                                        |

**Table 14: Messages and fields providing the fix validity**

## <span id="page-18-0"></span>**2.4 RTK configuration**

RTK technology introduces the concept of a base [4](#page-18-4) and a rover. In such a setup, the base sends corrections (complying with the RTCM 3.4 protocol) to the rover via a communication link. This enables the rover to compute its position relative to the base with high accuracy.

When operating as a rover, the ZED-X20P can receive RTCM 3.4 corrections from another ZED-X20P operating as a base, or via NTRIP from a VRS service provider operating a network of base receivers.In this mode, the receiver coordinates will be expressed in the datum used by the RTCM correction provider. For more information refer to the Reference frames section in the Appendix.

After describing the RTCM protocol and corresponding supported message types, this section describes how to configure the ZED-X20P high precision receiver as a base or rover receiver.

PointPerfect Live is a u-blox service delivering the highest accuracy in real time on a regional scale through IP-based network RTK corrections, while ensuring precise positioning when and where it matters most. Designed to work seamlessly with any GNSS RTK hardware using RTCM standards, it provides maximum flexibility for integration. The service is continuously monitored with u-blox receivers.

#### <span id="page-18-1"></span>**2.4.1 RTCM corrections**

RTCM is a standard-based binary protocol for the communication of GNSS correction information. The ZED-X20P high precision receiver supports RTCM as specified by RTCM 10403.4, Differential GNSS (Global Navigation Satellite Systems) Services – Version 4 (December 1, 2023).

The RTCM specification is currently at version 3.4 and RTCM version 2 messages are not supported by this standard.

To modify the RTCM input/output settings, see the configuration section in the applicable Interface description [\[2\]](#page-83-1).

Users should be aware of the datum used by the correction source. The rover's reported position is in a coordinate system based on the correction service provider's reference frame. This may need

<span id="page-18-4"></span><sup>4</sup> The terms base, base station, reference and reference station can be used interchangeably



to be taken into account when using the RTK rover position depending on the application. See the Reference frames section in the Appendix for more information.

| Message type | Description                                              |
|--------------|----------------------------------------------------------|
| RTCM 1001    | L1-only GPS RTK observables                              |
| RTCM 1002    | Extended L1-only GPS RTK observables                     |
| RTCM 1003    | L1/L2 GPS RTK observables                                |
| RTCM 1004    | Extended L1/L2 GPS RTK observables                       |
| RTCM 1005    | Stationary RTK reference station ARP                     |
| RTCM 1006    | Stationary RTK reference station ARP with antenna height |
| RTCM 1007    | Antenna descriptor                                       |
| RTCM 1033    | Receiver and Antenna Description                         |
| RTCM 1074    | GPS MSM4                                                 |
| RTCM 1075    | GPS MSM5                                                 |
| RTCM 1077    | GPS MSM7                                                 |
| RTCM 1094    | Galileo MSM4                                             |
| RTCM 1095    | Galileo MSM5                                             |
| RTCM 1097    | Galileo MSM7                                             |
| RTCM 1124    | BeiDou MSM4                                              |
| RTCM 1125    | BeiDou MSM5                                              |
| RTCM 1127    | BeiDou MSM7                                              |
|              |                                                          |

#### <span id="page-19-0"></span>**2.4.2 List of supported RTCM input messages**

**Table 15: ZED-X20P supported input RTCM version 3.4 messages**

#### <span id="page-19-1"></span>**2.4.3 List of supported RTCM output messages**

| Message type | Description                          |
|--------------|--------------------------------------|
| RTCM 1005    | Stationary RTK reference station ARP |
| RTCM 1074    | GPS MSM4                             |
| RTCM 1077    | GPS MSM7                             |
| RTCM 1094    | Galileo MSM4                         |
| RTCM 1097    | Galileo MSM7                         |
| RTCM 1124    | BeiDou MSM4                          |
| RTCM 1127    | BeiDou MSM7                          |

**Table 16: ZED-X20P supported output RTCM version 3.4 messages**

#### <span id="page-19-2"></span>**2.4.4 Rover operation**

In its default configuration, ZED-X20P attempts to provide the best positioning accuracy depending on the received correction data. It enters RTK float mode shortly after it starts receiving an input stream of RTCM correction messages. Once the rover has resolved the carrier phase ambiguities, it enters the RTK fixed mode. When in this mode, the relative position accuracy between the base and the rover is expected to be at centimeter-level accuracy. The time period between the RTK float and RTK fixed operations is referred to as the convergence time. Note that the convergence time is affected by the baseline length as well as multipath and satellite visibility at both rover and base station.

To function optimally ZED-X20P has to receive RTCM corrections matching its GNSS signal configaration. The rover requires both base station observation (MSM4 or MSM7 messages) and



position message (RTCM 1005 or RTCM 1006) to attempt ambiguity fixes. The rover attempts to provide RTK fixed operation when sufficient number of ambiguities is resolved. If phase lock on sufficient number of signals cannot be maintained, the rover drops back to the RTK float mode. Once the minimum number of signals has been restored, the rover continues attempting to resolve carrier ambiguities and to revert to the RTK fixed mode.

The RTK mode that an RTK rover operates in can be configured through the CFG-NAVHPG-DGNSSMODE configuration item. The following two RTK modes are available:

- RTK fixed: The rover attempts to fix ambiguities whenever possible.
- RTK float: The rover estimates the ambiguities as float but makes no attempts at fixing them.

The rover stops using RTCM corrections that are older than 60s (default value) and drops back to the 3D or 3D/DGNSS mode. This is meant to prevent the computation of grossly misleading differential solutions. If desired, this value can be changed through the CFG-NAVSPG-CONSTR\_DGNSSTO and CFG-NAVSPG-CONSTR\_DGNSSTO\_SCALE configuration items.

The received correction messages stream should comply with the following:

• The reference station ID in the reference station message (RTCM 1005 or RTCM 1006) must match that used in the MSM observation messages. Otherwise, the rover cannot compute the RTK fixed position.

CFG-RTCM-DF003\_IN can be used to configure the desired reference station ID and CFG-RTCM-DF003\_IN\_FILTER can be used to configure how strict the filtering should be (RELAXED is the recommended setting).

#### **2.4.4.1 Message output in RTK mode**

When operating in RTK rover mode users should take note of the modified information within the following NMEA and UBX messages:

- NMEA-GGA: The quality field is 4 for RTK fixed and 5 for RTK float (see NMEA position fix flags in interface description). The age of differential corrections and base station ID is set.
- NMEA-GLL, NMEA-VTG: The posMode indicator is D for RTK float and RTK fixed (see NMEA position fix flags in interface description).
- NMEA-RMC, NMEA-GNS: The posMode indicator is F for RTK float and R for RTK fixed (see NMEA position fix flags in interface description).
- UBX-NAV-PVT: The carrSoln flag is set to 1 for RTK float and 2 for RTK fixed. The age of differential corrections are reported.
- UBX-NAV-RELPOSNED
  - The diffSoln and relPosValid flags are set
  - The carrSoln flag is set to 1 for RTK float and 2 for RTK fixed
- UBX-NAV-SAT
  - The diffCorr flag is set for satellites with valid RTCM data
  - The rtcmCorrUsed, prCorrUsed, and crCorrUsed flags are set for satellites for which the RTCM corrections have been applied
- UBX-NAV-SIG
  - For signals to which the RTCM corrections have been applied, the correction source is set to RTCM3 OSR and the crUsed, prCorrUsed, and crCorrUsed flags are set
- UBX-NAV-STATUS
  - The diffSoln flag and the diffCorr flag is set
  - The carrSoln flag is set to 1 for RTK float and 2 for RTK fixed





• If the baseline exceeds 100 km, a UBX-INF-WARNING will be output, e.g. "WARNING: DGNSS long baseline: 102.7 km"

#### <span id="page-21-0"></span>**2.4.5 Stationary base operation**

The default operation of ZED-X20P high precision receiver begins without producing any RTCM messages. RTCM observation messages will be streamed as soon as they are configured for output. However, any stationary reference positionmessages are output onlywhen the base station position has been initialized and the receiver is operating in the time mode. It sets the receiver to operate as a stationary base station in a fixed position and only time is estimated.

To initialize the base station position, do one of the following:

- Use the built-in survey-in procedure to estimate the position.
- Enter the coordinates which have been generated independently or taken from an accurate position such as a survey marker.
- Use the receiver in the rover mode while feeding the corrections to it and enter the resulting estimated position coordinates as above.

#### **2.4.5.1 Survey-in**

Survey-in is a procedure that is carried out prior to entering the time mode. It estimates the receiver position by building a weighted mean of all valid 3D position solutions.

Two major parameters are required when configuring the receiver:

- The **minimum observation time** defines the minimum observation time independent of the actual number of 3D fixes used for the position estimate. Values can range from one day for high accuracy requirements to a few minutes for coarse position determination.
- The **3D position standard deviation** defines the limit on the spread of positions that contribute to the calculated mean.

The survey-in ends when both requirements are successfully met. The receiver begins operation in the time mode and can output a base position message if configured. The survey-in status can be queried using the UBX-NAV-SVIN message.

Do not feed RTCM corrections to the base station receiver while it is in the survey-in mode. If a corrected position is desired, pre-survey the base station coordinates using the RTCM corrections. The resulting position can be used to set the base station in the fixed mode.

To configure a base station into survey-in mode (CFG-TMODE-MODE=SURVEY\_IN), the following items are required:

| Configuration item       | Description                                  |
|--------------------------|----------------------------------------------|
| CFG-TMODE-MODE           | Receiver mode (disabled, survey-in or fixed) |
| CFG-TMODE-SVIN_MIN_DUR   | Survey-in minimum duration                   |
| CFG-TMODE-SVIN_ACC_LIMIT | Survey-in position accuracy limit            |

**Table 17: Configuration items used for setting a base station into survey-in mode**

#### **2.4.5.2 Fixed position**

As an alternative to the survey-in procedure, manually enter the receiver's coordinates. Any error in the base station position directly translates into rover position errors. The base station position accuracy should therefore match or exceed the desired rover absolute position accuracy.

To configure Fixed mode (CFG-TMODE-MODE=FIXED), the following items are relevant:



| Configuration item      | Description                                                            |
|-------------------------|------------------------------------------------------------------------|
| CFG-TMODE-MODE          | Receiver mode (disabled or survey-in or fixed)                         |
| CFG-TMODE-POS_TYPE      | Determines whether the ARP position is given in ECEF or LAT/LON/HEIGHT |
| CFG-TMODE-ECEF_X        | ECEF X coordinate of the ARP position                                  |
| CFG-TMODE-ECEF_Y        | ECEF Y coordinate of the ARP position                                  |
| CFG-TMODE-ECEF_Z        | ECEF Z coordinate of the ARP position                                  |
| CFG-TMODE-LAT           | Latitude of the ARP position                                           |
| CFG-TMODE-LON           | Longitude of the ARP position                                          |
| CFG-TMODE-HEIGHT        | Height of the ARP position                                             |
| CFG-TMODE-ECEF_X_HP     | High-precision ECEF X coordinate of the ARP position                   |
| CFG-TMODE-ECEF_Y_HP     | High-precision ECEF Y coordinate of the ARP position                   |
| CFG-TMODE-ECEF_Z_HP     | High-precision ECEF Z coordinate of the ARP position                   |
| CFG-TMODE-LAT_HP        | High-precision latitude of the ARP position                            |
| CFG-TMODE-LON_HP        | High-precision longitude of the ARP position                           |
| CFG-TMODE-HEIGHT_HP     | High-precision height of the ARP position                              |
| CFG-TMODE-FIXED_POS_ACC | Fixed position 3D accuracy estimate                                    |

**Table 18: Configuration items used for setting a base station into fixed mode**

Once the receiver is set in the fixed mode, select the position format to use: either LLH or ECEF with optional high precision (mm) coordinates compared to the default cm level precision.

For example, with CFG-TMODE-POS\_TYPE=ECEF, the base antenna position can be entered with cm precision using CFG-TMODE-ECEF\_X, CFG-TMODE-ECEF\_Y, CFGTMODE-ECEF\_Z. For high precision (mm) coordinates, use CFG-TMODEECEF\_X\_HP, CFG-TMODE-ECEF\_Y\_HP, CFG-TMODE-ECEF\_Z\_HP. The same applies with corresponding coordinates used with CFG-TMODE-POS\_TYPE=LLH.

The "3D accuracy estimate" in "Fixed Position" and the "Position accuracy limit" in "Survey-in" affect the rover's absolute position accuracy. Note that the availability of the position accuracy does not mitigate the error in the rover position, but only accounts for it when calculating the resulting positioning accuracy.

- In the stationary base station mode, a current position check is made with respect to the fixed coordinates. If the result indicates the fixed position coordinates are incorrect, the receiver issues the UBX-INF-WARNING message "Base station position seems incorrect". The message is output when the coordinates are incorrect by more than ~50 m up to 25 km.
- If the base station is moved during operation, new position coordinates must be configured to it.

#### **2.4.5.3 Base station: RTCM output configuration**

The desired RTCM messages must be selected and configured for the corresponding GNSS constellations received. The recommended list of RTCM output messages for a base operating in default GNSS configuration are:

- RTCM 1005 Stationary RTK reference station ARP
- RTCM 1074 GPS MSM4
- RTCM 1094 Galileo MSM4
- RTCM 1124 BeiDou MSM4

The configuration messages for these are shown in the [Table](#page-23-2) 19.



The following configuration items output the recommended messages for a default satellite constellation setting. Note that these are given for the UART1 interface:

<span id="page-23-2"></span>

| Configuration item     | Description                                                             |
|------------------------|-------------------------------------------------------------------------|
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1005 message on port UART1: RTCM base    |
| RTCM_3X_TYPE1005_UART1 | station message                                                         |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1074 message on port UART1: RTCM GPS     |
| RTCM_3X_TYPE1074_UART1 | MSM4 message                                                            |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1094 message on port UART1: RTCM Galileo |
| RTCM_3X_TYPE1094_UART1 | MSM4 message                                                            |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1124 message on port UART1: RTCM BeiDou  |
| RTCM_3X_TYPE1124_UART1 | MSM4 message                                                            |

**Table 19: Configuration items used for typical RTCM output configuration on UART1**

CFG-RTCM-DF003\_OUT can be used to configure the reference station ID that will be reported in all RTCM messages containing the RTCM DF003 data field.

The configuration of the RTCM 3.4 correction stream must be made with the following guidance:

- All observation messages must be broadcast at the same rate.
- The static reference station message (RTCM 1005 or RTCM 1006) does not need to be broadcast at the same rate as the observation messages, however, a rover will not be able to compute its position until it has received a valid reference station message.
- The correction stream should only contain one type of observation messages per constellation. When using a multi-constellation configuration, all constellations should use the same type of observation messages. Mixing MSM4 and MSM7 messages will possibly lead to incorrect setting of the multiple message bit.
- If the receiver is configured to output RTCM messages on several ports, they must all have the same RTCM configuration, otherwise, the MSM multiple message bit might not be set properly.

## <span id="page-23-0"></span>**2.5 PPP-RTK configuration**

#### <span id="page-23-1"></span>**2.5.1 SPARTN corrections**

When operating as a rover, ZED-X20P can receive SPARTN corrections:

- via the internet from a service provider
- via a host application that receives L-band satellite data. For more information, see section Multiple [SPARTN](#page-24-0) sources.
- PointPerfect Flex is a u-blox service offering flexible plans and usage models on a continental scale through IP-based network and in some locations L-band satellite link. It offers wide uniform coverage and 3-6 cm accuracy and convergence in seconds. The service is continuously monitored with u-blox receivers.

#### **2.5.1.1 SPARTN protocol**

SPARTN is a binary protocol for the communication of SSR correction information.

ZED-X20P supports SPARTN as specified by SPARTN Interface Control Document – Version 2.0.2 (February, 2022).

To modify the SPARTN input/output settings, see the configuration section in the applicable Interface description [\[2\]](#page-83-1).



#### **2.5.1.2 List of supported SPARTN 2.0.2 input messages**

<span id="page-24-1"></span>

| Message type-subtype | Description                                         |
|----------------------|-----------------------------------------------------|
| SM 0-0               | GPS orbit, clock, bias (OCB)                        |
| SM 0-2               | Galileo orbit, clock, bias (OCB)                    |
| SM 0-3               | BeiDou orbit, clock, bias (OCB)                     |
| SM 1-0               | GPS high-precision atmosphere correction (HPAC)     |
| SM 1-2               | Galileo high-precision atmosphere correction (HPAC) |
| SM 1-3               | BeiDou high-precision atmosphere correction (HPAC)  |
| SM 2-0               | Geographic area definition (GAD)                    |

**Table 20: ZED-X20P supported input SPARTN version 2.0.2 messages**

- Only the messages in [Table](#page-24-1) 20 are supported. The implementation recognizes unsupported correction messages but they are not applied for the RTK solution such as QZSS correction messages, for instance.
- Group and embedded authentication messages are not supported.
- SM1 messages must contain tropospheric model for the receiver to reach an RTK fixed solution.

Application designs using ZED-X20P and SPARTN correction streams should provide firmware upgrade capability; upcoming firmware versions will implement further SPARTN messages and functionalities.

Some SPARTN correction service providers broadcast different sets of messages in different regions and support different signals or satellites. These variations may affect the accuracy of the ZED-X20P.

#### <span id="page-24-0"></span>**2.5.2 Multiple SPARTN sources**

ZED-X20P supports multiple SPARTN correction stream sources. It can support a SPARTN correction stream received over the internet (SPARTN message formatted IP stream).

Only one source can be configured to be used at a time by ZED-X20P. The configuration item CFG-SPARTN-USE\_SOURCE can be configured to select which source will be used. Alternatively, the input protocol configuration items of a physical port can be configured to block input support for the UBX or the SPARTN protocols on the desired ports, for example CFG-UART1INPROT-UBX, etc.

| Source           | Description                                                                                                                                                                                                                       | CFG-SPARTN<br>USE_SOURCE |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| SPARTN IP stream | This refers to corrections received in a SPARTN message format by any<br>interface of the ZED-X20P. The SPARTN corrections must follow the<br>SPARTN protocol specification and the source can be any SPARTN service<br>provider. | IP (default)             |

#### **Table 21: Supported SPARTN correction stream sources**

ZED-X20P provides additional monitoring information in the form of UBX-RXM-COR messages. This help to identify what the current stream status is to assist the host application in deciding which stream to use. Among other information, UBX-RXM-COR reports:

- The type/subtype of the received SPARTN messages.
- The source of the received SPARTN message (IP or L-band) and if it is used by ZED-X20P.

Additionally some SPARTN input status information is also available in other UBX messages, such as UBX-MON-COMMS. For the full message specification, see ZED-X20P Interface description [[2](#page-83-1)].



If the selected SPARTN source contains encrypted SPARTN corrections, extra monitoring information is reported through the UBX-RXM-COR, this includes, for example, information if the message is encrypted and if it has been decrypted.

#### <span id="page-25-0"></span>**2.5.3 Encrypted SPARTN support**

SPARTN messages may be encrypted as indicated by the TF004 SPARTN field (Encryption and authentication flag). ZED-X20P supports both encrypted and unencrypted SPARTN messages. The unencrypted SPARTN messages can be utilized by ZED-X20P as is without any special setup. Encrypted SPARTN messages can be decrypted and utilized by ZED-X20P once the appropriate dynamic keys have been set and the host application manages them.

Different dynamic keys apply for the IP-only stream. The type of service available to a user is specified by u-blox Terms and Services.

For information on enabling encrypted SPARTN support for the u-blox PointPerfect service, see [Table](#page-25-1) 22.

<span id="page-25-1"></span>

| Step                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Example/notes                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obtain PointPerfect<br>dynamic key                                      | Request a PointPerfect dynamic key lease.<br>The keys come in a json structure containing two dynamic<br>keys: the current key and the next key. The request can<br>be postponed if the host application already holds a json<br>structure obtained earlier and the current time falls within<br>the current key validity time.                                                                                                                                                                      | Current:<br>•<br>Key: current key in byte array format<br>•<br>Expires: current key expiring date<br>Next:<br>•<br>Key: next key in byte array format<br>•<br>Expires: next key expiring date                                                                                              |
| Check if current<br>and next dynamic<br>keys are currently<br>available | To see the current and next keys saved in ZED-X20P,<br>poll the UBX-RXM-SPARTNKEY at every power cycle<br>of or whenever the host application needs to decrypt<br>the encrypted SPARTN messages for the first time. If<br>no key is saved or both keys have expired, then no key<br>is reported. If one key is available and/or one key has<br>expired, then only one current key is reported. If two keys<br>are available and no key has expired, then both current<br>and next keys are reported. | See description of UBX-RXM-SPARTNKEY<br>message in the applicable Interface<br>description [2].                                                                                                                                                                                            |
| Set current and<br>next dynamic keys                                    | To set the current and next dynamic keys, convert the<br>json structure into a UBX-RXM-SPARTNKEY. Repeat this<br>at every power cycle, or whenever the host application<br>needs to decrypt encrypted SPARTN messages for the<br>first time, or when the dynamic keys are close to expiring<br>(e.g. only one key is available and is close to expiring), or<br>when no dynamic key has been saved.                                                                                                  | This will load the current and next dynamic<br>keys in this sequence. See the description<br>of UBX-RXM-SPARTNKEY in the applicable<br>interface description [2]. Although setting<br>the current key only is sufficient, it is<br>recommended that both current and next<br>keys are set. |
| Forward or<br>relay SPARTN<br>corrections                               | Design the host application so that SPARTN corrections<br>arrive to the ZED-X20P interfaces as SPARTN format<br>messages (over an IP stream). If there are multiple<br>SPARTN sources, the receiver only attempts to be<br>decrypt/use the one selected by the CFG-SPARTN<br>USE_SOURCE configuration item. The other available<br>SPARTN source will not be decrypted and will be reported<br>as such.                                                                                              |                                                                                                                                                                                                                                                                                            |
| Monitor decryption<br>status                                            | UBX-RXM-COR reports information on the selected<br>stream if has been encrypted and decryption has been<br>performed. Further key status information are reported<br>by the UBX-RXM-SPARTNKEY message.                                                                                                                                                                                                                                                                                               | Decryption success cannot be verified in<br>SPARTN messages                                                                                                                                                                                                                                |
| Monitor key status                                                      | UBX-RXM-SPARTNKEY reports information on the current<br>and next key and if both, one, or no key is available.                                                                                                                                                                                                                                                                                                                                                                                       | See description of UBX-RXM-SPARTNKEY<br>message in the applicable Interface<br>description [2].                                                                                                                                                                                            |



| Step                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      | Example/notes |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Key switching from<br>current to next | The host application does not need to handle the key<br>switching form current to next as long as both keys have<br>been saved in ZED-X20P. Once the current key expires, it<br>gets removed and replaced by the next key (if available).<br>In this case, only the next key is available and reported<br>as the current one. If no next key is available to become<br>current, the decryption stops and the above steps need<br>to be repeated. |               |

**Table 22: PointPerfect dynamic key handling**

#### <span id="page-26-0"></span>**2.5.4 Rover operation**

The rover operation and configuration, when using SPARTN corrections, is similar to the setup when using RTCM corrections (see RTCM rover [operation](#page-19-2)).

The float/fix carrier phase ambiguities resolution concept is maintained and, where relevant, the NMEA and UBX output contents are updated accordingly. Small adjustments are made where necessary, for example the correction source field in UBX messages will be set to SPARTN instead of RTCM.

To verify that the rover is receiving and using SPARTN or corrections, observe the following messages:

- UBX-MON-COMMS message reports which data has been received on which port.
- UBX-NAV-SIG message reports which type of corrections are applied for each signal in the field "corrSource".
- UBX-RXM-COR message reports which SPARTN messages have been received and used.

For further details, see the the applicable Interface description [[2](#page-83-1)].

Users should be aware of the datum used by the correction source. The rover position provides coordinates in the correction source reference frame. This may need to be taken into account when using the PPP-RTK rover position.

If the rover switches between different correction types (SPARTN or RTCM) it is recommended to reset the receiver before using a new type of correction

## <span id="page-26-1"></span>**2.6 OTP memory configuration**

ZED-X20P contains a one-time programmable (OTP) memory. This is a non-volatile memory for storing configuration settings and ROM patches permanently in the device. The stored data cannot be modified after it has been initially programmed.The device applies the settings and ROM patches on the device startup.

As the space in the OTP memory is limited, it should be used only for storing essential system configuration settings. The total space used for device configuration and ROM patches in the OTP memory must not exceed 150 bytes. Other settings can be stored in the BBR or sent from the host to the device on each device startup.

Ensure that the final configuration stored and optional ROM patches do not require more than 150 bytes of OTP memory space.



## <span id="page-27-0"></span>**3 Receiver functionality**

This chapter describes the ZED-X20P operational features and their configuration.

## <span id="page-27-1"></span>**3.1 Augmentation systems**

#### <span id="page-27-2"></span>**3.1.1 SBAS**

ZED-X20P is capable of receiving multiple Satellite Based Augmentation System (SBAS) signals concurrently, even from different SBAS systems (WAAS, EGNOS, BDSBAS, GAGAN, etc.).

For receiving correction data, ZED-X20P automatically chooses the best SBAS satellite as its primary source. It selects only one satellite since the information received fromotherSBASsatellites is redundant and could be inconsistent. The selection strategy is determined by the proximity of the satellites, the services offered by the satellite, the configuration of the receiver (test mode allowed/ disallowed, integrity enabled/disabled) and the signal link quality to the satellite.

If corrections are available from the chosen SBAS satellite and used in the navigation calculation, the differential status is indicated in several output messages such as UBX-NAV-PVT, UBX-NAV-STATUS, UBX-NAV-SAT, NMEA-GGA, NMEA-GLL, NMEA-RMC, and NMEA-GNS. The UBX-NAV-SBAS message provides detailed information about the corrections being available and applied. Refer to the Interface description [\[2\]](#page-83-1) for a detailed description of the messages.

The most important SBAS feature for accuracy improvement is the ionosphere correction parameters. The measured data from regional Ranging and Integrity Monitoring Stations (RIMS) are combined to make a Total Electron Content (TEC) map. This map is transferred to the receiver via SBAS satellites to correct for ionospheric delays of each received signal.

| Message type | Message content                    | Source  |
|--------------|------------------------------------|---------|
| 0(0/2)       | Test mode                          | All     |
| 1            | PRN mask assignment                | Primary |
| 2, 3, 4, 5   | Fast corrections                   | Primary |
| 6            | Integrity                          | Primary |
| 7            | Fast correction degradation        | Primary |
| 9            | Satellite navigation (ephemeris)   | All     |
| 10           | Degradation                        | Primary |
| 12           | Time offset                        | Primary |
| 17           | Satellite almanac                  | All     |
| 18           | Ionosphere grid point assignment   | Primary |
| 24           | Mixed fast / long-term corrections | Primary |
| 25           | Long-term corrections              | Primary |
| 26           | Ionosphere delays                  | Primary |

**Table 23: Supported SBAS messages**

To configure the SBAS functionality, use the CFG-SBAS configuration group.

| Parameter             | Description                                                                            |
|-----------------------|----------------------------------------------------------------------------------------|
| CFG-SIGNAL-SBAS_ENA   | Enabled/disabled status of the SBAS subsystem                                          |
| CFG-SBAS-USE_TESTMODE | Allow/disallow SBAS usage from satellites in test mode (enable when BDSBAS is<br>used) |
| CFG-SBAS-USE_RANGING  | Use the SBAS satellites for navigation (ranging)                                       |



| Parameter                         | Description                                                                                                                    |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| CFG-SBAS-USE_DIFFCORR             | Combined enable/disable switch for fast, long-term, and ionosphere corrections                                                 |
| CFG-SBAS-USE_INTEGRITY            | Apply integrity information data                                                                                               |
| CFG-SBAS<br>ACCEPT_NOT_IN_PRNMASK | Allow usage of SBAS data even when SBAS SV is not included in PRN MASK<br>(Compatible only with BDSBAS, enable BDSBAS is used) |
| CFG-SBAS-USE_IONOONLY             | Allow/disallow usage of SBAS ionospheric corrections only (enabled by default)                                                 |
| CFG-SBAS-PRNSCANMASK              | Allows selectively enabling/disabling SBAS satellites (BDSBAS disabled by default)                                             |

**Table 24: SBAS configuration parameters**

- When SBAS integrity data is applied, the navigation engine stops using all signals for which no integrity data is available (including all non-GPS signals). It is not recommended to enable SBAS integrity on borders of SBAS service regions in order not to inadvertently restrict the number of available signals.
- SBAS integrity information is required for at least five GPS satellites. If this condition is not met, SBAS integrity data will not be applied.
- SBAS is only used if no correction services are available. If the connection stream is lost during the operation, the receiver will switch to using the SBAS corrections after the time set in CFG-NAVSPG-CONSTR\_DGNSSTO (60 s by default) has elapsed.
- When the receiver switches from a solution using correction data to a standard position solution, the reference frame of the output position switches as well. For an SBAS solution, the reference frame is aligned within a few centimeters of WGS84 (and modern ITRF realizations).
- Although u-blox receivers try to select the best available SBAS correction data, it is recommended to configure them to exclude the unwanted SBAS satellites.

Each satellite serves a specific region and its correction signal is only useful within that region. Planning is crucial to determine the best possible configuration, especially in areas where signals from different SBAS systems can be received:

- **Example 1 - SBAS receiver in North America:** In eastern parts of North America, make sure that EGNOS satellites do not take preference over WAAS satellites. The satellite signals from the EGNOS system should be disallowed by using the PRN scan mask (configuration key CFG-SBAS-PRNSCANMASK).
- **Example 2 - SBAS receiver in Europe:** Some WAAS satellite signals can be received in some parts of western Europe and GAGAN SBAS satellites in other parts of Europe. Therefore, it is recommended that satellites from all but the EGNOS system are disabled using the PRN scan mask.

#### <span id="page-28-0"></span>**3.1.2 BeiDou SBAS configuration**

BeiDou satellite based augmentation system (BDSBAS) provides SBAS services to China and surrounding regions. BDSBAS is integrated in the BeiDou system and uses BDS-3 type satellites to broadcast SBAS L1/L5 signal, providing augmentation for GPS system.

BeiDou SBAS is in testing mode and it is not enabled by default. Enabling Beidou SBAS may improve navigation solution by its correction data. To enable the BeiDou SBAS functionality, configure the following configuration items.

<span id="page-28-1"></span>

| Configuration item             | Value              |
|--------------------------------|--------------------|
| CFG-SBAS-ACCEPT_NOT_IN_PRNMASK | BDSBAS             |
| CFG-SBAS-PRNSCANMASK           | 0x0000000001800400 |
| CFG-SBAS-USE_DIFFCORR          | TRUE (default)     |



| Configuration item     | Value           |
|------------------------|-----------------|
| CFG-SBAS-USE_INTEGRITY | FALSE (default) |
| CFG-SBAS-USE_IONOONLY  | FALSE (default) |
| CFG-SBAS-USE_RANGING   | FALSE           |
| CFG-SBAS-USE_TESTMODE  | TRUE            |

**Table 25: BeiDou SBAS configuration item**

- BeiDou SBAS is still in testing mode and it has not been officially released for operational use. Do not use it for safety related applications.
- The CFG-SBAS-PRNSCANMASK in [Table](#page-28-1) 25 includes only BeiDou SBAS PRNs. Alternatively, the BeiDou SBAS PRNs can be added to the default list of PRNs enabled in the firmware or modified list of PRNs that is configured. This allows other SBAS systems to be used if BeiDou SBAS is not available.

### <span id="page-29-0"></span>**3.2 Communication interfaces and PIOs**

u-blox receivers are equipped with a communication interface which is multi-protocol capable. The interface ports can be used to transmit GNSS measurements, monitor status information and configure the receiver.

A protocol (e.g. UBX, NMEA) can be assigned to several ports simultaneously, each configured with individual settings (e.g. baud rate, message rates, etc.). More than one protocol (e.g. UBX protocol and NMEA) can be assigned to a single port (multi-protocol capability), which is particularly useful for debugging purposes.

The ZED-X20P provides UART1, UART2, SPI and I2C interfaces for communication with a host CPU. The interfaces are configured via the configuration methods described in the applicable interface description [\[2\]](#page-83-1).

| Port no. | UBX-MON-COMMS portId | Electrical interface |
|----------|----------------------|----------------------|
| 0        | 0x0000               | I2C                  |
| 1        | 0x0100               | UART1                |
| 2        | 0x0200               | UART2                |
| 3        | 0x0400               | SPI                  |

The following table shows the port numbers reported in the UBX-MON-COMMS messages.

#### **Table 26: Port number assignment**

When **VCC** is removed, it is important to isolate the interface pins. They can be allowed to float or they can be connected to a high impedance.

#### <span id="page-29-1"></span>**3.2.1 UART**

ZED-X20P supports a Universal Asynchronous Receiver/Transmitter (UART) port consisting of an RX and a TX line. The UART can be used as a host interface which supports a configurable baud rate and protocol selection.

The UART interface does not support handshaking signals or hardware flow control signals.

The UART baud rate can be configured for selected speeds. Only the rates listed in [Table](#page-30-1) 27 are supported for transmission and reception.

The UART RX interface is disabled when more than 100 frame errors are detected during a onesecond period.This can happen if the wrong baud rate is used or the **UART RX** pin is grounded. An



error message appears when the UART RX interface is re-enabled at the end of the one-second period.

<span id="page-30-1"></span>

| Baud rate | Data bits | Parity | Stop bits |
|-----------|-----------|--------|-----------|
| 4800      | 8         | none   | 1         |
| 9600      | 8         | none   | 1         |
| 19200     | 8         | none   | 1         |
| 38400     | 8         | none   | 1         |
| 57600     | 8         | none   | 1         |
| 115200    | 8         | none   | 1         |
| 230400    | 8         | none   | 1         |
| 460800    | 8         | none   | 1         |
| 921600    | 8         | none   | 1         |
| 2000000   | 8         | none   | 1         |
| 4000000   | 8         | none   | 1         |
| 8000000   | 8         | none   | 1         |
|           |           |        |           |

#### **Table 27: Possible UART interface configurations**

Allow a short time delay of typically 100 ms between sending a baud rate change message and providing input data at the new rate. Otherwise some input characters may be ignored or the port could be disabled until the interface is able to process the new baud rate.

If there is too much data for the interface's bandwidth, the output buffer may overflow. Once the buffer space is exceeded, new messages to be sent will be dropped. To prevent message loss, the baud rate and the number of enabled messages should be selected carefully.

#### <span id="page-30-0"></span>**3.2.2 I2C**

An I2C interface is available for communication with an external host CPU in the I2C Fast-mode. Backwards compatibility with the Standard-mode I2C bus operation is not supported. The interface can be operated only in the peripheral mode with the maximum bit rate of 400 kbit/s. The interface can make use of clock stretching by holding the **SCL** line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms.

The **SCL** and **SDA** pins have internal pull-up resistors which should be sufficient for most applications. However, depending on the clock speed of the host and the capacitive load on the I2C lines, additional external pull-up resistors may be necessary. The higher the speed and the capacitance load, the lower the pull-up resistor needs to be.

To poll or set the I2C address, use the CFG-I2C-ADDRESS configuration item. Refer to Interface description [] for details. The CFG-I2C-ADDRESS configuration item is an 8-bit value containing the I2C address in the 7 most significant bits plus a 0 as the least significant bit. Thus, the default address becomes 0x84(1000 0100).

In designs where the host uses the same I2C bus to communicate with more than one u-blox receiver, each receiver's I2C address must be configured with a different value.

#### <span id="page-30-2"></span>**3.2.2.1 I2C register layout**

As shown in [Figure](#page-31-0) 6, there are 256 registers.The data registers 0 to 252, at addresses 0x00 to 0xFC, contain reserved information and must not be used. Hence, only the last three registers are left for communication. The registers 0xFD and 0xFE contain the currently available number of bytes to be read, while the register 0xFF buffers the message stream. The 0xFF address delivers a 0xFF byte value if there is no data awaiting for transmission, or all the bytes have been read.



<span id="page-31-0"></span>



#### **3.2.2.2 Read access types**

The host can choose one of the following two modes:

- Random read access: the controller first reads the number of available bytes at the 0xFD and 0xFE before accessing the data at 0xFF.
- Current address read access: the controller directly reads the data at the register 0xFF, without knowing first if there is any data waiting. If there is no data, the read result is a 0xFF byte value. This mode basically skips the first step of the "random read access", as it does not address to any particular register.

[Figure](#page-32-0) 7 shows the format of the "random access" form of the request.

Following the start condition from the controller, the 7-bit device address and the R/W bit (which is a logic low for write access) are clocked onto the bus by the controller transmitter. The receiver answers with an acknowledge (logic low) to indicate that it recognizes the address.

Next, the 8-bit address of the register to be read must be written to the bus (0xFD for u-blox receivers). Following the receiver's acknowledgment, the controller again triggers a start condition and writes the device address, but this time the R/W bit is a logic high to initiate the read access. Now, the controller can read 1 to N bytes from the receiver. The receiver will first deliver the byte value at 0xFD, followed by the value at 0xFE. At this point the controller knows the number of bytes waiting at the 0xFF register, and by acknowledging again, the data stream follows.The data transfer will stop once the controller emits a not-acknowledge response or a stop condition is triggered after the last byte has been read.



<span id="page-32-0"></span>

**Figure 7: I2C random read access**

If "current address" is used, an address pointer in the receiver is used to determine which register to read. This address pointer will increment after each read operation unless it is already pointing at register 0xFF, the highest addressable register, in which case it remains unaltered.

The initial value of this address pointer at startup is 0xFF, so by default all current address read operations will repeatedly read register 0xFF and receive the next byte of message data (or 0xFF value if no message data is waiting).



**Figure 8: I2C current address read access**

Only after addressing the peripheral, the receiver starts the data stream. If the controller does not read data from the receiver for a certain timeout, the receiver assumes that the communication is broken and stops the data stream, preventing an overflow of the output buffer. This timeout is 1.5 seconds by default. However, it can be extended by setting the CFG-I2C-EXTENDEDTIMEOUT configuration item to true. Refer to the Interface description [[2](#page-83-1)] for details. By disabling the timeout, the receiver will only interrupt the data stream when the buffer is full. The buffer can store up to 4 kB and the time for an overflow event depends on the number of messages enabled.

#### **3.2.2.3 Write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. Therefore, the register set mentioned in section [I2C](#page-30-2) [register](#page-30-2) layout is not writeable.



Following the start condition from the controller, the 7-bit device address and the R/W bit (which is a logic low for write access) are clocked onto the bus by the controller. The receiver answers with an acknowledge (logic low) response to indicate that it is responsible for the given address.

The controller can write 2 to N bytes to the receiver, generating a stop condition after the last byte being written. To properly distinguish from the write access to set the address counter in random read accesses, the number of data bytes must be at least 2.





#### <span id="page-33-0"></span>**3.2.3 SPI**

The ZED-X20P has an SPI peripheral interface that can be selected by setting **D\_SEL** = 0. The SPI peripheral interface is shared with UART1 and I2C port, the physical pins are same. The SPI pins available are:

- **SPI\_SDO (TXD)**
- **SPI\_SDI (RXD)**
- **SPI\_CS\_N**
- **SPI\_CLK**

For more information about the communication interface selection, see [D\\_SEL.](#page-34-1)

The SPI interface is designed to allow communication to a host CPU and thus, the interface can only be operated in peripheral mode.

The SPI interface transmits data in Most Significant Bit (MSB) first order.

#### **3.2.3.1 Read access**

The register mode is not implemented for the SPI interface and thus, the NMEA and UBX message stream is accessible using the [Back-to-back](#page-34-2) read and write access implementation. When no data is available to be written to the receiver, **SDI** should be held logic high, i.e., all bytes written to the receiver are set to 0xFF.

To prevent the receiver from being busy parsing incoming data, the parsing process is stopped after 50subsequent bytes containing0xFF.The parsing process is re-enabled with thefirst byte not equal to 0xFF.

If the receiver has no more data to send, it sets **SDO** to logic high, i.e. all bytes transmitted decode to 0xFF. An efficient parser in the host will ignore all 0xFF bytes which are not part of a message and will resume data processing as soon as the first byte not equal to 0xFF is received.



#### <span id="page-34-2"></span>**3.2.3.2 Back-to-back read and write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. For every byte written to the receiver, a byte will simultaneously be read from the receiver. While the controller writes to **SDI** of the peripheral, at the same time it needs to read from **SDO** of the peripheral, as any pending data will be output by the receiver with this access. The data on **SDO** represents the results from a current address read, returning 0xFF when no more data is available.



**Figure 10: SPI back-to-back read/write access**

#### <span id="page-34-0"></span>**3.2.4 Predefined PIOs**

This section describes the PIOs supported by ZED-X20P. All PIO active voltage levels are referenced to the **VCC** supply voltage. All the inputs have internal pull-up resistors in normal operation and can be left open if unused.

#### <span id="page-34-1"></span>**3.2.4.1 D\_SEL**

The **D\_SEL** pin can be used to configure the functionality of the combined UART1, I2C, and SPI pins. It is possible to configure the pins as UART1 + I2C, or as SPI. SPI is not available unless **D\_SEL** pin is set to low. See [Table](#page-34-3) 28 below.

<span id="page-34-3"></span>

| Pin no. | D_SEL == 0 | D_SEL == 1 |
|---------|------------|------------|
| 42      | SPI_SDO    | UART1 TXD  |
| 43      | SPI_SDI    | UART1 RXD  |
| 44      | SPI_CS_N   | I2C SDA    |
| 45      | SPI_CLK    | I2C SCL    |

#### **Table 28: D\_SEL configuration**

#### <span id="page-34-4"></span>**3.2.4.2 RESET\_N**

The ZED-X20P provides a **RESET\_N** pin to reset the receiver. The **RESET\_N** pin is input-only with an internal pull-up resistor and can be left open for normal operation. Driving **RESET\_N** low for at least 100 ms will trigger a reset of the receiver. The **RESET\_N** complies with the **VCC** level and can be actively driven high.

- The **RESET\_N** pin will delete all information and trigger a cold start. It should only be used as a recovery option.
- No capacitor should be placed at **RESET\_N** to GND, otherwise it could trigger a reset on every startup.



#### **3.2.4.3 SAFEBOOT\_N**

The ZED-X20P provides a **SAFEBOOT\_N** pin that is used to command the receiver safeboot mode.

If this pin is low at power up, the receiver starts in safeboot mode and GNSS operation is disabled.

The safeboot mode can be used to recover from situations where the flash content has become corrupted and needs to be restored.

In this mode UART1, I2C or SPI communication is possible. For communication via UART1 in safeboot mode, the host must send a training sequence (0x55 0x55 at 9600 baud) to the receiver in order to begin communication. After this the host must wait at least 2 ms before sending any data.

It is recommended to have the possibility to pull the **SAFEBOOT\_N** pin low in the application. This can be provided using an externally connected test point or a host I/O port.

#### **3.2.4.4 TIMEPULSE**

The ZED-X20P features one time pulse output at the **TIMEPULSE** pin.

More information about the time pulse feature and its configuration can be found in the Time [pulse](#page-46-0) section.

#### **3.2.4.5 TX\_READY**

This feature enables each port to define a corresponding pin, which indicates if bytes are ready to be transmitted. A listener can wait on the **TX\_READY** signal instead of polling the I2C or SPI interfaces. The CFG-TXREADY configuration group lets you configure the polarity and the number of bytes in the buffer before the **TX\_READY** signal goes active. By default, this feature is disabled. If the number of pending bytes reaches the threshold configured for this port, the corresponding pin will become active (configurable active-low or active-high), and stay active until the last bytes have been transferred from software to hardware.

This is not necessarily equal to all bytes transmitted, i.e. after the pin has become inactive, up to 16 bytes might still need to be transferred to the host.

The **TX\_READY** pin can be selected from all PIOs which are not in use (see UBX-MON-HW3 in the applicable interface description [\[2\]](#page-83-1) for a list of the PIOs and their mapping). Each **TX\_READY** pin is exclusively associated to one port and cannot be shared. If PIO is invalid or already in use, only the configuration for the specific **TX\_READY** pin is ignored, the rest of the port configuration is applied if valid. The acknowledge message does not indicate if the **TX\_READY** configuration is successfully set, it only indicates the successful configuration of the port. To validate successful configuration of the **TX\_READY** pin, the port configuration should be read back and the settings of **TX\_READY** feature verified (will be set to disabled/all zero if the settings are invalid).

The threshold when **TX\_READY** is asserted should not be set above 2 kB as it is possible that the internal message buffer limit is reached before this. This results in the **TX\_READY** pin never being set as the messages are discarded before the threshold is reached.

#### **3.2.4.5.1 Extended TX timeout**

If the host does not communicate over SPI or I2C for more than approximately 2 seconds, the device assumes that the host is no longer using this interface and no more packets are scheduled for this port. This mechanism can be changed by enabling "extended TX timeouts", in which case the receiver delays idling the port until the allocated and undelivered bytes for this port reach 4 kB. This feature is especially useful when using the **TX\_READY** feature with a message output rate of less than once per second, and polling data only when data is available, determined by the **TX\_READY** pin becoming active.



#### **3.2.4.6 EXTINT**

**EXTINT** is an external interrupt pin with fixed input voltage thresholds with respect to **VCC**. It can be used for functions such as accurate external frequency aiding and on/off control. The external frequency aiding can be used to calibrate the clock. This enables faster fix of satellite signals (UBX-MGA-INI-FREQ or UBX-MGA-INI-TIME\_XXX) and can be used during normal operation or during the production test. Another possibility to use the extint feature is to wake up the receiver after putting it into backup mode; this can be set up with UBX-RXM-PMREQ. Leave open if unused, this function is disabled by default.

#### **3.2.4.7 GEOFENCE\_STAT pin**

The ZED-X20P provides a **GEOFENCE\_STAT** pin that indicates the current geofence status as to whether the receiver is inside any of the active areas.

This feature can be used for example to wake up a sleeping host when a defined geofence condition is reached. It is possible to configure up to four circular areas as geofence locations. Once configured, the receiver continuously compares its current position with the preset geofenced areas.

The receiver toggles the assigned pin according to the combined geofence state of all areas.

There are three possible outcomes for each geofence:

- *Inside* The position is inside the geofence with the configured confidence level
- *Outside* The position lies outside of the geofence with the configured confidence level
- *Unknown* There is no valid position solution or the position uncertainty does not allow for unambiguous state evaluation

The **GEOFENCE\_STAT** pin is always set to high level when the combined geofence state is unknown. The low level can either represent the inside state or the outside state according to the value set in the CFG-GEOFENCE-PINPOL configuration item. If the receiver is in software backup or in a reset, the pin will go to high accordingly.

See [Geofencing](#page-0-0) for more information.

#### **3.2.4.8 RTK\_STAT pin**

The ZED-X20P provides an **RTK\_STAT** pin that provides an indication of the RTK positioning status. It can be used to confirm if a valid stream of correction messages is being received. As valid correction messages we only consider the correction messages that are supported and used by the receiver.

The **RTK\_STAT** pin status can be mapped to the carrSoln field of the UBX-NAV-PVT and interpreted as follows:

- An active low pin level indicates that RTK fixed mode has been achieved
- Alternating (blinking) pin level, indicates that a valid stream of correction messages is being received and utilized but no RTK fixed mode has been achieved
- An active high pin level indicates that no carrier phase solution is available

### <span id="page-36-0"></span>**3.3 Antenna supervisor**

The antenna supervisor provides means to detect open and short circuits in the active antenna supply circuit by observing the signals described in [Table](#page-37-5) 29. Furthermore, it can shut off the antenna supply if a short circuit is detected. Configure the antenna monitor as discussed in section Antenna supervisor [configuration](#page-15-1). If enabled, the antenna supervisor provides the antenna status



as discussed in section Antenna status [reporting.](#page-37-4) For details about the required circuit, refer to section Antenna [supervisor](#page-64-0) circuit.

<span id="page-37-5"></span>

| Signal      | Pin | Description                                       |
|-------------|-----|---------------------------------------------------|
| ANT_DETECT  | 4   | See Antenna open circuit detection (ANT_DETECT) . |
| ANT_SHORT_N | 6   | See Antenna short detection (ANT_SHORT_N).        |
| ANT_OFF     | 5   | See Antenna voltage control (ANT_OFF).            |

**Table 29: Antenna supervisor signals**

#### <span id="page-37-0"></span>**3.3.1 Antenna voltage control (ANT\_OFF)**

Antenna voltage control allows the receiver to control the external LNA with the ANT\_OFF signal. The antenna voltage control is enabled by default in ZED-X20P with the CFG-HW-ANT\_CFG\_VOLTCTRL configuration item set to 1 (true). The receiver provides the antenna status in UBX-MON-RF and UBX-INF-NOTICE messages only if the antenna voltage control has been enabled. For more details, see section Antenna status [reporting](#page-37-4).

#### <span id="page-37-1"></span>**3.3.2 Antenna short detection (ANT\_SHORT\_N)**

Antenna short detection allows the receiver to detect short circuits in the antenna supply circuit with the ANT\_SHORT\_N signal. Enable the antenna short detection by setting the CFG-HW-ANT\_CFG\_SHORTDET configuration item to 1 (true). Change also the ANT\_SHORT\_N polarity with the CFG-HW-ANT\_CFG\_SHORTDET\_POL configuration item if required by the design.

Furthermore, consider enabling the CFG-HW-ANT\_CFG\_PWRDOWN feature to allow the receiver to automatically disable the external LNA with the LNA\_EN signal when it detects a short circuit. For more details, see section Antenna supervisor [configuration](#page-15-1).

If the receiver detects a short circuit, it continues reporting the antenna status as a "SHORT" until the next power cycle or switching the detection off and on again, or until the status is recovered by the [auto-recovery](#page-37-2) feature. For more details, see section Antenna status [reporting](#page-37-4).

#### <span id="page-37-2"></span>**3.3.3 Antenna short detection auto-recovery**

Antenna short detection auto-recovery allows the receiver to retest the short circuit condition after a timeout period of 60 seconds by enabling the antenna supply. Consequently, the receiver recovers the antenna supply if it doesn't detect a short circuit. Enable the auto-recovery by setting the CFG-HW-ANT\_CFG\_RECOVER configuration item to 1 (true) as discussed in section Antenna [supervisor](#page-15-1) [configuration.](#page-15-1)

#### <span id="page-37-3"></span>**3.3.4 Antenna open circuit detection (ANT\_DETECT)**

Antenna open circuit detection allows the receiver to detect open circuit in the antenna supply circuit with the ANT\_DETECT signal. Enable the antenna open circuit detection by setting the CFG-HW-ANT\_CFG\_OPENDET configuration item to 1 (true) as discussed in section Antenna [supervisor](#page-15-1) [configuration.](#page-15-1) If required by the design, also change the ANT\_DETECT polarity with the CFG-HW-ANT\_CFG\_OPENDET configuration item.

#### <span id="page-37-4"></span>**3.3.5 Antenna status reporting**

The receiver reports the antenna detection and antenna power status over the UBX-MON-RF and NMEA notice messages. The UBX-MON-RF message reports the antenna status in the antStatus



and antPower fields as summarized in [Table](#page-38-0) 30. [Table](#page-38-1) 31 provides examples of use cases for the NMEA notice messages. For more information, refer to the Interface description [[2](#page-83-1)].

<span id="page-38-0"></span>

| UBX-MON-RF | Status          | Description                                                                                                                                                                                                                                            |
|------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| antStatus  | 0x00 (INIT)     | CFG-HW-ANT_VOLTCTRL is enabled and antenna voltage control has been<br>initialized.                                                                                                                                                                    |
|            | 0x01 (DONTKNOW) | Antenna status is unknown.                                                                                                                                                                                                                             |
|            | 0x02 (OK)       | Antenna has been detected and no short has been detected.                                                                                                                                                                                              |
|            | 0x03 (SHORT)    | A short has been detected from the antenna input. That is, a lot of current is<br>drawn from the active antenna supply circuit.                                                                                                                        |
|            | 0x04 (OPEN)     | No antenna is detected. That is, little or no current is drawn from the active<br>antenna supply circuit.                                                                                                                                              |
| antPower   | 0x00 (OFF)      | GNSS is OFF or CFG-HW-ANT_PWRDOWN is enabled and a short has been<br>detected. This status also applies when GNSS has been restarted via UBX-CFG<br>RST, the GNSS selection has been reconfigured or when GNSS has been stopped<br>in the backup mode. |
|            | 0x01 (ON)       | GNSS is ON and no short/open is detected from the antenna input. This status<br>also applies when there is a short and CFG-HW-ANT_PWRDOWN is not enabled.                                                                                              |
|            | 0x02 (DONTKNOW) | CFG-HW-ANT_VOLTCTRL is not configured.                                                                                                                                                                                                                 |

**Table 30: Antenna detection and antenna power status**

<span id="page-38-1"></span>

| NMEA notice message output                     | Use case and description                                                   |  |
|------------------------------------------------|----------------------------------------------------------------------------|--|
| \$GNTXT,01,01,02,ANTSUPERV=AC*00               | Antenna voltage control (AC) is active: ANTSUPERV=AC.                      |  |
| \$GNTXT,01,01,02,ANTSTATUS=INIT*3B             |                                                                            |  |
| \$GNTXT,01,01,02,ANTSTATUS=OK*25               |                                                                            |  |
| \$GNTXT,01,01,02,ANTSUPERV=AC SD *37           | Antenna short circuit detection (SD) is active: ANTSUPERV=AC               |  |
| \$GNTXT,01,01,02,ANTSTATUS=INIT*3B             | SD.                                                                        |  |
| \$GNTXT,01,01,02,ANTSTATUS=OK*25               | \$GNTXT,01,01,02,ANTSTATUS=SHORT*73, a short circuit<br>has been detected. |  |
| \$GNTXT,01,01,02,ANTSUPERV=AC SD PDoS SR*3E    | Antenna short detection auto-recovery (SR) and the power                   |  |
| \$GNTXT,01,01,02,ANTSTATUS=INIT*3B             | down antenna logic CFG-HW-ANT_CFG_PWRDOWN (PDoS) are                       |  |
| \$GNTXT,01,01,02,ANTSTATUS=OK*25               | active: ANTSUPERV=AC SD OD PDoS SR.                                        |  |
| \$GNTXT,01,01,02,ANTSUPERV=AC SD OD PDoS SR*15 | Antenna<br>open<br>circuit<br>detection<br>(OD)<br>is<br>activated:        |  |
| \$GNTXT,01,01,02,ANTSTATUS=INIT*3B             | ANTSUPERV=AC SD OD PDoS SR.                                                |  |
| \$GNTXT,01,01,02,ANTSTATUS=OK*25               | \$GNTXT,01,01,02,ANTSTATUS=OPEN*35, an open circuit<br>has been detected.  |  |

**Table 31: Antenna status in NMEA notice messages**

The reported output depends on the physical state of the antenna as shown in [Table](#page-38-2) 32. The short detection takes priority over the open detection and the "X" implies an unconfigured or undetected physical state.

<span id="page-38-2"></span>

|      | Configuration keys |         |         |         |                            | Physical antenna state |          | Reported antenna status |
|------|--------------------|---------|---------|---------|----------------------------|------------------------|----------|-------------------------|
|      | VOLTCTRL SHORTDET  | OPENDET | PWRDOWN | RECOVER | Short circuit Open circuit |                        | antPower | antStatus               |
| TRUE | X                  | X       | X       | X       | NO                         | NO                     |          |                         |
| TRUE | FALSE              | X       | X       | X       | X                          | NO                     |          |                         |
| TRUE | X                  | FALSE   | X       | X       | NO                         | X                      | ON       | OK                      |
| TRUE | FALSE              | FALSE   | X       | X       | X                          | X                      |          |                         |
| TRUE | FALSE              | TRUE    | X       | X       | X                          | YES                    |          |                         |
| TRUE | X                  | TRUE    | X       | X       | NO                         | YES                    | ON       | OPEN                    |



| Configuration keys |                   |         |         |         | Physical antenna state     | Reported antenna status |          |           |
|--------------------|-------------------|---------|---------|---------|----------------------------|-------------------------|----------|-----------|
|                    | VOLTCTRL SHORTDET | OPENDET | PWRDOWN | RECOVER | Short circuit Open circuit |                         | antPower | antStatus |
| TRUE               | TRUE              | X       | FALSE   | X       | YES                        | X                       | ON       | SHORT     |
| TRUE               | TRUE              | X       | TRUE    | X       | YES                        | X                       | OFF      | SHORT     |
| FALSE              | TRUE              | X       | X       | X       | YES                        | X                       | DONTKNOW | SHORT     |
| FALSE              | FALSE             | TRUE    | X       | X       | X                          | YES                     |          |           |
| FALSE              | X                 | TRUE    | X       | X       | NO                         | YES                     | DONTKNOW | OPEN      |

**Table 32: Antenna supervisor configuration and antenna states**

### <span id="page-39-0"></span>**3.4 Receiver reset and startup**

Forcing the receiver reset and defining its startup mode can be used to control the receiver's startup performance and behavior.

#### <span id="page-39-1"></span>**3.4.1 Reset types**

Forcing receiver resets can help observe the effects of maintaining or losing data stored in RAM and/or BBR between restarts. Use the UBX-CFG-RST message to trigger a reset, specifying the type with the resetMode field to either clear or maintain navigation data in RAM and clear the RTC. Additionally, you can use the navBbrMask to initiate a cold, warm, or hot start configuration, or to define specific BBR data sections to be cleared, as detailed in the Interface description [[2](#page-83-1)]. [Table](#page-39-3) 33 outlines all the available reset types, detailing how each one affects the RTC and the data stored in BBR and RAM.

<span id="page-39-3"></span>

| Immediate hardware reset (watchdog):<br>Uses the on-chip watchdog to electrically reset the chip as an                                          | All        | All       |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------|-----|
|                                                                                                                                                 |            |           | Yes |
| immediate asynchronous reset without generating stop events.                                                                                    |            |           |     |
| Hardware reset (watchdog) after shutdown:                                                                                                       | All        | All       | Yes |
| Uses the on-chip watchdog to reset the receiver after shutdown.                                                                                 |            |           |     |
| Controlled Software reset:                                                                                                                      | All        | Selection | No  |
| Terminates all running processes and restarts the receiver.                                                                                     |            |           |     |
| Controlled Software reset (GNSS only):                                                                                                          | Navigation | Selection | No  |
| Restarts<br>only<br>the<br>GNSS-related<br>processing<br>and<br>clears<br>the<br>navigation data in RAM without reinitializing the full system. |            |           |     |
| Controlled GNSS stop:                                                                                                                           | Navigation | Selection | No  |
| Stops only the GNSS-related processing and clears the navigation<br>data in RAM without reinitializing the full system.                         |            |           |     |
| Controlled GNSS start:                                                                                                                          | Navigation | Selection | No  |
| Starts only the GNSS-related processing and clears the navigation<br>data in RAM without reinitializing the full system.                        |            |           |     |
| Hardware reset by the RESET_N pin:                                                                                                              | All        | All       | Yes |
| Resets the chip immediately as discussed in section RESET_N.                                                                                    |            |           |     |
|                                                                                                                                                 |            |           |     |

**Table 33: Available reset types**

A receiver reset doesn't clear data or configurations stored in the flash memory.

#### <span id="page-39-2"></span>**3.4.2 Startup modes**

GNSS receivers typically make a distinction between cold, warm and hot start modes based on the valid information the receiver has during the restart. Thus, the startup modes differ by means of TTFF and accuracy as the receiver can calculate the position and velocity data only when it receives



enough signals from satellites with a valid ephemeris. [Table](#page-40-3) 34 describes the different startup modes. Refer to the Data sheet for the startup performance specifications [].

<span id="page-40-3"></span>

| Startup mode | Description                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cold start   | •<br>The receiver starts in a cold start mode if it has no information about the last position, time,<br>velocity, frequency and the currently available satellites (almanac or ephemeris).      |
|              | •<br>In a cold start, the receiver must search through the full time and frequency space for all supported<br>satellite signals to find and track satellite signals.                             |
|              | •<br>Once the receiver has found and started tracking a signal, it usually takes 18-36 seconds to decode<br>the satellite's ephemeris under strong signal conditions.                            |
|              | •<br>Some GNSS receiver manufacturers call the cold start mode a factory startup mode.                                                                                                           |
| Warm start   | •<br>The receiver starts in the warm start mode if it has approximate information for time, position and<br>satellite position (almanac).                                                        |
|              | •<br>The receiver needs to download the ephemeris from the satellites prior calculating a PVT solution.                                                                                          |
| Hot start    | •<br>The receiver starts in the hot start mode if it has a valid ephemeris, RTC and the last position<br>available.                                                                              |
|              | •<br>A hot start is achievable after any controlled software reset or when restarting from the backup<br>mode as the satellite ephemeris and RTC are maintained in the receiver's backup domain. |
|              | •<br>From the backup mode, hot starts are possible for up to 4 hours until the ephemeris data expires.                                                                                           |
| Aided start  | •<br>The receiver starts in the aided start mode if it is assisted upon the startup as described in section<br>Multiple GNSS assistance (MGA).                                                   |
|              | •<br>The startup performance depends on the quality and the latency of the assistance data.                                                                                                      |

**Table 34: Receiver startup modes**

## <span id="page-40-0"></span>**3.5 Time**

Maintaining receiver local time and keeping it synchronized with GNSS time is essential for proper timing and positioning functionality. This section explains how the receiver maintains local time and introduces the supported GNSS time bases.

#### <span id="page-40-1"></span>**3.5.1 Receiver local time**

The receiver is dependent on a local oscillator for both the operation of its radio parts and also for timing within its signal processing. No matter what nominal frequency the local oscillator has, u-blox receivers subdivide the oscillator signal to provide a 1-kHz reference clock signal, which is used to drivemany of the receiver's processes. In particular, themeasurement of satellite signals is arranged to be synchronized with the "ticking" of this 1-kHz clock signal.

When the receiver first starts, it has no information about how these clock ticks relate to other time systems; it can only count time in 1 millisecond steps. However, as the receiver derives information from the satellites it is tracking or from aiding messages, it estimates the time that each 1-kHz clock tick takes in the time base of the chosen GNSS system. This estimate of GNSS time based on the local 1-kHz clock is called receiver local time.

As receiver local time is a mapping of the local 1-kHz reference onto a GNSS time base, it may experience occasional discontinuities, especially when the receiver first starts up and the information it has about the time base is changing. Indeed, after a cold start, the receiver local time initially indicates the length of time that the receiver has been running. However, when the receiver obtains some credible timing information from a satellite or an aiding message, it jumps to an estimate of GNSS time.

#### <span id="page-40-2"></span>**3.5.2 GNSS time bases**

GNSS receivers must handle a variety of different time bases as each GNSS has its own reference system time. What is more, although each GNSS provides a model for converting their system time into UTC, they all support a slightly different variant of UTC. So, for example, GPS supports a variant



of UTC as defined by the US National Observatory, while BeiDou uses UTC from the National Time Service Center (NTSC) of China. While the different UTC variants are normally closely aligned, they can differ by as much as a few hundreds of nanoseconds.

Although u-blox receivers can combine a variety of different GNSS times internally, the user must choose a single source of GNSS time and, separately, a single type of UTC for input (on **EXTINT** pins) and output (via the **TIMEPULSE** pin) and the parameters reported in corresponding messages.

The CFG-TP-TIMEGRID\_TP configuration item allows the user to choose between any of the supported GNSS (GPS, BeiDou, etc.) time bases and UTC. Also, the CFG-NAVSPG-UTCSTANDARD configuration item allows the user to select which variant of UTC the receiver should use. This includes an "automatic" option which causes the receiver to select an appropriate UTC version itself, based on the GNSS configuration, using, in order of preference, USNO if GPS is enabled, NTSC if BeiDou is enabled,

The receiver assumes that an input time pulse uses the same GNSS time base as specified for the time pulse output. Where UTC is selected for time pulse output, any GNSS time pulse input will be assumed to be aligned to GPS time.

The receiver allows users to independently choose GNSS signals used in the receiver (using the CFG-SIGNAL configuration group) and the input/output time base (using the CFG-TP configuration group). For example it is possible to instruct the receiver to use GPS satellite signals to generate BeiDou time. This practice compromises time pulse accuracy if the receiver cannot measure the timing difference between the constellations directly and is therefore not recommended.

The information that allows GNSS times to be converted to the associated UTC times is only transmitted by the GNSS at relatively infrequent periods. For example GPS transmits UTC(USNO) information only once every 12.5 minutes. Therefore, if a time pulse is configured to use a variant of UTC time, after a cold start, substantial delays before the receiver has sufficient information to start outputting the time pulse can be expected.

Each GNSS has its own time reference for which detailed and reliable information is provided in the messages listed in the table below.

| Time reference | Message          |
|----------------|------------------|
| GPS time       | UBX-NAV-TIMEGPS  |
| BeiDou time    | UBX-NAV-TIMEBDS  |
| Galileo time   | UBX-NAV-TIMEGAL  |
| QZSS time      | UBX-NAV-TIMEQZSS |
| UTC time       | UBX-NAV-TIMEUTC  |

**Table 35: GNSS time messages**

#### <span id="page-41-0"></span>**3.5.3 Navigation epochs**

Each navigation solution is triggered by the tick of the 1 kHz clock nearest to the desired navigation solution time. This tick is referred to as a navigation epoch. If the navigation solution attempt is successful, one of the results is an accurate measurement of time in the time base of the chosen GNSS system, called GNSS system time. The difference between the calculated GNSS system time and receiver local time is called the clock bias (and the clock drift is the rate at which this bias is changing).

In practice the receiver's local oscillator is not as stable as the atomic clocks to which GNSS systems are referenced and consequently clock bias tends to accumulate. However, when selecting the next navigation epoch, the receiver always tries to use the1kHz clock tickwhich it estimates to be closest



to the desired fix period as measured in GNSSsystem time. Consequently, the number of 1 kHz clock ticks between fixes occasionally varies. This means that when producing one fix per second, there are normally 1000 clock ticks between fixes, but sometimes, to correct drift away from the GNSS system time, there are 999 or 1001 ticks.

The GNSS system time calculated in the navigation solution is always converted to a time in both the GPS and UTC time bases for output.

Clearly when the receiver has chosen to use the GPS time base for its GNSS system time, conversion to GPS time requires no work at all, but conversion to UTC requires knowledge of the number of leap seconds since GPS time started (and other minor correction terms). The relevant GPS-to-UTC conversion parameters are transmitted periodically (every 12.5 minutes) by GPS satellites, but can also be supplied to the receiver via the UBX-MGA-GPS-UTC aiding message.

When insufficient information is available for the receiver to perform any of these time base conversions precisely, predefined default offsets are used. Consequently, plausible times are nearly always generated, but they may be wrong by a few seconds (especially shortly after receiver start). Depending on the configuration of the receiver, such "invalid" times may well be output, but with flags indicating their state (e.g. the "valid" flags in UBX-NAV-PVT).

#### <span id="page-42-0"></span>**3.5.4 iTOW timestamps**

All the main UBX-NAV messages (and some other messages) contain an iTOW field which indicates the GPS time at which the navigation epoch occurred. Messages with the same iTOW value can be assumed to have come from the same navigation solution.

Note that iTOW values may not be valid (i.e. they may have been generated with insufficient conversion data) and therefore it is not recommended to use the iTOW field for any other purpose.

The original designers of GPS chose to express time/date as an integer week number (starting with the first full week in January 1980) and a time of week (often abbreviated to TOW) expressed in seconds. Manipulating time/date in this form is far easier for digital systems than the more conventional year/month/day, hour/minute/second representation. Consequently, most GNSS receivers use this representation internally, only converting to a more conventional form at external interfaces. The iTOW field is the most obvious externally visible consequence of this internal representation.

If reliable absolute time information is required, it is recommended to use the UBX-NAV-PVT navigation solution message which also contains additional fields that indicate the validity (and accuracy in UBX-NAV-PVT) of the calculated times (see also the GNSS times section below for further messages containing time information).

#### <span id="page-42-1"></span>**3.5.5 Time validity**

Information about the validity of the time solution is given in the following form:

- **Time validity**: Information about time validity is provided in the valid flags (e.g. validDate and validTime flags in the UBX-NAV-PVT message). If these flags are set, the time is known and considered valid for use. These flags are shown in table GNSS times in section GNSS times above as well as in the UBX-NAV-PVT message.
- **Time validity confirmation**: Information about confirmed validity is provided in the confirmedDate and confirmedTime flags in the UBX-NAV-PVT message. If these flags are set, the time validity can be confirmed by using an additional independent source, meaning that the probability of the time to be correct is very high. Note that information about time validity confirmation is only available if the confirmedAvai bit in the UBX-NAV-PVT message is set.



- validDate means that the receiver has knowledge of the current date. However, it must be noted that this date might be wrong for various reasons. Only when the confirmedDate flag is set, the probability of the incorrect date information drops significantly.
- validTime means that the receiver has knowledge of the current time. However, it must be noted that this time might be wrong for various reasons. Only when the confirmedTime flag is set, the probability of incorrect time information drops significantly.
- fullyResolved means that the UTC time is known without full seconds ambiguity. When deriving UTC time from GNSS time the number of leap seconds must be known. It might take several minutes to obtain such information from the GNSS payload. When the one second ambiguity has not been resolved, the time accuracy is usually in the range of ~20s.

#### <span id="page-43-0"></span>**3.5.6 UTC representation**

UTC time is used in many NMEA and UBX messages. In NMEA messages, time is always rounded to the nearest hundredth of a second and it is normally reported with two decimal places (e.g. 124923.52). When using NMEA compatibility mode (selected using CFG-NMEA-COMPAT) where the output must have three decimal places, the third digit is always zero since the underlying time is rounded to the nearest hundredth of a second.

UTC time is also reported within some UBX messages, such as UBX-NAV-TIMEUTC and UBX-NAV-PVT. In these messages date and time are separated into seven distinct integer fields. Six of these (year, month, day, hour, min. and sec.) have fairly obvious meanings and are all guaranteed to match the corresponding values in NMEA messages generated by the same navigation epoch. This facilitates simple synchronization between associated UBX and NMEA messages.

The seventh field is called nano and it contains the number of nanoseconds by which the rest of the time and date fields need to be corrected to get the precise time. So, for example, the UTC time 12:49:23.521 would be reported as: hour: 12, min: 49, sec: 23, nano: 521000000.

It is however important to note that the first six fields are the result of rounding to the nearest hundredth of a second. Consequently the nano value can range from -5000000 (i.e. -5 ms) to +994999999 (i.e. nearly 995 ms).

When the nano field is negative, the number of seconds (and maybe minutes, hours, days, months or even years) have been rounded up. Therefore, some or all of them must be adjusted to get the correct time and date. Thus in an extreme example, the UTC time 23:59:59.9993 on 31st December 2011 would be reported as: year: 2012, month: 1, day: 1, hour: 0, min: 0, sec: 0, nano: -700000.

If a resolution of one hundredth of a second is adequate, negative nano values can simply be rounded up to 0 and effectively ignored.

The UBX-NAV-TIMEUTC message gives information about the UTC time reference clock.

The preferred variant of UTC time can be specified using the CFG-NAVSPG-UTCSTANDARD configuration item. The UTC time variant configured must correspond to a GNSS that is currently enabled. Otherwise the reported UTC time is inaccurate.

#### <span id="page-43-1"></span>**3.5.7 Leap seconds**

Due to the slightly uneven spin rate of the Earth, UTC time gradually moves out of alignment with the mean solar time (that is, the sun no longer appears directly overhead at 0 longitude at midday). Occasionally, a "leap second" is announced to bring UTC back into close alignment with the mean solar time. Usually this means adding an extra second to the last minute of the year, but this can also



happen on 30th June.When this happens, UTC clocks are expected to go from 23:59:59 to 23:59:60, and only then on to 00:00:00.

It is also possible to have a negative leap second, in which case there will only be 59 seconds in a minute and 23:59:58 will be followed by 00:00:00.

u-blox receivers are designed to handle leap seconds in their UTC output and consequently applications processing UTC times from either NMEA or UBX messages should be prepared to handle minutes that are either 59 or 61 seconds long.

Leap second information can be polled from the receiver with the message UBX-NAV-TIMELS.

#### <span id="page-44-0"></span>**3.5.8 Date ambiguity**

Each navigation satellite transmits information about the current date and time in the data message. The time of week (TOW) indicates the elapsed number of seconds since the start of the week (midnight Saturday/Sunday). The week number (WN) indicates the elapsed number of weeks since the particular GNSS system was started. By combining these two values the current date and time can be known. Modern GPS satellites use a 13-bit value for the week number. As GPS system was started in 1980, it allows the week number to represent dates up to year 2137. Unfortunately, at the time when the commonly used GPS L1C/A data message was designed the signal had only 10 bits available for the week number. The top bits of the full week number had to be left out. The 10 bottom bits of the week number are not sufficient to yield a completely unambiguous date as every 1024 weeks (a bit less than 20 years), the transmitted week number value "rolls over" back to zero. Consequently, the information in GPSL1 message does not differentiate between, for example, 1980, 1999, or 2019. GPS L1 receivers must thus use additional methods to calculate the full week number.

Although BeiDou and Galileo have similar representations of time, they still transmit sufficient bits for the week number to be unambiguous for the foreseeable future (the first ambiguity will be in 2078 for Galileo, and not until 2163 for BeiDou). Therefore, the receiver regards the date information transmitted by BeiDou, and Galileo to be unambiguous and, where necessary, uses this information to resolve any ambiguity in the GPS date.

If the receiver is connected to a simulator, note that GPStime is referenced to 6th January 1980, Galileo to 22 August 1999 and BeiDou to 1 January 2006. The receiver doesn't work reliably with signals simulated before these dates.

#### **3.5.8.1 GPS-only date resolution**

If only GPS L1C/A signals are available, the receiver establishes the date by assuming that all week numbers must be at least as large as the reference rollover week number. The default value for the reference rollover week number is selected at the compile time of the receiver firmware and is normally set to a value of a few weeks before the software is completed. The value can be overridden by CFG-NAVSPG-WKNROLLOVER configuration item.

The following example illustrates how this works:

Assume that the reference rollover week number set in the firmware at compile time is 2148 (which corresponds to aweek incalendar year2021,but is transmittedby the satellites as100). Inthis case, if the receiver sees transmissions containing week numbers in the range of 100 ... 1023, they are interpreted as week numbers 2148 ... 3071 (calendar years 2021 ... 2038), whereas transmissions with week numbers from 0 to 99 are interpreted as week numbers 3072 ... 3171 (calendar years 2038 ... 2040).



It is important to set the reference rollover week number correctly when supplying the receiver with simulated signals, especially when the scenarios are in the past.

### <span id="page-45-0"></span>**3.6 Time mark**

The receiver can be used to provide an accurate measurement of the time at which a pulse was detected on the external interrupt pin. The reference time can be chosen by setting the time source parameter to UTC, BeiDou, Galileo, NAVIC or local time in the CFG-TP configuration group. The UTC standard can be set in the CFG-NAVSPG configuration group. The delay figures defined with CFG-TP are also applied to the results output in the UBX-TIM-TM2 message.

A UBX-TIM-TM2 message is output at the next epoch if

- The UBX-TIM-TM2 message is enabled, and
- a rising or falling edge was triggered since last epoch on the **EXTINT** pin.

The UBX-TIM-TM2 messages includes the time of the last time mark, new rising/falling edge indicator, time source, validity, number of marks and an accuracy estimate.

Only the last rising and falling edge detected between two epochs is reported since the output rate of the UBX-TIM-TM2 message corresponds to the measurement rate configured with CFG-RATE-MEAS (see [Figure](#page-45-1) 11 below).

<span id="page-45-1"></span>

#### **Figure 11: Time mark**



### <span id="page-46-0"></span>**3.7 Time pulse**

The receiver includes a time pulse feature providing clock pulses with configurable duration and frequency. The time pulse function can be configured using the CFG-TP configuration group. The UBX-TIM-TP message provides time information for the next pulse and the time source.



**Figure 12: Time pulse**

#### <span id="page-46-1"></span>**3.7.1 Recommendations**

- The time pulse can be aligned to a wide variety of GNSS times or to variants of UTC derived from them. For further information, see [GNSS time bases](#page-40-2). However, it is strongly recommended that the choice of time base is aligned with the available GNSS signals (for example, to produce GPS time or UTC(USNO), ensure GPS signals are available). This involves coordinating the setting of CFG-SIGNAL configuration group with the choice of time pulse time base.
- When using time pulse for precision timing applications it is recommended to calibrate the antenna cable delay against a reference timing source.
- To get the best timing accuracy with the antenna, a fixed and accurate position is needed.
- If relative time accuracy between multiple receivers is required, do not mix receivers of different product families. If this is required, the receivers must be calibrated accordingly, by setting cable delay and user delay.
- The recommended configuration when using the UBX-TIM-TP message is to set both the measurement rate (CFG-RATE-MEAS) and the time pulse frequency (CFG-TP) to 1 Hz.

The sequential order of the signal present at the **TIMEPULSE** pin and the respective output message for the simple case of 1 pulse per second (1PPS) is shown in the following figure.





**Figure 13: Time pulse and TIM-TP**

### <span id="page-47-0"></span>**3.7.2 Time pulse configuration**

The time pulse (**TIMEPULSE**) signal has configurable pulse period, length and polarity (rising or falling edge).

It is possible to define different signal behavior (i.e. output frequency and pulse length) depending on whether or not the receiver is locked to reliable time source.

The CFG-TP configuration group can be used to change the time pulse settings, and includes the following parameters defining the pulse:

- **time pulse enable** If this item is set, the time pulse is active.
- **frequency/period type** Determines whether the time pulse is interpreted as frequency or period.
- **length/ratio type** Determines whether the time pulse length is interpreted as length [us] or pulse ratio [%].
- **antenna cable delay** Signal delay due to the cable between the antenna and the receiver.
- **pulse frequency/period** Frequency or pulse time period when locked mode is not configured or not active.
- **pulse frequency/period lock** Frequency or pulse time period for locked mode. In use as soon as the receiver has calculated a valid time from a received signal. Only used if the corresponding item is set to use another setting in locked mode.
- **pulse length/ratio** Length or duty cycle of the generated pulse, specifies either time or ratio for the pulse to be on/off.
- **pulse length/ratio lock** Length or duty cycle of the generated pulse for locked mode. In use as soon as the receiver has calculated a valid time from a received signal. Only used if the corresponding item is set to use another setting in locked mode.
- **user delay** The cable delay from the receiver to the user device plus signal delay of any user application.
- **lock to GNSS freq** If this item is set, uses the frequency gained from the GNSS signal information rather than the local oscillator's frequency.
- **locked other setting** If this item is set, the alternative setting is used as soon as the receiver can calculate a valid time. This mode can be used, for example, to disable time pulse if the time is not locked, or to indicate a lock with different duty cycles.
- **align to TOW** If this item is set, pulses are aligned to the top of a second.
- **polarity** If set, the first edge of the pulse is a rising edge (pulse polarity: rising).
- **grid UTC/GNSS** Selection between UTC (0), GPS (1), BeiDou (3), (4) Galileo and NAVIC (5) time grid. Also affects the time output by UBX-TIM-TP message.

The maximum pulse length cannot exceed the pulse period.



The high and the low period of the output cannot be less than 50 ns, otherwise pulses can be lost.

#### **3.7.2.1 Example**

The example below shows the 1PPS **TIMEPULSE** signal generated on the time pulse output according to the specific parameters of the CFG-TP configuration group:

- CFG-TP-TP1\_ENA = 1
- CFG-TP-PERIOD\_TP1 = 1 000 000 µs
- CFG-TP-LEN\_TP1 = 100 000 µs
- CFG-TP-TIMEGRID\_TP1 = 1 (GPS)
- CFG-TP-PULSE\_LENGTH\_DEF = 0 (Period)
- CFG-TP-ALIGN\_TO\_TOW\_TP1 = 1
- CFG-TP-USE\_LOCKED\_TP1 = 1
- CFG-TP-POL\_TP1 = 1
- CFG-TP-PERIOD\_LOCK\_TP1 = 1 000 000 µs
- CFG-TP-LEN\_LOCK\_TP1 = 100 000 µs

The 1 Hz output is maintained whether or not the receiver is locked to GPS time. The alignment to TOW can only be maintained when GPS time is locked.



**Figure 14: Time pulse signal with the example parameters**

## <span id="page-48-0"></span>**3.8 Security**

The security concept of ZED-X20P covers:

- **Over-the-air signal integrity and security** monitors and detects threats such as spoofing and jamming in the communication between the receiver and GNSS satellites, ensuring accurate and reliable data.
- **GNSS receiver integrity and security** protects the receiver from unauthorized firmware and configuration changes, ensuring secure operation and maintaining the integrity of the data.

Some security functions monitor and detect threats and report them to the host system. Other functions mitigate threats and allow the receiver to operate normally.

[Table](#page-48-1) 36 outlines security domains and their threat detection and mitigation functions.

<span id="page-48-1"></span>

| Security domain                            | u-blox solution                               |
|--------------------------------------------|-----------------------------------------------|
| Over-the-air signal integrity and security | Spoofing detection and monitoring             |
|                                            | Jamming/interference detection and monitoring |
|                                            | Compliance with DHS allow list                |



| Security domain                      | u-blox solution             |  |
|--------------------------------------|-----------------------------|--|
| GNSS receiver integrity and security | Secure boot                 |  |
|                                      | Secure firmware update      |  |
|                                      | Receiver configuration lock |  |

**Table 36: u-blox security solutions**

#### <span id="page-49-0"></span>**3.8.1 Over-the-air signal integrity and security**

#### <span id="page-49-2"></span>**3.8.1.1 Jamming/interference detection and monitoring**

Intentional and/or unintentional jamming of GNSSreceivers candegrade the quality of GNSSsignals and receiver performance. All u-blox receivers can detect and monitor jamming and report it to the user. The monitoring function is always enabled to inform the user about interference in the GNSS RF bands.

In case of excessive false jamming alerts, the jamming detector sensitivity can be configured with the CFG-SEC-JAMDET\_SENSITIVITY\_HI configuration message.

#### <span id="page-49-1"></span>**3.8.1.2 Spoofing detection and monitoring**

Spoofing is the process where a counterfeit GNSS signal is transmitted locally to deceive the receiver/user and produce an erroneous position fix and/or time solution. The detection algorithm monitors GNSS signals for implausible changes or inconsistencies. These are evaluated with regards to spoofing.

Spoofing detection is typically successful when a signal transitions from an initially genuine state to a spoofed version. The detection algorithms benefit from having signals from multiple GNSS constellations, enhancing the spoofing detection capabilities. Additionally, depending on the spoofing detection mechanisms implemented in the firmware, it may also be possible to detect spoofing if the receiver starts under spoofing conditions.

#### **3.8.1.3 Messages related to jamming, RF interference, and spoofing**

ZED-X20P has the capability to both detect and monitor jamming, RF interference and spoofing and to report it to the user.

The information about jamming, RF interference and spoofing detection are reported in two messages:

- UBX-SEC-SIG: signal security status
- UBX-SEC-SIGLOG: signal security logfile

For more information, see the Interface description [\[2\]](#page-83-1).

#### **Signal security status (UBX-SEC-SIG)**

The UBX-SEC-SIG message provides information related to the security of the signals, in particular about their integrity. It provides information about the jamming/interference and spoofingdetectionmechanisms at eachnavigationepoch, informationuseful to alert thehost about potential jamming/RF interference or spoofing events.

Fields related to jamming and spoofing states in the UBX-SEC-SIG message are described in [Table](#page-49-3) [37](#page-49-3).

<span id="page-49-3"></span>

| Message fields | Jamming/spoofing state | Description                                                                                                                   |
|----------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| jamDetEnabled  | 0/1                    | Flag indicates whether jamming, RF interference detection is<br>enabled or not. If 0, it is disabled and if 1, it is enabled. |



| Message fields | Jamming/spoofing state        | Description                                                                                                   |
|----------------|-------------------------------|---------------------------------------------------------------------------------------------------------------|
| jamState       | 0: Unknown                    | Monitor is not enabled, monitor is uninitialized, or the antenna is<br>disconnected                           |
|                | 1: No jamming indicated       | No jamming or RF interference is detected                                                                     |
|                | 2: Warning; jamming indicated | Position OK but jamming or RF interference is visible (above the<br>thresholds)                               |
| spfDetEnabled  | 0/1                           | Flag indicates whether spoofing detection is enabled or not. If 0, it is<br>disabled and if 1, it is enabled. |
| spoofingState  | 0: Unknown                    | Monitor is not enabled, monitor is uninitialized, or the antenna is<br>disconnected                           |
|                | 1: No spoofing indicated      | No spoofing detectors indicate spoofing                                                                       |
|                | 2: Spoofing indicated         | Spoofing detectors indicate spoofing                                                                          |
|                | 3: Spoofing affirmed          | The indicated spoofing is confirmed                                                                           |

**Table 37: Fields related to jamming and spoofing states in the UBX-SEC-SIG message**

Note that the spoofing state value only reflects the detector state for the current navigation epoch. The value of '1: No spoofing indicated' does not indicate the absence of GNSS spoofing in other navigation epochs.

#### **Signal security logfile (UBX-SEC-SIGLOG)**

The UBX-SEC-SIGLOG message provides a log of past events triggered by jamming/interference or spoofing detection.

Each event consists of a detection type and an event type. The event types indication started and indication stopped form one pair, while indication triggered and indication timeout form another.

The receiver logs up to 16 events and new events take precedence over the past events in the log. Power cycles and restarts of the receiver reset the log, deleting its content.

Fields related to jamming and spoofing detection states in the UBX-SEC-SIGLOG message are described in [Table](#page-50-0) 38.

<span id="page-50-0"></span>

| Message fields | Signal security log state            | Description                                         |
|----------------|--------------------------------------|-----------------------------------------------------|
| ttag           |                                      | Shows the time tag in millisecond.                  |
| detectionType  |                                      | Type of the spoofing or jamming detection:          |
|                | 0 = simulated signal                 | Signal from simulator with changed navigation data  |
|                | 1 = abnormal signal                  | Not supported                                       |
|                | 2 = INS/GNSS mismatch                | Not supported                                       |
|                | 3 = abrupt changes in GNSS<br>signal | Abrupt changes in GNSS signal level and time offset |
|                | 4 = jamming indicated                | Jamming indicated in the GNSS signal environment    |
|                | 5 = authentication failed            | Authentication of GNSS signal failed                |
|                | 6 = replayed signals                 | GNSS signals identified as replayed                 |
| eventType      |                                      | Type of the event:                                  |
|                | 0 = indication started               |                                                     |
|                | 1 = indication stopped               |                                                     |
|                | 2 = indication triggered             |                                                     |
|                | 3 = indication timed-out             |                                                     |

**Table 38: Fields related to jamming and spoofing detection states in the UBX-SEC-SIGLOG message**



Single epoch events, caused by abrupt changes due to switching from the real to the spoofing signal or vice versa are handled as time-out events. This means that the time-out event is reported after a certain cool off period which is not related to any observations in the signal. The other detection types make use of 'start' and 'stop' event types.

#### <span id="page-51-1"></span>**3.8.1.4 Compliance with DHS allow list**

The GPS allow list is a set of validation checks implemented in the ZED-X20P receiver firmware to ensure the reliability of LNAV navigation data received from the GPS satellites. These checks help improve the receiver's performance by blocking unreliable data from affecting the navigation solution or alerting the user about issues in the navigation message.

The DHS- GPS Receiver Allow List [Development](https://www.dhs.gov/science-and-technology/publication/gps-receiver-allow-list-development-guide) Guide provides an example of an allow list and offers guidelines for creating validation rules. To enhance security and reduce vulnerabilities, the ZED-X20P firmware includes a comprehensive set of these checks.

#### <span id="page-51-0"></span>**3.8.2 GNSS receiver integrity and security**

#### <span id="page-51-2"></span>**3.8.2.1 Secure boot**

The ZED-X20P boots only with firmware images that are signed by u-blox. This prevents the execution of non-genuine firmware images on the receiver.

#### <span id="page-51-3"></span>**3.8.2.2 Secure firmware update**

The firmware image is signed by u-blox. The ZED-X20P verifies the signature during the firmware update.

#### <span id="page-51-4"></span>**3.8.2.3 Receiver configuration lock**

The receiver configuration lock feature ensures that no configuration changes are possible once the feature is enabled. The configuration lock is enabled by setting the configuration item CFG-SEC-CFG\_LOCK to "true".

The configuration lock can be applied to different configuration layers including the RAM, BBR, and flash memory. At startup, the receiver constructs the configuration database from different configuration layers and maintains it in the run-time RAM memory. When the configuration lock is set in the run-time RAM, the receiver configuration cannot be changed on any configuration layer.

For more information on the configuration layers including the order of priority they are applied in, see the applicable Interface description [[2](#page-83-1)].

The configuration lock set on a configuration layer in volatile memory (RAM, BBR) is removed when the memory is cleared. However, the configuration lock set in non-volatile memory (flash memory) is permanent apart from one exception: during firmware upload to flash memory, the flash is erased during the process causing the configuration lock to be cleared. Refer to [Firmware](#page-0-0) update to flash for more information on firmware update.

To test the lock functionality, set it on the RAM configuration layer. After a power cycle, the information on RAM layer is cleared and the lock is no longer set.

It is recommended to apply the configuration lock on the same layer the configuration is stored.

An example of use case is that the host application locks the receiver configuration. A user communicating with the ZED-X20P through any of the available interfaces can poll, enable or send messages, but cannot change the configuration by sending UBX configuration messages.



## <span id="page-52-0"></span>**3.9 Multiple GNSS assistance (MGA)**

The u-blox AssistNow services provide a proprietary implementation of an A-GNSS protocol compatible with u-blox GNSS receivers. The MGA services consist of AssistNow Online and Offline variants delivered by HTTP or HTTPS protocol.

When a client device makes an AssistNow request, the service responds with the requested data using standard UBX protocol MGA messages. These messages are ready for direct transmission from the client to the receiver port without requiring any modification.

AssistNow Online optionally provides immediate satellite ephemerides, health information and time aiding data suitable for GNSS receiver systems with direct internet access.

The ZED-X20P supports AssistNow Online only.

Refer to the ZED-X20P datasheet for the supported GNSS signals by each MGA service [\[1\]](#page-83-2).

#### <span id="page-52-1"></span>**3.9.1 Authorization**

To use the AssistNow services, customers will need to obtain an authorization token from u-blox. Go to <https://www.u-blox.com/en/solution/services/assistnow> or contact your local technical support to get more information and to request access to the service.

#### <span id="page-52-2"></span>**3.9.2 Preserving MGA and operational data during power-off**

The time-to-fix after a receiver power interruption is dependent on the amount of operational data available at startup. Satellite broadcast information and an estimate of accurate time can be fetched form the AssistNow service. In addition, the following techniques can restore the data that was stored prior to powering down.

• **Battery-backed RAM:**The receiver operational state stored in this RAM can be maintained during power outages by connecting the **V\_BCKP** pin to an independent supply, e.g. a battery. This is a recommended method as it will maintain all MGA-related information, any user configuration, calibration data, and an estimate of time via the real-time clock. See section [V\\_BCKP](#page-55-3) for more information.

### <span id="page-52-3"></span>**3.10 u-blox protocol feature descriptions**

#### <span id="page-52-4"></span>**3.10.1 Broadcast navigation data**

The receiver collects broadcast navigation data message for each tracked signal and reports it in the UBX-RXM-SFRBX message. When enabled, a separate message is generated each time the receiver decodes a complete subframe of data from a tracked signal. The data bits are reported as received, including preambles and error checking bits as appropriate. However, because there is considerable variation in the data structure of the different GNSS signals, the reported data also varies. This document uses the term "subframe", but other GNSS data structures might use different terms. For example Galileo uses the term "pages".

#### **3.10.1.1 Parsing navigation data subframes**

Each UBX-RXM-SFRBX message contains a subframe of data bits appropriate for the relevant GNSS, delivered in a number of 32-bit words, as indicated by numWords field.

Due to the variation in data structure between different GNSS, the most important step in parsing a UBX-RXM-SFRBX message is to identify the form of the data. This should be done by reading the gnssId field, which indicates which GNSS the data was decoded from. In almost all cases, this is sufficient to indicate the structure. Because of this, the following sections are organized by GNSS.



However, in some cases the identity of the GNSS is not sufficient, and this is described, where appropriate, in the following sections.

In most cases, the data does not map perfectly into a number of 32-bit words and, consequently, some of the words reported in UBX-RXM-SFRBX messages contain fields marked as "Pad". These fields should be ignored and no assumption should be made about their contents.

UBX-RXM-SFRBX messages are only generated when complete subframes are detected by the receiver and all appropriate parity checks have passed.

Where the parity checking algorithm requires data to be inverted before it is decoded (e.g. GPS L1C/A), the receiver carries this out before the message output. Therefore, users can process data directly and do not need to worry about repeating any parity processing.

The meaning of the content of each subframe depends on the sending GNSS and is described in the relevant interface control documents (ICD).

#### **3.10.1.2 UBX-RXM-SFRBX data message formats**

The following table gives a summary of the different data message formats reported by the UBX-RXM-SFRBX message. For more details, refer to corresponding signal ICD documents.

| GNSS    | Signal | gnssId | sigId | numWords         | period | ICD                         |
|---------|--------|--------|-------|------------------|--------|-----------------------------|
| GPS     | L1C/A  | 0      | 0     | 10               | 6 s    | IS-GPS-200N                 |
| GPS     | L2CL   | 0      | 3     | 10               | 12 s   | IS-GPS-200N                 |
| GPS     | L2CM   | 0      | 4     | 10               | 12 s   | IS-GPS-200N                 |
| GPS     | L5 I   | 0      | 6     | 10               | 6 s    | IS-GPS-705J                 |
| SBAS    | L1C/A  | 1      | 0     | 9                | 1 s    | See SBAS<br>system ICD      |
| Galileo | E1     | 2      | 1     | 8                | 2 s    | Galileo OS SIS<br>ICD v.2.1 |
| Galileo | E5a    | 2      | 3     | 8                | 10 s   | Galileo OS SIS<br>ICD v.2.1 |
| Galileo | E6     | 2      | 8     | 16               | 1 s    | Galileo OS SIS<br>ICD v.2.1 |
| BeiDou  | B1C    | 3      | 4     | variable(3,3,19) | 18 s   | BDS-SIS-ICD<br>B1C-1.0      |
| BeiDou  | B1I D1 | 3      | 0     | 10               | 6 s    | Beidou SIS ICD<br>B1I v.3.0 |
| BeiDou  | B1I D2 | 3      | 1     | 10               | 0.6 s  | Beidou SIS ICD<br>B1I v.3.0 |
| BeiDou  | B2a    | 3      | 7     | 9                | 3 s    | BDS-SIS-ICD<br>B2a -1.0     |
| BeiDou  | B3ID1  | 3      | 4     | 10               | 6 s    | BDS-SIS-ICD<br>B3I-1.0      |
| BeiDou  | B3ID2  | 3      | 10    | 10               | 0.6 s  | BDS-SIS-ICD<br>B3I-1.0      |
| QZSS    | L1C/A  | 5      | 0     | 10               | 6 s    | IS-QZSS<br>PNT-006          |
| NavIC   | L5 A   | 7      | 0     | 10               | 12 s   | ISRO-IRNSS<br>ICD-SPS-1.1   |

**Table 39: Data message formats reported by UBX-RXM-SFRBX**



## <span id="page-54-0"></span>**3.11 Firmware update**

ZED-X20P is supplied with firmware. u-blox may release updated images containing for example security fixes, enhancements, bug fixes, etc. Therefore, it is important that customers implement a firmware update mechanism in their system.

A firmware image is a binary file containing the software to be run by the GNSS receiver. A firmware update is the process of transferring a firmware image to the receiver and storing it in non-volatile flash memory.

Contact u-blox for more information on firmware update.



## <span id="page-55-0"></span>**4 Hardware integration**

This chapter provides instructions for integrating the receiver into an application design.

## <span id="page-55-1"></span>**4.1 Power supply**

ZED-X20P has the following power supply pins: [VCC](#page-55-2) and [V\\_BCKP](#page-55-3).

A power supply at **VCC** must be present for normal operation. A supply at **V\_BCKP** is optional. If present, it enables the hardware backup mode when the **VCC** supply is off.

For absolute maximum ratings, operating conditions, and power requirements, refer to the ZED-X20P Data sheet [].

### <span id="page-55-2"></span>**4.1.1 VCC**

The **VCC** pin is connected to the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude. For this reason, it is important that the supply circuitry be able to support the peak power for a short time (see the applicable data sheet [] for specification).

The module integrates a DC/DC converter, which allows reduced power consumption.

- When switching from backup mode to normal operation or at startup, u-blox ZED-X20P modules must charge the internal capacitors in the core domain. In certain situations, this can result in a significant current draw. For low-power applications using backup mode, it is important that the power supply or low ESR capacitors at the module input be able to deliver this current/charge.
- To reduce peak current during power on, users can employ an LDO that has a built-in current limiter.
- Do not add any series resistance greater than 0.2 Ω to the **VCC** supply as it will generate input voltage noise due to dynamic current conditions.
- For the ZED-X20P module the equipment must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1.

#### <span id="page-55-3"></span>**4.1.2 V\_BCKP**

The **V\_BCKP** pin can be used to provide power to maintain the real-time clock (RTC) and batterybacked RAM (BBR) when **VCC** is removed.

If the module supply has a power failure, the **V\_BCKP** pin supplies the real-time clock (RTC) and battery-backed RAM (BBR). Use of valid time and the GNSS orbit data at start up will improve the GNSS performance, as with hot starts and warm starts.

If **V\_BCKP** is not provided, the module performs a cold start at power up.

If a host is connected to ZED-X20P, **V\_BCKP** can be partially emulated by using UBX-UPD-SOS functionality. BBR data can saved to the host and restored at startup. See the applicable Interface description [\[2\]](#page-83-1) for more information.

- Avoid high resistance on the **V\_BCKP** line: During the switch from main supply to backup supply, a short current adjustment peak can cause a high voltage drop on the pin with possible malfunctions.
- Add a 2 uF capacitor on the **V\_BCKP** pin to absorb the current adjustment peak when switching from **VCC** to **V\_BCKP** supply.



If no backup supply voltage is available, connect the **V\_BCKP** pin to **VCC**.

Allow all I/O including UART and other interfaces to float or connect to a high impedance in HW backup mode (**V\_BCKP** supplied when **VCC** is removed). See the applicable Interface description [\[2](#page-83-1)].

#### **Real-time clock (RTC)**

The real-time clock (RTC) is driven by a 32-kHz oscillator using an RTC crystal. If **VCC** is removed while a battery is connected to **V\_BCKP**, most of the receiver is switched off leaving the RTC and BBR powered. This operating mode is called Hardware Backup Mode which enables time keeping and all relevant data to be saved to allow a hot or warm start.

#### <span id="page-56-0"></span>**4.1.3 ZED-X20P power supply**

ZED-X20P requires a low-noise, low-dropout voltage, and a very low source impedance power supply of 3.3 V typically. No inductors or ferrite beads should be used from LDO to the module **VCC** pin. The peak currents need to be taken into account for the source supplying the LDO for the module.

A power supply fed by 5 V is shown in the figure below. This example circuit is intended only for the module supply.



#### **Figure 15: ZED-X20P power supply**

### <span id="page-56-1"></span>**4.2 RF interference**

The GNSS signal power received at the antenna is very low compared to other wireless communication signals. The received nominal –130 dBm GNSS signal strength makes the GNSS receiver susceptible to interference from many kinds of nearby RF sources.

As an example, cellular applications emit signals with power levels of approximately +30 dBm, while the GNSS signal is less than –130 dBm when reaching the antenna. By simply comparing these



numbers, it is obvious that interference issues must be seriously considered during the design phase.

#### <span id="page-57-0"></span>**4.2.1 In-band interference**

Although the radio communications standards prevent intentional RF signal sources from interfering the GNSS frequencies, many devices emit RF power into the GNSS band at levels much higher than the GNSS signal itself.

One reason is that the frequency band above 1 GHz is not well regulated with regards to EMI, and even if permitted, signal levels are much higher than the GNSS signal power. In particular, all types of digital equipment, such as PCs, digital cameras, LCD screens, etc. tend to emit a broad frequency spectrum up to several GHz of frequency. Also wireless transmitters may generate spurious emissions that fall into the GNSS band.

#### <span id="page-57-1"></span>**4.2.2 Out-of-band interference**

Out-of-band interference is caused by signal frequencies that are different from the GNSS carrier frequency. The main sources are wireless communication systems such as LTE, GSM, CDMA, WCDMA, Wi-Fi, BT, etc. Typically, these systems may emit their specified maximum transmit power in close proximity to the GNSS receiving antenna, especially if such a system is integrated with the GNSS receiver. Even at reasonable antenna selectivity, destructive power levels may reach the RF input of the GNSS receiver. In addition, larger signal interferers may generate intermodulation products inside the GNSS receiver front-end that fall into the GNSS band and contribute to in-band interference.

#### <span id="page-57-2"></span>**4.2.3 Spectrum analyzer**

The UBX-MON-SPAN message can be enabled in u-center 2 to provide a low-resolution spectrum analyzer sufficient to identify noise or jammers in the reception band. Once enabled, u-center 2 includes a real-time chart that is updated once per second with the message data. See [Figure](#page-58-0) 16 for an example.

The design or device environment can generate interference at the in-band that can be analyzed from the spectrum in the UBX-MON-SPAN message. Hence, the shape of the spectrum as well as visible peaks help to identify in-band interference. Out-of-band interference can also cause peaks that appear in the in-band. However, there can be out-of-band interference that is not visible within the span of the spectrum. The presence of out-of-band interference may be seen as reduction in the PGA (Programmable Gain Amplifier) value.

The vertical axis compares the power level in dB for each frequency. A good spectrum shape is characterized by an even noise floor along with the GNSS band. For example, if any unwanted interference peak stands out, the vertical axis gives a rough approximation of the power level in dB compared to the noise floor.

Next to the chart, the center frequency, span, and resolution values set for the spectrum, and the PGA value are also displayed. The PGA value represents the internal gain set by the receiver, which depends on the external amplification of the GNSS input signal.

The vertical discontinuous lines in the chart area represent the offset to the center frequency in MHz. This helps to estimate the frequency of any spurious emission seen.

In addition, u-center 2 includes three functions commonly found in any spectrum analyzer. These features support the RF front-end design and help to spot out any jammer present during the application operation.



- Hold: if selected, the current spectrum shape freezes in a colored line. This allows for a comparison between the time the spectrum was frozen and the real-time spectrum. This is particularly helpful in assessing the impact of running other onboard components.
- Average: if selected, a colored line shows the averaged spectrum for each frequency. This supports the analysis over time and obtaining a less noisy shape.
- Max hold: if selected, a colored line shows the maximum amplitude measured at each frequency. This option helps to spot out any jammer over a period of time.

[Figure](#page-58-0) 16 shows the spectrum view in u-center 2 with the hold, average and max hold options selected.The green, yellow and red lines represent the frozen hold, average and max hold spectrums, while the blue line represents the current continuous spectrum.

<span id="page-58-0"></span>

#### **Figure 16: Spectrum analyzer view in u-center 2**

By changing the enabled GNSS constellations, the span widens or narrows. This has a direct impact on the spectrum resolution, since the number of measured values is fixed at 256 bins. For further details about this message and how to calculate each frequency, see the Interface description [\[2\]](#page-83-1).





A peak may be visible around the center frequency.The signal comes internally from the receiver and it does not cause any degradation in the performance.

## <span id="page-59-0"></span>**4.3 RF front-end**

GNSS receivers operate with very low signal levels, ranging from –130 dBm to approximately –167 dBm. This alone is a challenge for the GNSS application design. Out-of-band sources of interference such as GSM, CDMA, WCDMA, LTE, Wi-Fi, or Bluetooth wireless systems with a much higher signal level require additional specific measures. The goal of the RF front-end design is to receive the inband signal with minimum loss and added noise while suppressing the out-of-band interference.

Refer to the Block [diagram](#page-8-0) for an overview of the RF front-end.

#### <span id="page-59-1"></span>**4.3.1 Internal LNA modes**

In addition to the integrated PGA gains in the RF front-end circuitry, ZED-X20P provides three independently configurable internal LNAs, one in each RF path. These [configurable](#page-11-4) LNAs have two operating modes: normal gain and low gain as shown in [Table](#page-59-4) 40.

<span id="page-59-4"></span>

| Internal LNA mode     | Minimum external gain | Maximum external gain |
|-----------------------|-----------------------|-----------------------|
| Normal gain (default) | 17 dB                 | 40 dB                 |
| Low gain              | 20 dB                 | 50 dB                 |
|                       |                       |                       |

**Table 40: Overview of the internal LNA modes**

Ensure the external gain is within the recommendations to provide the integrated PGAs with a sufficient dynamic range in all conditions. Exceeding the maximum external gain degrades the receiver's performance.

#### <span id="page-59-2"></span>**4.3.2 Out-of-band blocking immunity**

Out-of-band RF interference may degrade the quality and availability of the navigation solution. Out-of-band immunity limit describes the maximum power allowed at the receiver RF input with no degradation in performance. Minor violation of the immunity limit may reduce C/N0 of the received signals but does not necessarily affect the overall receiver performance. However, a significant violation may reduce receiver sensitivity or cause a complete loss of signal reception. The severity of the interference depends on the repetition rate, frequency, signal level, modulation, and bandwidth of the signal.

The immunity decreases closer to the GNSS in-band. The limit is defined at room temperature using a test signal with 64QAM modulation and 10 MHz bandwidth similar to an LTE signal.

If the out-of-band immunity limit is exceeded, it is recommended to verify that the receiver performance is not affected or is at an acceptable level in the presence of interference.

#### <span id="page-59-3"></span>**4.3.3 Interference coupling**

RF interference is typically first coupled into the antenna and subsequently conducted into the receiver input. Typical out-of-band interference sources include transmitting antennas of other radio systems. Estimation of the RF interference level coupled into the receiver antenna is a starting point for RF front-end design.

For designs with other radio systems, the maximum power coupled into the antenna can be estimated from the maximum transmission power and the isolation between the antennas. Practical values for antenna isolation can range from 15–20 dB down to 6–10 dB for very small devices. RF interference may also couple from external sources such as nearby mobile devices or base stations.



A simplified test board can be used to estimate the isolation between two antennas. The size of the board and the placement of the antennas must match the final design. Connect the RF cables to the antenna inputs and measure S21 over the frequency band of interest with a vector network analyzer (VNA).

It is more difficult to estimate RF interference from other parts of the design. One option is to measure the interference level at the receiver input using a spectrum analyzer. Interference within the design is primarily a problem at the receiver in-band, where it cannot be addressed by filtering on the RF path. Outside the GNSS band, the required filtering is determined by the estimated interference level and the immunity of the receiver.

The maximum power coupled into the receiver RF input is compared against the immunity limit of the receiver defined in [Out-of-band](#page-59-2) blocking immunity.

### <span id="page-60-0"></span>**4.4 Antenna**

ZED-X20P requires an active antenna with an integrated Low Noise Amplifier (LNA) to ensure good performance under nominal signal reception.

When implementing a custom antenna installation, it is recommended that an OEM active antenna module be used that meets our specification. Implementing a custom active antenna design is an important exercise to meet the required bandwidths and group delay specifications compared to previous L1-only designs.

[Figure](#page-60-1) 17 with information from u-blox ANN-MB2 active antenna provides an example of a typical all-band antenna design.

<span id="page-60-1"></span>

**Figure 17: Internal structure of u-blox low cost, all-band antenna**

A suitable ground plane is required for the antenna to achieve good performance.

Location of the antenna is critical to reach the stated performance. Unsuitable locations within a vehicle could include, under vehicle dash, rear-view mirror location, etc.

A set of recommended specifications for an all-band active antenna is given below.

| Parameter                      | Specification     | Rating | Units |
|--------------------------------|-------------------|--------|-------|
|                                | Minimum gain5     | 17     | dB    |
| Active antenna recommendations | 5<br>Maximum gain | 50     | dB    |
|                                | Noise figure      | <3.5   | dB    |

<span id="page-60-2"></span>5 Including passive losses (filters, cables, connectors etc.)



| Parameter                          | Specification                 | Rating                         | Units |
|------------------------------------|-------------------------------|--------------------------------|-------|
| 6<br>Group delay variation in-band |                               | <10 typ.                       | ns    |
| Out-of-band rejection              |                               | 40 typ.                        | dB    |
|                                    | L band antenna gain           | 4 typ.                         | dBic  |
|                                    | L1/L2/L5/E6 band antenna gain | 3 typ.                         |       |
|                                    | L/L1 band axial ratio         | 2 max                          | dB    |
|                                    | (1535 - 1602 MHz)             | at Zenith                      |       |
| 7<br>Antenna element specification | L5/L2/B3/E6 band axial ratio  | 2.9 max                        | dB    |
|                                    | (1166 - 1285 MHz)             | at Zenith                      |       |
|                                    | Polarization                  | RHCP                           |       |
|                                    | Phase center variation        | <10                            | mm    |
|                                    |                               | in all directions              |       |
| 8<br>EMI immunity out-of-band      |                               | 30                             | V/m   |
| ESD circuit protection             |                               | 15                             | kV    |
|                                    |                               | human body model air discharge |       |

#### **Table 41: Antenna specifications for ZED-X20P modules**

The antenna system should include filtering to ensure adequate protection from nearby transmitters. Take care in the selection of antennas placed close to cellular or Wi-Fi transmitting antennas.

ZED-X20P provides three independently configurable [internal](#page-0-0) LNAs, one for each RF block.

#### <span id="page-61-0"></span>**4.4.1 Active Antenna Power Supply**

The antenna power supply is typically used to power GNSS active antennas. The power supply should be able to provide the correct voltage and current to the antenna to ensure optimal performance of ZED-X20P.

To power and limit the current to the antenna, you have the following options:

- [External](#page-62-0) power supply
- [External](#page-63-0) power supply and current limiting
- [VCC\\_RF](#page-64-1) power supply

The diagram shows the Z impedance of the antenna bias L4 inductor. This inductor is found in all the reference circuits mentioned in the subsequent sections. It is important for the Z impedance to be greater than 500 Ω within the 1–1.8 GHz frequency range. This impedance ensures efficient blocking of RF signals from reaching the power supply.

<span id="page-61-1"></span><sup>6</sup> GNSS system bandwidths: L,B1I,L1,E1,B1C 1535…1602 MHz; L2C 1223…1231 MHz; L5,E5a,E6,B2a,B3I 1166…1285 MHz

<span id="page-61-2"></span><sup>7</sup> Measured with a ground plane d=120 mm

<span id="page-61-3"></span><sup>8</sup> Exception GNSS system band +/- 200 MHz, emphasis on cellular bands





**Figure 18: ZED-X20P antenna bias inductor impedance**

#### <span id="page-62-0"></span>**4.4.1.1 External power supply**

[Figure](#page-62-1) 19 shows an example with an external filtered supply **V\_ANT** 3.3 V. Consider the power dissipation in both the resistor and inductor based on the supply voltage and short circuit current. Calculate the current capacity of the bias-T inductor and the value of the bias resistor. Include the supply voltage and its current capacity for the bias-T in the calculation.

<span id="page-62-1"></span>

**Figure 19: ZED-X20P with external voltage antenna bias**

| Part | Specifications      | Values        |
|------|---------------------|---------------|
| C22  | Filtering capacitor | 100 nF, 16 V  |
| FB1  | Ferrite bead        | BLM15HB121SH1 |



| Part | Specifications                                                            | Values        |
|------|---------------------------------------------------------------------------|---------------|
| L4   | Minimum Current of 300 mA or more impedance >500<br>Ω at GNSS frequencies | LQG15HS47NJ02 |
| R19  | Current limit resistor                                                    | 10 Ω          |

**Table 42: ZED-X20P external voltage antenna bias components**

#### <span id="page-63-0"></span>**4.4.1.2 External power supply and current limiting**

[Figure](#page-63-1) 20 shows an example with an external voltage **V\_ANT** 3.3 V. In this example, the current limiting threshold is set at 60 mA and the use of ferrite bead is recommended.

Note that active antennas typically draw 5–20 mA current, contributing to the overall power consumption of the system.

<span id="page-63-1"></span>

#### **Figure 20: ZED-X20P with external voltage antenna bias and current limit circuit**

| Part   | Specifications                                                            | Values                        |
|--------|---------------------------------------------------------------------------|-------------------------------|
| C14    | Filtering capacitor                                                       | 10n, Bias-T, X7R 10N 10% 16 V |
| C21    | Filtering capacitor                                                       | 100 nF, 16 V                  |
| FB1    | Ferrite bead                                                              | BLM15HB121SH1                 |
| L4     | Minimum Current of 300 mA or more impedance >500<br>Ω at GNSS frequencies | LQG15HS47NJ02                 |
| R7     | Passive pull-up to control T6                                             | PNP off 2.2 kΩ                |
| R18    | Defines the threshold of the comparator                                   | 220 Ω                         |
| R17    | Defines the threshold of the comparator                                   | 10 Ω                          |
| T6, T7 | BJT PNP transistors                                                       | PNP                           |

**Table 43: ZED-X20P antenna bias components**



#### <span id="page-64-1"></span>**4.4.1.3 VCC\_RF power supply**

When using the **VCC\_RF** supply pin from ZED-X20P:

- Limit the current to a maximum of 300 mA at the module supply voltage under short circuit conditions, requiring a 10 Ω resistor for a 3 V module supply.
- The bias-T inductor's DC resistance is assumed to be 1–2 Ω, and the module's internal feed inductor is assumed to be 1.2 Ω.



**Figure 21: ZED-X20P VCC\_RF antenna bias**

| Part | Specifications                                                            | Values        |
|------|---------------------------------------------------------------------------|---------------|
| C22  | Filtering capacitor                                                       | 100 nF, 16 V  |
| FB1  | Ferrite bead                                                              | BLM15HB121SH1 |
| L4   | Minimum Current of 300 mA or more impedance >500<br>Ω at GNSS frequencies | LQG15HS47NJ02 |
| R19  | Current limit resistor                                                    | 10 Ω          |

**Table 44: ZED-X20P VCC\_RF antenna bias components**

#### <span id="page-64-0"></span>**4.4.2 Antenna supervisor circuit**

The active antenna supervisor circuit connects to three ZED-X20P pins:

- **ANT\_OFF**
- **ANT\_DETECT**
- **ANT\_SHORT\_N**

For example the antenna open circuit detection is made using **ANT\_DET** pin. A "high" at **ANT\_DET** pin indicates an antenna is detected (antenna consumes current) and a "low" at **ANT\_DET** pin indicates an antenna is not detected (no current drawn).

The following schematic details the required circuit:





#### **Figure 22: ZED-X20P antenna supervisor circuit**

The bias-T inductor L4 should support multi-band operation within the 1–1.8 GHz frequency range. For additional information, see Active [Antenna](#page-61-0) Power Supply.

| Part       | Specifications                                                          |  |  |
|------------|-------------------------------------------------------------------------|--|--|
| C14        | Filtering capacitor                                                     |  |  |
| L4         | Minimum Current of 300 mA or more. Impedance >500 Ω at GNSS frequencies |  |  |
| R7         | Passive pull-up to control T5                                           |  |  |
| R8         | Current limiter in the event of a short circuit                         |  |  |
| R9         | Defines the threshold of the comparator                                 |  |  |
| R10        | Defines the threshold of the comparator                                 |  |  |
| T5         | P-FET transistor acting as a switch to control the antenna supply       |  |  |
| U3, U7, U8 | Open drain buffer to shift voltage levels                               |  |  |
| U6         | Comparator (op-amp)                                                     |  |  |

**Table 45: Antenna supervisor components**

- Buffers U3, U7 and U8 are optional depending on the application.They are not needed if the **VCC\_RF** pin is used.
- An open drain buffer is recommended in case the antenna is supplied while the module is not, since IO pins must not be driven. If the antenna operates at a higher voltage like 5 V or 12 V, use of the buffer is also recommended.



## <span id="page-66-0"></span>**4.5 I2C design recommendations**

The I2C communication bus is based on open-drain/open-collector ICs. Pull-up resistors must be connected from the I2C lines to the supply rails to pull the line high when it's not driven low by the open-drain interface.

The u-blox chip integrates internal pull-up resistors at the **SCL** and **SDA** pins. These resistors have a large value variation (chip to chip, over temperature, voltage), see product datasheet. To minimize timing variations, it is suggested adding external pull-up resistors with lower resistance at the **SCL** and **SDA** pins in parallel to the internal ones.

#### <span id="page-66-1"></span>**4.5.1 I2C pull up calculation**

According to the I2C specification, the electrical input reference levels are set as 30% and 70% of the amplitude. The rise time of the **SCL**/**SDA** lines is given by the pull-up resistors and the total bus capacitance.



**Figure 23: I2C bus signal rise and fall time**

The minimum pull up Rp(min) resistance is based on the bus voltage (VCC), the maximum voltage that can be read as a logic-low (VOL), and the maximum current that the pins can sink when at or below VOL (IOL).

Rp(min) = (VCC – VOL) / IOL.

The maximum pull-up resistance is based on the maximum rise-time (t<sup>r</sup> ) requirement (dependent on the I2C clock frequency) and the total capacitance (Cb) on the bus.

Rp(max) = t<sup>r</sup> / (0.8473 \* Cb).

#### **Example:**

For Fast-mode (400 kHz) I2C communication with t<sup>r</sup> = 300 ns, bus voltage VCC = 3.3 V, VOL = 0.4 V, IOL = 2 mA and assuming a total bus capacitance (input pad, line trace, filtering etc.) of max 100 pF (the I2C specification lists the maximum total bus capacitance with a pull-up resistor to be 200 pF):

Rp(min) ≈ 1.5 kΩ and Rp(max) ≈ 3.5 kΩ.

For an internal chip pull-up value between 8 kΩ to 40 kΩ, adding an external pull-up resistor of 3 kΩ between the **SCL**/**SDA** lines and the IO supply rail results in a total pull-up resistance in the range of 2.18 kΩ (3 kΩ||8 kΩ) to 2.79 kΩ (3 kΩ||40 kΩ).

#### <span id="page-66-2"></span>**4.5.2 EMI/EMC considerations for I2C bus**

To minimize potential radiated emissions from the I2C lines near GNSS frequencies and address possible I2C timing issues, add filtering capacitors (typically 68 pF) to ground at the **SCL** and **SDA** pins or ensure placeholders for the capacitors are provided.

Route the I2C traces away from the PCB edges and connectors to further reduce radiated emissions.



## <span id="page-67-0"></span>**4.6 Layout**

This section details layout and placement requirements of the ZED-X20P high precision receiver.

#### <span id="page-67-1"></span>**4.6.1 Placement**

GNSS signals at the surface of the Earth are below the thermal noise floor. A very important factor in achieving maximum GNSS performance is the placement of the receiver on the PCB. The placement used may affect RF signal loss from antenna to receiver input and enable interference into the sensitive parts of the receiver chain, including the antenna itself. When defining a GNSS receiver layout, the placement of the antenna with respect to the receiver, as well as grounding, shielding and interference from other digital devices are crucial issues and need to be considered very carefully.

Signal loss on the RF connection from antenna to receiver input must be minimized as much as possible. Hence, the connection to the antenna must be kept as short as possible.

Ensure that RF critical circuits are clearly separated from any other digital circuits on the system board. To achieve this, position digital part of the receiver close to the digital section of the system PCB and place the RF section and antenna as far away from the other digital circuits on the board as possible.

A proper GND concept shall be followed: the RF section shall not be subject to noisy digital supply currents running through its GND plane.

#### <span id="page-67-2"></span>**4.6.2 Thermal and mechanical considerations**

Temperature-sensitive components, such as TCXOs and crystals, are highly susceptible to sudden changes in ambient temperature, which can negatively impact the GNSS signal tracking. Additionally, mechanical stress and vibration can further degrade performance. For best practices on thermal and mechanical design to enhance GNSS stability and accuracy, and ensure reliable performance in challenging conditions, refer to [Table](#page-67-4) 46.

<span id="page-67-4"></span>

| Topic                                    | Description and design practices                                                                                             |  |  |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--|--|
| Minimize temperature gradients           | Avoid placing the receiver circuitry in the proximity of cooling fans or heat<br>emitting components, such as power devices. |  |  |
|                                          | Shield the temperature-sensitive components to reduce air convection and<br>improve thermal stability.                       |  |  |
| Thermal conduction via the PCB           | Use a continuous ground (GND) plane to facilitate uniform heat dissipation<br>and maintain thermal stability.                |  |  |
|                                          | Connect the receiver'sground to the commonground using aninnerPCBlayer<br>to enhance heat distribution.                      |  |  |
| External vibration and mechanical stress | Position the receiver circuitry away from sources of vibration.                                                              |  |  |
|                                          | Avoid mechanical stress that could affect TCXO or crystal stability.                                                         |  |  |
|                                          | If necessary, use additional mechanical support points near the receiver or<br>thicken the PCB.                              |  |  |

**Table 46: Thermal and mechanical considerations**

#### <span id="page-67-3"></span>**4.6.3 Package footprint, copper and paste mask**

This section provides recommendations for copper and soldermask dimensioning for the ZED-X20P module packages.

- These are recommendations only and not specifications. The exact copper, solder and paste mask geometries, distances, stencil thickness and solder paste volumes must be adapted to the specific production processes (e.g. soldering etc.).
- PIN 1 indicator is the ground opening, do not route any signal below this pad.



Refer to the applicable Data sheet [] for the mechanical dimensions.

#### **4.6.3.1 Footprint**



#### **Figure 24: ZED-X20P suggested footprint (i.e. copper mask)**

| Symbol | Dimension (mm) | Symbol | Dimension (mm) |
|--------|----------------|--------|----------------|
| A      | 23.00          | B      | 17.40          |
| C      | 1.50           | D      | 0.80           |
| E      | 1.10           | F      | 2.10           |
| G      | 1.10           | H      | 1.05           |
| I      | 0.55           | J      | 9.95           |
| K      | 7.45           | L      | 0.85           |
| M      | 2.80           | N      | 0.20           |
| O      | 1.35           | P      | 1.00           |
| Q      | 0.50           | -      | -              |

**Table 47: ZED-X20P footprint dimensions**



ZED-X20P - Integration manual

#### **4.6.3.2 Paste mask**



#### **Figure 25: ZED-X20P suggested paste mask**

| Symbol | Dimension (mm) | Symbol | Dimension (mm) |
|--------|----------------|--------|----------------|
| C      | 1.55           | D      | 0.75           |
| E      | 1.05           | F      | 2.10           |
| G      | 1.10           | H      | 1.05           |
| I      | 0.55           | J      | 10.00          |
| K      | 7.50           | L      | 0.90           |
| M      | 2.85           | N      | 0.20           |
| O      | 1.35           | -      | -              |

**Table 48: ZED-X20P paste mask dimensions**

#### <span id="page-69-0"></span>**4.6.4 Layout guidance**

The presented layout guidance reduces the risk of performance issues at design level.

#### **4.6.4.1 RF In trace**

The RF in trace has to work in the combined GNSS signal bands.

For FR-4 PCB material with a dielectric permittivity of for example 4.7, the trace width for the 50 Ω line impedance can be calculated.



A grounded co-planar RF trace is recommended as it provides the maximum shielding from noise with adequate vias to the ground layer.

The RF trace must be shielded by vias to ground along the entire length of the trace and the ZED-X20P **RF\_IN** pad should be surrounded by vias as shown in the figure below.



**Figure 26: RF input trace**

The **RF\_IN** trace on the top layer should be referenced to a suitable ground layer.

#### **4.6.4.2 Vias for the ground pads**

The ground pads under the ZED-X20P high precision receiver need to be grounded with vias to the lower ground layer of the PCB. A solid ground layer fill on the top layer of the PCB is recommended. This is shown in the figure below.



**Figure 27: Top layer fill and vias**



#### **4.6.4.3 VCC pads**

The **VCC** pads for the ZED-X20P high precision receiver must have as low impedance as possible with large vias to the lower power layer of the PCB. The **VCC** pads need a large combined pad and the de-coupling capacitors must be placed as close as possible. This is shown in the figure below.



**Figure 28: VCC pads**



## <span id="page-72-0"></span>**5 Production test**

u-blox delivers products of the highest quality to its customers. To achieve this, we only supply fully tested units. At the end of the production process, every unit is tested. Defective units are analyzed in detail to continuously improve the production quality.

This is achieved with automatic test equipment, which delivers a detailed test report for each unit. The following measurements are done:

- Digital self-test (software download, verification of FLASH firmware, etc.)
- Measurement of voltages and currents
- Measurement of RF characteristics (e.g. C/N0)

Thanks to the 100 % test coverage done by u-blox, the OEM manufacturer doesn't need to repeat firmware tests or measurements of the GNSS parameters/characteristics (e.g. TTFF) in the production test.

The OEM manufacturer can focus on testing:

- Overall sensitivity of the device (including antenna, if applicable)
- Communication to a host controller

## <span id="page-72-1"></span>**5.1 Connected sensitivity test**

The best way to test the sensitivity of a positioning device is with the use of a GNSS simulator. It assures reliable and constant signals at every measurement.

Guidelines for sensitivity tests:

- Connect a GNSS simulator to the OEM product
- Choose the power level in a way that the "Golden Device" would report a C/N0 ratio of 38-40 dBHz
- Power up the DUT (Device Under Test) and allow enough time for the acquisition
- Read the C/N0 value from the NMEA GSV or the UBX-NAV-SAT message (e.g. with u-center)
- Compare the results to a "Golden Device", a u-blox Evaluation Kit or Application Board.

## <span id="page-72-2"></span>**5.2 Go/no go tests for integrated devices**

- For best results, place the device in an outdoor position with excellent sky view (HDOP < 3.0).
- Let the receiver acquire satellites and compare the signal strength with a "Golden Device". As the electro-magnetic field of a signal repeaters is not homogenous, indoor tests are not reliable in most cases.

These kinds of tests are useful as a go/no go test but not for sensitivity measurements.



## <span id="page-73-0"></span>**6 Product handling**

## <span id="page-73-1"></span>**6.1 ESD precautions**

CAUTION! Risk of electrostatic discharge (ESD) damage. u-blox chips and modules are electrostatic sensitive devices containing highly sensitive electronic circuitry. A discharge of static electricity may damage the device or reduce the life expectancy of the device. To avoid ESD damage, adhere to the standard guidelines for handling ESD devices.

Consider the following:

#### **Preventing electrostatic discharge**

- Keep components in their original packages during transport.
- Open the package within an ESD-protected area (EPA), as in [Figure](#page-74-2) 29.
- At a workstation, store components in an EPA.
- PlaceESD sensitive devices inside of shielding packaging or containers when transported outside of an EPA.
- Use protective clothing and proper personnel grounding at all necessary points when touching electrostatic sensitivedevice or assembly. For instance, wear ESD-safe clothing and shoes and wear an ESD wrist strap connected to a groundedworkstation. Use heel straps when standing on conductive floors or dissipating floor mats.
- Hold the devices by the edges and avoid touching component contacts, pins, or circuitry

#### **Product handling**

- When handling RF transceivers and patch antennas, work in an EPA.
- When connecting test equipment or any other electronics to the module (as a standalone or PCBmounted device), the first point of contact must always be between the local ground and the PCB ground.
- Before mounting a ceramic patch antenna, connect the device to ground.
- When handling the RF pin, do not touch any charged capacitors. Be especially careful when handling materials likepatch antennas (~10 pF), coaxial cables (~50-80 pF/m), soldering irons, or any other materials that can develop charges.
- If there is any risk of touching an exposed antenna area in a non-ESD protected work area, implement proper ESDprotection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, use an ESD-safe soldering iron (tip)



<span id="page-74-2"></span>

**Figure 29: Standard workstation setup for safe handling of ESD-sensitive devices**

## <span id="page-74-0"></span>**6.2 Safety precautions**

The ZED-X20Pmodulesmust be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1. In addition to external limited power source, only Separated or Safety Extra-Low Voltage (SELV) circuits are to be connected to the module including interfaces and antennas.

For more information about SELV circuits see section 2.2 in Safety standard IEC 60950-1.

## <span id="page-74-1"></span>**6.3 Soldering**

Reflow soldering procedures are described in the IPC/JEDEC J-STD-020 standard.

When populating the modules, make sure that the pick and place machine is aligned to the copper pins of the module instead of the module edge.

#### **Soldering paste**

Use of "no clean" soldering paste is highly recommended, as it does not require cleaning after the soldering process. For instance, the following paste meets these criteria.

- Soldering paste: OM338 SAC405 / Nr.143714 (Cookson Electronics)
- Alloy specification: Sn 95.5/ Ag 4/ Cu 0.5 (95.5% tin/ 4% silver/ 0.5% copper)
- Melting temperature: 217 °C
- Stencil: The exact geometry, distances, stencil thicknesses and solder paste volumes must be adapted to the customer's specific production processes.

#### **Reflow soldering**

CAUTION. Risk of device damage. Exceeding the peak temperature of the recommended soldering profile may permanently damage the device.

The final soldering temperature chosen at the factory depends on additional external factors such as the choice of soldering paste, size, thickness and properties of the base board, etc.



As a reference, see "IPC-7530 Guidelines for temperature profiling for mass soldering (reflow and wave) processes", published in 2001.

A convection-type soldering oven is highly recommended over the infrared-type radiation oven. Convection-heated ovens allow precise control of the temperature, and all parts will heat up evenly, regardless of material properties, thickness of components and surface color.

CAUTION. Risk of device damage. Modules must not be soldered with a damp heat process.

To avoid falling off, the modules should be placed on the topside of the board during soldering.

For the recommended soldering profile and conditions, see [Figure](#page-75-0) 30 and [Table](#page-75-1) 49

<span id="page-75-0"></span>

**Figure 30: Recommended soldering profile**

<span id="page-75-1"></span>

| Phase                 | Value        | Details                                                                                                                                                                                  |
|-----------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Preheating            |              | During the initial heating of component leads and balls,<br>residual humidity is dried out. Note that the preheating phase<br>does not replace prior baking procedures.                  |
| Temperature rise rate | Max 3 °C/s   | If the temperature rise is too rapid in the preheat phase,<br>excessive slumping may be caused.                                                                                          |
| Time                  | 60 – 120 s   | If the preheating is insufficient, rather large solder balls tend<br>to be generated. Conversely, if performed excessively, fine<br>balls and large balls will be generated in clusters. |
| End temperature       | 150 – 200 °C | If the temperature is too low, non-melting tends to be caused<br>in areas containing large heat capacity.                                                                                |
| Heating - reflow      |              |                                                                                                                                                                                          |



| Phase                                | Value      | Details                                                                                                                                                                                                                                                                   |  |  |
|--------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Time limit above 217 °C<br>40 – 60 s |            | The temperature rises above the liquidus temperature of 217                                                                                                                                                                                                               |  |  |
| liquidus temperature                 |            | °C. Avoid a sudden rise in temperature as the slump of the<br>paste could become worse.                                                                                                                                                                                   |  |  |
| Peak reflow temperature              | 245 °C     |                                                                                                                                                                                                                                                                           |  |  |
| Cooling                              |            |                                                                                                                                                                                                                                                                           |  |  |
| Temperature fall rate                | Max 4 °C/s | A controlled cooling prevents negative metallurgical effects<br>of the solder (solder becomes more brittle) and possible<br>mechanical tensions in the products. Controlled cooling helps<br>to achieve bright solder fillets with a good shape and low<br>contact angle. |  |  |

**Table 49: Recommended conditions for reflow soldering**

#### **Optical inspection**

After soldering the module, consider optical inspection.

#### **Wave soldering**

Base boards with combined through-hole technology (THT) components and surface-mount technology (SMT) devices require wave soldering to solder the THT components. Only a single wave soldering process is encouraged for boards populated with modules.

### <span id="page-76-0"></span>**6.4 Safe handling of modules**

This section outlines safe practices of handling modules.

#### **Cleaning**

- Do not clean the module with water, solvent, or ultrasonic cleaner:
  - Cleaning with water leads to capillary effects where water is absorbed into the gap between the baseboard and the module. The combination of residues of soldering flux and encapsulated water leads to short circuits or resistor-like interconnections between neighboring pins.
  - Cleaning with alcohol or other organic solvents can result in soldering flux residues flowing underneath the module, into areas that are not accessible for post-cleaning inspections. The solvent also damages the sticker and the printed text on the module.
- CAUTION. Risk of device damage. Ultrasonic cleaning permanently damages the module, in particular the quartz oscillators.

The best approach is to use a "no clean" soldering paste to eliminate the cleaning step after the soldering.

#### **Repeated reflow soldering**

Repeated reflow soldering processes or soldering the module upside down are not recommended.

A board that is populated with components on both sides may require more than one reflow soldering cycle. In such a case, the process should ensure the module is only placed on the board submitted for a single final upright reflow cycle. A module placed on the underside of the board may detach during a reflow soldering cycle due to lack of adhesion.

The module can also tolerate an additional reflow cycle for rework purposes.

After the module is removed from the reflow oven, clean the pins before reapplying the solder paste, placing the module in the oven and proceeding with the reflow soldering of a new module.

#### **Rework**



- CAUTION. Risk of device damage. Using a hot air gun is an uncontrolled process. It can lead to overheating and severely damage the module. Always avoid overheating the module.
- Never attempt to alter the module itself, e.g. by replacing individual components. Such actions immediately void the warranty.

#### **Conformal coating**

Certain applications employ a conformal coating of the PCB using HumiSeal® or other related coating products. These materials affect the RF properties of the GNSS. It is important to prevent them from flowing into the module. The RF shields do not provide 100% protection for the module from coating liquids with low viscosity. Apply the coating carefully.

Conformal coating of the module voids the warranty.

#### **Casting**

If casting is required, use viscose or another type of silicon pottant. The OEM is strongly advised to qualify that such processes are suitable for the module before implementing them in the production.



#### **Grounding metal covers**

Attempts to improve grounding by soldering ground cables, wick or other forms of metal strips directly onto the EMI covers is done at the customer's own risk. The numerous ground pins should be sufficient to provide optimum immunity to interference and noise.

u-blox provides no warranty for damages to the module caused by soldering metal cables or any other forms of metal strips directly onto the EMI covers.

#### **Use of ultrasonic processes**

Some components on the module are sensitive to ultrasonic waves.

- CAUTION. Risk of device damage. Use of any ultrasonic processes (cleaning, welding etc.) may cause damage to the receiver.
- u-blox provides no warranty against damages to the module caused by ultrasonic processes.



## <span id="page-78-0"></span>**Appendix**

## <span id="page-78-1"></span>**A Migration**

u-blox is committed to ensuring that products in the same form factor are backwards compatible over several technology generations.

This section describes the main differences to consider when migrating from ZED-F9P to the ZED-X20P module.

#### <span id="page-78-2"></span>**A.1 Hardware functionality**

The ZED-X20P module is pin-to-pin compatible with u-blox ZED-F9P module other than USB interface. It is recommended to have a design review with a u-blox support team to verify proper use of the product features[.Table](#page-78-4) 50 presents the key hardware-related changes between ZED-F9P and ZED-X20P modules.

<span id="page-78-4"></span>

| Functionality     | ZED-F9P          | ZED-X20P                   | Action needed/remarks                                      |
|-------------------|------------------|----------------------------|------------------------------------------------------------|
| Antenna bands     | L1, L2 or L1, L5 | All bands                  | Using all bands requires an antenna that<br>supports them. |
| Internal LNA gain | Not supported    | Normal gain or<br>low gain | For more details, see Internal LNA modes                   |
| USB interface     | Supported        | Not supported              |                                                            |

**Table 50: Summary of hardware differences**

## <span id="page-78-3"></span>**B Reference Design**

The key features of a typical ZED-X20P design include:

- **V\_BCKP supply (optional):** If present, the hardware backup mode is supported. This mode maintains the RTC time and GNSS orbit data in the battery-backed RAM memory if the main supply is switched off.
- **Active antenna** can be supplied either with the **VCC\_RF** output from ZED-X20P or an external power supply.
- **UART communication interfaces:** UART1 and UART2 communication interfaces are available.
- **PIOs (EXTINT, TIMEPULSE):** For a typical design, these can be left open.
- **RESET\_N and SAFEBOOT\_N connections:** It is recommended to connect these to the host system to enable hardware reset and safe boot mode.
- **Current limiter circuitry:** Designs using the **VCC\_RF** output to supply the GNSS antenna require a current limiter circuitry to protect against short circuits on the antenna side. The antenna bias indicates the required components, and the R19 resistor value determines the maximum current in the event of an antenna short circuit.

For more details, see [VCC\\_RF](#page-64-1) power supply.

For antenna supervisor design, see Antenna [supervisor](#page-64-0) circuit.





**Figure 31: Typical ZED-X20P design**

## <span id="page-79-0"></span>**C Reference frames**

Real time kinematic (RTK) is a differential system where the rover uses the corrections from a reference station or a reference station network. The rover receiver will calculate its position in the reference frame used by the service provider in its correction stream. If the output is required in a different reference frame, then a (custom) datum transformation is required.

For example, if an application requires the position in the ITRF14 reference frame but the correction service is using the ETRF14 reference frame - to which the RTK solution will also be referring - then this reference frame offset needs to be compensated. For example if utilizing a truth system which is using corrections referring to different reference frame, it is important to compensate for the reference frame offset to avoid systematic errors in the analysis.

Terrestrial reference system is a coordinate reference system which is rotating in space with the rotation of the Earth. The reference system is an abstract concept that is realized by obtaining coordinates for some points on the surface of the Earth. This kind of realization is called a reference frame. For more details, see for example the ITRF [webpage](http://itrf.ensg.ign.fr/trs_trf.php). Commonly used reference systems include International Terrestrial Reference System (ITRS) and European Terrestrial Reference System 1989 (ETRS89).

Widely used reference frames include for example International Terrestrial Reference Frame (ITRF) andEuropeanTerrestrial Reference Frame (ETRF). ITRF is a realization of ITRS, done every few years. Latest realizations of ITRF are ITRF2008 and ITRF2014. ETRF is a realization of ETRS89, done every few years. Latest realizations are ITRF2005 and ETRF2014.

For example, the EUREF is used to realize the ETRS89. For information, see their homepage: [EUREF](http://www.epncb.oma.be/).



See the ITRF website for more information and an online transform calculator: [ITRF](http://itrf.ensg.ign.fr/ITRF_solutions/index.php).

Another online tool for transformations is available on the EUREF network page: [EUREF](http://www.epncb.oma.be/_productsservices/coord_trans/) [Transformation](http://www.epncb.oma.be/_productsservices/coord_trans/).

Reference frames can have constant offsets between each other but, in addition to that, they can also drift and rotate with respect to each other. One major reason for this is that the tectonic plates move constantly and the reference frames that are attached to the tectonic plates move along with the plates.

The ZED-X20P stores the EGM96 geoid model with limited resolution, leading to degraded precision of the reported mean sea level height and geoid separation. If the user application needs higher geoid separation accuracy, it is required to apply its own adjustment to the ellipsoidal height output from the ZED-X20P.

## <span id="page-80-0"></span>**D Creating RTK configuration with u-center 2**

This section provides instructions on using u-center 2 to configure base and rover operation.

#### <span id="page-80-1"></span>**D.1 Creating static base configuration with u-center 2**

Configure the module for base station operation as follows:

- **1.** Start u-center 2 and connect to the ZED-X20P device.
- **2.** In u-center 2, open the **Device configuration** window, **Advanced configuration** tab containing the list of configuration items.
- **3.** Expand the CFG-MSGOUT group.
- **4.** Select each required RTCM message. Set the value to 1 and click **Set**. The message is displayed in the **Configuration changes** pane as in [Figure](#page-80-2) 32
- **5.** Once all the required RTCM messages have been added to the list, send them to the receiver by clicking **Send**.

<span id="page-80-2"></span>

| <b>Device configuration</b>   |                                                                        |           |                                                             |                |              | Device - COM35 |      | $\times$<br>□ |
|-------------------------------|------------------------------------------------------------------------|-----------|-------------------------------------------------------------|----------------|--------------|----------------|------|---------------|
| <b>Categories</b>             | $\equiv \blacktriangleright$ Filter parameters by name and description |           |                                                             |                |              |                |      |               |
| Quick configuration           | <b>Configuration items</b>                                             | 81<br>. . | CFG-MSGOUT-RTCM 3X TYPE4072 0 UART1                         |                |              |                |      |               |
| <b>Advanced configuration</b> |                                                                        |           | Output rate of the RTCM-3X-TYPE4072_0 message on port UART1 |                |              |                |      |               |
|                               | PUBX ID POLYT UART2<br>ゝ同<br>$: 01 -$                                  |           |                                                             |                |              |                |      |               |
|                               | PUBX ID POLYT USB<br>$\rightarrow \boxdot$<br>$: 01 -$                 |           | Key name (ID): 0x209102ff                                   |                |              |                |      |               |
|                               | RTCM 3X TYPE1005 I2C<br>〉同<br>$: U1 -$                                 |           | Value (hex)<br><b>Value (raw)</b>                           |                |              |                |      |               |
| Quick preset examples $\vee$  | RTCM_3X_TYPE1005_SPI<br>ゝ同<br>$101 -$                                  |           | $\overline{1}$<br>$\blacksquare$                            |                |              |                |      |               |
| D Vehicle tracker             | > 5<br>RTCM_3X_TYPE1005_UART1 : U1 1                                   |           | Write to layer                                              |                |              |                |      |               |
| People tracker                | RTCM 3X TYPE1005 UART2 : U1 -<br>ゝ同                                    |           |                                                             |                |              |                |      |               |
| □ Wearable application        | RTCM_3X_TYPE1005_USB<br>> 同<br>$: 01 -$                                |           | $\vee$ RAM<br><b>BBR</b><br><b>Flash</b>                    |                |              |                |      |               |
| Saved configurations $\vee$   | RTCM_3X_TYPE1074_I2C<br>> 5<br>$101 -$                                 |           | <b>Action</b>                                               |                |              |                |      |               |
|                               | RTCM_3X_TYPE1074_SPI<br>> 5<br>$101 -$                                 |           | <b>Delete</b><br>Set                                        |                |              |                |      |               |
| + Import                      | RTCM 3X TYPE1074 UART1 : U1 -<br>ゝ同                                    |           |                                                             |                |              |                |      |               |
|                               | RTCM 3X TYPE1074 UART2 : U1 -<br>〉同                                    |           |                                                             |                |              |                |      |               |
|                               | RTCM_3X_TYPE1074_USB<br>> 5<br>$-101 -$                                |           |                                                             |                |              |                |      |               |
|                               | > 5<br>RTCM_3X_TYPE1077_I2C<br>$: 01 -$                                |           |                                                             |                |              |                |      |               |
|                               | RTCM 3X TYPE1077 SPI<br>$>$ $\Box$<br>$: 01 -$                         |           |                                                             |                |              |                |      |               |
|                               | RTCM 3X TYPE1077 UART1 : U1 1<br>ゝ同                                    |           | * Configuration changes<br>Message hex codes                |                |              |                |      |               |
|                               | RTCM_3X_TYPE1077_UART2 : U1 -<br>> 5                                   |           |                                                             |                |              |                |      |               |
|                               | RTCM_3X_TYPE1077_USB<br>ゝ同<br>$101 -$                                  |           | <b>Keyname (Key ID)</b>                                     | Layer          | Value (raw)  | <b>Action</b>  |      |               |
|                               | RTCM_3X_TYPE1084_I2C<br>> 5<br>$: 01 -$                                |           | CFG-MSGOUT-RTCM 3X TYPE1005 UART1<br>$\circ$                | <b>RAM</b> (0) | $\mathbf{1}$ | <b>Set</b>     | Edit | Clear         |
|                               | RTCM 3X TYPE1084 SPI<br>〉同<br>$: 01 -$                                 |           | C CFG-MSGOUT-RTCM 3X TYPE1077 UART1<br>$\overline{c}$       | <b>RAM</b> (0) | -1           | Set            | Edit | Clear         |
|                               | RTCM_3X_TYPE1084_UART1 : U1 -<br>> 5                                   |           | CFG-MSGOUT-RTCM 3X TYPE1087 UART1<br>$\circ$<br>з           | <b>RAM</b> (0) | -1           | Set            | Edit | Clear         |
|                               | > 5<br>RTCM_3X_TYPE1084_UART2 : U1 -                                   |           | CFG-MSGOUT-RTCM 3X TYPE1097 UART1<br>4                      | <b>RAM</b> (0) | -1.          | Set            | Edit | Clear         |
|                               | RTCM_3X_TYPE1084_USB<br>ゝ同<br>$: 01 -$                                 |           |                                                             |                |              |                |      |               |
|                               | > 7<br>RTCM 3X TYPE1087 I2C<br>$: 01 -$                                |           | 5 CFG-MSGOUT-RTCM_3X_TYPE1127_UART1                         | <b>RAM (0)</b> | -1           | Set:           | Edit | Clear         |
|                               | RTCM_3X_TYPE1087_SPI<br>〉同<br>$1.01 -$                                 |           | 6 CFG-MSGOUT-RTCM_3X_TYPE1230_UART1                         | <b>RAM (0)</b> | -1           | Set.           | Edit | Clear         |
|                               | RTCM_3X_TYPE1087_UART1 : U1 1<br>> 5                                   |           | Va Save changes   <b>El Save as</b>   Ô Revert changes      |                |              |                |      | Clear all     |
|                               | > 7<br>RTCM_3X_TYPE1087_UART2 : U1 -                                   |           |                                                             |                |              |                |      |               |
|                               | RTCM_3X_TYPE1087_USB<br>> 7<br>$: 01 -$                                |           | Send Configurations in batch mode                           |                |              |                | Send |               |
|                               | > 同 RTCM 3X TYPE1094 I2C<br>$-111.$                                    |           |                                                             |                |              |                |      |               |

**Figure 32: Using u-center 2 to configure the module as a static base**

**6.** Set the receiver in the base mode by enabling a survey-in procedure or specify fixed coordinates via items within the **Time Mode** of **Quick configuration** window. An example of survey-in configuration is shown in [Figure](#page-81-1) 33.



<span id="page-81-1"></span>

| <b>Device configuration</b> |                                      | COM17<br>п<br>$\times$                                                                                                                                                                                                 |  |  |  |
|-----------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| Categories                  | <b>Quick configurations</b>          | <b><i>O</i></b> Reload values<br><b>Time mode</b>                                                                                                                                                                      |  |  |  |
| Quick configuration         | <b>E</b> Constellation configuration |                                                                                                                                                                                                                        |  |  |  |
| Advanced configuration      | Time Mode                            | This allows the simple configuration of a time mode compatible device (supports CFG-TMODE configuration<br>properties). Your selections will be used to construct a set of CFG-TMODE configuration properties packaged |  |  |  |
|                             | 同 Time Pulse Mode                    | in a single UBX-CFG-VALSET message that will write to the device's selected layers. If a device is connected,                                                                                                          |  |  |  |
|                             | <b>D</b> OSNMA configuration         | this constructed UBX-CFG-VALSET message can be sent to the device.                                                                                                                                                     |  |  |  |
|                             |                                      | <b>Receiver mode</b>                                                                                                                                                                                                   |  |  |  |
|                             |                                      | 0 - Disabled<br>$\bigcirc$ 1 - Survey in<br>2 - Fixed                                                                                                                                                                  |  |  |  |
|                             |                                      | <b>Survey in mode</b>                                                                                                                                                                                                  |  |  |  |
|                             |                                      | Minimum duration [s]:<br>60                                                                                                                                                                                            |  |  |  |
|                             |                                      | Position accuracy limit [mm]:<br>5000                                                                                                                                                                                  |  |  |  |
|                             |                                      | <b>Fixed mode</b>                                                                                                                                                                                                      |  |  |  |
|                             |                                      | Fixed position accuracy [mm]:<br>$\overline{0}$                                                                                                                                                                        |  |  |  |
|                             |                                      | Position type:<br>$\circ$ 0 - ECEF<br>$1 - LLH$                                                                                                                                                                        |  |  |  |
|                             |                                      | <b>Write to layer</b>                                                                                                                                                                                                  |  |  |  |
|                             |                                      | <b>BBR</b><br>$\checkmark$<br><b>RAM</b><br>Flash                                                                                                                                                                      |  |  |  |
|                             |                                      | <b>Hex string</b>                                                                                                                                                                                                      |  |  |  |
|                             |                                      | B5 62 06 8A 19 00 01 01 00 00 01 00 03 20 01 10 00 03 40 3C 00 00 00 11 00 03 40 50 C3<br>00 00 C6 D6                                                                                                                  |  |  |  |
|                             |                                      |                                                                                                                                                                                                                        |  |  |  |
|                             |                                      | Sending configuration was<br>✓<br>successful                                                                                                                                                                           |  |  |  |

**Figure 33: Configuring survey-in with u-center 2**

- **7.** When using the survey-in mode, select the settings based on the environment and achievable accuracy in the base location. Start with an estimated accuracy of 50000 (0.1 mm x 50000 = 5 m) and survey-in time of 60 seconds. In difficult satellite visibility, the base is unlikely to achieve an accuracy better than 1 m.
- **8.** In multi-path conditions, it can take longer to achieve the specified accuracy. To achieve that, you may need to relocate the base antenna or extend the required accuracy and/or survey-in time. Monitor the status of the survey-in with the NAV-SVIN message.
- **9.** The receiver outputs messages upon configuration settings. However, RTCM 1005 is output only once the survey-in has been completed, or the fixed coordinates have been entered for the base antenna.
- **10.** Verify the message output in the u-center 2 **Packet Console View**. Once surveyed-in correctly, it indicates a TIME solution mode in the u-center 2 **Data view**.
- The configuration illustration shows the use of RTCM MSM7 messages. MSM4 messages are equally applicable as recommended in the receiver configuration section.

#### <span id="page-81-0"></span>**D.2 Creating rover configuration with u-center 2**

- **1.** Set an appropriate baud rate to UART1 for communicating with the host.
- **2.** Enable receiver status monitoring by enabling a set of output messages.
- **3.** Monitor the RTK status in u-center 2 to make sure the receiver is getting correction data:
  - Monitor the UBX-RXM-COR message view to confirm the required RTCM correction messages, most importantly including RTCM 1005 or 1006, are being received.
  - Check the position status of the receiver in the **Fix mode** field in the **Data view(Add view > Data view)**. This displays **Float** or **Fixed** if correction data is used.
  - Alternatively, in the UBX-NAV-PVT (Add view > Message view) message view, check that the **carrSoln** field shows the Carrier phase range solution status. The value should be 1 (Float) or 2 (Fixed) if correction data is used.
  - Once the rover has started receiving valid RTCM messages, it transitions through 3D Fix to 3D/DGNSS to Float, and, ultimately, into Fixed mode. This occurs when it has received all required RTCM messages, including RTCM 1005 or 1006, under sufficient signal conditions. See [Figure](#page-82-0) 34.



<span id="page-82-0"></span>

|   | Workspace<br>$\triangleright$ Play log<br>(®) Record log<br>ExplorerKit & |                                                                                                                                                                                                                           |                                                      |  |  |
|---|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|--|--|
| Ф | $\times$<br><b>Add view</b>                                               | $\pm$<br>Consoles $\times$<br>Views $\times$                                                                                                                                                                              |                                                      |  |  |
|   |                                                                           | $\times$<br><b>5</b> Message View                                                                                                                                                                                         | $O \times$<br>5 Data View                            |  |  |
| 即 | <b>Info &amp; Statistics</b>                                              | ति<br>√ Autopoll<br>$=$<br>Filter messages                                                                                                                                                                                | Fix mode: 3D-fix/FIXED<br>TTFF: 15.194 s             |  |  |
| ⊙ | $\equiv$<br><b>Message View</b>                                           | EKFSTATUS - (Dead Reckoning softw<br>Table<br><b>Tree</b><br>$\rightarrow$ EOE - (End of epoch)                                                                                                                           | Longitude: - 0.074828237°<br>Latitude: 52.222733118° |  |  |
|   | <b>Console View</b><br>IЕ                                                 | Clear <sub>Os</sub><br><b>UBX-NAV-PVT</b><br>GEOFENCE - (Geofencing status)<br>nano 475305 ns<br>HPPOSECEF - (High precision positio                                                                                      | Altitude: 129,0010 m<br>Altitude MSL: 83.2469 m      |  |  |
| 白 | ₽<br><b>Data View</b>                                                     | fixTvpe 3<br>HPPOSLLH - (High precision geodetic<br>$\blacktriangledown$ flags $\{\}$ 5 keys<br>IMES - (Indoor Messaging System inf<br>anssFixOK 7                                                                        | Velocity: 0.005 m/s<br>UTC time: 12:49:55            |  |  |
|   | <b>Table View</b>                                                         | NMI - (Navigation message cross-che<br>diffSoln 1<br>$psmState$ $\theta$<br>ODO - (Odometer solution)<br>$\mapsto$<br>$\bigcirc$ $\bigcirc$ $\bigcirc$                                                                    | 3D acc. (0-50): 0.7115 m<br>2D acc. (0-50): 0.3828 m |  |  |
|   | A Chart View                                                              | headVehValid 0<br>ORB - (GNSS orbit database info)<br>carrSoln 2<br>PL - (Protection level information)                                                                                                                   | PDOP (0-10): 1.090<br>HDOP (0-10): 0.660             |  |  |
|   | Location                                                                  | $\blacktriangleright$ flags2 $\{\}$ 3 kevs<br>POSECEF - (Position solution in ECEF)<br>$numSV$ 28<br>POSLLH - (Geodetic position solution)                                                                                | <b>Satellites in navigation</b><br>Used: 24/51       |  |  |
|   | $\circ$<br>Map View                                                       | $1$ on - $\theta$ , $\theta$ 748282 dea<br>PVAT - (Navigation position velocity a<br>lat 52.2227331 deg<br>ら<br>PVT - (Navigation position velocity ti<br>height 128983 mm                                                | Not used: 16/51<br>Not tracked: 11/51                |  |  |
|   | <b>Satellite Views</b>                                                    | RELPOSNED - (Relative positioning i<br>5C 88 78 9B 5A 17 F9 87 83<br><b>AAAA</b><br>62<br>0 <sup>1</sup><br>A7                                                                                                            |                                                      |  |  |
|   | <b>Satellite Position View</b><br>-(0)                                    | A RESETODO<br>8818<br>38 37<br>15 88 88 88 49 48 87 88 83 83 FA<br>8828<br><b>SF 28</b><br>1F D7 F7 01 00 1C 45 01<br>83<br>$\rightarrow$ SAT - (Satellite information)<br>00 00 58 02 00 00 01 00 00 00 FF FF FF<br>0030 |                                                      |  |  |
|   | <b>Satellite Signal View</b>                                              | SBAS - (SBAS status data)<br>AAA<br>02 00 00 00 00 00 00 00 34 00 00<br>4 SIG-(Signal information)<br>00 00 00 10 00 00 00 00 00 10 00 00 00<br>0.050                                                                     |                                                      |  |  |
|   | 8<br><b>Deviation Map</b>                                                 | <b>5</b> Satellite Position View<br>O<br>$\times$                                                                                                                                                                         |                                                      |  |  |

**Figure 34: Rover in u-center 2 data view with RTK Fixed**

If using a virtual reference service, the rover must output the NMEA GGA message to return to the NTRIP caster. Without this, the NTRIP caster does not provide correction information. NMEA messages are enabled by default on the UART1, I2C and SPI interface.



## <span id="page-83-0"></span>**Related documents**

- <span id="page-83-2"></span>**[1]** ZED-X20P-0B Data sheet, [UBXDOC-963802114-12690](https://www.u-blox.com/docs/UBXDOC-963802114-12690)
- <span id="page-83-1"></span>**[2]** HPG 2.00 Interface description, [UBXDOC-304424225-19888](https://www.u-blox.com/docs/UBXDOC-304424225-19888)
- **[3]** Product packaging reference guide [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



## <span id="page-84-0"></span>**Revision history**

| Revision | Date        | Comments        |
|----------|-------------|-----------------|
| R01      | 19-May-2025 | Initial release |



## **Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).