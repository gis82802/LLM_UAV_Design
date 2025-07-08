

### **Release Notes LAP 1.30**

**Author Date Topic Firmware FW1.00 LAP1.30 for ZED-F9K and F9940-KA-DR** UBX-22009742 Martin Wallebohr 15 May 2023

> Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

#### **Contents**

| 1      | General Information                                  | 2 |
|--------|------------------------------------------------------|---|
| 1.1    | Scope                                                | 2 |
| 1.2    | Related documentation                                | 2 |
| 2      | Software releases                                    | 3 |
| 2.1    | u-blox F9 firmware Images                            | 3 |
| 2.2    | u-center                                             | 3 |
| 2.3    | Firmware update tool                                 | 3 |
| 3      | Message Interfaces                                   | 3 |
| 3.1    | UBX protocol                                         | 3 |
| 3.1.1  | New messages                                         | 3 |
| 3.1.2  | Modified messages                                    | 5 |
| 3.1.3  | Deprecated messages                                  | 6 |
| 3.1.4  | Removed messages                                     | 6 |
| 3.2    | Configuration interface                              | 7 |
| 3.3    | NMEA protocol                                        | 7 |
| 3.4    | RTCM                                                 | 7 |
| 3.5    | SPARTN                                               | 7 |
| 4      | New features                                         | 7 |
| 4.1.1  | Secondary position output                            | 7 |
| 4.1.2  | Improved accuracy and update rate                    | 7 |
| 4.1.3  | Advanced spoofing detection                          | 7 |
| 4.1.4  | GNSS band selection                                  | 8 |
| 4.1.5  | Protection Level for band option A (L1/L2/E5b)       | 8 |
| 4.1.6  | SPARTN 2.0.1 support                                 | 8 |
| 4.1.7  | 100Hz low latency IMU raw data                       | 8 |
| 4.1.8  | Wake-on-motion (modules only)                        | 8 |
| 4.1.9  | ADR w/o directional information                      | 8 |
| 4.1.10 | Better navigation output debugging with UBX-NAV-PVAT | 8 |
| 4.1.11 | Advanced calibration handling                        | 8 |
| 4.1.12 | Jamming detection algorithms                         | 9 |
| 4.2    | Removed features                                     | 9 |
| 4.2.1  | QZSS L1S support                                     | 9 |
| 4.2.2  | Magnetic Declination output                          | 9 |



| Odometer feature         | 9  |
|--------------------------|----|
| Geofence feature         | 9  |
| Supported sensor drivers | 9  |
| Support and questions    | 9  |
| Limitations              | 9  |
| Further notes            | 10 |
| Open Source Software     | 10 |
| Revision History         | 10 |
|                          |    |

# <span id="page-1-0"></span>**1 General Information**

This release note describes the u-blox F9 firmware LAP 1.30, designed to run on the following products:

- Modules: ZED-F9K
- Chipset: UBX-F9940-KA-C1003A

### <span id="page-1-1"></span>**1.1 Scope**

This release note covers the changes to the LAP 1.30 firmware compared to the LAP 1.20 firmware version. For a comprehensive list of changes with respect to earlier versions, this release note should be read in conjunction with the LAP 1.20 release notes [12].

### <span id="page-1-2"></span>**1.2 Related documentation**

- [1] LAP 1.30 Interface description, UBX-22005157
- [2] ZED-F9K integration manual, UBX-20046189
- [3] ZED-F9K-00B Data sheet, UBX-17061422
- [4] ZED-F9K-01A Data sheet, UBX-21045820
- [5] LAP 1.30 Interface description, UBX-22005159, C2-Restricted
- [6] UBX-F9940-KA-DR Integration Manual, UBX- 19028876 C2-restricted
- [7] UBX-F9940-KA-DR Data Sheet UBX- 19028878, C2-restricted
- [8] Firmware-Update-Tool-v22.12 ReleaseNotes\_R01, UBX-22039023 C2-restricted
- [9] Service-description: [https://developer.thingstream.io/guides/location-services/pointperfect](https://developer.thingstream.io/guides/location-services/pointperfect-service-description)[service-description](https://developer.thingstream.io/guides/location-services/pointperfect-service-description)
- [10] Getting-started-guide: [https://developer.thingstream.io/guides/location](https://developer.thingstream.io/guides/location-services/pointperfect-getting-started)[services/pointperfect-getting-started](https://developer.thingstream.io/guides/location-services/pointperfect-getting-started)
- [11] Zero-touch-provisioning: [https://developer.thingstream.io/guides/location](https://developer.thingstream.io/guides/location-services/pointperfect-zero-touch-provisioning)[services/pointperfect-zero-touch-provisioning](https://developer.thingstream.io/guides/location-services/pointperfect-zero-touch-provisioning)
- [12] LAP 1.20 Release Notes, UBX-20033290



# <span id="page-2-0"></span>**2 Software releases**

### <span id="page-2-1"></span>**2.1 u-blox F9 firmware Images**

| 1st released firmware image | Audience                                                 |
|-----------------------------|----------------------------------------------------------|
| File                        | JUJU_ROX_100_LAP130.9681faa29bb4f243289dd04c9efa9efe.bin |
| Firmware Version            | EXT CORE 1.00 (71c984)<br>FWVER=LAPL1L2L5 1.30           |
| ROM base support            | ROM 1.02 - ROM BASE 0x118B2060                           |

### <span id="page-2-2"></span>**2.2 u-center**

The u-center version 22.07 (or later) should be used together with this released product.

#### <span id="page-2-3"></span>**2.3 Firmware update tool**

u-blox recommends using firmware update tool software version 22.12 (or later) with the released product. Please see release notes of firmware update tool for details [8].

## <span id="page-2-4"></span>**3 Message Interfaces**

### <span id="page-2-5"></span>**3.1 UBX protocol**

This firmware supports UBX protocol version 30.30.

#### <span id="page-2-6"></span>**3.1.1 New messages**

| Message / Configuration item                                                                                        |     | Audience Description / Comment                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NMEA-NAV2-GGA<br>NMEA-NAV2-GLL<br>NMEA-NAV2-GNS<br>NMEA-NAV2-GSA<br>NMEA-NAV2-RMC<br>NMEA-NAV2-VTG<br>NMEA-NAV2-ZDA | PUB | Support for NMEA messages on the secondary output.<br>Message output rate configurable with configuration items in<br>the format of CFG-MSGOUT-NMEA_NAV2_ID_XXX_* where<br>XXX denotes the NMEA message type e.g., GGA, ZDA etc                |
| UBX-MGA-SF                                                                                                          | PUB | Support for aiding messages for sensor fusion calibration and<br>temperature compensation                                                                                                                                                      |
| UBX-MGA-INI-ATT                                                                                                     | PUB | Support for a new message to supply attitude aiding (input<br>only)                                                                                                                                                                            |
| UBX-MON-SYS                                                                                                         | PUB | Support for a new message UBX-MON-SYS which outputs<br>system performance information. Message output rate<br>configurable with new CFG-MSGOUT-UBX_MON_SYS_*<br>configuration items                                                            |
| UBX-NAV-PL                                                                                                          | PUB | Support for a new messages UBX-NAV-PL which outputs the<br>protection level                                                                                                                                                                    |
| UBX-NAV-PVAT                                                                                                        | PUB | Support for a new message UBX-NAV-PVAT which outputs<br>position, velocity, and time information along with heading<br>and altitude information. Message output rate configurable<br>with new CFG-MSGOUT-UBX_NAV_PVAT_* configuration<br>items |
| UBX-NAV-TIMEQZSS                                                                                                    | PUB | Support for new messages which output information about<br>QZSS time in primary and secondary output respectively.                                                                                                                             |



|                                                                                                                                                                                                                                                                                                                                                                          |     | Message output rate configurable with CFG-MSGOUT<br>UBX_NAV_TIMEQZSS_* and CFG-MSGOUT<br>UBX_NAV2_TIMEQZSS_* configuration items respectively                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UBX-SEC-SIG                                                                                                                                                                                                                                                                                                                                                              | PUB | Support for a new message to output state of signal security<br>measures like jamming and spoofing detection. Message<br>output rate is configuration with a new CFG-MSGOUT<br>UBX_SEC_SIG_* configuration items           |
| UBX-SEC-SIGLOG                                                                                                                                                                                                                                                                                                                                                           | PUB | Support for new message to output a log of detected<br>jamming/spoofing events. Message output rate is<br>configuration with a new CFG-MSGOUT-UBX_SEC_SIGLOG_*<br>configuration items                                      |
| UBX-NAV2-CLOCK<br>UBX-NAV2-COV<br>UBX-NAV2-DOP<br>UBX-NAV2-EELL<br>UBX-NAV2-EOE<br>UBX-NAV2-POSECEF<br>UBX-NAV2-POSLLH<br>UBX-NAV2-PVT<br>UBX-NAV2-SAT<br>UBX-NAV2-SBAS<br>UBX-NAV2-SIG<br>UBX-NAV2-STATUS<br>UBX-NAV2-TIMEBDS<br>UBX-NAV2-TIMEGAL<br>UBX-NAV2-TIMEGLO<br>UBX-NAV2-TIMEGPS<br>UBX-NAV2-TIMELS<br>UBX-NAV2-TIMEUTC<br>UBX-NAV2-VELECEF<br>UBX-NAV2-VELNED | PUB | Support for new UBX messages to output navigation<br>information for secondary output. Each message output rate<br>is configurable with a new configuration item in the form of<br>UBX-MSGOUT_UBX_NAV2_CLOCK_* for example |
| CFG-NAV2-OUT_ENABLED                                                                                                                                                                                                                                                                                                                                                     | PUB | Configuration to enable secondary navigation output                                                                                                                                                                        |
| CFG-NAV2-SBAS_USE_INTEGRITY                                                                                                                                                                                                                                                                                                                                              | PUB | Configuration to enable use of SBAS integrity flag in<br>secondary navigation output                                                                                                                                       |
| CFG-HW-SENS_WOM_MODE                                                                                                                                                                                                                                                                                                                                                     | PUB | Configuration to set the WoM mode of operation                                                                                                                                                                             |
| CFG-HW-SENS_WOM_THLD                                                                                                                                                                                                                                                                                                                                                     | PUB | Configuration to set the acceleration threshold which when<br>reached would wake up the IMU sensor                                                                                                                         |
| CFG-SFODO-DIS_DIR_INFO                                                                                                                                                                                                                                                                                                                                                   | PUB | Configuration to disable the use of WT directional information                                                                                                                                                             |
| CFG-TP-DRSTR_TP1                                                                                                                                                                                                                                                                                                                                                         | PUB | Configuration to set TP1 drive strength (default 4mA)                                                                                                                                                                      |
| CFG-SFIMU-IMU_EN                                                                                                                                                                                                                                                                                                                                                         | PUB | Enable the use of internal IMUs/ IMUs connected on I2C pins                                                                                                                                                                |
| UBX-CFG-VALDEL                                                                                                                                                                                                                                                                                                                                                           | PUB | Part of the new configuration interface                                                                                                                                                                                    |
| UBX-CFG-VALGET                                                                                                                                                                                                                                                                                                                                                           | PUB | Part of the new configuration interface                                                                                                                                                                                    |
| UBX-CFG-VALSET                                                                                                                                                                                                                                                                                                                                                           | PUB | Part of the new configuration interface                                                                                                                                                                                    |
| UBX-SEC-SESSID                                                                                                                                                                                                                                                                                                                                                           | PUB | Session ID for message authentication when locking<br>configuration                                                                                                                                                        |
| UBX-RXM-PMP                                                                                                                                                                                                                                                                                                                                                              | PUB | Point to Multipoint (LBAND) input message                                                                                                                                                                                  |
| UBX-RXM-SPARTN                                                                                                                                                                                                                                                                                                                                                           | PUB | This message shows info on a received SPARTN input<br>message                                                                                                                                                              |
| UBX-RXM-SPARTNKEY                                                                                                                                                                                                                                                                                                                                                        | PUB | Depending on the number of active keys, the receiver shall<br>send a UBX-RXM-SPARTNKEY message describing the keys                                                                                                         |



| CFG-I2CINPROT-SPARTN                                                                                                                           | PUB | Flag to indicate if SPARTN should be an input protocol on I2C                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|
| CFG-NAVSPG-PL_ENA                                                                                                                              | PUB | Enable protection level                                                                                                                       |
| CFG-SBAS-USE_IONOONLY                                                                                                                          | PUB | New config item use SBAS ionosphere correction only                                                                                           |
| CFG-SEC-JAMDET_SENSITIVITY_HI                                                                                                                  | PUB | New config item for security features. When set, go for a more<br>sensitive jamming detection (at the cost of increased false<br>alarm rate). |
| CFG-SIGNAL-BDS_B2A_ENA                                                                                                                         | PUB | New config item for BeiDou B2a                                                                                                                |
| CFG-SIGNAL-GAL_E5A_ENA                                                                                                                         | PUB | New config item for Galileo E5A                                                                                                               |
| CFG-SIGNAL-GPS_L5_ENA                                                                                                                          | PUB | New config item for GPS L5                                                                                                                    |
| CFG-SIGNAL-QZSS_L5_ENA                                                                                                                         | PUB | New config item for QZSS L5                                                                                                                   |
| CFG-SPARTN-USE_SOURCE                                                                                                                          | PUB | Select source for SPARTN stream                                                                                                               |
| CFG-SPIINPROT-SPARTN                                                                                                                           | PUB | Config item for SPARTN over SPI                                                                                                               |
| CFG-UART1INPROT-SPARTN                                                                                                                         | PUB | Config item for SPARTN over UART1                                                                                                             |
| CFG-UART2INPROT-SPARTN                                                                                                                         | PUB | Config item for SPARTN over UART2                                                                                                             |
| CFG-USBINPROT-SPARTN                                                                                                                           | PUB | Config item for SPARTN over USB                                                                                                               |
| SPARTN-1X-OCB_GPS<br>SPARTN-1X-OCB_GLO<br>SPARTN-1X-HPAC_GPS<br>SPARTN-1X-HPAC_GLO<br>SPARTN-1X-GAD<br>SPARTN-1X-OCB_GAL<br>SPARTN-1X-HPAC_GAL | PUB | SPARTN input messages support                                                                                                                 |
| UBX-RXM-COR                                                                                                                                    | PUB | Message to output differential corrections input status                                                                                       |
| CFG-SBAS-ACCEPT_NOT_IN_PRNMASK                                                                                                                 | PUB | Accept corrections from SBAS SV                                                                                                               |

#### <span id="page-4-0"></span>**3.1.2 Modified messages**

| Message / Configuration item | Audience | Description / Comment                                                                                                                 |
|------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------|
| CFG-NMEA-PROTVER             | PUB      | New default value: NMEA protocol version 4.11 configured by<br>default                                                                |
|                              |          | Previous default value: NMEA protocol version 4.10                                                                                    |
| CFG-BDS-USE_GEO_PRN          | PUB      | Configuration item name changed from CFG-BDS<br>USE_PRN_1_TO_5 to CFG-BDSUSE_<br>GEO_PRN. Configuration item key ID remains the same. |
| CFG-SBAS-PRNSCANMASK         | PUB      | SBAS search mask changed from 0x0000000000072bc8 to<br>0x0000000000072b88                                                             |
| CFG-SFIMU-ACCEL_ACCURACY     | PUB      | Default accelerometer accuracy changed from 0 to 1000                                                                                 |
| CFG-SFIMU-GYRO_ACCURACY      | PUB      | Default gyroscope accuracy changed from 0 to 100                                                                                      |
| NMEA-Standard-GAQ            | PUB      | It is now possible to poll a standard message if the current<br>Talker ID is GA.                                                      |
| NMEA-Standard-DTM            | PUB      | The message now supports the display of PZ90 datum (as<br>P90).                                                                       |
| NMEA-Standard-GST            | PUB      | Support the output of the error ellipse as defined by its semi<br>major and semi-minor axis as well as its orientation.               |
| NMEA-Standard-GSV            | PUB      | Various implementation errors fixed, e.g. null fields, range of<br>azimuth angle [0359], etc.                                         |



| NMEA-Standard-GRS | PUB | Various implementation errors fixed, e.g., null fields, residual<br>ordering.                                 |
|-------------------|-----|---------------------------------------------------------------------------------------------------------------|
| UBX-TIM-TP        | PUB | Added "qErrInvalid" flag to indicate when quantization error is<br>not provided                               |
| UBX-MON-COMMS     | PUB | Reports new SPARTN message                                                                                    |
| UBX-MON-RF        | PUB | Jamming state has been dropped from this message. See the<br>new UBX-SEC-SIG message for jamming information. |
| UBX-NAV-PVT       | PUB | Reports the approximate age of the most recently received<br>differential correction                          |
| UBX-NAV-SBAS      | PUB | Now it reports a flag to indicate if Integrity information is<br>being used                                   |
| UBX-NAV-SIG       | PUB | SPARTN correction source is now reported                                                                      |
| UBX-NAV-SAT       | PUB | SPARTN correction source is now reported                                                                      |

#### <span id="page-5-0"></span>**3.1.3 Deprecated messages**

| Message       | Audience | Description / Comment                           |
|---------------|----------|-------------------------------------------------|
| UBX-CFG-ANT   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-DAT   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-DGNSS | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-INF   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-ITFM  | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-MSG   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-NAV5  | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-NAVX5 | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-NMEA  | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-ODO   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-PRT   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-RATE  | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-RINV  | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-SBAS  | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-TP5   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-CFG-USB   | PUB      | Use UBX-CFG-VAL[SET DEL GET] instead 1          |
| UBX-MON-HW    | PUB      | Use UBX-MON-HW3 and UBX-MON-RF as a replacement |
| UBX-MON-HW2   | PUB      | Use UBX-MON-HW3 and UBX-MON-RF as a replacement |

#### <span id="page-5-1"></span>**3.1.4 Removed messages**

| Message      | Audience | Description / Comment                                                                                          |
|--------------|----------|----------------------------------------------------------------------------------------------------------------|
| NMEA-ID-VLW  | PUB      | Odometer feature has been removed                                                                              |
| UBX-CFG-ESFA | PUB      | Legacy configuration messages that were dropped, please<br>refer to the interface description document for the |

<sup>1</sup> See Legacy UBX message field reference in the Interface description.



| UBX-CFG-ESFALG<br>UBX-CFG-ESFG<br>UBX-CFG-ESFWT<br>UBX-CFG-GEOFENCE<br>UBX-CFG-GNSS<br>UBX-CFG-PWR<br>UBX-CFG-SENIF |     | recommended configuration items to use in the new<br>configuration concept. |
|---------------------------------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------|
| UBX-NAV-GEOFENCE                                                                                                    | PUB | Geofence feature is not available in this release                           |
| UBX-NAV-ODO                                                                                                         | PUB | Odometer feature is not available in this release                           |
| UBX-NAV-ODORESET                                                                                                    | PUB | Odometer feature is not available in this release                           |
| UBX-NAV-SLAS                                                                                                        | PUB | QZSS L1S feature is not available in this release                           |

### <span id="page-6-0"></span>**3.2 Configuration interface**

u-blox F9 introduces a new configuration mechanism compared to u-blox M8, based on UBX-CFG-VALSET, UBX-CFG-VALDEL and UBX-CFG-VALGET. Refer to the Interface description [1] for a description of this feature and the available settings.

## <span id="page-6-1"></span>**3.3 NMEA protocol**

This firmware adds support for NMEA version 4.11. Five NMEA standards are supported. The default NMEA version is 4.11, and, alternatively, versions 4.10, 4.0, 2.3, and 2.1 can be enabled.

# <span id="page-6-2"></span>**3.4 RTCM**

LAP 1.30 firmware supports up to RTCM3 standard version 3.3

### <span id="page-6-3"></span>**3.5 SPARTN**

LAP 1.30 firmware supports up to SPARTN protocol version 2.0.1.

# <span id="page-6-4"></span>**4 New features**

#### <span id="page-6-5"></span>**4.1.1 Secondary position output**

In addition to sensor fused position solution, a second output delivers an independent GNSSonly based positioning solution. Secondary output is disabled by default. It can be enabled using the configuration item CFG-NAV2-OUT\_ENABLED. When enabled, the primary filter is configured for sensor fusion, and the secondary filter as GNSS-only.

### <span id="page-6-6"></span>**4.1.2 Improved accuracy and update rate**

Main position output is improved in terms of accuracy and update rate which can be configured up to 50Hz using priority navigation mode.

#### <span id="page-6-7"></span>**4.1.3 Advanced spoofing detection**

This firmware includes advanced algorithms (e.g., sensor-based) to identify spoofing attacks which are then reported via new message class UBX-SEC. For details, please see integration manual [2] and interface description [1].



## <span id="page-7-0"></span>**4.1.4 GNSS band selection**

This firmware can switch between band u-blox band option A (L1/L2/E5b) and band option B (L1/L5) by configuration of the respective GNSS signals via UBX commands. Please note that the corresponding RF frontend needs to support above bands options as well. For more details, please see integration manual.

### <span id="page-7-1"></span>**4.1.5 Protection Level for band option A (L1/L2/E5b)**

Protection level output for accuracy with 95% confidence level. For details, please see integration manual [2].

### <span id="page-7-2"></span>**4.1.6 SPARTN 2.0.1 support**

This firmware supports SPARTN 2.0.1 formatted corrections (e.g., from u-blox PointPerfect correction service). SPARTN, Safe Position Augmentation for Real-Time Navigation, is an open standard format available at [https://www.spartnformat.org/.](https://www.spartnformat.org/)

This firmware supports as well SPARTN corrections as broadcasted by L-band satellites. Receiving SPARTN correction stream in this way requires a NEO-D9S module which must pass the corrections over to the receiver in the form of UBX-RXM-PMP messages.

This firmware supports on-device decryption of encrypted PointPerfect SPARTN correction streams.

### <span id="page-7-3"></span>**4.1.7 100Hz low latency IMU raw data**

This firmware minimizes latency of IMU raw data for directly connected IMU sensors up to 100Hz.

#### <span id="page-7-4"></span>**4.1.8 Wake-on-motion (modules only)**

IMU inside module can be utilized to wake up host system by interrupt line. Please refer to the integration manual [2] for more detailed information regarding this feature.

#### <span id="page-7-5"></span>**4.1.9 ADR w/o directional information**

This release introduces the ability to use wheel tick data without the directional input to reach a sensor fusion fix. The use of the WT directional input can be configured with CFG-SFODO-DIS\_DIR\_INFO configuration item.

### <span id="page-7-6"></span>**4.1.10 Better navigation output debugging with UBX-NAV-PVAT**

A new additional message UBX-NAV-PVAT has been implemented to improve debugging and unify navigation solution output. The new message which has a similar structure to UBX-NAV-PVT but includes additional information about attitude solution.

#### <span id="page-7-7"></span>**4.1.11 Advanced calibration handling**

Advanced calibration handling feature allows a customer to regularly save and later apply sensor fusion initialization and calibration parameters to quickly achieve a sensor fusion fix following a device restart/reset. UBX-MGA-SF message group has been implemented to enable polling and pushing of this data from the receiver. Please refer to the integration manual [2] for more information regarding how to use the feature.



### <span id="page-8-0"></span>**4.1.12 Jamming detection algorithms**

Jamming detection algorithms have been revisited and updated. The benefit is better support of multi-band/multi-constellation operation. Reporting of Jamming and spoofing is available via UBX-SEC message class (see interface description [1]).

### <span id="page-8-1"></span>**4.2 Removed features**

### <span id="page-8-2"></span>**4.2.1 QZSS L1S support**

Support for the QZSS L1S signal (SLAS service) has been removed from this release.

#### <span id="page-8-3"></span>**4.2.2 Magnetic Declination output**

Magnetic Declination output has been removed and now appears as n/a in messages such as UBX-NAV-PVT.

#### <span id="page-8-4"></span>**4.2.3 Odometer feature**

Odometer feature was removed from this firmware.

#### <span id="page-8-5"></span>**4.2.4 Geofence feature**

Geofence feature was removed from this firmware.

## <span id="page-8-6"></span>**5 Supported sensor drivers**

The following IMUs have been fully characterized and are therefore supported by this release.

Operating temperature -40˚C to +105˚C: STm ISM330DHCX, TDK IIM42652

Operating temperature -40˚C to +85˚C: Bosch BMI 160, STm LSM6DSR (reports the same 'Sensor Id' as the STm ISM330DHCX in sensor self-test), TDK ICM42605

In addition, the following sensor drivers are also included in this release: MPU6500, MPU6515, Bosch SMI130, Bosch SMI230, Bosch BMI320, STm ISM330DLC, TDK IAM20680, 20680HT, 20680HP and 20680M

All other sensors not listed above were removed from the firmware.

# <span id="page-8-7"></span>**6 Support and questions**

u-blox products are designed for best performance and u-blox is doing the very best to ensure customers are completely satisfied. In the unlikely case an issue is observed please check first documentation to ensure the product is configured and used in the right way. In case the issue is reproducible please forward a comprehensive description of the issue (ideally with ubx debug log files) to your local u-blox support team. u-blox is eager to improve products continuously and is looking forward supporting customers on their way to success.

# <span id="page-8-8"></span>**7 Limitations**

Protection level for GNSS bands L1/L5 band configuration is not fine-tuned yet and hence marked as invalid.



# <span id="page-9-0"></span>**8 Further notes**

- GPS L5 signal is marked as not healthy at the time of the release. Therefore, this firmware will not use GPS L5 signals for navigation purpose.
- Please note that the firmware name given by UBX-MON-VER message outputs "LAPL1L2L5 1.30" but not "LAP 1.30". This is expected behavior.

# <span id="page-9-1"></span>**9 Open Source Software**

The u-blox F9 firmware image LAP 1.30 does not contain any open-source software components.

# <span id="page-9-2"></span>**10 Revision History**

| Revision | Date          | Name | Comments                                                                                                                                            |
|----------|---------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 26th-Jan-2023 | mawa | st version; release notes for LAP 1.30B03<br>1                                                                                                      |
| R02      | 21th-Mar-2023 | mawa | Final release LAP 1.30                                                                                                                              |
| R03      | 10th-May-2023 | mawa | Updated tables on new, modified, deprecated, removed UBX messages;<br>added chapters for SPARTN, RTCM messages: updated u-center<br>version number. |