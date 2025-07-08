

# **NEO-F9P FW 1.00 HPG L1L5 1.40**

### **NEO-F9P**

**Release Note**



#### **Abstract**

This document contains general information, interface changes and firmware changes (features, improvements), along with known limitations for NEO-F9P FW 1.00 HPG L1L5 1.40.

**www.u-blox.com**



UBX-23007025 - R01 C1-Public



## **Document information**

| Title                  | NEO-F9P FW 1.00 HPG L1L5 1.40 |             |
|------------------------|-------------------------------|-------------|
| Subtitle               | NEO-F9P                       |             |
| Document type          | Release Note                  |             |
| Document number        | UBX-23007025                  |             |
| Revision and date      | R01                           | 15-Jun-2023 |
| Disclosure restriction | C1-Public                     |             |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2023, u-blox AG.



| 1 General<br>information4                                                           |  |
|-------------------------------------------------------------------------------------|--|
| 1.1 Scope4                                                                          |  |
| 1.2 Released firmware image4                                                        |  |
| 1.3 Related software 4                                                              |  |
| 1.4 Open-Source declaration 4                                                       |  |
| 1.5 Related documents4                                                              |  |
| 2 Firmware<br>description5                                                          |  |
| 2.1 Supported GNSS constellations and signals5<br>2.2 High precision GNSS features5 |  |
| 3 Message<br>interface7                                                             |  |
| 3.1 UBX7                                                                            |  |
| 3.2 NMEA7                                                                           |  |
| 3.3 RTCM 7                                                                          |  |
| 3.4 SPARTN 7                                                                        |  |
| 4 Known<br>limitations8                                                             |  |



# <span id="page-3-0"></span>**1 General information**

#### <span id="page-3-1"></span>**1.1 Scope**

This Release Note applies to NEO-F9P with Firmware 1.00 HPG L1L5 1.40.

#### <span id="page-3-2"></span>**1.2 Released firmware image**

| File             | UBX_F9_100_HPGL1L5_140_F9P.a953bd2d71061ed21cc6fdc431ab39a5.bin |
|------------------|-----------------------------------------------------------------|
| Firmware version | EXT CORE 1.00 (8d3640)                                          |
|                  | FWVER=HPGL1L5 1.40                                              |
| ROM base support | ROM 1.02 - ROM BASE 0x118B2060                                  |
|                  | ROM 1.01 - ROM BASE 0xDD3FE36C                                  |
|                  | ROM 0.40 - ROM BASE 0xCAAF619C                                  |

**Table 1: Released firmware image for u-blox NEO-F9P**

#### <span id="page-3-3"></span>**1.3 Related software**

Version 23.05 (or later) of u-center GNSS evaluation software is recommended for use with the released firmware. Please contact FAE if this version is not available on the official web site.

#### <span id="page-3-4"></span>**1.4 Open-Source declaration**

This u-blox positioning product described in this release note, comprising the company's proprietary software, does not contain open-source software to declare.

#### <span id="page-3-5"></span>**1.5 Related documents**

- **[1]** HPG L1L5 1.40 Interface description, UBX-23006991
- **[2]** NEO-F9P-15B Data sheet, UBX-22021920
- **[3]** NEO-F9P Integration manual, UBX-22028362
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage ([https://www.u-blox.com\)](https://www.u-blox.com).



# <span id="page-4-0"></span>**2 Firmware description**

This section highlights selected features supported by this firmware.

- The firmware image contains multi-band (L1/L5) RTK rover using all major GNSS constellations.
- The firmware image supports raw code and carrier phase measurement output for all supported GNSS signals.

#### <span id="page-4-1"></span>**2.1 Supported GNSS constellations and signals**

- GPS: L1C/A, L5
- GLONASS: L1OF
- Galileo: E1B/C, E5a
- BeiDou: B1I, B2a
- QZSS: L1C/A, L5
- NavIC: L5

All signals are enabled in the default configuration, except GPS L5 and NavIC L5.

#### <span id="page-4-2"></span>**2.2 High precision GNSS features**

- RTK rover receiver features:
  - High precision RTK fixed navigation using multi-band, multi-constellation GNSS
  - RTCM input support (details below), supporting Network RTK (VRS) and local base stations, e.g. another NEO-F9P or ZED-F9P module
  - SPARTN input support for GPS, GLONASS, Galileo and Beidou with fast reconvergence time
  - CLAS input support for QZSS
    - The CLAS augmentation service is broadcasted by a QZSS L6 signal which is not part of the frequency range covered by NEO-F9P. As such, NEO-F9P does not support receiving, demodulating and decoding of the QZSS L6 signal. This is supported by NEO-D9C which then must pass the correction stream to NEO-F9P in the form of UBX-RXM-QZSSL6 messages. This enables the NEO-F9P to directly use these messages and extract the compact SSR (cSSR) formatted corrections in order to use them directly without further processing or reformatting by an intermediary.
    - At the time of this release note, a CLAS solution with NEO-F9P augments GPS L1C/A L5, QZSS L1S, and Galileo E5a
  - SBAS
- RTK reference receiver features:
  - Fixed position mode and Survey-in mode
  - Output RTCM standard format
- Raw measurements:
  - Multi-band, multi-GNSS raw measurement data output (UBX-RXM-RAWX)
  - Navigation data subframe output (UBX-RXM-SFRBX)
- Support of active and passive antennas
- UBX messages on all interfaces
- Protection Level output to indicate level of trust in position output
- Secondary standard precision GNSS output in addition to RTK output
- Jamming detector with logging
- Embedded spectrum analyzer to visualize in-band noise sources



- Direct physical connection with L-band receiver
- Option to use GPS L5 signals



# <span id="page-6-0"></span>**3 Message interface**

The message interface is described in the NEO-F9P FW 1.00 HPG L1L5 1.40 Interface description, UBX-23006991. The released firmware supports UBX protocol version 27.40.

#### <span id="page-6-1"></span>**3.1 UBX**

The NEO-F9P relies exclusively on the configuration interface using the UBX-CFG-VALSET, UBX-CFG\_VALGET and UBX-CFG-VALDEL. Although some undocumented legacy UBX-CFG-\* messages are functional, users are strongly discouraged from using these deprecated messages.

The protocol is completely documented in the Interface description.

#### <span id="page-6-2"></span>**3.2 NMEA**

NEO-F9P FW 1.00 HPG L1L5 1.40 supports up to NMEA protocol version 4.11.

Five NMEA standards are supported. The default NMEA version is 4.11, and, alternatively, versions 4.10, 4.0, 2.3, and 2.1 can be enabled.

#### <span id="page-6-3"></span>**3.3 RTCM**

NEO-F9P FW 1.00 HPG L1L5 1.40 supports up to RTCM3 standard version 3.3.

#### <span id="page-6-4"></span>**3.4 SPARTN**

NEO-F9P FW 1.00 HPG L1L5 1.40 supports up to SPARTN protocol version 2.0.1.



# <span id="page-7-0"></span>**4 Known limitations**

- A receiver moving at very slow speed (less than 10 cm/s) does not update the heading information in UBX-NAV-PVT. The velocity vectors can be used reliably.
- Geofence status pin must not be re-assigned to another pin
- If the receiver is configured to output RTCM messages on several ports, the ports must have the same RTCM configuration, otherwise the MSM multiple message bit might not be set correctly
- Time pulse can only be synced to GNSS. Configuration items and relevant flag cannot be set to false (CFG-TP-SYNC\_GNSS\_TP1, UBX-CFG-TP5)