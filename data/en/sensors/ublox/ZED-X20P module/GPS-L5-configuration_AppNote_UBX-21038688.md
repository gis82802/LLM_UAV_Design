

# **GPS L5 configuration**

**GNSS receiver handling of GPS L5 health status**

**Application note**

#### **Abstract**

This document provides options and guidelines for configuring the receiver so that it ignores the broadcast GPS L5 health flag and overrides it with the respective GPS L1 signal health flag of the same satellite.

This document applies to u-blox GNSS receivers with GPS L5 support.





## <span id="page-1-0"></span>**Document information**

| Title                  | GPS L5 configuration                           |             |
|------------------------|------------------------------------------------|-------------|
| Subtitle               | GNSS receiver handling of GPS L5 health status |             |
| Document type          | Application note                               |             |
| Document number        | UBX-21038688                                   |             |
| Revision and date      | R03                                            | 20-Jul-2023 |
| Disclosure restriction | C1-Public                                      |             |

This document applies to u-blox GNSS receivers with GPS L5 support.

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.



<span id="page-2-0"></span>

| Document information2                     |
|-------------------------------------------|
| 3                                         |
| 4                                         |
| Background4                               |
| Solution 4                                |
| Setting the required configuration5       |
| u-blox products5                          |
| Using u-center to send binary strings 5   |
| Using u-center 2 to send binary strings 6 |
| 8                                         |
| 8                                         |
| Revision history8                         |
| Contact8                                  |
|                                           |



## <span id="page-3-0"></span>**1 Overview of GPS L5 signal health status**

L5 is the third civilian GPS signal, designed to meet the demanding requirements of many highperformance applications. It features higher power, greater bandwidth, and an advanced signal design. L5 provides the most advanced civilian GPS signal to users worldwide.

Broadcasting of Civil Navigation (CNAV) messages on the L5 signal began in April 2014. At the time of writing, GPS L5 signals remain [pre-operational](https://www.gps.gov/systems/gps/modernization/civilsignals/) and should be employed at the user's own risk until declared operational.

**⚠** Pre-operational GPS L5 signals should not be used for safety-of-life or other critical purpose.

Pre-operational signals are set unhealthy until sufficient monitoring capability is established and as such are not used by u-blox receivers as a default. GPS L5 signals are currently broadcasted by 18 GPS satellites (as of June 15, 2023).

## <span id="page-3-1"></span>**2 Background**

GPS L5 signals are broadcasted as unhealthy. At the same time, the user application may have interest in evaluating these signals and be ready for when they become fully operational.

This is an operational issue concerning the satellites / space segment and not a limitation or specific configuration of u-blox products.

With this unhealthy status being broadcasted, it is difficult to assess the signal performance for evaluation and testing purposes. This calls for a solution to have a configuration setting to overcome the GPS L5 unhealthy status to interested customers.

### <span id="page-3-2"></span>**2.1 Solution**

The current solution is to configure the receiver to ignore the GPS L5 signal health status and override it with the respective GPS L1 signal health status of the same satellite, as explained in section [3.](#page-4-0)

**⚠** Customers who choose to ignore the GPS L5 signal health status in their production system do so at their own risk and must be fully aware of the implications. The system should also include a mechanism to revert to the mode where the L5 signal health status is acknowledged.

u-blox does not recommended to use these configurations in safety-of-life or other critical systems.



## <span id="page-4-0"></span>**3 Setting the required configuration**

The binary UBX configuration message enables configuration of the receiver behavior with respect to the GPS health status. The configuration can be stored in RAM, BBR (battery-backed RAM), and flash.

Writing to RAM ensures the UBX messages are taken into use immediately. Writing to BBR allows the UBX message to be carried out at next power-on if battery backup is maintained.

Writing to flash ensures the UBX message is taken into use at every startup until the firmware is replaced in flash.

#### <span id="page-4-1"></span>**3.1 u-blox products**

The receiver does not use unhealthy signals for navigation by default. To ignore the GPS L5 signal health status and override it with the respective GPS L1 signal health status, the following UBX binary strings can be used.

| Configuration layer | UBX messages                                       |
|---------------------|----------------------------------------------------|
| RAM                 | B5 62 06 8A 09 00 00 01 00 00 01 00 32 10 01 DE ED |
| BBR                 | B5 62 06 8A 09 00 00 02 00 00 01 00 32 10 01 DF F5 |
| Flash               | B5 62 06 8A 09 00 00 04 00 00 01 00 32 10 01 E1 05 |

**Table 1: UBX binary string to override GPS L5 health status with GPS L1 health status**

To revert to default behavior, send

| Configuration layer | UBX messages                                       |
|---------------------|----------------------------------------------------|
| RAM                 | B5 62 06 8A 09 00 00 01 00 00 01 00 32 10 00 DD EC |
| BBR                 | B5 62 06 8A 09 00 00 02 00 00 01 00 32 10 00 DE F4 |
| Flash               | B5 62 06 8A 09 00 00 04 00 00 01 00 32 10 00 E0 04 |

**Table 2: UBX binary strings to revert the GPS L5 health status monitoring to default**

To confirm that the above UBX messages are sent successfully to the receiver, check that you receive a UBX-ACK-ACK message afterwards.

#### <span id="page-4-2"></span>**3.2 Using u-center to send binary strings**

You can use the u-center GNSS evaluation software for Windows to send the binary command strings to the receiver for u-blox F9 products. u-center is available from u-blox website at [https://www.u](https://www.u-blox.com/en/product/u-center)[blox.com/en/product/u-center.](https://www.u-blox.com/en/product/u-center)

To send the binary command strings to the receiver, first open the Messages View in u-center by pressing F9 or by selecting "Messages View" under "View" menu. Then select CUSTOM message type as shown in Figure 1, paste the binary command string to the window, and finally press "Send" at the bottom of the window.







**Figure 1: u-center user interface for sending binary strings**

#### <span id="page-5-0"></span>**3.3 Using u-center 2 to send binary strings**

You can use the u-center 2 GNSS evaluation software for Windows to send the binary command strings to the receiver for u-blox F10 products. u-center 2 is available from u-blox website at [https://www.u-blox.com/en/u-center-2.](https://www.u-blox.com/en/u-center-2)

To send the binary command strings to the receiver, first open the "Tools and Services" on the left in u-center 2 as shown in Figure 2. Then select "Hex utilities", paste the binary command string to the window, acknowledge that the user is aware of the implications, and finally press the "Send" bottom.



|                      | U u-center 2 - ver -23.07.66290-rc<br>Workspace<br>ExplorerKit                                                                                                                                               | $\triangleright$ Play log                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | $\circledcirc$ Reco |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| 0                    | <b>Tools and Services</b><br>$\times$                                                                                                                                                                        | $+$<br>Consoles $\times$<br>Views $\times$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                     |
| Ф<br>$^{\circ}$<br>甴 | <b>Services</b><br>AssistNow Offline<br>∾<br>AssistNow Online<br>⌒<br><b>Tools</b><br>Convert Log to KML<br>O<br>O<br>Firmware update<br>且<br><b>Hex utilities</b><br>$\overline{11}$<br>Current measurement | $O \times$<br><b>Map View</b><br><b>Satellite Position View</b><br>$\circ$<br>$\pmb{\times}$<br><b>GNSS</b> constellation<br>GPS (G)<br>0/9<br>٠<br>SBAS (S)<br>0/0<br>$\circledcirc$<br>$\Box$ Galileo (E)<br>O/O<br><b>Hex utilities</b><br>Device - COM6<br>Send raw data<br>Send UBX message<br><b>Enter hex codes</b><br>B5 62 86 8A 89 88 88 81 88 88 81 88 32 18 81 DE ED<br>Caution! Risk of device damage. Before configuring the device, check the product<br>$\checkmark$<br>Send<br>specification and ensure the configuration data is correct to avoid permanently<br>changing the receiver's configuration. | $\times$            |
|                      |                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                     |

**Figure 2: u-center 2 user interface for sending binary strings**



## <span id="page-7-0"></span>**Appendix**

## <span id="page-7-1"></span>**A Glossary**

| Abbreviation | Definition                                                     |
|--------------|----------------------------------------------------------------|
| ACK          | UBX message received and executed acknowledge                  |
| BBR          | Battery Backed RAM                                             |
| Flash        | EEPROM (electronically erasable programmable read-only memory) |
| RAM          | Random Access Memory                                           |

**Table 3: Explanation of the abbreviations and terms used**

## <span id="page-7-2"></span>**Revision history**

| Revision | Date       | Name | Comments                                 |
|----------|------------|------|------------------------------------------|
| R01      | 15-09-2021 | apai | Initial release                          |
| R02      | 20-07-2023 | angi | Editorial and added u-center screenshots |
| R03      | 04-09-2023 | angi | Include F10 products and u-center 2      |

## <span id="page-7-3"></span>**Contact**

For further support and contact information, visit us at [www.u-blox.com/support.](http://www.u-blox.com/support)