

# **ZED-F9H**

## **u-blox F9 module for heading applications**

**Integration manual**



#### **Abstract**

This document describes the features and application of ZED-F9H, a multiband GNSS module for heading applications, designed to provide the best possible heading information to applications where precise attitude is of greatest importance.

**www.u-blox.com**



UBX-19030120 - R05 C1-Public



## **Document information**

| Title                  | ZED-F9H                                   |             |
|------------------------|-------------------------------------------|-------------|
| Subtitle               | u-blox F9 module for heading applications |             |
| Document type          | Integration manual                        |             |
| Document number        | UBX-19030120                              |             |
| Revision and date      | R05                                       | 18-Feb-2022 |
| Disclosure restriction | C1-Public                                 |             |

#### This document applies to the following products:

| Type number    | FW version | PCN reference | RN reference |
|----------------|------------|---------------|--------------|
| ZED-F9H-00B-01 | HDG 1.12   | UBX-19057484  | UBX-19027215 |
| ZED-F9H-01B-00 | HDG 1.13   | -             | UBX-20047673 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2022, u-blox AG.



| 1 Integration<br>manual<br>overview                   | 6 |  |
|-------------------------------------------------------|---|--|
| 2 System<br>description7                              |   |  |
| 2.1 Overview 7                                        |   |  |
| 2.1.1 GNSS-based attitude determination7              |   |  |
| 2.2 Architecture8                                     |   |  |
| 2.2.1 Block diagram8                                  |   |  |
| 2.2.2 Typical ZED-F9H application setups 8            |   |  |
| 3 Receiver<br>functionality11                         |   |  |
| 3.1 Receiver configuration11                          |   |  |
| 3.1.1 Changing the receiver configuration 11          |   |  |
| 3.1.2 Default GNSS configuration 11                   |   |  |
| 3.1.3 Default interface settings12                    |   |  |
| 3.1.4 Basic receiver configuration 12                 |   |  |
| 3.1.5 Moving base RTK configuration 15                |   |  |
| 3.1.6 Legacy configuration interface compatibility 18 |   |  |
| 3.1.7 Navigation configuration18                      |   |  |
| 3.2 SBAS23                                            |   |  |
| 3.3 QZSS SLAS 25                                      |   |  |
| 3.3.1 Features 25                                     |   |  |
| 3.3.2 Configuration 26                                |   |  |
| 3.4 Geofencing26                                      |   |  |
| 3.4.1 Introduction26                                  |   |  |
| 3.4.2 Interface 26                                    |   |  |
| 3.4.3 Geofence state evaluation 27                    |   |  |
| 3.4.4 Using a PIO for geofence state output 27        |   |  |
| 3.5 Logging27                                         |   |  |
| 3.5.1 Introduction27                                  |   |  |
| 3.5.2 Setting the logging system up 28                |   |  |
| 3.5.3 Information about the log28                     |   |  |
| 3.5.4 Recording 29                                    |   |  |
| 3.5.5 Retrieval 30                                    |   |  |
| 3.5.6 Command message acknowledgment31                |   |  |
| 3.6 Communication interfaces 31                       |   |  |
| 3.6.1 UART32                                          |   |  |
| 3.6.2 I2C interface33                                 |   |  |
| 3.6.3 SPI interface36                                 |   |  |
| 3.6.4 USB interface37                                 |   |  |
| 3.7 Predefined PIOs38                                 |   |  |
| 3.7.1 D_SEL38                                         |   |  |
| 3.7.2 RESET_N 38                                      |   |  |
| 3.7.3 SAFEBOOT_N38                                    |   |  |
| 3.7.4 TIMEPULSE 39                                    |   |  |
| 3.7.5 TX_READY 39                                     |   |  |
| 3.7.6 EXTINT39                                        |   |  |



| 3.7.7 GEOFENCE_STAT interface 40                              |    |
|---------------------------------------------------------------|----|
| 3.7.8 RTK_STAT interface40                                    |    |
| 3.8 Antenna supervisor 40                                     |    |
| 3.8.1 Antenna voltage control - ANT_OFF41                     |    |
| 3.8.2 Antenna short detection - ANT_SHORT_N 42                |    |
| 3.8.3 Antenna short detection auto recovery42                 |    |
| 3.8.4 Antenna open circuit detection - ANT_DETECT 43          |    |
| 3.9 Multiple GNSS assistance (MGA) 44                         |    |
| 3.9.1 Authorization 44                                        |    |
| 3.9.2 Preserving MGA and operational data during power-off 44 |    |
| 3.10 Clocks and time44                                        |    |
| 3.10.1 Receiver local time 44                                 |    |
| 3.10.2 Navigation epochs45                                    |    |
| 3.10.3 iTOW timestamps 45                                     |    |
| 3.10.4 GNSS times46                                           |    |
| 3.10.5 Time validity46                                        |    |
| 3.10.6 UTC representation47                                   |    |
| 3.10.7 Leap seconds47                                         |    |
| 3.10.8 Real-time clock48                                      |    |
| 3.10.9 Date48                                                 |    |
| 3.11 Timing functionality49                                   |    |
| 3.11.1 Time pulse49                                           |    |
| 3.11.2 Timemark 52                                            |    |
| 3.12 Security53                                               |    |
| 3.12.1 Spoofing detection / monitoring 54                     |    |
| 3.12.2 Jamming/interference detection / monitoring54          |    |
| 3.12.3 GNSS receiver integrity55                              |    |
| 3.13 u-blox protocol feature descriptions55                   |    |
| 3.13.1 Broadcast navigation data 55                           |    |
| 3.14 Forcing a receiver reset62                               |    |
| 3.15 Firmware upload 62                                       |    |
| 3.16 Spectrum analyzer63                                      |    |
|                                                               |    |
| 4 Design                                                      | 65 |
| 4.1 Pin assignment65                                          |    |
| 4.2 Power supply67                                            |    |
| 4.2.1 VCC: Main supply voltage 67                             |    |
| 4.2.2 V_BCKP: Backup supply voltage 67                        |    |
| 4.2.3 ZED-F9H power supply68                                  |    |
| 4.3 ZED-F9H minimal design68                                  |    |
| 4.4 Antenna69                                                 |    |
| 4.4.1 Antenna bias71                                          |    |
| 4.5 EOS/ESD precautions 73                                    |    |
| 4.5.1 ESD protection measures 73                              |    |
| 4.5.2 EOS precautions74                                       |    |
| 4.5.3 Safety precautions 74                                   |    |
| 4.6 Electromagnetic interference on I/O lines74               |    |
| 4.6.1 General notes on interference issues75                  |    |
| 4.6.2 In-band interference mitigation75                       |    |
| 4.6.3 Out-of-band interference 76                             |    |
| 4.7 Layout76                                                  |    |
|                                                               |    |



| 4.7.1 Placement76                                                                         |    |
|-------------------------------------------------------------------------------------------|----|
| 4.7.2 Thermal management 76                                                               |    |
| 4.7.3 Package footprint, copper and paste mask 77                                         |    |
| 4.7.4 Layout guidance 78                                                                  |    |
| 4.8 Design guidance80                                                                     |    |
| 4.8.1 General considerations 80                                                           |    |
| 4.8.2 Backup battery 80                                                                   |    |
| 4.8.3 RF front-end circuit options 80                                                     |    |
| 4.8.4 Antenna/RF input 81                                                                 |    |
| 4.8.5 Ground pads82                                                                       |    |
| 4.8.6 Schematic design 82                                                                 |    |
| 4.8.7 Layout design-in guideline 82                                                       |    |
| 5 Product<br>handling                                                                     | 83 |
| 5.1 ESD handling precautions 83                                                           |    |
| 5.2 Soldering83                                                                           |    |
| 5.3 Tapes 86                                                                              |    |
| 5.4 Reels 87                                                                              |    |
|                                                                                           |    |
| 5.5 Moisture sensitivity levels 87                                                        |    |
|                                                                                           |    |
| Appendix                                                                                  | 88 |
| A Glossary88                                                                              |    |
| B RTK configuration procedures with u-center88<br>B.1 Rover configuration with u-center88 |    |
| C Stacked patch antenna92                                                                 |    |
| Related<br>documents                                                                      | 96 |



## <span id="page-5-0"></span>**1 Integration manual overview**

This document is an important source of information on all aspects of ZED-F9H system, software and hardware design. The purpose of this document is to provide guidelines for a successful integration of the receiver with the customer's end product.



# <span id="page-6-0"></span>**2 System description**

## <span id="page-6-1"></span>**2.1 Overview**

The ZED-F9H positioning module features the u-blox F9 receiver platform, which provides multiband GNSS to high-volume industrial applications in a compact form factor. The module with integrated RTK enables precise heading, even when not moving, for automation of moving machinery in industrial and consumer-grade products in a small surface-mounted form factor of 17.0 x 22.0 x 2.4 mm.

#### <span id="page-6-2"></span>**2.1.1 GNSS-based attitude determination**

u-blox ZED-F9H high precision receiver takes GNSS precision to the next level:

- Delivers accurate heading for receiver pairs mounted on the same moving platform: 0.4 deg 50% for 1 m baseline
- Heading accuracy independent of vehicle motion and calibration
- Fast time to heading output and robust performance with multi-band, multi-constellation reception
- Compatible with ZED-F9P moving bases

Some typical applications for the ZED-F9H are shown below:

**Figure 1: Typical applications for the ZED-F9H**

#### **2.1.1.1 RTK modes of operation**

The ZED-F9H supports the following modes of operation:

**1.** ZED-F9H operating as a rover in a moving baseline setup: It receives RTCM correction data from a ZED-F9P operating as a moving base and then provides heading information.



## <span id="page-7-0"></span>**2.2 Architecture**

The ZED-F9H receiver provides all the necessary RF and baseband processing to enable multiconstellation operation. The block diagram below shows the key functionality.

### <span id="page-7-1"></span>**2.2.1 Block diagram**



#### **Figure 2: ZED-F9H block diagram**

An active antenna is mandatory with the ZED-F9H.

#### <span id="page-7-2"></span>**2.2.2 Typical ZED-F9H application setups**

The moving base feature also enables derivation of the vehicle orientation by mounting two or three GNSSreceivers onthe same vehicleplatform, i.e.byfixingthepositionof the GNSSantennas relative to each other, as illustrated in [Figure](#page-8-0) 3.

See the ZED-F9P Moving Base application note [[4](#page-95-1)] for more information on designing in and using moving base.





<span id="page-8-0"></span>

**Figure 3: ZED-F9H orientation of a vehicle in space**



**Figure 4: ZED-F9H used for drone heading determination**





**Figure 5: ZED-F9H used for automotive heading determination**



## <span id="page-10-0"></span>**3 Receiver functionality**

This section describes the ZED-F9H operational features and their configuration.

## <span id="page-10-1"></span>**3.1 Receiver configuration**

The ZED-F9H is fully configurable with UBX configuration interface keys. The configuration database in the receiver's RAM holds the current configuration, which is used by the receiver at run-time. It is constructed on start-up of the receiver from several sources of configuration. The configuration interface and the available keys are described fully in the applicable interface description [\[2\]](#page-95-2).

A configuration setting stored in RAM remains effective until power-down or reset. If stored in BBR (battery-backed RAM), the setting will be used as long as the backup battery supply remains. Configuration settings can be saved permanently in flash memory.

**CAUTION** The configuration interface has changed from earlier u-blox positioning receivers. Legacy messages are deprecated, and will not be supported in future firmware releases. Users are advised to adopt the configuration interface described in this document. See legacy UBX-CFG message fields reference section in the applicable interface description [[2](#page-95-2)].

Configuration interface settings are held in a database consisting of separate configuration items. An item is made up of a pair consisting of a key ID and a value. Related items are grouped together and identified under a common group name: CFG-GROUP-\*; a convention used in u-center and within this document. Within u-center, a configuration group is identified as "Group name" and the configuration item is identified as the "item name" under the "Generation 9 Configuration View" - "Advanced Configuration" view.

The UBX messages available to change or poll the configurations are the UBX-CFG-VALSET, UBX-CFG-VALGET, and UBX-CFG-VALDEL messages. For more information about these messages and the configuration keys see the configuration interface section in the applicable interface description [\[2](#page-95-2)].

#### <span id="page-10-2"></span>**3.1.1 Changing the receiver configuration**

All configuration messages, including legacy UBX-CFG messages, will result in a UBX-ACK-ACK or UBX-ACK-NAK response. If several configuration messages are sent without waiting for this response then the receiver may pause processing of input messages until processing of a previous configuration message has been completed. When this happens a warning message "wait for cfg ACK" will be sent to the host.

#### <span id="page-10-3"></span>**3.1.2 Default GNSS configuration**

The ZED-F9H default GNSS configuration is set as follows:

- GPS: L1C/A, L2C
- GLONASS: L1OF, L2OF
- Galileo: E1B/C, E5b
- BeiDou: B1I, B2I
- QZSS: L1C/A, L2C
- SBAS [1](#page-10-4) : L1C/A

<span id="page-10-4"></span><sup>1</sup> Supported from firmware version HDG 1.13 onwards



For more information about the default configuration, see the applicable interface description [[2](#page-95-2)].

| Interface    | Settings                                                                                                                                                                                                                                                                                       |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART1 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                                 |
|              | NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output by default.                                                                                                                                                                                                           |
|              | UBX protocol is enabled by default but no output messages are enabled by default.                                                                                                                                                                                                              |
|              | RTCM 3.3 protocol output is not supported.                                                                                                                                                                                                                                                     |
| UART1 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                                 |
|              | UBX, NMEA and RTCM 3.3 input protocols are enabled by default.                                                                                                                                                                                                                                 |
| UART2 output | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                                 |
|              | UBX protocol cannot be enabled.                                                                                                                                                                                                                                                                |
|              | RTCM 3.3 protocol output is not supported.                                                                                                                                                                                                                                                     |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                                          |
| UART2 input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.                                                                                                                                                                                                                                                 |
|              | UBX protocol cannot be enabled and will not receive UBX input messages.                                                                                                                                                                                                                        |
|              | RTCM 3.3 protocol is enabled by default.                                                                                                                                                                                                                                                       |
|              | NMEA protocol is disabled by default.                                                                                                                                                                                                                                                          |
| USB          | Default messages activated as in UART1. Input/output protocols available as in UART1.                                                                                                                                                                                                          |
| I2C          | 2<br>Fully compatible with the I2C<br>industry standard, available for communication with an external<br>host CPU or u-blox cellular modules, operated in slave mode only. Default messages activated as<br>in UART1. Input/output protocols available as in UART1. Maximum bit rate 400 kb/s. |
| SPI          | Allow communication to a host CPU, operated in slave mode only. Default messages activated as<br>in UART1. Input/output protocols available as in UART1. SPI is not available unless D_SEL pin is<br>set to low (see the D_SEL section).                                                       |

#### <span id="page-11-0"></span>**3.1.3 Default interface settings**

**Table 1: Default interface settings**

UART2 can function as the main correction interface; RTCM 3.3 (from a ZED-F9P moving base) is the default input protocol. UART2 can also optionally be configured for NMEA input or output protocol.

Refer to the applicable interface description [[2](#page-95-2)] for information about further settings.

By default the ZED-F9H outputs NMEA messages that include satellite data for all GNSS bands being received. This results in a high NMEA output load for each navigation period. Make sure the UART baud rate used is sufficient for the selected navigation rate and the number of GNSS signals being received.

#### <span id="page-11-1"></span>**3.1.4 Basic receiver configuration**

This section summarizes the basic receiver configuration most commonly used.

#### <span id="page-11-3"></span>**3.1.4.1 Communication interface configuration**

Several configuration groups allow operation mode configuration of the various communication interfaces. These include parameters for the data framing, transfer rate and enabled input/output protocols. See [Communication](#page-30-1) interfaces section for details. The configuration groups available for each interface are:

| Interface | Configuration groups                               |
|-----------|----------------------------------------------------|
| UART1     | CFG-UART1-*, CFG-UART1INPROT-*, CFG-UART1OUTPROT-* |

<span id="page-11-2"></span><sup>2</sup> I2C is a registered trademark of Philips/NXP



| Interface | Configuration groups                               |
|-----------|----------------------------------------------------|
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

All message output is additionally subject to the protocol configuration of the communication interfaces. Messages of a given protocol will not be output until the protocol is enabled for output on the interface (see [Communication](#page-11-3) interface configuration).

#### **3.1.4.3 GNSS signal configuration**

The GNSS constellations and signal bands are selected using keys from configuration group CFG-SIGNAL-\*. Each GNSS constellation can be enabled or disabled independently except for QZSS and SBAS which are dependant on GPSselection. A GNSSconstellation is considered to be enabled when the constellation enable key is set and at least one of the constellation's band keys is enabled.

ZED-F9H only supports certain combinations of constellations and bands. For all constellations, both L1 and L2 bands must either be enabled or disabled. BeiDou B2 is the exception (can either have BeiDou B1+B2 or B1-only). Unsupported combinations will be rejected with a UBX-ACK-NAK and the warning: "invalid sig cfg" will be sent via UBX-INF and NMEA-TXT messages (if enabled).

The following table shows possible configuration key combinations for the GPS constellation.

| Constellation key  | Band key                | Band key               | Constellation              |  |
|--------------------|-------------------------|------------------------|----------------------------|--|
| CFG-SIGNAL-GPS_ENA | CFG-SIGNAL-GPS_L1CA_ENA | CFG-SIGNAL-GPS_L2C_ENA | enabled?                   |  |
| false (0)          | false (0)               | false (0)              | no                         |  |
| false (0)          | false (0)               | true (1)               | no                         |  |
| false (0)          | true (1)                | false (0)              | no                         |  |
| false (0)          | true (1)                | true (1)               | no                         |  |
| true (1)           | false (0)               | false (0)              | no                         |  |
| true (1)           | false (0)               | true (1)               | Unsupported<br>combination |  |



| Constellation key<br>CFG-SIGNAL-GPS_ENA | Band key<br>CFG-SIGNAL-GPS_L1CA_ENA | Band key<br>CFG-SIGNAL-GPS_L2C_ENA | Constellation<br>enabled?  |
|-----------------------------------------|-------------------------------------|------------------------------------|----------------------------|
| true (1)                                | true (1)                            | false (0)                          | Unsupported<br>combination |
| true (1)                                | true (1)                            | true (1)                           | yes                        |

**Table 3: Example of possible values of configuration items for the GPS constellation**

#### **3.1.4.4 Antenna supervisor configuration**

This section describes the antenna supervisor configuration, its use and restrictions.

The antenna supervisor is used to control an active antenna. The configuration of the antenna supervisor allows the following:

- Control voltage supply to the antenna, which allows the antenna supervisor to cut power to the antenna in the event of a short circuit or optimize power to the antenna in power save mode
- Detect a short circuit in the antenna and auto recover the antenna supply in such an event
- Detect an open antenna, which can be used to indicate if the antenna has been disconnected

See the table below for a description of the configuration items related to the antenna supervisor operation.

| Configuration item                                           | Description                                                                                     | Comments                                                                              |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| CFG-HW-ANT_CFG_VOLTCTRL                                      | Enable active antenna voltage control                                                           |                                                                                       |
| CFG-HW-ANT_CFG_SHORTDET                                      | Enable short circuit detection                                                                  |                                                                                       |
| CFG-HW-ANT_CFG_SHORTDET_POL Short antenna detection polarity |                                                                                                 | Set to 1 if the required logic polarity is<br>active-low (default)                    |
| CFG-HW-ANT_CFG_OPENDET                                       | Enable open circuit detection                                                                   |                                                                                       |
| CFG-HW-ANT_CFG_OPENDET_POL                                   | Open antenna detection polarity                                                                 | Set to 1 if the required logic polarity is<br>active-low (default)                    |
| CFG-HW-ANT_CFG_PWRDOWN                                       | Power down antenna supply if short<br>circuit is detected                                       | Requires CFG-HW<br>ANT_CFG_VOLTCTRL and CFG-HW<br>ANT_CFG_SHORTDET to be enabled.     |
| CFG-HW-ANT_CFG_PWRDOWN_POL Power down antenna logic polarity |                                                                                                 | Set to 1 if the required logic polarity is<br>active-high (default)                   |
| CFG-HW-ANT_CFG_RECOVER                                       | Enable auto recovery in the event of a<br>short circuit                                         | To use this feature, enable short<br>circuit detection and CFG-HW<br>ANT_CFG_PWRDOWN. |
| CFG-HW-ANT_SUP_SWITCH_PIN                                    | PIO-Pin (PIO number) used for switching<br>antenna supply                                       | It is recommended that you use the<br>default PIO and assigned pin                    |
| CFG-HW-ANT_SUP_SHORT_PIN                                     | PIO-Pin (PIO number) used for detecting<br>a short-circuit in the antenna supply                | It is recommended that you use the<br>default PIO and assigned pin                    |
| CFG-HW-ANT_SHORT_THR                                         | Defines the threshold (in mV) for the<br>antenna supervisor when a short status<br>is detected. | Only applicable for the discrete<br>antenna supervisor (based on MADC)                |
| CFG-HW-ANT_OPEN_THR                                          | Defines the threshold (in mV) for the<br>antenna supervisor when an open<br>status is detected. | Only applicable for the discrete<br>antenna supervisor (based on MADC)                |
| CFG-HW-ANT_ENGINE                                            | With this configuration key, the antenna<br>supervisor engine can be selected.                  | Default value is "EXT"                                                                |

#### **Table 4: Antenna supervisor configuration**

It is possible to obtain the status of the antenna supervisor through the UBX-MON-RF message. Moreover, any changes in the status of the antenna supervisor are reported to the host interface in the form of notice messages. See the applicable interface description [\[2\]](#page-95-2) for *antStatus* and *antPower* field description.



| Status   | Description                       |
|----------|-----------------------------------|
| OFF      | Antenna is off                    |
| ON       | Antenna is on                     |
| DONTKNOW | Antenna power status is not known |

**Table 5: Antenna power status**

### <span id="page-14-0"></span>**3.1.5 Moving base RTK configuration**

Moving base (MB) RTK technology introduces the concept of a ZED-F9P moving base and a ZED-F9H rover. In such a setup, the base and the rover are mounted on the same moving platform. The ZED-F9P moving base sends correction to the ZED-F9H rover, enabling it to compute its heading relative to the base, i.e. the platform heading, with high accuracy.

In the MB RTK context, the base and rover receivers are referred to as MB base and MB rover respectively.

After describing the RTCM protocol and corresponding supported message types, this section describes how to configure the ZED-F9H high precision receiver as an MB rover receiver.

See the ZED-F9P Moving Base application note [[4](#page-95-1)] for more information on designing in, configuring and using a moving base setup.

#### **3.1.5.1 ZED-F9P base RTCM corrections for the ZED-F9H**

RTCM is a binary data protocol for communicating GNSS correction information. The ZED-F9H high precision receiver only supports RTCM corrections provided by a ZED-F9P base receiver operating in moving-base mode.

The following ZED-F9P moving-base messages are required:

- RTCM 4072.0 [3](#page-14-1) (Reference station PVT)
- MSM4[4](#page-14-2) or MSM7 GNSS observations for systems configured on the rover
- GLONASS code phase biases message RTCM 1230 if GLONASS is configured on the rover

#### **3.1.5.2 List of supported RTCM input messages**

| Message type | Description                                                                |  |
|--------------|----------------------------------------------------------------------------|--|
| RTCM 1074    | GPS MSM4                                                                   |  |
| RTCM 1077    | GPS MSM7                                                                   |  |
| RTCM 1084    | GLONASS MSM4                                                               |  |
| RTCM 1087    | GLONASS MSM7                                                               |  |
| RTCM 1094    | Galileo MSM4                                                               |  |
| RTCM 1097    | Galileo MSM7                                                               |  |
| RTCM 1124    | BeiDou MSM4                                                                |  |
| RTCM 1127    | BeiDou MSM7                                                                |  |
| RTCM 1230    | GLONASS code-phase biases                                                  |  |
| RTCM 4072.0  | Reference station PVT (u-blox proprietary RTCM Message)                    |  |
| RTCM 4072.1  | Additional reference station information (u-blox proprietary RTCM Message) |  |
|              | Only valid with firmware version HDG 1.12.                                 |  |

#### **Table 6: ZED-F9H supported input RTCM version 3.3 messages**

<span id="page-14-1"></span><sup>3</sup> Message 4072.1 it is also necessary if using firmware version HDG 1.12

<span id="page-14-2"></span><sup>4</sup> MSM4 messages in moving-base mode are supported from firmware version HDG 1.13 onwards



#### **3.1.5.3 MB rover operation**

In its default configuration, the ZED-F9H will attempt to provide the best heading accuracy depending on the received correction data from a ZED-F9P base in moving base mode. It will enter RTK float mode shortly after it starts receiving an input stream of RTCM correction messages. Once the rover has resolved the carrier phase ambiguities, it will enter RTK fixed mode. When in this mode, the relative heading between base and rover can be expected to be accurate. The time period between RTK float and RTK fixed operation is referred to as the convergence time. Note that the convergence time is affected by multipath and satellite visibility at both rover and base station.

The ZED-F9H should receive RTCM corrections matching its GNSS signal configuration to function optimally. The rover requires both base station observation (MSM4 or MSM7 messages) and position message (RTCM 4072.0) in order to attempt ambiguity fixes. The rover will attempt to provide RTK fixed operation when sufficient number of ambiguities are resolved. If phase lock on sufficient number of signals cannot be maintained, the rover will drop back to RTK float mode. The rover will continue to attempt to resolve carrier ambiguities and revert to RTK fixed mode once the minimum number of signals has been restored.

The RTK mode that an RTK rover operates in can be configured through the CFG-NAVHPG-DGNSSMODE configuration item. The following two RTK modes are available:

- RTK fixed: The rover will attempt to fix ambiguities whenever possible.
- RTK float: The rover will estimate the ambiguities as float but will make no attempts at fixing them.
- To provide accurate heading information RTK fixed mode should be kept.

The received correction messages stream should comply with the following:

- The reference station ID in the reference station message (RTCM 4072.0) must match that used in the MSM observation messages. Otherwise, the rover cannot compute its position. With a direct connection between the ZED-F9P moving base and the ZED-F9H rover this will not be an issue. On a more complex networked communication system such as automotive or a shipping vessel this needs to be considered.
- In order to fix GLONASS ambiguities the correction stream must contain RTCM message 1230. Otherwise, the carrier ambiguities will be estimated as float even when set to operate in RTK fixed mode. This will significantly degrade heading accuracy.

CFG-RTCM-DF003\_IN [5](#page-15-0) can be used to configure the desired reference station ID and CFG-RTCM-DF003\_IN\_FILTER [5](#page-15-0) can be used to configure how strict the filtering should be (RELAXED is the recommended setting).

#### **3.1.5.3.1 Message output in MB RTK mode**

When operating in MB RTK rover mode users should take note of the modified information within the following NMEA and UBX messages:

- NMEA-GGA: The quality field will be 4 for RTK fixed and 5 for RTK float (see NMEA position fix flags in interface description). The age of differential corrections and base station ID will be set.
- NMEA-GLL, NMEA-VTG: The posMode indicator will be D for RTK float and RTK fixed (see NMEA position fix flags in interface description).
- NMEA-RMC, NMEA-GNS: The posMode indicator will be F for RTK float and R for RTK fixed (see NMEA position fix flags in interface description).
- UBX-NAV-PVT: The carrSoln flag will be set to 1 for RTK float and 2 for RTK fixed. The age of differential corrections will be reported.

<span id="page-15-0"></span><sup>5</sup> CFG-RTCM-DF003\_\* items are supported from firmware version HDG 1.13 onwards



- UBX-NAV-RELPOSNED
  - The diffSoln and relPosValid flags will be set
  - The carrSoln flag will be set to 1 for RTK float and 2 for RTK fixed
  - The isMoving flag will be set
  - The relPosValid flag will be set if the rover managed to get the time-matched observations in time and process the moving base solution
  - The length of the relative position vector and its accuracy will be output
  - The relative position vector will be normalized to 1m and the relPosNormalized flag will be set
  - The relPosHeading and its accuracy will be output
  - The relPosHeadingValid flag will be set unless the length of the relative position vector and/ or its accuracy are not sufficient to reliably derive the heading information
- UBX-NAV-SAT
  - The diffCorr flag will be set for satellites with valid RTCM data
  - The rtcmCorrUsed, prCorrUsed, and crCorrUsed flags will be set for satellites for which the RTCM corrections have been applied
- UBX-NAV-SIG
  - For signals to which the RTCM corrections have been applied, the correction source will be set to RTCM3 OSR and the crUsed, prCorrUsed, and crCorrUsed flags will be set
- UBX-NAV-STATUS
  - The diffSoln flag and the diffCorr flag will be set
  - The carrSoln flag will be set to 1 for RTK float and 2 for RTK fixed
- No position information will be output in the messages. If position is required, consider the ZED-F9P receiver as an alternative.

An illustrated procedure for configuring a rover using u-center is shown in the [Appendix](#page-87-3) C.2.

#### **3.1.5.4 Rover operation in MB RTK mode**

When operating in MB RTK mode, the following performance limitations may apply:

- A moving base receiver typically experiences worse GNSS tracking than a static base receiver in an open-sky environment and therefore the MB RTK performance may be degraded.
- The MB rover will wait as long as possible to compute a navigation solution, possibly lowering the navigation rate all the way to 1 Hz while doing so. If not time-matched observations are received in time, the receiver will flag the relative position as invalid.
- The achievable navigation update rate of the MB RTK solution is limited by the communication link latency. Latency here refers to the delay we have in getting the RTCM messages on the rover from the time they are sent from the base station.
- It is a good idea to try and minimize the latency in the communication link, especially if trying to achieve high navigation update rate. As a rule of thumb, the communication link latency should be less than the desired navigation update period minus 50 ms.
- If the communication link latency is too high to achieve the configured navigation update rate the receiver will lower the navigation update rate until it reaches 1 Hz.
- If the communication link latency is too high for 1 Hz rover operation, the receiver will declare the relative position as invalid.
- To ensure that the moving base processing works, the MB base and rover must use the same navigation update rate and measurement rate.
- With firmware version HDG 1.12, the time-matched observations must be received within 700 ms. When the limit is exceeded, the MB reference observations and/or position will be extrapolated for up to 3 s before falling back to standard GNSS operation. The refPosMiss and refObsMiss flags will be set for epochs during which the extrapolated base position or



observations have been used. These flags are no longer supported from firmware version HDG 1.13 onwards.

#### <span id="page-17-0"></span>**3.1.6 Legacy configuration interface compatibility**

Although there is some backwards compatibility for the legacy UBX-CFG configuration messages, users are strongly advised to adopt the configuration interface described in this document.

See Legacy UBX-CFG message fields reference section in the applicable interface description [[2\]](#page-95-2).

#### <span id="page-17-1"></span>**3.1.7 Navigation configuration**

This section presents various configuration options related to the navigation engine. These options can be configured through CFG-NAVSPG-\* configuration keys.

#### **3.1.7.1 Platform settings**

u-blox receivers support different dynamic platform models to adjust the navigation engine to the expected application environment. These platform settings can be changed dynamically without performing a power cycle or reset. The settings improve the receiver's interpretation of the measurements and thus provide a more accurate heading output. Setting the receiver to an unsuitable platform model for the given application environment is likely to result in a loss of receiver performance and heading accuracy.

The dynamic platform model can be configured through the CFG-NAVSPG-DYNMODEL configuration item. The supported dynamic platform models and their details can be seen in [Table](#page-17-2) [7](#page-17-2) and [Table](#page-17-3) 8 below.

<span id="page-17-2"></span>

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

**Table 7: Dynamic platform models**

<span id="page-17-3"></span>

| Platform     | Max altitude [m] | Max horizontal<br>velocity [m/s] | Max vertical velocity<br>[m/s] | Sanity check type     | Max<br>position<br>deviation |
|--------------|------------------|----------------------------------|--------------------------------|-----------------------|------------------------------|
| Portable     | 12000            | 310                              | 50                             | Altitude and velocity | Medium                       |
| Stationary   | 9000             | 10                               | 6                              | Altitude and velocity | Small                        |
| Pedestrian   | 9000             | 30                               | 20                             | Altitude and velocity | Small                        |
| Automotive   | 6000             | 100                              | 15                             | Altitude and velocity | Medium                       |
| At sea       | 500              | 25                               | 5                              | Altitude and velocity | Medium                       |
| Airborne <1g | 80000            | 100                              | 6400                           | Altitude              | Large                        |
| Airborne <2g | 80000            | 250                              | 10000                          | Altitude              | Large                        |



| Platform     | Max altitude [m] | Max horizontal<br>velocity [m/s] | Max vertical velocity<br>[m/s] | Sanity check type     | Max<br>position<br>deviation |
|--------------|------------------|----------------------------------|--------------------------------|-----------------------|------------------------------|
| Airborne <4g | 80000            | 500                              | 20000                          | Altitude              | Large                        |
| Wrist        | 9000             | 30                               | 20                             | Altitude and velocity | Medium                       |

#### **Table 8: Dynamic platform model details**

Applying dynamic platform models designed for high acceleration systems (e.g. airborne <2g) can result in a higher standard deviation in the reported position.

If a sanity check against a limit of the dynamic platform model fails, then the position solution is invalidated. [Table](#page-17-3) 8 above shows the types of sanity checks which are applied for a particular dynamic platform model.

#### **3.1.7.2 Navigation input filters**

The navigation input filters in CFG-NAVSPG-\* configuration group provide the input data of the navigation engine.

These settings are primarily for the initial standard 2D/3D only GNSS fix indication when not in RTK float/fixed mode.

| Configuration item                                     | Description                                                                                                                                                                                                          |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFG-NAVSPG-FIXMODE                                     | By default, the receiver calculates a 3D position fix if possible but reverts to 2D<br>position if necessary (auto 2D/3D). The receiver can be forced to only calculate 2D<br>(2D only) or 3D (3D only) positions.   |
| CFG-NAVSPG-CONSTR_ALT, CFG<br>NAVSPG-CONSTR_ALTVAR     | The fixed altitude is used if fixMode is set to 2D only. A variance greater than zero<br>must also be supplied.                                                                                                      |
| CFG-NAVSPG-INFIL_MINELEV                               | Minimum elevation of a satellite above the horizon in order to be used in the<br>navigation solution. Low elevation satellites may provide degraded accuracy, due to<br>the long signal path through the atmosphere. |
| CFG-NAVSPG-INFIL_NCNOTHRS,<br>CFG-NAVSPG-INFIL_CNOTHRS | A navigation solution will only be attempted if there are at least the given number of<br>SVs with signals at least as strong as the given threshold.                                                                |

#### **Table 9: Navigation input filter parameters**

If the receiver only has three satellites for calculating a position, the navigation algorithm uses a constant altitude to compensate for the missing fourth satellite. When a satellite is lost after a successful 3D fix (min four satellites available), the altitude is kept constant at the last known value. This is called a 2D fix.

u-blox receivers do not calculate any navigation solution with less than three satellites.

#### <span id="page-18-0"></span>**3.1.7.3 Navigation output filters**

The result of a navigation solution is initially classified by the fix type (as detailed in the fixType field of UBX-NAV-PVT message). This distinguishes between failures to obtain a fix at all ("No Fix") and cases where a fix has been achieved, which are further subdivided into specific types of fixes (e.g. 2D, 3D, dead reckoning).

The ZED-F9H firmware does not support the dead reckoning position fix type.

Where a fix has been achieved, a check is made to determine whether the fix should be classified as valid or not. A fix is only valid if it passes the navigation output filters as defined in CFG-NAVSPG-OUTFIL. In particular, both PDOP and accuracy values must be below the respective limits.

Important: Users are recommended to check the gnssFixOK flag in the UBX-NAV-PVT or the NMEA valid flag. Fixes not marked valid should not be used.



UBX-NAV-STATUS message also reports whether a fix is valid in the gpsFixOK flag. This message has only been retained for backwards compatibility and users are recommended to use the UBX-NAV-PVT message.

The CFG-NAVSPG-OUTFIL\_TDOP and CFG-NAVSPG-OUTFIL\_TACC configuration items also define [TDOP](#page-87-1) and time accuracy values that are used in order to establish whether a fix is regarded as locked to GNSS or not, and as a consequence of this, which time pulse setting has to be used. Fixes that do not meet both criteria will be regarded as unlocked to GNSS, and the corresponding time pulse settings of CFG-TP-\* configuration group will be used to generate a time pulse.

When in RTK float/fixed mode there are no navigation output filter settings for this mode. This is handled internally in the RTK core.

#### **3.1.7.3.1 Speed (3D) low-pass filter**

The CFG-ODO-OUTLPVEL configuration item offers the possibility to activate a speed (3D)low-pass filter. The output of the speed low-pass filter is published in the UBX-NAV-VELNED message (speed field). The filtering level can be set via the CFG-ODO-VELLPGAIN configuration item and must be comprised between 0 (heavy low-pass filtering) and 255 (weak low-pass filtering).

The internal filter gain is computed as a function of speed. Therefore, the level as defined in the CFG-ODO-VELLPGAIN configuration item defines the nominal filtering level for speeds below 5 m/s.

#### **3.1.7.3.2 Course over ground low-pass filter**

The CFG-ODO-OUTLPCOG configuration item offers the possibility to activate a course over ground low-pass filter when the speed is below 8 m/s. The output of the course over ground (also named heading of motion 2D) low-pass filter is published in the UBX-NAV-PVT message (headMot field), UBX-NAV-VELNED message (heading field), NMEA-RMC message (cog field) and NMEA-VTG message (cogt field).The filtering level can be set via the CFG-ODO-COGLPGAIN configuration item and must be comprised between 0 (heavy low-pass filtering) and 255 (weak low-pass filtering).

The filtering level as defined in the CFG-ODO-COGLPGAIN configuration item defines the filter gain for speeds below 8 m/s. If the speed is higher than 8 m/s, no course over ground low-pass filtering is performed.

#### **3.1.7.3.3 Low-speed course over ground filter**

The CFG-ODO-USE\_COG activates this feature and the CFG-ODO-COGMAXSPEED, CFG-ODO-COGMAXPOSACC configuration items offer the possibility to configure a low-speed course over ground filter (also named heading of motion 2D). This filter derives the course over ground from position at very low speed. The output of the low-speed course over ground filter is published in the UBX-NAV-PVT message (headMot field), UBX-NAV-VELNED message (heading field), NMEA-RMC message (cog field) and NMEA-VTG message (cogt field). If the low-speed course over ground filter is not configured, then the course over ground is computed as described in section [Freezing](#page-21-0) the course over [ground](#page-21-0).

#### **3.1.7.4 Static hold**

Static hold mode allows the navigation algorithms to decrease the noise in the position output when the velocity is below a pre-defined "Static Hold Threshold". This reduces the position wander caused by environmental factors such as multi-path and improves position accuracy especially in stationary applications. By default, static hold mode is disabled.

If the speed drops below the defined "Static Hold Threshold", the static hold mode will be activated. Once static hold mode has been entered, the position output is kept static and the velocity is set to zero until there is evidence of movement again. Such evidence can be velocity, acceleration, changes



of the valid flag (e.g. position accuracy estimate exceeding the position accuracy mask, see also section [Navigation](#page-18-0) output filters), position displacement, etc.

The CFG-MOT-GNSSDIST\_THRS configuration item additionally allows for configuration of distance threshold. If the estimated position is farther away from the static hold position than this threshold, static mode will be quit.The CFG-MOT-GNSSSPEED\_THRSconfiguration item allows you to set a speed that the static hold will release.



**Figure 6: Position publication in static hold mode**





**Figure 7: Flowchart of the static hold mode**

#### <span id="page-21-0"></span>**3.1.7.5 Freezing the course over ground**

If the low-speed course over ground filter is deactivated or inactive, the receiver derives the course over ground from the GNSS velocity information. If the velocity cannot be calculated with sufficient accuracy (e.g., with bad signals) or if the absolute speed value is very low (under 0.1 m/s) then the course over ground value becomes inaccurate too. In this case the course over ground value is frozen, i.e. the previous value is kept and its accuracy is degraded over time. These frozen values will not be output in the NMEA messages NMEA-RMC and NMEA-VTG unless the NMEA protocol is explicitly configured to do so (see NMEA protocol configuration in the applicable interface description [\[2\]](#page-95-2)).





**Figure 8: Flowchart of the course over ground freezing**

#### **3.1.7.6 ZED-F9H position output**

The ZED-F9H does not provide position information in any output message. For backwards compatibility, UBX and NMEA messages with position information are still available. Note that in such messages the position information fields will be set to NULL (NMEA), or to 0/0/0 (UBX, NMEA) or to corresponding XYZ value (UBX). Affected messages are the following:

- UBX-NAV-PVT
- UBX-NAV-POSLLH
- UBX-NAV-POSECEF
- UBX-NAV-HPPOSLLH
- UBX-NAV-HPPOSECE
- NMEA-RMC
- NMEA-GLL
- NMEA-GGA
- NMEA-GNS

See the ZED-F9H Interface description [[2](#page-95-2)].

## <span id="page-22-0"></span>**3.2 SBAS**

Supported from firmware version HDG 1.13 onwards

The ZED-F9H is capable of receiving multiple SBAS signals concurrently, even from different SBAS systems (WAAS, EGNOS, MSAS, etc.). They can be tracked and used for navigation simultaneously. Every SBAS satellite that broadcasts ephemeris or almanac information can be used for navigation, just like a normal GNSS satellite.

For receiving correction data, the ZED-F9H automatically chooses the best SBAS satellite as its primary source. It will select only one since the information received from other SBAS satellites is redundant and could be inconsistent. The selection strategy is determined by the proximity of the



satellites, the services offered by the satellite, the configuration of the receiver (test mode allowed/ disallowed, integrity enabled/disabled) and the signal link quality to the satellite.

If corrections are available fromthe chosenSBASsatellite and used in the navigation calculation, the differential status will be indicated in several output messages such as UBX-NAV-PVT, UBX-NAV-STATUS, UBX-NAV-SAT, NMEA-GGA, NMEA-GLL, NMEA-RMC and NMEA-GNS (see the applicable interface description [\[2\]](#page-95-2)). The message UBX-NAV-SBAS provides detailed information about which corrections are available and applied.

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

#### **Table 10: Supported SBAS messages**

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
| CFG-SBAS-USE_DIFFCORR  | Combined enable/disable switch for fast-, long-term and ionosphere corrections |
| CFG-SBAS-USE_INTEGRITY | Apply integrity information data                                               |





| Parameter            | Description                                           |
|----------------------|-------------------------------------------------------|
| CFG-SBAS-PRNSCANMASK | Allows selectively enabling/disabling SBAS satellites |

#### **Table 11: SBAS configuration parameters**

- When SBAS integrity data are applied, the navigation engine stops using all signals for which no integrity data are available (including all non-GPS signals). It is not recommended to enable SBAS integrity on borders of SBAS service regions in order not to inadvertently restrict the number of available signals.
- SBAS integrity information is required for at least 5 GPS satellites. If this condition is not met, SBAS integrity data will not be applied.
- SBAS is only used if no correction services are available. If the connection stream is lost during the operation, the receiver will switch to using the SBAS corrections after the time set in CFG-NAVSPG-CONSTR\_DGNSSTO (60 s by default) has elapsed.
- When the receiver switches from a solution using correction data to a standard position solution, the reference frame of the output position will switch from the one of the correction data to that of the standard position solution. For an SBAS solution this reference frame will be aligned within a few cm of WGS84 (and modern ITRF realizations).

### <span id="page-24-0"></span>**3.3 QZSS SLAS**

Supported from firmware version HDG 1.13 onwards

QZSS SLAS (Sub-meter Level Augmentation Service) is an augmentation technology, which provides correction data for pseudoranges of GPS, QZSS, and other major GNSS satellites. The correction stream is transmitted on the L1S signal at the L1 frequency (1575.42 MHz).

For more information on QZSS SLAS, visit the web site [qzss.go.jp/en/](http://qzss.go.jp/en/).

QZSS SLAS is only used if no other correction services are available (e.g. RTCM, SPARTN, CLAS). If the connection stream is lost during the operation, the receiver will switch to use the SLAS corrections after the time set in CFG-NAVSPG-CONSTR\_DGNSSTO (60 s by default) has elapsed.

#### <span id="page-24-1"></span>**3.3.1 Features**

Multiple QZSS SLAS signals can be received simultaneously.

When receiving QZSS SLAS correction data, the ZED-F9H high precision receiver will autonomously select the best QZSS satellite. The selection strategy is determined by the quality of the QZSS L1S signals, the receiver configuration (test mode allowed or not), and the location of the receiver with respect to the QZSS SLAS coverage area. When outside of this coverage area, the receiver will likely fall back to using SBAS corrections.

If QZSS SLAS corrections are used in the navigation solution, the differential status will be indicated in several output messages such as UBX-NAV-PVT, UBX-NAV-STATUS, UBX-NAV-SAT, NMEA-GGA, NMEA-GLL, NMEA-RMC and NMEA-GNS (see the applicable interface description [[2](#page-95-2)]). The message UBX-NAV-SLAS provides detailed information about which corrections are available and applied.

| Message type | Message content                |
|--------------|--------------------------------|
| 0            | Test mode                      |
| 47           | Monitoring station information |
| 48           | PRN mask                       |
| 49           | Data issue number              |



| Message type | Message content  |  |
|--------------|------------------|--|
| 50           | DGPS correction  |  |
| 51           | Satellite health |  |
|              |                  |  |

**Table 12: Supported QZSS L1S SLAS messages for navigation enhancing**

#### <span id="page-25-0"></span>**3.3.2 Configuration**

To enable support for the necessary QZSS L1S signal, use the CFG-SIGNAL-QZSS\_L1S\_ENA configuration item.To configure further QZSSSLASfunctionalities, use the CFG-QZSS-USE\_SLAS\* configuration items.

| Parameter                        | Description                                                                                                                                                                                                                                                                                                                               |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFG-QZSS-USE_SLAS_DGNSS          | Apply QZSS SLAS corrections                                                                                                                                                                                                                                                                                                               |
| CFG-QZSS-USE_SLAS_TESTMODE       | Allow the correction provided by QZSS satellites that are in test mode                                                                                                                                                                                                                                                                    |
| CFG-QZSS<br>USE_SLAS_RAIM_UNCORR | If this configuration is set, the receiver will try to estimate the position by using only<br>corrected measurements; if all corrected measurements are not available, it will not<br>use any corrections. If this configuration is not set, the receiver will mix corrected<br>and uncorrected measurements for the navigation solution. |

**Table 13: QZSS SLAS configuration parameters**

If the RAIM option is set, other GNSS time systems than the QZSS time system cannot be observed by measurements.

## <span id="page-25-1"></span>**3.4 Geofencing**

#### <span id="page-25-2"></span>**3.4.1 Introduction**



#### **Figure 9: Geofence**

The geofencing feature allows for the configuration of up to four circular areas (geofences) on the Earth's surface. The receiver will then evaluate for each of these areas whether the current position lies within the area or not and signal the state via UBX messaging and PIO toggling.

#### <span id="page-25-3"></span>**3.4.2 Interface**

Geofencing can be configured using the CFG-GEOFENCE-\* configuration group. The geofence evaluation is active whenever there is at least one geofence configured.



The current state of each geofence plus the combined state is output in UBX-NAV-GEOFENCE with every navigation epoch.

#### <span id="page-26-0"></span>**3.4.3 Geofence state evaluation**

With every navigation epoch the receiver will evaluate the current solution's position versus the configured geofences. There are three possible outcomes for each geofence:

- *Inside* The position is inside the geofence with the configured confidence level
- *Outside* The position lies outside of the geofence with the configured confidence level
- *Unknown* There is no valid position solution or the position uncertainty does not allow for unambiguous state evaluation

The position solution uncertainty (standard deviation) is multiplied with the configured confidence sigma level and taken into account when evaluating the geofence state (red circle in [Figure](#page-26-4) 10).

<span id="page-26-4"></span>

**Figure 10: Geofence states**

The combined state for all geofences is evaluated as the combination (Union) of all geofences:

- *Inside* The position lies inside of at least one geofence
- *Outside* The position lies outside of all geofences
- *Unknown* All remaining states

A pin is made available to indicate the status of the geofence. See the [GEOFENCE\\_STAT](#page-39-0) interface.

#### <span id="page-26-1"></span>**3.4.4 Using a PIO for geofence state output**

This feature can be used, for example, for waking up a sleeping host when a defined geofence condition is reached. The receiver will toggle the assigned pin according to the combined geofence state. Due to hardware restrictions, the geofence unknown state is not configurable and is always represented as HIGH. If the receiver is in the software backup mode or in the reset state, the pin will go to HIGH accordingly. The meaning of the LOW state can be configured using the CFG-GEOFENCE-PINPOL configuration item.

The CFG-GEOFENCE-PIN configuration item refers to a PIO and not a physical device pin. The PIO number must be set so that it is mapped to the assigned geofence state device pin. The ZED-F9H is assigned PIO3 that is assigned to module pin 19.

## <span id="page-26-2"></span>**3.5 Logging**

#### <span id="page-26-3"></span>**3.5.1 Introduction**

The logging feature allows position fixes and arbitrary byte strings from the host to be logged in the receiver's flash memory. Logging of position fixes happens independently of the host system, and can continue while the host is powered down.

The following table lists all the logging-related messages:

| Message        | Description                                         |
|----------------|-----------------------------------------------------|
| UBX-LOG-CREATE | Creates a log file and activates the logging system |



| Message                                              | Description                                                       |
|------------------------------------------------------|-------------------------------------------------------------------|
| UBX-LOG-ERASE                                        | Erases a log file and deactivates the logging subsystem           |
| UBX-LOG-INFO                                         | Provides information about the logging system                     |
| UBX-LOG-STRING                                       | Enables a host process to write a string of bytes to the log file |
| Table 14: Logging control and configuration messages |                                                                   |
| Message                                              | Description                                                       |
| UBX-LOG-RETRIEVE                                     | Starts the log retrieval process                                  |
| UBX-LOG-RETRIEVEPOS                                  | A position log entry returned by the receiver                     |
| UBX-LOG-RETRIEVEPOSEXTRA                             | Odometer position data                                            |
| UBX-LOG-RETRIEVESTRING                               | A byte string log entry returned by the receiver                  |

UBX-LOG-FINDTIME Finds the index of the first entry (given time)

**Table 15: Logging retrieval messages**

#### <span id="page-27-0"></span>**3.5.2 Setting the logging system up**

An empty log can be created using the UBX-LOG-CREATE message and a log can be deleted with the UBX-LOG-ERASE message. The logging system will only run if a log is in existence, so most logging messages will be rejected with a UBX-ACK-NAK message if there is no log present. Only one log can be created at any one time so a UBX-ACK-NAK message will be returned if a log already exists. The message specifies the maximum size of the log in bytes (with some pre-set values provided). Both the logging subsystem and the receiver file-store have implementation overheads, so the total space available for log entries will be somewhat smaller than the size specified.

UBX-LOG-CREATE also allows the log to be specified as a circular log. If the log is circular, a set of older log entries will be deleted when it fills up, and the space freed up is used for new log entries. By contrast, if a non-circular log becomes full then new entries which do not fit will be rejected. UBX-LOG-CREATE also causes the logging system to start up so that further logging messages can be processed. The logging system will start up automatically on power-up if there is a log in existence. The log will remain in the receiver until specifically erased using the UBX-LOG-ERASE message.

The CFG-LOGFILTER-\* configuration group controls whether logging of entries is currently enabled and selects position fix messages for logging.



**Figure 11: The top level active/inactive states of the logging subsystem**

#### <span id="page-27-1"></span>**3.5.3 Information about the log**

The receiver can be polled for a UBX-LOG-INFO message which will give information about the log. This will include the maximum size that the log can grow to (which, due to overheads, will be smaller than that requested in UBX-LOG-CREATE) and the amount of log space currently occupied. It will also report the number of entries currently in the log together with the time and date of the newest and oldest messages that have a valid time stamp.



Log entries are compressed and have housekeeping information associated with them, so the actual space occupied by log messages may be difficult to predict.The minimum size for a position fix entry is 9 bytes and the maximum 24 bytes, the typical size is 10 or 11 bytes. If the odometer is enabled then this will use at least another three bytes per fix.

Each log also has a fixed overhead which is dependent on the log type. The approximate size of this overhead is shown in the following table.

| Log type     | Overhead    |
|--------------|-------------|
| circular     | Up to 40 kB |
| non-circular | Up to 8 kB  |

#### **Table 16: Log overhead size**

The number of entries that can be logged in any given flash size can be estimated as follows:

Approx. number of entries = (flash size available for logging - log overhead)/typical entry size

For example, if 1500 kB of flash is available for logging (after other flash usage such as the firmware image is taken into account) a non-circular log would be able to contain approximately 139000 entries: ((1500\*1024)- (8\*1024))/11 = 138891.

#### <span id="page-28-0"></span>**3.5.4 Recording**

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

#### <span id="page-29-0"></span>**3.5.5 Retrieval**

UBX-LOG-RETRIEVE starts the process which allows the receiver to output log entries. UBX-LOG-INFO may be helpful to a host system in order to understand the current log status before retrieval is started.

Once retrieval has started, one message will be output from the receiver for each log entry requested. Sending any logging message to the receiver during retrieval will cause the retrieval to stop before the message is processed.

To maximize the speed of transfer it is recommended that a high communications data rate is used and GNSS processing is stopped during the transfer (see UBX-CFG-RST).

UBX-LOG-RETRIEVE can specify a start-entry index and entry-count. The maximum number of entries that can be returned in response to a single UBX-LOG-RETRIEVE message is 256. If more entries than this are required the message will need to be sent multiple times with different startEntry indices. It might be useful to stop recording via CFG\_LOGFILTER-RECORD\_ENA while retrieving log entries from a circular log to avoid deletion of the requested entries between the request and transmission.

The receiver will send a UBX-LOG-RETRIEVEPOS message for each position fix log entry and a UBX-LOG-RETRIEVESTRING message for each string log entry. If the odometer was enabled at the time a position was logged, then a UBX-LOG-RETRIEVEPOSEXTRA will also be sent. Messages will be sent in the order inwhich theywere logged, so UBX-LOG-RETRIEVEPOSand UBX-LOG-RETRIEVESTRING messages may be interspersed in the message stream.



The UBX-LOG-FINDTIME message can be used to search a log for the index of the first entry less than or equal to the given time. This index can then be used with the UBX-LOG-RETRIEVE message to provide timebased retrieval of log entries.

#### <span id="page-30-0"></span>**3.5.6 Command message acknowledgment**

Some log operations may take a long time to execute because of the time taken to write to flash memory. The time for some operations may be unpredictable since the number and timing of flash operations may vary. In order to allow host software to synchronize to these delays logging messages will always produce a response.This will be UBX-ACK-NAK in case of error, otherwise UBX-ACK-ACK unless there is some other defined response to the message.

It is possible to send a small number of logging commands without waiting for acknowledgment, since there is a command queue, but this risks confusion between the acknowledgments for the commands. Also a command queue overflow would result in commands being lost.

## <span id="page-30-1"></span>**3.6 Communication interfaces**

u-blox receivers are equipped with a communication interface which is multi-protocol capable. The interface ports can be used to transmit GNSS measurements, monitor status information and configure the receiver.

A protocol (e.g. UBX, NMEA) can be assigned to several ports simultaneously, each configured with individual settings (e.g. baud rate, message rates, etc.). More than one protocol (e.g. UBX protocol and NMEA) can be assigned to a single port (multi-protocol capability), which is particularly useful for debugging purposes.

The ZED-F9H provides UART1, UART2, SPI, I2C and USB interfaces for communication with a host CPU. The interfaces are configured via the configuration methods described in the applicable interface description [\[2\]](#page-95-2).

| Port no. | UBX-MON-COMMS portId | Electrical interface |
|----------|----------------------|----------------------|
| 0        | 0x0000               | I2C                  |
| 1        | 0x0100               | UART1                |
| 2        | 0x0201               | UART2                |
| 3        | 0x0300               | USB                  |
| 4        | 0x0400               | SPI                  |

The following table shows the port numbers reported in the UBX-MON-COMMS messages.

**Table 17: Port number assignment**

It is important to isolate interface pins when VCC is removed. They can be allowed to float or they can be connected to a high impedance.

Example isolation circuit is shown below.





**Figure 13: ZED-F9H output isolation**



**Figure 14: ZED-F9H input isolation**

#### <span id="page-31-0"></span>**3.6.1 UART**

A Universal Asynchronous Receiver/Transmitter (UART) port consists of an RX and a TX line. Neither handshaking signals nor hardware flow control signals are available. The UART interface protocol and baud rate can be configured but there is no support for setting different baud rates for reception and transmission.

The ZED-F9H includes two UART serial ports. UART1 can be used as a host interface for configuration, monitoring and control. UART2 is available as an optional interface and cannot be used as a single host interface.

The UART RX interface will be disabled when more than 100 frame errors are detected during a one-second period. This can happen if the wrong baud rate is used or the UART RX pin is grounded. An error message appears when the UART RX interface is re-enabled at the end of the one-second period.

| Baud rate | Data bits | Parity | Stop bits |
|-----------|-----------|--------|-----------|
| 9600      | 8         | none   | 1         |
| 19200     | 8         | none   | 1         |
| 38400     | 8         | none   | 1         |
| 57600     | 8         | none   | 1         |
| 115200    | 8         | none   | 1         |



| Baud rate | Data bits | Parity | Stop bits |
|-----------|-----------|--------|-----------|
| 230400    | 8         | none   | 1         |
| 460800    | 8         | none   | 1         |
| 921600    | 8         | none   | 1         |

#### **Table 18: Possible UART interface configurations**

The default baud rate is 38400 baud. To prevent buffering problems it is recommended not to run at a lower baud rate than the default.

Users should allow a short time delay of typically 100 ms between sending a baud rate change message and providing input data at the new rate. Otherwise some input characters may be ignored or the port could be disabled until the interface is able to process the new baud rate.

Note that for protocols such as NMEA or UBX, it does not make sense to change the default word length values (data bits) since these properties are defined by the protocol and not by the electrical interface.

If the amount of data configured is too much for a certain port's bandwidth (e.g. all UBX messages output on a UART port with a baud rate of 9600), the buffer will fill up. Once the buffer space is exceeded, new messages to be sent will be dropped. To prevent message loss, the baud rate and communication speed or the number of enabled messages should be carefully selected so that the expected number of bytes can be transmitted in less than one second.

#### <span id="page-32-0"></span>**3.6.2 I2C interface**

An I2C interface is available for communication with an external host CPU or u-blox cellular modules. The interface can be operated in slave mode only. The I2C protocol and electrical interface are fully compatible with the I2C industry standard fast mode. Since the maximum SCL clock frequency is 400 kHz, the maximum transfer rate is 400 kb/s. The SCL and SDA pins have internal pull-up resistors which should be sufficient for most applications. However, depending on the speed of the host and the load on the I2C lines additional external pull-up resistors may be necessary.

- To use the I2C interface D\_SEL pin must be left open.
- In designs where the host uses the same I2C bus to communicate with more than one ublox receiver, the I2C slave address for each receiver must be configured to a different value. Typically most u-blox receivers are configured to the same default I2C slave address value. To poll or set the I2C slave address, use the CFG-I2C-ADDRESS configuration item (see the applicable interface description [\[2\]](#page-95-2)).

The CFG-I2C-ADDRESS configuration item is an 8-bit value containing the I2C slave address in 7 most significant bits, and the read/write flag in the least significant bit.

#### **3.6.2.1 I2C register layout**

The I2C interface allows 256 registers to be addressed. As shown in [Figure](#page-33-0) 15, only three of these are currently implemented.

The data registers 0 to 252 at addresses 0x00 to 0xFC contain reserved information, the result from their reading is currently undefined. The data registers 0 to 252 are 1 byte wide.

At addresses 0xFD and 0xFE it is possible to read the currently available number of bytes.

The register at address 0xFF allows the data stream to be read. If there is no data awaiting transmission from the receiver, then this register delivers value 0xFF, which cannot be the first byte of a valid message. If the message data is ready for transmission, the successive reads of register 0xFF will deliver the waiting message data.



#### Do not use registers 0x00 to 0xFC. They are reserved for future use and they do not currently provide any meaningful data.

<span id="page-33-0"></span>

#### **Figure 15: I2C register layout**

#### **3.6.2.2 Read access types**

There are two I2C read transfer forms:

- The "random access" form: includes a slave register address and allows any register to be read.
- The "current address" form: omits the register address.

[Figure](#page-34-0) 16 shows the format of the first one, the "random access" form of the request. Following the start condition from the master, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the master transmitter. The receiver answers with an acknowledge (logic low) to indicate that it recognizes the address.

Next, the 8-bit address of the register to be read must be written to the bus. Following the receiver's acknowledgment, the master again triggers a start condition and writes the device address, but this time the RW bit is a logic high to initiate the read access. Now, the master can read 1 to N bytes from the receiver, generating a not-acknowledge and a stop condition after the last byte being read.



<span id="page-34-0"></span>

**Figure 16: I2C random read access**

If the second form, "current address" is used, an address pointer in the receiver is used to determine which register to read. This address pointer will increment after each read unless it is already pointing at register 0xFF, the highest addressable register, in which case it remains unaltered.

The initial value of this address pointer at start-up is 0xFF, so by default all current address reads will repeatedly read register 0xFF and receive the next byte of message data (or 0xFF if no message data is waiting).



**Figure 17: I2C current address read access**

#### **3.6.2.3 Write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. Therefore, the register set mentioned in the section Read [access](#page-35-1) is not writeable.

Following the start condition from the master, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the master transmitter. The receiver answers with an acknowledge (logic low) to indicate that it is responsible for the given address.

The master can write 2 to N bytes to the receiver, generating a stop condition after the last byte being written. The number of data bytes must be at least 2 to properly distinguish from the write access to set the address counter in random read accesses.







#### <span id="page-35-0"></span>**3.6.3 SPI interface**

ZED-F9H has an SPI slave interface that can be selected by setting D\_SEL = 0. The SPI slave interface is shared with UART1 and I2C port, the physical pins are same. The SPI pins available are:

- SPI\_MISO (TXD)
- SPI\_MOSI (RXD)
- SPI\_CS\_N
- SPI\_CLK

See more information about communication interface selection from the [D\\_SEL](#page-37-1) section.

The SPI interface is designed to allow communication to a host CPU. The interface can be operated in slave mode only.

#### <span id="page-35-1"></span>**3.6.3.1 Read access**

As the register mode is not implemented for the SPI port, only the UBX/NMEA message stream is provided. This stream is accessed using the back-to-back read and write access (see section [Back](#page-35-2)[to-back](#page-35-2) read and write access below). When no data is available to be written to the receiver, MOSI should be held logic high, i.e. all bytes written to the receiver are set to 0xFF.

To prevent the receiver from being busy parsing incoming data, the parsing process is stopped after 50subsequent bytes containing0xFF.The parsing process is re-enabled with thefirst byte not equal to 0xFF.

If the receiver has no more data to send, it sets MISO to logic high, i.e. all bytes transmitted decode to 0xFF. An efficient parser in the host will ignore all 0xFF bytes which are not part of a message and will resume data processing as soon as the first byte not equal to 0xFF is received.

#### <span id="page-35-2"></span>**3.6.3.2 Back-to-back read and write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. For every byte written to the receiver, a byte will simultaneously be read from the receiver.While the master writes to MOSI, at the same time it needs to read from MISO, as any pending data will be output by the receiver with this access. The data on MISO represents the results from a current address read, returning 0xFF when no more data is available.





**Figure 19: SPI back-to-back read/write access**

#### <span id="page-36-0"></span>**3.6.4 USB interface**

A single USB port is provided for host communication purposes.

The USB 2.0 FS (Full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface.

If the receiver executes code from internal ROM (i.e. when a valid flash firmware image is not detected), the USB behavior can differ compared to executing a firmware image from flash memory. USB host compatibility testing is thus recommended in this scenario.

The ZED-F9H receiver supports only self-powered mode operation in which the receiver is supplied from its own power supply. The V\_USB pin is used to detect the availability of the USB port, i.e. whether the receiver is connected to a USB host.

- USB suspend mode is not supported.
- USB bus-powered mode is not supported.
- It is important to connect V\_USB to ground and leave data lines open when the USB interface is not used in an application.
- The voltage range for V\_USB is specified from 3.0 V to 3.6 V, which differs slightly from the specification for VCC.
- The boot screen is retransmitted on the USB port after enumeration. However, messages generated between boot-up of the receiver and USB enumeration are not visible on the USB port.

There are additional hardware requirements if USB is used:

- V\_USB (pin 38) requires 1 uF capacitor mounted adjacent to the pin to ensure correct V\_USB voltage detection
- The V\_USB (Pin 38) voltage should be sourced from an LDO enabled by the module VCC and supplied from the USB host.
- A pull-down resistor is required on the output of this V\_USB LDO
- Apply USB\_DM and USB\_DP series resistors; typically 27 Ω





**Figure 20: ZED-F9H example circuit for USB interface**

R11 = 100 k Ω is recommended

R4, R5 = 27 Ω is recommended

## <span id="page-37-0"></span>**3.7 Predefined PIOs**

In addition to the communication ports, there are some predefined PIOs provided by ZED-F9H to interact with the receiver. These PIOs are described in this chapter.

If hardware backup mode is used a proper isolation of the interfaces is needed.

#### <span id="page-37-1"></span>**3.7.1 D\_SEL**

The D\_SEL pin can be used to configure the functionality of the combined UART1, I2C, and SPI pins. It is possible to configure the pins as UART1 + I2C, or as SPI. SPI is not available unless D\_SEL pin is set to low. See [Table](#page-37-4) 19 below.

<span id="page-37-4"></span>

| Pin no. | D_SEL == 0 | D_SEL == 1 |
|---------|------------|------------|
| 42      | SPI_MISO   | UART1 TXD  |
| 43      | SPI_MOSI   | UART1 RXD  |
| 44      | SPI_CS_N   | I2C SDA    |
| 45      | SPI_CLK    | I2C SCL    |

**Table 19: D\_SEL configuration**

#### <span id="page-37-2"></span>**3.7.2 RESET\_N**

The ZED-F9H provides the ability to reset the receiver. The RESET\_N pin is an input-only pin with an internal pull-up resistor. Driving RESET\_N low for at least 100 ms will trigger a cold start.



The RESET\_N pin will delete all information and trigger a cold start. It should only be used as a recovery option.

#### <span id="page-37-3"></span>**3.7.3 SAFEBOOT\_N**

The ZED-F9H provides a SAFEBOOT\_N pin that is used to command the receiver safe boot mode.

If this pin is low at power up, the receiver starts in safe boot mode and GNSS operation is disabled.

The safe boot mode can be used to recover from situations where the flash content has become corrupted and needs to be restored.

In safe boot mode the receiver runs from a passive oscillator circuit with less accurate timing and hence the receiver is unable to communicate via USB.

In this mode only UART1, I2C or SPI communication is possible. For communication via UART1 in safe boot mode, the host must send a training sequence (0x55 0x55 at 9600 baud) to the receiver in order to begin communication. After this the host must wait at least 2 ms before sending any data.



It is recommended to have the possibility to pull the SAFEBOOT\_N pin low in the application. This can be provided using an externally connected test point or a host I/O port.

### <span id="page-38-0"></span>**3.7.4 TIMEPULSE**

The ZED-F9H high precision receiver provides a time pulse on the TIMEPULSE pin.

More information about the time pulse feature and its configuration can be found in the Time [pulse](#page-48-1) section.

### <span id="page-38-1"></span>**3.7.5 TX\_READY**

This feature enables each port to define a corresponding pin, which indicates if bytes are ready to be transmitted. A listener can wait on the TX-READY signal instead of polling the I2C or SPI interfaces. The CFG-TXREADY message lets you configure the polarity and the number of bytes in the buffer before the TX-READY signal goes active. By default, this feature is disabled. For USB, this feature is configurable but might not behave as described below due to a different internal transmission mechanism. If the number of pending bytes reaches the threshold configured for this port, the corresponding pin will become active (configurable active-low or active-high), and stay active until the last bytes have been transferred from software to hardware.

This is not necessarily equal to all bytes transmitted, i.e. after the pin has become inactive, up to 16 bytes might still need to be transferred to the host.

The TX\_READY pin can be selected from all PIOs which are not in use (see UBX-MON-HW3 in the applicable interface description [\[2\]](#page-95-2) for a list of the PIOs and their mapping). Each TX\_READY pin is exclusively associated to one port and cannot be shared. If PIO is invalid or already in use, only the configuration for the specific TX\_READY pin is ignored, the rest of the port configuration is applied if valid. The acknowledge message does not indicate if the TX-READY configuration is successfully set, it only indicates the successful configuration of the port. To validate successful configuration of the TX\_READY pin, the port configuration should be read back and the settings of TX-READY feature verified (will be set to disabled/all zero if the settings are invalid).

The threshold when TX\_READY is asserted should not be set above 2 kB as it is possible that the internal message buffer limit is reached before this. This results in the TX\_READY pin never being set as the messages are discarded before the threshold is reached.

#### **3.7.5.1 Extended TX timeout**

If the host does not communicate over SPI or I2C for more than approximately 2 seconds, the device assumes that the host is no longer using this interface and no more packets are scheduled for this port. This mechanism can be changed by enabling "extended TX timeouts", in which case the receiver delays idling the port until the allocated and undelivered bytes for this port reach 4 kB. This feature is especially useful when using the TX-READY feature with a message output rate of less than once per second, and polling data only when data is available, determined by the TX\_READY pin becoming active.

#### <span id="page-38-2"></span>**3.7.6 EXTINT**

EXTINT is an external interrupt pin with fixed input voltage thresholds with respect to VCC. It can be used for functions such as accurate external frequency aiding and on/off control. The external frequency aiding can be used to calibrate the clock. This enables faster fix of satellite signals (UBX-MGA-INI-FREQ or UBX-MGA-INI-TIME\_XXX) and can be used during normal operation or during the production test. Another possibility to use the extint feature is to wake up the receiver after putting



it into backup mode; this can be set up with UBX-RXM-PMREQ. Leave open if unused, this function is disabled by default.

### <span id="page-39-0"></span>**3.7.7 GEOFENCE\_STAT interface**

The ZED-F9H provides a GEOFENCE\_STAT pin that indicates the current geofence status as to whether the receiver is inside any of the active areas.

This feature can be used for example to wake up a sleeping host when a defined geofence condition is reached. It is possible to configure up to four circular areas as geofence locations. Once configured, the receiver continuously compares its current position with the preset geofenced areas.

For more information in this functionality, see Geofence state [evaluation.](#page-26-0)

The receiver toggles the assigned pin according to the combined geofence state.

There are three possible outcomes for each geofence:

- *Inside* The position is inside the geofence with the configured confidence level
- *Outside* The position lies outside of the geofence with the configured confidence level
- *Unknown* There is no valid position solution or the position uncertainty does not allow for unambiguous state evaluation

The GEOFENCE\_STAT pin is always set to high level when the combine geofence state is unknown. The low level can either represent the inside state or the outside state according to the value set in the CFG-GEOFENCE-PINPOL configuration item. If the receiver is in software backup or in a reset, the pin will go to high accordingly.

The GEOFENCE\_STAT pin is the module pin 19 and it is assigned to PIO3.

### <span id="page-39-1"></span>**3.7.8 RTK\_STAT interface**

The ZED-F9H provides an RTK\_STATpin that provides an indication of the RTK positioning status. It can be used to confirm if a valid stream of correction messages is being received. As valid correction messages we only consider the correction messages that are supported and used by the receiver.

In general, the RTK\_STAT level can be interpreted as follows: Alternating (blinking) pin level, indicates that a valid stream of correction messages is being received and utilized but no RTK fixed mode has been achieved. An active low pin level indicates that RTK fixed mode has been achieved. Otherwise, the pin level is high.

The RTK\_STAT pin status can be mapped to the carrSoln field of the UBX-NAV-PVT and interpreted as follows:

- An active low pin level indicates that RTK fixed mode has been achieved
- Alternating (blinking) pin level, indicates that a valid stream of correction messages is being received and utilized but no RTK fixed mode has been achieved
- An active high pin level indicates that no carrier phase solution is available

## <span id="page-39-2"></span>**3.8 Antenna supervisor**

An active antenna supervisor provides the means to check the antenna for open and short circuits and to shut off the antenna supply if a short circuit is detected. Once enabled, the active antenna supervisor produces status messages, reporting in NMEA and/or UBX protocol.

The antenna supervisor can be configured through the CFG-HW-ANT\_\* configuration items. The current configuration of the active antenna supervisor can also be checked by polling the related CFG-HW\_ANT\_\* configuration items.



The current active antenna status can be determined by polling the UBX-MON-RF message. If an antenna is connected, the initial state after power-up is "Active Antenna OK" in the UBX-MON-RF message in the u-center "Message View".

An active antenna supervisor circuit is connected to the ANT\_DET, ANT\_OFF, ANT\_SHORT\_N pins. For an example the open circuit detection circuit using ANT\_DET, "high" = Antenna detected (antenna consumes current); "low" = Antenna not detected (no current drawn).

The following schematic details the required circuit and the sections following it explain how to enable and monitor each feature:



**Figure 21: ZED-F9H antenna supervisor**

The bias-t inductor must be chosen for multi-band operation; a value of 47 nH ±5% is required for our recommended Murata part, with the current limited below its 300 mA rating. See [Antenna](#page-70-0) bias section for additional information.

Circuit shows buffer [U4]. Buffer is not strictly necessary when supplied from VCC. It is only required when supplying antenna voltage that is not obtained from or controlled by module VCC or VCC\_RF .

| Part | Recommendation                       | Comment                                |
|------|--------------------------------------|----------------------------------------|
| L1   | Murata LQG15HS47NJ02/47N             | 300mA and >500 Ω at L-band frequencies |
| C2   | Murata GRM033R71C103KE14             | CAP CER X7R 0402 10N 10% 16V           |
|      | TYCO, 0.25PF, PESD0402-140 -55/+125C | ESD protection diode on RF trace       |

**Table 20: Recommended components for antenna supervisor**

#### <span id="page-40-0"></span>**3.8.1 Antenna voltage control - ANT\_OFF**

Antenna status (as reported in UBX-MON-RF and UBX-INF-NOTICE messages) is not reported unless the antenna voltage control has been enabled.

Enable the antenna voltage control by setting the configuration item CFG-HW-ANT\_CFG\_VOLTCTRL to true (1).



Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF pin = active high to turn antenna off therefore the pin is low to enable an external antenna.

Start-up message at power up if configuration stored:

```
$GNTXT,01,01,02,ANTSUPERV=AC *00
$GNTXT,01,01,02,ANTSTATUS=INIT*3B
```

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC indicates antenna control is activated

#### <span id="page-41-0"></span>**3.8.2 Antenna short detection - ANT\_SHORT\_N**

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

- ANT\_OFF = active high therefore still low (still enabled as auto power down is not enabled)
- After a detected antenna short, the reported antenna status will keep on being reported as shorted. If the antenna short detection auto recovery is enabled, then the antenna status can recover after a timeout. To recover the antenna status immediately, a power cycle is required or configuring the antenna short detection functionality off and on.

#### <span id="page-41-1"></span>**3.8.3 Antenna short detection auto recovery**

Enable the antenna short detection auto recovery by setting the configuration item CFG-HW-ANT\_CFG\_RECOVER to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high there for the PIO is low to enable an external antenna



• ANT\_SHORT\_N = high (PIO pull up enabled to be pulled low if shorted)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD PDoS SR\*3E

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD PDoS SR (indicates short circuit recovery added - SR)

Then if antenna is shorted (ANT\_SHORT\_N pulled low):

- \$GNTXT,01,01,02,ANTSTATUS=SHORT\*73
- UBX-MON-RF in u-center "Message View": Antenna status = SHORT. Antenna power status = OFF
- ANT\_OFF = high (to disable active high)

After a time out period receiver will re-test the short condition by enabling ANT\_OFF = LOW

If a short is not present it will report antenna condition is OK:

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON

#### <span id="page-42-0"></span>**3.8.4 Antenna open circuit detection - ANT\_DETECT**

Enable the antenna open circuit detection by setting the configuration item CFG-HW-ANT\_CFG\_OPENDET to true (1).

#### Result:

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

\$GNTXT,01,01,02,ANTSTATUS=OK\*25



## <span id="page-43-0"></span>**3.9 Multiple GNSS assistance (MGA)**

The u-blox AssistNow services provide a proprietary implementation of an A-GNSS protocol compatible with u-blox GNSS receivers.

The MGA services consist of AssistNow Online and Offline variants delivered by HTTP or HTTPS protocol. AssistNow Online optionally provides immediate satellite ephemerides, health information and time aiding data suitable for GNSS receiver systems with direct internet access.

When a client device makes an AssistNow request, the service responds with the requested data using standard UBX protocol MGA messages. These messages are ready for direct transmission from the client to the receiver port without requiring any modification.

The ZED-F9H supports AssistNow Online only.

#### <span id="page-43-1"></span>**3.9.1 Authorization**

To use the AssistNow services, customers will need to obtain an authorization token from u-blox. Go to https://www.u-blox.com/en/solution/services/assistnow or contact your local technical support to get more information and to request access to the service.

#### <span id="page-43-2"></span>**3.9.2 Preserving MGA and operational data during power-off**

The time-to-fix after a receiver power interruption is dependent on the amount of operational data available at start-up. Satellite broadcast information plus an estimate of accurate time can be fetched form the AssistNow service. In addition, the following techniques can restore previously stored data prior to power down.

- **Battery-backed RAM:**The receiver operational state stored in this RAM can be maintained during power outages by connecting the V\_BCKP pin to an independant supply, e.g a battery. This is a recommended method as it will maintain all MGA related information plus any user configuration, calibration data and an estimate of time via the Real Time Clock. See section [V\\_BCKP:](#page-66-2) Backup supply voltage for more information.
- **Save-on-shutdown:**The receiver can be instructed to dump its current state to flash memory as part of the shutdown procedure; this data is then automatically retrieved when the receiver is restarted. For more information, see section Save-on-shutdown feature for more info. For information on the UBX-UPD-SOS messages consult the applicable interface description [\[2\]](#page-95-2).
- **Database dump:** The receiver can be made to dump the state of its navigation database in the form of a sequence of UBX messages reported to the host; these messages can be stored by the host and then sent back to the receiver when it has been restarted. See the description of the UBX-MGA-DBD messages in the applicable interface description [\[2\]](#page-95-2) for more information.

## <span id="page-43-3"></span>**3.10 Clocks and time**

This section introduces and explains the concepts of receiver clocks and time bases.

#### <span id="page-43-4"></span>**3.10.1 Receiver local time**

The receiver is dependent on a local oscillator for both the operation of its radio parts and also for timing within its signal processing. No matter what nominal frequency the local oscillator has, u-blox receivers subdivide the oscillator signal to provide a 1-kHz reference clock signal, which is used to drivemany of the receiver's processes. In particular, themeasurement of satellite signals is arranged to be synchronized with the "ticking" of this 1-kHz clock signal.

When the receiver first starts, it has no information about how these clock ticks relate to other time systems; it can only count time in 1 millisecond steps. However, as the receiver derives information from the satellites it is tracking or from aiding messages, it estimates the time that each 1-kHz



clock tick takes in the time-base of the chosen GNSS system. This estimate of GNSS time based on the local 1-kHz clock is called receiver local time.

As receiver local time is a mapping of the local 1-kHz reference onto a GNSS time-base, it may experience occasional discontinuities, especially when the receiver first starts up and the information it has about the time-base is changing. Indeed, after a cold start, the receiver local time will initially indicate the length of time that the receiver has been running. However, when the receiver obtains some credible timing information from a satellite or an aiding message, it will jump to an estimate of GNSS time.

#### <span id="page-44-0"></span>**3.10.2 Navigation epochs**

Each navigation solution is triggered by the tick of the 1-kHz clock nearest to the desired navigation solution time. This tick is referred to as a **navigation epoch**. If the navigation solution attempt is successful, one of the results is an accurate measurement of time in the time-base of the chosen GNSS system, called **GNSS system time**. The difference between the calculated GNSS system time and receiver local time is called **clock bias** (and **clock drift** is the rate at which this bias is changing).

In practice the receiver's local oscillator will not be as stable as the atomic clocks to which GNSS systems are referenced and consequently clock bias will tend to accumulate. However, when selecting the next navigation epoch, the receiver will always try to use the 1-kHz clock tick which it estimates to be closest to the desired fix period as measured in GNSS system time. Consequently the number of 1-kHz clock ticks between fixes will occasionally vary. This means that when producing one fix per second, there will normally be 1000 clock ticks between fixes, but sometimes, to correct drift away from GNSS system time, there will be 999 or 1001.

The GNSS system time calculated in the navigation solution is always converted to a time in both the GPS and UTC time-bases for output.

Clearly when the receiver has chosen to use the GPStime-base for its GNSSsystem time, conversion to GPS time requires no work at all, but conversion to UTC requires knowledge of the number of leap seconds since GPS time started (and other minor correction terms). The relevant GPS-to-UTC conversion parameters are transmitted periodically (every 12.5 minutes) by GPS satellites, but can also be supplied to the receiver via the UBX-MGA-GPS-UTC aiding message. By contrast when the receiver has chosen to use the GLONASS time-base as its GNSS system time, conversion to GPS time is more difficult as it requires knowledge of the difference between the two time-bases, but as GLONASS time is closely linked to UTC, conversion to UTC is easier.

When insufficient information is available for the receiver to perform any of these time-base conversions precisely, pre-defined default offsets are used. Consequently plausible times are nearly always generated, but they may be wrong by a few seconds (especially shortly after receiver start). Depending on the configuration of the receiver, such "invalid" times may well be output, but with flags indicating their state (e.g. the "valid" flags in UBX-NAV-PVT).

u-blox receivers employ multiple GNSS system times and/or receiver local times (in order to support multiple GNSS systems concurrently), so users should not use UBX messages reporting GNSS system time or receiver local time. It is recommended to use messages that report UTC time and other messages are retained only for backwards compatibility reasons.

#### <span id="page-44-1"></span>**3.10.3 iTOW timestamps**

All the main UBX-NAV messages (and some other messages) contain an **iTOW** field which indicates the GPS time at which the navigation epoch occurred. Messages with the same iTOW value can be assumed to have come from the same navigation solution.



Note that iTOW values may not be valid (i.e. they may have been generated with insufficient conversion data) and therefore it is not recommended to use the iTOW field for any other purpose.

The original designers of GPS chose to express time/date as an integer week number (starting with the first full week in January 1980) and a time of week (often abbreviated to TOW) expressed in seconds. Manipulating time/date in this form is far easier for digital systems than the more conventional year/month/day, hour/minute/second representation. Consequently, most GNSS receivers use this representation internally, only converting to a more conventional form at external interfaces. The iTOW field is the most obvious externally visible consequence of this internal representation.

If reliable absolute time information is required, users are recommended to use the UBX-NAV-PVT navigation solution message which also contains additional fields that indicate the validity (and accuracy in UBX-NAV-PVT) of the calculated times (see also the [GNSS times](#page-45-0) section below for further messages containing time information).

### <span id="page-45-0"></span>**3.10.4 GNSS times**

Each GNSS has its own time reference for which detailed and reliable information is provided in the messages listed in the table below.

| Time reference | Message          |
|----------------|------------------|
| GPS time       | UBX-NAV-TIMEGPS  |
| BeiDou time    | UBX-NAV-TIMEBDS  |
| GLONASS time   | UBX-NAV-TIMEGLO  |
| Galileo time   | UBX-NAV-TIMEGAL  |
| QZSS time      | UBX-NAV-TIMEQZSS |
| UTC time       | UBX-NAV-TIMEUTC  |

**Table 21: GNSS times**

#### <span id="page-45-1"></span>**3.10.5 Time validity**

Information about the validity of the time solution is given in the following form:

- Time validity: Information about time validity is provided in the valid flags (e.g. validDate and validTime flags in the UBX-NAV-PVT message). If these flags are set, the time is known and considered valid for use. These flags are shown in table GNSS times in section GNSS times above as well as in the UBX-NAV-PVT message.
- Time validity confirmation: Information about confirmed validity is provided in the confirmedDate and confirmedTime flags in the UBX-NAV-PVT message. If these flags are set, the time validity can be confirmed by using an additional independent source, meaning that the probability of the time to be correct is very high. Note that information about time validity confirmation is only available if the confirmedAvai bit in the UBX-NAV-PVT message is set.
- validDate means that the receiver has knowledge of the current date. However, it must be noted that this date might be wrong for various reasons. Only when the confirmedDate flag is set, the probability of the incorrect date information drops significantly.
- validTime means that the receiver has knowledge of the current time. However, it must be noted that this time might be wrong for various reasons. Only when the confirmedTime flag is set, the probability of incorrect time information drops significantly.
- fullyResolved means that the UTC time is known without full seconds ambiguity. When deriving UTC time from GNSS time the number of leap seconds must be known, with the exception of GLONASS. It might take several minutes to obtain such information from the



GNSS payload. When the one second ambiguity has not been resolved, the time accuracy is usually in the range of ~20s.

#### <span id="page-46-0"></span>**3.10.6 UTC representation**

UTC time is used in many NMEA and UBX messages. In NMEA messages it is always reported rounded to the nearest hundredth of a second. Consequently, it is normally reported with two decimal places (e.g. 124923.52). Although compatibility mode (selected using CFG-NMEA-COMPAT) requires three decimal places, rounding to the nearest hundredth of a second remains, so the extra digit is always 0.

UTC time is also reported within some UBX messages, such as UBX-NAV-TIMEUTC and UBX-NAV-PVT. In these messages date and time are separated into seven distinct integer fields. Six of these (year, month, day, hour, min and sec) have fairly obvious meanings and are all guaranteed to match the corresponding values in NMEA messages generated by the same navigation epoch. This facilitates simple synchronization between associated UBX and NMEA messages.

The seventh field is called nano and it contains the number of nanoseconds by which the rest of the time and date fields need to be corrected to get the precise time. So, for example, the UTC time 12:49:23.521 would be reported as: hour: 12, min: 49, sec: 23, nano: 521000000.

It is however important to note that the first six fields are the result of rounding to the nearest hundredth of a second. Consequently the nano value can range from -5000000 (i.e. -5 ms) to +994999999 (i.e. nearly 995 ms).

When the nano field is negative, the number of seconds (and maybe minutes, hours, days, months or even years) will have been rounded up. Therefore, some or all of them must be adjusted in order to get the correct time and date. Thus in an extreme example, the UTC time 23:59:59.9993 on 31st December 2011 would be reported as: year: 2012, month: 1, day: 1, hour: 0, min: 0, sec: 0, nano: -700000.

Of course, if a resolution of one hundredth of a second is adequate, negative nano values can simply be rounded up to 0 and effectively ignored.

Which master clock the UTC time is referenced to is output in the message UBX-NAV-TIMEUTC.

The preferred variant of UTC time can be specified using CFG-NAVSPG-UTCSTANDARD configuration item.

#### <span id="page-46-1"></span>**3.10.7 Leap seconds**

Occasionally it is decided (by one of the international time keeping bodies) that, due to the slightly uneven spin rate of the Earth, UTC has moved sufficiently out of alignment with mean solar time (i.e. the Sun no longer appears directly overhead at 0 longitude at midday). A "leap second" is therefore announced to bring UTC back into close alignment. This normally involves adding an extra second to the last minute of the year, but it can also happen on 30th June. When this happens UTC clocks are expected to go from 23:59:59 to 23:59:60 and only then on to 00:00:00.

It is also theoretically possible to have a negative leap second, in which case there will only be 59 seconds in a minute and 23:59:58 will be followed by 00:00:00.

u-blox receivers are designed to handle leap seconds in their UTC output and consequently users processing UTC times from either NMEA or UBX messages should be prepared to handle minutes that are either 59 or 61 seconds long.



Leap second information can be polled from the u-blox receiver with the message UBX-NAV-TIMELS.

#### <span id="page-47-0"></span>**3.10.8 Real-time clock**

u-blox receivers contain circuitry to support a real-time clock, which (if correctly fitted and powered) keeps time while the receiver is otherwise powered off. When the receiver powers up, it attempts to use the real-time clock to initialize receiver local time and in most cases this leads to appreciably faster first fixes.

#### <span id="page-47-1"></span>**3.10.9 Date**

All GNSS frequently transmit information about the current time within their data message. In most cases, this is a time of week (often abbreviated to TOW), which indicates the elapsed number of seconds since the start of the week (midnight Saturday/Sunday). In order to map this to a full date, it is necessary to know the week and so the GNSS also transmit a week number, typically every 30 seconds. Unfortunately the GPS L1C/A data message was designed in a way that only allows the bottom 10 bits of the week number to be transmitted. This is not sufficient to yield a completely unambiguous date as every 1024 weeks (a bit less than 20 years), the transmitted week number value "rolls over" back to zero. Consequently, GPS L1 receivers cannot tell the difference between, for example, 1980, 1999 or 2019 etc.

Fortunately, although BeiDou and Galileo have similar representations of time, they transmit sufficient bits for the week number to be unambiguous for the foreseeable future (the first ambiguity will be in 2078 for Galileo and not until 2163 for BeiDou). GLONASS has a different structure, based on a time of day, but again transmits sufficient information to avoid any ambiguity during the expected lifetime of the system (the first ambiguous date will be in 2124). Therefore, ublox 9 receivers using Protocol Version 24 and above regard the date information transmitted by GLONASS, BeiDou and Galileo to be unambiguous and, where necessary, use this to resolve any ambiguity in the GPS date.

Customers attaching u-blox receivers to simulators should be aware that GPS time is referenced to 6th January 1980, GLONASS to 1st January 1996, Galileo to 22nd August 1999 and BeiDou to 1st January 2006; the receiver cannot be expected to work reliably with signals simulated before these dates.

#### **3.10.9.1 GPS-only date resolution**

In circumstances where only GPS L1C/A signals are available and for receivers with earlier firmware versions, the receiver establishes the date by assuming that all week numbers must be at least as large as a reference rollover week number. This reference rollover week number is hard-coded at compile time and is normally set a few weeks before the software is completed, but it can be overridden by CFG-NAVSPG-WKNROLLOVER configuration item to any value the user wishes.

The following example illustrates how this works: Assume that the reference rollover week number set in the firmware at compile time is 1524 (which corresponds to a week in calendar year 2009, but would be transmitted by the satellites as 500). In this case, if the receiver sees transmissions containing week numbers in the range of 500 ... 1023, these will be interpreted as week numbers 1524 ... 2047 (calendar year 2009 ... 2019), whereas transmissions with week numbers from 0 to 499 are interpreted as week numbers 2048 ... 2547 (calendar year 2019 ... 2028).

It is important to set the reference rollover week number appropriately when supplying ublox receivers with simulated signals, especially when the scenarios are in the past.



## <span id="page-48-0"></span>**3.11 Timing functionality**

In addition to positioning and navigation applications, GNSS signals are widely used as low-cost precision time or frequency references used by remote or distributed wireless communication, industrial, financial, and power distribution equipment. By capitalizing on atomic clocks which are on-board positioning satellites, GNSS signals which contain embedded timing information can be used to synchronize equipment, as well as to provide UTC time. For wireless communication standards that utilize Time Division Multiplex (TDM) and applications such as femtocell base stations, a precision time reference is mandatory.

#### <span id="page-48-1"></span>**3.11.1 Time pulse**

#### **3.11.1.1 Introduction**

u-blox receivers include a time pulse function providing clock pulses with configurable duration and frequency. The time pulse function can be configured using the CFG-TP-\* configuration group. The UBX-TIM-TP message provides time information for the next pulse and the time source.



**Figure 22: Time pulse**

#### **3.11.1.2 Recommendations**

- The time pulse can be aligned to a wide variety of GNSS times or to variants of UTC derived from them (see the chapter on [time bases\)](#page-49-0). However, it is strongly recommended that the choice of time base is aligned with the available GNSS signals (so to produce GPS time or UTC(USNO), ensure GPS signals are available, and for GLONASS time or UTC(SU) ensure the presence GLONASS signals). This will involve coordinating the setting of CFG-SIGNAL-\* configuration group with the choice of time pulse time base.
- When using time pulse for timing applications requiring absolute time accuracy, e.g. with requirements specifying offset to UTC, it is recommended to calibrate the user's full setup for TP output against a reference timing source. To achieve best absolute and consistent accuracy (e.g. for mass deployment), it is recommended that the user should calibrate each single setup and calibrate under different GNSS modes and different temperatures which are applicable to the user's application and operating requirements. The user should take the calibrated values and configure the compensation accordingly (see the section on Time pulse [configuration](#page-50-0))
- To get the best timing accuracy with the antenna, a fixed and *accurate* position is needed.



- If relative time accuracy between multiple receivers is required, do not mix receivers of different product families. If this is required, the receivers must be calibrated accordingly, by setting cable delay and user delay.
- The recommended configuration when using the UBX-TIM-TP message is to set both the measurement rate (CFG-RATE-MEAS) and the time pulse frequency (CFG-TP-\*) to 1 Hz.
- Since the rate of UBX-TIM-TP is bound to 1 Hz, more than one UBX-TIM-TP message can appear between two pulses if the time pulse frequency is set larger than 1 Hz. In this case all UBX-TIM-TP messages in between time pulses T1 and T2 belong to T2 and the last UBX-TIM-TP before T2 reports the most accurate quantization error. In general, if the time pulse rate is not configured to 1 Hz, there will not be a single UBX-TIM-TP message for each time pulse.

The sequential order of the signal present at theTIMEPULSEpinand the respective outputmessage for the simple case of 1 pulse per second (1PPS) is shown in the following figure.





#### <span id="page-49-0"></span>**3.11.1.3 GNSS time bases**

GNSS receivers must handle a variety of different time bases as each GNSS has its own reference system time. What is more, although each GNSS provides a model for converting their system time into UTC, they all support a slightly different variant of UTC. So, for example, GPS supports a variant of UTC as defined by the US National Observatory, while BeiDou uses UTC from the National Time Service Center, China (NTSC). While the different UTC variants are normally closely aligned, they can differ by as much as a few hundreds of nanoseconds.

Although u-blox receivers can combine a variety of different GNSS times internally, the user must choose a single type of GNSS time and, separately, a single type of UTC for input (on EXTINT pins) and output (via the TIMEPULSE pin) and the parameters reported in corresponding messages.

The CFG-TP-TIMEGRID\_TP\* configuration item allows the user to choose between any of the supported GNSS (GPS, GLONASS, BeiDou, etc.) time bases and UTC. Also, the CFG-NAVSPG-UTCSTANDARD configuration item allows the user to select which variant of UTC the receiver should use. This includes an "automatic" option which causes the receiver to select an appropriate UTC version itself, based on the GNSS configuration, using, in order of preference, USNO if GPS is enabled, SU if GLONASS is enabled, NTSC if BeiDou is enabled and, finally, European if Galileo is enabled.

The receiver will assume that an input time pulse uses the same GNSStime base as specified for the time pulse output. So if the user selects GLONASS time for time pulse output, any time pulse input must also be aligned to GLONASS time (or to the separately chosen variant of UTC). Where UTC is selected for time pulse output, any GNSStime pulse input will be assumed to be aligned to GPStime.



- u-blox receivers allow users to independently choose GNSS signals used in the receiver (using CFG-SIGNAL-\*) and the input/output time base (using CFG-TP-\*). For example it is possible to instruct the receiver to use GPS and GLONASS satellite signals to generate BeiDou time. This practice will compromise timepulse accuracy if the receiver cannot measure the timing difference between the constellations directly and is therefore not recommended.
- The information that allows GNSS times to be converted to the associated UTC times is only transmitted by the GNSS at relatively infrequent periods. For example GPS transmits UTC(USNO) information only once every 12.5 minutes. Therefore, if a time pulse is configured to use a variant of UTC time, after a cold start, substantial delays before the receiver has sufficient information to start outputting the time pulse can be expected.

#### **3.11.1.4 Time pulse configuration**

u-blox ZED-F9H receivers provide a time pulse (TIMEPULSE) signal with a configurable pulse period, length and polarity (rising or falling edge).

It is possible to define different signal behavior (i.e. output frequency and pulse length) depending on whether or not the receiver is locked to a reliable time source. Time pulse signal can be configured using the configuration group CFG-TP-\*.

#### <span id="page-50-0"></span>**3.11.1.5 Configuring time pulse with CFG-TP-\***

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
- **grid UTC/GNSS** Selection between UTC (0), GPS (1), GLONASS (2), BeiDou (3) and (4) Galileo timegrid. Also affects the time output by UBX-TIM-TP message.

The maximum pulse length cannot exceed the pulse period.

Time pulse settings shall be chosen in such a way that neither the high nor the low period of the output is less than 50 ns (except when disabling it completely), otherwise pulses can be lost.

#### **3.11.1.5.1 Example**

The example below shows the 1PPS TIMEPULSE signal generated on the time pulse output according to the specific parameters of the CFG-TP-\* configuration group:

- **CFG-TP-TP1\_ENA** = 1
- **CFG-TP-PERIOD\_TP1** = 1 000 000 µs
- **CFG-TP-LEN\_TP1** = 100 000 µs
- **CFG-TP-TIMEGRID\_TP1** = 1 (GPS)
- **CFG-TP-PULSE\_LENGTH\_DEF** = 0 (Period)
- **CFG-TP-ALIGN\_TO\_TOW\_TP1** = 1
- **CFG-TP-USE\_LOCKED\_TP1** = 1
- **CFG-TP-POL\_TP1** = 1
- **CFG-TP-PERIOD\_LOCK\_TP1** = 100 000 µs
- **CFG-TP-LEN\_LOCK\_TP1** = 100 000 µs

The 1 Hz output is maintained whether or not the receiver is locked to GPS time. The alignment to TOW can only be maintained when GPS time is locked.



**Figure 24: Time pulse signal with the example parameters**

#### <span id="page-51-0"></span>**3.11.2 Timemark**

The receiver can be used to provide an accurate measurement of the time at which a pulse was detected on the external interrupt pin. The reference time can be chosen by setting the time source parameter to UTC, GPS, GLONASS, BeiDou, Galileo or local time in the CFG-TP-\* configuration group. The UTC standard can be set in the CFG-NAVSPG-\* configuration group. The delay figures defined with CFG-TP-\* are also applied to the results output in the UBX-TIM-TM2 message.

A UBX-TIM-TM2 message is output at the next epoch if

- The UBX-TIM-TM2 message is enabled, and
- A rising or falling edge was triggered since last epoch on one of the EXTINT channels.

The UBX-TIM-TM2 messages includes the time of the last timemark, new rising/falling edge indicator, time source, validity, number of marks and an accuracy estimate.





Only the last rising and falling edge detected between two epochs is reported since the output rate of the UBX-TIM-TM2 message corresponds to the measurement rate configured with CFG-RATE-MEAS (see [Figure](#page-52-1) 25 below).

<span id="page-52-1"></span>

**Figure 25: Timemark**

## <span id="page-52-0"></span>**3.12 Security**

The security concept of ZED-F9H covers the air interface between the receiver and the GNSS satellites and the integrity of the receiver itself.

There are functions to monitor/detect certain security threats and report it to the host system. Other functions try to mitigate the threat and allow the receiver to operate normally.

The table below gives an overview about possible threats and which functionality is available to detect and/or mitigate it.

| Threat                    | u-blox solution                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Over air signal integrity | Spoofing detection / monitoring<br>Jamming/interference detection / monitoring |
| GNSS receiver integrity   | Secure boot                                                                    |



| Threat | u-blox solution        |  |
|--------|------------------------|--|
|        | Secure firmware update |  |

**Table 22: u-blox security options**

#### <span id="page-53-0"></span>**3.12.1 Spoofing detection / monitoring**

Spoofing is the process where a counterfeit GNSS signal is transmitted locally to prevent the true signal from being used and so produce an erroneous position fix and/or time solution.

The spoofing detection algorithm monitors multiple observed signal parameters for suspicious changes to identify external manipulation. A flag in UBX-NAV-STATUS message (flags2 spoofDetState) alerts the user to potential spoofing activity.

A detection is successful when a signal is observed to transition from an initially genuine one to a spoofed version. Hence detection is not possible if the receiver is started under spoofing conditions. The detection algorithms rely on availability of signals from multiple GNSS constellations - the detection algorithm does not work in single-GNSS mode.

#### <span id="page-53-1"></span>**3.12.2 Jamming/interference detection / monitoring**

The field jamInd of the UBX-MON-RF message can be used as an indicator for continuous wave (narrow-band) jammers/interference only. The interpretation of the value depends on the application. It is necessary to run the receiver in an unjammed environment to determine an appropriate threshold for the unjammed case. If the value rises significantly above this threshold, this indicates that a continuous wave jammer is present.

This monitoring function is always enabled.

The indicator reports any currently detected narrow-band interference over all currently configured signal bands.

#### **3.12.2.1 Jamming/interference monitor (ITFM) / broadband interference monitoring**

The field flags of the UBX-MON-RF message can be used as an indicator for both broadband and continuous wave (CW) jammers/interference. It is independent of the (CW only) jamming indicator described in [Jamming/interference](#page-53-1) indicator above.

This monitor reports whether jamming has been detected or suspected by the receiver. The receiver monitors the background noise and looks for significant changes. Normally, with no interference detected, it will report "OK". If the receiver detects that the noise has risen above a preset threshold, the receiver reports "Warning". If in addition, there is no current valid fix, the receiver reports "Critical".

| Value         | Reported state | Description                                                                                                                            |  |  |
|---------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------|--|--|
| 0             | Unknown        | Jamming/interference monitor not enabled,<br>uninitialized or antenna disconnected                                                     |  |  |
| 1             | OK             | no interference detected                                                                                                               |  |  |
| 2             | Warning        | position OK but interference is visible (above the<br>thresholds)                                                                      |  |  |
| 3<br>Critical |                | no reliable position fix and interference is visible (above<br>the thresholds); interference is probable reason why<br>there is no fix |  |  |

The monitor has four states as shown in the following table:

**Table 23: Jamming/interference monitor reported states**



The monitor is disabled by default. The monitor is enabled by setting the CFG-ITFM-ENABLE configuration item. In this message it is also possible to specify the thresholds at which broadband and CW jamming are reported. These thresholds should be interpreted as the dB level above "normal". It is also possible to specify whether the receiver expects an active or a passive antenna.

The monitoring algorithm relies on comparing the currently measured spectrum with a reference from when a good fix was obtained. Thus the monitor will only function when the receiver has had at least one (good) first fix, and will report "Unknown" before this time.

The monitor reports any currently detected interference over all currently configured signal bands.

#### <span id="page-54-0"></span>**3.12.3 GNSS receiver integrity**

#### <span id="page-54-3"></span>**3.12.3.1 Secure boot**

The ZED-F9H boots only with firmware images that are signed by u-blox. This prevents the execution of non-genuine firmware images run on the receiver.

#### <span id="page-54-4"></span>**3.12.3.2 Secure firmware update**

The firmware image itself is encrypted and signed by u-blox. The ZED-F9H verifies the signature at each start.

### <span id="page-54-1"></span>**3.13 u-blox protocol feature descriptions**

#### <span id="page-54-2"></span>**3.13.1 Broadcast navigation data**

This section describes the data reported via UBX-RXM-SFRBX.

UBX-RXM-SFRBX reports the broadcast navigation data message the receiver has collected from each tracked signal.When enabled, a separatemessage is generated each time the receiver decodes a complete subframe of data from a tracked signal. The data bits are reported as received, including preambles and error checking bits as appropriate. However, because there is considerable variation in the data structure of the different GNSS signals, the form of the reported data also varies. This document uses the term "subframe", but other GNSS data structures might use different terms, for example, GLONASS uses "strings" and Galileo uses "pages".

#### **3.13.1.1 Parsing navigation data subframes**

Each UBX-RXM-SFRBX message contains a subframe of data bits appropriate for the relevant GNSS, delivered in a number of 32-bit words, as indicated by numWords field.

Due to the variation in data structure between different GNSS, the most important step in parsing a UBX-RXM-SFRBX message is to identify the form of the data. This should be done by reading the gnssId field, which indicates which GNSS the data was decoded from. In almost all cases, this is sufficient to indicate the structure. Because of this, the following sections are organized by GNSS. However, in some cases the identity of the GNSS is not sufficient, and this is described, where appropriate, in the following sections.

In most cases, the data does not map perfectly into a number of 32-bit words and, consequently, some of the words reported in UBX-RXM-SFRBX messages contain fields marked as "Pad". These fields should be ignored and no assumption should be made about their contents.

UBX-RXM-SFRBX messages are only generated when complete subframes are detected by the receiver and all appropriate parity checks have passed.



Where the parity checking algorithm requires data to be inverted before it is decoded (e.g. GPS L1C/A), the receiver carries this out before the message output. Therefore, users can process data directly and do not need to worry about repeating any parity processing.

The meaning of the content of each subframe depends on the sending GNSS and is described in the relevant interface control documents (ICD).

#### **3.13.1.2 GPS**

The data message structure in the GPS L1C/A (LNAV) and L2C/L5 (CNAV) signals is different and thus the UBX-RXM-SFRBX message structure differs as well. For the GPS L1C/A and L2C/L5 signals it is as follows:

#### **3.13.1.2.1 GPS L1C/A**

For GPS L1C/A signals, there is a fairly straightforward mapping between the reported subframe and the structure of subframe and words described in the GPS ICD. Each subframe comprises ten data words, which are reported in the same order they are received.

Each word is arranged as follows:



#### **Figure 26: GPS L1C/A subframe word**

#### **3.13.1.2.2 GPS L2C**

For GPS L2C signals each reported subframe contains the CNAV message as described in the GPS ICD. The ten words are arranged as follows:





#### **Figure 27: GPS L2C subframe words**

#### **3.13.1.3 GLONASS**

For GLONASS L1OF signal, the UBX-RXM-SFRBX message contains a string content within the frame structure as described in the GLONASS ICD. This string comprises 85 data bits which are reported over three 32-bit words in the message. Data bits 1 to 8 are always a hamming code, while bits 81 to 84 are a string number and bit 85 is the idle chip, which should always have a value of zero. The meaning of other bits varies with string and frame number.

The fourth and final 32-bit word in the UBX-RXM-SFRBX message contains frame and superframe numbers (where available). These values are not actually transmitted by the satellites, but are deduced by the receiver and are included to aid decoding of the transmitted data. However, the receiver does not always know these values, in which case a value of zero is reported.

The four words are arranged as follows:





#### **Figure 28: GLONASS navigation message data**

In some circumstances, (especially on startup) the receiver may be able to decode data from a GLONASS satellite before it can identify it. When this occurs UBX-RXM-SFRBX messages will be issued with an svId of 255 to indicate "unknown".

#### **3.13.1.4 BeiDou**

For BeiDou signals there is a fairly straightforward mapping between the reported subframe and the structure of subframe and words described in the BeiDou ICD. Each subframe comprises ten data words, which are reported in the same order they are received.

Each word is arranged as follows:

| <b>MSB</b> |               |                 | <b>LSB</b>       |
|------------|---------------|-----------------|------------------|
| to<br>10   | Pad<br>2 bits | Data<br>22 bits | Parity<br>8 bits |

#### **Figure 29: BeiDou subframe word**

Note that as the BeiDou data words only comprise 30 bits, the 2 most significant bits in each word reported by UBX-RXM-SFRBX are padding and should be ignored.

#### **3.13.1.5 Galileo**

The Galileo E1-B and E5b in-phase signals transmit the I/NAV data message but in different configurations to enhance down-load time for dual frequency receivers. The UBX-RXM-SFRBX structure for the I/NAV message is shown below.



#### **3.13.1.5.1 Galileo E1-B**

For the Galileo E1-B signal, each reported subframe contains a pair of I/NAV pages as described in the Galileo ICD. Galileo pages can either be "Nominal" or "Alert" pages. For Galileo "Nominal" pages the eight words are arranged as follows:



**Figure 30: Galileo E1-B subframe words**



Alert pages are reported in very similar manner, but the page type bits will have value 1 and the structure of the eight words will be slightly different (as indicated by the Galileo ICD).

#### **3.13.1.5.2 Galileo E5b**

For the Galileo E5b in-phase signal data component, each reported subframe contains a pair of I/ NAV pages as described in the Galileo ICD. Galileo pages can either be "Nominal" or "Alert" pages. For Nominal pages the eight words are arranged as follows:



**Figure 31: Galileo E5b subframe words**



#### **3.13.1.6 SBAS**

For SBAS (L1C/A) signals each reported subframe contains eight 32-bit data words to deliver the 250 bits transmitted in each SBAS data block.

The eight words are arranged as follows:



#### **Figure 32: SBAS subframe words**

#### **3.13.1.7 QZSS**

The structure of the data delivered by QZSS L1C/A signals is effectively identical to that of GPS (L1C/A). Similarly the structure of the data delivered by the QZSS L2C signal is effectively identical to that of GPS (L2C). Similarly the structure of the data delivered by the QZSS L1S signal is effectively identical to that of SBAS (L1C/A).

#### **3.13.1.8 Summary**

The following table gives a summary of the different data message formats reported by the UBX-RXM-SFRBX message:

| GNSS    | Signal | gnssId | sigId | numWords | period |  |
|---------|--------|--------|-------|----------|--------|--|
| GPS     | L1C/A  | 0      | 0     | 10       | 6s     |  |
| GPS     | L2CL   | 0      | 3     | 10       | 12s    |  |
| GPS     | L2CM   | 0      | 4     | 10       | 12s    |  |
| SBAS    | L1C/A  | 1      | 0     | 9        | 1s     |  |
| Galileo | E1 B   | 2      | 1     | 8        | 2s     |  |
| Galileo | E5b I  | 2      | 5     | 8        | 2s     |  |
| BeiDou  | B1I D1 | 3      | 0     | 10       | 6s     |  |
| BeiDou  | B1I D2 | 3      | 1     | 10       | 0.6s   |  |
| BeiDou  | B2I D1 | 3      | 2     | 10       | 6s     |  |
| BeiDou  | B2I D2 | 3      | 3     | 10       | 0.6s   |  |
| QZSS    | L1C/A  | 5      | 0     | 10       | 6s     |  |
| QZSS    | L1S    | 5      | 1     | 9        | 1s     |  |
| QZSS    | L2CM   | 5      | 4     | 10       | 12s    |  |





| GNSS    | Signal | gnssId | sigId | numWords | period |
|---------|--------|--------|-------|----------|--------|
| QZSS    | L2CL   | 5      | 5     | 10       | 12s    |
| GLONASS | L1OF   | 6      | 0     | 3        | 2s     |
| GLONASS | L2OF   | 6      | 2     | 3        | 2s     |

**Table 24: Data message formats reported by UBX-RXM-SFRBX**

## <span id="page-61-0"></span>**3.14 Forcing a receiver reset**

Typically, in GNSS receivers, a distinction is made between cold, warm, and hot start, depending on the type of valid information the receiver has at the time of the restart.

- **Cold start:** In cold start mode, the receiver has no information from the last position (e.g. time, velocity, frequency etc.) at startup. Therefore, the receiver must search the full time and frequency space, and all possible satellite numbers. If a satellite signal is found, it is tracked to decode the ephemeris (18-36 seconds under strong signal conditions), whereas the other channels continue to search satellites. Once there is a sufficient number of satellites with valid ephemeris, the receiver can calculate position and velocity data. Other GNSS receiver manufacturers call this startup mode **Factory startup**.
- **Warm start:** In warm start mode, the receiver has approximate information for time, position, and coarse satellite position data (Almanac). In this mode, after power-up, the receiver normally needs to download ephemeris before it can calculate position and velocity data. As the ephemeris data usually is outdated after 4 hours, the receiver will typically start with a warm start if it has been powered down for more than 4 hours. In this scenario, several augmentations are possible. See Multiple GNSS [assistance.](#page-43-0)
- **Hot start:** In hot start mode, the receiver was powered down only for a short time (4 hours or less), so that its ephemeris is still valid. Since the receiver does not need to download ephemeris again, this is the fastest startup method.

Using the UBX-CFG-RST message, you can force the receiver to reset and clear data, in order to see the effects of maintaining/losing such data between restarts. For this, the UBX-CFG-RST message offers the navBbrMask field, where hot, warm and cold starts can be initiated, and also other combinations thereof.

The reset type can also be specified.This is not related to GNSS, but to the way the software restarts the system.

- **Hardware reset** uses the on-chip watchdog, in order to electrically reset the chip. This is an immediate, asynchronous reset. No Stop events are generated.
- **Controlled software reset** terminates all running processes in an orderly manner and, once the system is idle, restarts operation, reloads its configuration and starts to acquire and track GNSS satellites.
- **Controlled software reset (GNSS only)** only restarts the GNSS tasks, without reinitializing the full system or reloading any stored configuration.
- **Hardware reset (after shutdown)** uses the on-chip watchdog. This is a reset after shutdown.
- **Controlled GNSS stop** stops all GNSS tasks. The receiver will not be restarted, but will stop any GNSS-related processing.
- **Controlled GNSS start** starts all GNSS tasks.

## <span id="page-61-1"></span>**3.15 Firmware upload**

ZED-F9H is supplied with firmware. u-blox may release updated images containing, for example, security fixes, enhancements, bug fixes, etc. Therefore it is important that customers implement a firmware update mechanism in their system.



A firmware image is a binary file containing the software to be run by the GNSS receiver. A firmware update is the process of transferring a firmware image to the receiver and storing it in non-volatile flash memory.

Contact u-blox for more information on firmware update.

## <span id="page-62-0"></span>**3.16 Spectrum analyzer**

Supported from firmware version HDG 1.13 onwards

The UBX-MON-SPAN message provides a low-resolution RF spectrum analyzer function sufficient to identify noise or jammers in the receiver's reception band(s). It can be used for monitoring potential interferors during customer integration and in normal operation to identify interference, e.g. when the UBX-MON-RF message detects a possible jamming threat.See [Jamming/interference](#page-53-1) [indicator](#page-53-1) for more details. u-center provides a visualization of the message spectrum output(s) with features for max-hold and averaging.

This message is intended for comparative analysis of the RF spectrum rather than absolute and precise measurement.

The message is output once per second when enabled. Depending on the receiver type, one or two measurement blocks will be output, indicated by the numRfBlocks flag field. The first block provides L1 spectrum data which can be followed by an L2 or L5 block with multi-band receivers.

Each block comprises the following data:

- 256 spectrum data points (0.25 dB units)
- Spectrum span (Hz)
- Spectrum bin resolution (Hz)
- Center frequency (Hz)
- PGA setting (dB)

The frequency of each point can be calculated by Freq(i) = center frequency + spectrum span \* (i-128) / 256, where i=0-255. The number of points = span/resolution and is scaled in units of 0.25 dB. Changes in the PGA gain value can indicate an increased input in RF signal activity compared to normal operation.

[Figure](#page-63-0) 33 shows the spectrum view in u-center with the view/hold option selected. The red line represents the frozen spectrum before modifying the external gain, while the black line represents the current measurement.



<span id="page-63-0"></span>

#### **Figure 33: Spectrum analyzer view in u-center with the option view/hold selected**

- The span frequency depends on the number of constellations enabled which impacts the spectrum resolution owing to a fixed set of points. For further details about this message see the interface description [\[2\]](#page-95-2).
- A spur may be visible at the center frequency, this comes internally from the receiver and does not cause any performance degradation.



## <span id="page-64-0"></span>**4 Design**

This section provides information to help carry out a successful schematic and PCB design integrating the ZED-F9H.

## <span id="page-64-1"></span>**4.1 Pin assignment**

The pin assignment of the ZED-F9H module is shown in [Figure](#page-64-2) 34. The defined configuration of the PIOs is listed in [Table](#page-64-3) 25.

The ZED-F9H is an LGA package with the I/O on the outside edge and central ground pads.

<span id="page-64-2"></span>

#### **Figure 34: ZED-F9H pin assignment**

<span id="page-64-3"></span>

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
| 42      | TXD / SPI_MISO | O   | Host UART output if D_SEL = 1(or open). SPI_MISO if D_SEL = 0            |
| 43      | RXD / SPI_MOSI | I   | Host UART input if D_SEL = 1(or open). SPI_MOSI if D_SEL = 0             |
| 44      | SDA / SPI_CS_N | I/O | I2C Data if D_SEL = 1 (or open). SPI Chip Select if D_SEL = 0            |
| 45      | SCL / SPI_CLK  | I/O | I2C Clock if D_SEL = 1(or open). SPI Clock if D_SEL = 0                  |
| 46      | TX_READY       | O   | TX_Buffer full and ready for TX of data                                  |
| 47      | D_SEL          | I   | Interface select for pins 42-45                                          |
| 48      | GND            | -   | Ground                                                                   |
| 49      | RESET_N        | I   | RESET_N                                                                  |
| 50      | SAFEBOOT_N     | I   | SAFEBOOT_N (for future service, updates and reconfiguration, leave OPEN) |



| Pin no. | Name      | I/O | Description            |
|---------|-----------|-----|------------------------|
| 51      | EXTINT    | I   | External Interrupt Pin |
| 52      | Reserved  | -   | Reserved               |
| 53      | TIMEPULSE | O   | Time pulse             |
| 54      | Reserved  | -   | Reserved               |
|         |           |     |                        |

**Table 25: ZED-F9H pin assignment**

## <span id="page-66-0"></span>**4.2 Power supply**

The u-blox ZED-F9H module has three power supply pins: VCC, V\_BCKP and V\_USB.

#### <span id="page-66-1"></span>**4.2.1 VCC: Main supply voltage**

The **VCC** pin is connected to the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude. For this reason, it is important that the supply circuitry be able to support the peak power for a short time (see the applicable data sheet [\[1](#page-95-3)] for specification).

The module integrates a DC/DC converter, which allows reduced power consumption.

- When switching from backup mode to normal operation or at startup, u-blox ZED-F9H modules must charge the internal capacitors in the core domain. In certain situations, this can result in a significant current draw. For low-power applications using backup mode, it is important that the power supply or low ESR capacitors at the module input can deliver this current/charge.
- To reduce peak current during power on, users can employ an LDO that has an in-built current limiter.
- Do not add any series resistance greater than 0.2 Ω to the VCC supply as it will generate input voltage noise due to dynamic current conditions.
- For the ZED-F9H module the equipment must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1.

#### <span id="page-66-2"></span>**4.2.2 V\_BCKP: Backup supply voltage**

The V\_BCKP pin can be used to provide power to maintain the real-time clock (RTC) and batterybacked RAM (BBR) when VCC is removed.

If the module supply has a power failure, the **V\_BCKP** pin supplies the real-time clock (RTC) and battery-backed RAM (BBR). Use of valid time and the GNSS orbit data at start up will improve the GNSS performance, as with hot starts and warm starts.

If V\_BCKP is not provided, the module performs a cold start at power up.

If a host is connected to ZED-F9H, V\_BCKP can be partially emulated by using UBX-UPD-SOS functionality. BBR data can saved to the host and restored at startup. See the applicable [Interface](#page-95-2) [description](#page-95-2) for more information.

- Avoid high resistance on the **V\_BCKP** line: During the switch from main supply to backup supply, a short current adjustment peak can cause a high voltage drop on the pin with possible malfunctions.
- Add a 2 uF capacitor on the V\_BCKP pin to absorb the current adjustment peak when switching from VCC to V\_BCKP supply.
- If no backup supply voltage is available, connect the **V\_BCKP** pin to **VCC**.



Allow all I/O including UART and other interfaces to float or connect to a high impedance in HW backup mode (V\_BCKP supplied when VCC is removed). See the [Interfaces](#page-37-0) section.

#### **Real-time clock (RTC)**

The real-time clock (RTC) is driven by a 32-kHz oscillator using an RTC crystal. If VCC is removed while a battery is connected to **V\_BCKP**, most of the receiver is switched off leaving the RTC and BBR powered. This operating mode is called Hardware Backup Mode which enables time keeping and all relevant data to be saved to allow a hot or warm start.

#### <span id="page-67-0"></span>**4.2.3 ZED-F9H power supply**

The ZED-F9H requires a low-noise, low-dropout voltage, and a very low source impedance power supply of 3.3 V typically. No inductors or ferrite beads should be used from LDO to the module VCC pin. The peak currents need to be taken into account for the source supplying the LDO for the module.

A power supply fed by 5 V is shown in the figure below. This example circuit is intended only for the module supply.



**Figure 35: ZED-F9H power supply**

## <span id="page-67-1"></span>**4.3 ZED-F9H minimal design**

The minimal electrical circuit for ZED-F9H operation using the UART1 interface is shown in [Figure](#page-68-1) [36](#page-68-1) below.



<span id="page-68-1"></span>

#### **Figure 36: Minimal ZED-F9H design**

For a minimal design with the ZED-F9H GNSS modules, the following functions and pins should be considered:

- Connect the power supply to VCC and V\_BCKP.
- If hot or warm start operations are needed, connect a backup battery to V\_BCKP.
- If USB is not used connect V\_USB to ground.
- Ensure an optimal ground connection to all ground pins of the ZED-F9H GNSS module.
- If antenna bias is required, see ZED-F9H [antenna](#page-70-0) bias section.

The host interface typically supplies the RTCM messages required for RTK operation.

## <span id="page-68-0"></span>**4.4 Antenna**

The ZED-F9H requires an active antenna with integral LNA to ensure good performance under nominal signal reception.

When implementing a custom antenna installation, it is recommended that an OEM active antenna module be used that meets our specification. Implementing a custom active antenna design is an important exercise to meet the required bandwidths and group delay specifications compared to previous L1-only designs.

A typical dual band antenna design block diagram is shown below taken from the u-blox ANN-MB active antenna product.





#### **Figure 37: u-blox low cost dual-band antenna internal structure**

A suitable ground plane is required for the antenna to achieve good performance.

Location of the antenna is critical to reach the stated performance. For timing receivers locate to provide a good all round sky view. Unsuitable locations within a vehcle could include, under vehicle dash, rear-view mirror location, etc.

A set of recommended specifications for a dual band active antenna is given below.

| Specification                                                                         |                                  |
|---------------------------------------------------------------------------------------|----------------------------------|
| Minimum gain6                                                                         | 17 dB                            |
| 6<br>Maximum gain                                                                     | 50 dB                            |
| Noise figure                                                                          | <4 dB                            |
| 10 ns max at each GNSS system bandwidth. Note:<br>Inter-signal requirement 50 ns max. |                                  |
| 40 dB typ                                                                             |                                  |
| 8<br>L1 band antenna gain                                                             | 1559 - 1606 MHz:<br>3 dBic typ.  |
| 8<br>L2/E5b band antenna gain                                                         | 1197 - 1249 MHz:<br>2 dBic typ.  |
| Polarization                                                                          | RHCP                             |
| Axial ratio                                                                           | 2 dB max, at<br>Zenith           |
| Phase center variation                                                                | <10 mm over<br>elevation/azimuth |
| 9<br>EMI immunity out-of-band                                                         | 30 V/m                           |
| 15 kV human body model air discharge                                                  |                                  |
|                                                                                       |                                  |

**Table 26: Antenna specifications for ZED-F9H modules**

<span id="page-69-0"></span><sup>6</sup> Including passive losses (filters, cables, connectors etc.)

<span id="page-69-1"></span><sup>7</sup> GNSS system bandwidths: B1I 1559… 1563 MHz; L1,E1,B1C 1573… 1578 MHz; L1OF 1598… 1606 MHz; E5b,B2I 1192… 1212 MHz; L2C 1223… 1231 MHz; L2OF 1242… 1249 MHz

<span id="page-69-2"></span><sup>8</sup> Measured with a ground plane d=150 mm

<span id="page-69-3"></span><sup>9</sup> Exception L1,L2 bands +/- 200 MHz, emphasis on cellular bands



The antenna system should include filtering to ensure adequate protection from nearby transmitters. Take care in the selection of antennas placed close to cellular or Wi-Fi transmitting antennas.

#### <span id="page-70-0"></span>**4.4.1 Antenna bias**

Active antennas have an integrated low-noise amplifier that contributes an additional current of typically 5 to 20 mA to the system's power consumption budget.

If customers do not want to make use of the antenna supervisor function the filtered VCC\_RF supply voltage output can supply the antenna if the supply voltage of the ZED-F9H module matches the antenna working voltage (e.g. 3.0 V).

A series current limiting resistor is required to prevent short circuits destroying the bias-t inductor.

The bias-t inductor must be chosen for multi-band operation, a value of 47 nH ±5% is recommended for the recommended Murata L part. It has a self-resonance frequency of 1 GHz and a high impedance (> 500 Ω) at L-band frequencies.

The recommended bias-t inductor (Murata LQG15HS47NJ02) has a maximum current capacity of 300 mA. Hence the current is limited to 70 mA at 3.3V using an active limiter in the recommended circuit shown in [Figure](#page-71-0) 39 below. A 10 Ω resistor (R2)is provided to measure the current.This resistor power rating must be chosen to ensure reliability in the chosen circuit design.



**Figure 38: ZED-F9H antenna bias inductor impedance**

A recommended circuit design for an active antenna bias is shown below. This example shows an external voltage of 3.3 V with current limiting as described above. An ESD protection diode should also be connected to the input as shown.



<span id="page-71-0"></span>

#### **Figure 39: ZED-F9H reference design for antenna bias**

L1: Murata LQG15HS47NJ02 0402 47 N 5% 0.30 A -55/+125 C

D1: TYCO, 0.25PF, PESD0402-140 -55/+125C

C3: MURATA GRM033R61E104KE14 CER X5R 0201 100N 10% 25V

R2: RES THICK FILM CHIP 1206 10R 5% 0.25W

It is recommended to use active current limiting. If active current limiting is not used, the important points covered below need to be taken into account:



#### **Figure 40: ZED-F9H VCC\_RF antenna bias**

The bias-t inductor and current limiting resistor must be selected to be reliable with a shortcircuit on the antenna feed if no active current limiter is used. Our recommended part has a limit of 300 mA. A part with a higher current capability will be needed if the short circuit current is as described here. This will also be affected by the voltage level of the antenna



bias supply due to power dissipation. Take the current limit capability of the antenna bias supply into consideration. In the case where the module supplies the voltage via VCC\_RF, a higher value resistor will be needed to ensure the module supply inductor is protected. The current should be limited to below 150 mA at the module supply voltage under short-circuit conditions. In this case a value of 17 Ω or more is required at a module supply of 3 V to limit short circuit current to 150 mA. The DC resistance of the bias-t inductor is assumed to be 1-2 Ω and the module internal feed inductor is assumed to be 1.2 Ω.

If the VCC\_RF voltage does not match with the supply voltage of the active antenna, use a filtered external supply.

The power dissipation in the resistor and inductor needs to be taken into account based on the supply voltage and short circuit current. The bias-t inductor current capability and the bias resistor value need to be calculated as shown above. The supply voltage for the bias-t and its current capability is part of the calculation.



**Figure 41: ZED-F9H external voltage antenna bias**

## <span id="page-72-0"></span>**4.5 EOS/ESD precautions**

- To avoid overstress damage during production or in the field it is essential to observe strict EOS/ESD/EMI handling and protection measures.
- To prevent overstress damage at the RF\_IN of your receiver, never exceed the maximum input power as specified in the applicable data sheet [\[1\]](#page-95-3).

When integrating GNSS receivers into wireless systems, pay special attention to electromagnetic and voltage susceptibility issues. Wireless systems include components which can produce Electrostatic Discharge (ESD), Electrical Overstress (EOS) and Electro-Magnetic Interference (EMI). CMOS devices are more sensitive to such influences because their failure mechanism is defined by the applied voltage, whereas bipolar semiconductors are more susceptible to thermal overstress. The following design guidelines help in designing robust yet cost-effective solutions.

### <span id="page-72-1"></span>**4.5.1 ESD protection measures**

GNSS receivers are sensitive to Electrostatic Discharge (ESD). Special precautions are required when handling. Most defects caused by ESD can be prevented by following strict ESD protection rules for production and handling. When implementing passive antenna patches or external antenna connection points, then additional ESD measures as shown in the figure below can also avoid failures in the field.





**Figure 42: RF ESD precautions**

#### <span id="page-73-0"></span>**4.5.2 EOS precautions**

Electrical overstress (EOS) usually describes situations when the maximum input power exceeds the maximum specified ratings. EOS failure can happen if RF emitters are close to a GNSS receiver or its antenna. EOS causes damage to the chip structures. If the RF\_IN is damaged by EOS, it is hard to determine whether the chip structures have been damaged by ESD or EOS.

EOS protection measures as shown in the figure below are recommended for any designs combining wireless communication transceivers (e.g. GSM, GPRS) and GNSS in the same design or in close proximity.



**Figure 43: Active antenna EOS protection**

#### <span id="page-73-1"></span>**4.5.3 Safety precautions**

The ZED-F9H must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1. In addition to external limited power source, only Separated or Safety Extra-Low Voltage (SELV) circuits are to be connected to the module including interfaces and antennas.

For more information about SELV circuits see section 2.2 in Safety standard IEC 60950-1.

## <span id="page-73-2"></span>**4.6 Electromagnetic interference on I/O lines**

Any I/O signal line with a length greater than approximately 3 mm can act as an antenna and may pick up arbitrary RF signals transferring them as noise into the receiver. This specifically applies to unshielded lines, in which the corresponding GND layer is remote or missing entirely, and lines close to the edges of the printed circuit board.

If, for example, a cellular signal radiates into an unshielded high-impedance line, it is possible to generate noise in the order of volts and not only distort receiver operation but also damage it



permanently. Another type of interference can be caused by noise generated at the PIO pins that emits from unshielded I/O lines. Receiver performance may be degraded when this noise is coupled into the GNSS antenna.

EMI protection measures are particularly useful when RF emitting devices are placed next to the GNSS receiver and/or to minimize the risk of EMI degradation due to self-jamming. An adequate layout with a robust grounding concept is essential in order to protect against EMI.

Intended Use: In order to mitigate any performance degradation of a radio equipment under EMC disturbance, system integration shall adopt appropriate EMC design practice and not contain cables over three meters on signal and supply ports.

#### <span id="page-74-0"></span>**4.6.1 General notes on interference issues**

Received GNSSsignalpower at the antenna is very low. At thenominal receivedsignal strength(-128 dBm) it is below the thermal noise floor of -111 dBm. Due to this fact, a GNSS receiver is susceptible to interference from nearby RF sources of any kind. Two cases can be distinguished:

- Out-of-band interference: Typically any kind of wireless communications system (e.g. LTE, GSM, CDMA, 3G, WLAN, Bluetooth, etc.) may emit its specified maximum transmit power in close proximity to the GNSS receiving antenna, especially if such a system is integrated with the GNSS receiver. Even at reasonable antenna selectivity, destructive power levels may reach the RF input of the GNSS receiver. Also, larger signal interferers may generate intermodulation products inside the GNSS receiver front-end that fall into the GNSS band and contribute to inband interference.
- In-band interference: Although the GNSS band is kept free from intentional RF signal sources by radio-communications standards, many devices emit RF power into the GNSS band at levels much higher than the GNSS signal itself. One reason is that the frequency band above 1 GHz is not well regulated with regards to EMI, and even if permitted, signal levels are much higher than GNSS signal power. Notably, all types of digital equipment, such as PCs, digital cameras, LCD screens, etc. tend to emit a broad frequency spectrum up to several GHz of frequency. Also wireless transmitters may generate spurious emissions that fall into GNSS band.

As an example, GSM uses power levels of up to 2 W (+33 dBm). The absolute maximum power input at the RF input of the GNSS receiver can be +15 dBm. The GSM specification allows spurious emissions for GSM transmitters of up to +36 dBm, while the GNSS signal is less than -128 dBm. By simply comparing these numbers it is obvious that interference issues must be seriously considered in any design of a GNSS receiver. Different design goals may be achieved through different implementations:

- The primary focus is to prevent damaging the receiver from large input signals. Here the GNSS performance under interference conditions is not important and suppression of the signal is permitted. It is sufficient to just observe the maximum RF power ratings of all of the components in the RF input path.
- GNSS performance must be guaranteed even under interference conditions. In such a case, not only the maximum power ratings of the components in the receiver RF path must be observed. Further, non-linear effects like gain compression, NF degradation (desensitization) and intermodulation must be analyzed.
- Pulsed interference with a low-duty cycle such as GSM may be destructive due to the high peak power levels.

#### <span id="page-74-1"></span>**4.6.2 In-band interference mitigation**

With in-band interference, the signal frequency is very close to the GNSS frequency. Such interference signals are typically caused by harmonics fromdisplays,micro-controller operation, bus systems, etc. Measures against in-band interference include:



- Maintaining a good grounding concept in the design
- Shielding
- Layout optimization
- Low-pass filtering of noise sources, e.g. digital signal lines
- Remote placement of the GNSS antenna, far away from noise sources
- Adding an LTE, CDMA, GSM, WCDMA, BT band-pass filter before antenna

#### <span id="page-75-0"></span>**4.6.3 Out-of-band interference**

Out-of-band interference is caused by signal frequencies that are different from the GNSS carrier frequency. The main sources are wireless communication systems such as LTE, GSM, CDMA, WCDMA, Wi-Fi, BT, etc.

Measures against out-of-band interference include maintaining a good grounding concept in the design and adding a GNSS band-pass filter into the antenna input line to the receiver.

For GSM applications, such as typical handset design, an isolation of approximately 20 dB can be reached with careful placement of the antennas. If this is insufficient, an additional SAW filter is required on the GNSS receiver input to block the remaining GSM transmitter energy.

## <span id="page-75-1"></span>**4.7 Layout**

This section details layout and placement requirements of the ZED-F9H high precision receiver.

#### <span id="page-75-2"></span>**4.7.1 Placement**

GNSS signals at the surface of the Earth are below the thermal noise floor. A very important factor in achieving maximum GNSS performance is the placement of the receiver on the PCB. The placement used may affect RF signal loss from antenna to receiver input and enable interference into the sensitive parts of the receiver chain, including the antenna itself. When defining a GNSS receiver layout, the placement of the antenna with respect to the receiver, as well as grounding, shielding and interference from other digital devices are crucial issues and need to be considered very carefully.

Signal loss on the RF connection from antenna to receiver input must be minimized as much as possible. Hence, the connection to the antenna must be kept as short as possible.

Ensure that RF critical circuits are clearly separated from any other digital circuits on the system board. To achieve this, position the receiver digital part closer to the digital section of the system PCB and have the RF section and antenna placed as far as possible away from the other digital circuits on the board.

A proper GND concept shall be followed: The RF section shall not be subject to noisy digital supply currents running through its GND plane.

#### <span id="page-75-3"></span>**4.7.2 Thermal management**

During design-in do not place the receiver near sources of heating or cooling. The receiver oscillator is sensitive to sudden changes in ambient temperature which can adversely impact satellite signal tracking. Sources can include co-located power devices, cooling fans or thermal conduction via the PCB. Take into account the following questions when designing in the receiver.

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?



High temperature drift and air vents can affect the GNSS performance. For best performance, avoid high temperature drift and air vents near the receiver.

#### <span id="page-76-0"></span>**4.7.3 Package footprint, copper and paste mask**

Copper and solder mask dimensioning recommendations for the ZED-F9H module packages are provided in this section.

These are recommendations only and not specifications. The exact copper, solder and paste mask geometries, distances, stencil thickness and solder paste volumes must be adapted to the specific production processes (e.g. soldering etc.) of the customer.

Refer to the applicable data sheet [\[1\]](#page-95-3) for the mechanical dimensions.

#### **4.7.3.1 Footprint**



**Figure 44: ZED-F9H suggested footprint (i.e. copper mask)**



#### **4.7.3.2 Paste mask**



**Figure 45: ZED-F9H suggested paste mask**

#### <span id="page-77-0"></span>**4.7.4 Layout guidance**

The presented layout guidance reduces the risk of performance issues at design level.

#### **4.7.4.1 RF In trace**

The RF in trace has to work in the combined GNSS signal bands.

For FR-4 PCB material with a dielectric permittivity of for example 4.7, the trace width for the 50 Ω line impedance can be calculated.

A grounded co-planar RF trace is recommended as it provides the maximum shielding from noise with adequate vias to the ground layer.

The RF trace must be shielded by vias to ground along the entire length of the trace and the ZED-F9H RF\_IN pad should be surrounded by vias as shown in the figure below.





**Figure 46: RF input trace**

The RF\_IN trace on the top layer should be referenced to a suitable ground layer.

#### **4.7.4.2 Vias for the ground pads**

The ground pads under the ZED-F9H high precision receiver need to be grounded with vias to the lower ground layer of the PCB. A solid ground layer fill on the top layer of the PCB is recommended. This is shown in the figure below.



**Figure 47: Top layer fill and vias**

#### **4.7.4.3 VCC pads**

The VCC pads for the ZED-F9H high precision receiver must have as low impedance as possible with large vias to the lower power layer of the PCB. The VCC pads need a large combined pad and the decoupling capacitors must be placed as close as possible. This is shown in the figure below.





**Figure 48: VCC pads**

## <span id="page-79-0"></span>**4.8 Design guidance**

### <span id="page-79-1"></span>**4.8.1 General considerations**

Check power supply requirements and schematic:

- Is the power supply voltage within the specified range and noise-free?
- If USB is not used, connect the V\_USB pin to ground.
- It is recommended to have a separate LDO for V\_USB that is enabled by the module VCC. This is to comply with the USB self-powered specification.
- If USB is used, is there a 1 uF capacitor right near the V\_USB pin? This is just for the V\_USB pin.
- Is there a 1 uF cap right next to the module VCC pin?
- Compare the peak current consumption of the ZED-F9H GNSS module with the specification of your power supply.
- GNSS receivers require a stable power supply. Avoid series resistance (less than 0.2 Ω) in your power supply line (the line to VCC) to minimize the voltage ripple on VCC. See the ZED-F9H Power [supply](#page-66-0) section in the [Design](#page-64-0) chapter for more information on the power supply requirements.
- Allow all I/O to Float/High impedance (High-Z) when VCC is not applied.

#### <span id="page-79-2"></span>**4.8.2 Backup battery**

Check backup supply requirements and schematic:

- For achieving a minimal time to first fix (TTFF) after a power down (warm starts, hot starts), make sure to connect a backup battery to V\_BCKP.
- Verify that your battery backup supply can provide the battery backup current specified in the applicable data sheet.
- Allow all I/O including UART and other interfaces to Float/High impedance in HW backup mode (battery backup connected with VCC removed).

#### <span id="page-79-3"></span>**4.8.3 RF front-end circuit options**

It is important that the RF input is fed by an active antenna meeting the requirements for the ZED-F9H.

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

#### <span id="page-80-0"></span>**4.8.4 Antenna/RF input**

Check RF input requirements and schematic:

- An OEM active antenna module that meets our requirements should be used if there is a need to integrate the antenna.
- The total maximum noise figure including external LNA (or the LNA in the active antenna) should be around 3 dB.
- Ensure active antenna gain is ideally between 30 40 dB gain.
- Make sure the antenna is not placed close to noisy parts of the circuitry and does not face any other noisy elements (for example micro-controller, display).
- Signal levels above 40 C/N0 average are required for optimal RTK performance.
- If a patch type antenna is used, an antenna ground plane with minimum 100 150 mm diameter is required.
- Ensure antenna supports both L1 and L2 bands.
- Ensure antenna element gain is between 2 and 3 dBic typical for each band.
- Ensure the group delay variation including active antenna is 10 ns max at each GNSS system bandwidth. Note: Inter-signal requirement 50 ns max.
- ESD protection on the RF input is mandatory.
- A Bias-t inductor must be selected with high impedance in the GNSS bands.



• Ensure RF trace is tuned for 50 Ω to ensure adequate bandwidth and power matching.

#### <span id="page-81-0"></span>**4.8.5 Ground pads**

Ensure the ground pads of the module are connected to ground.

#### <span id="page-81-1"></span>**4.8.6 Schematic design**

For a **minimal design** with the ZED-F9H GNSS modules, consider the following functions and pins:

- Connect the power supply to VCC and V\_BCKP.
- V\_USB: If USB is used it is recommended V\_USB is to be powered as per USB self-powered mode specification.
- If USB is not used connect V\_USB to ground.
- Ensure an optimal ground connection to all ground pins of the ZED-F9H GNSS module.
- Choose the required serial communication interfaces (UART, USB, SPI or I2C) and connect the appropriate pins to your application.
- If you need hot or warm start in your application, connect a backup battery to V\_BCKP.
- Antenna bias is required, see ZED-F9H antenna bias section.

#### <span id="page-81-2"></span>**4.8.7 Layout design-in guideline**

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?
- Is the receiver placed as recommended in the [Layout](#page-75-1) and Layout [guidance](#page-77-0)?
- Assure a low serial resistance on the VCC power supply line (choose a line width > 400 um).
- Keep the power supply line as short as possible.
- Add a ground plane underneath the module to reduce interference. This is especially important for the RF input line.
- For improved shielding, add as many vias as possible around the micro strip/co-planar waveguide, around the serial communication lines, underneath the module, etc.



# <span id="page-82-0"></span>**5 Product handling**

## <span id="page-82-1"></span>**5.1 ESD handling precautions**

ZED-F9H contains highly sensitive electronic circuitry and is an Electrostatic Sensitive Device (ESD). Observe precautions for handling! Failure to observe these precautions can result in severe damage to the GNSS receiver!

• Unless there is a galvanic coupling between the local GND (i.e. the work table) and the PCB GND, then the first point of contact when handling the PCB must always be between the local GND and PCB GND.

- Before mounting an antenna patch, connect ground of the device.
- When handling the RF pin, do not come into contact with any charged capacitors and be careful when contacting materials that can develop charges (e.g. patch antenna ~10 pF, coax cable ~50-80 pF/m or soldering iron).
- To prevent electrostatic discharge through the RF input, do not touch any exposed antenna area. If there is any risk that such exposed antenna area is touched in non-ESD protected work area, implement proper ESD protection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, make sure to use an ESD-safe soldering iron (tip)







## <span id="page-82-2"></span>**5.2 Soldering**

#### **Soldering paste**

Use of "no clean" soldering paste is highly recommended, as it does not require cleaning after the soldering process. The paste in the example below meets these criteria.

- Soldering paste: OM338 SAC405 / Nr.143714 (Cookson Electronics)
- Alloy specification: Sn 95.5/ Ag 4/ Cu 0.5 (95.5% tin/ 4% silver/ 0.5% copper)
- Melting temperature: 217 °C
- Stencil thickness: The exact geometry, distances, stencil thicknesses and solder paste volumes must be adapted to the customer's specific production processes (e.g. soldering).

#### **Reflow soldering**

**A convection-type soldering oven is highly recommended** over the infrared-type radiation oven. Convection-heated ovens allow precise control of the temperature, and all parts will heat up evenly, regardless of material properties, thickness of components and surface color.



As a reference, see "IPC-7530 Guidelines for temperature profiling for mass soldering (reflow and wave) processes", published in 2001.

#### **Preheat phase**

During the initial heating of component leads and balls, residual humidity will be dried out. Note that the preheat phase does not replace prior baking procedures.

- Temperature rise rate: max 3 °C/s. If the temperature rise is too rapid in the preheat phase, excessive slumping may be caused
- Time: 60 120 s. If the preheat is insufficient, rather large solder balls tend to be generated. Conversely, if performed excessively, fine balls and large balls will be generated in clusters
- End temperature: 150 200 °C. If the temperature is too low, non-melting tends to be caused in areas containing large heat capacity

#### **Heating - reflow phase**

The temperature rises above the liquidus temperature of 217 °C. Avoid a sudden rise in temperature as the slump of the paste could become worse.

- Limit time above 217 °C liquidus temperature: 40 60 s
- Peak reflow temperature: 245 °C

#### **Cooling phase**

A controlled cooling prevents negative metallurgical effects of the solder (solder becomes more brittle) and possible mechanical tensions in the products. Controlled cooling helps to achieve bright solder fillets with a good shape and low contact angle.

- Temperature fall rate: max 4 °C/s
- To avoid falling off, the modules should be placed on the topside of the motherboard during soldering.

The final soldering temperature chosen at the factory depends on additional external factors such as the choice of soldering paste, size, thickness and properties of the base board, etc. Exceeding the maximum soldering temperature in the recommended soldering profile may permanently damage the module.



**Figure 49: Soldering profile**



Modules **must not** be soldered with a damp heat process.

#### **Optical inspection**

After soldering the module, consider optical inspection.

#### **Cleaning**

Do not clean with water, solvent, or ultrasonic cleaner:

- Cleaning with water will lead to capillary effects where water is absorbed into the gap between the baseboard and the module. The combination of residues of soldering flux and encapsulated water leads to short circuits or resistor-like interconnections between neighboring pads.
- Cleaning with alcohol or other organic solvents can result in soldering flux residues flowing underneath the module, into areas that are not accessible for post-cleaning inspections. The solvent will also damage the sticker and the printed text.
- Ultrasonic cleaning will permanently damage the module, in particular the quartz oscillators.

The best approach is to use a "no clean" soldering paste and eliminate the cleaning step after the soldering.

#### **Repeated reflow soldering**

Repeated reflow soldering processes or soldering the module upside down are not recommended.

A board that is populated with components on both sides may require more than one reflow soldering cycle. In such a case, the process should ensure the module is only placed on the board submitted for a single final upright reflow cycle. A module placed on the underside of the board may detach during a reflow soldering cycle due to lack of adhesion.

The module can also tolerate an additional reflow cycle for re-work purposes.

#### **Wave soldering**

Base boards with combined through-hole technology (THT) components and surface-mount technology (SMT) devices require wave soldering to solder the THT components. Only a single wave soldering process is encouraged for boards populated with modules.

#### **Rework**

We do not recommend using a hot air gun because it is an uncontrolled process and can damage the module.

Use of a hot air gun can lead to overheating and severely damage the module. Always avoid overheating the module.

After the module is removed, clean the pads before re-applying solder paste, placing and reflow soldering a new module.

Never attempt a rework on the module itself, e.g. by replacing individual components. Such actions will immediately void the warranty.

#### **Conformal coating**

Certain applications employ a conformal coating of the PCB using HumiSeal® or other related coating products. These materials affect the RF properties of the GNSS module and it is important to prevent them from flowing into the module. The RF shields do not provide 100% protection for the module from coating liquids with low viscosity. Apply the coating carefully.



Conformal coating of the module will void the warranty.



#### **Casting**

If casting is required, use viscose or another type of silicon pottant. The OEM is strongly advised to qualify such processes in combination with the module before implementing this in the production.



Casting will void the warranty.

#### **Grounding metal covers**

Attempts to improve grounding by soldering ground cables, wick or other forms of metal strips directly onto the EMI covers is done at the customer's own risk. The numerous ground pins should be sufficient to provide optimum immunity to interferences and noise.

u-blox makes no warranty for damages to the module caused by soldering metal cables or any other forms of metal strips directly onto the EMI covers.

#### **Use of ultrasonic processes**

Some components on the module are sensitive to ultrasonic waves. Use of any ultrasonic processes (cleaning, welding etc.) may cause damage to the GNSS receiver.

u-blox offers no warranty against damages to the module caused by ultrasonic processes.

### <span id="page-85-0"></span>**5.3 Tapes**

[Figure](#page-85-1) 50 shows the feed direction and illustrates the orientation of the ZED-F9Hs on the tape:

<span id="page-85-1"></span>

#### **Figure 50: Orientation of ZED-F9H on the tape**

The feed direction to the pick and place pick-up is shown by the orientation of the pin 1 location. In [Figure](#page-85-1) 50, with pin 1 location on the bottom of the tape, the feed direction into the pick and place pick-up is from the reel (located on the right of the figure) towards left.

The dimensions of the tapes for ZED-F9H are specified in [Figure](#page-86-2) 51 (measurements in mm).



<span id="page-86-2"></span>

**Figure 51: ZED-F9H tape dimensions (mm)**

## <span id="page-86-0"></span>**5.4 Reels**

The ZED-F9H receivers are deliverable in quantities of 250 pieces on a reel.The receivers are shipped on reel type B, as specified in the u-blox Package Information Guide [\[3\]](#page-95-4).

## <span id="page-86-1"></span>**5.5 Moisture sensitivity levels**

The moisture sensitivity level (MSL) for ZED-F9H is specified in the table below.

| Package | MSL level |
|---------|-----------|
| LGA     | 4         |
|         |           |

**Table 27: MSL level**

For MSL standard see IPC/JEDEC J-STD-020, which can be downloaded from www.jedec.org.

For more information regarding moisture sensitivity levels, labeling, storage and drying, see the u-blox Package Information Guide [\[3\]](#page-95-4).



# <span id="page-87-0"></span>**Appendix**

## <span id="page-87-1"></span>**A Glossary**

| Abbreviation | Definition                                        |
|--------------|---------------------------------------------------|
| ANSI         | American National Standards Institute             |
| ARP          | Antenna reference point                           |
| BeiDou       | Chinese navigation satellite system               |
| BBR          | Battery-backed RAM                                |
| CDMA         | Code-division multiple access                     |
| EMC          | Electromagnetic compatibility                     |
| EMI          | Electromagnetic interference                      |
| EOS          | Electrical overstress                             |
| EPA          | Electrostatic protective area                     |
| ESD          | Electrostatic discharge                           |
| Galileo      | European navigation satellite system              |
| GLONASS      | Russian navigation satellite system               |
| GND          | Ground                                            |
| GNSS         | Global navigation satellite system                |
| GPS          | Global Positioning System                         |
| GSM          | Global System for Mobile Communications           |
| I2C          | Inter-integrated circuit bus                      |
| IEC          | International Electrotechnical Commission         |
| ITRF         | International Terrestrial Reference Frame         |
| MB           | Moving base                                       |
| MSM          | Multiple signal messages                          |
| NTRIP        | Networked Transport of RTCM via Internet Protocol |
| OSR          | Observation Space Representation                  |
| PCB          | Printed circuit board                             |
| QZSS         | Quasi-Zenith Satellite System                     |
| RF           | Radio frequency                                   |
| RTCM         | Radio Technical Commission for Maritime Services  |
| RTK          | Real-Time Kinematic                               |
| SBAS         | Satellite-based Augmentation System               |
| SV           | Space vehicle, a satellite                        |
| TDOP         | Time dilution of precision                        |
| UBX          | u-blox                                            |

## <span id="page-87-2"></span>**B RTK configuration procedures with u-center**

This section provides some guidance when using u-center to configure rover operation.

#### <span id="page-87-3"></span>**B.1 Rover configuration with u-center**

This overview will help when setting up a rover when using u-center.





In this procedure, the UART1 is set with an appropriate baud rate for communicating with a host. Then a set of output messages are set to enable receiver status monitoring.

Using the **UBX-CFG-VALSET** configuration window in the u-center **Message View**, set the UART1 interface for the correct host baud rate:

<span id="page-88-0"></span>**1.** Select **Group**: CFG-UART1, **Key name**: CFG-UART1-BAUDRATE. See [Figure](#page-88-0) 52.

| Compose list entry<br>Group<br>Key name | CFG-UART1<br>CFG-UART1-BAUDRATE | $\overline{\phantom{a}}$ |                          |          | Details:    |                                                         |  |
|-----------------------------------------|---------------------------------|--------------------------|--------------------------|----------|-------------|---------------------------------------------------------|--|
|                                         |                                 |                          |                          | Title    |             | The baud rate that should be configured on the<br>UART1 |  |
|                                         |                                 |                          | $\overline{\phantom{a}}$ |          | Description |                                                         |  |
| Key ID                                  | 40520001                        |                          | Add to List              | Type: U4 |             |                                                         |  |
|                                         | Configuration changes to send-  |                          |                          |          |             |                                                         |  |
| Key                                     |                                 |                          | Key ID                   | Type     | Value       |                                                         |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             | Remove                                                  |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |
|                                         |                                 |                          |                          |          |             | Remove all                                              |  |
|                                         |                                 |                          |                          |          |             |                                                         |  |

**Figure 52: u-center UBX-CFG-VALSET message view**

**2.** Select **Add to List**, it will appear in the table below.



**3.** Select the added **Key**. It will now give the option of setting or reading the current value. See [Figure](#page-89-0) 53.

<span id="page-89-0"></span>

|          | Compose list entry            |                      | Details<br>Title |             | The baud rate that should be configured on the | À.            |
|----------|-------------------------------|----------------------|------------------|-------------|------------------------------------------------|---------------|
| Group    | CFG-UART1                     | $\vert$              |                  |             | UART1                                          | $\sim$        |
| Key name | CFG-UART1-BAUDRATE            | $\blacktriangledown$ |                  | Description |                                                | A             |
| Key ID   | 40520001                      | Add to List          | Type: U4         |             |                                                |               |
|          | Configuration changes to send |                      |                  |             |                                                |               |
| Key      |                               | Key ID               | Type             | Value       |                                                |               |
|          | CFG-UART1-BAUDRATE            | 0x40520001           | ΪÜ4              |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                | Remove        |
|          |                               |                      |                  |             |                                                | Remove all    |
|          |                               |                      |                  |             |                                                |               |
| Value    |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             | Value hex                                      |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                |               |
|          |                               |                      |                  |             |                                                | Read receiver |
|          |                               |                      |                  |             |                                                |               |

**Figure 53: Example u-center UBX-CFG-VALSET message view when selecting a configuration item**

**4.** Next add the value, for example, 230400, into the **Value** window that appears below the list. See [Figure](#page-90-0) 54.



**5.** Then set the configuration by clicking the **Send** button at the bottom of the message tree view. Remember to set the u-center baud rate to match the value set in the receiver.

<span id="page-90-0"></span>

| Compose list entry<br>CFG-UART1<br>Group<br>ᅬ |                     | Details<br>Title | The baud rate that should be configured on the<br>UART1 | A.<br>÷             |
|-----------------------------------------------|---------------------|------------------|---------------------------------------------------------|---------------------|
| Key name<br>CFG-UART1-BAUDRATE                | $\vert \cdot \vert$ | Description      |                                                         | ۸                   |
| 40520001<br>Key ID                            | Add to List         | Type: U4         |                                                         | $\overline{\nabla}$ |
| Configuration changes to send                 |                     |                  |                                                         |                     |
| Key                                           | Key ID              | Type             | Value                                                   |                     |
|                                               |                     |                  |                                                         | Remove              |
|                                               |                     |                  |                                                         | Remove all          |
| Value                                         |                     |                  | Value hex                                               |                     |
| 230400                                        |                     |                  | 38400                                                   |                     |
|                                               |                     |                  |                                                         | Read receiver       |

**Figure 54: Rover: u-center UBX-CFG-VALSET message view for setting the CFG-UART1-BAUDRATE configuration item that controls the baudrate of UART1**

Next, some UBX example messages are configured to enable viewing the rover status.

- **1.** Select **Group** CFG-MSGOUT, **Key name**: CFG-MSGOUT-UBX and select the UART1 required messages.
- **2.** Add each message to the list, setting the value of each to 1.



#### <span id="page-91-1"></span>**3.** Click **Send**. See [Figure](#page-91-1) 55.

| Compose list entry<br>CFG-MSGOUT<br>Group<br>$\blacktriangledown$ |                          | Details<br>Title |                                       | Output rate of the UBX-NAV-SOL message on<br>port UART1 | $\hat{\rho}_{\rm{t}}$<br>v |
|-------------------------------------------------------------------|--------------------------|------------------|---------------------------------------|---------------------------------------------------------|----------------------------|
| Key name<br>CFG-MSGOUT-UBX_NAV_SOL_UART1                          | $\overline{\phantom{a}}$ |                  | Description                           |                                                         | $\wedge$                   |
| 20910002<br>Key ID                                                | Add to List              | Type: U1         |                                       |                                                         | $\backslash \mathcal{J}$   |
| Configuration changes to send-                                    |                          |                  |                                       |                                                         |                            |
| Key                                                               | Key ID                   | Type             | Value                                 |                                                         |                            |
| CFG-MSGOUT-UBX_NAV_SIG_UART1                                      | 0x20910346               | U1               | $\overline{\phantom{a}}$              |                                                         |                            |
| CFG-MSGOUT-UBX_NAV_PVT_UART1<br>CFG-MSGOUT-UBX NAV POSLLH UART1   | 0x20910007<br>0x2091002a | U1<br>U1         | ÷                                     |                                                         |                            |
| CFG-MSGOUT-UBX NAV RELPOSNED UART1                                | 0x2091008e               | U1               | $\mathcal{L}_{\mathcal{A}}$<br>$\sim$ |                                                         |                            |
| CFG-MSGOUT-UBX_NAV_STATUS_UART1                                   | 0x2091001b               | U1               | $\epsilon$                            |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       | Remove                                                  |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       | Remove all                                              |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
| Value                                                             |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |
|                                                                   |                          |                  |                                       | Read receiver                                           |                            |
|                                                                   |                          |                  |                                       |                                                         |                            |

**Figure 55: Rover: u-center UBX-CFG-VALSET message view for setting the CFG-MSGOUT-\* configuration items for enabling the output of some recommended UBX messages**

To ensure all the required RTCM messages, including most importantly RTCM 4072.0, are being received regularly, examine the **UBX-RXM-RTCM** output in u-center.

Once the rover has started to receive valid RTCM messages, it will transition through 3D Fix to 3D/ DGNSStoFloat and, ultimately, intoFixedmode.Thiswill occurwhen it is receiving all required RTCM messages, including RTCM 4072.0, under sufficient signal conditions.

The ZED-F9H will not output any position information in u-center or in any messages.

### <span id="page-91-0"></span>**C Stacked patch antenna**

A typical low-cost L1 + L2 antenna is based on a stacked patch antenna design. This consists of two discrete ceramic patch elements with an L1 patch above an L2 patch.





#### **Figure 56: Stacked patch antenna**

The absolute antenna position for a survey-grade antenna is normally given as the antenna reference point (ARP), usually specified at amechanicalmounting point.The antenna nominal phase center is given by a phase center combination of the L1 and L2 patches. Survey-grade antenna makers provide offset data for phase variation with respect to the ARP.



**Figure 57: Ceramic stack**

When used in an application, the antenna placement affects the phase center variation owing to the size and shape of the ground plane coupled with the effects of the adjacent structures. A phase center variation calibration is required to check the average phase center. A successful calibration can be made if the phase variation of a specific antenna is repeatable between samples.

To obtain the best antenna performance in an automotive application, mount the antenna in the center of a conductive car roof without any inclination. The antenna requires good signal levels and as wide a view of the sky as possible. The antenna must not be placed under a dashboard, in the rear view mirror, or on the rear parcel shelf.



An L1 + L2 stacked patch antenna must have a good band-pass performance from the patch elements with low attenuation from SAW band-pass filtering. An example of the measured frequency characteristics of a low-cost L1 + L2 antenna is shown below.



**Figure 58: Low-cost L1/L2 antenna band characteristics**

The u-blox low-cost antenna design is shown below, followed by some examples of antennas from other manufacturers which can be used with ZED-F9H.





**Figure 59: u-blox low-cost L1/L2 RTK antenna**

There are antenna types that can be used without a substantial ground plane, such as a helical antenna type. This is a useful solution where space is limited, for example, for drone or small form factor applications.



## <span id="page-95-0"></span>**Related documents**

- <span id="page-95-3"></span>**[1]** ZED-F9H-01B Data sheet, UBX-21025012
- <span id="page-95-2"></span>**[2]** HDG 1.13 Interface description, UBX-21025013
- <span id="page-95-4"></span>**[3]** Packaging information for u-blox chips, modules, and antennas, [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-95-1"></span>**[4]** ZED-F9P Moving Base application note, [UBX-19009093](https://www.u-blox.com/docs/UBX-19009093)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage [https://www.u-blox.com.](https://www.u-blox.com)



# <span id="page-96-0"></span>**Revision history**

| Revision | Date        | Name | Status / comments                                                                                                                                                                                                                                            |
|----------|-------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 24-Sep-2019 | ghun | HDG 1.12 and ZED-F9H-00B-01 release                                                                                                                                                                                                                          |
| R02      | 25-Feb-2020 | jhak | Updated minimum and maximum gains in Antenna specifications table.<br>Tape feed and dimension pictures updated. Added suggested footprint and<br>paste mask images. Improved sections Communications interfaces and<br>Security. Module type number updated. |
| R03      | 02-Jun-2020 | dama | HDG 1.13 update. ZED-F9H-01B-00 update.                                                                                                                                                                                                                      |
| R04      | 18-Jun-2021 | dama | Maintenance update.<br>Overall text improvement and typo corrections plus:                                                                                                                                                                                   |
|          |             |      | 3.1.7.1 platform settings updated, 3.2 SBAS section updated, 3.6.4<br>USB interface section updated, 3.9 MGA section updated, 4.7.2 Thermal<br>management added.                                                                                             |
| R05      | 18-Feb-2022 | dbhu | Maintenance update.<br>Overall text improvement and typo corrections plus:                                                                                                                                                                                   |
|          |             |      | 3.9 Multiple GNSS assistance (MGA) section update, 3.16 Spectrum<br>Analyzer section update and Related documents update.                                                                                                                                    |



## **Contact**

For complete contact information visit us at [www.u-blox.com.](https://www.u-blox.com)

#### **u-blox Offices**

#### **North, Central and South America Headquarters Asia, Australia, Pacific**

#### **Europe, Middle East, Africa**

|         | u-blox America, Inc. | u-blox AG |                  |         | u-blox Singapore Pte. Ltd. |
|---------|----------------------|-----------|------------------|---------|----------------------------|
| Phone:  | +1 703 483 3180      | Phone:    | +41 44 722 74 44 | Phone:  | +65 6734 3811              |
| E-mail: | info_us@u-blox.com   | E-mail:   | info@u-blox.com  | E-mail: | info_ap@u-blox.com         |
|         |                      |           |                  |         |                            |

| Support: | support@u-blox.com | Support: | support_ap@u-blox.com |
|----------|--------------------|----------|-----------------------|

|         | Regional Office West Coast |          | Regional Office Australia |
|---------|----------------------------|----------|---------------------------|
| Phone:  | +1 408 573 3640            | Phone:   | +61 3 9566 7255           |
| E-mail: | info_us@u-blox.com         | E-mail:  | info_anz@u-blox.com       |
|         |                            | Support: | support_ap@u-blox.com     |
|         |                            |          |                           |

|         | Technical Support     |          | Regional Office China (Beijing) |
|---------|-----------------------|----------|---------------------------------|
| Phone:  | +1 703 483 3185       | Phone:   | +86 10 68 133 545               |
| E-mail: | support_us@u-blox.com | E-mail:  | info_cn@u-blox.com              |
|         |                       | Support: | support_cn@u-blox.com           |

**Regional Office China (Chongqing)**

| Phone:   | +86 23 6815 1588      |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

| Regional Office China (Shanghai) |  |
|----------------------------------|--|
|----------------------------------|--|

| Phone:   | +86 21 6090 4832      |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

|  | Regional Office China (Shenzhen) |
|--|----------------------------------|
|  |                                  |

| Phone:   | +86 755 8627 1083     |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

#### **Regional Office India**

Phone: +91 80 4050 9200 E-mail: info\_in@u-blox.com Support: support\_in@u-blox.com

#### **Regional Office Japan (Osaka)**

Phone: +81 6 6941 3660 E-mail: info\_jp@u-blox.com Support: support\_jp@u-blox.com

**Regional Office Japan (Tokyo)**

Phone: +81 3 5775 3850

E-mail: info\_jp@u-blox.com Support: support\_jp@u-blox.com

**Regional Office Korea**

| Phone:   | +82 2 542 0861        |
|----------|-----------------------|
| E-mail:  | info_kr@u-blox.com    |
| Support: | support_kr@u-blox.com |

#### **Regional Office Taiwan**

| Phone:   | +886 2 2657 1090      |
|----------|-----------------------|
| E-mail:  | info_tw@u-blox.com    |
| Support: | support_tw@u-blox.com |