

#### **Product change note**

#### **Topic Boot loader update**

UBX-19057484

**Author**

#### **Date** Mårten Ström 18 December 2019

Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, visit www.u-blox.com. Copyright© u-blox AG.

# **1 Affected products**

| Product name | Order code   | Type no. (Old) | Type no. (New)  | Remarks |
|--------------|--------------|----------------|-----------------|---------|
| ZED-F9T      | ZED-F9T-00B  | ZED-F9T-00B-00 | ZED-F9T-00B-01  |         |
| RCB-F9T      | RCB-F9T-0    | RCB-F9T-0-00   | RCB-F9T-0-01    |         |
| ZED-F9P      | ZED-F9P-01B  | ZED-F9P-01B-00 | ZED-F9P-01B-01  |         |
| ZED-F9H      | ZED-F9H-00B  | ZED-F9H-00B-00 | ZED-F9H-00B-01  |         |
| NEO-D9C      | NEO-D9C -00B | NEO-D9C-00B-00 | NEO-D9C -00B-01 |         |

# **2 Type of change**

- ☐ Hardware modification
- ☐ Firmware update
- ☐ Documentation update
- ☒ Others; Boot loader update

## **3 Description of change**

Two patches are applied to the boot loader located in module ROM. The first patch ensures correct operation at module startup and prevents a rare event that could result in memory corruption. The second patch ensures security related features are not tempered with.

Product labels are changed with the new product type numbers.

# **4 Schedule**

From the date indicated below the patches will be applied in production to the affected products.

Estimated first shipping date: April 1st, 2020

Samples of the affected product with new type numbers are available as of now (December 18th , 2019) for evaluation purposes.

## **5 Customer impact and recommended action**

- The patches are applied to the boot loader stored in ROM and do not alter the receiver firmware in any way.
- All customers are recommended to migrate to the latest versions as they become available.