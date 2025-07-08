

# <span id="page-0-0"></span>**ZED-F9P**

# **High precision GNSS module**

**Integration manual**



### **Abstract**

This document describes the features and application of the ZED-F9P, a multi-band GNSS module with integrated RTK offering centimeter-level accuracy.

**www.u-blox.com**







# **Document information**

| Title                  | ZED-F9P                    |             |
|------------------------|----------------------------|-------------|
| Subtitle               | High precision GNSS module |             |
| Document type          | Integration manual         |             |
| Document number        | UBX-18010802               |             |
| Revision and date      | R16                        | 30-Oct-2024 |
| Disclosure restriction | C1-Public                  |             |

This document applies to the following products:

| Type number    | FW version    | IN/PCN reference       | RN reference           |
|----------------|---------------|------------------------|------------------------|
| ZED-F9P-01B-01 | HPG 1.12      | UBX-19057484           | UBX-19026698           |
| ZED-F9P-02B-00 | HPG 1.13      | -                      | UBX-20019211           |
| ZED-F9P-04B-01 | HPG 1.32      | UBX-22010309           | UBX-22004887           |
| ZED-F9P-15B-00 | HPG L1L5 1.40 | -                      | UBX-23010071           |
| ZED-F9P-05B-00 | HPG 1.50      | -                      | UBXDOC-963802114-12826 |
| ZED-F9P-05B-00 | HPG 1.51      | UBXDOC-963802114-13129 | UBXDOC-963802114-13110 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents and product statuses, visit www.u-blox.com.

Copyright © 2024, u-blox AG.



| 1 Integration<br>manual<br>overview                   | 6 |
|-------------------------------------------------------|---|
| 2 System<br>description7                              |   |
| 2.1 Overview 7                                        |   |
| 2.1.1 Correction services 7                           |   |
| 2.1.2 Real time kinematic7                            |   |
| 2.2 Architecture9                                     |   |
| 2.2.1 Block diagram9                                  |   |
| 2.2.2 Typical ZED-F9P application setups9             |   |
| 3 Receiver<br>functionality12                         |   |
| 3.1 Receiver configuration12                          |   |
| 3.1.1 Changing the receiver configuration 12          |   |
| 3.1.2 Default GNSS configuration 12                   |   |
| 3.1.3 Default interface settings13                    |   |
| 3.1.4 Basic receiver configuration 14                 |   |
| 3.1.5 RTK configuration16                             |   |
| 3.1.6 PPP-RTK configuration24                         |   |
| 3.1.7 Legacy configuration interface compatibility 28 |   |
| 3.1.8 Navigation configuration28                      |   |
| 3.2 Primary and secondary output 33                   |   |
| 3.2.1 Introduction33                                  |   |
| 3.2.2 Configuration 34                                |   |
| 3.2.3 Expected output behavior35                      |   |
| 3.2.4 Example use cases 35                            |   |
| 3.3 SBAS35                                            |   |
| 3.4 QZSS SLAS 37                                      |   |
| 3.4.1 Features 37                                     |   |
| 3.4.2 Configuration 38                                |   |
| 3.5 Geofencing38                                      |   |
| 3.5.1 Introduction38                                  |   |
| 3.5.2 Interface 38                                    |   |
| 3.5.3 Geofence state evaluation 39                    |   |
| 3.5.4 Using a PIO for geofence state output 39        |   |
| 3.6 Logging39                                         |   |
| 3.6.1 Introduction39                                  |   |
| 3.6.2 Setting the logging system up 40                |   |
| 3.6.3 Information about the log40                     |   |
| 3.6.4 Recording 41                                    |   |
| 3.6.5 Retrieval 42                                    |   |
| 3.6.6 Command message acknowledgment43                |   |
| 3.7 Protection level43                                |   |
| 3.7.1 Introduction43                                  |   |
| 3.7.2 Interface 44                                    |   |
| 3.7.3 Expected behavior45                             |   |
| 3.7.4 Example use cases 46                            |   |



| 3.8 Communication interfaces 47                                          |    |
|--------------------------------------------------------------------------|----|
| 3.8.1 UART48                                                             |    |
| 3.8.2 I2C interface49                                                    |    |
| 3.8.3 SPI interface52                                                    |    |
| 3.8.4 USB interface53                                                    |    |
| 3.9 Predefined PIOs54                                                    |    |
| 3.9.1 D_SEL54                                                            |    |
| 3.9.2 RESET_N 54                                                         |    |
| 3.9.3 SAFEBOOT_N54                                                       |    |
| 3.9.4 TIMEPULSE 55                                                       |    |
| 3.9.5 TX_READY 55                                                        |    |
| 3.9.6 EXTINT55                                                           |    |
| 3.9.7 GEOFENCE_STAT interface 56                                         |    |
| 3.9.8 RTK_STAT interface56                                               |    |
| 3.10 Antenna supervisor56                                                |    |
| 3.10.1 Antenna voltage control - ANT_OFF 57                              |    |
| 3.10.2 Antenna short detection - ANT_SHORT_N57                           |    |
| 3.10.3 Antenna short detection auto recovery58                           |    |
| 3.10.4 Antenna open circuit detection - ANT_DETECT58                     |    |
| 3.11 Multiple GNSS assistance (MGA)59                                    |    |
| 3.11.1 Authorization59                                                   |    |
| 3.11.2 Preserving MGA and operational data during power-off59            |    |
| 3.12 Clocks and time60                                                   |    |
| 3.12.1 Receiver local time 60                                            |    |
| 3.12.2 Navigation epochs60                                               |    |
| 3.12.3 iTOW timestamps 61                                                |    |
| 3.12.4 GNSS times61                                                      |    |
| 3.12.5 Time validity61                                                   |    |
| 3.12.6 UTC representation62                                              |    |
| 3.12.7 Leap seconds62                                                    |    |
| 3.12.8 Real-time clock63                                                 |    |
| 3.12.9 Date63                                                            |    |
| 3.13 Timing functionality64                                              |    |
| 3.13.1 Time pulse64                                                      |    |
| 3.13.2 Time mark 67                                                      |    |
| 3.14 Security68                                                          |    |
| 3.14.1 Spoofing detection and monitoring69                               |    |
| 3.14.2 Jamming and interference detection and monitoring 69              |    |
| 3.14.3 Spoofing and jamming indication69                                 |    |
| 3.14.4 GNSS receiver security69                                          |    |
| 3.14.5 Galileo Open Service Navigation Message Authentication (OSNMA) 70 |    |
| 3.15 u-blox protocol feature descriptions74                              |    |
| 3.15.1 Broadcast navigation data 74                                      |    |
| 3.16 Forcing a receiver reset82                                          |    |
| 3.17 Firmware upload 82                                                  |    |
| 3.18 Spectrum analyzer83                                                 |    |
| 3.19 Production test 84                                                  |    |
| 3.19.1 Connected sensitivity test 84                                     |    |
| 3.19.2 Go/No go tests for integrated devices85                           |    |
| 4 Design                                                                 | 86 |



| 4.1 Pin assignment86                                             |     |
|------------------------------------------------------------------|-----|
| 4.2 Power supply88                                               |     |
| 4.2.1 VCC: Main supply voltage 88                                |     |
| 4.2.2 V_BCKP: Backup supply voltage 88                           |     |
| 4.2.3 ZED-F9P power supply 89                                    |     |
| 4.3 ZED-F9P minimal design 89                                    |     |
| 4.4 Antenna90                                                    |     |
| 4.4.1 Active Antenna Power Supply92                              |     |
| 4.4.2 Antenna supervisor circuit95                               |     |
| 4.5 EOS/ESD precautions 97                                       |     |
| 4.5.1 ESD protection measures 97                                 |     |
| 4.5.2 EOS precautions97                                          |     |
| 4.5.3 Safety precautions 98                                      |     |
| 4.6 Electromagnetic interference on I/O lines98                  |     |
| 4.6.1 General notes on interference issues98                     |     |
| 4.6.2 In-band interference mitigation99                          |     |
| 4.6.3 Out-of-band interference 99                                |     |
| 4.7 Layout100                                                    |     |
| 4.7.1 Placement100                                               |     |
| 4.7.2 Thermal management100                                      |     |
| 4.7.3 Package footprint, copper and paste mask100                |     |
| 4.7.4 Layout guidance102                                         |     |
| 4.8 Design guidance 104                                          |     |
| 4.8.1 General considerations104                                  |     |
| 4.8.2 Backup battery104                                          |     |
| 4.8.3 RF front-end circuit options105                            |     |
| 4.8.4 Antenna/RF input105                                        |     |
| 4.8.5 Ground pads106                                             |     |
| 4.8.6 Schematic design106<br>4.8.7 Layout design-in guideline106 |     |
| 4.8.8 I2C design recommendations106                              |     |
|                                                                  |     |
| 5 Product<br>handling108                                         |     |
| 5.1 ESD handling precautions108                                  |     |
| 5.2 Soldering109                                                 |     |
| 5.3 Tapes112                                                     |     |
| 5.4 Reels113                                                     |     |
| Appendix114                                                      |     |
| A Glossary 114                                                   |     |
| B Reference frames 115                                           |     |
| C RTK configuration procedures with u-center 115                 |     |
| C.1 Base configuration with u-center115                          |     |
| C.2 Rover configuration with u-center 119                        |     |
| D Stacked patch antenna123                                       |     |
| Related<br>documents127                                          |     |
|                                                                  |     |
| Revision<br>history                                              | 128 |



# <span id="page-5-0"></span>**1 Integration manual overview**

This document is an important source of information on all aspects of ZED-F9P system, software and hardware design. The purpose of this document is to provide guidelines for a successful integration of the receiver with the customer's end product.



# <span id="page-6-0"></span>**2 System description**

# <span id="page-6-1"></span>**2.1 Overview**

The ZED-F9P positioning module features the u-blox F9 receiver platform, which provides multiband GNSS to high-volume industrial applications. ZED-F9P has integrated u-blox multi-band RTK and PPP-RTK [1](#page-6-4) technologies for centimeter-level accuracy. The module enables precise navigation

and automation of moving machinery in industrial and consumer-grade products in a compact surface-mounted form factor of only

The ZED-F9P includes moving base support, allowing both base and rover to move while computing the position between them. The moving base is ideal for UAV applications where the UAV is programmed to follow its owner or to land on a moving platform. It is also well suited to attitude sensing applications where both base and rover modules are mounted on the same moving platform and the relative position is used to derive attitude information for the vehicle or tool.

Firmware version HPG L1L5 1.40 does not support the moving base feature.

### <span id="page-6-2"></span>**2.1.1 Correction services**

u-blox ZED-F9P can use different types of correction services which broadly fall into two categories, based either on an Observation Space Representation (OSR) or a State Space Representation (SSR) of the errors. These categories use different techniques, delivery mechanisms, and core technologies to solve the same problem – the mitigation of key GNSS errors in order to enable high precision GNSS:

- **1.** OSR services provide GNSS observations from the nearest reference station, or virtual reference station (VRS) to the rover. A communication link from reference station or VRS service provider to the rover is needed. The data is dependent on the position of the rover.
- **2.** SSR services rely on GNSS reference station network to model key errors (such as satellite or atmospheric errors) over large geographical regions and provide corrections to the rover via broadcast link such as internet or satellite L-band. All receivers receive the same data over a large area.

In this document, the following terminology is used: RTK refers to OSR-based solution (using RTCM corrections) while PPP-RTK refers to SSR-based solution (using SPARTN or CLAS corrections).

### <span id="page-6-3"></span>**2.1.2 Real time kinematic**

u-blox ZED-F9P high precision receiver takes GNSS precision to the next level:

- Delivers accuracy down to the centimeter level: 0.01 m + 1 ppm CEP
- Fast time to first fix and robust performance with multi-band, multi-constellation reception
- Compatible with leading correction services for global coverage and versatility

Some typical applications for the ZED-F9P are shown below:

<span id="page-6-4"></span><sup>1</sup> PPP-RTK technology is only available from firmware HPG1.30 onwards













**Figure 1: Typical applications for the ZED-F9P**

#### **2.1.2.1 RTK modes of operation**

The ZED-F9P supports the following modes of operation:

- **1.** ZED-F9P operating as a base: It provides RTCM correction data to a rover, or to a network of rovers.
- **2.** ZED-F9P operating as a rover: It receives RTCM correction data from a ZED-F9P operating as a base, or from a VRS service provider operating a network of base receivers.

#### **2.1.2.2 PPP-RTK modes of operation**

The ZED-F9P operating as a rover supports the following additional operation modes:

- It can receive SPARTN correction data via internet from the data center of the GNSS reference station network
- It can receive SPARTN correction data via L-band satellite channel (a u-blox NEO-D9S may be used for such purposes)
- It can receive CLAS correction data transmitted from Japan's QZSS constellation (from u-blox NEO-D9C message)

### **2.1.2.3 NTRIP - networked transport of RTCM via internet protocol**

Networked Transport of RTCM via internet protocol, or NTRIP, is an open standard protocol for streaming differential data and other kinds of GNSS streaming data over the internet in accordance with specifications published by RTCM.

The NTRIP protocol is also used by SSR correction service providers to stream SSR correction data over the internet (e.g. SPARTN corrections).

There are three major parts to the NTRIP system: The NTRIP client, the NTRIP server, and the NTRIP caster:

- **1.** The NTRIP server is a PC or an on-board computer running NTRIP server software communicating directly with a GNSS reference station. The NTRIP server serves as the intermediary between the GNSS receiver (NTRIP Source) streaming correction data and the NTRIP caster.
- **2.** The NTRIP caster is an HTTP server which receives streaming correction data from one or more NTRIP servers and in turn streams the correction data to one or more NTRIP clients via the internet.
- **3.** The NTRIP client receives streaming correction data from the NTRIP caster to apply as realtime corrections to a GNSS receiver.



u-center GNSS [evaluation](https://www.u-blox.com/en/product/u-center) software provides a NTRIP client and server application that can be used to easily evaluate a ZED-F9P base or rover. Typically a u-center NTRIP client connects to an NTRIP service provider over the internet. The u-center NTRIP client then provides the corrections to a ZED-F9P rover connected to the local u-center application. VRS service is also supported by the u-center NTRIP client.

# <span id="page-8-0"></span>**2.2 Architecture**

The ZED-F9P receiver provides all the necessary RF and baseband processing to enable multi-band, multi-constellation operation. The block diagram below shows the key functionality.



### <span id="page-8-1"></span>**2.2.1 Block diagram**

**Figure 2: ZED-F9P block diagram**

An active antenna is mandatory with the ZED-F9P.

### <span id="page-8-2"></span>**2.2.2 Typical ZED-F9P application setups**

Two application examples are illustrated below as typical system implementations. Both are representative of a simple "short baseline" setup in which the base and rover receivers are within a few hundred meters of each other. In [Figure](#page-9-0) 3 and [Figure](#page-9-1) 4 ZED-F9P is used as a base station providing corrections to a ZED-F9P rover receiver.

Alternatively, the rover can use corrections provided over longer baselines from a correction stream distributed as a subscription service. This method can use a single fixed reference source which is local (within 50 km) to the rover receiver or via a VRS service in which corrections are synthesized based on the rover's location.



The moving base feature also enables derivation of the vehicle orientation by mounting two or three GNSSreceivers onthe same vehicleplatform, i.e.byfixingthepositionof the GNSSantennas relative to each other, as illustrated in [Figure](#page-10-0) 5.

Firmware version HPG L1L5 1.40 does not support the moving base feature.

<span id="page-9-0"></span>

**Figure 3: ZED-F9P base and rover in a short baseline drone application**

<span id="page-9-1"></span>

**Figure 4: ZED-F9P base and rover in a short baseline robotic mower application**



<span id="page-10-0"></span>

**Figure 5: ZED-F9P orientation of a vehicle in space**



# <span id="page-11-0"></span>**3 Receiver functionality**

This chapter describes the ZED-F9P operational features and their configuration.

# <span id="page-11-1"></span>**3.1 Receiver configuration**

ZED-F9P is fully configurable with UBX configuration interface keys. The configuration database in the receiver's RAM holds the current configuration, which is used by the receiver at run-time. It is constructed on startup of the receiver from several sources of configuration. The configuration interface and the available keys are described fully in the applicable Interface description [[2](#page-126-1)].

A configuration setting stored in RAM remains effective until power-down or reset. If stored in BBR (battery-backed RAM), the setting will be used as long as the backup battery supply remains. Configuration settings can be saved permanently in flash memory.

**CAUTION** The configuration interface has changed from earlier u-blox positioning receivers. Legacy messages have been deprecated and will not be supported in future firmware releases. Users are advised to adopt the configuration interface described in this document. See legacy UBX-CFG message fields reference section in the applicable Interface description [\[2\]](#page-126-1).

Configuration interface settings are held in a database consisting of separate configuration items. An item is made up of a pair consisting of a key ID and a value. Related items are grouped together and identified under a common group name: CFG-GROUP-\*; a convention used in u-center and within this document. Within u-center, a configuration group is identified as "Group name" and the configuration item is identified as the "item name" under the "Generation 9 Configuration View" - "Advanced Configuration" view.

The UBX messages available to change or poll the configurations are UBX-CFG-VALSET, UBX-CFG-VALGET, and UBX-CFG-VALDEL. For more information about these messages and the configuration keys, see the configuration interface section in the applicable Interface description [[2\]](#page-126-1).

### <span id="page-11-2"></span>**3.1.1 Changing the receiver configuration**

All configuration messages, including legacy UBX-CFG messages, will result in a UBX-ACK-ACK or UBX-ACK-NAK response. If several configuration messages are sent without waiting for this response then the receiver may pause processing of input messages until processing of a previous configuration message has been completed. When this happens a warning message "wait for cfg ACK" will be sent to the host.

### <span id="page-11-3"></span>**3.1.2 Default GNSS configuration**

The ZED-F9P default GNSS configuration is set as follows:

### **ZED-F9P-01B\02B\04B\05B:**

- GPS: L1C/A, L2C
- GLONASS: L1OF, L2OF
- Galileo: E1B/C, E5b
- BeiDou: B1I, B2I
- QZSS: L1C/A, L2C
- SBAS [2](#page-11-4) : L1C/A

#### **ZED-F9P-15B:**

<span id="page-11-4"></span><sup>2</sup> Supported from firmware version HPG 1.13 onwards



- GPS: L1C/A
- GLONASS: L1OF
- Galileo: E1B/C, E5a
- BeiDou: B1I, B2a
- QZSS: L1C/A, L5
- SBAS: L1C/A

For more information about the default configuration, see the applicable Interface description [\[2](#page-126-1)].

| Interface    | Settings                                                                                                                                                                                                                                                                         |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART1 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                   |
|              | NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output by default.                                                                                                                                                                                             |
|              | UBX and RTCM 3.3 protocols are enabled by default but no output messages are enabled by<br>default.                                                                                                                                                                              |
| UART1 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                   |
|              | UBX, NMEA and RTCM 3.3 input protocols are enabled by default.                                                                                                                                                                                                                   |
|              | SPARTN input protocol is enabled by default.                                                                                                                                                                                                                                     |
| UART2 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                   |
|              | UBX protocol is disabled by default. It can be enabled as an output protocol from firmware version<br>HPG 1.30 onwards. It cannot be enabled as an output protocol on any of the previous firmware<br>versions and will not output UBX messages.                                 |
|              | RTCM 3.3 protocol is enabled by default but no output messages are enabled by default.                                                                                                                                                                                           |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                            |
| UART2 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                   |
|              | UBX protocol is enabled by default from firmware version HPG 1.32 onwards. It can be enabled as<br>an input protocol on firmware version HPG1.30. It cannot be enabled as an input protocol on any<br>of the previous firmware versions and will not receive UBX input messages. |
|              | RTCM 3.3 protocol is enabled by default.                                                                                                                                                                                                                                         |
|              | SPARTN protocol is enabled by default.                                                                                                                                                                                                                                           |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                            |
| USB          | Default messages activated as in UART1. Input/output protocols available as in UART1.                                                                                                                                                                                            |
| I2C          | Available for communication in the Fast-mode with an external host CPU in peripheral mode<br>only. Default messages activated as in UART1. Input/output protocols available as in UART1.<br>Maximum bit rate 400 kb/s.                                                           |
| SPI          | Allow communication to a host CPU, operated in peripheral mode only. Default messages<br>activated as in UART1. Input/output protocols available as in UART1. SPI is not available unless<br>D_SEL pin is set to low (see the D_SEL section).                                    |

### <span id="page-12-0"></span>**3.1.3 Default interface settings**

#### **Table 1: Default interface settings**

UART2 can function as the main interface for receiving corrections; RTCM 3.3 is the default input and output protocol. With firmware versions HPG 1.30 or later, SPARTN [3](#page-12-1) is enabled by default as input protocol. UART2 can also optionally be configured for NMEA input or output protocol.

- Refer to the applicable Interface description [[2](#page-126-1)] for information about further settings.
- By default, ZED-F9P outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.

<span id="page-12-1"></span><sup>3</sup> SPARTN protocol is supported from firmware HPG1.30 onwards



As of firmware version HPG 1.30, it is possible to enable the UBX protocol input/output support on UART2. Do not use UART2 as the only one interface to the host. Not all UBX functionality is available on UART2, such as firmware upgrade, safeboot or backup modes functionalities. No start-up boot screen is sent out from UART2.

### <span id="page-13-0"></span>**3.1.4 Basic receiver configuration**

This section summarizes the basic receiver configuration most commonly used.

#### <span id="page-13-1"></span>**3.1.4.1 Communication interface configuration**

Several configuration groups allow operation mode configuration of the various communication interfaces. These include parameters for the data framing, transfer rate and enabled input/output protocols. See [Communication](#page-46-0) interfaces section for details. The configuration groups available for each interface are:

| Interface | Configuration groups                               |
|-----------|----------------------------------------------------|
| UART1     | CFG-UART1-*, CFG-UART1INPROT-*, CFG-UART1OUTPROT-* |
| UART2     | CFG-UART2-*, CFG-UART2INPROT-*, CFG-UART2OUTPROT-* |
| USB       | CFG-USB-*, CFG-USBINPROT-*, CFG-USBOUTPROT-*       |
| I2C       | CFG-I2C-*, CFG-I2CINPROT-*, CFG-I2COUTPROT-*       |
| SPI       | CFG-SPI-*, CFG-SPIINPROT-*, CFG-SPIOUTPROT-*       |

**Table 2: Interface configurations**

#### **3.1.4.2 Message output configuration**

The rate of the supported output messages is configurable.

If the rate configuration value is zero, then the corresponding message will not be output. Values greater than zero indicate how often the message is output.

For periodic output messages the rate relates to the event the message is related to. For example, the UBX-NAV-PVT (navigation, position, velocity and time solution) is related to the navigation epoch. If the rate of this message is set to one (1), it will be output for every navigation epoch. If the rate is set to two (2), it will be output every other navigation epoch.The rates of the output messages are individually configurable per communication interface. See the CFG-MSGOUT-\* configuration group.

Some messages, such as UBX-MON-VER, are non-periodic and will only be output as an answer to a poll request.

The UBX-INF-\* and NMEA-Standard-TXT information messages are non-periodic output messages that do not have a message rate configuration. Instead they can be enabled for each communication interface via the CFG-INFMSG-\* configuration group.

All message output is additionally subject to the protocol configuration of the communication interfaces.Messages of a givenprotocolwillnot be output until the protocol is enabled for output on the interface (see [Communication](#page-13-1) interface configuration).

#### **3.1.4.3 GNSS signal configuration**

The GNSS constellations and signals are selected using keys from the CFG-SIGNAL-\*. configuration group. Each GNSS constellation can be enabled or disabled independently except for QZSS [4](#page-13-2) and

<span id="page-13-2"></span><sup>4</sup> QZSS can be enabled only if GPS is selected



SBAS [5](#page-14-0) . A GNSS constellation is considered to be enabled when the constellation enable key is set and at least one of the constellation's signal keys is enabled.

ZED-F9P only supports certain combinations of constellations and bands. For all constellations, both L1 and L2 or L1 and L5 bands must either be enabled or disabled. BeiDou B2 and GPS L5 are the exception (can either have BeiDou B1+B2 or B1-only, and either GPS L1+L5 or GPS L1-only). Unsupported combinations will be rejected with a UBX-ACK-NAK and the warning: "inv sig cfg" will be sent via UBX-INF and NMEA-TXT messages (if enabled).

| Constellation key  | Band key              | Band key               | Constellation enabled?  |
|--------------------|-----------------------|------------------------|-------------------------|
| CFG-SIGNAL-GAL_ENA | CFG-SIGNAL-GAL_E1_ENA | CFG-SIGNAL-GAL_E5A_ENA |                         |
|                    |                       | (or) GAL_E5B_ENA       |                         |
| false (0)          | false (0)             | false (0)              | no                      |
| false (0)          | false (0)             | true (1)               | no                      |
| false (0)          | true (1)              | false (0)              | no                      |
| false (0)          | true (1)              | true (1)               | no                      |
| true (1)           | false (0)             | false (0)              | no                      |
| true (1)           | false (0)             | true (1)               | Unsupported combination |
| true (1)           | true (1)              | false (0)              | Unsupported combination |
| true (1)           | true (1)              | true (1)               | yes                     |

The following table shows possible configuration key combinations for the Galileo constellation.

**Table 3: Example of possible values of configuration items for the Galileo constellation**

#### **3.1.4.4 Antenna supervisor configuration**

This section describes the antenna supervisor configuration, its use and restrictions.

The antenna supervisor is used to control an active antenna. The configuration of the antenna supervisor allows the following:

- Control voltage supply to the antenna, which allows the antenna supervisor to cut power to the antenna in the event of a short circuit or optimize power to the antenna in power save mode
- Detect a short circuit in the antenna and auto recover the antenna supply in such an event
- Detect an open antenna, which can be used to indicate if the antenna has been disconnected

See the table below for a description of the configuration items related to the antenna supervisor operation.

| Configuration item                                           | Description                                               | Comments                                                                          |
|--------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------|
| CFG-HW-ANT_CFG_VOLTCTRL                                      | Enable active antenna voltage control                     |                                                                                   |
| CFG-HW-ANT_CFG_SHORTDET                                      | Enable short circuit detection                            |                                                                                   |
| CFG-HW-ANT_CFG_SHORTDET_POL Short antenna detection polarity |                                                           | Set to 1 if the required logic polarity is<br>active-low (default)                |
| CFG-HW-ANT_CFG_OPENDET                                       | Enable open circuit detection                             |                                                                                   |
| CFG-HW-ANT_CFG_OPENDET_POL                                   | Open antenna detection polarity                           | Set to 1 if the required logic polarity is<br>active-low (default)                |
| CFG-HW-ANT_CFG_PWRDOWN                                       | Power down antenna supply if short<br>circuit is detected | Requires CFG-HW<br>ANT_CFG_VOLTCTRL and CFG-HW<br>ANT_CFG_SHORTDET to be enabled. |
| CFG-HW-ANT_CFG_PWRDOWN_POL Power down antenna logic polarity |                                                           | Set to 1 if the required logic polarity is<br>active-high (default)               |

<span id="page-14-0"></span><sup>5</sup> SBAS can be enabled with GPS only or GAL only or both



| Configuration item        | Description                                                                      | Comments                                                                              |
|---------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| CFG-HW-ANT_CFG_RECOVER    | Enable auto recovery in the event of a<br>short circuit                          | To use this feature, enable short<br>circuit detection and CFG-HW<br>ANT_CFG_PWRDOWN. |
| CFG-HW-ANT_SUP_SWITCH_PIN | PIO-Pin (PIO number) used for switching<br>antenna supply                        | It is recommended that you use the<br>default PIO and assigned pin                    |
| CFG-HW-ANT_SUP_SHORT_PIN  | PIO-Pin (PIO number) used for detecting<br>a short circuit in the antenna supply | It is recommended that you use the<br>default PIO and assigned pin                    |

**Table 4: Antenna supervisor configuration**

It is possible to obtain the status of the antenna supervisor through the UBX-MON-RF message. Moreover, any changes in the status of the antenna supervisor are reported to the host interface in the form of notice messages. See the applicable Interface description [\[2\]](#page-126-1) for *antStatus* and *antPower* field description.

| Status   | Description                       |
|----------|-----------------------------------|
| OFF      | Antenna is off                    |
| ON       | Antenna is on                     |
| DONTKNOW | Antenna power status is not known |
|          |                                   |

**Table 5: Antenna power status**

#### **3.1.4.5 NMEA high precision mode**

ZED-F9P supports NMEA high precision mode.This mode increases the number of significant digits of the position output; latitude and longitude will have seven digits after the decimal point, and altitude will have three digits after the decimal point. By default it is not enabled since it violates the NMEA standard. NMEA high precision mode cannot be used while in NMEA compatibility mode or when NMEA output is limited to 82 characters. See configuration item CFG-NMEA-HIGHPREC in the applicable Interface description [[2](#page-126-1)] for more details.

NMEA high precision mode is disabled by default meaning that the default NMEA output will be insufficient to report a high precision position.

### <span id="page-15-0"></span>**3.1.5 RTK configuration**

RTK technology introduces the concept of a base [6](#page-15-1) and a rover. In such a setup, the base sends corrections (complying with the RTCM 3.3 protocol) to the rover via a communication link. This enables the rover to compute its position relative to the base with high accuracy.

When operating as a rover, the ZED-F9P can receive RTCM 3.3 corrections from another ZED-F9P operating as a base, or via NTRIP from a VRS service provider operating a network of base receivers. In this mode, the receiver coordinates will be expressed in the datum used by the RTCM correction provider. For more information refer to the [Reference](#page-114-0) frames section in the Appendix.

After describing the RTCM protocol and corresponding supported message types, this section describes how to configure the ZED-F9P high precision receiver as a base or rover receiver. This includes both the static base use case and the moving base use case.

See the ZED-F9P Moving Base application note [[4](#page-126-2)] for more information on designing in, configuring and using a moving base setup.

<span id="page-15-1"></span><sup>6</sup> The terms base, base station, reference and reference station can be used interchangeably



#### **3.1.5.1 RTCM corrections**

RTCM is a standard-based binary protocol for the communication of GNSS correction information. The ZED-F9P high precision receiver supports RTCM as specified by RTCM 10403.4, Differential GNSS (Global Navigation Satellite Systems) Services – Version 4 (December 1, 2023).

The RTCM specification is currently at version 3.4 and RTCM version 2 messages are not supported by this standard.

To modify the RTCM input/output settings, see the configuration section in the applicable Interface description [\[2\]](#page-126-1).

Users should be aware of the datum used by the correction source. The rover position will provide coordinates in the correction source reference frame. This may need to be taken into account when using the RTK rover position. See the [Reference](#page-114-0) frames section in the Appendix for more information.

| Message type | Description                                              |
|--------------|----------------------------------------------------------|
| RTCM 1001    | L1-only GPS RTK observables                              |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1002    | Extended L1-only GPS RTK observables                     |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1003    | L1/L2 GPS RTK observables                                |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1004    | Extended L1/L2 GPS RTK observables                       |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1005    | Stationary RTK reference station ARP                     |
| RTCM 1006    | Stationary RTK reference station ARP with antenna height |
| RTCM 1007    | Antenna descriptor                                       |
| RTCM 1009    | L1-only GLONASS RTK observables                          |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1010    | Extended L1-only GLONASS RTK observables                 |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1011    | L1/L2 GLONASS RTK observables                            |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1012    | Extended L1/L2 GLONASS RTK observables                   |
|              | Unsupported in firmware version HPG L1L5 1.40.           |
| RTCM 1033    | Receiver and Antenna Description                         |
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

#### **3.1.5.2 List of supported RTCM input messages**



| Message type | Description                                                                        |
|--------------|------------------------------------------------------------------------------------|
| RTCM 1125    | BeiDou MSM5                                                                        |
| RTCM 1127    | BeiDou MSM7                                                                        |
| RTCM 1230    | GLONASS code-phase biases                                                          |
| RTCM 4072.0  | Reference station PVT (u-blox proprietary RTCM Message)                            |
|              | Unsupported in firmware version HPG L1L5 1.40.                                     |
| RTCM 4072.1  | Additional reference station information (u-blox proprietary RTCM Message)         |
|              | Only valid with firmware version HPG 1.12 and necessary for moving base operation. |
|              |                                                                                    |

**Table 6: ZED-F9P supported input RTCM version 3.4 messages**

| 3.1.5.3 List of supported RTCM output messages |  |
|------------------------------------------------|--|
|------------------------------------------------|--|

| Message type | Description                                                                        |
|--------------|------------------------------------------------------------------------------------|
| RTCM 1005    | Stationary RTK reference station ARP                                               |
| RTCM 1074    | GPS MSM4                                                                           |
| RTCM 1077    | GPS MSM7                                                                           |
| RTCM 1084    | GLONASS MSM4                                                                       |
| RTCM 1087    | GLONASS MSM7                                                                       |
| RTCM 1094    | Galileo MSM4                                                                       |
| RTCM 1097    | Galileo MSM7                                                                       |
| RTCM 1124    | BeiDou MSM4                                                                        |
| RTCM 1127    | BeiDou MSM7                                                                        |
| RTCM 1230    | GLONASS code-phase biases                                                          |
| RTCM 4072.0  | Reference station PVT (u-blox proprietary RTCM Message)                            |
|              | Unsupported in firmware version HPG L1L5 1.40.                                     |
| RTCM 4072.1  | Additional reference station information (u-blox proprietary RTCM Message)         |
|              | Only valid with firmware version HPG 1.12 and necessary for moving base operation. |

**Table 7: ZED-F9P supported output RTCM version 3.4 messages**

#### <span id="page-17-0"></span>**3.1.5.4 Rover operation**

In its default configuration, the ZED-F9P will attempt to provide the best positioning accuracy depending on the received correction data. It will enter RTK float mode shortly after it starts receiving an input stream of RTCM correction messages. Once the rover has resolved the carrier phase ambiguities, it will enter RTK fixed mode. When in this mode, the relative position accuracy between base and rover can be expected to be correct to the cm-level. The time period between RTK float and RTK fixed operation is referred to as the convergence time. Note that the convergence time is affected by the baseline length as well as by multipath and satellite visibility at both rover and base station.

The ZED-F9P should receive RTCM corrections matching its GNSS signal configuration to function optimally. The rover requires both base station observation (MSM4 or MSM7 messages) and position message (RTCM 1005 or RTCM 1006) in order to attempt ambiguity fixes. The rover will attempt to provide RTK fixed operation when sufficient number of ambiguities are resolved. If phase lock on sufficient number of signals cannot be maintained, the rover will drop back to RTK float mode. The rover will continue to attempt to resolve carrier ambiguities and revert to RTK fixed mode once the minimum number of signals has been restored.

The RTK mode that an RTK rover operates in can be configured through the CFG-NAVHPG-DGNSSMODE configuration item. The following two RTK modes are available:

• RTK fixed: The rover will attempt to fix ambiguities whenever possible.



• RTK float: The rover will estimate the ambiguities as float but will make no attempts at fixing them.

The rover will stop using RTCM corrections that are older than 60s (default value) and will drop back to a 3D or 3D/DGNSS mode. This is meant to prevent the computation of grossly misleading differential solutions. If desired, this value can be changed through the CFG-NAVSPG-CONSTR\_DGNSSTO configuration item.

The received correction messages stream should comply with the following:

- The reference station ID in the reference station message (RTCM 1005 or RTCM 1006) must match that used in the MSM observation messages. Otherwise, the rover cannot compute its position.
- In order to fix GLONASS ambiguities the correction stream must contain RTCM message 1230 or 1033. Otherwise, the carrier ambiguities will be estimated as float even when set to operate in RTK fixed mode. This will result in degraded performance, especially in challenging environments.

CFG-RTCM-DF003\_IN [7](#page-18-0) can be used to configure the desired reference station ID and CFG-RTCM-

DF003\_IN\_FILTER [7](#page-18-0) can be used to configure how strict the filtering should be (RELAXED is the recommended setting).

#### **3.1.5.4.1 Conservative ambiguity fix mode**

The conservative ambiguity fix mode offers a tradeoff for longer time to first fix or more float solutions in exchange for near absolute certainty when RTK is achieved. This mode is useful in challenging environment, for instance surveying in urban environment, or when an extra degree of certainty during ambiguity resolution is required.

To configure the conservative ambiguity fix mode, set the value of **CFG-NAVHPG-DGNSSMODE** to **RTK\_CAR**.

This feature is available as of firmware version HPG 1.50.

#### **3.1.5.4.2 Message output in RTK mode**

When operating in RTK rover mode users should take note of the modified information within the following NMEA and UBX messages:

- NMEA-GGA: The quality field will be 4 for RTK fixed and 5 for RTK float (see NMEA position fix flags in interface description). The age of differential corrections and base station ID will be set.
- NMEA-GLL, NMEA-VTG: The posMode indicator will be D for RTK float and RTK fixed (see NMEA position fix flags in interface description).
- NMEA-RMC, NMEA-GNS: The posMode indicator will be F for RTK float and R for RTK fixed (see NMEA position fix flags in interface description).
- UBX-NAV-PVT: The carrSoln flag will be set to 1 for RTK float and 2 for RTK fixed. The age of differential corrections will be reported. [8](#page-18-1)
- UBX-NAV-RELPOSNED
  - The diffSoln and relPosValid flags will be set
  - The carrSoln flag will be set to 1 for RTK float and 2 for RTK fixed
- UBX-NAV-SAT
  - The diffCorr flag will be set for satellites with valid RTCM data
  - The rtcmCorrUsed, prCorrUsed, and crCorrUsed flags will be set for satellites for which the RTCM corrections have been applied

<span id="page-18-0"></span><sup>7</sup> CFG-RTCM-DF003\_\* items are supported from firmware version HPG 1.13 onwards

<span id="page-18-1"></span><sup>8</sup> Age of differential corrections reported from firmware version HPG 1.30 onwards



- UBX-NAV-SIG
  - For signals to which the RTCM corrections have been applied, the correction source will be set to RTCM3 OSR and the crUsed, prCorrUsed, and crCorrUsed flags will be set
- UBX-NAV-STATUS
  - The diffSoln flag and the diffCorr flag will be set
  - The carrSoln flag will be set to 1 for RTK float and 2 for RTK fixed
- If the baseline exceeds 100 km [9](#page-19-0) , a UBX-INF-WARNING will be output, e.g. "WARNING: DGNSS long baseline: 102.7 km"

An illustrated procedure for configuring a rover using u-center is shown in the [Appendix](#page-118-0) C.2.

#### **3.1.5.5 Stationary base operation**

The ZED-F9P high precision receiver default operation begins without producing any RTCM messages. RTCM observation messages will be streamed as soon as they are configured for output. However, any stationary reference positionmessages are output onlywhen the base station position has been initialized and is operating in time mode. Time mode sets the receiver to operate as a stationary base station in fixed position and only time is estimated.

The following procedures can be used to initialize the base station position:

- Use the built-in survey-in procedure to estimate the position.
- Enter coordinates independently generated or taken from an accurate position such as a survey marker.
- Use in rover mode while feeding the receiver corrections and then enter the resulting estimated position coordinates as above.

#### **3.1.5.5.1 Survey-in**

Survey-in is a procedure that is carried out prior to entering time mode. It estimates the receiver position by building a weighted mean of all valid 3D position solutions.

Two major parameters are required when configuring:

- A **minimum observation time** defines the minimum observation time independent of the actual number of fixes used for the position estimate. Values can range from one day for high accuracy requirements to a few minutes for coarse position determination.
- A **3D position standard deviation** defines a limit on the spread of positions that contribute to the calculated mean.

Survey-in ends when both requirements are successfully met. The receiver begins operation in time mode and can output a base position message if configured. The survey-in status can be queried using the UBX-NAV-SVIN message.

The base station receiver should not be fed RTCM corrections while it is in survey-in mode. If a corrected position is desired, the base station coordinates should be pre-surveyed using RTCM corrections; the resultant position can be used to set the base station in fixed mode.

To configure a base station into survey-in mode (CFG-TMODE-MODE=SURVEY\_IN), the following items are required:

| Configuration item       | Description                                  |
|--------------------------|----------------------------------------------|
| CFG-TMODE-MODE           | Receiver mode (disabled, survey-in or fixed) |
| CFG-TMODE-SVIN_MIN_DUR   | Survey-in minimum duration                   |
| CFG-TMODE-SVIN_ACC_LIMIT | Survey-in position accuracy limit            |

#### **Table 8: Configuration items used for setting a base station into survey-in mode**

<span id="page-19-0"></span><sup>9</sup> With firmware version HPG 1.12 the maximum baseline is 50 km, e.g. "WARNING: DGNSS long baseline: 52.7 km"



#### **3.1.5.5.2 Fixed position**

An alternative to the survey-in procedure is to manually enter the receiver's coordinates. Any error in the base station position will directly translate into rover position errors. The base station position accuracy should therefore match or exceed the desired rover absolute position accuracy.

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
|                         |                                                                        |

**Table 9: Configuration items used for setting a base station into fixed mode**

Once the receiver is set in fixed mode, select the position format to use: either LLH or ECEF with optional high precision (mm) coordinates compared to the standard cm value.

For example, with CFG-TMODE-POS\_TYPE=ECEF the base antenna position can be entered to cm precision using CFG-TMODE-ECEF\_X, CFG-TMODE-ECEF\_Y, CFGTMODE-ECEF\_Z. For high precision (mm) coordinates use CFG-TMODEECEF\_X\_HP, CFG-TMODE-ECEF\_Y\_HP, CFG-TMODE-ECEF\_Z\_HP. The same applies with corresponding coordinates used with CFG-TMODE-POS\_TYPE=LLH.

The "3D accuracy" estimate in "Fixed Position" and the "Position accuracy limit" in "Survey-in" will affect the rover absolute position accuracy. Note that the availability of the position accuracy does not mitigate the error in the rover position, but only accounts for it when calculating the resulting positioning accuracy.

- In stationary base station mode a current position check is made with respect to the fixed coordinates. If the result indicates the fixed position coordinates are incorrect, a UBX-INF-WARNING message "Base station position seems incorrect" is issued. The message is output when the coordinates are incorrect by more than ~50 m up to 25 km.
- If the base station is moved during operation then new position coordinates must be configured.

An illustrated procedure for configuring a base receiver using u-center is shown in the [Appendix](#page-114-1) C.1.

#### **3.1.5.5.3 Base station: RTCM output configuration**

The desired RTCM messages must be selected and configured for the corresponding GNSS constellations received. The recommended list of RTCM output messages for a base operating in default GNSS configuration are:

• RTCM 1005 Stationary RTK reference station ARP



- RTCM 1074 GPS MSM4
- RTCM 1084 GLONASS MSM4
- RTCM 1094 Galileo MSM4
- RTCM 1124 BeiDou MSM4
- RTCM 1230 GLONASS code-phase biases

The configuration messages for these are shown in the [Table](#page-21-0) 10.

The following configuration items output the recommended messages for a default satellite constellation setting. Note that these are given for the UART1 interface:

<span id="page-21-0"></span>

| Configuration item     | Description                                                             |
|------------------------|-------------------------------------------------------------------------|
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1005 message on port UART1: RTCM base    |
| RTCM_3X_TYPE1005_UART1 | station message                                                         |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1074 message on port UART1: RTCM GPS     |
| RTCM_3X_TYPE1074_UART1 | MSM4 message                                                            |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1084 message on port UART1: RTCM GLONASS |
| RTCM_3X_TYPE1084_UART1 | MSM4 message                                                            |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1094 message on port UART1: RTCM Galileo |
| RTCM_3X_TYPE1094_UART1 | MSM4 message                                                            |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1124 message on port UART1: RTCM BeiDou  |
| RTCM_3X_TYPE1124_UART1 | MSM4 message                                                            |
| CFG-MSGOUT             | Output rate of the RTCM-3X-TYPE1230 message on port UART1: RTCM GLONASS |
| RTCM_3X_TYPE1230_UART1 | bias message                                                            |

**Table 10: Configuration items used for typical RTCM output configuration on UART1**

CFG-RTCM-DF003\_OUT [10](#page-21-1) can be used to configure the reference station ID that will be reported in all RTCM messages containing the RTCM DF003 data field.

The configuration of the RTCM 3.3 correction stream must be made with the following guidance:

- All observation messages must be broadcast at the same rate.
- The RTCM 3.3 correction stream must contain the GLONASS code-phase biases message (RTCM 1230) or the Receiver Antenna Description message (RTCM 1033) otherwise the GLONASS ambiguities can only be estimated as float, even in RTK fixed mode.
- The static reference station message (RTCM 1005 or RTCM 1006) does not need to be broadcast at the same rate as the observation messages, however, a rover will not be able to compute its position until it has received a valid reference station message.
- The correction stream should only contain one type of observation messages per constellation. When using a multi-constellation configuration, all constellations should use the same type of observation messages. Mixing MSM4 and MSM7 messages will possibly lead to incorrect setting of the multiple message bit.
- If the receiver is configured to output RTCM messages on several ports, they must all have the same RTCM configuration, otherwise, the MSM multiple message bit might not be set properly.

#### **3.1.5.6 Base and rover configuration for moving base RTK operation**

Firmware version HPG L1L5 1.40 does not support the moving base feature.

The moving base (MB) mode differs from the standard RTK operation in that the base station is no longer stationary at a predetermined location. Both the reference station and rover receivers are allowed to move while computing an accurate vector between the receiver antennas. This mode enables the calculation of heading on dynamic or static platforms, plus provides a centimeter-level accurate 3D vector for use in dynamic positioning applications, e.g. a UAV "follow me" feature.

<span id="page-21-1"></span><sup>10</sup> CFG-RTCM-DF003\_\* items are supported from firmware version HPG 1.13 onwards



In the MB RTK mode, the base and rover receivers are referred to as MB base and MB rover respectively.

This section describes how to configure the ZED-F9P high precision receiver in a moving base setup.

#### **3.1.5.6.1 Base operation in moving base RTK mode**

In addition to the rules described in RTCM output configuration section above, the following moving base specific rules apply:

- The RTCM 3.3 stream must contain reference station message 4072.0 (position information) and MSM4[11](#page-22-0) or MSM7 observation messages, otherwise the rover will be unable to operate in MB rover mode.
- Message 4072.1 [12](#page-22-1) (timing information) is no longer necessary for moving base rover and as such it is no longer used by a moving base rover. To reduce the bandwidth requirements between a moving base rover and a moving base, it is recommended to disable RTCM 4072.1 output on the base.
- Message 4072.0 must be sent for each epoch the MB base observations are sent.
- To ensure that the moving base processing works, the MB base and rover must use the same navigation update rate and measurement rate.

The desired RTCM messages must be selected and configured for the corresponding GNSS constellations received. The recommended list of RTCM output messages for a base operating in MB configuration are:

- RTCM 4072.0 Reference station PVT information
- RTCM 1074 GPS MSM4
- RTCM 1084 GLONASS MSM4
- RTCM 1094 Galileo MSM4
- RTCM 1124 BeiDou MSM4
- RTCM 1230 GLONASS code-phase biases
- With firmware version HPG 1.12, only MSM7 messages are supported and message 4072.1 is needed.

Additionally, while an MB receiver operates as a base, it is able to simultaneously:

- Apply RTCM 3.3 corrections and reach RTK fixed mode.
- Generate an MB correction stream for accompanying MB rover(s).

#### **3.1.5.6.2 Rover operation in moving base RTK mode**

While the MB RTK solution aims at estimating the relative position with centimeter-level accuracy, the absolute position of each receiver is expected to be known with a standard GNSS accuracy of a few meters, unless the base is receiving RTCM 3.3 corrections.

In addition to the rules described in the rover operation section, the following moving base specific rules apply:

- A moving base receiver typically experiences worse GNSS tracking than a static base receiver in an open-sky environment and therefore the MB RTK performance may be degraded.
- The MB rover will wait as long as possible to compute a navigation solution, possibly lowering the navigation rate all the way to 1 Hz while doing so. If no time-matched observations are received in time, the receiver will flag the relative position as invalid.

<span id="page-22-0"></span><sup>11</sup> MSM4 messages in moving base mode are supported from firmware version HPG 1.13 onwards

<span id="page-22-1"></span><sup>12</sup> Message 4072.1 is no longer necessary from firmware version HPG 1.13 onwards



- The achievable navigation update rate of the MB RTK solution is limited by the communication link latency. Latency here refers to the delay we have in getting the RTCM messages on the rover from the time they are sent from the base station.
- It is a good practice to try and minimize the latency in the communication link, especially if trying to achieve high navigation update rate. As a rule of thumb, the communication link latency should be less than the desired navigation update period minus 50 ms.
- If the communication link latency is too high to achieve the configured navigation update rate the receiver will lower the navigation update rate until it reaches 1 Hz.
- If the communication link latency is too high for 1 Hz rover operation, the receiver will declare the relative position as invalid.
- To ensure that the moving base processing works, the MB base and rover must use the same navigation update rate and measurement rate.

In addition to the modified output described in the rover operation section, the following moving base output message modifications will be observed:

#### **UBX-NAV-RELPOSNED:**

- The isMoving flag will be set
- The relPosValid flag will be set if the rover managed to get the time-matched observations in time and process the moving base solution
- The length of the relative position vector and its accuracy will be output
- The heading for the relative position vector and its accuracy will be output
- The relPosHeadingValid flag will be set, unless the length of the relative position vector and/or its accuracy are not sufficient to reliably derive the heading information
- With firmware version HPG 1.12, the time-matched observations must be received within 700 ms. When the limit is exceeded, the MB reference observations and/or position will be extrapolated for up to 3 s before falling back to standard GNSS operation. The refPosMiss and refObsMiss flags will be set for epochs during which the extrapolated base position or observations have been used. These flags are no longer supported from firmware version HPG 1.13 onwards.

### <span id="page-23-0"></span>**3.1.6 PPP-RTK configuration**

Supported from firmware version HPG 1.30 onwards

#### **3.1.6.1 SPARTN corrections**

When operating as a rover, the ZED-F9P can receive SPARTN corrections:

- via the internet from a service provider
- via a host application that receives L-band satellite data (u-blox NEO-D9S may be used for this). For more information, see section Multiple [SPARTN](#page-24-0) sources.

If you choose PointPerfect service, contact your local u-blox technical support

#### **3.1.6.1.1 SPARTN protocol**

SPARTN is a binary protocol for the communication of SSR correction information.

ZED-F9P supports SPARTN as specified by SPARTN Interface Control Document – Version 2.0.1 (September, 2021).

To modify the SPARTN input/output settings, see the configuration section in the applicable Interface description [\[2\]](#page-126-1).



<span id="page-24-1"></span>

| Message type-subtype | Description                                           |
|----------------------|-------------------------------------------------------|
| SM 0-0               | GPS orbit, clock, bias (OCB)                          |
| SM 0-1               | GLONASS orbit, clock, bias (OCB)                      |
| SM 0-2               | Galileo orbit, clock, bias (OCB)                      |
| SM 0-3               | BeiDou orbit, clock, bias (OCB)                       |
|                      | Supported from firmware version HPG L1L5 1.40 onwards |
| SM 1-0               | GPS high-precision atmosphere correction (HPAC)       |
| SM 1-1               | GLONASS high-precision atmosphere correction (HPAC)   |
| SM 1-2               | Galileo high-precision atmosphere correction (HPAC)   |
| SM 1-3               | BeiDou high-precision atmosphere correction (HPAC)    |
|                      | Supported from firmware version HPG L1L5 1.40 onwards |
| SM 2-0               | Geographic area definition (GAD)                      |

#### **3.1.6.1.2 List of supported SPARTN 2.0.1 input messages**

#### **Table 11: ZED-F9P supported input SPARTN version 2.0.1 messages**

The SPARTN protocol version 2.0.1 is supported as of firmware version HPG 1.30, where:

- Only the messages in [Table](#page-24-1) 11 are supported. The implementation recognizes unsupported correction messages but they are not applied for the RTK solution such as QZSS correction messages, for instance.
- Group and embedded authentication messages are not supported.
- SM1 messages must contain tropospheric model for the receiver to reach an RTK fixed solution.

Application designs using ZED-F9P and SPARTN correction streams should provide firmware upgrade capability; upcoming firmware versions will implement further SPARTN messages and functionalities.

Some SPARTN correction service providers broadcast different sets of messages in different regions and support different signals or satellites. These variations may affect the accuracy of the ZED-F9P.

#### <span id="page-24-0"></span>**3.1.6.2 Multiple SPARTN sources**

ZED-F9P supports multipleSPARTN correction stream sources. It can support aSPARTN correction stream received over the internet (SPARTN message formatted IP stream) or over L-band satellites (SPARTN L-band stream formatted as UBX-RXM-PMP messages).

Only one source can be configured to be used at a time by ZED-F9P. The configuration item CFG-SPARTN-USE\_SOURCE can be configured to select which source will be used. Alternatively, the input protocol configuration items of a physical port can be configured to block input support for the UBX or the SPARTN protocols on the desired ports, for example CFG-UART1INPROT-UBX, CFG-USBINPROT-SPARTN, etc.

| Source                  | Description                                                                                                                                                                                                                                                           | CFG-SPARTN<br>USE_SOURCE |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| SPARTN IP stream        | This refers to corrections received in a SPARTN message format by any<br>interface of the ZED-F9P. The SPARTN corrections must follow the<br>SPARTN protocol specification and the source can be any SPARTN service<br>provider.                                      | IP (default)             |
| SPARTN L-band<br>stream | This refers to corrections received in a UBX-RXM-PMP message format by<br>any interface of the ZED-F9P. UBX-RXM-PMP messages are provided by u<br>blox L-band NEO-D9S receivers and contain frames of SPARTN messages<br>following the SPARTN protocol specification. | LBAND                    |

#### **Table 12: ZED-F9P supported SPARTN correction stream sources**



- In case a host application receives a SPARTN L-band stream through other means and converts UBX-RXM-PMP messages to SPARTN messages, then ZED-F9P treats these corrections as a SPARTN IP stream
- When providing a SPARTN L-band stream formatted as UBX-RXM-PMP messages, it is recommended to enable both UBX and SPARTN input protocol support on the port where the UBX-RXM-PMP is received. For example, as the default configuration on UART2, where CFG-UART2INPROT-UBX = 1 (true) and CFG-UART2INPROT-SPARTN = 1 (true).

The host application is responsible for deciding which stream to use. This can be based, for example, on the current IP or L-band reception conditions, the needs of the host application, power/cost considerations etc. The ZED-F9P does not provide any intelligent or automatic stream selection.

ZED-F9P provides additional monitoring information in the form of UBX-RXM-COR messages to help identify what is the current stream status in order to assist the host application in deciding which stream to use. UBX-RXM-COR reports, among other information:

- What is the type/subtype of the received SPARTN messages.
- Which is the source of the received SPARTN message (IP or L-band) and if it is used by ZED-F9P.
- What is the signal status in case of L-band streams.

Additionally some SPARTN input status information is also available in other UBX messages, such as UBX-MON-COMMS. For the full message specification, see ZED-F9P Interface description [[2](#page-126-1)].

If the selected SPARTN source contains encrypted SPARTN corrections, then extra monitoring information are reported through UBX-RXM-COR, such as if the message is encrypted and if it got decrypted.

#### **3.1.6.3 Encrypted SPARTN support**

SPARTN messages may be encrypted as indicated by SPARTN field TF004 (Encryption and authentication flag). ZED-F9P supports both encrypted and unencrypted SPARTN messages. Unencrypted SPARTN messages can be utilized as is by ZED-F9P without any special setup. Encrypted SPARTN messages can be decrypted and utilized by ZED-F9P once the appropriate dynamic keys are set and managed by the host application.

- The rest of this section describes the steps needed to enable encrypted SPARTN support for the u-blox PointPerfect service only
- Different dynamic keys apply for IP-only stream or IP+L-band stream. The type of service available to a user is specified by u-blox Terms and Services.

| Step                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example/notes                                                                                                                                                                                 |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Obtain PointPerfect<br>dynamic key                                      | Request by any means available a PointPerfect dynamic<br>key lease. It should come in a json structure containing<br>two dynamic keys; the current key and the next key. The<br>request can be postponed if the host application already<br>holds such a json structure obtained earlier and the<br>current time falls within the current key validity time.                                                                                                                                                       | current:<br>•<br>Key: current key in byte array format<br>•<br>Expires: current key expiring date<br>next:<br>•<br>Key: next key in byte array format<br>•<br>Expires: next key expiring date |
| Check if current<br>and next dynamic<br>keys are currently<br>available | At every power cycle of ZED-F9P or whenever the<br>host application needs to decrypt encrypted SPARTN<br>messages for the first time, poll UBX-RXM-SPARTNKEY<br>to see what are the current and next keys saved in the<br>ZED-F9P. If no key is saved or both keys have expired,<br>then no keys are reported. If one key is available and/or<br>one key has expired, then only one current key is reported.<br>If two keys are available and no key has expired, then both<br>current and next keys are reported. | See description of UBX-RXM-SPARTNKEY<br>message in the applicable interface<br>description [2].                                                                                               |



| Step                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Example/notes                                                                                                                                                                                                                                                                              |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set current and<br>next dynamic keys      | Convert the json structure into a UBX-RXM-SPARTNKEY<br>to set the current and next dynamic keys. This process<br>should be repeated at every power cycle of ZED-F9P,<br>or whenever the host application needs to decrypt<br>encrypted SPARTN messages for the first time, or when<br>the dynamic keys are close to expiring (e.g. only one key is<br>available and is close to expire), or when no dynamic keys<br>are saved.                                                              | This will load the current and next dynamic<br>keys in this sequence. See the description<br>of UBX-RXM-SPARTNKEY in the applicable<br>interface description [2]. Although setting<br>the current key only is sufficient, it is<br>recommended that both current and next<br>keys are set. |
| Forward or<br>relay SPARTN<br>corrections | The host application and design should be such that<br>SPARTN corrections arrive to the ZED-F9P interfaces,<br>either as SPARTN format messages (over an IP stream)<br>and/or as UBX-RXM-PMP format messages (over an L<br>band stream). In case of multiple SPARTN sources only<br>the one selected by the configuration item CFG-SPARTN<br>USE_SOURCE will be attempted to be decrypted/used.<br>The other available SPARTN source will not be decrypted<br>and will be reported as such. |                                                                                                                                                                                                                                                                                            |
| Monitor decryption<br>status              | UBX-RXM-COR reports info on the stream selected, if it is<br>encrypted and if the decryption was performed. Further<br>key status information are reported by the UBX-RXM<br>SPARTNKEY message.                                                                                                                                                                                                                                                                                             | Decryption success cannot be verified in<br>SPARTN messages                                                                                                                                                                                                                                |
| Monitor key status                        | UBX-RXM-SPARTNKEY reports info on the current and<br>next key and if both, or one, or no keys are available.                                                                                                                                                                                                                                                                                                                                                                                | See description of UBX-RXM-SPARTNKEY<br>message in the applicable interface<br>description [2].                                                                                                                                                                                            |
| Key switching from<br>current to next     | The host application does not need to handle the key<br>switching form current to next, as long as both keys have<br>been saved in the ZED-F9P. Once a current key expires, it<br>gets removed and replaced by the next key (if available).<br>Then only the next key will be available and reported as<br>current. If no next key is available to become current,<br>then the decryption stops and the above steps need to be<br>repeated.                                                 |                                                                                                                                                                                                                                                                                            |

**Table 13: PointPerfect dynamic key handling**

#### **3.1.6.4 CLAS corrections**

QZSS CLAS (centimeter-level augmentation service) is the satellite-based Japan's nationwide open service providing centimeter positioning accuracy. Corrections are transmitted on the QZSS L6 signal and encoded with Compact SSR (cSSR) protocol. Currently, the CLAS service provides corrections for GPS, Galileo, and QZSS satellites in view.

ZED-F9P supports CLAS corrections directly provided from NEO-D9C output in the form of UBX-RXM-QZSSL6. ZED-F9P can be directly connected to a NEO-D9C or the host application can forward the UBX-RXM-QZSSL6 message from NEO-D9C to ZED-F9P with no parsing needed.

For more information see the NEO-D9C integration manual and applicable interface description.

#### **3.1.6.5 Rover operation**

The rover operation and configuration, when using SPARTN or CLAS corrections, is similar to the setup when using RTCM corrections (see RTCM rover [operation](#page-17-0)).

The float/fix carrier phase ambiguities resolution concept is maintained and, where relevant, the NMEA and UBX output contents are updated accordingly. Small adjustments are made where necessary, for example the correction source field in UBX messages will be set to SPARTN or CLAS (UBX-RXM-QZSSL6) instead of RTCM.

In order to verify that the rover is receiving and using SPARTN or CLAS corrections, the following messages can be observed:

• UBX-MON-COMMS message reports which data are received on which port



- UBX-NAV-SIG message reports which type of corrections is applied for each signal in the field "corrSource"
- UBX-RXM-COR message reports the received SPARTN or UBX-RXM-QZSSL6 messages and if they were used

For further details see the the applicable interface description [\[2\]](#page-126-1).

Users should be aware of the datum used by the correction source. The rover position will provide coordinates in the correction source reference frame. This may need to be taken into account when using the PPP-RTK rover position.

If the rover switches between different correction types (SPARTN, CLAS or RTCM) it is recommended to reset the receiver before using a new type of correction

### <span id="page-27-0"></span>**3.1.7 Legacy configuration interface compatibility**

Although there is some backwards compatibility for the legacy UBX-CFG configuration messages, users are strongly advised to adopt the configuration interface described in this document.

See Legacy UBX-CFG message fields reference section in the applicable Interface description [[2](#page-126-1)].

### <span id="page-27-1"></span>**3.1.8 Navigation configuration**

This section presents various configuration options related to the navigation engine. These options can be configured through various configuration groups, such as CFG-NAVSPG-\*, CFG-ODO-\*, and CFG-MOT-\*.

#### **3.1.8.1 Platform settings**

u-blox receivers support different dynamic platform models (see the table below) to adjust the navigation engine to the expected application environment. These platform settings can be changed dynamically without performing a power cycle or reset. The settings improve the receiver's interpretation of the measurements and thus provide a more accurate position output. Setting the receiver to an unsuitable platform model for the given application environment is likely to result in a loss of receiver performance and position accuracy.

The dynamic platform model can be configured through the CFG-NAVSPG-DYNMODEL configuration item. The supported dynamic platform models and their details can be seen in [Table](#page-27-2) [14](#page-27-2) and [Table](#page-28-0) 15 below.

<span id="page-27-2"></span>

| Platform           | Description                                                                                                                                        |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Portable (default) | Applications with low acceleration, e.g. portable devices. Suitable for most situations.                                                           |
| Stationary         | Used in timing applications (antenna must be stationary) or other stationary applications.<br>Velocity restricted to 0 m/s. Zero dynamics assumed. |
| Pedestrian         | Applications with low acceleration and speed, e.g. how a pedestrian would move. Low<br>acceleration assumed.                                       |
| Automotive         | Used for applications with equivalent dynamics to those of a passenger car. Low vertical<br>acceleration assumed.                                  |
| At sea             | Recommended for applications at sea, with zero vertical velocity. Zero vertical velocity assumed.<br>Sea level assumed.                            |
| Airborne <1g       | Used for applications with a higher dynamic range and greater vertical acceleration than a<br>passenger car. No 2D position fixes supported.       |
| Airborne <2g       | Recommended for typical airborne environments. No 2D position fixes supported.                                                                     |
| Airborne <4g       | Only recommended for extremely dynamic environments. No 2D position fixes supported.                                                               |
| Wrist              | Only recommended for wrist-worn applications. Receiver will filter out arm motion.                                                                 |

**Table 14: Dynamic platform models**



<span id="page-28-0"></span>

| Platform     | Max altitude [m] | Max horizontal<br>velocity [m/s] | Max vertical velocity<br>[m/s] | Sanity check type     | Max<br>position<br>deviation |
|--------------|------------------|----------------------------------|--------------------------------|-----------------------|------------------------------|
| Portable     | 12000            | 310                              | 50                             | Altitude and velocity | Medium                       |
| Stationary   | 9000             | 10                               | 6                              | Altitude and velocity | Small                        |
| Pedestrian   | 9000             | 30                               | 20                             | Altitude and velocity | Small                        |
| Automotive   | 6000             | 100                              | 15                             | Altitude and velocity | Medium                       |
| At sea       | 500              | 25                               | 5                              | Altitude and velocity | Medium                       |
| Airborne <1g | 80000            | 100                              | 6400                           | Altitude              | Large                        |
| Airborne <2g | 80000            | 250                              | 10000                          | Altitude              | Large                        |
| Airborne <4g | 80000            | 500                              | 20000                          | Altitude              | Large                        |
| Wrist        | 9000             | 30                               | 20                             | Altitude and velocity | Medium                       |
|              |                  |                                  |                                |                       |                              |

#### **Table 15: Dynamic platform model details**

Applying dynamic platform models designed for high acceleration systems (e.g. airborne <2g) can result in a higher standard deviation in the reported position.

If a sanity check against a limit of the dynamic platform model fails, then the position solution is invalidated. [Table](#page-28-0) 15 above shows the types of sanity checks which are applied for a particular dynamic platform model.

#### **3.1.8.2 Navigation input filters**

The navigation input filters in CFG-NAVSPG-\* configuration group provide the input data of the navigation engine.

These settings are primarily for the initial standard 2D/3D only GNSS fix indication when not in RTK float/fixed mode.

| Configuration item                                     | Description                                                                                                                                                                                                          |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFG-NAVSPG-FIXMODE                                     | By default, the receiver calculates a 3D position fix if possible but reverts to 2D<br>position if necessary (auto 2D/3D). The receiver can be forced to only calculate 2D<br>(2D only) or 3D (3D only) positions.   |
| CFG-NAVSPG-CONSTR_ALT, CFG<br>NAVSPG-CONSTR_ALTVAR     | The fixed altitude is used if fixMode is set to 2D only. A variance greater than zero<br>must also be supplied.                                                                                                      |
| CFG-NAVSPG-INFIL_MINELEV                               | Minimum elevation of a satellite above the horizon in order to be used in the<br>navigation solution. Low elevation satellites may provide degraded accuracy, due to<br>the long signal path through the atmosphere. |
| CFG-NAVSPG-INFIL_NCNOTHRS,<br>CFG-NAVSPG-INFIL_CNOTHRS | A navigation solution will only be attempted if there are at least the given number of<br>SVs with signals at least as strong as the given threshold.                                                                |

#### **Table 16: Navigation input filter parameters**

If the receiver only has three satellites for calculating a position, the navigation algorithm uses a constant altitude to compensate for the missing fourth satellite. When a satellite is lost after a successful 3D fix (min four satellites available), the altitude is kept constant at the last known value. This is called a 2D fix.

u-blox receivers do not calculate any navigation solution with less than three satellites.

#### <span id="page-28-1"></span>**3.1.8.3 Navigation output filters**

The result of a navigation solution is initially classified by the fix type (as detailed in the fixType field of UBX-NAV-PVT message). This distinguishes between failures to obtain a fix at all ("No Fix") and cases where a fix has been achieved, which are further subdivided into specific types of fixes (e.g. 2D, 3D, dead reckoning).



#### The ZED-F9P firmware does not support the dead reckoning position fix type.

Where a fix has been achieved, a check is made to determine whether the fix should be classified as valid or not. A fix is only valid if it passes the navigation output filters as defined in CFG-NAVSPG-OUTFIL. In particular, both PDOP and accuracy values must be below the respective limits.

Important: Users are recommended to check the gnssFixOK flag in the UBX-NAV-PVT or the NMEA valid flag. Fixes not marked valid should not be used.

UBX-NAV-STATUS message also reports whether a fix is valid in the gpsFixOK flag. This message has only been retained for backwards compatibility and users are recommended to use the UBX-NAV-PVT message.

The CFG-NAVSPG-OUTFIL\_TDOP and CFG-NAVSPG-OUTFIL\_TACC configuration items also define [TDOP](#page-113-1) and time accuracy values that are used in order to establish whether a fix is regarded as locked to GNSS or not, and as a consequence of this, which time pulse setting has to be used. Fixes that do not meet both criteria will be regarded as unlocked to GNSS, and the corresponding time pulse settings of CFG-TP-\* configuration group will be used to generate a time pulse.

When in RTK float/fixed mode there are no navigation output filter settings for this mode. This is handled internally in the RTK core.

#### **3.1.8.3.1 Speed (3D) low-pass filter**

The CFG-ODO-OUTLPVEL configuration item offers the possibility to activate a speed (3D)low-pass filter. The output of the speed low-pass filter is published in the UBX-NAV-VELNED message (speed field). The filtering level can be set via the CFG-ODO-VELLPGAIN configuration item with values between 0 (heavy low-pass filtering) and 255 (weak low-pass filtering).

The internal filter gain is computed as a function of speed. Therefore, the level as defined in the CFG-ODO-VELLPGAIN configuration item defines the nominal filtering level for speeds below 5 m/s.

#### **3.1.8.3.2 Course over ground low-pass filter**

The CFG-ODO-OUTLPCOG configuration item offers the possibility to activate a course over ground low-pass filter when the speed is below 8 m/s. The output of the course over ground (also named heading of motion 2D) low-pass filter is published in the UBX-NAV-PVT message (headMot field), UBX-NAV-VELNED message (heading field), NMEA-RMC message (cog field) and NMEA-VTG message (cogt field).The filtering level can be set via the CFG-ODO-COGLPGAIN configuration item with values between 0 (heavy low-pass filtering) and 255 (weak low-pass filtering).

The filtering level as defined in the CFG-ODO-COGLPGAIN configuration item defines the filter gain for speeds below 8 m/s. If the speed is higher than 8 m/s, no course over ground low-pass filtering is performed.

#### <span id="page-29-0"></span>**3.1.8.3.3 Low-speed course over ground filter**

The CFG-ODO-USE\_COG activates a low-speed course over ground filter and the CFG-ODO-COGMAXSPEED, CFG-ODO-COGMAXPOSACC configuration items offer the possibility to configure this feature (also named heading of motion 2D). This filter derives the course over ground from position at very low speed. The output of the low-speed course over ground filter is published in the UBX-NAV-PVT message (headMot field), UBX-NAV-VELNED message (heading field), NMEA-RMC message (cog field) and NMEA-VTG message (cogt field). If the low-speed course over ground filter is not configured, then the course over ground is computed as described in section [Freezing](#page-31-0) the course over [ground](#page-31-0).



### **3.1.8.4 Static hold**

Static hold mode allows the navigation algorithms to decrease the noise in the position output when the velocity is below a predefined "Static Hold Threshold". This reduces the position wander caused by environmental factors such as multi-path and improves position accuracy especially in stationary applications. By default, static hold mode is disabled.

If the speed drops below the defined "Static Hold Threshold", the static hold mode will be activated. Once static hold mode has been entered, the position output is kept static and the velocity is set to zero until there is evidence of movement again. Such evidence can be velocity, acceleration, changes of the valid flag (e.g. position accuracy estimate exceeding the position accuracy mask, see also section [Navigation](#page-28-1) output filters), position displacement, etc.

The CFG-MOT-GNSSDIST\_THRS configuration item additionally allows for configuration of distance threshold. If the estimated position is farther away from the static hold position than this threshold, static mode will be quit.The CFG-MOT-GNSSSPEED\_THRSconfiguration item allows you to set a speed that the static hold will release.



**Figure 6: Position publication in static hold mode**





**Figure 7: Flowchart of the static hold mode**

### <span id="page-31-0"></span>**3.1.8.5 Freezing the course over ground**

If the low-speed course over ground filter is deactivated or inactive (see section [Low-speed](#page-29-0) course over [ground](#page-29-0) filter), the receiver derives the course over ground from the GNSS velocity information. If the velocity cannot be calculated with sufficient accuracy (e.g., with bad signals) or if the absolute speed value is very low (under 0.1 m/s) then the course over ground value becomes inaccurate too. In this case the course over ground value is frozen, i.e. the previous value is kept and its accuracy is degraded over time. These frozen values will not be output in the NMEA messages NMEA-RMC and NMEA-VTG unless the NMEA protocol is explicitly configured to do so (see NMEA protocol configuration in the applicable Interface description [[2\]](#page-126-1)).





**Figure 8: Flowchart of the course over ground freezing**

# <span id="page-32-0"></span>**3.2 Primary and secondary output**

Supported from firmware version HPG 1.30 onwards

### <span id="page-32-1"></span>**3.2.1 Introduction**

u-blox GNSS receivers output various navigation results and data calculated as part of the navigation solution. These include results such as position, altitude, velocity, status flags, accuracy estimate figures, satellite/signal information and more.

The ZED-F9P can provide this output in two streams:

- **Primary output:** Reports the results of a full navigation solution using all capabilities of the ZED-F9P, such as, for example, high precision positioning.
- **Secondary output:** Reports the results of a GNSS standalone navigation solution.

Both the primary output and secondary output provide a similar set of information but the two outputs report different results.The primary output is reported in the form of UBX-NAV-\* messages, while the secondary output is reported in the form of UBX-NAV2-\* messages. Therefore, the UBX message class can be used to distinguish between the primary output and the secondary output. For the specification of the UBX-NAV2-\* messages and for a full list of available UBX-NAV2-\* messages, see the applicable Interface description [[2](#page-126-1)].

The secondary output is complementary to the primary output. It does not provide the full navigation solution of the primary output. It can be used to expand the applications of the ZED-F9P to enable using a second navigation solution in parallel with the primary navigation solution.



The rest of this section describes how to configure and use the secondary output, what is the expected output behavior, and provides examples that illustrate potential uses for the secondary output, while highlighting the differences between the primary and the secondary output.

### <span id="page-33-0"></span>**3.2.2 Configuration**

Configuring the secondary output to the application's needs requires:

- Enabling the secondary output
- Configuring the desired secondary output UBX-NAV2-\* messages
- Optionally, configuring the properties of the secondary output navigation solution

The configuration items relevant to the secondary output are in the CFG-NAV2-\* configuration group. The configuration items for enabling and configuring the output rate of the UBX-NAV2-\* messages are in the CFG-MSGOUT-\* group and are of the form CFG-MSGOUT-UBX\_NAV2\_\*. An example set of secondary output configuration items is shown in the table below. For all available configuration items, see the applicable Interface description [\[2\]](#page-126-1).

| Configuration item            | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| CFG-NAV2-OUT_ENABLED          | Enables secondary output                                         |
| CFG-NAV2-SBAS_USE_INTEGRITY   | Enables using SBAS integrity information in the secondary output |
| CFG-MSGOUT-UBX_NAV2_PVT_*     | Enables UBX-NAV2-PVT secondary output message                    |
| CFG-MSGOUT-UBX_NAV2_TIMEGPS_* | Enables UBX-NAV2-TIMEGPS secondary output message                |

**Table 17: Example secondary output configuration items**

**Enabling the secondary output:** The first necessary step to enable the secondary output is to configure the CFG-NAV2-OUT\_ENABLED configuration item appropriately. This will enable the secondary output navigation solution to run in parallel with the primary output navigation solution. By default, the secondary output is disabled. Note that if you do not follow the next step, there will be no secondary output visible in the ZED-F9P communication interfaces in the form of UBX-NAV2- \* messages.

- - Both primary and secondary output report a navigation solution computed at the same navigation rate. Enabling the secondary output may affect the maximum achievable navigation update rate due to the extra computational load.

**Configuring the desired secondary output UBX-NAV2-\* messages:** The second necessary step is to configure the desired CFG-MSGGOUT-UBX\_NAV2\_\* configuration items appropriately. These set the message output rates for the UBX-NAV2-\* messages that you wish to output. By default, all UBX-NAV2-\* message output rates are set to 0 and as such are not being output.

Due to the increased message output, the interface load will be higher while the secondary output messages are enabled. Therefore, the interface baud rate may need to be adapted accordingly. Alternatively, it is possible to configure the UBX-NAV2-\* messages with a different output rate from that of their primary output UBX-NAV-\* counterparts.

**Configuring the properties of the secondary output navigation solution:** Optionally, it is possible to configure the properties of the secondary output navigation solution in order to adapt it to the application's needs.

A minimal subset of the primary output navigation solution configuration is available for the secondary output navigation solution configuration. All such available configuration items are in the CFG-NAV2-\* configuration group (see applicable Interface description [\[2](#page-126-1)]).

Configuring any of the CFG-NAV2-\* configuration items changes the behavior of the secondary output navigation solution only and not the primary output one. All such configuration items have a



primary output configuration counterpart and have the same default value as their primary output configuration counterpart.

For example, the CFG-NAV2-SBAS\_USE\_INTEGRITY configuration item allows configuring the SBAS integrity feature differently for the primary output and the secondary output. Its primary output counterpart is the CFG-SBAS-USE\_INTEGRITY configuration item and the default value of both configuration items is the same.

### <span id="page-34-0"></span>**3.2.3 Expected output behavior**

Once the secondary output is enabled and the desired secondary output UBX-NAV2-\* messages are configured, the ZED-F9P will output both primary and secondary output data in the form of the enabled UBX-NAV-\* and UBX-NAV2-\* messages respectively.

In every navigation epoch, a set of UBX-NAV-\* messages will be output followed by another set of UBX-NAV2-\* messages. Both sets will be referring to the navigation solution of the same navigation epoch.

Each set will be delimited at its end with a UBX-NAV-EOE or a UBX-NAV2-EOE message respectively. In other words, a UBX-NAV-EOE message will be output at the end of the UBX-NAV-\* class enabled messages and a UBX-NAV2-EOE message will be output at the end of the UBX-NAV2-\* class enabled messages. For example, if only UBX-NAV-PVT, UBX-NAV2-PVT, UBX-NAV-TIMEGPSand UBX-NAV2- TIMEGPS are enabled on the same port with message output rate 1, then every navigation epoch output will be as follows: UBX-NAV-PVT, UBX-NAV-TIMEGPS, UBX-NAV-EOE, UBX-NAV2-PVT, UBX-NAV2-TIMEGPS, UBX-NAV2-EOE.

- Secondary output messages appear after the primary output messages. This results in a higher latency for the secondary output messages than the primary output messages.
- Contrary to UBX-NAV2-\* messages, secondary output NMEA-NAV2-\* messages are not delimited by an NMEA-equivalent to UBX-NAV-EOE.

The specification of the UBX-NAV2-\* messages resembles that of the UBX-NAV-\* messages. The payload specification of a UBX-NAV2 message is identical to the payload specification of its UBX-NAV counterpart, allowing to easily adapt any existing message parsers. The primary output will contain results and data reflecting the full navigation solution of the ZED-F9P. The secondary output will contain results and data reporting a GNSS standalone navigation solution.

### <span id="page-34-1"></span>**3.2.4 Example use cases**

As an example, an application using a ZED-F9P can compare the secondary output solution to be used as a sanity check against large errors in the RTK solution or errors originating from the correction data.

# <span id="page-34-2"></span>**3.3 SBAS**

Supported from firmware version HPG 1.13 onwards

The ZED-F9P is capable of receiving multiple SBAS signals concurrently, even from different SBAS systems (WAAS, EGNOS, MSAS, etc.). They can be tracked and used for navigation simultaneously. Every SBAS satellite that broadcasts ephemeris or almanac information can be used for navigation, just like a normal GNSS satellite.

For receiving correction data, the ZED-F9P automatically chooses the best SBAS satellite as its primary source. It will select only one since the information received from other SBAS satellites is redundant and could be inconsistent. The selection strategy is determined by the proximity of the



satellites, the services offered by the satellite, the configuration of the receiver (test mode allowed/ disallowed, integrity enabled/disabled) and the signal link quality to the satellite.

If corrections are available fromthe chosenSBASsatellite and used in the navigation calculation, the differential status will be indicated in several output messages such as UBX-NAV-PVT, UBX-NAV-STATUS, UBX-NAV-SAT, NMEA-GGA, NMEA-GLL, NMEA-RMC and NMEA-GNS (see the applicable Interface description [\[2\]](#page-126-1)). The message UBX-NAV-SBAS provides detailed information about which corrections are available and applied.

The most important SBAS feature for accuracy improvement is ionosphere correction. The measured data from regional Ranging and Integrity Monitoring Stations (RIMS) are combined to make a Total Electron Content (TEC) map. This map is transferred to the receiver via SBAS satellites to allow a correction of the ionosphere error on each received signal.

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
|              |                                    |         |

#### **Table 18: Supported SBAS messages**

Each satellite services a specific region and its correction signal is only useful within that region. Planning is crucial to determine the best possible configuration, especially in areas where signals from different SBAS systems can be received:

- **Example 1 - SBAS receiver in North America:** In the eastern parts of North America, make sure that EGNOS satellites do not take preference over WAAS satellites. The satellite signals from the EGNOS system should be disallowed by using the PRN mask.
- **Example 2 - SBAS receiver in Europe:** Some WAAS satellite signals can be received in the western parts of Europe, therefore it is recommended that the satellites from all but the EGNOS system should be disallowed using the PRN mask.
- Although u-blox receivers try to select the best available SBAS correction data, it is recommended to configure them to exclude unwanted SBAS satellites.

To configure the SBAS functionalities use the CFG-SBAS-\* configuration group.

| Parameter              | Description                                                                    |
|------------------------|--------------------------------------------------------------------------------|
| CFG-SIGNAL-SBAS_ENA    | Enabled/disabled status of the SBAS subsystem                                  |
| CFG-SBAS-USE_TESTMODE  | Allow/disallow SBAS usage from satellites in test mode                         |
| CFG-SBAS-USE_RANGING   | Use the SBAS satellites for navigation (ranging)                               |
| CFG-SBAS-USE_DIFFCORR  | Combined enable/disable switch for fast, long-term, and ionosphere corrections |
| CFG-SBAS-USE_INTEGRITY | Apply integrity information data                                               |



| Parameter                         | Description                                                         |
|-----------------------------------|---------------------------------------------------------------------|
| CFG-SBAS<br>ACCEPT_NOT_IN_PRNMASK | Use corrections from SBAS SV, even if not self-included in PRN MASK |
| CFG-SBAS-USE_IONOONLY             | Use SBAS ionosphere correction only                                 |
| CFG-SBAS-PRNSCANMASK              | Allows selectively enabling/disabling SBAS satellites               |

**Table 19: SBAS configuration parameters**

- When SBAS integrity data is applied, the navigation engine stops using all signals for which no integritydata are available (includingallnon-GPSsignals). It isnot recommendedto enableSBAS integrity on borders of SBAS service regions in order not to inadvertently restrict the number of available signals.
- SBAS integrity information is required for at least 5 GPS satellites. If this condition is not met, SBAS integrity data will not be applied.
- SBAS is only used if no correction service is available. If the connection stream is lost during the operation, the receiver will switch to using the SBAS corrections after the time set in CFG-NAVSPG-CONSTR\_DGNSSTO (60 s by default) has elapsed.
- When the receiver switches from a solution using correction data to a standard position solution, the reference frame of the output position will switch from the one of the correction data to that of the standard position solution. For an SBAS solution this reference frame will be aligned within a few cm of WGS84 (and modern ITRF realizations).

## <span id="page-36-0"></span>**3.4 QZSS SLAS**

Supported from firmware version HPG 1.13 onwards

QZSS SLAS (Sub-meter Level Augmentation Service) is an augmentation technology, which provides correction data for pseudoranges of GPS and QZSS satellites. The correction stream is transmitted on the L1S signal at the L1 frequency (1575.42 MHz).

For more information on QZSS SLAS, visit the website [qzss.go.jp/en/.](http://qzss.go.jp/en/)

QZSS SLAS is only used if no other correction services are available (e.g. RTCM, SPARTN, CLAS). If the connection stream is lost during the operation, the receiver will switch to use the SLAS corrections after the time set in CFG-NAVSPG-CONSTR\_DGNSSTO (60 s by default) has elapsed.

### <span id="page-36-1"></span>**3.4.1 Features**

Multiple QZSS SLAS signals can be received simultaneously.

When receiving QZSS SLAS correction data, the ZED-F9P high precision receiver will autonomously select the best QZSS satellite. The selection strategy is determined by the quality of the QZSS L1S signals, the receiver configuration (test mode allowed or not), and the location of the receiver with respect to the QZSS SLAS coverage area. When outside of this coverage area, the receiver will likely fall back to using SBAS corrections.

If QZSS SLAS corrections are used in the navigation solution, the differential status will be indicated in several output messages such as UBX-NAV-PVT, UBX-NAV-STATUS, UBX-NAV-SAT, NMEA-GGA, NMEA-GLL, NMEA-RMC and NMEA-GNS (see the applicable interface description [[2](#page-126-1)]). The message UBX-NAV-SLAS provides detailed information about which corrections are available and applied.

<sup>13</sup> Supported only for TIM 2.24.



| Message type | Message content                |
|--------------|--------------------------------|
| 0            | Test mode                      |
| 47           | Monitoring station information |
| 48           | PRN mask                       |
| 49           | Data issue number              |
| 50           | DGPS correction                |
| 51           | Satellite health               |

**Table 20: Supported QZSS L1S SLAS messages for navigation enhancing**

### <span id="page-37-0"></span>**3.4.2 Configuration**

To enable support for the necessary QZSS L1S signal, use the CFG-SIGNAL-QZSS\_L1S\_ENA configuration item.To configure further QZSSSLASfunctionalities, use the CFG-QZSS-USE\_SLAS\* configuration items.

| Parameter<br>Description         |                                                                                                                                                                                                                                                                                                                                           |  |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| CFG-QZSS-USE_SLAS_DGNSS          | Apply QZSS SLAS corrections                                                                                                                                                                                                                                                                                                               |  |
| CFG-QZSS-USE_SLAS_TESTMODE       | Allow the correction provided by QZSS satellites that are in test mode                                                                                                                                                                                                                                                                    |  |
| CFG-QZSS<br>USE_SLAS_RAIM_UNCORR | If this configuration is set, the receiver will try to estimate the position by using only<br>corrected measurements; if all corrected measurements are not available, it will not<br>use any corrections. If this configuration is not set, the receiver will mix corrected<br>and uncorrected measurements for the navigation solution. |  |

**Table 21: QZSS SLAS configuration parameters**

If the RAIM option is set, other GNSS time systems than the QZSS time system cannot be observed by measurements.

## <span id="page-37-1"></span>**3.5 Geofencing**

### <span id="page-37-2"></span>**3.5.1 Introduction**



#### **Figure 9: Geofence**

The geofencing feature allows for the configuration of up to four circular areas (geofences) on the Earth's surface. The receiver will then evaluate for each of these areas whether the current position lies within the area or not and signal the state via UBX messaging and PIO toggling.

### <span id="page-37-3"></span>**3.5.2 Interface**

Geofencing can be configured using the CFG-GEOFENCE-\* configuration group. The geofence evaluation is active whenever there is at least one geofence configured.



The current state of each geofence plus the combined state is output in UBX-NAV-GEOFENCE with every navigation epoch.

### <span id="page-38-0"></span>**3.5.3 Geofence state evaluation**

With every navigation epoch the receiver will evaluate the current solution's position versus the configured geofences. There are three possible outcomes for each geofence:

- *Inside* The position is inside the geofence with the configured confidence level
- *Outside* The position lies outside of the geofence with the configured confidence level
- *Unknown* There is no valid position solution or the position uncertainty does not allow for unambiguous state evaluation

The position solution uncertainty (standard deviation) is multiplied with the configured confidence sigma level and taken into account when evaluating the geofence state (red circle in [Figure](#page-38-4) 10).

<span id="page-38-4"></span>

**Figure 10: Geofence states**

The combined state for all geofences is evaluated as the combination (Union) of all geofences:

- *Inside* The position lies inside of at least one geofence
- *Outside* The position lies outside of all geofences
- *Unknown* All remaining states

A pin is made available to indicate the status of the geofence. See the [GEOFENCE\\_STAT](#page-55-0) interface.

### <span id="page-38-1"></span>**3.5.4 Using a PIO for geofence state output**

This feature can be used, for example, for waking up a sleeping host when a defined geofence condition is reached. The receiver will toggle the assigned pin according to the combined geofence state. Due to hardware restrictions, the geofence unknown state is not configurable and is always represented as HIGH. If the receiver is in the software backup mode or in the reset state, the pin will go to HIGH accordingly. The meaning of the LOW state can be configured using the CFG-GEOFENCE-PINPOL configuration item.

The CFG-GEOFENCE-PIN configuration item refers to a PIO and not a physical device pin. The PIO number must be set so that it is mapped to the assigned geofence state device pin. The ZED-F9P is assigned PIO3 that is assigned to module pin 19.

# <span id="page-38-2"></span>**3.6 Logging**

### <span id="page-38-3"></span>**3.6.1 Introduction**

The logging feature allows position fixes and arbitrary byte strings from the host to be logged in the receiver's flash memory. Logging of position fixes happens independently of the host system, and can continue while the host is powered down.

The following table lists all the logging-related messages:

| Message        | Description                                         |  |
|----------------|-----------------------------------------------------|--|
| UBX-LOG-CREATE | Creates a log file and activates the logging system |  |



| Message                                              | Description                                                       |  |
|------------------------------------------------------|-------------------------------------------------------------------|--|
| UBX-LOG-ERASE                                        | Erases a log file and deactivates the logging subsystem           |  |
| UBX-LOG-INFO                                         | Provides information about the logging system                     |  |
| UBX-LOG-STRING                                       | Enables a host process to write a string of bytes to the log file |  |
| Table 22: Logging control and configuration messages |                                                                   |  |
| Message                                              | Description                                                       |  |
| UBX-LOG-RETRIEVE                                     | Starts the log retrieval process                                  |  |
| UBX-LOG-RETRIEVEPOS                                  | A position log entry returned by the receiver                     |  |
| UBX-LOG-RETRIEVEPOSEXTRA                             | Odometer position data                                            |  |
| UBX-LOG-RETRIEVESTRING                               | A byte string log entry returned by the receiver                  |  |
| UBX-LOG-FINDTIME                                     | Finds the index of the first entry (given time)                   |  |

**Table 23: Logging retrieval messages**

### <span id="page-39-0"></span>**3.6.2 Setting the logging system up**

An empty log can be created using the UBX-LOG-CREATE message and a log can be deleted with the UBX-LOG-ERASE message. The logging system will only run if a log is in existence, so most logging messages will be rejected with a UBX-ACK-NAK message if there is no log present. Only one log can be created at any one time so a UBX-ACK-NAK message will be returned if a log already exists. The message specifies themaximumsize of the log in bytes (with some preset values provided).Both the logging subsystem and the receiver file-store have implementation overheads, so the total space available for log entries will be somewhat smaller than the size specified.

UBX-LOG-CREATE also allows the log to be specified as a circular log. If the log is circular, a set of older log entries will be deleted when it fills up, and the space freed up is used for new log entries. By contrast, if a non-circular log becomes full then new entries which do not fit will be rejected. UBX-LOG-CREATE also causes the logging system to start up so that further logging messages can be processed. The logging system will start up automatically on power-up if there is a log in existence. The log will remain in the receiver until specifically erased using the UBX-LOG-ERASE message.

The CFG-LOGFILTER-\* configuration group controls whether logging of entries is currently enabled and selects position fix messages for logging.



**Figure 11: The top level active/inactive states of the logging subsystem**

### <span id="page-39-1"></span>**3.6.3 Information about the log**

The receiver can be polled for a UBX-LOG-INFO message which will give information about the log. This will include the maximum size that the log can grow to (which, due to overheads, will be smaller than that requested in UBX-LOG-CREATE) and the amount of log space currently occupied. It will also report the number of entries currently in the log together with the time and date of the newest and oldest messages that have a valid time stamp.



Log entries are compressed and have housekeeping information associated with them, so the actual space occupied by log messages may be difficult to predict.The minimum size for a position fix entry is 9 bytes and the maximum 24 bytes, the typical size is 10 or 11 bytes. If the odometer is enabled then this will use at least another three bytes per fix.

Each log also has a fixed overhead which is dependent on the log type. The approximate size of this overhead is shown in the following table.

| Log type     | Overhead    |
|--------------|-------------|
| circular     | Up to 40 kB |
| non-circular | Up to 8 kB  |

#### **Table 24: Log overhead size**

The number of entries that can be logged in any given flash size can be estimated as follows:

Approx. number of entries = (flash size available for logging - log overhead)/typical entry size

For example, if 1500 kB of flash is available for logging (after other flash usage such as the firmware image is taken into account) a non-circular log would be able to contain approximately 139000 entries: ((1500\*1024)- (8\*1024))/11 = 138891.

### <span id="page-40-0"></span>**3.6.4 Recording**

The CFG-LOGFILTER-RECORD\_ENA configuration item must be set to *true* to enable recording into the log. Nothing will be recorded if recording is disabled, otherwise positionfix and UBX-LOG\_STRING entries can be recorded.When recording is enabled an entry will also be created from each UBX-LOG-STRING message. These will be timestamped if the receiver has current knowledge of time.

The CFG-LOGFILTER-\* configuration group has several values which can be used to select position fix entries for logging. If CFG-LOGFILTER-APPLY\_ALL\_FILTERS is *false*, then all position fixes will be logged (subject to a maximum rate of 1 Hz). Otherwise, a position is logged if any of the or if all of MIN\_INTERVAL, TIME\_THRS, SPEED\_THRS or POSITION\_THRS thresholds are exceeded. If a threshold is set to zero it is ignored.

Position fixes are only recorded if a valid fix is obtained. Failed and invalid fixes are not recorded. Position fixes are compressed to reduce the amount of flash space used. In order to improve the compression, the fix values are rounded. This means that the values returned by the logging system may differ slightly from those that are gathered in real time.

The recorded data for a fix comprises:

- The time and date of the fix recorded to a precision of one second.
- Latitude and longitude to a precision of one millionth of a degree. Depending on position on Earth this is a precision in the order of 0.1 m.
- Altitude (height above mean sea level) to a precision of 0.1 m. Entries with an altitude lower than -470 m (lower than the lowest point on earth) or higher than 20,000 m may not be recorded in the log.
- Ground speed to a precision of 1 cm/s.
- The fix type (only successful fix types, since these are the only ones recorded).
- The number of satellites used in the fix is recorded, but there is a maximum count which can be recorded. If the actual count exceeds this maximum count then the maximum count will be recorded. If a log entry is retrieved with a satellite count equal to the maximum this means that value or more. The maximum count is 51.



- A horizontal accuracy estimate is recorded to give an indication of fix quality. This is an approximate compressed representation of the accuracy as determined by the fix process. Any accuracy less than 0.7 m will be recorded as 0.7 m and any value above 1 km will be recorded as 1 km. Within these limits, the recorded accuracy will always be greater than the fix accuracy number (by up to 40%).
- Heading to a precision of one degree.
- Odometer distance data (if odometer is enabled).



**Figure 12: The states of the active logging subsystem**

### <span id="page-41-0"></span>**3.6.5 Retrieval**

UBX-LOG-RETRIEVE starts the process which allows the receiver to output log entries. UBX-LOG-INFO may be helpful to a host system in order to understand the current log status before retrieval is started.

Once retrieval has started, one message will be output from the receiver for each log entry requested. Sending any logging message to the receiver during retrieval will cause the retrieval to stop before the message is processed.

To maximize the speed of transfer it is recommended that a high communications data rate is used and GNSS processing is stopped during the transfer (see UBX-CFG-RST).

UBX-LOG-RETRIEVE can specify a start entry index and entry count. The maximum number of entries that can be returned in response to a single UBX-LOG-RETRIEVE message is 256. If more entries than this are required the message will need to be sent multiple times with different startEntry indices. It might be useful to stop recording via CFG\_LOGFILTER-RECORD\_ENA while retrieving log entries from a circular log to avoid deletion of the requested entries between the request and transmission.

The receiver will send a UBX-LOG-RETRIEVEPOS message for each position fix log entry and a UBX-LOG-RETRIEVESTRING message for each string log entry. If the odometer was enabled at the time a position was logged, then a UBX-LOG-RETRIEVEPOSEXTRA will also be sent. Messages will be sent in the order inwhich theywere logged, so UBX-LOG-RETRIEVEPOSand UBX-LOG-RETRIEVESTRING messages may be interspersed in the message stream.



The UBX-LOG-FINDTIME message can be used to search a log for the index of the first entry less than or equal to the given time. This index can then be used with the UBX-LOG-RETRIEVE message to provide time-based retrieval of log entries.

### <span id="page-42-0"></span>**3.6.6 Command message acknowledgment**

Some log operations may take a long time to execute because of the time taken to write to flash memory. The time for some operations may be unpredictable since the number and timing of flash operations may vary. In order to allow host software to synchronize to these delays logging messages will always produce a response.This will be UBX-ACK-NAK in case of error, otherwise UBX-ACK-ACK unless there is some other defined response to the message.

It is possible to send a small number of logging commands without waiting for acknowledgment, since there is a command queue, but this risks confusion between the acknowledgments for the commands. Also a command queue overflow would result in commands being lost.

## <span id="page-42-1"></span>**3.7 Protection level**

Supported from firmware version HPG 1.30 onwards

### <span id="page-42-2"></span>**3.7.1 Introduction**

Critical applications need to know how much trust they can place in their GNSS receiver's output at any given moment. Computed by the GNSS receiver in real-time, the protection level (PL) quantifies the reliability of the position information, to allow systems to change their mode of operation to improve the efficiency and quality of the tasks being performed.

The GNSS receiver's protection level describes the maximum likely position error to a specified degree of confidence. For example, if a GNSS receiver determines its position with a 95% protection level of one meter, there is only a 5% chance that the reported position is more than one meter away from its true position. Like the accuracy estimate of the GNSS receiver, the protection level constantlyfluctuates, influenced by all the common error sources that affect GNSSsolutions. Unlike the accuracy estimate, the confidence level of the protection level is much higher and is validated against specific operating scenarios to ensure that the output bounds the true error.





**Figure 13: PL bounding true position error**

### <span id="page-43-0"></span>**3.7.2 Interface**

The protection level bounds the true position error with a target misleading information risk (TMIR), for example 5[%MI/epoch] (read: 5% probability of having an MI per epoch). The target misleading information risk describes the probability per epoch of having misleading information (MI), that is, the true position error is larger than the protection level and fails to bound the true position error (see [Figure](#page-43-1) 14).

<span id="page-43-1"></span>

#### **Figure 14: Misleading information**

The output of the protection level is published through the UBX-NAV-PL message.

- Protection level computing can be disabled through the CFG-NAVSPG-PL\_ENA configuration item. See the applicable interface description [\[2\]](#page-126-1) for availability of the configuration item.
- TMIR is specified in one dimension for PL. It is not specified as a horizontal 2D or 3D value.
- The protection level values (UBX-NAV-PL.plPos1/2/3) are confidence intervals around the reported position (for example, UBX-NAV-PVT or UBX-NAV-HPPOSLLH).
- The target misleading information risk is provided in exponential notation (UBX-NAV-PL.tmirCoeff and UBX-NAV-PL.tmirExp), for example UBX-NAV-PL.tmirCoeff=5 and UBX-NAV-PL.tmirExp=0 results in 5e0 (= 5).

The user may have a threshold defined for the largest acceptable position error for their application. This threshold is known as the Alert Limit. If the reported PL exceeds this threshold, the user shall



consider changing the mode of operation of the system or in the worst case declare the system unavailable. Examples of a change in the operating mode of the system could be stopping, reversing the direction of operation, slowing down or calculating a new acceptable error threshold appropriate to the mode of operation. This state is also known as the receiver being unavailable (see [Figure](#page-44-1) 15).

In case the PL is smaller than the alert limit, the receiver is said to be available (see [Figure](#page-44-1) 15).

<span id="page-44-1"></span>

#### **Figure 15: Positioning function**

True position error is generally unknown, unless a very accurate and reliable truth positioning system is reporting an estimate for the true position

When the GNSSenvironment deviates significantly from the normal mode of operation as compared to scenarios where the PL has been validated, a validity flag is set to false to indicate these conditions. These conditions tend to be binary in nature, such as jamming has been detected, or the minimum number of satellites is being observed. UBX-NAV-PL reports a PL validity flag (see UBX-NAV-PL.plPosValid), which indicates whether the PL is usable. This mechanism is not depicted in [Figure](#page-44-1) 15.

- The protection level performance depends on many external and internal factors.Some external factors such as the harsh GNSS environment, correction data, etc. may lead to degraded PL performance.
  - The protection level validity is not to be confused with misleading information and is independent of misleading information.

| PL validity values        | Description                                 |  |
|---------------------------|---------------------------------------------|--|
| UBX-NAV-PL.plPosValid = 1 | PL values are valid and can be used         |  |
| UBX-NAV-PL.plPosValid = 0 | PL values are invalid and shall not be used |  |
|                           |                                             |  |

**Table 25: Position PL validity**

### <span id="page-44-0"></span>**3.7.3 Expected behavior**

For each navigation epoch and for each coordinate axis, a PL value is provided. For example, if the coordinate frame reported is North/East/Down, then the UBX-NAV-PL contents can be interpreted as follows:

| PL values         | Description                 |  |
|-------------------|-----------------------------|--|
| UBX-NAV-PL.plPos1 | 1 stands for the north axis |  |
| UBX-NAV-PL.plPos2 | 2 stands for the east axis  |  |



| PL values         | Description                |
|-------------------|----------------------------|
| UBX-NAV-PL.plPos3 | 3 stands for the down axis |
|                   |                            |

**Table 26: Position PL values**

If the PL coordinate frame is set to invalid (UBX-NAV-PL.plPosFrame = 0), then the PL values shall not be used. If the PL validity flag is cleared (UBX-NAV-PL.plValid =0), the PL values shall not be used. Both must be checked.

Only if the PL is set to valid (UBX-NAV-PL.plPosValid), the PL values (UBX-NAV-PL.plPos1/2/3) can be used and are reliable with respect to the target misleading information risk.

### <span id="page-45-0"></span>**3.7.4 Example use cases**

The protection level is effective for the Robotic Lawn Mower (RLM) applications if the receiver's dynamic platform model is set to portable (default) mode.

**Robot navigation:** In robotic navigation, the protection level helps ensure that the device, for example an autonomous lawnmower, operates in the best possible way to carry out the task of mowing the lawn within a defined boundary. The boundary is typically defined by a learning phase where the user accompanies the mower and shows the device the boundaries of the area. During this learning phase, it is assumed that because of the known geometries of the lawn, any significant errors can be smoothed out by the user and corrected, and the mower's internal map has the correct area. The mower can be implemented with different modes of operation. Some examples are:

- Clear open sky mode where the position accuracy is very good and reliable
- Near-fence mode where obstructions do not cause any kind of damage to the environment or cause the mower to exit the predefined area
- Critical areas where it is better to be conservative than aggressive, such as the edge of the swimming pool or the neighbor's flower bed

When the mower is moving in the middle of the lawn, if the sky is clear and the PL is low, it can travel at the maximum speed and the minimum overlap from pass to pass and be the most efficient it can be. When it gets near a physical fence, even though the PL might be higher than in the middle of the lawn, the mower may reduce its speed and increase the amount of overlap to account for the increased uncertainty of its position over the route. When the mower gets near an extremely critical area, it may adopt a strategy of revisiting the same area on multiple occasions to get better measurements due to the changes in the satellite configurations in the sky. If the protection level value fails to compute, the device can stop and wait for environmental error sources, such as RF interference or adverse atmospheric conditions, to subside or go back until a valid protection level value is available.

**Drones and UAVs:** Drones and other unmanned aerial vehicles are typically used to survey photogrammetry, to help in applying a minimal amount of pesticides in agriculture, or to inspect assets such as pipelines or infrastructure. The protection level can be used to determine whether the job has been done completely with high enough accuracy before the team can leave the area. It is often much better to make a second pass of the area than to have to return to the site on another day.When applying pesticides, the routes planned can be adjusted to increase the amount of overlap if the confidence in the position accuracy is insufficient.



# <span id="page-46-0"></span>**3.8 Communication interfaces**

u-blox receivers are equipped with a communication interface [14](#page-46-1) which is multi-protocol capable. The interface ports can be used to transmit GNSS measurements, monitor status information and configure the receiver.

A protocol (e.g. UBX, NMEA) can be assigned to several ports simultaneously, each configured with individual settings (e.g. baud rate, message rates, etc.). More than one protocol (e.g. UBX protocol and NMEA) can be assigned to a single port (multi-protocol capability), which is particularly useful for debugging purposes.

The ZED-F9P provides UART1, UART2, SPI, I2C and USB interfaces for communication with a host CPU. The interfaces are configured via the configuration methods described in the applicable interface description [\[2\]](#page-126-1).

| Port no. | UBX-MON-COMMS portId | Electrical interface |
|----------|----------------------|----------------------|
| 0        | 0x0000               | I2C                  |
| 1        | 0x0100               | UART1                |
| -        | 0x0101               | Reserved             |
| -        | 0x0200               | Reserved             |
| 2        | 0x0201               | UART2                |
| 3        | 0x0300               | USB                  |
| 4        | 0x0400               | SPI                  |

The following table shows the port numbers reported in the UBX-MON-COMMS messages.

**Table 27: Port number assignment**

It is important to isolate interface pins when VCC is removed. They can be allowed to float or they can be connected to a high impedance.

Example isolation circuit is shown below.



**Figure 16: ZED-F9P output isolation**

<span id="page-46-1"></span><sup>14</sup> The signal names and related terms have been replaced with new terminology in this document.





**Figure 17: ZED-F9P input isolation**

### <span id="page-47-0"></span>**3.8.1 UART**

A Universal Asynchronous Receiver/Transmitter (UART) port consists of an RX and a TX line. Neither handshaking signals nor hardware flow control signals are available. The UART interface protocol and baud rate can be configured but there is no support for setting different baud rates for reception and transmission.

The ZED-F9P includes two UART serial ports. UART1 can be used as a host interface for configuration, monitoring and control. UART2 is available as an optional interface and cannot be used as a single host interface.

From firmware version 1.30 onwards it is possible to enable UBX protocol input/output support on UART2.

Do not use UART2 as the only one interface to the host. Not all UBX functionality is available on UART2, such as firmware upgrade, safeboot or backup modes functionalities. No startup boot screen is sent out from UART2.

The UART RX interface will be disabled when more than 100 frame errors are detected during a one-second period. This can happen if the wrong baud rate is used or the UART RX pin is grounded. An error message appears when the UART RX interface is re-enabled at the end of the one-second period.

| Baud rate | Data bits | Parity | Stop bits |
|-----------|-----------|--------|-----------|
| 9600      | 8         | none   | 1         |
| 19200     | 8         | none   | 1         |
| 38400     | 8         | none   | 1         |
| 57600     | 8         | none   | 1         |
| 115200    | 8         | none   | 1         |
| 230400    | 8         | none   | 1         |
| 460800    | 8         | none   | 1         |
| 921600    | 8         | none   | 1         |

**Table 28: Possible UART interface configurations**

- The default baud rate is 38400 baud. To prevent buffering problems it is recommended not to run at a lower baud rate than the default.
- The baud rate for safeboot mode is 9600 baud. See more information about safeboot mode in the [SAFEBOOT\\_N](#page-53-3) section.



Allow a short time delay of typically 100 ms between sending a baud rate change message and providing input data at the new rate. Otherwise some input characters may be ignored or the port could be disabled until the interface is able to process the new baud rate.

Note that for protocols such as NMEA or UBX, it does not make sense to change the default word length values (data bits) since these properties are defined by the protocol and not by the electrical interface.

If the amount of data configured is too much for a certain port's bandwidth (e.g. all UBX messages output on a UART port with a baud rate of 9600), the buffer will fill up. Once the buffer space is exceeded, new messages to be sent will be dropped. To prevent message loss, the baud rate and communication speed or the number of enabled messages should be carefully selected so that the expected number of bytes can be transmitted in less than one second.

### <span id="page-48-0"></span>**3.8.2 I2C interface**

An I2C interface is available for communication with an external host CPU or u-blox cellular modules in peripheral mode only. The I2C protocol and electrical interface supports the Fast-mode of the I2C industry standard with a maximum SCL clock frequency of 400 kHz. Backwards compatibility with Standard-mode I2C bus operation is not supported.

The SCL and SDA pins have internal pull-up resistors which should be sufficient for most applications. However, depending on the speed of the host and the load on the I2C lines additional external pull-up resistors may be necessary.

To use the I2C interface D\_SEL pin must be left open.

In designs where the host uses the same I2C bus to communicate with more than one u-blox receiver, the I2C peripheral address for each receiver must be configured to a different value. Typically most u-blox receivers are configured to the same default I2C peripheral address value. To poll or set the I2C peripheral address, use the CFG-I2C-ADDRESS configuration item (see the applicable interface description [[2](#page-126-1)]).

The CFG-I2C-ADDRESS configuration item is an 8-bit value that includes the I2C peripheral address in the 7 most significant bits and the read/write flag in the least significant bit.

#### **3.8.2.1 I2C register layout**

The I2C interface allows 256 registers to be addressed. As shown in [Figure](#page-49-0) 18, only three of these are currently implemented.

The data registers 0 to 252 at addresses 0x00 to 0xFC contain reserved information, the result from their reading is currently undefined. The data registers 0 to 252 are 1 byte wide.

At addresses 0xFD and 0xFE it is possible to read the currently available number of bytes.

The register at address 0xFF allows the data stream to be read. If there is no data awaiting transmission from the receiver, then this register delivers value 0xFF, which cannot be the first byte of a valid message. If the message data is ready for transmission, the successive reads of register 0xFF will deliver the waiting message data.

Do not use registers 0x00 to 0xFC. They are reserved for future use and they do not currently provide any meaningful data.



<span id="page-49-0"></span>



#### **3.8.2.2 Read access types**

There are two I2C read transfer forms:

- The "random access" form: includes a peripheral register address and allows any register to be read.
- The "current address" form: omits the register address.

[Figure](#page-50-0) 19 shows the format of the first one, the "random access" form of the request. Following the start condition from the controller, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the controller transmitter. The receiver answers with an acknowledge (logic low) to indicate that it recognizes the address.

Next, the 8-bit address of the register to be read must be written to the bus. Following the receiver's acknowledgment, the controller again triggers a start condition and writes the device address, but this time the RW bit is a logic high to initiate the read access. Now, the controller can read 1 to N bytes from the receiver, generating a not-acknowledge and a stop condition after the last byte being read.



<span id="page-50-0"></span>

#### **Figure 19: I2C random read access**

If the second form, "current address" is used, an address pointer in the receiver is used to determine which register to read. This address pointer will increment after each read unless it is already pointing at register 0xFF, the highest addressable register, in which case it remains unaltered.

The initial value of this address pointer at startup is 0xFF, so by default all current address reads will repeatedly read register 0xFF and receive the next byte of message data (or 0xFF if no message data is waiting).



**Figure 20: I2C current address read access**

#### **3.8.2.3 Write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. Therefore, the register set mentioned in the section Read [access](#page-51-1) is not writeable.

Following the start condition from the controller, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the controller transmitter. The receiver answers with an acknowledge (logic low) to indicate that it is responsible for the given address.

The controller can write 2 to N bytes to the receiver, generating a stop condition after the last byte being written. The number of data bytes must be at least 2 to properly distinguish from the write access to set the address counter in random read accesses.







### <span id="page-51-0"></span>**3.8.3 SPI interface**

ZED-F9P has an SPI peripheral interface that can be selected by setting D\_SEL = 0. The SPI peripheral interface is shared with UART1 and I2C port, the physical pins are same. The SPI pins available are:

- SPI\_SDO (TXD)
- SPI\_SDI (RXD)
- SPI\_CS\_N
- SPI\_CLK

See more information about communication interface selection from the [D\\_SEL](#page-53-1) section.

The SPI interface is designed to allow communication to a host CPU. The interface can be operated in peripheral mode only.

#### <span id="page-51-1"></span>**3.8.3.1 Read access**

As the register mode is not implemented for the SPI port, only the UBX/NMEA message stream is provided. This stream is accessed using the back-to-back read and write access (see section [Back](#page-51-2)[to-back](#page-51-2) read and write access below). When no data is available to be written to the receiver, SDI should be held logic high, i.e. all bytes written to the receiver are set to 0xFF.

To prevent the receiver from being busy parsing incoming data, the parsing process is stopped after 50subsequent bytes containing0xFF.The parsing process is re-enabled with thefirst byte not equal to 0xFF.

If the receiver has no more data to send, it sets SDO to logic high, i.e. all bytes transmitted decode to 0xFF. An efficient parser in the host will ignore all 0xFF bytes which are not part of a message and will resume data processing as soon as the first byte not equal to 0xFF is received.

#### <span id="page-51-2"></span>**3.8.3.2 Back-to-back read and write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. For every byte written to the receiver, a byte will simultaneously be read from the receiver. While the controller writes to SDI of the peripheral, at the same time it needs to read from SDO of the peripheral, as any pending data will be output by the receiver with this access. The data on SDO represents the results from a current address read, returning 0xFF when no more data is available.





**Figure 22: SPI back-to-back read/write access**

### <span id="page-52-0"></span>**3.8.4 USB interface**

A single USB port is provided for host communication purposes.

The USB 2.0 FS (Full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface.

If the receiver executes code from internal ROM (i.e. when a valid flash firmware image is not detected), the USB behavior can differ compared to executing a firmware image from flash memory. USB host compatibility testing is thus recommended in this scenario.

The ZED-F9P receiver supports only self-powered mode operation in which the receiver is supplied from its own power supply. The V\_USB pin is used to detect the availability of the USB port, i.e. whether the receiver is connected to a USB host.

- USB suspend mode is not supported.
- USB bus-powered mode is not supported.
- It is important to connect V\_USB to ground and leave data lines open when the USB interface is not used in an application.
- The voltage range for V\_USB is specified from 3.0 V to 3.6 V, which differs slightly from the specification for VCC.
- The boot screen is retransmitted on the USB port after enumeration. However, messages generated between receiver startup and USB enumeration are not visible on the USB port.

There are additional hardware requirements if USB is used:

- V\_USB (pin 38) requires 1 uF capacitor mounted adjacent to the pin to ensure correct V\_USB voltage detection
- The V\_USB (Pin 38) voltage should be sourced from an LDO enabled by the module VCC and supplied from the USB host.
- A pull-down resistor is required on the output of this V\_USB LDO
- Apply USB\_DM and USB\_DP series resistors; typically 27 Ω





**Figure 23: ZED-F9P example circuit for USB interface**

R11 = 100 k Ω is recommended

R4, R5 = 27 Ω is recommended

# <span id="page-53-0"></span>**3.9 Predefined PIOs**

In addition to the communication ports, there are some predefined PIOs provided by ZED-F9P to interact with the receiver. These PIOs are described in this section.

If hardware backup mode is used a proper isolation of the interfaces is needed.

### <span id="page-53-1"></span>**3.9.1 D\_SEL**

The D\_SEL pin can be used to configure the functionality of the combined UART1, I2C, and SPI pins. It is possible to configure the pins as UART1 + I2C, or as SPI. SPI is not available unless D\_SEL pin is set to low. See [Table](#page-53-4) 29 below.

<span id="page-53-4"></span>

| Pin no. | D_SEL == 0 | D_SEL == 1 |
|---------|------------|------------|
| 42      | SPI_SDO    | UART1 TXD  |
| 43      | SPI_SDI    | UART1 RXD  |
| 44      | SPI_CS_N   | I2C SDA    |
| 45      | SPI_CLK    | I2C SCL    |

**Table 29: D\_SEL configuration**

### <span id="page-53-2"></span>**3.9.2 RESET\_N**

The ZED-F9P provides the ability to reset the receiver. The RESET\_N pin is an input-only pin with an internal pull-up resistor. Driving RESET\_N low for at least 100 ms will trigger a cold start.

The RESET\_N pin will delete all information and trigger a cold start. It should only be used as a recovery option.

### <span id="page-53-3"></span>**3.9.3 SAFEBOOT\_N**

The ZED-F9P provides a SAFEBOOT\_N pin that is used to command the receiver safeboot mode.

If this pin is low at power up, the receiver starts in safeboot mode and GNSS operation is disabled.

The safeboot mode can be used to recover from situations where the flash content has become corrupted and needs to be restored.

In safeboot mode the receiver runs from a passive oscillator circuit with less accurate timing and hence the receiver is unable to communicate via USB.

In this mode UART1, I2C or SPI communication is possible. For communication via UART1 in safeboot mode, the host must send a training sequence (0x55 0x55 at 9600 baud) to the receiver in order to begin communication. After this the host must wait at least 2 ms before sending any data.



It is recommended to have the possibility to pull the SAFEBOOT\_N pin low in the application. This can be provided using an externally connected test point or a host I/O port.

### <span id="page-54-0"></span>**3.9.4 TIMEPULSE**

The ZED-F9P high precision receiver provides a time pulse on the TIMEPULSE pin.

More information about the time pulse feature and its configuration can be found in the Time [pulse](#page-63-1) section.

### <span id="page-54-1"></span>**3.9.5 TX\_READY**

This feature enables each port to define a corresponding pin, which indicates if bytes are ready to be transmitted. A listener can wait on the TX-READY signal instead of polling the I2C or SPI interfaces. The CFG-TXREADY message lets you configure the polarity and the number of bytes in the buffer before the TX-READY signal goes active. By default, this feature is disabled. For USB, this feature is configurable but might not behave as described below due to a different internal transmission mechanism. If the number of pending bytes reaches the threshold configured for this port, the corresponding pin will become active (configurable active-low or active-high), and stay active until the last bytes have been transferred from software to hardware.

This is not necessarily equal to all bytes transmitted, i.e. after the pin has become inactive, up to 16 bytes might still need to be transferred to the host.

The TX\_READY pin can be selected from all PIOs which are not in use (see UBX-MON-HW3 in the applicable interface description [\[2\]](#page-126-1) for a list of the PIOs and their mapping). Each TX\_READY pin is exclusively associated to one port and cannot be shared. If PIO is invalid or already in use, only the configuration for the specific TX\_READY pin is ignored, the rest of the port configuration is applied if valid. The acknowledge message does not indicate if the TX-READY configuration is successfully set, it only indicates the successful configuration of the port. To validate successful configuration of the TX\_READY pin, the port configuration should be read back and the settings of TX-READY feature verified (will be set to disabled/all zero if the settings are invalid).

The threshold when TX\_READY is asserted should not be set above 2 kB as it is possible that the internal message buffer limit is reached before this. This results in the TX\_READY pin never being set as the messages are discarded before the threshold is reached.

### **3.9.5.1 Extended TX timeout**

If the host does not communicate over SPI or I2C for more than approximately 2 seconds, the device assumes that the host is no longer using this interface and no more packets are scheduled for this port. This mechanism can be changed by enabling "extended TX timeouts", in which case the receiver delays idling the port until the allocated and undelivered bytes for this port reach 4 kB. This feature is especially useful when using the TX-READY feature with a message output rate of less than once per second, and polling data only when data is available, determined by the TX\_READY pin becoming active.

### <span id="page-54-2"></span>**3.9.6 EXTINT**

EXTINT is an external interrupt pin with fixed input voltage thresholds with respect to VCC. It can be used for functions such as accurate external frequency aiding and on/off control. The external frequency aiding can be used to calibrate the clock. This enables faster fix of satellite signals (UBX-MGA-INI-FREQ or UBX-MGA-INI-TIME\_XXX) and can be used during normal operation or during the production test. Another possibility to use the extint feature is to wake up the receiver after putting



it into backup mode; this can be set up with UBX-RXM-PMREQ. Leave open if unused, this function is disabled by default.

### <span id="page-55-0"></span>**3.9.7 GEOFENCE\_STAT interface**

The ZED-F9P provides a GEOFENCE\_STAT pin that indicates the current geofence status as to whether the receiver is inside any of the active areas.

This feature can be used for example to wake up a sleeping host when a defined geofence condition is reached. It is possible to configure up to four circular areas as geofence locations. Once configured, the receiver continuously compares its current position with the preset geofenced areas.

For more information in this functionality, see Geofence state [evaluation.](#page-38-0)

The receiver toggles the assigned pin according to the combined geofence state.

There are three possible outcomes for each geofence:

- *Inside* The position is inside the geofence with the configured confidence level
- *Outside* The position lies outside of the geofence with the configured confidence level
- *Unknown* There is no valid position solution or the position uncertainty does not allow for unambiguous state evaluation

The GEOFENCE\_STAT pin is always set to high level when the combine geofence state is unknown. The low level can either represent the inside state or the outside state according to the value set in the CFG-GEOFENCE-PINPOL configuration item. If the receiver is in software backup or in a reset, the pin will go to high accordingly.

The GEOFENCE\_STAT pin is the module pin 19 and it is assigned to PIO3.

### <span id="page-55-1"></span>**3.9.8 RTK\_STAT interface**

The ZED-F9P provides an RTK\_STAT pin that provides an indication of the RTK positioning status. It can be used to confirm if a valid stream of correction messages is being received. As valid correction messages we only consider the correction messages that are supported and used by the receiver.

In general, the RTK\_STAT level can be interpreted as follows: Alternating (blinking) pin level, indicates that a valid stream of correction messages is being received and utilized but no RTK fixed mode has been achieved. An active low pin level indicates that RTK fixed mode has been achieved. Otherwise, the pin level is high.

The RTK\_STAT pin status can be mapped to the carrSoln field of the UBX-NAV-PVT and interpreted as follows:

- An active low pin level indicates that RTK fixed mode has been achieved
- Alternating (blinking) pin level, indicates that a valid stream of correction messages is being received and utilized but no RTK fixed mode has been achieved
- An active high pin level indicates that no carrier phase solution is available

## <span id="page-55-2"></span>**3.10 Antenna supervisor**

An active antenna supervisor provides the means to check the antenna for open and short circuits and to shut off the antenna supply if a short circuit is detected. Once enabled, the active antenna supervisor produces status messages, reporting in NMEA and/or UBX protocol.

The antenna supervisor can be configured through the CFG-HW-ANT\_\* configuration items. The current configuration of the active antenna supervisor can also be checked by polling the related CFG-HW\_ANT\_\* configuration items.



The current active antenna status can be determined by polling the UBX-MON-RF message. If an antenna is connected, the initial state after power-up is "Active Antenna OK" in the UBX-MON-RF message in the u-center "Message View".

The Antenna [supervisor](#page-94-0) circuit section details the required circuit and the following sections explain how to enable and monitor each feature:

### <span id="page-56-0"></span>**3.10.1 Antenna voltage control - ANT\_OFF**

Antenna status (as reported in UBX-MON-RF and UBX-INF-NOTICE messages) is not reported unless the antenna voltage control has been enabled.

Enable the antenna voltage control by setting the configuration item CFG-HW-ANT\_CFG\_VOLTCTRL to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF pin = active high to turn antenna off therefore the pin is low to enable an external antenna.

Start-up message at power up if configuration stored:

\$GNTXT,01,01,02,ANTSUPERV=AC \*00

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC indicates antenna control is activated

### <span id="page-56-1"></span>**3.10.2 Antenna short detection - ANT\_SHORT\_N**

Enable the antenna short detection by setting the configuration item CFG-HW-ANT\_CFG\_SHORTDET to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high to disable an external antenna therefore the pin is low to enable an external antenna.
- ANT\_SHORT\_N = active low to detect a short therefore the pin is high (PIO pull up enabled to be pulled low if shorted)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD \*37

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD (Antenna control and short detection activated)

Then if shorted (ANT\_SHORT\_N pulled low):

• UBX-MON-RF in u-center "Message View": Antenna status = SHORT. Antenna power status = ON (Antenna power control power down when short has not been enabled = off by default).

\$GNTXT,01,01,02,ANTSTATUS=SHORT\*73

• ANT\_OFF = active high therefore still low (still enabled as auto power down is not enabled)



After a detected antenna short, the reported antenna status will keep on being reported as shorted. If the antenna short detection auto recovery is enabled, then the antenna status can recover after a timeout. To recover the antenna status immediately, a power cycle is required or configuring the antenna short detection functionality off and on.

### <span id="page-57-0"></span>**3.10.3 Antenna short detection auto recovery**

Enable the antenna short detection auto recovery by setting the configuration item CFG-HW-ANT\_CFG\_RECOVER to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high there for the PIO is low to enable an external antenna
- ANT\_SHORT\_N = high (PIO pull up enabled to be pulled low if shorted)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD PDoS SR\*3E

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD PDoS SR (indicates short circuit recovery added - SR)

Then if antenna is shorted (ANT\_SHORT\_N pulled low):

- \$GNTXT,01,01,02,ANTSTATUS=SHORT\*73
- UBX-MON-RF in u-center "Message View": Antenna status = SHORT. Antenna power status = OFF
- ANT\_OFF = high (to disable active high)

After a time out period receiver will retest the short condition by enabling ANT\_OFF = LOW

If a short is not present it will report antenna condition is OK:

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON

### <span id="page-57-1"></span>**3.10.4 Antenna open circuit detection - ANT\_DETECT**

Enable the antenna open circuit detection by setting the configuration item CFG-HW-ANT\_CFG\_OPENDET to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high therefore PIO is low to enable external antenna
- ANT\_SHORT\_N = active low therefore PIO is high (PIO pull up enabled to be pulled low if shorted)
- ANT\_DETECT = active high therefore PIO is high (PIO pull up enabled to be pulled low if antenna not detected)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD OD PDoS SR\*15

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B



\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD OD PDoS SR (indicates open circuit detection added - OD)

Then if ANT\_DETECT is pulled low to indicate no antenna:

\$GNTXT,01,01,02,ANTSTATUS=OPEN\*35

Then if ANT\_DETECT is left floating or it is pulled high to indicate antenna connected:

```
$GNTXT,01,01,02,ANTSTATUS=OK*25
```

# <span id="page-58-0"></span>**3.11 Multiple GNSS assistance (MGA)**

The u-blox AssistNow services provide a proprietary implementation of an A-GNSS protocol compatible with u-blox GNSS receivers.

The MGA services consist of AssistNow Online and Offline variants delivered by HTTP or HTTPS protocol. AssistNow Online optionally provides immediate satellite ephemerides, health information and time aiding data suitable for GNSS receiver systems with direct internet access.

When a client device makes an AssistNow request, the service responds with the requested data using standard UBX protocol MGA messages. These messages are ready for direct transmission from the client to the receiver port without requiring any modification.

The ZED-F9P supports AssistNow Online only.

### <span id="page-58-1"></span>**3.11.1 Authorization**

To use the AssistNow services, customers will need to obtain an authorization token from u-blox. Go to https://www.u-blox.com/en/solution/services/assistnow or contact your local technical support to get more information and to request access to the service.

### <span id="page-58-2"></span>**3.11.2 Preserving MGA and operational data during power-off**

The time-to-fix after a receiver power interruption is dependent on the amount of operational data available at startup. Satellite broadcast information plus an estimate of accurate time can be fetched form the AssistNow service. In addition, the following techniques can restore previously stored data prior to power down.

- **Battery-backed RAM:**The receiver operational state stored in this RAM can be maintained during power outages by connecting the V\_BCKP pin to an independent supply, e.g a battery. This is a recommended method as it will maintain all MGA related information plus any user configuration, calibration data and an estimate of time via the Real Time Clock. See section [V\\_BCKP:](#page-87-2) Backup supply voltage for more information.
- **Save-on-shutdown:**The receiver can be instructed to dump its current state to flash memory as part of the shutdown procedure; this data is then automatically retrieved when the receiver is restarted. For more information, see section [Save-on-shutdown](#page-0-0) feature for more info. For information on the UBX-UPD-SOS messages consult the applicable Interface description [[2\]](#page-126-1).
- **Database dump:** The receiver can be made to dump the state of its navigation database in the form of a sequence of UBX messages reported to the host; these messages can be stored by the host and then sent back to the receiver when it has been restarted. See the description of the UBX-MGA-DBD messages in the applicable Interface description [\[2\]](#page-126-1) for more information.



# <span id="page-59-0"></span>**3.12 Clocks and time**

This section introduces and explains the concepts of receiver clocks and time bases.

### <span id="page-59-1"></span>**3.12.1 Receiver local time**

The receiver is dependent on a local oscillator for both the operation of its radio parts and also for timing within its signal processing. No matter what nominal frequency the local oscillator has, u-blox receivers subdivide the oscillator signal to provide a 1-kHz reference clock signal, which is used to drivemany of the receiver's processes. In particular, themeasurement of satellite signals is arranged to be synchronized with the "ticking" of this 1-kHz clock signal.

When the receiver first starts, it has no information about how these clock ticks relate to other time systems; it can only count time in 1 millisecond steps. However, as the receiver derives information from the satellites it is tracking or from aiding messages, it estimates the time that each 1-kHz clock tick takes in the time base of the chosen GNSS system. This estimate of GNSS time based on the local 1-kHz clock is called receiver local time.

As receiver local time is a mapping of the local 1-kHz reference onto a GNSS time base, it may experience occasional discontinuities, especially when the receiver first starts up and the information it has about the time base is changing. Indeed, after a cold start, the receiver local time will initially indicate the length of time that the receiver has been running. However, when the receiver obtains some credible timing information from a satellite or an aiding message, it will jump to an estimate of GNSS time.

### <span id="page-59-2"></span>**3.12.2 Navigation epochs**

Each navigation solution is triggered by the tick of the 1-kHz clock nearest to the desired navigation solution time. This tick is referred to as a **navigation epoch**. If the navigation solution attempt is successful, one of the results is an accurate measurement of time in the time base of the chosen GNSS system, called **GNSS system time**. The difference between the calculated GNSS system time and receiver local time is called **clock bias** (and **clock drift** is the rate at which this bias is changing).

In practice the receiver's local oscillator will not be as stable as the atomic clocks to which GNSS systems are referenced and consequently clock bias will tend to accumulate. However, when selecting the next navigation epoch, the receiver will always try to use the 1-kHz clock tick which it estimates to be closest to the desired fix period as measured in GNSS system time. Consequently the number of 1-kHz clock ticks between fixes will occasionally vary. This means that when producing one fix per second, there will normally be 1000 clock ticks between fixes, but sometimes, to correct drift away from GNSS system time, there will be 999 or 1001.

The GNSS system time calculated in the navigation solution is always converted to a time in both the GPS and UTC time bases for output.

Clearly when the receiver has chosen to use the GPS time base for its GNSS system time, conversion to GPS time requires no work at all, but conversion to UTC requires knowledge of the number of leap seconds since GPS time started (and other minor correction terms). The relevant GPS-to-UTC conversion parameters are transmitted periodically (every 12.5 minutes) by GPS satellites, but can also be supplied to the receiver via the UBX-MGA-GPS-UTC aiding message. By contrast, when the receiver has chosen to use the GLONASS time base as its GNSS system time, conversion to GPS time is more difficult as it requires knowledge of the difference between the two time bases, but as GLONASS time is closely linked to UTC, conversion to UTC is easier.

When insufficient information is available for the receiver to perform any of these time base conversions precisely, predefined default offsets are used. Consequently plausible times are nearly



always generated, but they may be wrong by a few seconds (especially shortly after receiver start). Depending on the configuration of the receiver, such "invalid" times may well be output, but with flags indicating their state (e.g. the "valid" flags in UBX-NAV-PVT).

### <span id="page-60-0"></span>**3.12.3 iTOW timestamps**

All the main UBX-NAV messages (and some other messages) contain an **iTOW** field which indicates the GPS time at which the navigation epoch occurred. Messages with the same iTOW value can be assumed to have come from the same navigation solution.

Note that iTOW values may not be valid (i.e. they may have been generated with insufficient conversion data) and therefore it is not recommended to use the iTOW field for any other purpose.

The original designers of GPS chose to express time/date as an integer week number (starting with the first full week in January 1980) and a time of week (often abbreviated to TOW) expressed in seconds. Manipulating time/date in this form is far easier for digital systems than the more conventional year/month/day, hour/minute/second representation. Consequently, most GNSS receivers use this representation internally, only converting to a more conventional form at external interfaces. The iTOW field is the most obvious externally visible consequence of this internal representation.

If reliable absolute time information is required, users are recommended to use the UBX-NAV-PVT navigation solution message which also contains additional fields that indicate the validity (and accuracy in UBX-NAV-PVT) of the calculated times (see also the [GNSS times](#page-60-1) section below for further messages containing time information).

### <span id="page-60-1"></span>**3.12.4 GNSS times**

Each GNSS has its own time reference for which detailed and reliable information is provided in the messages listed in the table below.

| Time reference | Message          |
|----------------|------------------|
| GPS time       | UBX-NAV-TIMEGPS  |
| BeiDou time    | UBX-NAV-TIMEBDS  |
| GLONASS time   | UBX-NAV-TIMEGLO  |
| Galileo time   | UBX-NAV-TIMEGAL  |
| QZSS time      | UBX-NAV-TIMEQZSS |
| UTC time       | UBX-NAV-TIMEUTC  |

**Table 30: GNSS times**

### <span id="page-60-2"></span>**3.12.5 Time validity**

Information about the validity of the time solution is given in the following form:

- Time validity: Information about time validity is provided in the valid flags (e.g. validDate and validTime flags in the UBX-NAV-PVT message). If these flags are set, the time is known and considered valid for use. These flags are shown in table GNSS times in section GNSS times above as well as in the UBX-NAV-PVT message.
- Time validity confirmation: Information about confirmed validity is provided in the confirmedDate and confirmedTime flags in the UBX-NAV-PVT message. If these flags are set, the time validity can be confirmed by using an additional independent source, meaning that the probability of the time to be correct is very high. Note that information about time validity confirmation is only available if the confirmedAvai bit in the UBX-NAV-PVT message is set.



- validDate means that the receiver has knowledge of the current date. However, it must be noted that this date might be wrong for various reasons. Only when the confirmedDate flag is set, the probability of the incorrect date information drops significantly.
- validTime means that the receiver has knowledge of the current time. However, it must be noted that this time might be wrong for various reasons. Only when the confirmedTime flag is set, the probability of incorrect time information drops significantly.
- fullyResolved means that the UTC time is known without full seconds ambiguity. When deriving UTC time from GNSS time the number of leap seconds must be known, with the exception of GLONASS. It might take several minutes to obtain such information from the GNSS payload. When the one second ambiguity has not been resolved, the time accuracy is usually in the range of ~20s.

### <span id="page-61-0"></span>**3.12.6 UTC representation**

UTC time is used in many NMEA and UBX messages. In NMEA messages it is always reported rounded to the nearest hundredth of a second. Consequently, it is normally reported with two decimal places (e.g. 124923.52). Although compatibility mode (selected using CFG-NMEA-COMPAT) requires three decimal places, rounding to the nearest hundredth of a second remains, so the extra digit is always 0.

UTC time is also reported within some UBX messages, such as UBX-NAV-TIMEUTC and UBX-NAV-PVT. In these messages date and time are separated into seven distinct integer fields. Six of these (year, month, day, hour, min and sec) have fairly obvious meanings and are all guaranteed to match the corresponding values in NMEA messages generated by the same navigation epoch. This facilitates simple synchronization between associated UBX and NMEA messages.

The seventh field is called nano and it contains the number of nanoseconds by which the rest of the time and date fields need to be corrected to get the precise time. So, for example, the UTC time 12:49:23.521 would be reported as: hour: 12, min: 49, sec: 23, nano: 521000000.

It is however important to note that the first six fields are the result of rounding to the nearest hundredth of a second. Consequently the nano value can range from -5000000 (i.e. -5 ms) to +994999999 (i.e. nearly 995 ms).

When the nano field is negative, the number of seconds (and maybe minutes, hours, days, months or even years) will have been rounded up. Therefore, some or all of them must be adjusted in order to get the correct time and date. Thus in an extreme example, the UTC time 23:59:59.9993 on 31st December 2011 would be reported as: year: 2012, month: 1, day: 1, hour: 0, min: 0, sec: 0, nano: -700000.

Of course, if a resolution of one hundredth of a second is adequate, negative nano values can simply be rounded up to 0 and effectively ignored.

The UBX-NAV-TIMEUTC message gives information about UTC time reference clock.

The preferred variant of UTC time can be specified using CFG-NAVSPG-UTCSTANDARD configuration item.

### <span id="page-61-1"></span>**3.12.7 Leap seconds**

Occasionally it is decided (by one of the international time keeping bodies) that, due to the slightly uneven spin rate of the Earth, UTC has moved sufficiently out of alignment with mean solar time (i.e. the Sun no longer appears directly overhead at 0 longitude at midday). A "leap second" is therefore announced to bring UTC back into close alignment. This normally involves adding an extra second to the last minute of the year, but it can also happen on 30th June. When this happens UTC clocks are expected to go from 23:59:59 to 23:59:60 and only then on to 00:00:00.

It is also theoretically possible to have a negative leap second, in which case there will only be 59 seconds in a minute and 23:59:58 will be followed by 00:00:00.

u-blox receivers are designed to handle leap seconds in their UTC output and consequently users processing UTC times from either NMEA or UBX messages should be prepared to handle minutes that are either 59 or 61 seconds long.

Leap second information can be polled from the u-blox receiver with the message UBX-NAV-TIMELS.

### <span id="page-62-0"></span>**3.12.8 Real-time clock**

u-blox receivers contain circuitry to support a real-time clock, which (if correctly fitted and powered) keeps time while the receiver is otherwise powered off. When the receiver powers up, it attempts to use the real-time clock to initialize receiver local time and in most cases this leads to appreciably faster first fixes.

### <span id="page-62-1"></span>**3.12.9 Date**

All GNSS frequently transmit information about the current time within their data message. In most cases, this is a time of week (often abbreviated to TOW), which indicates the elapsed number of seconds since the start of the week (midnight Saturday/Sunday). In order to map this to a full date, it is necessary to know the week and so the GNSS also transmit a week number, typically every 30 seconds. Unfortunately the GPS L1C/A data message was designed in a way that only allows the bottom 10 bits of the week number to be transmitted. This is not sufficient to yield a completely unambiguous date as every 1024 weeks (a bit less than 20 years), the transmitted week number value "rolls over" back to zero. Consequently, GPS L1 receivers cannot tell the difference between, for example, 1980, 1999 or 2019 etc.

Fortunately, although BeiDou and Galileo have similar representations of time, they transmit sufficient bits for the week number to be unambiguous for the foreseeable future (the first ambiguity will be in 2078 for Galileo and not until 2163 for BeiDou). GLONASS has a different structure, based on a time of day, but again transmits sufficient information to avoid any ambiguity during the expected lifetime of the system (the first ambiguous date will be in 2124). Therefore, ublox 9 receivers using Protocol Version 24 and above regard the date information transmitted by GLONASS, BeiDou and Galileo to be unambiguous and, where necessary, use this to resolve any ambiguity in the GPS date.

Customers attaching u-blox receivers to simulators should be aware that GPStime is referenced to 6th January 1980, GLONASS to 1st January 1996, Galileo to 22nd August 1999 and BeiDou to 1st January 2006; the receiver cannot be expected to work reliably with signals simulated before these dates.

#### **3.12.9.1 GPS-only date resolution**

In circumstances where only GPS L1C/A signals are available and for receivers with earlier firmware versions, the receiver establishes the date by assuming that all week numbers must be at least as large as a reference rollover week number. This reference rollover week number is hard-coded at compile time and is normally set a few weeks before the software is completed, but it can be overridden by CFG-NAVSPG-WKNROLLOVER configuration item to any value the user wishes.

The following example illustrates how this works: Assume that the reference rollover week number set in the firmware at compile time is 1524 (which corresponds to a week in calendar year 2009, but would be transmitted by the satellites as 500). In this case, if the receiver sees transmissions



containing week numbers in the range of 500 ... 1023, these will be interpreted as week numbers 1524 ... 2047 (calendar year 2009 ... 2019), whereas transmissions with week numbers from 0 to 499 are interpreted as week numbers 2048 ... 2547 (calendar year 2019 ... 2028).

It is important to set the reference rollover week number appropriately when supplying u-blox receivers with simulated signals, especially when the scenarios are in the past.

# <span id="page-63-0"></span>**3.13 Timing functionality**

In addition to positioning and navigation applications, GNSS signals are widely used as low-cost precision time or frequency references used by remote or distributed wireless communication, industrial, financial, and power distribution equipment. By capitalizing on atomic clocks which are on-board positioning satellites, GNSS signals which contain embedded timing information can be used to synchronize equipment, as well as to provide UTC time. For wireless communication standards that utilize Time Division Multiplex (TDM) and applications such as femtocell base stations, a precision time reference is mandatory.

### <span id="page-63-1"></span>**3.13.1 Time pulse**

#### **3.13.1.1 Introduction**

u-blox receivers include a time pulse function providing clock pulses with configurable duration and frequency. The time pulse function can be configured using the CFG-TP-\* configuration group. The UBX-TIM-TP message provides time information for the next pulse and the time source.



#### **Figure 24: Time pulse**

#### **3.13.1.2 Recommendations**

- The time pulse can be aligned to a wide variety of GNSS times or to variants of UTC derived from them (see the section on [time bases](#page-64-0)). However, it is strongly recommended that the choice of time base is aligned with the available GNSS signals (so to produce GPS time or UTC(USNO), ensure GPS signals are available, and for Galileo time or UTC(EU) ensure the presence of Galileo signals, etc). This will involve coordinating the setting of CFG-SIGNAL-\* configuration group with the choice of time pulse time base.
- When using time pulse for timing applications requiring absolute time accuracy, e.g. with requirements specifying offset to UTC, it is recommended to calibrate the user's full setup for TP output against a reference timing source. To achieve best absolute and consistent accuracy (e.g. for mass deployment), it is recommended that the user should calibrate each single setup and calibrate under different GNSS modes and different temperatures which are applicable to



the user's application and operating requirements. The user should take the calibrated values and configure the compensation accordingly (see the section on Time pulse [configuration](#page-65-0))

- To get the best timing accuracy with the antenna, a fixed and *accurate* position is needed.
- If relative time accuracy between multiple receivers is required, do not mix receivers of different product families. If this is required, the receivers must be calibrated accordingly, by setting cable delay and user delay.
- The recommended configuration when using the UBX-TIM-TP message is to set both the measurement rate (CFG-RATE-MEAS) and the time pulse frequency (CFG-TP-\*) to 1 Hz.
- Since the rate of UBX-TIM-TP is bound to 1 Hz, more than one UBX-TIM-TP message can appear between two pulses if the time pulse frequency is set larger than 1 Hz. In this case all UBX-TIM-TP messages in between time pulses T1 and T2 belong to T2 and the last UBX-TIM-TP before T2 reports the most accurate quantization error. In general, if the time pulse rate is not configured to 1 Hz, there will not be a single UBX-TIM-TP message for each time pulse.

The sequential order of the signal present at theTIMEPULSEpinand the respective outputmessage for the simple case of 1 pulse per second (1PPS) is shown in the following figure.



#### **Figure 25: Time pulse and TIM-TP**

#### <span id="page-64-0"></span>**3.13.1.3 GNSS time bases**

GNSS receivers must handle a variety of different time bases as each GNSS has its own reference system time. What is more, although each GNSS provides a model for converting their system time into UTC, they all support a slightly different variant of UTC. So, for example, GPS supports a variant of UTC as defined by the US National Observatory, while BeiDou uses UTC from the National Time Service Center, China (NTSC). While the different UTC variants are normally closely aligned, they can differ by as much as a few hundreds of nanoseconds.

Although u-blox receivers can combine a variety of different GNSS times internally, the user must choose a single type of GNSS time and, separately, a single type of UTC for input (on EXTINT pins) and output (via the TIMEPULSE pin) and the parameters reported in corresponding messages.

The CFG-TP-TIMEGRID\_TP\* configuration item allows the user to choose between any of the supported GNSS (Galileo, GPS, BeiDou, etc.) time bases and UTC. Also, the CFG-NAVSPG-UTCSTANDARD configuration item allows the user to select which variant of UTC the receiver should use. This includes an "automatic" option which causes the receiver to select an appropriate UTC version itself, based on the GNSS configuration, using, in order of preference, USNO if GPS is enabled, SU if GLONASS is enabled, NTSC if BeiDou is enabled, European if Galileo is enabled, finally, NPLI if NAVIC is enabled.

The receiver will assume that an input time pulse uses the same GNSS time base as specified for the time pulse output. So, if the user selects Galileo time for time pulse output, any time pulse input



must also be aligned to Galileo time (or to the separately chosen variant of the UTC). When UTC is selected for the time pulse output, any GNSS time pulse input must be aligned to GPS time.

- u-blox receivers allow users to independently choose GNSS signals used in the receiver (using CFG-SIGNAL-\*) and the input/output time base (using CFG-TP-\*). For example, it is possible to instruct the receiver to use GPS and Galileo satellite signals to generate BeiDou time. This practice will compromise time pulse accuracy if the receiver cannot measure the timing difference between the constellations directly and is therefore not recommended.
- The information that allows GNSS times to be converted to the associated UTC times is only transmitted by the GNSS at relatively infrequent periods. For example GPS transmits UTC(USNO) information only once every 12.5 minutes. Therefore, if a time pulse is configured to use a variant of UTC time, after a cold start, substantial delays before the receiver has sufficient information to start outputting the time pulse can be expected.

#### **3.13.1.4 Time pulse configuration**

u-blox ZED-F9P receivers provide a time pulse (TIMEPULSE) signal with a configurable pulse period, length and polarity (rising or falling edge).

It is possible to define different signal behavior (i.e. output frequency and pulse length) depending on whether or not the receiver is locked to a reliable time source. Time pulse signal can be configured using the configuration group CFG-TP-\*.

#### <span id="page-65-0"></span>**3.13.1.5 Configuring time pulse with CFG-TP-\***

The configuration group CFG-TP-\* can be used to change the time pulse settings, and includes the following parameters defining the pulse:

- **timepulse enable** If this item is set, the time pulse is active.
- **frequency/period type** Determines whether the time pulse is interpreted as frequency or period.
- **length/ratio type** Determines whether the time pulse length is interpreted as length [us] or pulse ratio [%].
- **antenna cable delay** Signal delay owning to RF components (e.g. antenna, cable, and splitter etc.) before the receiver input. This delay parameter affects the receiver calculation of GNSS time and it is used to compensate for the signal transit time prior to the receiver and any uncompensated delay from the receiver; a positive value compensates this delay, i.e. advances the time pulse
- **pulse frequency/period** Frequency or pulse time period when locked mode is not configured or active.
- **pulse frequency/period lock** Frequency or pulse time period, as soon as the receiver has calculated a valid time from a received signal. Only used if the corresponding item is set to use another setting in locked mode.
- **pulse length/ratio** Length or duty cycle of the generated pulse, either specifies a time or ratio for the pulse to be on/off.
- **pulse length/ratio lock** Length or duty cycle of the generated pulse, as soon as the receiver has calculated a valid time from a received signal. Only used if the corresponding item is set to use another setting in locked mode.
- **user delay** A time offset of the TP output for adjustment in a user application. It adjusts the time pulse position only with respect to GNSS time. Configuring a positive value will add a delay, i.e. retard the pulse with respect to GNSS time. Conversely, a negative value will advance the pulse. This configuration is available for all supported TP outputs.
- **lock to GNSS freq** If this item is set, uses the frequency gained from the GNSS signal information rather than the local oscillator's frequency.



- **locked other setting** If this item is set, the alternative setting will be used as soon as the receiver can calculate a valid time. This mode can be used, for example, to disable time pulse if the time is not locked, or to indicate a lock with different duty cycles.
- **align to TOW** If this item is set, pulses are aligned to the top of a second.
- **polarity** If set, the first edge of the pulse is a rising edge (pulse polarity: rising).
- **grid UTC/GNSS** Selection between UTC and various GNSS time grids. Also affects the time output by UBX-TIM-TP message.

The maximum pulse length cannot exceed the pulse period.

Time pulse settings shall be chosen in such a way that neither the high nor the low period of the output is less than 50 ns (except when disabling it completely), otherwise pulses can be lost.

#### **3.13.1.5.1 Example**

The example below shows the 1PPS TIMEPULSE signal generated on the time pulse output according to the specific parameters of the CFG-TP-\* configuration group:

- **CFG-TP-TP1\_ENA** = 1
- **CFG-TP-PULSE\_DEF** = 0 (PERIOD)
- **CFG-TP-PULSE\_LENGTH\_DEF** = 1 (LENGTH)
- **CFG-TP-PERIOD\_TP1** = 1 000 000 µs
- **CFG-TP-LEN\_TP1** = 100 000 µs
- **CFG-TP-TIMEGRID\_TP1** = 1 (GPS)
- **CFG-TP-ALIGN\_TO\_TOW\_TP1** = 1
- **CFG-TP-USE\_LOCKED\_TP1** = 1
- **CFG-TP-POL\_TP1** = 1
- **CFG-TP-PERIOD\_LOCK\_TP1** = 1 000 000 µs
- **CFG-TP-LEN\_LOCK\_TP1** = 100 000 µs

The 1 Hz output is maintained whether or not the receiver is locked to GPS time. The alignment to TOW can only be maintained when GPS time is locked.



**Figure 26: Time pulse signal with the example parameters**

### <span id="page-66-0"></span>**3.13.2 Time mark**

The receiver can be used to provide an accurate measurement of the time at which a pulse was detected on the external interrupt pin. The reference time can be chosen by setting the time source parameter to UTC, GPS, GLONASS, BeiDou, Galileo or local time in the CFG-TP-\* configuration group. The UTC standard can be set in the CFG-NAVSPG-\* configuration group. The delay figures defined with CFG-TP-\* are also applied to the results output in the UBX-TIM-TM2 message.

A UBX-TIM-TM2 message is output at the next epoch if

- The UBX-TIM-TM2 message is enabled, and
- A rising or falling edge was triggered since last epoch on one of the EXTINT channels.



The UBX-TIM-TM2 messages includes the time of the last time mark, new rising/falling edge indicator, time source, validity, number of marks and an accuracy estimate.

Only the last rising and falling edge detected between two epochs is reported since the output rate of the UBX-TIM-TM2 message corresponds to the measurement rate configured with CFG-RATE-MEAS (see [Figure](#page-67-1) 27 below).

<span id="page-67-1"></span>

**Figure 27: Time mark**

## <span id="page-67-0"></span>**3.14 Security**

The security concept of ZED-F9P covers:

- the security of the receiver
- communication between the receiver and the GNSS satellites

Some receiver security functions monitor and detect threats and report them to the host system. Other security functions mitigate threats and allow the receiver to operate normally.

The table below gives an overview about possible threats and which functionality is available to detect and/or mitigate it.

| Threat                   | u-blox solution                                                |  |
|--------------------------|----------------------------------------------------------------|--|
| Over air signal security | Spoofing detection and monitoring                              |  |
|                          | Jamming interference detection and monitoring                  |  |
|                          | Galileo Open Service Navigation Message Authentication (OSNMA) |  |



| Threat                 | u-blox solution             |  |
|------------------------|-----------------------------|--|
| GNSS receiver security | Secure boot                 |  |
|                        | Secure firmware update      |  |
|                        | Receiver configuration lock |  |

**Table 31: u-blox security options**

### <span id="page-68-0"></span>**3.14.1 Spoofing detection and monitoring**

Spoofing is the process where a counterfeit GNSS signal is transmitted locally to deceive the receiver/user and produce an erroneous position fix and/or time solution.

The detection algorithm monitors GNSS signals for implausible changes or inconsistencies.These are evaluated with regards to spoofing.

A detection is successful when a signal is observed to transition from an initially genuine one to a spoofed version. Hence detection is not possible if the receiver is started under spoofing conditions. The detection algorithms also rely on availability of signals from multiple GNSS constellations to improve the spoofing detection capabilities.

### <span id="page-68-1"></span>**3.14.2 Jamming and interference detection and monitoring**

Intentional and/or unintentional jamming of GNSSreceivers candegrade the quality of GNSSsignals and receiver performance. All u-blox receivers can detect and monitor jamming and report it to the user. The monitoring function is always enabled to inform the user about interference in the GNSS RF bands.

In case of excessive false jamming alerts, the jamming detector sensitivity can be configured with the CFG-SEC-JAMDET\_SENSITIVITY\_HI configuration.

### <span id="page-68-2"></span>**3.14.3 Spoofing and jamming indication**

The UBX-SEC-SIG message provides a direct method for monitoring the current security status at each navigation epoch to alert the host about potential jamming or spoofing events.

The UBX-SEC-SIGLOG message provides a log of past events triggered by jamming or spoofing detection.

Each event is a combination of a detection type and an event type, where the event type 'indication started' and 'indication stopped' and also the event type 'indication triggered' and 'indication timeout' form a pair.

A maximum of 16 events are logged and new events take precedence over the past events in the log. Power cycles and restarts of the receiver reset the log, deleting its content.

See the applicable Interface description [\[2\]](#page-126-1).

### <span id="page-68-3"></span>**3.14.4 GNSS receiver security**

#### <span id="page-68-4"></span>**3.14.4.1 Secure boot**

The ZED-F9Pboots only withfirmware images that are signed by u-blox.This prevents the execution of non-genuine firmware images on the receiver.

#### <span id="page-68-5"></span>**3.14.4.2 Secure firmware update**

The firmware image is signed by u-blox. The ZED-F9P verifies the signature during the firmware update.



#### <span id="page-69-1"></span>**3.14.4.3 Receiver configuration lock**

Supported from firmware version HPG 1.30 onwards

The receiver configuration lock feature ensures that no configuration changes are possible once the feature is enabled. The configuration lock is enabled by setting the configuration item CFG-SEC-CFG\_LOCK to "true".

The configuration lock can be applied to different configuration layers including the RAM, BBR, and flash memory. At startup, the receiver constructs the configuration database from different configuration layers and maintains it in the run-time RAM memory. When the configuration lock is set in the run-time RAM, the receiver configuration cannot be changed on any configuration layer.

For more information on the configuration layers including the order of priority they are applied in, see the applicable interface description [[2](#page-126-1)].

The configuration lock set on a configuration layer in volatile memory (RAM, BBR) is removed when the memory is cleared. However, the configuration lock set in non-volatile memory (flash memory) is permanent apart from one exception: during firmware upload to flash memory, the flash is erased during the process causing the configuration lock to be cleared. Refer to [Firmware](#page-81-1) upload for more information on firmware update.

To test the lock functionality, set it on the RAM configuration layer. After a power cycle, the information on RAM layer is cleared and the lock is no longer set.

It is recommended to apply the configuration lock on the same layer the configuration is stored.

An example of use case is that the host application locks the receiver configuration. A user communicating with the ZED-F9P through any of the available interfaces can poll, enable or send messages, but cannot change the configuration by sending UBX configuration messages.

#### **3.14.4.4 Compliance with DHS allow list**

The GPS allow list is a list of checks that have been implemented in the ZED-F9P receiver firmware in order to validate LNAV navigation input data downloaded from the GPS satellites. These checks will improve the reliability of the receiver, blocking unreliable data from entering in the navigation solution or warning the user about issues in the navigation message.

The official DHS allow list guide DHS - GPS Receiver Allow List [Development](https://www.dhs.gov/science-and-technology/publication/gps-receiver-allow-list-development-guide) Guide provides an example of an allow list, and guidelines on building a series of rules to validate the input data. To ensure product security and minimize vulnerabilities, a significant number of checks have been added to the ZED-F9P firmware.

This feature is available as of firmware version HPG 1.50.

### <span id="page-69-0"></span>**3.14.5 Galileo Open Service Navigation Message Authentication (OSNMA)**

- This feature is available as of firmware version HPG 1.50.
- The OSNMA Initial Service Declaration process has not been initiated at the time of writing the document.

Open Service Navigation Message Authentication (OSNMA) is a free data authentication service for Galileo Open Service users worldwide. It allows users to confirm that the received Galileo OS navigation data originates from the Galileo system itself and has not been modified. It serves as a strong layer of protection in detecting various spoofing attacks and delayed attacks, also known as meaconing or record-and-replay attacks.

The OSNMA protocol data is transmitted in the previously reserved fields of the Galileo I/NAV message broadcasted on the E1B signal component. As the OSNMA data uses previously reserved



fields of the I/NAV message, it is fully backwards compatible. Legacy receivers function with the same performance by simply ignoring the OSNMA fields of I/NAV message.

The ZED-F9P also supports cross-authentication. This means that the receiver can authenticate navigation messages from both the Galileo satellites which transmit and don't transmit the OSNMA protocol data, the receiver utilizes the data retrieved from the satellites transmitting OSNMA data.

#### **3.14.5.1 Cryptographic keys**

The cryptographic keys which the OSNMA security relies on, namely the Public Key and the Merkle tree root, are not factory installed. They need to be provisioned securely to the receiver and it is crucial to protect the integrity and authenticity of the these keys.

#### **Public Key:**

The Public Key is used to verify the TESLA chain provided within the Digital Signature Message of the OSNMA protocol data. The Public Key is transmitted in the I/NAV data of the E1B signal every 6 hours for 30 minutes starting at 00:00 GST. Alternatively, the Public Key can be retrieved as an xml file from the GSC web portal. The host system can provide it to the receiver.

#### **Merkle tree root:**

The Merkle tree root is used to verify the Public Key transmitted over the signal in space. It is only available as a Merkle tree xml file from the GSC web portal, not as a signal in space. Merkle tree root is not needed if the Public Key is provided to the receiver by the host system.

#### **3.14.5.1.1 Downloading the OSNMA cryptographic keys**

To download the Public Key and Merkle tree root, register at the European GNSS Service Center (GSC) web portal (https://www.gsc-europa.eu). Subscribe to the OSNMA products and after that has been confirmed, download the Public Key and Merkle tree xml files from the GSC PRODUCTS menu.

The interface to the GSC OSNMA Server is specified in the Galileo Open Service Navigation Message Authentication (OSNMA) Internet Data Distribution (IDD) Interface Control Document (https://www.gsc-europa.eu/sites/default/files/sites/all/files/ Galileo\_OSNMA\_IDD\_ICD\_v1.1.pdf).

#### **3.14.5.1.2 Sending the OSNMA cryptographic keys to the receiver**

See [Table](#page-70-0) 32 for the cryptographic key messages related to the OSNMA feature. For more details, refer to the Interface description [\[2](#page-126-1)].

<span id="page-70-0"></span>

| OSNMA Cryptographic keys | Description                                                                                                                                                                                                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UBX-MGA-GAL-OSNMA_PUBKEY | To avoid waiting for the Public Key to be transmitted in the signal, it<br>can be sent to the receiver with the UBX-MGA-GAL-OSNMA_PUBKEY<br>message.                                                                                                                                  |
|                          | This message requires the corresponding Public Key ID (PKID), the hash<br>function with which the Public Key is hashed (Example: SHA-256 or<br>SHA-512), the actual hexadecimal Public Key point which can be found<br>in the Public Key xml file downloaded from the GSC web portal. |
| UBX-MGA-GAL-OSNMA_MERKLE | Use this message to send the OSNMA Merkle tree root to the receiver.<br>This message requires the applicability time of the Merkle tree root<br>(current or future), and the hexadecimal Merkle tree root which can be<br>found in the Merkle tree xml file.                          |
|                          | The current and future applicability time of the Merkle tree root is used<br>during the Merkle tree renewal process. The future Merkle tree root will<br>be published in the GSC web portal 2 years prior to the renewal.                                                             |

**Table 32: OSNMA cryptographic key messages**



- The ZED-F9P does not contain factory installed cryptographic keys. It is the user's responsibility to ensure the receiver always has the current valid keys, even after a Public Key and/or Merkle tree renewal event.
- The Public Key and Merkle tree root are sent from the host to the receiver over the host communication interface and stored in the non-volatile storage. During this process both keys are unprotected. To protect the keys, the host system must prevent unauthorized access to the system.

#### **3.14.5.1.3 Storing the cryptographic keys on the receiver**

The cryptographic keys sent to the receiver are stored in the non-volatile storage (NVS) on the receiver and they are retained after a power-down event.

If the Public Key stored in the NVS has expired, it is replaced with the one retrieved from the Galileo signal if the Merkle tree root available on the receiver is still valid.

If both the Public Key and the Merkle tree root stored in the NVS have expired, both keys must be updated by the host.

#### **3.14.5.2 Trusted time**

To detect delayed attacks, an OSNMA-capable receiver cannot trust on the time decoded from the Galileo satellites. Therefore, the host needs to provide the trusted time. This is compared to the time which the receiver decodes from the Galileo satellites. If the difference between the time decoded from the satellites and the trusted time provided by the host is:

- < 15 sec: OSNMA uses fast MACs (Message Authentication Codes) which is the normal OSNMA operation.
- 15 165 sec: OSNMA uses slow MACs. It takes longer to authenticate Galileo navigation data than using fast MACs.
- >= 165 sec: OSNMA will not be performed.

#### **3.14.5.2.1 Providing trusted time to the receiver**

See [Table](#page-71-0) 33 for the messages related to Trusted time. For more details, refer to the Interface description [\[2\]](#page-126-1).

<span id="page-71-0"></span>

| Trusted time messages | Description                                                                            |  |
|-----------------------|----------------------------------------------------------------------------------------|--|
| UBX-MGA-INI-TIME_UTC  | These messages can be used to provide trusted time either in UTC or                    |  |
| UBX-MGA-INI_TIME_GNSS | GNSS time, respectively. Both messages allow to provide a trusted flag<br>to the time. |  |

#### **Table 33: Trusted time messages**

To protect the integrity of the trusted time provided by the host, it is propagated by the receiver using an internal free-running TCXO. This ensures the trusted time is completely independent from the Galileo satellite data. Due to the imperfections of the TCXO, the propagated trusted time accuracy will degrade over time.

See [Table](#page-71-1) 34 for the items related to Trusted time propagation. For more details, refer to the Interface description [\[2\]](#page-126-1).

<span id="page-71-1"></span>

| Trusted time propagation | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| UBX-NAV-TIMETRUSTED      | Provides information about the current propagated trusted time<br>accuracy. |

#### **Table 34: Trusted time propagation messages**

The host system must monitor the propagated trusted time accuracy from the UBX-NAV-TIMETRUSTED message and periodically provide the trusted time to the receiver to maintain the



accuracy within 15 seconds to avoid fall back to slow MACs or even losing OSNMA operation altogether.

#### **3.14.5.3 Configuring OSNMA**

See [Table](#page-72-0) 35 for the configuration messages related to the OSNMA feature. For more details, refer to the Interface description [[2](#page-126-1)].

<span id="page-72-0"></span>

| OSNMA Configuration           | Description                                                                                                                                |  |  |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| CFG-GAL-USE_OSNMA             | Enables the execution of OSNMA.                                                                                                            |  |  |
| CFG-GAL-OSNMA_TIMESYNC        | Enables trusted time synchronization requirement for the OSNMA. By<br>default, set to true as instructed by the OSNMA Receiver Guidelines. |  |  |
| CFG-NAVSPG-ONLY_AUTHDATA      | When enabled, navigation uses only signals with authenticated                                                                              |  |  |
| CFG-NAV2-NAVSPG_ONLY_AUTHDATA | navigation data.                                                                                                                           |  |  |
| CFG-GAL-OSNMA_INAVPRIM        | Use authenticated I/NAV as primary data source over non<br>authenticated FNAV in E1-E5a configuration.                                     |  |  |
| CFG-GAL-OSNMA_MINTAGLENGTH    | The minimum tag length that defines the number of times the data<br>needs to be authenticated before declaring it authenticated.           |  |  |

**Table 35: OSNMA configuration messages**

#### **3.14.5.4 Verifying OSNMA**

See [Table](#page-72-1) 36 for the messages that give information about the status of the OSNMA processing in the receiver. For more details, refer to the Interface description [[2](#page-126-1)].

<span id="page-72-1"></span>

| OSNMA Verification messasges | Description                                                                                                                                                                                                                                                                                                                                             |  |  |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| UBX-SEC-OSNMA                | Provides information related to the status and execution of the OSNMA<br>protocol.                                                                                                                                                                                                                                                                      |  |  |
|                              | The latest authentication service status and configuration.                                                                                                                                                                                                                                                                                             |  |  |
|                              | The total number of satellites transmitting the OSNMA protocol data<br>and the authentication results per satellite are reported periodically.                                                                                                                                                                                                          |  |  |
|                              | The status of Digital Signature Message authentication.                                                                                                                                                                                                                                                                                                 |  |  |
|                              | TESLA key authentication.                                                                                                                                                                                                                                                                                                                               |  |  |
|                              | Time synchronization.                                                                                                                                                                                                                                                                                                                                   |  |  |
|                              | The difference between the propagated trusted time and the time<br>decoded from the Galileo navigation data.                                                                                                                                                                                                                                            |  |  |
| UBX-NAV-SIG                  | Includes an additional field to indicate the authentication status of the<br>navigation data used to compute the satellite's position in the current<br>epoch per signal.                                                                                                                                                                               |  |  |
| UBX-NAV-PVT                  | Indicates if the PVT fix has been verified with the NMA data. The<br>nmaFixStatus flag is set to 1, indicating the PVT fix has been verified.                                                                                                                                                                                                           |  |  |
|                              | Indicates if the output time has been validated against the external<br>trusted time source.                                                                                                                                                                                                                                                            |  |  |
|                              | If<br>the<br>difference<br>between<br>the<br>receiver<br>estimated<br>time<br>and<br>the<br>external<br>trusted<br>time<br>provided<br>by<br>the<br>host<br>is<br>smaller<br>than<br>the<br>threshold<br>configured<br>with<br>the<br>CFG-NAVSPG<br>MAX_TIMETRUSTED_ACC message, the authTime flag is set to 1,<br>meaning time has been authenticated. |  |  |
| UBX-NAV-TIMEUTC              | Indicates if the parameters used to convert GNSS time into UTC time<br>have been authenticated.                                                                                                                                                                                                                                                         |  |  |
|                              | As the Galileo OSNMA protocol provides the data authentication<br>function only for the I/NAV message of the E1B signal, only UTC(EU) and<br>UTC(USNO) can be authenticated.                                                                                                                                                                            |  |  |

**Table 36: OSNMA verification messages**



# <span id="page-73-0"></span>**3.15 u-blox protocol feature descriptions**

### <span id="page-73-1"></span>**3.15.1 Broadcast navigation data**

This section describes the data reported via UBX-RXM-SFRBX.

UBX-RXM-SFRBX reports the broadcast navigation data message the receiver has collected from each tracked signal.When enabled, a separatemessage is generated each time the receiver decodes a complete subframe of data from a tracked signal. The data bits are reported as received, including preambles and error checking bits as appropriate. However, because there is considerable variation in the data structure of the different GNSS signals, the form of the reported data also varies. This document uses the term "subframe", but other GNSS data structures might use different terms, for example, GLONASS uses "strings" and Galileo uses "pages".

### **3.15.1.1 Parsing navigation data subframes**

Each UBX-RXM-SFRBX message contains a subframe of data bits appropriate for the relevant GNSS, delivered in a number of 32-bit words, as indicated by numWords field.

Due to the variation in data structure between different GNSS, the most important step in parsing a UBX-RXM-SFRBX message is to identify the form of the data. This should be done by reading the gnssId field, which indicates which GNSS the data was decoded from. In almost all cases, this is sufficient to indicate the structure. Because of this, the following sections are organized by GNSS. However, in some cases the identity of the GNSS is not sufficient, and this is described, where appropriate, in the following sections.

In most cases, the data does not map perfectly into a number of 32-bit words and, consequently, some of the words reported in UBX-RXM-SFRBX messages contain fields marked as "Pad". These fields should be ignored and no assumption should be made about their contents.

UBX-RXM-SFRBX messages are only generated when complete subframes are detected by the receiver and all appropriate parity checks have passed.

Where the parity checking algorithm requires data to be inverted before it is decoded (e.g. GPS L1C/A), the receiver carries this out before the message output. Therefore, users can process data directly and do not need to worry about repeating any parity processing.

The meaning of the content of each subframe depends on the sending GNSS and is described in the relevant interface control documents (ICD).

#### **3.15.1.2 GPS**

The data message structure in the GPS L1C/A (LNAV) and L2C/L5 (CNAV) signals is different and thus the UBX-RXM-SFRBX message structure differs as well. For the GPS L1C/A and L2C/L5 signals it is as follows:

#### **3.15.1.2.1 GPS L1C/A**

For GPS L1C/A signals, there is a fairly straightforward mapping between the reported subframe and the structure of subframe and words described in the GPS ICD. Each subframe comprises ten data words, which are reported in the same order they are received.

Each word is arranged as follows:



| <b>MSB</b> |               |                 | <b>LSB</b>       |
|------------|---------------|-----------------|------------------|
| to<br>10   | Pad<br>2 bits | Data<br>24 bits | Parity<br>6 bits |

#### **Figure 28: GPS L1C/A subframe word**

#### **3.15.1.2.2 GPS L2C**

For GPS L2C signals each reported subframe contains the CNAV message as described in the GPS ICD. The ten words are arranged as follows:



#### **Figure 29: GPS L2C subframe words**

#### **3.15.1.2.3 GPS L5**

For GPS L5 signals each reported subframe contains the CNAV message as described in the GPS ICD. The ten words are arranged as follows:





#### **Figure 30: GPS L5 subframe words**

#### **3.15.1.3 GLONASS**

For GLONASS L1OF signal, the UBX-RXM-SFRBX message contains a string content within the frame structure as described in the GLONASS ICD. This string comprises 85 data bits which are reported over three 32-bit words in the message. Data bits 1 to 8 are always a hamming code, while bits 81 to 84 are a string number and bit 85 is the idle chip, which should always have a value of zero. The meaning of other bits varies with string and frame number.

The fourth and final 32-bit word in the UBX-RXM-SFRBX message contains frame and superframe numbers (where available). These values are not actually transmitted by the satellites, but are deduced by the receiver and are included to aid decoding of the transmitted data. However, the receiver does not always know these values, in which case a value of zero is reported.

The four words are arranged as follows:





#### **Figure 31: GLONASS navigation message data**

In some circumstances, (especially on startup) the receiver may be able to decode data from a GLONASS satellite before it can identify it. When this occurs UBX-RXM-SFRBX messages will be issued with an svId of 255 to indicate "unknown".

#### **3.15.1.4 BeiDou**

For BeiDou signals there is a fairly straightforward mapping between the reported subframe and the structure of subframe and words described in the BeiDou ICD. Each subframe comprises ten data words, which are reported in the same order they are received.

Each word is arranged as follows:

| <b>MSB</b>      |               |                 | <b>LSB</b>       |
|-----------------|---------------|-----------------|------------------|
| $\frac{10}{10}$ | Pad<br>2 bits | Data<br>22 bits | Parity<br>8 bits |

#### **Figure 32: BeiDou subframe word**

Note that as the BeiDou data words only comprise 30 bits, the 2 most significant bits in each word reported by UBX-RXM-SFRBX are padding and should be ignored.

#### **3.15.1.5 Galileo**

The Galileo E1-B and E5b in-phase signals (ZED-F9P-01B\02B\04B\05B) transmit the I/NAV data message but in different configurations to enhance download time for dual frequency receivers. The Galileo E1-B and E5a signals (ZED-F9P-15B) transmit the I/NAV and F/NAV message respectively. The UBX-RXM-SFRBX structure for the I/NAV and F/NAV messages are shown below.



#### **3.15.1.5.1 Galileo E1-B**

For the Galileo E1-B signal, each reported subframe contains a pair of I/NAV pages as described in the Galileo ICD. Galileo pages can either be "Nominal" or "Alert" pages. For Galileo "Nominal" pages the eight words are arranged as follows:



**Figure 33: Galileo E1-B subframe words**



Alert pages are reported in very similar manner, but the page type bits will have value 1 and the structure of the eight words will be slightly different (as indicated by the Galileo ICD).

#### **3.15.1.5.2 Galileo E5b**

For the Galileo E5b in-phase signal data component, each reported subframe contains a pair of I/ NAV pages as described in the Galileo ICD. Galileo pages can either be "Nominal" or "Alert" pages. For Nominal pages the eight words are arranged as follows:



**Figure 34: Galileo E5b subframe words**



#### **3.15.1.5.3 Galileo E5a**

For the Galileo E5a in-phase signal data component, each reported subframe contains a number of F/NAV pages as described in the Galileo ICD. For each page the eight words are arranged as follows:



#### **Figure 35: Galileo E5a subframe words**

#### **3.15.1.6 SBAS**

For SBAS (L1C/A) signals each reported subframe contains eight 32-bit data words to deliver the 250 bits transmitted in each SBAS data block.

The eight words are arranged as follows:





#### **Figure 36: SBAS subframe words**

#### **3.15.1.7 QZSS**

The structure of the data delivered by QZSS L1C/A signals is effectively identical to that of GPS (L1C/A). Similarly the structure of the data delivered by the QZSS L2C signal is effectively identical to that of GPS (L2C). Similarly the structure of the data delivered by the QZSS L5 signal is effectively identical to that of GPS L5. Similarly the structure of the data delivered by the QZSS L1S signal is effectively identical to that of SBAS (L1C/A).

#### **3.15.1.8 Summary**

The following table gives a summary of the different data message formats reported by the UBX-RXM-SFRBX message:

| GNSS    | Signal | gnssId | sigId | numWords | period |  |
|---------|--------|--------|-------|----------|--------|--|
| GPS     | L1C/A  | 0      | 0     | 10       | 6s     |  |
| GPS     | L2CL   | 0      | 3     | 10       | 12s    |  |
| GPS     | L2CM   | 0      | 4     | 10       | 12s    |  |
| GPS     | L5 I   | 0      | 6     | 10       | 6s     |  |
| SBAS    | L1C/A  | 1      | 0     | 9        | 1s     |  |
| Galileo | E1 B   | 2      | 1     | 8        | 2s     |  |
| Galileo | E5b I  | 2      | 5     | 8        | 2s     |  |
| Galileo | E5a I  | 2      | 3     | 8        | 10s    |  |
| BeiDou  | B1I D1 | 3      | 0     | 10       | 6s     |  |
| BeiDou  | B1I D2 | 3      | 1     | 10       | 0.6s   |  |
| BeiDou  | B2I D1 | 3      | 2     | 10       | 6s     |  |
| BeiDou  | B2I D2 | 3      | 3     | 10       | 0.6s   |  |
| BeiDou  | B2a    | 3      | 7     | 9        | 3s     |  |
| QZSS    | L1C/A  | 5      | 0     | 10       | 6s     |  |
| QZSS    | L1S    | 5      | 1     | 9        | 1s     |  |
| QZSS    | L2CM   | 5      | 4     | 10       | 12s    |  |
| QZSS    | L2CL   | 5      | 5     | 10       | 12s    |  |



| GNSS    | Signal | gnssId | sigId | numWords | period |
|---------|--------|--------|-------|----------|--------|
| QZSS    | L5 I   | 5      | 8     | 10       | 6s     |
| GLONASS | L1OF   | 6      | 0     | 3        | 2s     |
| GLONASS | L2OF   | 6      | 2     | 3        | 2s     |
| NavIC   | L5 A   | 7      | 0     | 10       | 12s    |

**Table 37: Data message formats reported by UBX-RXM-SFRBX**

# <span id="page-81-0"></span>**3.16 Forcing a receiver reset**

Typically, in GNSS receivers, a distinction is made between cold, warm, and hot start, depending on the type of valid information the receiver has at the time of the restart.

- **Cold start:** In cold start mode, the receiver has no information from the last position (e.g. time, velocity, frequency etc.) at startup. Therefore, the receiver must search the full time and frequency space, and all possible satellite numbers. If a satellite signal is found, it is tracked to decode the ephemeris (18-36 seconds under strong signal conditions), whereas the other channels continue to search satellites. Once there is a sufficient number of satellites with valid ephemeris, the receiver can calculate position and velocity data. Other GNSS receiver manufacturers call this startup mode **Factory startup**.
- **Warm start:** In warm start mode, the receiver has approximate information for time, position, and coarse satellite position data (Almanac). In this mode, after power-up, the receiver normally needs to download ephemeris before it can calculate position and velocity data. As the ephemeris data usually is outdated after 4 hours, the receiver will typically start with a warm start if it has been powered down for more than 4 hours. In this scenario, several augmentations are possible. See Multiple GNSS [assistance.](#page-58-0)
- **Hot start:** In hot start mode, the receiver was powered down only for a short time (4 hours or less), so that its ephemeris is still valid. Since the receiver does not need to download ephemeris again, this is the fastest startup method.

Using the UBX-CFG-RST message, you can force the receiver to reset and clear data, in order to see the effects of maintaining/losing such data between restarts. For this, the UBX-CFG-RST message offers the navBbrMask field, where hot, warm and cold starts can be initiated, and also other combinations thereof.

The reset type can also be specified.This is not related to GNSS, but to the way the software restarts the system.

- **Hardware reset** uses the on-chip watchdog, to electrically reset the chip. This is an immediate, asynchronous reset. No Stop event is generated.
- **Controlled software reset** terminates all running processes in an orderly manner and, once the system is idle, restarts operation, reloads its configuration and starts to acquire and track GNSS satellites.
- **Controlled software reset (GNSS only)** only restarts the GNSS tasks, without reinitializing the full system or reloading any stored configuration.
- **Hardware reset (after shutdown)** uses the on-chip watchdog. This is a reset after shutdown.
- **Controlled GNSS stop** stops all GNSS tasks. The receiver will not be restarted, but will stop any GNSS-related processing.
- **Controlled GNSS start** starts all GNSS tasks.

## <span id="page-81-1"></span>**3.17 Firmware upload**

ZED-F9P is supplied with firmware. u-blox may release updated images containing, for example, security fixes, enhancements, bug fixes, etc. Therefore it is important that customers implement a firmware update mechanism in their system.



A firmware image is a binary file containing the software to be run by the GNSS receiver. A firmware update is the process of transferring a firmware image to the receiver and storing it in non-volatile flash memory.

Contact u-blox for more information on firmware update.

## <span id="page-82-0"></span>**3.18 Spectrum analyzer**

Supported from firmware version HPG 1.13 onwards

The UBX-MON-SPAN message provides a low-resolution RF spectrum analyzer function sufficient to identify noise or jammers in the receiver's reception band(s). It can be used for monitoring potential interferers during customer integration and in normal operation to identify interference, e.g. when the UBX-SEC-SIG or UBX-MON-RF message detects a possible jamming threat. See [Jamming/interference](#page-68-1) indicator for more details. u-center provides a visualization of the message spectrum output(s) with features for max-hold and averaging.

This message is intended for comparative analysis of the RF spectrum rather than absolute and precise measurement.

The message is output once per second when enabled. Depending on the receiver type, one or two measurement blocks will be output, indicated by the numRfBlocks flag field. The first block provides L1 spectrum data which can be followed by an L2 or L5 block with multi-band receivers.

Each block comprises the following data:

- 256 spectrum data points (0.25 dB units)
- Spectrum span (Hz)
- Spectrum bin resolution (Hz)
- Center frequency (Hz)
- PGA setting (dB)

The frequency of each point can be calculated by Freq(i) = center frequency + spectrum span \* (i-128) / 256, where i=0-255. The number of points = span/resolution and is scaled in units of 0.25 dB. Changes in the PGA gain value can indicate an increased input in RF signal activity compared to normal operation.

[Figure](#page-83-2) 37 shows the spectrum view in u-center with the view/hold option selected. The red line represents the frozen spectrum before modifying the external gain, while the black line represents the current measurement.



<span id="page-83-2"></span>

**Figure 37: Spectrum analyzer view in u-center with the option view/hold selected**

- The span frequency depends on the number of constellations enabled which impacts the spectrum resolution owing to a fixed set of points. For further details about this message see the Interface description [\[2\]](#page-126-1).
- A spur may be visible at the center frequency, this comes internally from the receiver and does not cause any performance degradation.

# <span id="page-83-0"></span>**3.19 Production test**

u-blox focuses on high quality for its products. To achieve this, we only supply fully tested units. At the end of the production process, every unit is tested. Defective units are analyzed in detail to continuously improve the production quality.

This is achieved with automatic test equipment, which delivers a detailed test report for each unit. The following measurements are done:

- Digital self-test (software download, verification of FLASH firmware, etc.)
- Measurement of voltages and currents
- Measurement of RF characteristics (e.g. C/No)

Thanks to the 100 % test coverage done by u-blox, the OEM manufacturer doesn't need to repeat firmware tests or measurements of the GNSS parameters/characteristics (e.g. TTFF) in the production test.

The OEM manufacturer can focus on testing:

- Overall sensitivity of the device (including antenna, if applicable)
- Communication to a host controller

### <span id="page-83-1"></span>**3.19.1 Connected sensitivity test**

The best way to test the sensitivity of a positioning device is with the use of a GNSS simulator. It assures reliable and constant signals at every measurement.

Guidelines for sensitivity tests:

- Connect a GNSS simulator to the OEM product
- Choose the power level in a way that the "Golden Device" would report a C/No ratio of 38-40 dBHz
- Power up the DUT (Device Under Test) and allow enough time for the acquisition



- Read the C/No value from the NMEA GSV or the UBX-NAV-SAT message (e.g. with u-center)
- Compare the results to a "Golden Device", a u-blox Evaluation Kit or Application Board.

### <span id="page-84-0"></span>**3.19.2 Go/No go tests for integrated devices**

- For best results, place the device in an outdoor position with excellent sky view (HDOP < 3.0).
- Let the receiver acquire satellites and compare the signal strength with a "Golden Device". As the electro-magnetic field of a redistribution antenna is not homogenous, indoor tests are not reliable in most cases.

These kinds of tests are useful as a go/no go test but not for sensitivity measurements.



# <span id="page-85-0"></span>**4 Design**

This section provides information to help carry out a successful schematic and PCB design integrating the ZED-F9P.

Do not load Pin 4 (ANT\_DETECT) with a capacitance more than 1 nF.

## <span id="page-85-1"></span>**4.1 Pin assignment**

The pin assignment of the ZED-F9P module is shown in [Figure](#page-85-2) 38. The defined configuration of the PIOs is listed in [Table](#page-85-3) 38.

ZED-F9P is an LGA package with the I/O on the outside edge and central ground pads.

<span id="page-85-2"></span>

#### **Figure 38: ZED-F9P pin assignment**

<span id="page-85-3"></span>

| Pin no. | Name        | I/O | Description                                      |  |
|---------|-------------|-----|--------------------------------------------------|--|
| 1       | GND         | -   | Ground                                           |  |
| 2       | RF_IN       | I   | RF input                                         |  |
| 3       | GND         | -   | Ground                                           |  |
| 4       | ANT_DETECT  | I   | Active antenna detect - default active high      |  |
| 5       | ANT_OFF     | O   | External LNA disable - default active high       |  |
| 6       | ANT_SHORT_N | I   | Active antenna short detect - default active low |  |
| 7       | VCC_RF      | O   | Voltage for external LNA                         |  |



| Pin no. | Name           | I/O | Description                                                   |
|---------|----------------|-----|---------------------------------------------------------------|
| 8       | Reserved       | -   | Reserved                                                      |
| 9       | Reserved       | -   | Reserved                                                      |
| 10      | Reserved       | -   | Reserved                                                      |
| 11      | Reserved       | -   | Reserved                                                      |
| 12      | GND            | -   | Ground                                                        |
| 13      | Reserved       | -   | Reserved                                                      |
| 14      | GND            | -   | Ground                                                        |
| 15      | Reserved       | -   | Reserved                                                      |
| 16      | Reserved       | -   | Reserved                                                      |
| 17      | Reserved       | -   | Reserved                                                      |
| 18      | Reserved       | -   | Reserved                                                      |
| 19      | GEOFENCE_STAT  | O   | Geofence status, user defined                                 |
| 20      | RTK_STAT       | O   | RTK status:                                                   |
|         |                |     | 0 = RTK/PPP-RTK fixed                                         |
|         |                |     | blinking = receiving and using corrections                    |
|         |                |     | 1 = no corrections                                            |
| 21      | Reserved       | -   | Reserved                                                      |
| 22      | Reserved       | -   | Reserved                                                      |
| 23      | Reserved       | -   | Reserved                                                      |
| 24      | Reserved       | -   | Reserved                                                      |
| 25      | Reserved       | -   | Reserved                                                      |
| 26      | RXD2           | I   | Correction UART input                                         |
| 27      | TXD2           | O   | Correction UART output                                        |
| 28      | Reserved       | -   | Reserved                                                      |
| 29      | Reserved       | -   | Reserved                                                      |
| 30      | Reserved       | -   | Reserved                                                      |
| 31      | Reserved       | -   | Reserved                                                      |
| 32      | GND            | -   | Ground                                                        |
| 33      | VCC            | I   | Voltage supply                                                |
| 34      | VCC            | I   | Voltage supply                                                |
| 35      | Reserved       | -   | Reserved                                                      |
| 36      | V_BCKP         | I   | Backup supply voltage                                         |
| 37      | GND            | -   | Ground                                                        |
| 38      | V_USB          | I   | USB supply                                                    |
| 39      | USB_DM         | I/O | USB data                                                      |
| 40      | USB_DP         | I/O | USB data                                                      |
| 41      | GND            | -   | Ground                                                        |
| 42      | TXD / SPI_SDO  | O   | Host UART output if D_SEL = 1(or open). SPI_SDO if D_SEL = 0  |
| 43      | RXD / SPI_SDI  | I   | Host UART input if D_SEL = 1(or open). SPI_SDI if D_SEL = 0   |
| 44      | SDA / SPI_CS_N | I/O | I2C Data if D_SEL = 1 (or open). SPI Chip Select if D_SEL = 0 |
| 45      | SCL / SPI_CLK  | I/O | I2C Clock if D_SEL = 1(or open). SPI Clock if D_SEL = 0       |
| 46      | TX_READY       | O   | TX_Buffer full and ready for TX of data                       |
| 47      | D_SEL          | I   | Interface select for pins 42-45                               |
| 48      | GND            | -   | Ground                                                        |



| Pin no. | Name       | I/O | Description                                                              |  |
|---------|------------|-----|--------------------------------------------------------------------------|--|
| 49      | RESET_N    | I   | RESET_N                                                                  |  |
| 50      | SAFEBOOT_N | I   | SAFEBOOT_N (for future service, updates and reconfiguration, leave OPEN) |  |
| 51      | EXTINT     | I   | External interrupt pin                                                   |  |
| 52      | Reserved   | -   | Reserved                                                                 |  |
| 53      | TIMEPULSE  | O   | Time pulse                                                               |  |
| 54      | Reserved   | -   | Reserved                                                                 |  |

**Table 38: ZED-F9P pin assignment**

# <span id="page-87-0"></span>**4.2 Power supply**

The u-blox ZED-F9P module has three power supply pins: VCC, V\_BCKP and V\_USB.

### <span id="page-87-1"></span>**4.2.1 VCC: Main supply voltage**

The **VCC** pin is connected to the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude. For this reason, it is important that the supply circuitry be able to support the peak power for a short time (see the applicable data sheet [\[1](#page-126-3)] for specification).

The module integrates a DC/DC converter, which allows reduced power consumption.

- When switching from backup mode to normal operation or at startup, u-blox ZED-F9P modules must charge the internal capacitors in the core domain. In certain situations, this can result in a significant current draw. For low-power applications using backup mode, it is important that the power supply or low ESR capacitors at the module input can deliver this current/charge.
- To reduce peak current during power on, users can employ an LDO that has a built-in current limiter.
- Do not add any series resistance greater than 0.2 Ω to the VCC supply as it will generate input voltage noise due to dynamic current conditions.
- For the ZED-F9P module the equipment must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1.

### <span id="page-87-2"></span>**4.2.2 V\_BCKP: Backup supply voltage**

The V\_BCKP pin can be used to provide power to maintain the real-time clock (RTC) and batterybacked RAM (BBR) when VCC is removed.

If the module supply has a power failure, the **V\_BCKP** pin supplies the real-time clock (RTC) and battery-backed RAM (BBR). Use of valid time and the GNSS orbit data at start up will improve the GNSS performance, as with hot starts and warm starts.

If V\_BCKP is not provided, the module performs a cold start at power up.

If a host is connected to ZED-F9P, V\_BCKP can be partially emulated by using UBX-UPD-SOS functionality. BBR data can saved to the host and restored at startup. See the applicable [Interface](#page-126-1) [description](#page-126-1) for more information.

- Avoid high resistance on the **V\_BCKP** line: During the switch from main supply to backup supply, a short current adjustment peak can cause a high voltage drop on the pin with possible malfunctions.
- Add a 2 uF capacitor on the V\_BCKP pin to absorb the current adjustment peak when switching from VCC to V\_BCKP supply.
- If no backup supply voltage is available, connect the **V\_BCKP** pin to **VCC**.





Allow all I/O including UART and other interfaces to float or connect to a high impedance in HW backup mode (V\_BCKP supplied when VCC is removed). See the [Interfaces](#page-53-0) section.

#### **Real-time clock (RTC)**

The real-time clock (RTC) is driven by a 32-kHz oscillator using an RTC crystal. If VCC is removed while a battery is connected to **V\_BCKP**, most of the receiver is switched off leaving the RTC and BBR powered. This operating mode is called Hardware Backup Mode which enables time keeping and all relevant data to be saved to allow a hot or warm start.

### <span id="page-88-0"></span>**4.2.3 ZED-F9P power supply**

The ZED-F9P requires a low-noise, low-dropout voltage, and a very low source impedance power supply of 3.3 V typically. No inductors or ferrite beads should be used from LDO to the module VCC pin. The peak currents need to be taken into account for the source supplying the LDO for the module.

A power supply fed by 5 V is shown in the figure below. This example circuit is intended only for the module supply.



**Figure 39: ZED-F9P power supply**

# <span id="page-88-1"></span>**4.3 ZED-F9P minimal design**

The minimal electrical circuit for ZED-F9P operation using the UART1 interface is shown in [Figure](#page-89-1) [40](#page-89-1) below.



<span id="page-89-1"></span>

#### **Figure 40: Minimal ZED-F9P design**

For a minimal design with the ZED-F9P GNSS modules, the following functions and pins should be considered:

- Connect the power supply to VCC and V\_BCKP.
- If hot or warm start operations are needed, connect a backup battery to V\_BCKP.
- If USB is not used connect V\_USB to ground.
- Ensure an optimal ground connection to all ground pins of the ZED-F9P GNSS module.
- If antenna bias is required, see ZED-F9P [antenna](#page-0-0) bias section.

The host interface typically supplies the RTCM messages required for RTK operation.

# <span id="page-89-0"></span>**4.4 Antenna**

The ZED-F9P requires an active antenna with an integrated LNA to ensure good performance under nominal signal reception.

When implementing a custom antenna installation, it is recommended that an OEM active antenna module be used that meets our specification. Implementing a custom active antenna design is an important exercise to meet the required bandwidths and group delay specifications compared to previous L1-only designs.

A typical dual band antenna design block diagram is shown below taken from the u-blox ANN-MB active antenna product.





#### **Figure 41: u-blox low cost dual-band antenna internal structure**

A suitable ground plane is required for the antenna to achieve good performance.

Location of the antenna is critical to reach the stated performance. Unsuitable locations within a vehicle could include, under vehicle dash, rear-view mirror location, etc.

A set of recommended specifications for a dual band active antenna is given below.

| Parameter                           | Specification                                                                         |                               |
|-------------------------------------|---------------------------------------------------------------------------------------|-------------------------------|
|                                     | Minimum gain15                                                                        | 17 dB                         |
| Active antenna recommendations      | 15<br>Maximum gain                                                                    | 50 dB                         |
|                                     | Noise figure                                                                          | <4 dB                         |
| 16<br>Group delay variation in-band | 10 ns max at each GNSS system bandwidth.<br>Note: Inter-signal requirement 50 ns max. |                               |
| Out-of-band rejection               | 40 dB typ                                                                             |                               |
|                                     | 17<br>L1 band antenna gain                                                            | 1559 - 1606 MHz: 3 dBic typ.  |
|                                     | 17<br>L2/E5b band antenna gain                                                        | 1197 - 1249 MHz: 2 dBic typ.  |
| Antenna element specification       | 17<br>L5/E5a band antenna gain                                                        | 1164 - 1188 MHz: 2 dBic typ.  |
|                                     | Polarization                                                                          | RHCP                          |
|                                     | Axial ratio                                                                           | 2 dB max, at Zenith           |
|                                     | Phase center variation                                                                | <10 mm over elevation/azimuth |
| 18<br>EMI immunity out-of-band      | 30 V/m                                                                                |                               |
| ESD circuit protection              | 15 kV human body model air discharge                                                  |                               |
|                                     |                                                                                       |                               |

**Table 39: Antenna specifications for ZED-F9P modules**

<span id="page-90-0"></span><sup>15</sup> Including passive losses (filters, cables, connectors etc.)

<span id="page-90-1"></span><sup>16</sup> GNSS system bandwidths: **ZED-F9P-01B\02B\04B\05B:** B1I 1559…1563 MHz; L1,E1,B1C 1573…1578 MHz; L1OF 1598…1606 MHz; E5b,B2I 1192…1212 MHz; L2C 1223…1231 MHz; L2OF 1242…1249 MHz

**ZED-F9P-15B:**B1I 1559…1563 MHz; L1,E1,B1C 1573…1578 MHz; L1OF 1598…1606 MHz; L5,E5a,B2a 1166…1286 MHz

B1I 1559…1563 MHz; L1,E1,B1C 1573…1578 MHz;E5b,B2I 1192…1212 MHz; L2C 1223…1231 MHz; L5,E5a,B2a 1166… 1286 MHz

<span id="page-90-2"></span><sup>17</sup> Measured with a ground plane d=150 mm

<span id="page-90-3"></span><sup>18</sup> Exception L1,L2 ,L5 bands +/- 200 MHz, emphasis on cellular bands



The antenna system should include filtering to ensure adequate protection from nearby transmitters. Take care in the selection of antennas placed close to cellular or Wi-Fi transmitting antennas.

### <span id="page-91-0"></span>**4.4.1 Active Antenna Power Supply**

The antenna power supply is typically used to power GNSS active antennas. The power supply should be able to provide the correct voltage and current to the antenna to ensure optimal performance of ZED-F9P.

To power and limit the current to the antenna, you have the following options:

- [External](#page-91-1) power supply
- [External](#page-92-0) power supply and current limiting
- [VCC\\_RF](#page-93-0) power supply

The diagram shows the Z impedance of the antenna bias L4 inductor. This inductor is found in all the reference circuits mentioned in the subsequent sections. It is important for the Z impedance to be greater than 500 Ω within the 1–1.8 GHz frequency range. This impedance ensures efficient blocking of RF signals from reaching the power supply.



**Figure 42: ZED-F9P antenna bias inductor impedance**

#### <span id="page-91-1"></span>**4.4.1.1 External power supply**

[Figure](#page-92-1) 43 shows an example with an external filtered supply V\_ANT 3.3 V. Consider the power dissipation in both the resistor and inductor based on the supply voltage and short circuit current. Calculate the current capacity of the bias-T inductor and the value of the bias resistor. Include the supply voltage and its current capacity for the bias-T in the calculation.



<span id="page-92-1"></span>

**Figure 43: ZED-F9P with external voltage antenna bias**

| Part | Specifications                                                            | Values        |
|------|---------------------------------------------------------------------------|---------------|
| C22  | Filtering capacitor                                                       | 100 nF, 16 V  |
| FB1  | Ferrite bead                                                              | BLM15HB121SH1 |
| L4   | Minimum Current of 300 mA or more impedance >500<br>Ω at GNSS frequencies | LQG15HS47NJ02 |
| R19  | Current limit resistor                                                    | 10 Ω          |

**Table 40: ZED-F9P external voltage antenna bias components**

#### <span id="page-92-0"></span>**4.4.1.2 External power supply and current limiting**

[Figure](#page-93-1) 44 shows an example with an external voltage V\_ANT 3.3 V. In this example, the current limiting threshold is set at 60 mA and the use of ferrite bead is recommended.

Note that active antennas typically draw 5–20 mA current, contributing to the overall power consumption of the system.



<span id="page-93-1"></span>

#### **Figure 44: ZED-F9P with external voltage antenna bias and current limit circuit**

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

#### **Table 41: ZED-F9P antenna bias components**

#### <span id="page-93-0"></span>**4.4.1.3 VCC\_RF power supply**

When using the VCC\_RF supply pin from ZED-F9P:

- Limit the current to a maximum of 300 mA at the module supply voltage under short circuit conditions, requiring a 10 Ω resistor for a 3 V module supply.
- The bias-T inductor's DC resistance is assumed to be 1–2 Ω, and the module's internal feed inductor is assumed to be 1.2 Ω.





#### **Figure 45: ZED-F9P VCC\_RF antenna bias**

| Part | Specifications                                                            | Values        |
|------|---------------------------------------------------------------------------|---------------|
| C22  | Filtering capacitor                                                       | 100 nF, 16 V  |
| FB1  | Ferrite bead                                                              | BLM15HB121SH1 |
| L4   | Minimum Current of 300 mA or more impedance >500<br>Ω at GNSS frequencies | LQG15HS47NJ02 |
| R19  | Current limit resistor                                                    | 10 Ω          |
|      |                                                                           |               |

**Table 42: ZED-F9P VCC\_RF antenna bias components**

### <span id="page-94-0"></span>**4.4.2 Antenna supervisor circuit**

The active antenna supervisor circuit connects to three ZED-F9P pins:

- ANT\_OFF
- ANT\_DETECT
- ANT\_SHORT\_N

For example the antenna opencircuitdetectionismadeusing ANT\_DETpin. A "high" at ANT\_DETpin indicates an antenna is detected (antenna consumes current) and a "low" at ANT\_DET pin indicates an antenna is not detected (no current drawn).

The following schematic details the required circuit:





#### **Figure 46: ZED-F9P antenna supervisor circuit**

The bias-T inductor L4 should support multi-band operation within the 1–1.8 GHz frequency range. For additional information, see Active [Antenna](#page-91-0) Power Supply section.

| Part       | Specifications                                                          |
|------------|-------------------------------------------------------------------------|
| C14        | Filtering capacitor                                                     |
| L4         | Minimum Current of 300 mA or more. Impedance >500 Ω at GNSS frequencies |
| R7         | Passive pull-up to control T5                                           |
| R8         | Current limiter in the event of a short circuit                         |
| R9         | Defines the threshold of the comparator                                 |
| R10        | Defines the threshold of the comparator                                 |
| T5         | P-FET transistor acting as a switch to control the antenna supply       |
| U3, U7, U8 | Open drain buffer to shift voltage levels                               |
| U6         | Comparator (op-amp)                                                     |
|            |                                                                         |

**Table 43: Antenna supervisor components**

- Buffers U3, U7 and U8 are optional depending on the application.They are not needed if the VCC\_RF pin is used.
- An open drain buffer is recommended in case the antenna is supplied while the module is not, since IO pins must not be driven. If the antenna operates at a higher voltage like 5 V or 12 V, use of the buffer is also recommended.



# <span id="page-96-0"></span>**4.5 EOS/ESD precautions**

- To avoid overstress damage during production or in the field it is essential to observe strict EOS/ ESD/EMI handling and protection measures.
- To prevent overstress damage at the RF\_IN of your receiver, never exceed the maximum input power as specified in the applicable Data sheet [\[1\]](#page-126-3).

When integrating GNSS receivers into wireless systems, pay special attention to electromagnetic and voltage susceptibility issues. Wireless systems include components which can produce Electrostatic Discharge (ESD), Electrical Overstress (EOS) and Electro-Magnetic Interference (EMI). CMOS devices are more sensitive to such influences because their failure mechanism is defined by the applied voltage, whereas bipolar semiconductors are more susceptible to thermal overstress. The following design guidelines help in designing robust yet cost-effective solutions.

### <span id="page-96-1"></span>**4.5.1 ESD protection measures**

GNSS receivers are sensitive to Electrostatic Discharge (ESD). Special precautions are required when handling. Most defects caused by ESD can be prevented by following strict ESD protection rules for production and handling. When implementing passive antenna patches or external antenna connection points, then additional ESD measures as shown in the figure below can also avoid failures in the field.





### <span id="page-96-2"></span>**4.5.2 EOS precautions**

Electrical overstress (EOS) usually describes situations when the maximum input power exceeds the maximum specified ratings. EOS failure can happen if RF emitters are close to a GNSS receiver or its antenna. EOS causes damage to the chip structures. If the RF\_IN is damaged by EOS, it is hard to determine whether the chip structures have been damaged by ESD or EOS.

EOS protection measures as shown in the figure below are recommended for any designs combining wireless communication transceivers (e.g. GSM, GPRS) and GNSS in the same design or in close proximity.





**Figure 48: Active antenna EOS protection**

### <span id="page-97-0"></span>**4.5.3 Safety precautions**

The ZED-F9P must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1. In addition to external limited power source, only Separated or Safety Extra-Low Voltage (SELV) circuits are to be connected to the module including interfaces and antennas.

For more information about SELV circuits see section 2.2 in Safety standard IEC 60950-1.

# <span id="page-97-1"></span>**4.6 Electromagnetic interference on I/O lines**

Any I/O signal line with a length greater than approximately 3 mm can act as an antenna and may pick up arbitrary RF signals transferring them as noise into the receiver. This specifically applies to unshielded lines, in which the corresponding GND layer is remote or missing entirely, and lines close to the edges of the printed circuit board.

If, for example, a cellular signal radiates into an unshielded high-impedance line, it is possible to generate noise in the order of volts and not only distort receiver operation but also damage it permanently. Another type of interference can be caused by noise generated at the PIO pins that emits from unshielded I/O lines. Receiver performance may be degraded when this noise is coupled into the GNSS antenna.

EMI protection measures are particularly useful when RF emitting devices are placed next to the GNSS receiver and/or to minimize the risk of EMI degradation due to self-jamming. An adequate layout with a robust grounding concept is essential in order to protect against EMI.

Intended Use: Inorder tomitigate any performance degradationof a radio equipment underEMC disturbance, system integration shall adopt appropriate EMC design practice and not contain cables over three meters on signal and supply ports.

### <span id="page-97-2"></span>**4.6.1 General notes on interference issues**

Received GNSSsignalpower at the antenna is very low. At thenominal receivedsignal strength(-128 dBm) it is below the thermal noise floor of -111 dBm. Due to this fact, a GNSS receiver is susceptible to interference from nearby RF sources of any kind. Two cases can be distinguished:

• Out-of-band interference: Typically any kind of wireless communications system (e.g. LTE, GSM, CDMA, 3G, WLAN, Bluetooth, etc.) may emit its specified maximum transmit power in close proximity to the GNSS receiving antenna, especially if such a system is integrated with the GNSS receiver. Even at reasonable antenna selectivity, destructive power levels may reach the RF input of the GNSS receiver. Also, larger signal interferers may generate intermodulation products inside the GNSS receiver front-end that fall into the GNSS band and contribute to inband interference.



• In-band interference: Although the GNSS band is kept free from intentional RF signal sources by radio-communications standards, many devices emit RF power into the GNSS band at levels much higher than the GNSS signal itself. One reason is that the frequency band above 1 GHz is not well regulated with regards to EMI, and even if permitted, signal levels are much higher than GNSS signal power. Notably, all types of digital equipment, such as PCs, digital cameras, LCD screens, etc. tend to emit a broad frequency spectrum up to several GHz of frequency. Also wireless transmitters may generate spurious emissions that fall into GNSS band.

As an example, GSM uses power levels of up to 2 W (+33 dBm). The absolute maximum power input at the RF input of the GNSS receiver can be +15 dBm. The GSM specification allows spurious emissions for GSM transmitters of up to +36 dBm, while the GNSS signal is less than -128 dBm. By simply comparing these numbers it is obvious that interference issues must be seriously considered in any design of a GNSS receiver. Different design goals may be achieved through different implementations:

- The primary focus is to prevent damaging the receiver from large input signals. Here the GNSS performance under interference conditions is not important and suppression of the signal is permitted. It is sufficient to just observe the maximum RF power ratings of all of the components in the RF input path.
- GNSS performance must be guaranteed even under interference conditions. In such a case, not only the maximum power ratings of the components in the receiver RF path must be observed. Further, non-linear effects like gain compression, NF degradation (desensitization) and intermodulation must be analyzed.
- Pulsed interference with a low-duty cycle such as GSM may be destructive due to the high peak power levels.

### <span id="page-98-0"></span>**4.6.2 In-band interference mitigation**

With in-band interference, the signal frequency is very close to the GNSS frequency. Such interference signals are typically caused by harmonics fromdisplays,micro-controller operation, bus systems, etc. Measures against in-band interference include:

- Maintaining a good grounding concept in the design
- Shielding
- Layout optimization
- Low-pass filtering of noise sources, e.g. digital signal lines
- Remote placement of the GNSS antenna, far away from noise sources
- Adding an LTE, CDMA, GSM, WCDMA, BT band-pass filter before antenna

### <span id="page-98-1"></span>**4.6.3 Out-of-band interference**

Out-of-band interference is caused by signal frequencies that are different from the GNSS carrier frequency. The main sources are wireless communication systems such as LTE, GSM, CDMA, WCDMA, Wi-Fi, BT, etc.

Measures against out-of-band interference include maintaining a good grounding concept in the design and adding a GNSS band-pass filter into the antenna input line to the receiver.

For GSM applications, such as typical handset design, an isolation of approximately 20 dB can be reached with careful placement of the antennas. If this is insufficient, an additional SAW filter is required on the GNSS receiver input to block the remaining GSM transmitter energy.



# <span id="page-99-0"></span>**4.7 Layout**

This section details layout and placement requirements of the ZED-F9P high precision receiver.

### <span id="page-99-1"></span>**4.7.1 Placement**

GNSS signals at the surface of the Earth are below the thermal noise floor. A very important factor in achieving maximum GNSS performance is the placement of the receiver on the PCB. The placement used may affect RF signal loss from antenna to receiver input and enable interference into the sensitive parts of the receiver chain, including the antenna itself. When defining a GNSS receiver layout, the placement of the antenna with respect to the receiver, as well as grounding, shielding and interference from other digital devices are crucial issues and need to be considered very carefully.

Signal loss on the RF connection from antenna to receiver input must be minimized as much as possible. Hence, the connection to the antenna must be kept as short as possible.

Ensure that RF critical circuits are clearly separated from any other digital circuits on the system board. To achieve this, position digital part of the receiver close to the digital section of the system PCB and place the RF section and antenna as far away from the other digital circuits on the board as possible.

A proper GND concept shall be followed: the RF section shall not be subject to noisy digital supply currents running through its GND plane.

### <span id="page-99-2"></span>**4.7.2 Thermal management**

During the design-in, do not place the receiver near sources of heating or cooling. The receiver oscillator is sensitive to sudden changes in ambient temperature which can adversely impact satellite signal tracking. Sources can include co-located power devices, cooling fans or thermal conduction via the PCB. Take the following questions into account when designing in the receiver.

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?
- High temperature drift and air vents can affect the GNSS performance. For best performance, avoid high temperature drift and air vents near the receiver.

### <span id="page-99-3"></span>**4.7.3 Package footprint, copper and paste mask**

This section provides recommendations for copper and solder mask dimensioning for the ZED-F9P module packages.

- These are recommendations only and not specifications. The exact copper, solder and paste mask geometries, distances, stencil thickness and solder paste volumes must be adapted to the specific production processes (e.g. soldering etc.).
- PIN 1 indicator is the ground opening, do not route any signal below this pad.

Refer to the applicable Data sheet [\[1\]](#page-126-3) for the mechanical dimensions.



#### **4.7.3.1 Footprint**



#### **Figure 49: ZED-F9P suggested footprint (i.e. copper mask)**

| Dimension (mm) | Symbol | Dimension (mm) |
|----------------|--------|----------------|
| 23.00          | B      | 17.40          |
| 1.50           | D      | 0.80           |
| 1.10           | F      | 2.10           |
| 1.10           | H      | 1.05           |
| 0.55           | J      | 9.95           |
| 7.45           | L      | 0.85           |
| 2.80           | N      | 0.20           |
| 1.35           | P      | 1.20           |
| 0.30           | -      | -              |
|                |        |                |

**Table 44: ZED-F9P footprint dimensions**



#### **4.7.3.2 Paste mask**



#### **Figure 50: ZED-F9P suggested paste mask**

| Symbol | Dimension (mm) | Symbol | Dimension (mm) |
|--------|----------------|--------|----------------|
| C      | 1.55           | D      | 0.75           |
| E      | 1.05           | F      | 2.10           |
| G      | 1.10           | H      | 1.05           |
| I      | 0.55           | J      | 10.00          |
| K      | 7.50           | L      | 0.90           |
| M      | 2.85           | N      | 0.20           |
| O      | 1.35           | -      | -              |

**Table 45: ZED-F9P paste mask dimensions**

### <span id="page-101-0"></span>**4.7.4 Layout guidance**

The presented layout guidance reduces the risk of performance issues at design level.

#### **4.7.4.1 RF In trace**

The RF in trace has to work in the combined GNSS signal bands.

For FR-4 PCB material with a dielectric permittivity of for example 4.7, the trace width for the 50 Ω line impedance can be calculated.



A grounded co-planar RF trace is recommended as it provides the maximum shielding from noise with adequate vias to the ground layer.

The RF trace must be shielded by vias to ground along the entire length of the trace and the ZED-F9P RF\_IN pad should be surrounded by vias as shown in the figure below.



**Figure 51: RF input trace**

The RF\_IN trace on the top layer should be referenced to a suitable ground layer.

#### **4.7.4.2 Vias for the ground pads**

The ground pads under the ZED-F9P high precision receiver need to be grounded with vias to the lower ground layer of the PCB. A solid ground layer fill on the top layer of the PCB is recommended. This is shown in the figure below.



**Figure 52: Top layer fill and vias**



### **4.7.4.3 VCC pads**

The VCC pads for the ZED-F9P high precision receiver must have as low impedance as possible with large vias to the lower power layer of the PCB. The VCC pads need a large combined pad and the decoupling capacitors must be placed as close as possible. This is shown in the figure below.



**Figure 53: VCC pads**

# <span id="page-103-0"></span>**4.8 Design guidance**

### <span id="page-103-1"></span>**4.8.1 General considerations**

Do not load Pin 4 (ANT\_DETECT) with a capacitance more than 1 nF.

Check power supply requirements and schematic:

- Is the power supply voltage within the specified range and noise-free?
- If USB is not used, connect the V\_USB pin to ground.
- It is recommended to have a separate LDO for V\_USB that is enabled by the module VCC. This is to comply with the USB self-powered specification.
- If USB is used, is there a 1 uF capacitor right near the V\_USB pin? This is just for the V\_USB pin.
- Is there a 1 uF cap right next to the module VCC pin?
- Compare the peak current consumption of the ZED-F9P GNSS module with the specification of your power supply.
- GNSS receivers require a stable power supply. Avoid series resistance (less than 0.2 Ω) in your power supply line (the line to VCC) to minimize the voltage ripple on VCC. See the ZED-F9P Power [supply](#page-87-0) section in the [Design](#page-85-0) chapter for more information on the power supply requirements.
- Allow all I/O to Float/High impedance (High-Z) when VCC is not applied.

### <span id="page-103-2"></span>**4.8.2 Backup battery**

Check backup supply requirements and schematic:

- For achieving a minimal time to first fix (TTFF) after a power down (warm starts, hot starts), make sure to connect a backup battery to V\_BCKP.
- Verify that your battery backup supply can provide the battery backup current specified in the applicable data sheet.



• Allow all I/O including UART and other interfaces to Float/High impedance in HW backup mode (battery backup connected with VCC removed).

### <span id="page-104-0"></span>**4.8.3 RF front-end circuit options**

It is important that the RF input is fed by an active antenna meeting the requirements for the ZED-F9P.

The first stages of the signal processing chain are crucial to the overall receiver performance.

When an RF input connector is employed this can provide a conduction path for harmful or destructive electrical signals. If this is a likely factor the RF input should be protected accordingly.

#### **Additional points on the RF input**

- What is the expected quality of the signal source (antenna)?
- What is the external active antenna signal power?
- What is the bandwidth and filtering of the external active antenna?
- Does the external antenna and filtering components meet the group delay variation requirements? This is critical for high accuracy applications such as RTK and timing.

Are destructive RF power levels expected to reach the RF input? Is interference from wireless transmitters expected?

- What are the characteristics of these signals (duty cycle, frequency range, power range, spectral purity)?
- What is the expected GNSS performance under interference conditions?

Is there a risk of RF input exposure to excessive ESD stress?

- In the field: Can the user access the antenna connector?
- PCB / system assembly: Is there risk that statically charged parts (e.g. patch antennas) may be discharged through the RF input?

The following subsections provide several options addressing the various questions above:

- In some applications, such as cellular transceivers, interference signals may exceed the maximum power rating of the RF\_IN input. To avoid device destruction use of external input protection is mandatory.
- During assembly of end-user devices which contain passive patch antennas, an ESD discharge may occur during production when pre-charged antennas are soldered to the GNSS receiver board. In such cases, use of external protection in front of RF\_IN is mandatory to avoid device destruction.

ESD discharge cannot be avoided during assembly and / or field use. Note that SAW filters are susceptible to ESD damage. To provide additional robustness an ESD protection diode may be placed at the antenna RF connector to GND.

### <span id="page-104-1"></span>**4.8.4 Antenna/RF input**

Check RF input requirements and schematic:

- An OEM active antenna module that meets our requirements should be used if there is a need to integrate the antenna.
- The total maximum noise figure including external LNA (or the LNA in the active antenna) should be around 3 dB.
- Ensure active antenna gain is ideally between 30 40 dB gain.
- Make sure the antenna is not placed close to noisy parts of the circuitry and does not face any other noisy elements (for example microcontroller, display).



- Signal levels above 40 C/N0 average are required for optimal RTK performance.
- If a patch type antenna is used, an antenna ground plane with minimum 100 150 mm diameter is required.
- Ensure antenna supports both L1 and L2 bands for ZED-F9P-01B\02B\04B\05B or L1 and L5 bands for ZED-F9P-15B.
- Ensure antenna element gain is between 2 and 3 dBic typical for each band.
- Ensure the group delay variation including active antenna is 10 ns max at each GNSS system bandwidth. Note: Inter-signal requirement 50 ns max.
- ESD protection on the RF input is mandatory.
- A Bias-t inductor must be selected with high impedance in the GNSS bands.
- Ensure RF trace is tuned for 50 Ω to ensure adequate bandwidth and power matching.

### <span id="page-105-0"></span>**4.8.5 Ground pads**

Ensure the ground pads of the module are connected to ground.

### <span id="page-105-1"></span>**4.8.6 Schematic design**

For a **minimal design** with the ZED-F9P GNSS modules, consider the following functions and pins:

- Connect the power supply to VCC and V\_BCKP.
- V\_USB: If USB is used it is recommended V\_USB is to be powered as per USB self-powered mode specification.
- If USB is not used connect V\_USB to ground.
- Ensure an optimal ground connection to all ground pins of the ZED-F9P GNSS module.
- Choose the required serial communication interfaces (UART, USB, SPI or I2C) and connect the appropriate pins to your application.
- If you need hot or warm start in your application, connect a backup battery to V\_BCKP.
- Antenna bias is required, see ZED-F9P antenna bias section.

### <span id="page-105-2"></span>**4.8.7 Layout design-in guideline**

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?
- Is the receiver placed as recommended in the [Layout](#page-99-0) and Layout [guidance](#page-101-0)?
- Assure a low serial resistance on the VCC power supply line (choose a line width > 400 um).
- Keep the power supply line as short as possible.
- Add a ground plane underneath the module to reduce interference. This is especially important for the RF input line.
- For improved shielding, add as many vias as possible around the micro strip/co-planar waveguide, around the serial communication lines, underneath the module, etc.

### <span id="page-105-3"></span>**4.8.8 I2C design recommendations**

The I2C communication bus is based on open-drain/open-collector ICs. Pull-up resistors must be connected from the I2C lines to the supply rails to pull the line high when it's not driven low by the open-drain interface.

The u-blox chip integrates internal pull-up resistors at the SCL and SDA pins. These resistors have a large value variation (chip to chip, over temperature, voltage), see product datasheet. To minimize timing variations, it is suggested adding external pull-up resistors with lower resistance at the SCL and SDA pins in parallel to the internal ones.



### **4.8.8.1 I2C pull up calculation**

According to the I2C specification, the electrical input reference levels are set as 30% and 70% of the amplitude. The rise time of the SCL/SDA lines is given by the pull-up resistors and the total bus capacitance.



**Figure 54: I2C bus signal rise and fall time**

The minimum pull up Rp(min) resistance is based on the bus voltage (VCC), the maximum voltage that can be read as a logic-low (VOL), and the maximum current that the pins can sink when at or below VOL (IOL).

Rp(min) = (VCC – VOL) / IOL.

The maximum pull-up resistance is based on the maximum rise-time (t<sup>r</sup> ) requirement (dependent on the I2C clock frequency) and the total capacitance (Cb) on the bus.

Rp(max) = t<sup>r</sup> / (0.8473 \* Cb).

#### **Example:**

For Fast-mode (400 kHz) I2C communication with t<sup>r</sup> = 300 ns, bus voltage VCC = 3.3 V, VOL = 0.4 V, IOL = 2 mA and assuming a total bus capacitance (input pad, line trace, filtering etc.) of max 100 pF (the I2C specification lists the maximum total bus capacitance with a pull-up resistor to be 200 pF):

Rp(min) ≈ 1.5 kΩ and Rp(max) ≈ 3.5 kΩ.

For an internal chip pull-up value between 7 kΩ to 30 kΩ, adding an external pull-up resistor of 3 kΩ between the SCL/SDA lines and the IO supply rail results in a total pull-up resistance in the range of 2.1 kΩ (3 kΩ||7 kΩ) to 2.73 kΩ (3 kΩ||30 kΩ).

### **4.8.8.2 EMI/EMC considerations for I2C bus**

To minimize potential radiated emissions from the I2C lines near GNSS frequencies and address possible I2C timing issues, add filtering capacitors (typically 68 pF) to ground at the SCL and SDA pins or ensure placeholders for the capacitors are provided.

Route the I2C traces away from the PCB edges and connectors to further reduce radiated emissions.



# <span id="page-107-0"></span>**5 Product handling**

# <span id="page-107-1"></span>**5.1 ESD handling precautions**

CAUTION! Risk of electrostatic discharge (ESD) damage. u-blox chips and modules are electrostatic sensitive devices containing highly sensitive electronic circuitry. A discharge of static electricity may damage the device or reduce the life expectancy of the device. To avoid ESD damage, adhere to the standard guidelines for handling ESD devices.

Consider the following:

#### **Preventing electrostatic discharge**

- Keep components in their original packages during transport.
- Open the package within an ESD-protected area (EPA), as in [Figure](#page-108-1) 55.
- At a workstation, store components in an EPA.
- PlaceESD sensitive devices inside of shielding packaging or containers when transported outside of an EPA.
- Use protective clothing and proper personnel grounding at all necessary points when touching electrostatic sensitive device or assembly. For instance, wear ESD-safe clothing and shoes and wear an ESD wrist strap connected to a grounded workstation. Use heel straps when standing on conductive floors or dissipating floor mats.
- Hold the devices by the edges and avoid touching component contacts, pins, or circuitry

#### **Product handling**

- When handling RF transceivers and patch antennas, work in an EPA.
- When connecting test equipment or any other electronics to the module (as a standalone or PCBmounted device), the first point of contact must always be between the local ground and the PCB ground.
- Before mounting a ceramic patch antenna, connect the device to ground.
- When handling the RF pin, do not touch any charged capacitors. Be especially careful when handling materials like patch antennas (~10 pF), coaxial cables (~50-80 pF/m), soldering irons, or any other materials that can develop charges.
- If there is any risk of touching an exposed antenna area in a non-ESD protected work area, implement proper ESD protection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, use an ESD-safe soldering iron (tip)



<span id="page-108-1"></span>



# <span id="page-108-0"></span>**5.2 Soldering**

### **Soldering paste**

Use of "no clean" soldering paste is highly recommended, as it does not require cleaning after the soldering process. For instance, the paste in the example below meets these criteria.

- Soldering paste: OM338 SAC405 / Nr.143714 (Cookson Electronics)
- Alloy specification: Sn 95.5/ Ag 4/ Cu 0.5 (95.5% tin/ 4% silver/ 0.5% copper)
- Melting temperature: 217 °C
- Stencil thickness: The exact geometry, distances, stencil thicknesses and solder paste volumes must be adapted to the customer's specific production processes (e.g. soldering).

#### **Reflow soldering**

CAUTION. Risk of device damage. Exceeding the peak temperature of the recommended soldering profile may permanently damage the device.

The final soldering temperature chosen at the factory depends on additional external factors such as the choice of soldering paste, size, thickness and properties of the base board, etc.

CAUTION. Risk of device damage. Modules must not be soldered with a damp heat process.

As a reference, see "IPC-7530 Guidelines for temperature profiling for mass soldering (reflow and wave) processes", published in 2001.

A convection-type soldering oven is highly recommended over the infrared-type radiation oven. Convection-heated ovens allow precise control of the temperature, and all parts will heat up evenly, regardless of material properties, thickness of components and surface color.

To avoid falling off, the modules should be placed on the topside of the board during soldering.

As a reference, see "IPC-7530 Guidelines for temperature profiling for mass soldering (reflow and wave) processes", published in 2001.



<span id="page-109-0"></span>

For the recommended soldering profile and conditions, see [Figure](#page-109-0) 56, and [Table](#page-109-1) 46

**Figure 56: Recommended soldering profile for professional grade ZED-F9P**

<span id="page-109-1"></span>

| Phase                   | Value        | Details                                                                                                                                                                                                                                                                   |
|-------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Preheating              |              | During the initial heating of component leads and balls,<br>residual humidity is dried out. Note that the preheating phase<br>does not replace prior baking procedures.                                                                                                   |
| Temperature rise rate   | Max 3 °C/s   | If the temperature rise is too rapid in the preheat phase,<br>excessive slumping may be caused.                                                                                                                                                                           |
| Time                    | 60 – 120 s   | If the preheating is insufficient, rather large solder balls tend<br>to be generated. Conversely, if performed excessively, fine<br>balls and large balls will be generated in clusters.                                                                                  |
| End temperature         | 150 – 200 °C | If the temperature is too low, non-melting tends to be caused<br>in areas containing large heat capacity.                                                                                                                                                                 |
| Heating - reflow        |              | The temperature rises above the liquidus temperature of 217<br>°C. Avoid a sudden rise in temperature as the slump of the<br>paste could become worse.                                                                                                                    |
| Time limit above 217 °C | 40 – 60 s    |                                                                                                                                                                                                                                                                           |
| liquidus temperature    |              |                                                                                                                                                                                                                                                                           |
| Peak reflow temperature | 245 °C       |                                                                                                                                                                                                                                                                           |
| Cooling                 |              | A controlled cooling prevents negative metallurgical effects<br>of the solder (solder becomes more brittle) and possible<br>mechanical tensions in the products. Controlled cooling helps<br>to achieve bright solder fillets with a good shape and low<br>contact angle. |



| Phase                 | Value      | Details |
|-----------------------|------------|---------|
| Temperature fall rate | Max 4 °C/s |         |

**Table 46: Recommended conditions for reflow soldering**

#### **Optical inspection**

After soldering the module, consider optical inspection.

#### **Cleaning**

Do not clean with water, solvent, or ultrasonic cleaner:

- Cleaning with water will lead to capillary effects where water is absorbed into the gap between the baseboard and the module. The combination of residues of soldering flux and encapsulated water leads to short circuits or resistor-like interconnections between neighboring pads.
- Cleaning with alcohol or other organic solvents can result in soldering flux residues flowing underneath the module, into areas that are not accessible for post-cleaning inspections. The solvent will also damage the sticker and the printed text.
- CAUTION. Risk of device damage. Ultrasonic cleaning permanently damages the module, in particular the quartz oscillators.

The best approach is to use a "no clean" soldering paste and eliminate the cleaning step after the soldering.

#### **Repeated reflow soldering**

Repeated reflow soldering processes or soldering the module upside down are not recommended.

A board that is populated with components on both sides may require more than one reflow soldering cycle. In such a case, the process should ensure the module is only placed on the board submitted for a single final upright reflow cycle. A module placed on the underside of the board may detach during a reflow soldering cycle due to lack of adhesion.

The module can also tolerate an additional reflow cycle for rework purposes.

#### **Wave soldering**

Base boards with combined through-hole technology (THT) components and surface-mount technology (SMT) devices require wave soldering to solder the THT components. Only a single wave soldering process is encouraged for boards populated with modules.

#### **Rework**

CAUTION. Risk of device damage. Using a hot air gun is an uncontrolled process. It can lead to overheating and severely damage the module. Always avoid overheating the module.

After the module is removed from the oven, clean the pins before reapplying the solder paste, placing the module in the oven and proceeding with the reflow soldering of a new module.

Never attempt to alter the module itself, e.g. by replacing individual components. Such actions immediately void the warranty.

#### **Conformal coating**

Certain applications employ a conformal coating of the PCB using HumiSeal® or other related coating products. These materials affect the RF properties of the GNSS module and it is important to prevent them from flowing into the module. The RF shields do not provide 100% protection for the module from coating liquids with low viscosity. Apply the coating carefully.



Conformal coating of the module will void the warranty.

#### **Casting**

If casting is required, use viscose or another type of silicon pottant. The OEM is strongly advised to qualify that such processes are suitable for the module before implementing them in the production.

Casting voids the warranty.

#### **Grounding metal covers**

Attempts to improve grounding by soldering ground cables, wick or other forms of metal strips directly onto the EMI covers is done at the customer's own risk. The numerous ground pins should be sufficient to provide optimum immunity to interference and noise.

u-blox provides no warranty for damages to the module caused by soldering metal cables or any other forms of metal strips directly onto the EMI covers.

#### **Use of ultrasonic processes**

- CAUTION. Risk of device damage. Use of any ultrasonic processes (cleaning, welding etc.) may cause damage to the receiver.
- u-blox provides no warranty against damages to the module caused by ultrasonic processes.

## <span id="page-111-0"></span>**5.3 Tapes**

<span id="page-111-1"></span>

#### **Figure 57: Orientation of ZED-F9P on the tape**

The feed direction to the pick and place pick-up is shown by the orientation of the pin 1 location. In [Figure](#page-111-1) 57, with pin 1 location on the bottom of the tape, the feed direction into the pick and place pick-up is from the reel (located on the right of the figure) towards right.

The dimensions of the tapes for ZED-F9P are specified in [Figure](#page-112-1) 58 (measurements in mm).



<span id="page-112-1"></span>

**Figure 58: ZED-F9P tape dimensions (mm)**

# <span id="page-112-0"></span>**5.4 Reels**

The ZED-F9Preceivers are deliverable in quantities of 250 pieces on a reel.The receivers are shipped on reel type B, as specified in the Product packaging reference guide [[3](#page-126-4)].



# <span id="page-113-0"></span>**Appendix**

# <span id="page-113-1"></span>**A Glossary**

| Abbreviation | Definition                                            |
|--------------|-------------------------------------------------------|
| ANSI         | American National Standards Institute                 |
| ARP          | Antenna reference point                               |
| BeiDou       | Chinese navigation satellite system                   |
| BBR          | Battery-backed RAM                                    |
| CDMA         | Code-division multiple access                         |
| EMC          | Electromagnetic compatibility                         |
| EMI          | Electromagnetic interference                          |
| EOS          | Electrical overstress                                 |
| EPA          | Electrostatic protective area                         |
| ESD          | Electrostatic discharge                               |
| Galileo      | European navigation satellite system                  |
| GLONASS      | Russian navigation satellite system                   |
| GND          | Ground                                                |
| GNSS         | Global navigation satellite system                    |
| GPS          | Global Positioning System                             |
| GSM          | Global System for Mobile Communications               |
| I2C          | Inter-integrated circuit bus                          |
| IEC          | International Electrotechnical Commission             |
| ITRF         | International Terrestrial Reference Frame             |
| MB           | Moving base                                           |
| MI           | Misleading Information                                |
| MSM          | Multiple signal messages                              |
| NTRIP        | Networked Transport of RTCM via Internet Protocol     |
| OSR          | Observation Space Representation                      |
| PCB          | Printed circuit board                                 |
| PPP-RTK      | Precise Point Positioning with Real-Time Kinematic    |
| QZSS         | Quasi-Zenith Satellite System                         |
| RF           | Radio frequency                                       |
| RTCM         | Radio Technical Commission for Maritime Services      |
| RTK          | Real-Time Kinematic                                   |
| SBAS         | Satellite-based Augmentation System                   |
| SPARTN       | Secure Position Augmentation for Real-Time Navigation |
| SSR          | State Space Representation                            |
| SV           | Space vehicle, a satellite                            |
| TDOP         | Time dilution of precision                            |
| UBX          | u-blox                                                |
| VRS          | Virtual reference station                             |



## <span id="page-114-0"></span>**B Reference frames**

Real time kinematic (RTK) is a differential system where the rover uses the corrections from a reference station or a reference station network. The rover receiver will calculate its position in the reference frame used by the service provider in its correction stream. If the output is required in a different reference frame, then a (custom) datum transformation is required.

For example, if an application requires the position in the ITRF14 reference frame but the correction service is using the ETRF14 reference frame - to which the RTK solution will also be referring - then this reference frame offset needs to be compensated. For example if utilizing a truth system which is using corrections referring to different reference frame, it is important to compensate for the reference frame offset to avoid systematic errors in the analysis.

Terrestrial reference system is a coordinate reference system which is rotating in space with the rotation of the Earth. The reference system is an abstract concept that is realized by obtaining coordinates for some points on the surface of the Earth. This kind of realization is called a reference frame. For more details, see for example the ITRF [webpage](http://itrf.ensg.ign.fr/trs_trf.php). Commonly used reference systems include International Terrestrial Reference System (ITRS) and European Terrestrial Reference System 1989 (ETRS89).

Widely used reference frames include for example International Terrestrial Reference Frame (ITRF) andEuropeanTerrestrial Reference Frame (ETRF). ITRF is a realization of ITRS, done every few years. Latest realizations of ITRF are ITRF2008 and ITRF2014. ETRF is a realization of ETRS89, done every few years. Latest realizations are ITRF2005 and ETRF2014.

For example, the EUREF is used to realize the ETRS89. For information, see their homepage: [EUREF](http://www.epncb.oma.be/).

See the ITRF website for more information and an online transform calculator: [ITRF](http://itrf.ensg.ign.fr/ITRF_solutions/index.php).

Another online tool for transformations is available on the EUREF network page: [EUREF](http://www.epncb.oma.be/_productsservices/coord_trans/) [Transformation](http://www.epncb.oma.be/_productsservices/coord_trans/).

Reference frames can have constant offsets between each other but, in addition to that, they can also drift and rotate with respect to each other. One major reason for this is that the tectonic plates move constantly and the reference frames that are attached to the tectonic plates move along with the plates.

The ZED-F9P stores the EGM96 geoid model with limited resolution, leading to degraded precision of the reported mean sea level height and geoid separation. If the user application needs higher geoid separation accuracy, it is required to apply its own adjustment to the ellipsoidal height output from the ZED-F9P.

# <span id="page-114-1"></span>**C RTK configuration procedures with u-center**

This section provides some guidance when using u-center to configure base and rover operation.

### <span id="page-114-2"></span>**C.1 Base configuration with u-center**

This section describes setting a static base configuration in the u-center "Messages View" window.

Start u-center and connect to the ZED-F9P device. Under the UBX-CFG message tree, three configuration messages are listed:

- **UBX-CFG-VALDEL**: Allows configuration deletion
- **UBX-CFG-VALGET**: Allows configuration reading
- **UBX-CFG-VALSET**: Allows configuration setting



All configuration item setting is done using the **UBX-CFG-VALSET** dialog. The general operation is as follows:

- **1.** To open a configuration setting dialog, select **UBX-CFG-VALSET** in the message tree list.
- **2.** Select the required **Group** in the "Compose list entry" section.
- **3.** Select the associated key in the "Key name" pull-down menu.
- **4.** Once you have selected the configuration key, move it to the configuration changes list by clicking **Add to List**.

You can edit or read key values from the receiver after selecting items in the "Configuration changes to send" list. See [Figure](#page-115-0) 59 below.

<span id="page-115-0"></span>

| The baud rate that should be configured on the<br>Title<br>UART1<br>▾<br>Description<br>CFG-UART1-BAUDRATE<br>$\blacktriangledown$<br>Type: U4<br>Add to List | ∸<br>$\overline{\phantom{a}}$<br>∸<br>$\overline{\phantom{a}}$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Configuration changes to send-                                                                                                                                |                                                                |
| Key ID<br>Value<br>Type                                                                                                                                       |                                                                |
|                                                                                                                                                               |                                                                |
|                                                                                                                                                               |                                                                |
|                                                                                                                                                               | Remove                                                         |
|                                                                                                                                                               | Remove all                                                     |
|                                                                                                                                                               |                                                                |
|                                                                                                                                                               |                                                                |
|                                                                                                                                                               | Read receiver                                                  |
| Transaction<br>$\Box$ Flash $\Box$ BBR<br>$\nabla$ RAM                                                                                                        |                                                                |

**Figure 59: u-center UBX-CFG-VALSET message view**

Use the following procedure to configure the module for base station operation:

Setting the required RTCM message output can be done in one session.

- **1.** Select **Group**: CFG-MSGOUT, **Key name**: CFG-MSGOUT-RTCM3X, and select the UART1 required messages.
- **2.** Add each message to the list and set the value of each to 1.
- **3.** Click **Send**

See [Figure](#page-116-0) 60 below.



<span id="page-116-0"></span>

| Compose list entry<br>CFG-MSGOUT<br>Group     |                          | Details<br>Title |       | on port UART1 | Output rate of the RTCM-3X-TYPE1230 message $\sim$ |               | $\overline{\phantom{a}}$ |
|-----------------------------------------------|--------------------------|------------------|-------|---------------|----------------------------------------------------|---------------|--------------------------|
| Key name<br>CFG-MSGOUT-RTCM_3X_TYPE1230_UART1 | $\overline{\phantom{a}}$ | Description      |       |               |                                                    |               | ۸                        |
| 20910304<br>Key ID                            | Add to List              | Type: U1         |       |               |                                                    |               | $\overline{\phantom{a}}$ |
| Configuration changes to send-                |                          |                  |       |               |                                                    |               |                          |
| Key                                           | Key ID                   | Type             | Value |               |                                                    |               |                          |
| CFG-MSGOUT-RTCM_3X_TYPE1005_UART1             | 0x209102be               | U1               | 10x1  |               |                                                    |               |                          |
| CFG-MSGOUT-RTCM 3X TYPE1077 UART1             | 0x209102cd               | U1               | 1.0x1 |               |                                                    |               |                          |
| CFG-MSGOUT-RTCM 3X TYPE1087 UART1             | 0x209102d2               | U1               | 1.0x1 |               |                                                    |               |                          |
| CFG-MSGOUT-RTCM 3X TYPE1127 UART1             | 0x209102d7               | U1               | 10x1  |               |                                                    |               |                          |
| CFG-MSGOUT-RTCM 3X TYPE1097 UART1             | 0x20910319               | U1               | 1.0x1 |               |                                                    |               |                          |
| CFG-MSGOUT-RTCM 3X TYPE1230 UART1             | 0x20910304               | U1               | 1.0x1 |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               | Remove                   |
|                                               |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               | Remove all               |
|                                               |                          |                  |       |               |                                                    |               |                          |
| Value                                         |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       | Value hex     |                                                    |               |                          |
| l1                                            |                          |                  |       | I1            |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    |               |                          |
|                                               |                          |                  |       |               |                                                    | Read receiver |                          |
|                                               |                          |                  |       |               |                                                    |               |                          |
| Lavers                                        |                          |                  |       |               | Transaction:                                       |               |                          |
| $\Box$ Flash $\Box$ BBR<br>$\nabla$ RAM       |                          |                  |       |               | No transaction                                     |               |                          |
|                                               |                          |                  |       |               |                                                    |               | ۰                        |

**Figure 60: Base station: u-center UBX-CFG-VALSET message view for setting the CFG-MSGOUT-\* configuration group for enabling the output of the required RTCM messages**

The configuration illustration shows the use of RTCM MSM7 messages. MSM4 messages are equally applicable as recommended in the receiver configuration section.

Set the receiver into base mode by enabling a survey-in procedure or specify fixed coordinates via items within the CFG-TMODE configuration group. An example of survey-in configuration is shown below.



| Compose list entry<br>CFG-TMODE<br>Group<br>$\vert \cdot \vert$ |                      | Details<br>Title |             | Survey-in minimum duration                              |               | ┻<br>$\overline{\nabla}$ |
|-----------------------------------------------------------------|----------------------|------------------|-------------|---------------------------------------------------------|---------------|--------------------------|
| Key name<br>CFG-TMODE-SVIN_MIN_DUR                              | $\blacktriangledown$ |                  | Description | This will only be used if CFG-TMODE-<br>MODE=SURVEY IN. |               | ∸                        |
| 40030010<br>Key ID                                              | Add to List          | Type: U4         |             |                                                         |               | $\overline{\phantom{a}}$ |
| Configuration changes to send                                   |                      |                  |             |                                                         |               |                          |
| Key                                                             | Key ID               | Type             | Value       |                                                         |               |                          |
| CFG-TMODE-MODE                                                  | 0x20030001           | E1               |             | 1 - SURVEY IN                                           |               |                          |
| CFG-TMODE-SVIN_ACC_LIMIT                                        | 0x40030011           | U4               |             | 50000 0xc350 mm scaled 0.1                              |               |                          |
| CFG-TMODE-SVIN_MIN_DUR                                          | 0x40030010           | U <sub>4</sub>   | 60 0x3c s   |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         | Remove        |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             |                                                         | Remove all    |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
| Value                                                           |                      |                  |             |                                                         |               |                          |
|                                                                 |                      |                  |             | Value hex                                               |               |                          |
| lsd                                                             |                      |                  |             | 3c                                                      |               |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |
| unit s                                                          |                      |                  |             |                                                         | Read receiver |                          |
|                                                                 |                      |                  |             |                                                         |               |                          |

**Figure 61: Base station: u-center UBX-CFG-VALSET message view for setting the CFG-TMODE-\* configuration group required for performing a survey-in**

When using the survey-in mode, you must select reasonable settings based on the environment and achievable accuracy in the base location. A figure of 50000 (0.1 mm x 50000 = 5 m) for estimated accuracy and survey-in time of 60 seconds is a sensible starting point. In good satellite visibility, the base is unlikely to achieve an accuracy better than 1 m.

In multi-path conditions, the time to achieve a specified accuracy can take longer than expected. You may need to relocate the base antenna or extend the required accuracy and/or survey-in time. You can monitor the status of the survey-in status using the NAV-SVIN message.

The receiver will output messages upon configuration setting, however RTCM 1005 will **only** be output once the survey-in is completed, or the fixed coordinates are entered for the base antenna. Use the u-center "Packet Console View" to verify message output. Once surveyed in correctly, it will indicate a TIME solution mode in the u-center Data view. See below in [Figure](#page-118-1) 62.



<span id="page-118-1"></span>

| $-0.20489633$<br>Longitude                      |
|-------------------------------------------------|
|                                                 |
| 51.24183667<br>Latitude                         |
| Altitude<br>152.500 m                           |
| <b>TTFF</b><br>32.403 s                         |
| Fix Mode<br>TIME                                |
| 3D Acc. [m] <b>0</b><br>1.08                    |
| Ę<br>$2D$ Acc. [m] $\overline{0}$<br>0.88       |
| PDOP                                            |
| HDOP                                            |
| <b>Satellites</b><br>,,,,,,,,,,,,,,,,,,,,,,,,,, |

**Figure 62: Base station: u-center data view in TIME mode**

### <span id="page-118-0"></span>**C.2 Rover configuration with u-center**

This overview will help when setting up a rover when using u-center.

In this procedure, the UART1 is set with an appropriate baud rate for communicating with a host. Then a set of output messages are set to enable receiver status monitoring.

Using the **UBX-CFG-VALSET** configuration window in the u-center **Message View**, set the UART1 interface for the correct host baud rate:

#### <span id="page-118-2"></span>**1.** Select **Group**: CFG-UART1, **Key name**: CFG-UART1-BAUDRATE. See [Figure](#page-118-2) 63.

| Compose list entry<br>CFG-UART1<br>Group | ⊻           | Details<br>Title | The baud rate that should be configured on the<br>UART1 | $\blacktriangle$<br>$\overline{\nabla}$ |
|------------------------------------------|-------------|------------------|---------------------------------------------------------|-----------------------------------------|
| Key name<br>CFG-UART1-BAUDRATE           |             | Description<br>▼ |                                                         | $\blacktriangle$                        |
| 40520001<br>Key ID                       | Add to List | Type: U4         |                                                         | $\overline{\phantom{a}}$                |
| Configuration changes to send            |             |                  |                                                         |                                         |
| Key                                      | Key ID      | Type<br>Value    |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         | Remove                                  |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         | Remove all                              |
| -Value                                   |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         |                                         |
|                                          |             |                  |                                                         | Read receiver                           |
| Layers                                   |             |                  | Transaction                                             |                                         |

**Figure 63: u-center UBX-CFG-VALSET message view**

- **2.** Select **Add to List**, it will appear in the table below.
- **3.** Select the added **Key**. It will now give the option of setting or reading the current value. See [Figure](#page-119-0) 64.



<span id="page-119-0"></span>

| Group    | Compose list entry<br>CFG-UART1<br>$\overline{\phantom{a}}$ |                      | Details<br>Title |             | The baud rate that should be configured on the<br>UART1 | ▲             |
|----------|-------------------------------------------------------------|----------------------|------------------|-------------|---------------------------------------------------------|---------------|
| Key name | CFG-UART1-BAUDRATE                                          | $\blacktriangledown$ |                  | Description |                                                         | À.            |
| Key ID   | 40520001                                                    | Add to List          | Type: U4         |             |                                                         |               |
|          | Configuration changes to send-                              |                      |                  |             |                                                         |               |
| Key      |                                                             | Key ID               | Type             | Value       |                                                         |               |
|          | CFG-UART1-BAUDRATE                                          | 0x40520001           | $\Box$ 4         |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         | Remove        |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         | Remove all    |
|          |                                                             |                      |                  |             |                                                         |               |
| Value    |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             | Value hex                                               |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         |               |
|          |                                                             |                      |                  |             |                                                         | Read receiver |
|          |                                                             |                      |                  |             |                                                         |               |
| Layers   |                                                             |                      |                  |             | Transaction                                             |               |

**Figure 64: Example u-center UBX-CFG-VALSET message view when selecting a configuration item**

- **4.** Next add the value, for example, 230400, into the **Value** window that appears below the list. See [Figure](#page-120-0) 65.
- **5.** Then set the configuration by clicking the **Send** button at the bottom of the message tree view. Remember to set the u-center baud rate to match the value set in the receiver.



<span id="page-120-0"></span>

| Compose list entry-<br>Group | CFG-UART1                      | ▾                    | Details<br>Title | UART1                   | The baud rate that should be configured on the<br>A.<br>$\overline{\nabla}$ |
|------------------------------|--------------------------------|----------------------|------------------|-------------------------|-----------------------------------------------------------------------------|
| Key name                     | CFG-UART1-BAUDRATE             | $\blacktriangledown$ | Description      |                         | ∸                                                                           |
| Key ID                       | 40520001                       | Add to List          | Type: U4         |                         | $\overline{\phantom{0}}$                                                    |
|                              | Configuration changes to send- |                      |                  |                         |                                                                             |
| Key                          | CFG-UART1-BAUDRATE             | Key ID<br>0x40520001 | Type<br>U4       | Value<br>230400 0x38400 |                                                                             |
|                              |                                |                      |                  |                         |                                                                             |
|                              |                                |                      |                  |                         |                                                                             |
|                              |                                |                      |                  |                         | Remove                                                                      |
|                              |                                |                      |                  |                         | Remove all                                                                  |
| Value                        |                                |                      |                  | Value hex               |                                                                             |
| 230400                       |                                |                      |                  | 38400                   |                                                                             |
|                              |                                |                      |                  |                         | Read receiver                                                               |

**Figure 65: Rover: u-center UBX-CFG-VALSET message view for setting the CFG-UART1-BAUDRATE configuration item that controls the baud rate of UART1**

Next, some UBX example messages are configured to enable viewing the rover status.

- **1.** Select **Group** CFG-MSGOUT, **Key name**: CFG-MSGOUT-UBX and select the UART1 required messages.
- **2.** Add each message to the list, setting the value of each to 1.
- **3.** Click **Send**. See [Figure](#page-121-0) 66.



<span id="page-121-0"></span>

| Compose list entry<br>CFG-MSGOUT<br>Group<br>$\blacktriangledown$     |                          | Details<br>Title |                | Output rate of the UBX-NAV-SOL message on<br>port UART1 | $\hat{\rho}_{\rm{N}}$<br>v |
|-----------------------------------------------------------------------|--------------------------|------------------|----------------|---------------------------------------------------------|----------------------------|
| Key name<br>CFG-MSGOUT-UBX_NAV_SOL_UART1                              | $\overline{\phantom{a}}$ |                  | Description    |                                                         | Α                          |
| 20910002<br>Key ID                                                    | Add to List              | Type: U1         |                |                                                         | $\sim$                     |
| Configuration changes to send-                                        |                          |                  |                |                                                         |                            |
| Key                                                                   | Key ID                   | Type             | Value          |                                                         |                            |
| CFG-MSGOUT-UBX_NAV_SIG_UART1                                          | 0x20910346               | U1               | ÷              |                                                         |                            |
| CFG-MSGOUT-UBX NAV PVT UART1                                          | 0x20910007               | U1               | ÷.             |                                                         |                            |
| CFG-MSGOUT-UBX NAV POSLLH UART1<br>CFG-MSGOUT-UBX NAV RELPOSNED UART1 | 0x2091002a<br>0x2091008e | U1<br>U1         | $\blacksquare$ |                                                         |                            |
| CFG-MSGOUT-UBX NAV STATUS UART1                                       | 0x2091001b               | U1               | ä,<br>÷        |                                                         |                            |
|                                                                       |                          |                  |                |                                                         |                            |
|                                                                       |                          |                  |                |                                                         | Remove                     |
|                                                                       |                          |                  |                |                                                         | Remove all                 |
| Value                                                                 |                          |                  |                |                                                         |                            |
|                                                                       |                          |                  |                |                                                         |                            |
|                                                                       |                          |                  |                |                                                         | Read receiver              |

**Figure 66: Rover: u-center UBX-CFG-VALSET message view for setting the CFG-MSGOUT-\* configuration items for enabling the output of some recommended UBX messages**

To ensure all the required RTCM messages, including most importantly RTCM 1005 or 4072.0, are being received regularly, examine the **UBX-RXM-RTCM** output in u-center. See [Figure](#page-121-1) 67.

<span id="page-121-1"></span>

| Message Type                                                                     | Total messages                           |             | CRC passed messages        |             | CRC failed messages | (Last) Reference Station ID |
|----------------------------------------------------------------------------------|------------------------------------------|-------------|----------------------------|-------------|---------------------|-----------------------------|
| 0                                                                                | 0                                        |             | 0                          |             | 0                   | n/a                         |
| 1002                                                                             | 0                                        |             | $\mathbf 0$                |             | 0                   | n/a                         |
| 1005                                                                             | 33                                       |             | 33                         |             | 0                   | 0                           |
| 1009                                                                             | 0                                        |             | $\mathbf 0$                |             | $\mathbf 0$         | n/a                         |
| 1010                                                                             | 0                                        |             | 0                          |             | 0                   | n/a                         |
| 1074                                                                             | $\mathbf 0$                              |             | $\overline{0}$             |             | $\mathbf 0$         | n/a                         |
| 1077                                                                             | 33                                       |             | 33                         |             | $\overline{0}$      | $\mathbf{0}$                |
| 1084                                                                             | 0                                        | $\mathbf 0$ |                            | $\mathbf 0$ |                     | n/a                         |
| 1087                                                                             | 33                                       |             | 33                         |             | 0                   | $\mathbf 0$                 |
| 1097                                                                             | 33                                       | 33          |                            |             | 0                   | 0                           |
| 1124                                                                             | $\mathbf{0}$                             |             | $\mathbf{0}$               |             | 0                   | n/a                         |
| 1127                                                                             | 33                                       |             | 33                         |             | $\overline{0}$      | $\mathbf 0$                 |
| 1230                                                                             | 33                                       |             | 33                         |             | $\mathbf 0$         | $\mathbf{0}$                |
| 1001                                                                             | 0                                        |             | 0                          |             | 0                   |                             |
|                                                                                  | * Messages not supported by the receiver |             |                            |             |                     | n/a                         |
|                                                                                  |                                          |             |                            |             |                     |                             |
|                                                                                  | Reference Station ID                     | Message ID  | CRC check                  | ▲           |                     |                             |
|                                                                                  | 0                                        |             | 1005 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1230 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1127 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1097 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1087 Passed                | Ξ           |                     |                             |
|                                                                                  | 0                                        |             | 1077 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1005 Passed                |             |                     |                             |
| Current messages:<br>ix.<br>198<br>197<br>196<br>195<br>194<br>193<br>192<br>191 | 0                                        |             | 1230 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1127 Passed                |             |                     |                             |
|                                                                                  | 0                                        |             | 1097 Passed                |             |                     |                             |
| 190<br>189<br>188                                                                | 0                                        |             | 1087 Passed                |             |                     |                             |
| 187                                                                              | 0                                        |             | 1077 Passed                |             |                     |                             |
| 186<br>185                                                                       | 0<br>0                                   |             | 1005 Passed<br>1230 Passed |             |                     |                             |

**Figure 67: Rover: u-center UBX-RXM-RTCM view**



Once the rover has started to receive valid RTCM messages, it will transition through 3D Fix to 3D/ DGNSS to Float, and, ultimately, into Fixed mode. This will occur when it is receiving all required RTCM messages, including RTCM 1005 or 4072.0, under sufficient signal conditions. See [Figure](#page-122-1) 68.

<span id="page-122-1"></span>

|                   |           | ×              |
|-------------------|-----------|----------------|
| Longitude         |           | $-0.20488940$  |
| Latitude          |           | 51.24184640    |
| Altitude          |           | 151.161 m      |
| <b>TTFF</b>       |           | 15.137         |
| Fix Mode          |           | 3D/DGNSS/FIXED |
| 3D Acc. [m]       | 0.02<br>0 |                |
| 2D Acc. [m]       | 0.01      |                |
| PDOP              | 1.2       |                |
| HDOP              |           |                |
| <b>Satellites</b> |           |                |
|                   |           |                |

**Figure 68: Rover: u-center data view with RTK Fixed**

If using a virtual reference service, the rover must output the NMEA GGA message to return to the NTRIP caster. Without this, the NTRIP caster will not provide correction information. NMEA messages are enabled by default on the UART1, I2C, SPI and USB interface.

# <span id="page-122-0"></span>**D Stacked patch antenna**

A typical low-cost L1 + L2 or L5 antenna is based on a stacked patch antenna design. This consists of two discrete ceramic patch elements with an L1 patch above an L2 or L5 patch.



#### **Figure 69: Stacked patch antenna**

The absolute antenna position for a survey-grade antenna is normally given as the antenna reference point (ARP), usually specified at amechanicalmounting point.The antenna nominal phase center is given by a phase center combination of the L1 and L2 or L5 patches. Survey-grade antenna makers provide offset data for phase variation with respect to the ARP.





**Figure 70: Ceramic stack**

When used in an application, the antenna placement affects the phase center variation owing to the size and shape of the ground plane coupled with the effects of the adjacent structures. A phase center variation calibration is required to check the average phase center. A successful calibration can be made if the phase variation of a specific antenna is repeatable between samples.

To obtain the best antenna performance in an automotive application, mount the antenna in the center of a conductive car roof without any inclination. The antenna requires good signal levels and as wide a view of the sky as possible. The antenna must not be placed under a dashboard, in the rear view mirror, or on the rear parcel shelf.

An L1 + L2 or L5 stacked patch antenna must have a good band-pass performance from the patch elements with low attenuation from SAW band-pass filtering. An example of the measured frequency characteristics of a low-cost L1 + L2 antenna is shown below.





**Figure 71: Low-cost L1/L2 antenna band characteristics**

The u-blox low-cost antenna design is shown below, followed by some examples of antennas from other manufacturers which can be used with ZED-F9P.





#### **Figure 72: u-blox low-cost RTK antenna**

There are antenna types that can be used without a substantial ground plane, such as a helical antenna type. This is a useful solution where space is limited, for example, for drone or small form factor applications.



# <span id="page-126-0"></span>**Related documents**

- <span id="page-126-3"></span>**[1]** ZED-F9P-01B Data sheet, UBX-17051259 ZED-F9P-02B Data sheet, UBX-21023276 ZED-F9P-04B Data sheet, UBX-21044850 ZED-F9P-05B Data sheet, UBXDOC-963802114-12824 ZED-F9P-15B Data sheet, [UBX-23009090](https://www.u-blox.com/docs/UBX-23009090)
- <span id="page-126-1"></span>**[2]** HPG 1.12 Interface description, UBX-21043658 HPG 1.13 Interface description, UBX-21023318 HPG 1.32 Interface description, UBX-22008968 HPG L1L5 1.40 Interface description, [UBX-23006991](https://www.u-blox.com/docs/UBX-23006991) HPG 1.50 Interface description, UBXDOC-963802114-12815 HPG 1.51 Interface description, UBXDOC-963802114-13124
- <span id="page-126-4"></span>**[3]** Product packaging reference guide, [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-126-2"></span>**[4]** ZED-F9P Moving Base application note, [UBX-19009093](https://www.u-blox.com/docs/UBX-19009093)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



# <span id="page-127-0"></span>**Revision history**

| Revision | Date        | Status / comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 22-May-2018 | HPG 1.00 and ZED-F9P-00B release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R02      | 03-Oct-2018 | HPG 1.00 update. ZED-F9P-00B update                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R03      | 20-Dec-2018 | HPG 1.10 update. ZED-F9P-00B-01 update                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R04      | 1-Mar-2019  | HPG 1.11 update. ZED-F9P-00B-02 update.<br>Added a design-in restriction for ANT_DETECT pin in section Design.                                                                                                                                                                                                                                                                                                                                                                                                         |
| R05      | 22-Aug-2019 | HPG 1.12 update. ZED-F9P-01B update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| R06      | 15-Jan-2020 | Tape feed and dimension pictures updated. PCN UBX-19057484 added and module type<br>number updated.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R07      | 25-Feb-2020 | Updated minimum and maximum gains in Antenna specifications table.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R08      | 02-Jun-2020 | HPG 1.13 update. ZED-F9P-02B-00 update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R09      | 25-Jun-2021 | ZED-F9P-02B-00 update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R10      | 17-Dec-2021 | HPG 1.30 update. ZED-F9P-04B-00 update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          |             | Overall text improvement and typo corrections plus:                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|          |             | 2.1 Overview updated, 3.1.3 default interface settings updated, 3.1.4.5 NMEA high precision<br>mode added, 3.1.5 RTK configuration updated, 3.1.6 PPP-RTK configuration added, 3.1.8.1<br>platform settings updated, 3.2 primary and secondary output added, 3.3 SBAS section<br>updated, 3.7 Protection level added, 3.8 Communication interfaces updated, 3.11 MGA<br>section updated, 3.14.3.3 configuration lockdown added, 3.18 Spectrum analyzer updated,<br>4.7.2 Thermal management added, Appendix B updated. |
| R11      | 18-Feb-2022 | Overall text improvement and typo corrections plus:                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|          |             | Document information section updated, Related documents section updated.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R12      | 03-May-2022 | HPG 1.32 update. ZED-F9P-04B-01 update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          |             | Overall text improvement and typo corrections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| R13      | 30-Aug-2023 | HPG L1L5 1.40 update. ZED-F9P-15B-00 update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|          |             | Overall text improvement and typo corrections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| R14      | 26-Sep-2023 | ZED-F9P-15B initial production release.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R15      | 05-Jul-2024 | ZED-F9P-05B engineering sample release.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          |             | 3.14.5 Added new feature OSNMA, 3.14.4.4 Added new feature Compliance with DHS allow<br>list, 3.1.5 Added new feature Conservative ambiguity mode under RTK configuration, 3.1.6.1<br>SPARTN corrections updated, 3.1.5.1 RTCM corrections updated.                                                                                                                                                                                                                                                                    |
| R16      | 30-Oct-2024 | ZED-F9P-05B initial production release.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          |             | HPG 1.51 update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|          |             | Added a note in the OSNMA section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



# **Contact**

### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).