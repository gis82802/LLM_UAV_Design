

### **Release note**

**ZED-F9R-04B with firmware FW1.00HPS1.40**

UBXDOC-304424225-18286 C1-Public Alex Ngi

**Author**

**Date** 7 February 2025

Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

#### Contents

| 1     | General information                                                     | 1 |
|-------|-------------------------------------------------------------------------|---|
| 1.1   | Scope                                                                   | 1 |
| 1.2   | Released firmware image                                                 | 2 |
| 1.3   | Related software                                                        | 2 |
| 1.4   | Open-source declaration                                                 | 2 |
| 1.5   | Related documentation                                                   | 2 |
| 2     | New features                                                            | 2 |
| 2.1   | Rail and tram use case support                                          | 2 |
| 2.2   | SPARTN 2.0.2 with Beidou & QZSS                                         | 2 |
| 2.3   | Improved modelling for SPARTN services during high ionospheric activity | 3 |
| 2.4   | Lever arm support                                                       | 3 |
| 2.5   | Support of RTCM 3.4 corrections                                         | 3 |
| 2.6   | Conservative Ambiguity Resolution mode                                  | 3 |
| 2.7   | Filtering of vibration impacting IMU                                    | 3 |
| 3     | Message interface                                                       | 3 |
| 3.1   | UBX protocol                                                            | 3 |
| 3.2   | NMEA protocol                                                           | 3 |
| 3.3   | New messages                                                            | 3 |
| 3.4   | Modified messages                                                       | 4 |
| 3.5   | Removed messages                                                        | 4 |
| 3.6   | Firmware changes                                                        | 4 |
| 4     | Known limitations                                                       | 5 |
| 4.1.1 | Known firmware limitations                                              | 5 |
| 4.1.2 | Known hardware limitations                                              | 5 |
| 5     | Revision history                                                        | 5 |

# <span id="page-0-0"></span>**1 General information**

The product with order code ZED-F9R-04B is delivered with the HPS 1.40 firmware. This document is also applicable to other devices capable of running this firmware.

#### <span id="page-0-1"></span>**1.1 Scope**

This release note covers the changes to the HPS 1.40 firmware compared to the HPS 1.30 firmware version.



# <span id="page-1-0"></span>**1.2 Released firmware image**

| Released firmware image |                                                         |  |  |  |  |
|-------------------------|---------------------------------------------------------|--|--|--|--|
| File                    | UBX_F9R_100_HPS140.88460c971188f659adcd706f217e85b6.bin |  |  |  |  |
| Firmware version        | EXT CORE 1.00 (f8b901)<br>FWVER=HPS 1.40                |  |  |  |  |
| ROM base support        | ROM 1.02 - ROM BASE 0x118B2060                          |  |  |  |  |

# <span id="page-1-1"></span>**1.3 Related software**

Version 24.10 (or later) of u-center GNSS evaluation software is recommended to be used with the released firmware. Please contact FAE if this version is not available on the official web site.

Version 23.11 (or later) of the firmware update tool supports this release.

## <span id="page-1-2"></span>**1.4 Open-source declaration**

This u-blox positioning product described in this release note, comprising the company's proprietary software, does not contain open-source software to declare.

#### <span id="page-1-3"></span>**1.5 Related documentation**

- [1] u-blox HPS 1.40 Interface description, [UBXDOC-963802114-13138](https://www.u-blox.com/en/docs/UBXDOC-963802114-13138)
- [2] u-blox ZED-F9R Integration manual, [UBX-20039643](https://www.u-blox.com/en/docs/UBX-20039643)
- [3] u-blox ZED-F9R-04B Data sheet, [UBXDOC-963802114-12930](https://www.u-blox.com/en/docs/UBXDOC-963802114-12930)

# <span id="page-1-4"></span>**2 New features**

When migrating from the previous version of the product, users are advised to perform retesting in their system.

### <span id="page-1-5"></span>**2.1 Rail and tram use case support**

Vehicle behaving as rail vehicle and trams can calibrate the inertial navigation system for applications requiring a meter level of accuracy. The system must provide a wheel tick and direction signal and must be manually aligned in the vehicle. The tolerance of the mounting alignment may be set to high or low using CFG-SFIMU-IMU\_MNTALG\_TOLERANCE. This provides a tradeoff between faster sensor fusion calibration times versus the effort required to properly mount the system.

Compared to a system using only a GNSS receiver, this solution improves the availability of the position even when the sky view is completely obstructed. Furthermore, the system can output the heading and attitude even where it is at standstill.

#### <span id="page-1-6"></span>**2.2 SPARTN 2.0.2 with Beidou & QZSS**

Secure Position Augmentation for Real Time Navigation (SPARTN) is an open standard format available at [https://www.spartnformat.org/.](https://www.spartnformat.org/)

In addition to GPS, GLONASS and Galileo, this SPARTN release also supports corrections for BDS and QZSS.



# <span id="page-2-0"></span>**2.3 Improved modelling for SPARTN services during high ionospheric activity**

This firmware includes improvements in the ambiguity resolution algorithms that provide increased robustness and reliability during periods of high solar activity while using SPARTN correction services. This implementation is equivalent to the algorithms found in ZED-F9P-05B with the HPS1.51 firmware.

## <span id="page-2-1"></span>**2.4 Lever arm support**

In systems where the level of accuracy is comparable to the offsets between the various reference points like GNSS antenna phase center, IMU reference frame, middle of the vehicle rear axle, these offsets need to be specified generally referred to as lever arms. In previous releases of the product, the lever arms were confidential messages reserved for advanced users. These messages are now publicly available to user and supported by u-center.

## <span id="page-2-2"></span>**2.5 Support of RTCM 3.4 corrections**

When operating in the RTK mode with RTCM corrections, this firmware now supports RTCM version 3.4 messages.

## <span id="page-2-3"></span>**2.6 Conservative Ambiguity Resolution mode**

This firmware includes a new option that can be selected via CFG-NAVHPG-DGNSSMODE, value 5 (RTK\_CAR), for a Conservative Ambiguity Resolution approach. When enabled, the occurrence of false RTK fixes is reduced, especially within challenging environments where disturbances such as multipath may be present. Please note that, depending on conditions, the time to ambiguity fix may be longer when the conservative mode is in use.

By default, this option is disabled. The firmware starts up with the default value 3 (RTK\_FIXED)

# <span id="page-2-4"></span>**2.7 Filtering of vibration impacting IMU**

In systems where there is strong undamped mechanical vibration affecting the quality of IMU data sufficient to impact sensor fusion performance, an optional digit filter is available to partially mitigate the issue. The presence of this kind of vibration can be confirmed by observing the level of noise reported by the UBX-ESF-STATUS message. By default, the filter is disabled. The filter is enabled by setting CFG-MOT-IMU\_FILT\_WINDOW to a non-zero value. For typical applications, 100 [ms] is suitable.

# <span id="page-2-5"></span>**3 Message interface**

### <span id="page-2-6"></span>**3.1 UBX protocol**

This firmware supports UBX protocol version 33.40.

#### <span id="page-2-7"></span>**3.2 NMEA protocol**

NMEA version 4.11 is the default and is unchanged.

#### <span id="page-2-8"></span>**3.3 New messages**

| Message / Configuration item | Description / Comment                                    |
|------------------------------|----------------------------------------------------------|
| SPARTN-1X-OCB_BDS            | Support for additional SPARTN input messages (BDS, QZSS) |



| SPARTN-1X-OCB_QZSS<br>SPARTN-1X-HPAC_BDS<br>SPARTN-1X-HPAC_QZSS               |                                                                                                                                                            |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UBX-ESF-RESETALG                                                              | Resets the automatic IMU-mount alignment.                                                                                                                  |
| CFG-SFCORE-IMU2CRP_LA_X<br>CFG-SFCORE-IMU2CRP_LA_Y<br>CFG-SFCORE-IMU2CRP_LA_Z | Configure IMU-to-CRP lever arms.                                                                                                                           |
| CFG-SFIMU-IMU2ANT_LA_X<br>CFG-SFIMU-IMU2ANT_LA_Y<br>CFG-SFIMU-IMU2ANT_LA_Z    | Configure IMU-to-Antenna lever arms.                                                                                                                       |
| CFG-SFIMU<br>IMU_MNTALG_TOLERANCE                                             | Set the tolerance of user-configured IMU-mount alignment angles. The<br>default is LOW tolerance (value 0), meaning the configured angles are<br>accurate. |
| CFG-SFODO-IMU2VRP_LA_X<br>CFG-SFODO-IMU2VRP_LA_Y<br>CFG-SFODO-IMU2VRP_LA_Z    | Configure IMU-to-VRP lever arms for wheel tick or speed information input.                                                                                 |
| CFG-HW-ANT_ON_SHORT_US                                                        | Delay in microseconds between turning the antenna power supply on and<br>enabling the antenna short circuit detection.                                     |
| CFG-SEC-SPOOFDET_SIM_SIG_DIS                                                  | Disable spoofing detection of simulated signals. The default is 0 (i.e. spoofing<br>detection is enabled).                                                 |
| CFG-MOT-IMU_FILT_WINDOW                                                       | Enable filtering of . The default is 0 (disabled)                                                                                                          |

## <span id="page-3-0"></span>**3.4 Modified messages**

| Message / Configuration item      | Description / Comment                                                                     |  |
|-----------------------------------|-------------------------------------------------------------------------------------------|--|
| UBX-MON-COMMS                     | New bitfield "outputPort" now reports the port from which this message was<br>output from |  |
| UBX-MON-RF                        | Now compatible with u-center.                                                             |  |
| CFG-NAVHPG-DGNSSMODE              | Value 5 is new for RTK_CAR                                                                |  |
| CFG-NAVSPG-DYNMODEL               | New option RAIL (value 13), for trains and trams dynamic model                            |  |
| CFG-NAVSPG-WKNROLLOVER            | New default value: 2349                                                                   |  |
| CFG-SBAS-PRNSCANMASK              | New default value: 0x000000000003ab88                                                     |  |
| CFG-SBAS<br>ACCEPT_NOT_IN_PRNMASK | Renamed existing configuration item CFG-SBAS<br>IGN_HEALTH_FROM_PRNMASK                   |  |

#### <span id="page-3-1"></span>**3.5 Removed messages**

**Message / Configuration item Description / Comment**

# <span id="page-3-2"></span>**3.6 Firmware changes**

- Low-level system errors were corrected to output in all ports
- SPARTN keys now switch to the next one even if the "valid from ToW" (i.e. start of the week) value is zero
- Corrected an issue where PointPerfect keys incorrectly switched when the server sent messages with GLONASS timetags. This caused the key switch to happen 3 hours too early



when the PointPerfect service sent a stream with GLONASS messages. Consequently, there was a 3-hour period during which the decrypted messages were invalid.

- Corrected some NMEA messages with a missing talker ID.
- Corrected the content of UBX-MON-RF messages to be compatible with u-center.

# <span id="page-4-0"></span>**4 Known limitations**

#### <span id="page-4-1"></span>**4.1.1 Known firmware limitations**

- The system signal configuration performed by CFG-SIGNAL-\* immediately after startup may be ignored until the next GNSS restart. Configuring to flash is a workaround.
- NMEA GxGRS and GxGNS messages may exceed the 82-character limit to 85 characters.
- Signal configuration may be ignored if sent immediately after startup.
- NMEA GNGNS posMode field reports the same status for all GNSSs, not per GNSS.

#### <span id="page-4-2"></span>**4.1.2 Known hardware limitations**

- It may not be possible to certify the USB interface according to the USB standard.
- The I2C has an issue with the setup time when used with clock stretching. It is recommended to use the fast mode.

### <span id="page-4-3"></span>**5 Revision history**

| Revision | Date       | Name | Comments                      |
|----------|------------|------|-------------------------------|
| R01      | 7-Feb-2025 | ANGI | First release of release note |
|          |            |      |                               |