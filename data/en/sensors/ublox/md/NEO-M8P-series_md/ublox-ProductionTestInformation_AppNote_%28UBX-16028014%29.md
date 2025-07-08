# **u-blox Production Test Information For u-blox 6 / 7 / 8 / M8 GNSS modules Application Note**

### **Abstract**

This document provides descriptions of production tests for u-blox GNSS modules.



**[www.u-blox.com](http://www.u-blox.com/)**

UBX-16028014 - R01





| Document Information |                                        |             |
|----------------------|----------------------------------------|-------------|
| Title                | u-blox Production Test Information     |             |
| Subtitle             | For u-blox 6 / 7 / 8 / M8 GNSS modules |             |
| Document type        | Application Note                       |             |
| Document number      | UBX-16028014                           |             |
| Revision and date    | R01                                    | 21-Nov-2016 |
| Document status      | Production Information                 |             |
|                      |                                        |             |

| Document status explanation  |                                                                                                          |  |
|------------------------------|----------------------------------------------------------------------------------------------------------|--|
| Objective Specification      | Document contains target values. Revised and supplementary data will be published later.                 |  |
| Advance Information          | Document contains data based on early testing. Revised and supplementary data will be published later.   |  |
| Early Production Information | Document contains data from product verification. Revised and supplementary data may be published later. |  |
| Production Information       | Document contains the final product specification.                                                       |  |

u-blox reserves all rights to this document and the information contained herein. Products, names, logos and designs described herein may in whole or in part be subject to intellectual property rights. Reproduction, use, modification or disclosure to third parties of this document or any part thereof without the express permission of u-blox is strictly prohibited.

The information contained herein is provided "as is" and u-blox assumes no liability for the use of the information. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, please visit www.u-blox.com.

Copyright © 2016, u-blox AG



<span id="page-2-0"></span>

|          | Contents3                                 |  |
|----------|-------------------------------------------|--|
| 1        | Introduction4                             |  |
| 1.1      | Purpose  4                                |  |
| 1.2      | Scope  4                                  |  |
| 2        | Product testing<br>5                      |  |
| 2.1      | u-blox in-series production test 5        |  |
| 2.2      | Test parameters for OEM manufacturer 5    |  |
| 2.3      | Test Environment 5                        |  |
| 3        | Recommended product tests6                |  |
| 3.1      | System sensitivity test  6                |  |
| 3.2      | Guidelines for sensitivity tests  6       |  |
| 3.3      | "Go/No go" tests for integrated devices 7 |  |
| 4        | Optional product tests<br>8               |  |
| 4.1      | Clock oscillator stability  8             |  |
| 4.2      | Digital PIO functionality  9              |  |
| Appendix | 10                                        |  |
| A        | Glossary<br>10                            |  |
|          | Revision history11                        |  |
|          | Contact12                                 |  |



## <span id="page-3-0"></span>**1 Introduction**

### <span id="page-3-1"></span>**1.1 Purpose**

This application note provides information for customers on how to test u-blox GNSS modules in their production. The information is in addition to what is provided in the product data sheets, protocol specifications and hardware integration manuals.

The following symbols are used to highlight important information within the document:

An index finger points out key information pertaining to product integration and performance.

**A warning symbol indicates actions that could negatively impact or damage the product.**

### <span id="page-3-2"></span>**1.2 Scope**

This application note provides general production test information for u-blox GNSS modules of various generations, including u-blox 6, 7, 8 and M8. It should be used in combination with the applicable data sheet, protocol specification and hardware integration manual, in order to have the exact product specifications and recommendations for product integration.

This application note does not apply to GNSS chipsets.



## <span id="page-4-0"></span>**2 Product testing**

## <span id="page-4-1"></span>**2.1 u-blox in-series production test**

u-blox focuses on high quality for its products. To achieve a high standard it is our philosophy to supply fully tested units. Therefore at the end of the production process, every unit is tested. Defective units are analyzed in detail to improve the production quality.

This is achieved with automatic test equipment, which delivers a detailed test report for each unit. The following measurements are done:

- Digital self-test (software download, verification of FLASH firmware, etc.)
- Measurement of voltages and currents
- Measurement of RF characteristics (e.g. C/N0)





**Figure 1: Automatic Test Equipment for Module Tests**

### <span id="page-4-2"></span>**2.2 Test parameters for OEM manufacturer**

Because of the testing done by u-blox (with 100% coverage), it is obvious that an OEM manufacturer doesn't need to repeat firmware tests or measurements of the GNSS parameters/characteristics (e.g. TTFF) in their production test.

An OEM manufacturer should focus on:

- Overall sensitivity of the device (including antenna, if applicable)
- Communication to a host controller

Additional optional tests may also be performed, but they can be omitted to minimize production testing:

- Clock oscillator stability
- Digital PIO functionality

### <span id="page-4-3"></span>**2.3 Test Environment**

The best method to validate the test environment is to record measurements on a number of samples of known good and bad units, at least 5 to 10 of each. Appropriate pass/fail limits can then be defined. The test conditions should be adjusted so that all the known good units will pass and all the known bad units will fail and these results are consistent when repeated. It is recommended to periodically re-calibrate the pass/fail limits to ensure they remain valid.



## <span id="page-5-0"></span>**3 Recommended product tests**

These are tests that u-blox recommends OEM manufacturers to perform on GNSS modules.

### <span id="page-5-1"></span>**3.1 System sensitivity test**

The best way to test the sensitivity of a GNSS device is with the use of a 1-channel GNSS simulator. It assures reliable and constant signals at every measurement.



#### **Figure 2: 1-channel GNSS simulator**

u-blox recommends one of the following 1-channel GNSS simulators from Spirent Communications Positioning Technology:

- Spirent GSS6100 (GPS)
- Spirent GSS6300 (GPS/GLONASS)

### <span id="page-5-2"></span>**3.2 Guidelines for sensitivity tests**

- 1. Connect a 1-channel GNSS simulator to the OEM product with no additional gain (no external LNA).
- 2. Choose the power level (typically -130 dBm) such that the "Golden Device" reports a C/N0 ratio of 40- 44 dBHz.
- 3. Power up the device under test (DUT) and allow enough time for it to acquire the signal.
- 4. Read the C/N0 value from the NMEA-GSV, UBX-NAV-SVINFO or UBX-NAV-SAT message (e.g. with u-center).
- 5. Compare the results to a "Golden Device" or if not available, a u-blox Evaluation Kit.

You can estimate the expected C/N0 ratio using the noise figure specified in the module data sheet. For example if the module noise figure is 2 dB and a signal power of -130 dBm is provided to the RF input of the module, the C/N0 ratio should be approximately 42 dBHz = -130 dBm + 174 dBm/Hz – 2 dB, where -174 dBm/Hz is the noise power density in a 50 system at room temperature. Pass/fail limits based on this should allow for a tolerance of +/- 2 dB, so in this case the recommended pass/fail limits should be 40-44 dBHz. It may be necessary to account for signal loss in any splitters and cables in use, as these may reduce the C/N0 ratio and the corresponding pass/fail limits. Comparison testing with "Golden Devices" will help confirm the limits to use.

If an additional SAW filter is integrated in the OEM product before the module RF input, then the insertion loss from the filter data sheet specified for the signal frequency in use should be deducted from the expected C/N0 ratio. A typical filter insertion loss is 1 dB, so in the case above, the expected C/N0 ratio would become 41 dBHz and the pass/fail limits would be reduced to 39-43 dBHz.



If the device includes an external LNA or combination SAW-LNA device before the module RF input, then replace the noise figure of the module in the above calculation with the figure specified in the LNA or SAW-LNA data sheet. For example, if the LNA noise figure is 1 dB the expected C/N0 ration will be approximately 43 dBHz (- 130 dBm + 174 dBm/Hz – 1 dB = 43 dBHz) and the pass/fail limits should be 41-45 dBHz.

The gain of any external LNA needs to be a minimum of 15-20 dB to be beneficial and for this estimate of C/N0 ratio to be valid.

If the device includes multiple SAW filter and LNA components prior to the module, then determining the system noise figure is less straightforward. It is valid to compare the results with a "Golden Device", but to estimate the expected C/N0, it is best to contact u-blox technical support to request assistance.

### <span id="page-6-0"></span>**3.3 "Go/No go" tests for integrated devices**

It is often not possible to connect a signal to the module RF input for devices with an internal antenna. The best test is to bring the device to an outdoor position **with excellent sky view** (HDOP < 3.0). Let the receiver acquire satellites and compare the signal strength with a "Golden Device" in the same location.

One or more "Golden Devices" should be used on a continuous basis as a comparison for RF signal tests, particularly for such integrated devices. This reduces the effects of any variations in the test environment and improves the reliability of the results from the device under test (DUT).

- As the electro-magnetic field of a redistribution antenna is not homogenous, **indoor tests are in most cases not reliable**. The results will be highly dependent on the location of the DUT with respect to the transmitting antenna, and will be unpredictable and difficult to reproduce. These kinds of tests may be useful as a simple "go/no go" test, but not for sensitivity measurements.
- HDOP is reported in the NMEA-GGA, NMEA-GNS, NMEA-GSA, NMEA-PUBX-POSITION and UBX-NAV-DOP messages.



## <span id="page-7-0"></span>**4 Optional product tests**

These additional tests are not necessary to confirm production functionality, but they may be useful for quality control.

## <span id="page-7-1"></span>**4.1 Clock oscillator stability**

- 1. Connect a 1-channel GNSS simulator to the device under test (DUT) with or without any additional gain (external LNA) and allow enough time for it to acquire the signal.
- 2. Choose a low power level (typically -140 dBm) such that the device reports a C/N0 ratio in the range 30- 34 dBHz.
- 3. Verify that the signal quality indicator reported in the UBX-NAV-SVINFO or UBX-NAV-SAT message (shown in u-center in the figure below as the "Qi" column), remains at a value of 7 for between 30 seconds and one minute. This confirms that the phase noise of the module's clock oscillator is acceptable and the receiver can decode data in the received signals.



**Figure 3: Example of UBX-NAV-SVINFO in u-center Messages View showing Qi column (UBX-NAV-SAT has a similar column)**



## <span id="page-8-0"></span>**4.2 Digital PIO functionality**

The status of the digital PIO pins on the module can be verified by using the UBX-MON-HW message (e.g. with u-center). This message indicates the function and high/low digital level for each signal. The condition of all signals can be checked against the schematic of the OEM product to confirm that all relevant signals are connected and functioning as expected. The host application can exercise input signals and sense output signals, and the resulting condition of the signals can be verified from this message, as shown in u-center in the figure below.

For u-blox 7 and later generations only the status of signals PIO0-PIO16 are useful, all others are reserved for u-blox 6 and can be ignored.



**Figure 4: Example of UBX-MON-HW in u-center Messages View showing status of PIO pins**



## <span id="page-9-0"></span>**Appendix**

## <span id="page-9-1"></span>**A Glossary**

| Abbreviation | Definition                         |
|--------------|------------------------------------|
| DUT          | Device under test                  |
| GLONASS      | Russian satellite system           |
| GNSS         | Global Navigation Satellite System |
| GPS          | Global Positioning System          |
| LNA          | Low Noise Amplifier                |
| SAW          | Surface Acoustic Wave (filter)     |

**Table 1: Explanation of abbreviations used**



## <span id="page-10-0"></span>**Revision history**

| Revision | Date        | Name | Status / Comments |
|----------|-------------|------|-------------------|
| -        | 21-Nov-2016 | iwes | Initial release   |



## <span id="page-11-0"></span>**Contact**

#### **u-blox Offices**

#### **North, Central and South America**

#### **u-blox America, Inc.**

| Phone:  | +1 703 483 3180    |
|---------|--------------------|
| E-mail: | info_us@u-blox.com |

#### **Regional Office West Coast:**

| Phone:  | +1 408 573 3640    |
|---------|--------------------|
| E-mail: | info_us@u-blox.com |

#### **Technical Support:**

Phone: +1 703 483 3185 E-mail: support\_us@u-blox.com

#### **Headquarters Europe, Middle East, Africa**

#### **u-blox AG**

| Phone:   | +41 44 722 74 44   |
|----------|--------------------|
| E-mail:  | info@u-blox.com    |
| Support: | support@u-blox.com |

#### **Asia, Australia, Pacific**

#### **u-blox Singapore Pte. Ltd.**

| Phone:   | +65 6734 3811         |
|----------|-----------------------|
| E-mail:  | info_ap@u-blox.com    |
| Support: | support_ap@u-blox.com |

#### **Regional Office Australia:**

| Phone:   | +61 2 8448 2016       |
|----------|-----------------------|
| E-mail:  | info_anz@u-blox.com   |
| Support: | support_ap@u-blox.com |

#### **Regional Office China (Beijing):**

Phone: +86 10 68 133 545 E-mail: info\_cn@u-blox.com Support: support\_cn@u-blox.com

#### **Regional Office China (Chongqing):**

Phone: +86 23 6815 1588 E-mail: info\_cn@u-blox.com Support: support\_cn@u-blox.com

#### **Regional Office China (Shanghai):**

| Phone:   | +86 21 6090 4832      |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

#### **Regional Office China (Shenzhen):**

Phone: +86 755 8627 1083

E-mail: info\_cn@u-blox.com Support: support\_cn@u-blox.com

#### **Regional Office India:**

Phone: +91 80 4050 9200 E-mail: info\_in@u-blox.com Support: support\_in@u-blox.com

#### **Regional Office Japan (Osaka):**

Phone: +81 6 6941 3660 E-mail: info\_jp@u-blox.com Support: support\_jp@u-blox.com

#### **Regional Office Japan (Tokyo):**

Phone: +81 3 5775 3850 E-mail: info\_jp@u-blox.com Support: support\_jp@u-blox.com

#### **Regional Office Korea:**

Phone: +82 2 542 0861 E-mail: info\_kr@u-blox.com Support: support\_kr@u-blox.com

#### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 E-mail: info\_tw@u-blox.com Support: support\_tw@u-blox.com