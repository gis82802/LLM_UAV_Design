

## **Information note**

#### **Topic u-blox M9-F9-D9 documentation update**

UBX-23000084 C1-Public

**Author**

Georgi Gorine 13 April 2023

**Date**

Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

# **1 Affected products**

| Product name    | Ordering code       | DS   | Remarks                                         |
|-----------------|---------------------|------|-------------------------------------------------|
| ZED-F9P         | ZED-F9P-01B         | [1]  | High Precision GNSS                             |
| ZED-F9P         | ZED-F9P-02B         | [2]  |                                                 |
| ZED-F9P         | ZED-F9P-04B         | [3]  |                                                 |
| ZED-F9H         | ZED-F9H-01B         | [4]  |                                                 |
| UBX-F9140-KA    | UBX-F9140-KA-C1006A | [5]  |                                                 |
| ZED-F9R         | ZED-F9R-01B         | [6]  | High Precision GNSS,<br>with Dead Reckoning     |
| ZED-F9R         | ZED-F9R-02B         | [7]  |                                                 |
| ZED-F9R         | ZED-F9R-03B         | [8]  |                                                 |
| ZED-F9K         | ZED-F9K-00B         | [9]  |                                                 |
| UBX-F9940-KA-DR | UBX-F9940-KA-C1003A | [10] |                                                 |
| NEO-D9C         | NEO-D9C-00A         | [11] | High Precision GNSS,<br>with correction data    |
| NEO-D9C         | NEO-D9C-00B         | [12] |                                                 |
| NEO-D9S         | NEO-D9S-00A         | [13] |                                                 |
| NEO-D9S         | NEO-D9S-01A         | [14] |                                                 |
| NEO-D9S         | NEO-D9S-00B         | [15] |                                                 |
| ZED-F9T         | ZED-F9T-00B         | [16] | Timing                                          |
| ZED-F9T         | ZED-F9T-10B         | [17] |                                                 |
| NEO-M9N         | NEO-M9N-00B         | [18] | Standard Precision GNSS                         |
| UBX-M9140-KA    | UBX-M9140-KA-C1100A | [19] |                                                 |
| UBX-M9140-KB    | UBX-M9140-KB-C1100A | [20] |                                                 |
| NEO-M9L         | NEO-M9L-01A         | [21] | Standard Precision GNSS,<br>with Dead Reckoning |
| NEO-M9L         | NEO-M9L-20A         | [22] |                                                 |
| UBX-M9140-KA-DR | UBX-M9140-KA-C1009A | [23] |                                                 |
| NEO-M9V         | NEO-M9V-20B         | [24] |                                                 |

### **2 Type**

- ☐ Product status change ☒ Documentation update
- ☐ Hardware/component change ☐ Certification information
- ☐ Firmware/software update ☐ Security advisory
- ☐ Label change ☐ Other

# **3 Description**

The documentation of the affected u-blox generation 9 products listed above has been improved by updating the following data sheet sections:



- 1. Electrical specifications → Absolute maximum ratings: increased the **maximum VCC\_RF output current** (ICC\_RF) (update not applicable to chipsets).
- 2. Electrical specifications → Operating conditions: added a description of the **backup power sequence** and updated the **I\_BCKP typical value** accordingly (update not applicable to D9 products). Added a note on the **current drive/sink** capability of **TIMEPULSE pin**.
- 3. Communication interfaces → SPI: added a table with additional **SPI slave input timing parameters (1 – 12)**.
- 4. Communication interfaces → I2C: restored decimal units in **I2C timings and specifications** table and removed standard mode values.

# **4 Customer impact and recommended action**

It is recommended that customers acquire the latest documentation and check the revision history for details on the changes.

Note that the minimum I2C data setup time for the u-blox 9 receivers is lower than the I2C Fast-mode specification. As a result, the performance of the I2C connection may be influenced by the specific master device and PCB layout.

## **5 Related documentation**

- <span id="page-1-0"></span>[1] ZED-F9P-01B data sheet, [UBX-17051259](https://www.u-blox.com/docs/UBX-17051259)
- <span id="page-1-1"></span>[2] ZED-F9P-02B data sheet, [UBX-21023276](https://www.u-blox.com/docs/UBX-21023276)
- <span id="page-1-2"></span>[3] ZED-F9P-04B data sheet, [UBX-21044850](https://www.u-blox.com/docs/UBX-21044850)
- <span id="page-1-3"></span>[4] ZED-F9H-01B data sheet, [UBX-21025012](https://www.u-blox.com/docs/UBX-21025012)
- <span id="page-1-4"></span>[5] UBX-F9140-KA data sheet, UBX-20053413, NDA required
- <span id="page-1-5"></span>[6] ZED-F9R-01B data sheet, [UBX-19054459](https://www.u-blox.com/docs/UBX-19054459)
- <span id="page-1-6"></span>[7] ZED-F9R-02B data sheet, [UBX-21017486](https://www.u-blox.com/docs/UBX-21017486)
- <span id="page-1-7"></span>[8] ZED-F9R-03B data sheet, [UBX-22024085](https://www.u-blox.com/docs/UBX-22024085)
- <span id="page-1-8"></span>[9] ZED-F9K-00B data sheet[, UBX-17061422](https://www.u-blox.com/docs/UBX-17061422)
- <span id="page-1-9"></span>[10] UBX-F9940-KA-DR data sheet, [UBX-19028878](https://www.u-blox.com/docs/UBX-19028878)
- <span id="page-1-10"></span>[11] NEO-D9C-00A data sheet, UBX-20057098, NDA required
- <span id="page-1-11"></span>[12] NEO-D9C-00B data sheet[, UBX-17053092](https://www.u-blox.com/docs/UBX-17053092)
- <span id="page-1-12"></span>[13] NEO-D9S-00A data sheet, [UBX-21008859](https://www.u-blox.com/docs/UBX-21008859)
- <span id="page-1-13"></span>[14] NEO-D9S-01A data sheet, [UBX-21008860](https://www.u-blox.com/docs/UBX-21008860)
- <span id="page-1-14"></span>[15] NEO-D9S-00B data sheet[, UBX-18012996](https://www.u-blox.com/docs/UBX-18012996)
- <span id="page-1-15"></span>[16] ZED-F9T-00B data sheet[, UBX-18053713](https://www.u-blox.com/docs/UBX-18053713)
- <span id="page-1-16"></span>[17] ZED-F9T-10B data sheet[, UBX-20033635](https://www.u-blox.com/docs/UBX-20033635)
- <span id="page-1-17"></span>[18] NEO-M9N-00B data sheet[, UBX-19014285](https://www.u-blox.com/docs/UBX-19014285)
- <span id="page-1-18"></span>[19] UBX-M9140-KA data sheet, UBX-18021372, NDA required
- <span id="page-1-19"></span>[20] UBX-M9140-KB data sheet, UBX-18020412, NDA required
- <span id="page-1-20"></span>[21] NEO-M9L-01A data sheet[, UBX-20016394](https://www.u-blox.com/docs/UBX-20016394)
- <span id="page-1-21"></span>[22] NEO-M9L-20A data sheet[, UBX-21028129](https://www.u-blox.com/docs/UBX-21028129)
- <span id="page-1-22"></span>[23] UBX-M9140-KA-DR data sheet, UBX-20030337, NDA required
- <span id="page-1-23"></span>[24] NEO-M9V-20B data sheet, [UBX-21029781](https://www.u-blox.com/docs/UBX-21029781)