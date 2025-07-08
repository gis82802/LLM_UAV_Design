# **ZED-F9K module** Product summary

## **High precision dead reckoning with integrated IMU sensors**

#### **Reliable lane identification for ADAS applications up to 105 °C**

- Fully integrated dead reckoning RTK solution up to 50 Hz with very low latency
- Multi-band operation for flexibility and security
- Multiple outputs to serve all possible architecture
- Dependable protection level output
- Advanced security by top-notch spoofing & jamming algorithms
- Native support of global PointPerfect augmentation



# 



**Professional**



#### **Product description**

The ZED-F9K-01A module features the u-blox F9 GNSS platform, which provides continuous decimeter-level positioning accuracy for the most challenging automotive use cases. It supports both L1/L2/E5B and L1/L5 bands for maximum flexibility, satellite availability, and security. The sophisticated built-in algorithms cleverly fuse the IMU data, GNSS measurements, wheel ticks, and vehicle dynamics model to identify driving lanes where GNSS alone would fail.

The module natively supports the u-box PointPerfect GNSS augmentation service. It delivers multiple GNSS and IMU outputs in parallel to support all possible architectures, including a 50 Hz sensor-fused solution with very low latency. It also enables advanced real-time applications like augmented reality, while the optimized multi-band and multiconstellation capability maximizes the number of visible satellites even in urban conditions.

The device is a self-contained solution, which provides the best possible system performance to address issues such as latency constraints, RF front-end design issues, or RTK algorithm integration. This eliminates the technical risk and effort of selecting and integrating RF components and third-party libraries, like positioning engines, which helps customers optimize time to market. The u-blox approach also dramatically reduces supply chain complexity during production.

The u-blox position engine incorporates a dependable protection level output and advanced security features including anti-spoofing and anti-jamming. Operation up to 105 ºC makes it possible to integrate the product anywhere in the car without design constraints.

u-blox manufacturing partners use ISO/TS 16949 certified sites and adhere to the latest standards in the automotive industry. Qualification tests are performed as stipulated in the AEC-Q104 standard: "Failure mechanism based stress test qualification for multichip modules (MCM) in automotive applications".

|                        | ZED-F9K |
|------------------------|---------|
| Grade                  |         |
| Automotive             | •       |
| Professional           |         |
| Standard               |         |
| GNSS                   |         |
| GPS / QZSS             | •       |
| GLONASS                | •       |
| Galileo                | •       |
| BeiDou                 | •       |
| NavIC                  | •       |
| Multi-band             | •       |
| Interfaces             |         |
| UART                   | 2       |
| USB                    | 1       |
| SPI                    | 1       |
| DDC (I2C compliant)    | 1       |
| Features               |         |
| Programmable (Flash)   | •       |
| Additional SAW         | •       |
| RTC crystal            | •       |
| Oscillator             | T       |
| OSR correction support | •       |
| PointPerfect support   | •       |
| Timepulse              | 1       |
| Power supply           |         |
| 2.7 V – 3.6 V          | •       |

T = TCXO



### **ZED-F9K module**



| Features              |                                                      |                                                                                                                                                                                 |
|-----------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Receiver type         | 184-channel u-blox F9 engine<br>QZSS L1/L2C, SBAS L1 | Option A: GPS L1/L2C, Galileo E1/E5b,<br>GLONASS L1/L2, BeiDou B1I/B2I,<br>Option B: GPS L1/L5, Galileo E1/E5a,<br>GLONASS L1, BeiDou B1I/B2a,<br>QZSS L1/L5, NavIC L5, SBAS L1 |
| Nav. update rate      | up to 50 Hz                                          |                                                                                                                                                                                 |
| Position accuracy     | RTK                                                  | < 0.2 m + 1 ppm CEP                                                                                                                                                             |
| ADR position error    |                                                      | < 1% of distance travelled without GNSS                                                                                                                                         |
| Convergence time      | RTK                                                  | < 10 s                                                                                                                                                                          |
| Acquisition           | Cold starts<br>Aided starts<br>Reacquisition         | 24 s<br>4 s<br>2 s                                                                                                                                                              |
| Sensitivity           | Tracking & nav. 1<br>Cold starts<br>Hot starts       | -160 dBm<br>-147 dBm<br>-158 dBm                                                                                                                                                |
| Built-in              |                                                      | TCXO, RTC, flash memory, 3D accelerometer,<br>3D gyroscope, diplexer, SAW filters                                                                                               |
| Supported<br>antennas | Active                                               |                                                                                                                                                                                 |

1 Limited by firmware for best DR performance

#### **Software features**

| Anti-jamming  | Advanced anti-jamming algorithms                                     |
|---------------|----------------------------------------------------------------------|
| Anti-spoofing | Advanced anti-spoofing algorithms<br>Sensor based spoofing detection |
| Raw data      | Code and Doppler measurements and IMU data                           |
| Protocols     | NMEA, UBX binary, RTCM version 3.3                                   |

#### **Interfaces**

| Serial interfaces | 2 UART<br>1 USB<br>1 SPI (optional)<br>1 DDC |  |
|-------------------|----------------------------------------------|--|
| Digital I/O       | Configurable timepulse                       |  |
| Timepulse         | Configurable: 0.25 Hz to 10 MHz              |  |
|                   |                                              |  |

#### **Package**

| 54-pin LGA (Land Grid Array) |  |
|------------------------------|--|
| 17 x 22 x 2.4 mm             |  |
|                              |  |

#### **Environmental data, quality & reliability**

| Operating temp.                                                             | −40 °C to +105 °C                                    |
|-----------------------------------------------------------------------------|------------------------------------------------------|
| Storage temp.                                                               | −40 °C to +105 °C                                    |
|                                                                             | RoHS compliant (lead-free, 2015/863/EU)              |
| Green (halogen-free)                                                        |                                                      |
| EU Radio Equipment Directive compliant 2014/53/EU                           |                                                      |
|                                                                             | Module qualification according to AEC-Q104           |
| Manufactured and fully tested in ISO/TS 16949 certified production<br>sites |                                                      |
|                                                                             | Uses u-blox F9 chips qualified according to AEC-Q100 |

#### **Electrical data**

| Supply voltage | 2.7 V to 3.6 V                               |
|----------------|----------------------------------------------|
|                | Power consumption 85 mA @ 3.0 V (continuous) |
| Backup supply  | 1.65 V to 3.6 V                              |

#### **Compatible u-blox products and services**

services

| Products          | NEO-D9S correction receiver                                        |
|-------------------|--------------------------------------------------------------------|
| Location services | AssistNow A-GNSS service<br>PointPerfect GNSS augmentation service |
|                   |                                                                    |
| Support products  |                                                                    |
| EVK-F9DR          | Easy to use evaluation board with various                          |

communication interfaces for correction

#### **Product variants**

| ZED-F9K-01A | u-blox F9 multi-band high precision dead<br>reckoning, automotive grade. L1/L2/E5b or L1/<br>L5 bands, up to 105 °C<br>LAP 1.30 firmware |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| ZED-F9K-02A | u-blox F9 multi-band high precision dead<br>reckoning, automotive grade. L1/L2/E5b or L1/<br>L5 bands, up to 105 °C<br>LAP 1.50 firmware |

#### **Further information**

For contact information, see **www.u-blox.com/contact-u-blox**. For more product details and ordering information, see the product data sheet.

#### **Legal Notice:**

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only. The information contained herein is provided "as is". No warranty of any kind, either

express or implied, is made in relation to the accuracy, reliability, fitness for a particular purpose, or content of this document. This document may be revised by u-blox at any time. For most recent documents and product statuses, please visit www.u-blox.com.