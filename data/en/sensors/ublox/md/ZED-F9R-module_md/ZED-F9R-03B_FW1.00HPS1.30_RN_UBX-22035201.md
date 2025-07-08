

#### **Release note**

**Topic ZED-F9R-03B with firmware FW1.00 HPS1.30**

UBX-22035201 C1-Public

**Author** Alex Ngi

**Date** 15 January 2025

> Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

#### Contents

| 1     | General information                           | 2 |  |
|-------|-----------------------------------------------|---|--|
| 1.1   | Scope                                         | 2 |  |
| 1.2   | Released firmware image                       | 2 |  |
| 1.3   | Related software                              | 2 |  |
| 1.4   | Open-Source declaration                       | 2 |  |
| 1.5   | Related documentation                         | 2 |  |
| 2     | New features                                  | 2 |  |
| 2.1   | SPARTN 2.0.1                                  | 2 |  |
| 2.2   | SPARTN over L-band                            | 3 |  |
| 2.3   | SPARTN source selection                       | 3 |  |
| 2.4   | PointPerfect encrypted SPARTN support         | 3 |  |
| 2.5   | CLAS CSSR                                     | 3 |  |
| 2.6   | QZSS L1S signal support for SLAS              | 3 |  |
| 2.7   | UBX protocol on UART2                         | 4 |  |
| 2.8   | Re-optimized sensor fusion                    | 4 |  |
| 2.9   | Improved jamming and spoofing detection       | 4 |  |
| 2.10  | Wheel Tick-based spoofing detection           | 4 |  |
| 2.11  | Advanced Calibration Handling                 | 4 |  |
| 2.12  | Secondary output                              | 4 |  |
| 2.13  | Processor loading monitoring                  | 4 |  |
| 2.14  | High-precision GNSS position protection level | 5 |  |
| 2.15  | Directionless Wheel Tick support              | 5 |  |
| 2.16  | Wake on motion                                | 5 |  |
| 3     | Message interface                             | 5 |  |
| 3.1   | UBX protocol                                  | 5 |  |
| 3.2   | NMEA protocol                                 | 5 |  |
| 3.3   | New messages                                  |   |  |
| 3.4   | Modified messages                             | 7 |  |
| 3.5   | Removed messages                              | 7 |  |
| 3.6   | Firmware changes                              | 8 |  |
| 3.6.1 | Improvements                                  | 8 |  |
| 3.6.2 | Firmware known limitations                    | 8 |  |
| 3.6.3 | Hardware known limitations                    | 9 |  |
| 4     | Revision history                              | 9 |  |



# <span id="page-1-0"></span>**1 General information**

The product with order code ZED-F9R-03B is delivered with the HPS1.30 firmware. This document is also applicable to other devices capable of running this firmware.

#### <span id="page-1-1"></span>**1.1 Scope**

This release note covers the changes to the HPS 1.30 firmware compared to the HPS 1.21 firmware version. For a comprehensive list of changes with respect to earlier versions, this release note should be read in conjunction with the HPS 1.21 release notes [4].

#### <span id="page-1-2"></span>**1.2 Released firmware image**

| Released firmware image |                                                         |  |
|-------------------------|---------------------------------------------------------|--|
| File                    | UBX_F9R_100_HPS130.3437fe3d1f7b8807403bed548d6142d0.bin |  |
| Firmware version        | EXT CORE 1.00 (a59682)<br>FWVER=HPS 1.30                |  |
| ROM base support        | ROM 1.02 - ROM BASE 0x118B2060                          |  |

### <span id="page-1-3"></span>**1.3 Related software**

Version 22.07 (or later) of u-center GNSS evaluation software is recommended to be used with the released firmware. Please contact FAE if this version is not available on the official web site.

Version 19.03 (or later) of the firmware update tool supports this release.

### <span id="page-1-4"></span>**1.4 Open-Source declaration**

This u-blox positioning product described in this release note, comprising the company's proprietary software, does not contain open-source software to declare.

#### <span id="page-1-5"></span>**1.5 Related documentation**

- [1] u-blox HPS 1.30 Interface description, [UBX-22010984](https://www.u-blox.com/en/docs/UBX-22010984)
- [2] u-blox ZED-F9R Integration Manual[, UBX-20039643](https://www.u-blox.com/en/docs/UBX-20039643)
- [3] u-blox ZED-F9R-03B Data Sheet[, UBX-22024085](https://www.u-blox.com/en/docs/UBX-22024085)
- <span id="page-1-6"></span>[4] ZED-F9R-02B-HPS\_Release Note[, UBX-21035491](https://www.u-blox.com/en/docs/UBX-UBX-21035491)

## **2 New features**

When migrating from a previous version of the product, users of the product are advised to perform a thorough re-testing in their system. HPS130 should be thought of as a new firmware release rather than an update or upgrade from HPS121.

### <span id="page-1-7"></span>**2.1 SPARTN 2.0.1**

SPARTN, Secure Position Augmentation for Real Time Navigation, is an open standard format available at [https://www.spartnformat.org/.](https://www.spartnformat.org/)

A service provider using SPARTN formatted corrections can enable high precision positioning applications with the ZED-F9R. Compared to RTCM, which is used primarily for OSR, SPARTN has a complete set of messages suitable for SSR models without the use of vendor specific messages. The use of SSR in the foundation allows services to be efficiently delivered over a



broadcast medium such as L-band satellite signal or cellular networks. This allows a product to be deployed anywhere on a continent with a single service provider.

This release of SPARTN supports corrections for GPS, GLONASS and Galileo.

## <span id="page-2-0"></span>**2.2 SPARTN over L-band**

ZED-F9R supports SPARTN corrections as broadcasted by L-band satellites.

Receiving the SPARTN correction stream requires a NEO-D9S who then must pass the correction stream to ZED-F9R in the form of UBX-RXM-PMP messages either by directly connecting the UART interfaces between the devices or the host relaying the messages.

#### <span id="page-2-1"></span>**2.3 SPARTN source selection**

ZED-F9R supports multiple SPARTN correction stream sources. It can support a SPARTN correction stream received over the internet (SPARTN IP stream) or over L-band satellites (SPARTN L-band stream). Only one source can be configured to be used at a time by ZED-F9R.

### <span id="page-2-2"></span>**2.4 PointPerfect encrypted SPARTN support**

ZED-F9R supports on-device decryption of encrypted PointPerfect SPARTN correction streams. PointPerfect is a correction service available from u-blox that can provide SPARTN correction streams over the internet or over L-band satellites.

## <span id="page-2-3"></span>**2.5 CLAS CSSR**

ZED-F9R supports CLAS (Centimeter Level Augmentation Service); an augmentation service broadcasted by the Japanese regional satellites system, QZSS. This free service is intended for mass market applications, such as surveying, heavy machinery used in precision construction, and precision agriculture.

The CLAS augmentation service is broadcasted by a QZSS L6 signal which is not part of the frequency range covered by ZED-F9R. As such, ZED-F9R does not support receiving, demodulating and decoding of the QZSS L6 signal. This is supported by NEO-D9C which then must pass the correction stream to ZED-F9R in the form of UBX-RXM-QZSSL6 messages. This enables the ZED-F9R to directly use these messages and extract the compact SSR (cSSR) formatted corrections in order to use them directly without further processing or reformatting by an intermediary.

At the time of this release note, a CLAS solution with ZED-F9R augments GPS L1C/A L2C, QZSS L1 C/A L2C, and Galileo E1B/C.

## <span id="page-2-4"></span>**2.6 QZSS L1S signal support for SLAS**

ZED-F9R supports SLAS (Sub-meter Level Augmentation Service); an augmentation service broadcasted by the Japanese regional satellites system, QZSS. This is a free service available in Japan.

The SLAS augmentation service is broadcasted by a QZSS L1S signal which is not part of the frequency range covered by ZED-F9R.

The CLAS solution augments systems using the GPS and QZSS constellations.



# <span id="page-3-0"></span>**2.7 UBX protocol on UART2**

ZED-F9R adds support for the UBX protocol as an input/output protocol on the UART2 interface.

Not all UBX functionality is available on UART2. UART2 should not be used as the sole interface.

### <span id="page-3-1"></span>**2.8 Re-optimized sensor fusion**

The sensor fusion system has been re-worked and optimized. As a result a higher GNSS update rate, when priority navigation mode is not enabled, can be achieved.

### <span id="page-3-2"></span>**2.9 Improved jamming and spoofing detection**

The ZED-F9R has improved mechanisms to detect jamming and spoofing related events that are reported to the user in a UBX message. Jamming is considered any kind of signal that is captured in RF band of the receiver and may affect the Carrier-to-noise ratio and signal tracking algorithms. Spoofing is broadly some kind of counterfeit signal generated intentionally by malicious parties in various possible ways.

The responses of different type of detectors are combined in a decision logic that is summarized in the log messages along with the duration of the detected events.

### <span id="page-3-3"></span>**2.10 Wheel Tick-based spoofing detection**

The ZED-F9R includes a specific spoofing detector for Dead Reckoning products that is using the wheel tick signal along with pure GNSS information for detecting spoofing events. The decision as to whether the indicator is a real threat to the system is use case dependent.

### <span id="page-3-4"></span>**2.11 Advanced Calibration Handling**

The ZED-F9R supports the restoration of sensor calibration values by the host after the system is powered off. Some hardware designs do not implement a battery backup due to costs. This feature allows the system to operate in sensor fusion mode after stopping the vehicle and backing up the values to the host.

### <span id="page-3-5"></span>**2.12 Secondary output**

A complete set of Navigation messages is available based on a solution computed by a secondary GNSS standalone filter at the same update rate as the primary output (GNS + sensor + RTK). These messages are available both in NMEA and UBX protocols.

These messages can be configured to restrict the use to only GPS satellites which have integrity monitoring messages. The resulting secondary output messages can be used as a check against potential software faults in the correction service or RTK software in the system. The secondary output is also a useful tool during development.

By default, the secondary output is disabled.

### <span id="page-3-6"></span>**2.13 Processor loading monitoring**

The UBX-MON-SYS message provides the instantaneous system performance in terms of CPU loading, memory usage and I/O usage. This may be used for user to evaluate the product in non-



default configurations to assess the impact on update rates on advanced functions like protection level or secondary outputs.

## <span id="page-4-0"></span>**2.14 High-precision GNSS position protection level**

ZED-F9R reports a high-precision GNSS position protection level (HPG PL) with a Target Misleading Information Risk (TMIR) of 5 [%MI/epoch], in other words a 5% probability of having misleading information per epoch.

ZED-F9R currently supports only position protection level output. It does not support velocity and time protection level output.

The confidence level of the protection level is validated against specific operating conditions. In the case of ZED-F9R it has been validated for RTK operation with RTCM input correction streams for VRS and local base as well as PPP-RTK with only the automotive dynamic model. The protection level output generated by the use of other dynamic models are marked as invalid.

#### <span id="page-4-1"></span>**2.15 Directionless Wheel Tick support**

For systems where the direction input is not available in conjunction with the wheel tick, the ZED-F9R offers a configuration item to support this operating mode. The accuracy may be degraded compared to a system where both wheel tick and direction input is available.

### <span id="page-4-2"></span>**2.16 Wake on motion**

This feature is only available in ZED-F9R-03B hardware. The module IMU can monitor an accelerometer threshold and wake-up the host using an interrupt output pin.

With previous generations of hardware this pin is reserved and this feature is not available.

# <span id="page-4-3"></span>**3 Message interface**

#### <span id="page-4-4"></span>**3.1 UBX protocol**

This firmware supports UBX protocol version 33.30.

#### <span id="page-4-5"></span>**3.2 NMEA protocol**

NMEA version 4.11 is the default and is unchanged.

#### <span id="page-4-6"></span>**3.3 New messages**

| Message / Configuration item | Description / Comment                                                                                                                                                 |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPARTN-1X-OCB_GAL            | SPARTN 2.0 input messages supported beyond SPARTN 1.8.                                                                                                                |
| SPARTN-1X-HPAC_GAL           |                                                                                                                                                                       |
| SPARTN-1X-OCB_BDS            |                                                                                                                                                                       |
| SPARTN-1X-OCB_QZSS           |                                                                                                                                                                       |
| SPARTN-1X-HPAC_BDS           |                                                                                                                                                                       |
| SPARTN-1X-HPAC_QZSS          |                                                                                                                                                                       |
| CFG-SPARTN-USE_SOURCE        | Select SPARTN input source to be used; can be IP stream containing<br>SPARTN format messages or L-band stream containing UBX-RXM-PMP<br>format messages (default: IP) |
| UBX-RXM-COR                  | Differential correction input status. Reported for all parsed correction input<br>and can be used instead of UBX-RXM-RTCM and UBX-RXM-SPARTN.                         |
|                              |                                                                                                                                                                       |



|                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Message output rate configurable with new CFG-MSGOUT-UBX_RXM_COR_*<br>configuration items.                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UBX-RXM-SPARTNKEY                                                                                                                                                                                                                                                                                                                                                                                                                               | Poll or transfer dynamic SPARTN keys to be used for decrypting input<br>SPARTN format messages                                                                                                                                                                                        |
| UBX-RXM-QZSSL6                                                                                                                                                                                                                                                                                                                                                                                                                                  | QZSS L6 message. Input support for QZSS L6 messages containing a CLAS<br>CSSR correction stream. UBX-RXM-QZSSL6 output requires a NEO-D9C.                                                                                                                                            |
| UBX-RXM-PMP                                                                                                                                                                                                                                                                                                                                                                                                                                     | Point to Multipoint (LBAND) message. Input support for SPARTN corrections<br>as broadcasted by L-band satellites. UBX-RXM-PMP output requires a NEO<br>D9S.                                                                                                                           |
| CFG-QZSS-SLAS_MAX_BASELINE                                                                                                                                                                                                                                                                                                                                                                                                                      | Maximum baseline distance to closest GMS for applying SLAS corrections<br>(default: 350 km)                                                                                                                                                                                           |
| CFG-QZSS-USE_SLAS_DGNSS<br>CFG-QZSS<br>USE_SLAS_RAIM_UNCORR<br>CFG-QZSS-USE_SLAS_TESTMODE                                                                                                                                                                                                                                                                                                                                                       | Configurations for SLAS corrections:<br>1. Set maximum baseline distance to the closest ground monitoring station<br>2. Use SLAS differential corrections<br>3. RAIM measurements that are not corrected by SLAS corrections<br>4. Enable Use of SLAS messages which are in test mode |
| CFG-NAV2-*<br>CFG-NAV2-OUT_ENABLED<br>CFG-NAV2-SBAS_USE_INTEGRITY                                                                                                                                                                                                                                                                                                                                                                               | Configuration group CFG-NAV2 with configuration items for secondary<br>output setup (default: secondary output disabled)                                                                                                                                                              |
| UBX-NAV2-CLOCK<br>UBX-NAV2-COV<br>UBX-NAV2-DOP<br>UBX-NAV2-EELL<br>UBX-NAV2-EOE<br>UBX-NAV2-ODO<br>UBX-NAV2-POSECEF<br>UBX-NAV2-POSLLH<br>UBX-NAV2-PVAT<br>UBX-NAV2-PVT<br>UBX-NAV2-SAT<br>UBX-NAV2-SBAS<br>UBX-NAV2-SIG<br>UBX-NAV2-SLAS<br>UBX-NAV2-STATUS<br>UBX-NAV2-TIMEBDS<br>UBX-NAV2-TIMEGAL<br>UBX-NAV2-TIMEGLO<br>UBX-NAV2-TIMEGPS<br>UBX-NAV2-TIMELS<br>UBX-NAV2-TIMEQZSS<br>UBX-NAV2-TIMEUTC<br>UBX-NAV2-VELECEF<br>UBX-NAV2-VELNED | Secondary output (NAV2) messages in UBX format. Message output rate<br>configurable with new CFG-MSGOUT-UBX_NAV2-* configuration items.                                                                                                                                               |
| NMEA-NAV2-ID-GGA<br>NMEA-NAV2-ID-GLL<br>NMEA-NAV2-ID-GNS<br>NMEA-NAV2-ID-GSA<br>NMEA-NAV2-ID-RMC<br>NMEA-NAV2-ID-VTG<br>NMEA-NAV2-ID-ZDA                                                                                                                                                                                                                                                                                                        | Secondary output (NAV2) messages in NMEA format. Available if configured<br>NMEA version is NMEA 4.0 or later. Message output rate configurable with<br>CFG-MSGOUT-NMEA_NAV2_ID_* configuration items.                                                                                |
| UBX-NAV-PL                                                                                                                                                                                                                                                                                                                                                                                                                                      | Protection level information. Message output rate configurable with new<br>CFG-MSGOUT-UBX_NAV_PL_* configuration items.                                                                                                                                                               |



| CFG-NAVSPG-PL_ENA                            | Enable/disable protection level computing (default: protection level<br>computing<br>enabled)                                                                   |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UBX-SEC-SIGLOG                               | A new message to output signal security log, message output rate is<br>configurable with CFG-MSGOUT-UBX_SEC_SIGLOG_ * configuration items                       |
| UBX-MON-SYS                                  | Current system performance information. Message output rate configurable<br>with new CFG-MSGOUT-UBX_MON_SYS_* configuration items.                              |
| UBX-MGA-SF                                   | Aiding message for sensor fusion calibration                                                                                                                    |
| CFG-HW-SENS_WOM_MODE<br>CFG-HW-SENS_WOM_THLD | Configuration to set the Wake-on-motion mode of operation<br>Configuration to set the acceleration threshold which when reached would<br>wake up the IMU sensor |
| CFG-SBAS-USE_IONOONLY                        | Configuration to enable use of SBAS ionosphere correction only                                                                                                  |
| CFG-SEC-JAMDET_SENSITIVITY_HI                | Enable to increase the sensitivity of jamming detection at the expense of<br>increased false alarm rate                                                         |
| CFG-SFODO-DIS_DIR_INFO                       | Configuration to disable the use of WT directional information                                                                                                  |
| CFG-SIGNAL-QZSS_L1S_ENA                      | Configuration to enable QZSS L1S signal                                                                                                                         |
| CFG-MSGOUT-UBX_RXM_COR_*                     | Configuration to enable output of differential correction input status                                                                                          |
| CFG-MSGOUT-UBX_NAV2-*                        | Configuration to enable output of secondary output messages in UBX format                                                                                       |
| CFG-MSGOUT-NMEA_NAV2_ID_*                    | Configuration to enable output of secondary output messages in NMEA<br>format                                                                                   |
| CFG-MSGOUT-UBX_NAV_PL_*                      | Configuration to enable output of Protection level messages                                                                                                     |
| CFG-MSGOUT-UBX_SEC_SIGLOG_ *                 | Configuration to enable output of security log messages                                                                                                         |

#### <span id="page-6-0"></span>**3.4 Modified messages**

| Message / Configuration item                        | Description / Comment                                                                                          |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| CFG-SBAS-PRNSCANMASK                                | Default value changed from 0x0000000000072bc8 to<br>0x0000000000072b88 and does not include PRN126             |
| CFG-SFIMU-ACCEL_ACCURACY<br>CFG-SFIMU-GYRO_ACCURACY | Default value was changed from FW default (0) to 1000 (10^-<br>4 * m/s^2) and 100 (10^-3 * deg/s) respectively |
| CFG-SFODO-DIS_AUTOSW                                | Default value was changed from false to true                                                                   |
| CFG-UART2INPROT-UBX                                 | UBX input on UART2 is now enabled by default                                                                   |
| UBX-NAV-SIG<br>UBX-NAV-SAT                          | New correction sources CLAS reported                                                                           |

#### <span id="page-6-1"></span>**3.5 Removed messages**

| Message / Configuration item | Description / Comment                                   |
|------------------------------|---------------------------------------------------------|
| UBX-CFG-ANT                  | Legacy configuration messages that were dropped, please |
| UBX-CFG-DAT                  | refer to the interface description document for the     |
| UBX-CFG-DGNSS                | recommended configuration items to use in the new       |
| UBX-CFG-ESFA                 | configuration concept.                                  |
| UBX-CFG-ESALG                |                                                         |
| UBX-CFG-ESFWT                |                                                         |
| UBX-CFG-GEOFENCE             |                                                         |
| UBX-CFG-GNSS                 |                                                         |
| UBX-CFG-INF                  |                                                         |
| UBX-CFG-ITFM                 |                                                         |
|                              |                                                         |



| UBX-CFG-NAV5         |                                                              |
|----------------------|--------------------------------------------------------------|
| UBX-CFG-NAVX5        |                                                              |
| UBX-CFG-NMEA         |                                                              |
| UBX-CFG-PWR          |                                                              |
| UBX-CFG-RATE         |                                                              |
| UBX-CFG-RINV         |                                                              |
| UBX-CFG-SBAS         |                                                              |
| UBX-CFG-SENIF        |                                                              |
| UBX-CFG-TP5          |                                                              |
| UBX-CFG-USB          |                                                              |
| CFG-ITFM-ANTSETTING  | Configuration for legacy interference monitor, this has been |
| CFG-ITFM-BBTHRESHOLD | replaced with simpler configuration interface                |
| CFG-ITFM-CWTHRESHOLD |                                                              |
| CFG-ITFM-ENABLE      |                                                              |
| CFG-ITFM-ENABLE_AUX  |                                                              |

## <span id="page-7-0"></span>**3.6 Firmware changes**

#### <span id="page-7-1"></span>**3.6.1 Improvements**

- Improved SBAS Message Type 1 content handling when containing invalid data
- Improved L2 tracking performance when receiver configured with GPS and GLONASS only
- Configuring the CFG-RATE-NAV configuration item with the unsupported value 128 no longer causes a system restart
- Improvements with handling of SPARTN ionospheric data and operations in Southern Hemisphere
- Improvements when working with datum other than WGS84 in corrections
- Improvements to bring the upper speed limits of the RLM dynamic model in line with specification. It has further been increased to 3 m/s.
- Improvements with many configurations written to flash quickly.

#### <span id="page-7-2"></span>**3.6.2 Firmware known limitations**

- After exiting a tunnel, solution stays in dead reckoning mode longer than expected.
- System signal configuration performed by CFG-SIGNAL-\* immediately after startup may be ignored until the next GNSS restart. Configuring to flash is a workaround.
- NMEA GxVLW and GxTHS messages in version 2.3 where information in version 4.0 is present.
- NMEA GxGRS and GxGNS messages may exceed the 82-character limit to 85 characters.
- Inconsistent WT (wheel tick or speed) input can lead to an unexpected receiver reset and a potential configuration reset to factory default values in RAM, BBR and flash. An exception string output (\$GNTXT,01,01,01,exception 0x00020002 has occurred\*2E) might be observed. This happens during the WT scale factor estimation process and is typically seen when starting to drive. There are two scenarios that could trigger the issue:
  - o The WT input signal reflecting vehicle movement is not provided to the WT pin while the configuration item CFG-SFODO-USE\_WT\_PIN is set to 1 (true).
  - o The WT is provided as data via UBX-ESF-MEAS messages, but the data values do not indicate true speed or distance travelled.
  - Workaround 1: Configure CFG-SFODO-USE\_WT\_PIN to 0 (false) if the WT pin is not intended to be used by the application.



Workaround 2: Refrain from sending inconsistent odometer data in UBX-ESF-MEAS which does not reflect the travelled distance.

• UBX-MON-RF message is incorrectly implemented. Flags fields and trailing reserved bytes are missing and the cwSuppresion field is in a different order within the repeat block. This is inconsistent with the same message implemented for other for products and the format supported by u-center. Logs could be made compatible with u-center by the user modifying the log. U-blox does not provide an application to do this. There may be other work arounds.

#### <span id="page-8-0"></span>**3.6.3 Hardware known limitations**

- USB interface may not be possible to certify according to the USB standard.
- I2C has setup time issue when used with clock stretching and using fast mode is recommended.

## <span id="page-8-1"></span>**4 Revision history**

| Revision | Date        | Name | Comments                                        |
|----------|-------------|------|-------------------------------------------------|
| R01      | 20-SEP-2022 | ANGI | First release of release note                   |
| R02      | 10-MAR-2023 | ANGI | Update of known limitation regarding WT         |
| R03      | 15-JAN-2025 | ANGI | Update of known limitation regarding UBX-MON-RF |