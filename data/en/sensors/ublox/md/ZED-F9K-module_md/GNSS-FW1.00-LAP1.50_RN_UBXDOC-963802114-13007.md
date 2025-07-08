

#### **Release note**

**Author Date Topic Firmware LAP1.50 for ZED-F9K & F9940-KA-DR** UBXDOC-963802114-13007 C1-public Martin Wallebohr 28 January 2025

> Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

#### **Contents**

| 1.1  | Scope                                                                   | 2 |
|------|-------------------------------------------------------------------------|---|
| 1.2  | Related documentation                                                   | 2 |
| 2    | Software releases                                                       | 3 |
| 2.1  | u-blox F9 firmware Images                                               | 3 |
| 2.2  | u-center and firmware update tool                                       | 3 |
| 3    | Message Interfaces                                                      | 3 |
| 3.1  | UBX protocol                                                            | 3 |
| 3.2  | NMEA protocol                                                           | 3 |
| 3.3  | RTCM and SPARTN                                                         | 3 |
| 4    | New features                                                            | 4 |
| 4.1  | New default band configuration                                          | 4 |
| 4.2  | NAVIC                                                                   | 4 |
| 4.3  | Improved allocation of tracking channel                                 | 4 |
| 4.4  | Map aiding                                                              | 4 |
| 4.5  | Support of RTCM 3.4 corrections                                         | 4 |
| 4.6  | Conservative Ambiguity Resolution option                                | 5 |
| 4.7  | Motorbike motion model                                                  | 5 |
| 4.8  | CLAS                                                                    | 5 |
| 4.9  | Improved modelling for SPARTN services during high ionospheric activity | 5 |
| 4.10 | IMU filter for noisy setups                                             | 5 |
| 4.11 | Configurable tolerance of IMU-mount alignment angles                    | 6 |
| 4.12 | New configuration item to disable simulated signal spoofing detection   | 6 |
| 4.13 | Compliance with GB/T 45086.1-2024 in China                              | 6 |
| 5    | Removed features                                                        | 6 |
| 6    | Improvements                                                            | 6 |
| 7    | Supported sensor drivers                                                | 6 |
| 8    | Support and questions                                                   | 7 |
| 9    | Further important notes and limitations                                 | 7 |
| 10   | Open-source software                                                    | 7 |
| 11   | Revision History                                                        | 7 |



#### **General Information**

This release note describes the u-blox F9 firmware LAP 1.50, designed to run on ZED-F9K modules and F9940-KA-DR chips.

### <span id="page-1-0"></span>**1.1 Scope**

This release note covers the changes to the LAP 1.50 firmware compared to the LAP 1.30 firmware version. For a comprehensive list of changes with respect to earlier versions, this Release note should be read in conjunction with the LAP 1.30 Release note [\[9\].](#page-1-2)

### <span id="page-1-1"></span>**1.2 Related documentation**

- <span id="page-1-4"></span>[1] ZED-F9K-01A Integration manual, UBX-18047567, C2-Restricted
- [2] LAP-1.50 Interface description, UBXDOC-963802114-13052, C2-Restricted
- [3] ZED-F9K-01A Data sheet, UBX-21045820, C2-Restricted
- [4] F9940-KA-DR Data sheet, UBXDOC-963802114-11073, C2-Restricted
- <span id="page-1-3"></span>[5] Firmware Update Tool v23.11 Release note, UBXDOC-586767278-71830, C2-restricted
- [6] Service-description: https://developer.thingstream.io/guides/locationservices/pointperfect-service-description
- [7] Getting-started-guide: [https://developer.thingstream.io/guides/location](https://developer.thingstream.io/guides/location-services/pointperfect-getting-started)[services/pointperfect-getting-started](https://developer.thingstream.io/guides/location-services/pointperfect-getting-started)
- [8] Zero-touch-provisioning: [https://developer.thingstream.io/guides/location](https://developer.thingstream.io/guides/location-services/pointperfect-zero-touch-provisioning)[services/pointperfect-zero-touch-provisioning](https://developer.thingstream.io/guides/location-services/pointperfect-zero-touch-provisioning)
- <span id="page-1-2"></span>[9] LAP 1.30 Release note, [UBX-22009742](https://content.u-blox.com/sites/default/files/documents/GNSS-FW1.00-LAP1.30_RN_UBX-22009742.pdf)
- [10] Application note GPS L5 configuration; [UBX-21038688,](https://content.u-blox.com/sites/default/files/documents/GPS-L5-configuration_AppNote_UBX-21038688.pdf) C1-Public



## <span id="page-2-0"></span>**2 Software releases**

#### <span id="page-2-1"></span>**2.1 u-blox F9 firmware Images**

| 1st released firmware image | Audience                                                 |
|-----------------------------|----------------------------------------------------------|
| File                        | JUJU_ROX_100_LAP150.ee9ad82af8f0aa5bc41413e77fd02a0d.bin |
| Firmware Version            | EXT CORE 1.00 (438518)<br>FWVER=LAPL1L2L5 1.50           |
| ROM base support            | ROM 1.02 - ROM BASE 0x118B2060                           |

### <span id="page-2-2"></span>**2.2 u-center and firmware update tool**

The u-center version 24.10 (or later) should be used together with this released product.

u-blox recommends using firmware update tool software version 23.11 (or later) with the released product. For details, see the Firmware update tool Release not[e \[5\].](#page-1-3)

# <span id="page-2-3"></span>**3 Message Interfaces**

### <span id="page-2-4"></span>**3.1 UBX protocol**

This firmware supports UBX protocol version 30.50.

#### <span id="page-2-5"></span>**3.2 NMEA protocol**

This firmware adds support for NMEA version 4.11. Five NMEA standards are supported. The default NMEA version is 4.11, and, alternatively, versions 4.10, 4.0, 2.3, and 2.1 can be enabled.

### <span id="page-2-6"></span>**3.3 RTCM and SPARTN**

- LAP 1.50 firmware supports up to RTCM3 standard version 3.4.
- LAP 1.50 firmware supports up to SPARTN protocol version 2.0.2.



# <span id="page-3-0"></span>**4 New features**

## <span id="page-3-1"></span>**4.1 New default band configuration**

This firmware can be configured for operation in either band option A (L1/L2/E5B) or band option B (L1/L5), with supported GNSS signal types as shown in the following table.

Please note that by default, and in contrast to the previous LAP 1.30 release, this firmware starts up in band option B configuration (L1/L5), with the GNSS signals enabled as in the last column.

| Constellation | L1 band | L2/E5B band | L5 band | Enabled by default |
|---------------|---------|-------------|---------|--------------------|
| GPS           | L1C/A   | L2C         | L5      | L1C/A              |
| Beidou        | B1I     | B2I         | B2A     | B1I, B2A           |
| GLONASS       | L1OF    | L2OF        | -       | L1OF               |
| Galileo       | E1      | E5B         | E5A     | E1, E5A            |
| NavIC         | -       | -           | L5      | -                  |
| QZSS          | L1C/A   | L2C         | L5      | L1C/A, L5          |
| SBAS          | L1C/A   | -           | -       | L1C/A              |

### <span id="page-3-2"></span>**4.2 NAVIC**

Added support for NAVIC L5 signals. NAVIC can be activated by configuration key CFG-SIGNAL-NAVIC\_L5\_ENA. For more information on configuring and enabling NAVIC, see the Integration manual [\[1\]](#page-1-4) and Interface description [2].

### <span id="page-3-3"></span>**4.3 Improved allocation of tracking channel**

When configured in band option A (L1/L2/E5B), the amount of tracking channels dedicated to L2/E5B frequency range has been revisited. Compared to previous LAP 1.30 firmware, this change improves the tracking capacity in those geographical areas where the availability of signals in the sky is particularly high, e.g. over the Asian countries.

### <span id="page-3-4"></span>**4.4 Map aiding**

Map data from external navigation data base can be fed into the receiver to enable map matching functionality for position output. The message UBX-AID-MAPM can be used to send map aiding information to the receiver.

### <span id="page-3-5"></span>**4.5 Support of RTCM 3.4 corrections**

When operating in the RTK mode with RTCM corrections, this firmware now supports RTCM version 3.4 (10403.4) messages.



### <span id="page-4-0"></span>**4.6 Conservative Ambiguity Resolution option**

This firmware includes a new option that can be selected via CFG-NAVHPG-DGNSSMODE, value 5 (RTK\_CAR), for a Conservative Ambiguity Resolution approach. When enabled, the occurrence of false RTK fixes is reduced, especially within challenging environments where disturbances such as multipath may be present. Please note that, depending on conditions, the time to ambiguity fix may be longer when the conservative option is in use.

By default this option is disabled, i.e. firmware starts up with default value 3 (RTK\_FIXED)

### <span id="page-4-1"></span>**4.7 Motorbike motion model**

Motorbikes have dedicated motion characteristics. This firmware supports an advanced dead reckoning motion model for motorbikes. For configuration details, see the integration manual.

### <span id="page-4-2"></span>**4.8 CLAS**

This firmware supports CLAS (Centimeter Level Augmentation Service); an augmentation service broadcasted by the Japanese regional satellites system, QZSS. This free service is intended for mass market applications, such as surveying, heavy machinery, and automotive.

The CLAS augmentation service is broadcasted by a QZSS L6 signal which is not part of the frequency range covered by this firmware. Demodulating and decoding of the QZSS L6 signal is supported by NEO-D9C which then must pass the correction stream to ZED-F9K in the form of UBX-RXM-QZSSL6 messages. This enables the ZED-F9K to directly use these messages and extract the compact SSR (cSSR) formatted corrections to use them directly without further processing or reformatting by an intermediary.

### <span id="page-4-3"></span>**4.9 Improved modelling for SPARTN services during high ionospheric activity**

This firmware includes improvements in the ambiguity resolution algorithms that provide increased robustness and reliability during periods of high solar activity while using SPARTN correction services.

### <span id="page-4-4"></span>**4.10 IMU filter for noisy setups**

This firmware includes the possibility to enable an internal digital filter that reduces a high level of noise that may contaminate the IMU data. A typical situation is the presence of strong vibrations in the vehicle that are not being damped appropriately by the setup and are captured by the IMU, and in turn they may affect sensor fusion performances.

Customers can enable this filter by setting a value above 0 in CFG-MOT-IMU\_FILT\_WINDOW, with a suggested value of 100 [ms] that addresses most common situations. By default, the filter is disabled (i.e. configuration value is 0).

Before enabling any IMU filtering, it is recommended to confirm that the IMU setup in use is indeed capturing too much noise. This can be done by checking that a high noise level indication is consistently reported by the UBX-ESF-STATUS message.



## <span id="page-5-0"></span>**4.11 Configurable tolerance of IMU-mount alignment angles**

This firmware includes the new public configuration item CFG-SFIMU-IMU\_MNTALG\_TOLERANCE. Users can now select the tolerance level when they configure the IMU-mount alignment angles (CFG-SFIMU-IMU\_MNTALG\_PITCH, ROLL, YAW).

By default, the tolerance level is set to LOW (value 0), meaning that the specified alignment angles are known with high accuracy, i.e. up to 2 degrees wrong. If needed, users can select the tolerance level HIGH (value 1), meaning that the configured angles must be considered coarse, for example because not professionally measured, and they can include errors preferably within 5 degrees, and in any case no more than 10 degrees. Alternatively, if angles cannot be set with such accuracies, users can enable the automatic IMU-mount alignment (CFG-SFIMU-AUTO\_MNTALG\_ENA), or at least enable it in a first run in order to measure the angles.

This configuration helps in the customization of the specific setup. A low tolerance level profits from shorter SF calibration times. A higher tolerance level increases calibration times but also increases robustness in case there are alignment deviations from nominal values.

### <span id="page-5-1"></span>**4.12 New configuration item to disable simulated signal spoofing detection**

A new configuration item called CFG-SEC-SPOOFDET\_SIM\_SIG\_DIS is now available and can be used to disable the anti-spoofing detection for simulated signals. When enabled, it can be useful when testing or evaluating the receiver in a laboratory environment that uses simulated RF signals, so that spoofing flags are not raised due to this reason. By default, this configuration is disabled (value 0).

## <span id="page-5-2"></span>**4.13 Compliance with GB/T 45086.1-2024 in China**

This firmware complies with new GB/T 45086.1-2024 standard and test cases in China.

### <span id="page-5-3"></span>**5 Removed features**

- Tunneling mechanism for UART
- ECDSA signature

### <span id="page-5-4"></span>**6 Improvements**

- RTK performance & convergence time for BDS satellite vehicles
- Maturity and robustness of RTK and Sensor fusion solution

### <span id="page-5-5"></span>**7 Supported sensor drivers**

The following IMUs have been fully characterized and are therefore supported by this release.

Operating temperature –40˚C to +105˚C: STm ISM330DHCX, TDK IIM42652

Operating temperature –40˚C to +85˚C: Bosch BMI 160, STm LSM6DSR (reports the same 'Sensor Id' as the STm ISM330DHCX in sensor self-test), TDK ICM42605



In addition, the following sensor drivers are also included in this release: MPU6500, MPU6515, Bosch SMI130, Bosch SMI230, SMI330, Bosch BMI320, BMI330, STm ISM330DLC, TDK IAM20680, 20680HT, 20680HP and 20680M.

All other sensors not listed above were removed from the firmware.

## <span id="page-6-0"></span>**8 Support and questions**

u-blox products are designed for the best performance and we are committed to ensuring customers are completely satisfied with them. In the unlikely case an issue is observed:

- first check the product documentation to ensure that the product is configured and used correctly.
- If you can reproduce the issue, send a comprehensive description of the issue to your local u-blox support team, ideally with ubx debug log files.

u-blox strives to continuously improve the products and is looking forward to supporting customers on their way to success.

# <span id="page-6-1"></span>**9 Further important notes and limitations**

- The GPS L5 signal is marked as not healthy at the time of the release. Therefore, this firmware does not use GPS L5 signals for navigation purpose by default. Activation of GPS L5 is described in [9].
- Note that the UBX-MON-VER message outputs the firmware name as "LAPL1L2L5 1.50", not as "LAP 1.50". This is expected behavior.
- Default GNSS band configuration for this firmware is L1/L5. Please note that default band configuration for LAP 1.30 is L1/L2.
- Protection level for GNSS bands L1/L5 band configuration is not fine-tuned and hence marked as invalid.

# <span id="page-6-2"></span>**10 Open-source software**

The u-blox F9 firmware image LAP 1.50 does not contain any open-source software components.

## <span id="page-6-3"></span>**11 Revision History**

| Revision | Date         | Name | Comments                                |
|----------|--------------|------|-----------------------------------------|
| R01      | 18-Sept-2024 | mawa | Prototype release notes for LAP 1.50A05 |
| R02      | 28-Jan-2025  | Mawa | Final LAP 1.50 release                  |