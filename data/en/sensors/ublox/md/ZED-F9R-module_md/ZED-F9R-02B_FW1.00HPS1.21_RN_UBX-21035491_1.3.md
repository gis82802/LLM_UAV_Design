

## **Release note**

**Topic ZED-F9R-02B with firmware FW1.00 HPS1.21**

UBX-21035491 C1-Public

**Author** Alex Ngi

**Date** 24 August 2021

> Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

#### Contents

| 1     | General information             | 1 |
|-------|---------------------------------|---|
| 1.1   | Scope                           | 1 |
| 1.2   | Released firmware image         | 1 |
| 1.3   | Related software                | 2 |
| 1.4   | Related documentation           | 2 |
| 2     | New features                    | 2 |
| 2.1   | SPARTN 1.8                      | 2 |
| 2.2   | E-scooter dynamic model         | 2 |
| 2.3   | Robotic lawnmower dynamic model | 3 |
| 3     | Message interface               | 3 |
| 3.1   | UBX protocol                    | 3 |
| 3.2   | NMEA protocol                   | 3 |
| 3.3   | New messages                    | 3 |
| 3.4   | Modified messages               | 4 |
| 3.5   | Removed messages                | 4 |
| 3.6   | Firmware changes                | 4 |
| 3.6.1 | Improvements                    | 4 |
| 3.6.2 | Firmware known limitations      | 5 |
| 3.6.3 | Hardware known limitations      | 5 |
| 4     | Revision history                | 5 |

# **1 General information**

The product with order code ZED-F9R-02B is delivered with the HPS1.21 firmware. This document is also applicable to other devices capable of running this firmware.

#### **1.1 Scope**

This release note covers the changes to the HPS 1.21 firmware compared to the HPS 1.20 firmware version. For a comprehensive list of changes with respect to earlier versions, this release note should be read in conjunction with the HPS 1.20 release notes [4].

#### **1.2 Released firmware image**

| Released firmware image |                                                         |
|-------------------------|---------------------------------------------------------|
| File                    | UBX_F9_100_HPS121. a1bca8df8b1e83c63fe957d8a644d3ac.bin |
|                         |                                                         |



| Firmware version | EXT CORE 1.00 (e2b374)<br>FWVER=HPS 1.21 |
|------------------|------------------------------------------|
| ROM base support | ROM 1.02 - ROM BASE 0x118B2060           |

# **1.3 Related software**

Version 21.05 (or later) of u-center GNSS evaluation software is recommended to be used with the released firmware. Please contact FAE if this version is not available on the official web site.

Version 19.03 (or later) of the firmware update tool supports this release.

## **1.4 Related documentation**

- [1] u-blox HPS 1.21 Interface description, [UBX-21019746](https://www.u-blox.com/en/docs/UBX-21019746)
- [2] u-blox ZED-F9R Integration Manual, [UBX-20039643](https://www.u-blox.com/en/docs/UBX-20039643)
- [3] u-blox ZED-F9R-02B Data Sheet, [UBX-21017486](https://www.u-blox.com/en/docs/UBX-21017486)
- [4] ZED-F9R-01B-HPS\_Release Note, [UBX-20057102](https://www.u-blox.com/en/docs/UBX-UBX-20057102)

## **2 New features**

## **2.1 SPARTN 1.8**

SPARTN, Safe Position Augmentation for Real-Time Navigation, is an open-standard format available at [https://www.spartnformat.org/.](https://www.spartnformat.org/)

A service provider using SPARTN-formatted corrections can enable high precision positioning applications with ZED-F9R. Compared to RTCM, which is used primarily for OSR, SPARTN has a complete set of messages suitable for SSR models without the use of vendor-specific messages. The use of SSR in the foundation allows services to be efficiently delivered over a broadcast medium such as L-band satellite signal or cellular networks. This allows a product to be deployed anywhere on the continent with a single service provider.

This release of SPARTN supports corrections for GPS and GLONASS and relies on a host library to decrypt the services, if necessary.

### **2.2 E-scooter dynamic model**

The dynamic model for an electric scooter often found in cities is available for the dead reckoning algorithm to improve the position accuracy in urban environments where GNSS signals are obstructed.

The purpose is to improve the accuracy in light urban environments to help police the user behavior to ensure compliance with local regulations in terms of operating in bike lanes and parking in designated areas. The E-scooter must be equipped with odometer readings and direction of travel information.

The model is tuned to the normal scooter operating behavior in terms of speed of travel, tilt, acceleration, and roll. The calibration speed of the IMU has been reduced to match the vehicle type.

Please consult the data sheet for additional information.

The default configuration is an automotive dynamic model.



# **2.3 Robotic lawnmower dynamic model**

The dynamic model for a robotic lawnmower is often used in commercial and residential settings. By incorporating high precision GNSS technology into robotic lawnmower designs, the machine can operate more efficiently than the early generation designs which can mostly randomly wander around an area. More complex areas can be handled as the mower builds an internal map of the area that has been cut. In many cases, the need for the boundary wire is eliminated, dramatically reducing installation costs. The dead reckoning algorithm improves the position accuracy in typical garden environments where GNSS signals are obstructed by homes, fences, bushes, and trees.

The model is tuned to the normal operating behavior of a lawn mower in terms of speed of travel, tilt, acceleration, and roll. The calibration of the IMU has been reduced to match the machine type and can start calibration at speed as low as 0.6 km per hour. The RLM dynamic model requires wheel ticks with polarity from both rear wheels. Automatic wheel tick polarity detection should not be used.

Please consult the data sheet for additional information.

The firmware default is an automotive dynamic model.

# **3 Message interface**

### **3.1 UBX protocol**

This firmware supports UBX protocol version 33.21.

### **3.2 NMEA protocol**

NMEA version 4.11 is the default instead of version 4.10 as it was in the in previous release.

#### **3.3 New messages**

| Message / Configuration item                                                                                             | Description / Comment                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPARTN-1X-OCB_GPS<br>SPARTN-1X-OCB_GLO<br>SPARTN-1X-HPAC_GPS<br>SPARTN-1X-HPAC_GLO<br>SPARTN-1X-GAD                      | SPARTN 1.8 input messages supported.                                                                                                                                       |
| CFG-I2CINPROT-SPARTN<br>CFG-SPIINPROT-SPARTN<br>CFG-UART1INPROT-SPARTN<br>CFG-UART2INPROT-SPARTN<br>CFG-USBINPROT-SPARTN | Enable/disable SPARTN protocol input support on all interfaces (default:<br>SPARTN input support enabled).                                                                 |
| UBX-RXM-SPARTN                                                                                                           | Message to report the SPARTN input status. Message output rate<br>configurable with new CFG-MSGOUT-UBX_RXM_SPARTN-* configuration<br>items.                                |
|                                                                                                                          | CFG-MSGOUT-UBX_RXM_SPARTN-* Enable UBX-RXM-SPARTN message as output across the different interfaces.                                                                       |
| UBX_NAV_PVAT                                                                                                             | Message output navigation and altitude position in a single message. Message<br>output rate is configurable with the new CFG-MSGOUT-UBX_NAV_PVAT_*<br>configuration items. |
| CFG-MSGOUT-UBX_NAV_PVAT_*                                                                                                | Enable UBX_NAV_PVAT message as output across the different interfaces.                                                                                                     |



| NMEA-GX-THS              | Support for NMEA-Standard-THS message. Message output rate is configured<br>with a new CFG-MSGOUT-NMEA_ID_THS_* configuration items.                                                        |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFG-MSGOUT-NMEA_ID_THS_* | Enables NMEA-Standard-THS message as output across the different<br>interfaces.                                                                                                             |
| CFG-TP-DRSTR_TP1         | Configuration to set TP1 drive strength (default 4mA).                                                                                                                                      |
| UBX-SEC-SIG              | Message to output state of signal security measures like jamming and<br>spoofing detection. Message output rate is configurable with a new CFG<br>MSGOUT-UBX_SEC_SIG_* configuration items. |
| CFG-MSGOUT-UBX_SEC_SIG_* | Enable UBX-SEC-SIG message as output across the different interfaces.                                                                                                                       |

## **3.4 Modified messages**

| Message / Configuration item | Description / Comment                                                                                                                  |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| CFG_NMEA_PROTVER             | Default is NMEA Version 4.11.                                                                                                          |
| CFG-NAVSPG-DYNMODEL          | Added two new dynamic models: robotic lawn mower (11) and<br>e-scooter model (12).                                                     |
| UBX-NAV-SIG                  | SPARTN correction source is reported rather than just<br>reserved.                                                                     |
| UBX-NAV-SAT                  | SPARTN correction source is reported rather than just<br>reserved.                                                                     |
| UBX-MON-COMMS                | SPARTN correction source is reported rather than just<br>reserved.                                                                     |
| CFG-BDS-USE_GEO_PRN          | Enable the use of BeiDou geostationary satellites (PRN 1-5<br>and 59-63). Previously, this configuration item had a different<br>name. |

## **3.5 Removed messages**

No messages were removed.

### **3.6 Firmware changes**

#### **3.6.1 Improvements**

- I2C robustness improvements.
- Accommodate systems with large wheel tick quantization. This supports low-cost sensors especially useful for applications with small wheels.
- Corrected use of almanac information of non-GPS systems.
- Corrected uninitialized values reported by UBX-ESF-ALG.
- Improved handling when not in RTK fix or float solutions under strong signals where tracking loop is wrong and results in larger measurement errors.
- Improved NMEA messages potentially exceeding length limits in strict configuration.
- Improved handling of Galileo satellites with high eccentric orbits.
- Improved performance handling of RTCM messages with millisecond-ambiguous corrections (RTCM MT 1001, 1003, 1009, 1011, MSM1 to MSM3).
- Corrected output of NMEA GxGSV message under some corner cases with untracked satellites.
- Corrected output of NMEA GxGRS message in version 4.11 regarding signal ID.
- General firmware improvements to reduce exceptions due to configuration changes



 Incorrect status information when SBAS/SLAS is disabled without restart. Entering backup mode.

#### **3.6.2 Firmware known limitations**

- After exiting a tunnel, solution stays in dead reckoning mode longer than expected.
- System signal configuration performed by CFG-SIGNAL-\* immediately after startup may be ignored until the next GNSS restart. Configuring to flash is a workaround.
- NMEA GxVLW and GxTHS messages in version 2.3 where information in version 4.0 is present.
- NMEA GxGRS and GxGNS messages may exceed the 82-character limit to 85 characters.

#### **3.6.3 Hardware known limitations**

- USB interface may not be possible to certify according to the USB standard.
- I2C has setup time issue when used with clock stretching and using fast mode is recommended.

# **4 Revision history**

| Revision | Date        | Name | Comments                      |
|----------|-------------|------|-------------------------------|
| R01      | 24-Aug-2021 | ANGI | First release of release note |