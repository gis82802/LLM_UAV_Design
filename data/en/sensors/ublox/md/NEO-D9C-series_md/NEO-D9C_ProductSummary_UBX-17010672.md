# **NEO-D9C** Product summary

# **u-blox QZSS L6 correction data receiver**

## **Easy access to Japan's high precision correction services**

- Grants access to the free CLAS correction service
- Ready for QZSS MADOCA correction service
- Enables GNSS accuracy down to centimeter level in Japan
- Easy and seamless integration with u-blox F9 receivers

12.2 × 16.0 × 2.4 mm



**Standard**



**Automotive**

## **Product description**

NEO-D9C is a satellite receiver for QZSS L6 high precision GNSS correction services - CLAS and MADOCA. It decodes the satellite signals and outputs a correction stream, enabling a high precision GNSS receiver to reach accuracies down to centimeter level. Depending on the receiver used, preprocessing on an external host might be needed.

NEO-D9C can easily be integrated with high precision GNSS receivers from the u-blox F9 platform portfolio, for a complete solution with little design effort. It grants access to the CLAS augmentation for a free lifetime operation of high precision positioning or a navigation system.

The NEO-D9C ensures high availability of the position output by decoding CLAS data from two QZSS satellites in parallel. By tracking all visible QZSS satellites, NEO-D9C can automatically select the optimal satellites used for the best access to a continuous CLAS service.

NEO-D9C implements u-blox security principles and advanced security features, including signature and anti-jamming mechanisms, thus allowing reliable GNSS positioning in enduser products.

#### **Supporting u-blox receivers**

u-blox F9 GNSS receivers support NEO-D9C and the CLAS service. For more information about the u-blox F9 products, refer to the u-blox website.

#### **About Quasi-Zenith Satellite System (QZSS)**

QZSS is a Japanese satellite positioning system. With satellites in quasi-zenith orbits, three satellites are visible at all times from locations in the Asia-Ocenia region.

#### **About Centimeter Level Augmentation Service (CLAS)**

CLAS provides high-accuracy augmentation to GNSS receivers and is provided for free. The CLAS service is transmitted on the L6 band. The CLAS service adopts a State Space Representation (SSR) of GNSS errors where each individual error source is described separately. The CLAS service is available over mainland Japan.

|                             | NEO-D9C-00A | NEO-D9C-00B |
|-----------------------------|-------------|-------------|
| Grade                       |             |             |
| Automotive                  | •           |             |
| Professional<br>Standard    |             | •           |
| GNSS                        |             |             |
| QZSS L6 band                | •           | •           |
| Concurrent signals          | 2           | 2           |
| Interfaces                  |             |             |
| UART                        | 2           | 2           |
| USB                         | 1           | 1           |
| SPI                         | 1           | 1           |
| DDC (I2C compliant)         | 1           | 1           |
| Features                    |             |             |
| Programmable (flash)        | •           | •           |
| Additional SAW filter       | •           | •           |
| RTC crystal                 | •           | •           |
| Oscillator                  | T           | T           |
| Active antenna / LNA supply | •           | •           |
| Power supply                |             |             |
| 2.7 V – 3.6 V               | •           | •           |
|                             |             |             |

T = TCXO



# **NEO-D9C**



### **Features**

| Receiver type                  | u-blox D9 engine<br>QZSS L2C and L6 receiver                    |                      |  |
|--------------------------------|-----------------------------------------------------------------|----------------------|--|
| Time-to-first-frame Cold start | Hot start                                                       | 18 s<br>3 s          |  |
| Acquisition<br>sensitivity     | Cold start<br>Hot start                                         | -137 dBm<br>-154 dBm |  |
| Oscillator                     | TCXO                                                            |                      |  |
| Frequency band                 | 1227.60 MHz +/- 5 MHz and<br>1278.75 MHz +/- 5 MHz              |                      |  |
| Memory                         | Flash                                                           |                      |  |
| Supported antennas Active      |                                                                 |                      |  |
| Anti-jamming                   | Active CW detection and removal<br>Onboard SAW band pass filter |                      |  |

#### **High precision GNSS architecture**



#### **Interfaces**

| Serial interfaces | 2 UART<br>1 USB<br>1 SPI<br>1 DDC (I2C compliant) |
|-------------------|---------------------------------------------------|
| Protocols         | UBX                                               |
| Digital I/O       | 1 EXTINT input for Wakeup                         |
|                   |                                                   |

#### **Electrical data**

| Supply voltage | 2.7 V to 3.6 V                             |
|----------------|--------------------------------------------|
|                | Power consumption 55 mA at 3.0 V (average) |

#### **Package**

| 24-pin LCC (Leadless Chip Carrier) |  |
|------------------------------------|--|
| 12.2 x 16.0 x 2.4 mm, 1.6 g        |  |

#### **Environmental data, quality & reliability**

|                                     | NEO-D9C-00A                                                              | NEO-D9C-00B                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Operating temp.                     | −40 °C to +105 °C                                                        | −40 °C to +85 °C                                                                               |
| Storage temp.                       | −40 °C to +105 °C                                                        | −40 °C to +85 °C                                                                               |
| Qualification                       | to ISO 16750<br>to AEC-Q104                                              | Professional-grade modules qualified according<br>Automotive-grade modules qualified according |
| RoHS compliant (lead-free)          |                                                                          |                                                                                                |
| Green (halogen-free)                |                                                                          |                                                                                                |
|                                     | Manufactured and fully tested in ISO/TS 16949 certified production sites |                                                                                                |
| High vibration and shock resistance |                                                                          |                                                                                                |
|                                     | Based on u-blox chips qualified according to AEC-Q100                    |                                                                                                |
|                                     |                                                                          |                                                                                                |

#### **Related u-blox products and services**

| GNSS products     | ZED-F9P high precision GNSS module<br>ZED-F9R high precision dead reckoning<br>module<br>ZED-F9K high precision dead reckoning<br>module for automotive markets |  |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Location services | PointPerfect GNSS augmentation service                                                                                                                          |  |

#### **Support products**

| Evaluation kits provide a reference design and allow efficient<br>integration and evaluation of u-blox positioning technology. |                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C101-D9C                                                                                                                       | NEO-D9C application board for evaluation<br>of the NEO-D9C as a stand-alone module or<br>combined with a suitable u-blox F9 evaluation<br>board, for example, C099-F9P or C100-F9K |

#### **Product variants**

| NEO-D9C-00A | QZSS L6 receiver, automotive grade   |
|-------------|--------------------------------------|
| NEO-D9C-00B | QZSS L6 receiver, professional grade |

#### **Further information**

For contact information, see **[www.u-blox.com/contact-u-blox](http://www.u-blox.com/contact-u-blox).** For more product details and ordering information, see the product data sheet.

#### **Legal Notice:**

u-blox reserves all rights to this document and the information contained herein. Products, names, logos and designs described herein may in whole or in part be subject to intellectual property rights. Reproduction, use, modification or disclosure to third parties of this document or any part thereof without the express permission of u-blox is strictly prohibited.

The information contained herein is provided "as is". No warranty of any kind, either express or implied, is made in relation to the accuracy, reliability, fitness for a particular purpose or content of this document. This document may be revised by u-blox at any time. For most recent documents, please visit www.u-blox.com. Copyright © 2021, u-blox AG