

# **F9 series Galileo configuration**

### **Addressing GAL eccentricity**

**Application note**



### **Abstract**

This application note explains how to disable Galileo E14 and E18 from being used by the ZED-F9 series receivers. These satellites exhibit eccentric orbits, which might affect u-box high precision receivers using RTCM3 corrections.





### <span id="page-1-0"></span>**Document information**

| Title                  | F9 series Galileo configuration |             |
|------------------------|---------------------------------|-------------|
| Subtitle               | Addressing GAL eccentricity     |             |
| Document type          | Application note                |             |
| Document number        | UBX-21000979                    |             |
| Revision and date      | R03                             | 25-Mar-2021 |
| Disclosure restriction | C1-Public                       |             |

#### This document applies to the following products:

| Product name    | Type number         | Firmware version | PCN reference |
|-----------------|---------------------|------------------|---------------|
| ZED-F9P         | ZED-F9P-01B-01      | HPG 1.00         | N/A           |
|                 | ZED-F9P-02B-00      | HPG 1.10         |               |
|                 |                     | HPG 1.11         |               |
|                 |                     | HPG 1.12         |               |
|                 |                     | HPG 1.13         |               |
| ZED-F9H         | ZED-F9H-00B-01      | HDG 1.12         |               |
|                 | ZED-F9H-01B-00      | HDG 1.13         |               |
| ZED-F9K         | ZED-F9K-01B-01      | LAP 1.01         | N/A           |
|                 |                     | LAP 1.20         |               |
| ZED-F9R         | ZED-F9R-00B-00      | HPS 1.00         | N/A           |
|                 | ZED-F9R-01B-00      | HPS 1.20         |               |
| UBX-F9940-KA-DR | UBX-F9940-KA-C1003A | LAP 1.10         | N/A           |
|                 |                     | LAP 1.20         |               |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.



<span id="page-2-0"></span>

| Document information2                  |  |
|----------------------------------------|--|
| Contents 3                             |  |
| 1<br>Overview of Galileo E14 and E18 4 |  |
| 2<br>Background and symptoms 4         |  |
| 2.1<br>Solution 4                      |  |
| 3<br>Setting required configuration 5  |  |
| 3.1<br>List of UBX message options5    |  |
| Appendix 6                             |  |
| A<br>Glossary 6                        |  |
| Related documentation 7                |  |
| Revision history7                      |  |
| Contact8                               |  |
|                                        |  |



### <span id="page-3-0"></span>**1 Overview of Galileo E14 and E18**

In 2014 Galileo launched two satellites, E14 and E18, that follow very elliptical orbits, unlike other GNSS satellites which follow almost circular orbits. In comparison to other satellites, the elliptical orbits make the two satellites move differently across the sky.

At the time of writing, these two satellites are marked as unhealthy and as such not used by u-blox receivers.

u-blox recommends applying the configuration instructed in this application note to avoid any problems in the future if the status of the satellites is changed to healthy.

### <span id="page-3-1"></span>**2 Background and symptoms**

During the time when Galileo E14 and E18 were set healthy, it was noticed that u-blox high precision receivers using RTCM3 corrections were affected.

The typical behavior seen was a degraded position accuracy. The errors were in the order of 2 – 20 cm. The problem could occur during periods when one of the GAL E14/E18 satellites was tracked with a very high elevation angle, when it was one of the highest satellites on the sky. This was typically observed 1 - 3 times per day and could last for up to an hour.

### <span id="page-3-2"></span>**2.1 Solution**

The current solution is to configure the receiver to not acquire and track these two satellites, E14 and E18, as explained below.

Again, u-blox recommends applying the configuration instructed in this application note to avoid any problems in the future if the status of the satellites is changed to healthy.

In the future, it will be possible to update the receiver firmware to again make full use of these two satellites.



### <span id="page-4-0"></span>**3 Setting required configuration**

The binary message to disable the use of these two satellites is configured and can be stored in RAM, BBR (battery-backed RAM), and flash.

Writing to RAM will ensure the UBX messages are taken into use immediately. Writing to BBR will allow the UBX message to be carried out at next power on if battery backup is maintained.

Writing to flash will ensure the UBX message will be taken into use at every startup until the firmware is replaced in flash.

**☞** The UBX message will be different based on the firmware version the module is running. Check the required UBX message in the tables below:

### <span id="page-4-1"></span>**3.1 List of UBX message options**

To store the UBX message to disable the satellites in your selected storage section, send the listed UBX message.

| Configuration layer | UBX messages                                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------------|
| RAM                 | B5 62 06 8A 1B 00 00 01 00 00 08 00 C6 20 01 09 00 C6 30 FF 02 0B 00 C6 50 00 40 04 00 00<br>00 00 00 00 5E |
| BBRAM               | B5 62 06 8A 1B 00 00 02 00 00 08 00 C6 20 01 09 00 C6 30 FF 02 0B 00 C6 50 00 40 04 00 00<br>00 00 00 01 78 |
| Flash               | B5 62 06 8A 1B 00 00 04 00 00 08 00 C6 20 01 09 00 C6 30 FF 02 0B 00 C6 50 00 40 04 00 00<br>00 00 00 03 AC |

HPG 1.12, HDG 1.12, LAP 1.01, HPS 1.00 and earlier firmware:

#### HPG 1.13, HDG 1.13, LAP 1.20, HPS 1.20 firmware:

| Configuration layer | UBX messages                                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------------|
| RAM                 | B5 62 06 8A 1B 00 00 01 00 00 08 00 C6 20 01 09 00 C6 30 FF 02 0B 00 C6 50 00 20 02 00 00<br>00 00 00 DE 72 |
| BBRAM               | B5 62 06 8A 1B 00 00 02 00 00 08 00 C6 20 01 09 00 C6 30 FF 02 0B 00 C6 50 00 20 02 00 00<br>00 00 00 DF 8C |
| Flash               | B5 62 06 8A 1B 00 00 04 00 00 08 00 C6 20 01 09 00 C6 30 FF 02 0B 00 C6 50 00 20 02 00 00<br>00 00 00 E1 C0 |

**Table 1: UBX message for selected configuration layer**

- **☞** Check that you have received an ACK after the UBX message is sent.
- **☞** Refer to the ZED-F9P interface description [\[1\],](#page-6-2) ZED-F9K interface description [\[2\],](#page-6-3) ZED-F9R interface description [\[3\],](#page-6-4) ZED-F9H interface description [\[5\],](#page-6-5) UBX-F9940-KA-DR interface description [\[4\].](#page-6-6)



## <span id="page-5-0"></span>**Appendix**

### <span id="page-5-1"></span>**A Glossary**

| Abbreviation | Definition                                                     |  |
|--------------|----------------------------------------------------------------|--|
| ACK          | UBX message received and executed acknowledge                  |  |
| BBR          | Battery Backed RAM                                             |  |
| eFuse        | Electrically Programmable Fuse                                 |  |
| Flash        | EEPROM (electronically erasable programmable read-only memory) |  |
| GAL          | Galileo                                                        |  |
| NOFIX        | RTK fixed solution is not achieved                             |  |
| RAM          | Random Access Memory                                           |  |
| RTK          | Real Time Kinematic                                            |  |

**Table 2: Explanation of the abbreviations and terms used**



### <span id="page-6-0"></span>**Related documentation**

- <span id="page-6-2"></span>[1] ZED-F9P interface description, [UBX-18010854](https://www.u-blox.com/en/docs/UBX-18010854)
- <span id="page-6-3"></span>[2] ZED-F9K interface description [UBX-20046191](https://www.u-blox.com/en/docs/UBX-20046191)
- <span id="page-6-4"></span>[3] ZED-F9R interface description [UBX-19056845](https://www.u-blox.com/en/docs/UBX-19056845)
- <span id="page-6-6"></span>[4] UBX-F9940-KA-DR interface description UBX-19028867 (NDA)
- <span id="page-6-5"></span>[5] ZED-F9H interface description[, UBX-19030118](https://www.u-blox.com/en/docs/UBX-19030118)

**☞** For product change notifications and regular updates of u-blox documentation, register on our website, [www.u-blox.com.](http://www.u-blox.com/)

### <span id="page-6-1"></span>**Revision history**

| Revision | Date       | Name       | Comments                                                    |
|----------|------------|------------|-------------------------------------------------------------|
| R01      | 29-01-2021 | ghun       | Initial release                                             |
| R02      | 17-02-2021 | mala       | Added section Galileo update.                               |
| R03      | 25-03-2021 | mala, mstr | Removed section Galileo update and edited chapters 1 and 2. |



### <span id="page-7-0"></span>**Contact**

#### For complete contact information, visit us at [www.u-blox.com.](http://www.u-blox.com/)

#### **u-blox Offices**

#### **North, Central and South America**

#### **u-blox America, Inc.**

Phone: +1 703 483 3180 Email: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Regional Office West Coast:**

Phone: +1 408 573 3640 Email: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Technical Support:**

Phone: +1 703 483 3185 Email: [support@u-blox.com](mailto:support@u-blox.com)

#### **Headquarters Europe, Middle East, Africa**

#### **u-blox AG**

Phone: +41 44 722 74 44 Email: [info@u-blox.com](mailto:info@u-blox.com) Support: [support@u-blox.com](mailto:support@u-blox.com)

#### **Asia, Australia, Pacific**

#### **u-blox Singapore Pte. Ltd.**

Phone: +65 6734 3811 Email: [info\\_ap@u-blox.com](mailto:info_ap@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

#### **Regional Office Australia:**

Phone: +61 3 9566 7255 Email: [info\\_anz@u-blox.com](mailto:info_anz@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

#### **Regional Office China (Beijing):**

Phone: +86 10 68 133 545 Email: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Chongqing):**

Phone: +86 23 6815 1588 Email: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Shanghai):**

Phone: +86 21 6090 4832 Email: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Shenzhen):**

Phone: +86 755 8627 1083 Email: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office India:**

Phone: +91 80 405 092 00 Email: [info\\_in@u-blox.com](mailto:info_in@u-blox.com) Support: [support\\_in@u-blox.com](mailto:support_in@u-blox.com)

#### **Regional Office Japan (Osaka):**

Phone: +81 6 6941 3660 Email: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

#### **Regional Office Japan (Tokyo):**

Phone: +81 3 5775 3850 Email: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

#### **Regional Office Korea:**

Phone: +82 2 542 0861 Email: [info\\_kr@u-blox.com](mailto:info_kr@u-blox.com) Support: [support\\_kr@u-blox.com](mailto:support_kr@u-blox.com)

#### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 Email: [info\\_tw@u-blox.com](mailto:info_tw@u-blox.com) Support: [support\\_tw@u-blox.com](mailto:support_tw@u-blox.com)