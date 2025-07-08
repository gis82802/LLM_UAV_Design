

# **ZED-F9P**

## **Moving base applications**

**Application note**



### **Abstract**

This application note explains how the ZED-F9P and ZED-F9H multi-band GNSS receivers can be employed in applications that require high precision relative position output or heading and attitude information.





## <span id="page-1-0"></span>**Document information**

| Title                  | ZED-F9P-MovingBase_AppNote_UBX-19009093 |             |  |  |
|------------------------|-----------------------------------------|-------------|--|--|
| Subtitle               | Moving base applications                |             |  |  |
| Document type          | Application note                        |             |  |  |
| Document number        | UBX-19009093                            |             |  |  |
| Revision and date      | R03                                     | 14-Sep-2023 |  |  |
| Disclosure Restriction | C1-Public                               |             |  |  |

#### This document applies to the following products:

| Product name | Type number    | Firmware version | RN reference |
|--------------|----------------|------------------|--------------|
| ZED-F9P      | ZED-F9P-01B-01 | HPG1.12          | UBX-19026698 |
| ZED-F9P      | ZED-F9P-02B-00 | HPG1.13          | UBX-20019211 |
| ZED-F9H      | ZED-F9H-01B-00 | HDG1.13          | UBX-20047673 |
| ZED-F9P      | ZED-F9P-04B-00 | HPG1.32          | UBX-22004887 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.





<span id="page-2-0"></span>

| Document information2                                           |  |
|-----------------------------------------------------------------|--|
| Contents 3                                                      |  |
| Introduction4                                                   |  |
| Terminology and fundamentals4                                   |  |
| Real-world applications5                                        |  |
| System-level considerations9                                    |  |
| GNSS antenna considerations for moving base RTK9                |  |
| 2.1.1<br>Ground plane size and shape9                           |  |
| 2.1.2<br>Multipath/obscuration from surrounding structures10    |  |
| Providing corrections between base and rover11                  |  |
| 2.2.1<br>Wired connection between base and rover 12             |  |
| 2.2.2<br>Wireless connection between base and rover 13          |  |
| 2.2.3<br>Testing and debugging RF link application15            |  |
| 2.2.4<br>Improving RF link performance16                        |  |
| Receiver configurations16                                       |  |
| 2.3.1<br>Default 1 Hz navigation rate application 16            |  |
| 2.3.2<br>5 Hz navigation rate application17                     |  |
| Using the heading output20                                      |  |
| Using the EVK-F9P as a moving base application 21               |  |
| Wired UART base and rover 22                                    |  |
| Using the C099-F9P as a moving base application (Deprecated) 23 |  |
| Wired UART base and rover 24                                    |  |
| Related documents  25                                           |  |
| Revision history 25                                             |  |
| Contact 26                                                      |  |



## <span id="page-3-0"></span>**Introduction**

The ZED-F9P and ZED-F9H multi-band GNSS receivers [\[1\]](#page-24-2)[\[2\]](#page-24-3)[\[6\]h](#page-24-4)ave integrated u-blox multi-band RTK technology for centimeter-level accuracy. This application note explains how ZED-F9P and ZED-F9H can be employed in applications that require high precision relative position output or heading and attitude information. This is enabled by the so-called moving base support in the module firmware.

This first section introduces the basic terminology and essential elements of a moving base setup with two or more GNSS receivers and shows some typical application scenarios. Section 2, which makes up the core of this application note, covers in-depth system-level considerations from antenna placement up to module configuration. Finally, we present how a moving base application can be easily set up with the help of the C099-F9P application board.

**☞** ZED-F9H can only be used as a rover and not a base.

## <span id="page-3-1"></span>**Terminology and fundamentals**

RTK technology introduces the concepts of a **base** and a **rover**. In such a setup, the base sends a continuous differential correction data stream (complying with the RTCM 3.3 protocol) to one or more rovers via a communication link. This enables the rover to compute its position relative to the base with high accuracy. The vector (or relative position) between the base and the rover is called the **baseline**.

In the standard RTK mode, the base remains static in a known position, while in the moving base (MB) RTK mode, both base and rover receivers can move. The latter is ideal for applications where the relative position offset between two moving vehicles is required such as, for example, the follow-me feature on a UAV.

The moving base feature also enables derivation of the **vehicle orientation** by mounting two or three GNSS receivers on the same vehicle platform, that is, by fixing the position of the GNSS antennas relative to each other.



#### **Figure 1: Orientation of a vehicle in space**

**☞** Mounting two antennas on the X-axis gives heading and roll information.

**☞** With three antennas you can derive full attitude; heading, roll and pitch.



The **heading** information and **relative position** is output by the rover. See section [2.4](#page-19-0) on the output from ZED-F9P and ZED-F9H rovers.

#### **Using differential correction data for the base receiver**

If the **absolute position** of the rover is required with high precision, the base unit can be provided with correction data as well. See [Figure 2](#page-4-1) for such a setup. This allows the base to enter the **RTK Fixed mode** with the resultant improvement of absolute position accuracy. Without receiving corrections, the base has a standard 3D Fix position accuracy.



#### <span id="page-4-1"></span>**Figure 2: Moving base setup for precise heading and precise absolute position of the rover.**

In [Figure 2,](#page-4-1) the rear antenna is the base antenna, and the front antenna is the rover antenna. Heading is from the base to the rover antenna.

## <span id="page-4-0"></span>**Real-world applications**

Moving base support can be used in a wide area of applications, for example:

- Drone attitude and heading determination.
- Drone "follow me" sport and filming applications.
- Ship heading determination.
- Ship portable pilot units.
- Vehicle heading determination.
- Heavy machinery motion control.
- Farming vehicle heading determination and control.
- Traditional survey with moving base addition.
- Sports data analysis.
- Cellular base station antenna alignment.





**Figure 3: Drone attitude determination – base and rover on the drone**



**Figure 4: Farming application – position and heading, base and rover on the vehicle**



**Figure 5: Drone "follow me" filming – typically only a rover on the drone**





**Figure 6: Heavy machinery control – blade leveling and heading, base and rover on the vehicle**



**Figure 7: Automotive vehicle heading determination – base and rover on the vehicle**



**Figure 8: Antenna pointing systems – base and rover on a single-cell antenna panel**





**Figure 9: Portable ship pilot systems for entering/exiting harbors - base and rover on the ship.**

[Table 1](#page-7-0) describes typical parameters of the above-mentioned applications.

| Application                                                                 | Key data            | Number of<br>GNSS receivers | Baseline length and type    |
|-----------------------------------------------------------------------------|---------------------|-----------------------------|-----------------------------|
| Drone attitude and heading determination                                    | Roll, pitch and yaw | 3                           | Fixed baseline, 20-30 cm    |
| Drone "follow me" sport and filming applications Heading, relative position |                     | 2                           | Several meters              |
| Precise ship navigation                                                     | Heading             | 2                           | Fixed baseline, up to 100 m |
| Automotive vehicle heading determination                                    | Heading             | 2                           | Fixed baseline, 1-3 m       |
| Antenna attitude measurement and control                                    | Heading / attitude  | 2                           | Fixed baseline, 10-50 cm    |

<span id="page-7-0"></span>**Table 1: Typical moving base applications and key characteristics**



## <span id="page-8-0"></span>**System-level considerations**

As outlined in the previous chapter, two or more GNSS receivers (with separate antennas) are required to determine the relative position between the GNSS receivers. This chapter provides recommendations and detailed examples on how to develop high-performance moving base applications with u-blox ZED-F9P and ZED-F9H receivers.

## <span id="page-8-1"></span>**GNSS antenna considerations for moving base RTK**

**☞** The following points only need to be considered if a patch antenna is used and the application has a short baseline and minimal space for ground planes. Typically, these points need to be considered for heading determination in drones and cellular antenna pointing. The use of a helix antenna would be ideal for such applications as they do not require ground planes. Long baselines (meters to kilometers) are not affected.

If used on the same vehicle for heading and precise attitude determination (for example a drone), the antennas should be identical and ideally on an identical ground plane size and shape. In addition, the antennas should be orientated in the same plane.



**Figure 10: Very short baseline, heading application – patch antenna mounting.**

### <span id="page-8-2"></span>**2.1.1 Ground plane size and shape**

In an application where the base and rover are located far from each other, for instance the rover on a drone and the base on a ship, the ground plane shape has much less effect as the baseline is very long – possibly kilometers. Nevertheless, it is still required that each antenna has the minimum ground plane size, except for a helix antenna which does not require a ground plane for good RTK performance.

A minimum ground plane size and uniform shape is required for best performance if using a patch antenna in a heading application on a moving object, such as a drone with a short distance between the antennas. The shorter the distance between the two antennas is, the more critical this becomes. The ground plane shape could distort the antenna phase center offset and create an error in the position. The performance of a patch antenna for good RTK performance is also affected by the size and shape of the ground plane. A helix antenna would prevent such issues.



**Figure 11: Average antenna phase center offset due to ground plane offset.**





**Figure 12: Non-uniform ground plane shape will offset the phase center (image on the left). Uniform circular ground plane (10 cm) provides best accuracy and performance (image on the right).**

### <span id="page-9-0"></span>**2.1.2 Multipath/obscuration from surrounding structures**

Any surrounding structures will cause multipath (causing position error) and obscure the satellites. Therefore, ensure that the GNSS antennas are above any structures that may cause this issue.



Antennas mounted above structure and noise from motors.

**Figure 13: Drone application and recommended position of the GNSS antennas**



Antennas mounted above metal back plane.

**Figure 14: Cellular base station antenna pointing application.**





Antennas mounted up and away from structure.

**Figure 15: Antenna placement in heavy machinery/machine control application**

## <span id="page-10-0"></span>**Providing corrections between base and rover**

The moving base algorithm was optimized for HPG 1.13 and later firmware as well as HDG 1.13. As a result, compared to HPG 1.12 and HDG 1.12, RTCM 4072.1 is no longer needed and the RTCM MSM7 messages can be replaced by RTCM MSM4 messages. Both will help reduce serial communication and RF link load.

For each navigation epoch the base will produce a batch of RTCM 3.3 compliant messages. For operation in default GNSS configuration mode, the recommended list of RTCM messages is:

- RTCM 4072.0 Reference station PVT information
- RTCM 4072.1 Additional reference station information (Only valid with firmware version HPG 1.12)
- RTCM 1074 GPS MSM4
- RTCM 1084 GLONASS MSM4
- RTCM 1094 Galileo MSM4
- RTCM 1124 BeiDou MSM4
- RTCM 1230 GLONASS code-phase biases

If you are already using MSM7 messages in your settings and are running at 1 Hz navigation rate with no issues with the RF or serial link, you can continue using your previous configuration without the RTCM 4072.1 message for HPG 1.13 and HDG 1.13 and later firmware:

- RTCM 4072.0 Reference station PVT information
- RTCM 4072.1 Additional reference station information (Only valid with firmware version HPG 1.12)
- RTCM 1077 GPS MSM7
- RTCM 1087 GLONASS MSM7
- RTCM 1097 Galileo MSM7
- RTCM 1127 BeiDou MSM7
- RTCM 1230 GLONASS code-phase biases

For detailed configuration instructions, refer to the ZED-F9P Integration manual [\[3\]](#page-24-5) section "3.1.5.6 Base and rover configuration for moving base RTK operation". Refer to the ZED-F9H integration manual [\[7\],](#page-24-6) section "3.1.5".

A further benefit of the moving base algorithm optimization done for HPG 1.13 (and later firmware) and HDG 1.13 is that, compared to HPG1.12 or HDG 1.12, the hard timeout thresholds are relaxed. This improves the reliability and stability of the MB RTK solution and allows easier integration of RF links and serial links.

For optimal MB RTK operation, this group of messages should be received at the rover without transmission losses or errors. The size of the messages can vary depending on the number of satellites received and the configured GNSS constellations.



The achievable navigation update rate of the MB RTK solution is limited by the communication link latency. As a rule of thumb, the communication link latency should be less than the desired navigation update period minus 50 ms.

The UART2 interface is recommended as the default RTCM interface. By default, the ZED-F9P and ZED-F9H UART2 is assigned a baud rate of 38400 baud. This will need to be increased for navigation rates above 1 Hz. For the UART interface a speed of 460800 baud is ideal.

### <span id="page-11-0"></span>**2.2.1 Wired connection between base and rover**

For a standard moving platform heading determination application the corrections from the moving base are supplied via a serial port to the rover. This can be on any of the available ports:

- UART1
- UART2
- USB (only via a USB "device host device" implementation)
- I2C (only via an I2C "device host device" implementation)
- SPI (only via an SPI "device host device" implementation)

It is important to ensure that only the RTCM correction data is supplied on the communication interface used between the two units.

No other protocol than RTCM is enabled by default on UART2. No RTCM message is enabled by default to be output on UART2. This allows the UART2, base TX/rover RX between the two devices to be connected without issues such as buffer overflowing or the wrong messages being sent into the rover ZED-F9P or ZED-F9H unit if powered on with default configuration. For example, do not allow NMEA output messages to be fed back into UART2. They are disabled by default. Only enable the required RTCM messages to be output on the base ZED-F9P UART2.

[Figure 16](#page-12-1) shows a high-level schematics diagram of a design where the base and the rover are connected via corresponding UART2 interfaces of the modules.





<span id="page-12-1"></span>**Figure 16: Simplified schematics diagram of a base and a rover (F9P or F9H) connected via their UART2 interfaces.**

**☞** Level converters and buffers may be required on the ZED-F9P or ZED-F9H RX/TX lines to the host. These must be supplied by the ZED VCC to ensure the correct ZED I/O states at power up and power off.

### <span id="page-12-0"></span>**2.2.2 Wireless connection between base and rover**

In some of the moving base applications illustrated before, for example in a ship-to-drone application, both base and rover are moving independently of each other. They are connected via a wireless link.

Typically, this wireless link has a single RX/TX interface. Therefore, we recommend using ZED-F9P or ZED-F9H UART1, as it supports all NMEA, UBX and RTCM 3.3 protocols.

- Stream RTCM data from the ZED-F9P base to the drone.
- From the drone, stream UBX and NMEA back to the host and not to the ZED-F9P base.

The radio system must be capable of supporting the RTCM messages downstream and the NMEA upstream, ensuring that the RTCM message transmission can be completed fast enough to support the desired rover update rate.

The throughput requirements for the wireless link are stricter if the maximum MB navigation rate of 5 Hz (default GNSS systems) is to be supported. In this case, the communication link must be able to stream RTCM messages to the rover with a maximum latency of roughly 150 ms. This link must also be capable to stream back the NMEA/UBX data back to the host at 5 Hz. The amount of UBX



messages and the type of messages (such as UBX debug info) have a drastic effect on the link capacity and latency. Depending on whether the RF link is also expected to carry a user system protocol and other data, this could be more difficult than expected.

2.4 GHz technologies such as Classic Bluetooth® and Wi-Fi are good for relatively short-range applications[1](#page-13-0). They have the RF throughput and low latency capacity as long as any user data does not load the data link to the detriment of the RTCM stream requirements.

Wi-Fi at 2.4 GHz offers good range with a 2.4 GHz single-band antenna due to better gain than a dual band 2.4/5 GHz Wi-Fi antenna. If the UDP protocol is used over the link, it offers the lowest latency and reduced data flow over the link.

Legacy low-power RF devices are usually not suitable as a wireless link due to their limited TX buffer size and real-time link data transfer capacity.

Longer ranges require RF links with greater RF transmit power/ lower frequency, but will need to have the same throughput and latency requirements if running the ZED-F9P or ZED-F9H at 5 Hz navigation rate. In most countries, longer communication ranges require the use of RF links in licensed bands. However, some countries allow much higher TX power on 2.4 GHz and 900 MHz bands than Europe,.

Considering that the minimum baud rate is 38400 baud for a 1 Hz navigation rate application and 460800 baud is recommended for a 5 Hz navigation rate application, this will usually limit the radio technology that can be used as the gross data rate will need to be considerably higher to transfer data forwards and backwards.

Bluetooth LE and Bluetooth 5 are not ideal technologies for the RF link between base and rover considering required throughput and range. Consider these very carefully along with practical testing before implementing these as the RF solution.

[Figure 17](#page-14-1) shows the schema for a ZED-F9P base connected to a ZED-F9P or ZED-F9H rover via a wireless link.

<span id="page-13-0"></span><sup>1</sup> Bluetooth® is a registered trademark of Bluetooth SIG, Inc.





<span id="page-14-1"></span>**Figure 17: Simplified schematics diagram of a base and a rover (F9P or F9H) connected via a wireless link.**

- **☞** Level converters and buffers may be required on the ZED-F9P or ZED-F9H RX/TX lines. These must be supplied by the ZED VCC to ensure the correct ZED-F9P or ZED-F9H I/O states at power up and power off.
- **☞** This circuit assumes the rover is already configured to provide the required output messages for the remote host. If dynamic message selection during use on the rover is required, the base host will need to have a gate to interrupt the RTCM message flow from the base to the rover and insert UBX configuration commands. This will however result in a loss of RTCM messages at the rover during this transfer of commands.

### <span id="page-14-0"></span>**2.2.3 Testing and debugging RF link application**

By definition and operation, an RF link is susceptible to loss of data, fading and limited RF link rate. In addition, the TX/RX buffer size and any existing protocol used has a dramatic effect on actual reception of RTCM messages. Moving baseline applications have more stringent requirements than standard static base RTK applications.



The time-tagged RTCM messages must arrive complete at the rover to be used for an RTK epoch. If running at higher than 1 Hz navigation rate, the latency in the rover receiving a group a valid timetagged messages becomes a factor. This is most evident at 5 Hz navigation rate with default GNSS constellations. The rover RTK solution effectively slows down its navigation rate if the latency is too high. A UART speed of 460800 baud is ideal for this application. However, the effective RF link rate and TX/RX buffer size must be sufficient at this UART speed as the ZED-F9P or ZED-F9H do not support hardware flow control.

It is quite simple to monitor the effective rover navigation rate:

1. UBX-NAV-PVT or NMEA RMC message can be monitored where GPS TOW is updated at the corresponding navigation rate (e.g. for 5 Hz navigation rate, GPS TOW update happens every 200 ms). Any other message could be used, but these are good examples as they should be set to be output at the effective navigation rate. UBX-NAV-RELPOSNED can also be used if it is set to be output at the selected navigation rate.

## <span id="page-15-0"></span>**2.2.4 Improving RF link performance**

To optimize the performance of a wireless base-rover setup, do the following:

- 1. Start by sending the minimum number of messages back from the rover.
- 2. Select 1 Hz navigation rate and check the GPS TOW update rate in the NMEA RMC or UBX-NAV-PVT or UBX-NAV-RELPOSNED message flag fields. Slowly increase the navigation rate if required and check if the GPS TOW update rate is the same as the set navigation rate. If the NMEA RMC or UBX-NAV-PVT output does not match the set navigation rate, the link latency and RF range have issues and some messages can be missing. If the link cannot work as expected with the base and rover near each other, it will not work at real ranges.
- 3. Test the wireless base-rover setup at the expected RF range and environment and monitor it as indicated in step 2. If your expected range is not achieved, ensure that the antennas on the base and the rover have the maximum legal gain for the frequency you are transmitting at and are not obscured in any way. If the range you need is higher than the link can reliably support, another RF technology could be required.
- 4. To reduce RF latency and load, decide on the minimum number of GNSS constellations you need and disable those you can do without. Reducing the GNSS systems being received on the base and rover reduces the number of messages and message contents that need to be transferred. If only GPS is needed, the other systems can be disabled.

## <span id="page-15-1"></span>**Receiver configurations**

### <span id="page-15-2"></span>**2.3.1 Default 1 Hz navigation rate application**

Running at a default 1 Hz navigation rate is the simplest implementation especially when a wireless link is used between base and rover. The minimum baud rate is 38400 baud if using NMEA only and the required RTCM 3.3 compliant messages.

By default, the receivers operate at 1 Hz, therefore no configuration of the navigation rate is required.

- The default UART1/UART2 baud rate of 38400 baud does not need changing.
- Set base ZED-F9P to output the required RTCM messages on UART2.

**☞** The binary messages include writing the configuration to flash for each message.

1. Set the base ZED-F9P UART2 to output the required RTCM messages:

|--|



| CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART2 | 0x20910300 | U1 | 1 (0x1) | 1 | 1 |
|-------------------------------------|------------|----|---------|---|---|
|-------------------------------------|------------|----|---------|---|---|

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 00 03 91 20 01 53 51**

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1074_UART2 | 0x20910360 | U1   | 1 (0x1) | 1   | 1     |
|                                   |            |      |         |     |       |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 60 03 91 20 01 B3 31**

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1084_UART2 | 0x20910365 | U1   | 1 (0x1) | 1   | 1     |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 65 03 91 20 01 B8 4A**

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1094_UART2 | 0x2091036a | U1   | 1 (0x1) | 1   | 1     |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 6A 03 91 20 01 BD 63**

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1124_UART2 | 0x2091036f | U1   | 1 (0x1) | 1   | 1     |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 6F 03 91 20 01 C2 7C**

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1230_UART2 | 0x20910305 | U1   | 1 (0x1) | 1   | 1     |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 05 03 91 20 01 58 6A**

With both the base and the rover having their own antennas connected, the base outputs all the RTCM messages and the rover goes to RTK Fixed mode if the GNSS signal conditions are OK.

The host UART1 interface has additional messages enabled as per the user's requirement. However, the rover must output UBX-NAV-RELPOSNED message to the host for the heading and base line length output.

#### 2. Enable UBX-NAV-RELPOSNED on the rover UART1:

| Key                                | Key ID     | Type | Value   | RAM | FLASH |
|------------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-UBX_NAV_RELPOSNED_UART1 | 0x2091008e | U1   | 1 (0x1) | 1   | 1     |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 8E 00 91 20 01 DE 0B**

**☞** The UART2 interface of ZED-F9P running FW HPG 1.12 and HPG1.13 does not support UBX messages. HPG 1.32 and above supports UBX on UART2.

### <span id="page-16-0"></span>**2.3.2 5 Hz navigation rate application**

Configure the base and rover UART2 baud rate to 460800 baud:

**☞** Set HPG1.32 firmware only to 7 Hz maximum navigation rate.



- Set the navigation rate on the base and rover to 5 Hz (200 ms).
- Set UART1 and UART2 on the base and rover to 460800 baud.
- Enable the required RTCM messages as shown above on the base.
- 1. Configure the base and rover navigation rates:

Send this message to each unit.

| Key           | Key ID     | Type | Value      | RAM | FLASH |
|---------------|------------|------|------------|-----|-------|
| CFG-RATE-MEAS | 0x30210001 | U2   | 200 (0xc8) | 1   | 1     |

**Binary message: b5 62 06 8a 0a 00 00 01 00 00 01 00 21 30 c8 00 b5 81**

#### 2. Configure the base and rover UART1 and UART2 configuration:

Send these messages to base and rover unit.

| Key                | Key ID     | Type | Value               | RAM | FLASH |
|--------------------|------------|------|---------------------|-----|-------|
| CFG-UART1-BAUDRATE | 0x40520001 | U4   | 460800<br>(0x70800) | 1   | 1     |

**Binary message: B5 62 06 8A 0C 00 00 05 00 00 01 00 52 40 00 08 07 00 43 AF**

| Key                | Key ID     | Type | Value               | RAM | FLASH |
|--------------------|------------|------|---------------------|-----|-------|
| CFG-UART2-BAUDRATE | 0x40530001 | U4   | 460800<br>(0x70800) | 1   | 1     |

**Binary message: B5 62 06 8A 0C 00 00 05 00 00 01 00 53 40 00 08 07 00 44 B5**



3. Set the base ZED-F9P UART2 to output the required RTCM messages:

| Key                                 | Key ID     | Type | Value   | RAM | FLASH |
|-------------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART2 | 0x20910300 | U1   | 1 (0x1) | 1   | 1     |

**Binary message: B5 62 06 8A 09 00 00 05 00 00 00 03 91 20 01 53 51**

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1074_UART2 | 0x20910360 | U1   | 1 (0x1) | 1   | 1     |

**Binary message: B5 62 06 8A 09 00 00 05 00 00 60 03 91 20 01 B3 31** 

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1084_UART2 | 0x20910365 | U1   | 1 (0x1) | 1   | 1     |

**Binary message: B5 62 06 8A 09 00 00 05 00 00 65 03 91 20 01 B8 4A** 

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1094_UART2 | 0x2091036a | U1   | 1 (0x1) | 1   | 1     |

**Binary message: B5 62 06 8A 09 00 00 05 00 00 6A 03 91 20 01 BD 63** 

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1124_UART2 | 0x2091036f | U1   | 1 (0x1) | 1   | 1     |

**Binary message: B5 62 06 8A 09 00 00 05 00 00 6F 03 91 20 01 C2 7C** 

| Key                               | Key ID     | Type | Value   | RAM | FLASH |
|-----------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-RTCM_3X_TYPE1230_UART2 | 0x20910305 | U1   | 1 (0x1) | 1   | 1     |

**Binary message: B5 62 06 8A 09 00 00 05 00 00 05 03 91 20 01 58 6A**

With both the base and rover having their own GNSS antennas connected, the base outputs all the RTCM messages and the rover goes to the RTK Fixed mode if GNSS signal conditions are OK.

The host UART1 interface has additional messages enabled as per the user's requirement. However, the rover must output UBX-NAV-RELPOSNED message to the host for the heading and base line length output.

3. Enable UBX-NAV-RELPOSNED on the rover UART1:

| Key                                | Key ID     | Type | Value   | RAM | FLASH |
|------------------------------------|------------|------|---------|-----|-------|
| CFG-MSGOUT-UBX_NAV_RELPOSNED_UART1 | 0x2091008e | U1   | 1 (0x1) | 1   | 1     |

#### **Binary message: B5 62 06 8A 09 00 00 05 00 00 8E 00 91 20 01 DE 0B**

- **☞** The UART2 interface of ZED-F9P running FW HPG 1.13 does not support UBX messages. HPG 1.32 and above supports UBX on UART2.
- **☞** The UART2 interface of the ZED-F9H running FW HDG 1.13 does not support UBX protocol.



## <span id="page-19-0"></span>**Using the heading output**

The heading output is provided in the UBX-NAV-RELPOSNED message by the ZED-F9P and ZED-F9H rover. For details, see the ZED-F9P [\[4\]](#page-24-7) Interface description and the ZED-F9H Interface description [\[5\].](#page-24-8) The ZED-F9P message provides the actual RTK calculated distance between the two antennas and the resultant RTK heading output. The ZED-F9H message outputs a normalized distance (1 m) between the base and rover antennas and the resultant RTK heading output.

For an application where two antennas are mounted on the same moving platform, the precise known distance between the two antennas can be used to validate the MB RTK solution, including the heading output. If the RTK calculated distance does not closely match with the known baseline distance, there is a high probability that ambiguities were fixed wrongly and, therefore, the computed rover relative position and baseline heading are wrong, especially if the distance between the antennas is very short. The ZED-F9H UBX-NAV-RELPOSNED message, normalized distance between base and rover antenna, cannot be used to verify good RTK performance as it is always output as 1 m.

The UBX-NAV-RELPOSNED heading output has no additional low pass filtering. This allows the user application to add additional low pass filtering depending on the application-specific operating conditions and required heading output for the end application.

For example for a cellular base station antenna attitude applications, there is a maximum settling time requirement for any large physical antenna heading change. The low pass filtering can be adjusted to match this to prevent short-term effects on the heading output in the application. Known dynamics of the antenna position changes can also be used to filter out any sudden angular rates.

For automotive applications, a different filtering strategy can be used due to the dynamics and rapidly changing satellite visibility. Urban canyon has the most multi-path and satellite obstruction causing position inaccuracy and it is typical to have angular rates of automobiles in this kind of environment. Sudden, large angular rates should be filtered.



## <span id="page-20-0"></span>**Using the EVK-F9P as a moving base application**

The EVK-F9P application board can be used in a base and rover pair using a wired serial connection for moving base applications.

In addition, the base EVK-F9P can receive RTCM 3.3 compliant correction data to improve absolute accuracy.

For further information see the EVK-F9P User guide [\[10\].](#page-24-9)

For further information on configuration of moving base, see ZED-F9P Integration manual [\[3\].](#page-24-5)



## <span id="page-21-0"></span>**Wired UART base and rover**

If two units are to be located close together for a heading application, the boards can be connected using wires and there is no need for a wireless link.

In this case we connect via the UART1 of the two boards. As one board only transmits and the other one only receives, we can achieve the needed communication by connecting the base TX line to the rover RX line. In addition, we connect the ground between the two boards.

The connections needed are summarized in the table below and illustrated in figure [18.](#page-21-1)

| Base       | Rover     | Remark                                 |
|------------|-----------|----------------------------------------|
| GND pin2   | GND pin 2 | Connects ground between the two boards |
| TXD pin 12 | RXD pin13 | Connects base TX line to rover RX line |

**Table 2: EVK-F9P UART1 wired connection list.**



Base EVK- Rover EVK-

<span id="page-21-1"></span>**Figure 18: Two EVK-F9P application boards connected via UART lines.**



## <span id="page-22-0"></span>**Using the C099-F9P as a moving base application (Deprecated)**

The C099-F9P application board can be used in a base and rover pair using the Wi-Fi or wired serial connection for moving base applications. The ZED-F9H rover firmware is not supported with the C099-F9P.

In addition, the base C099-F9P can receive RTCM 3.3 compliant correction data to improve absolute accuracy.

⚠ C099-F9P is deprecated and there is going to be no more support or development on this application board.

Further resources are listed here:

- 1. Using Wi-Fi base and rover pair is covered in the C099-F9P User guide [\[8\].](#page-24-10)
- 2. The u-blox GitHub repository provides configuration files for moving base:
  - Base ZED-F9P moving base configuration file [\[11\].](#page-24-11)
  - Rover ZED-F9P configuration file [\[12\].](#page-24-12)

Download these files using the u-center View > Generation 9 Configuration View. They cannot be downloaded using the legacy configuration file download.

- 3. The u-blox GitHub repository also provides a more detailed quick guide [\[13\]](#page-24-13) for downloading the moving base configuration files.
- 4. u-center evaluation software [\[14\].](#page-24-14)



## <span id="page-23-0"></span>**Wired UART base and rover**

If two units are to be located close together for a heading application, the boards can be connected using wires and there is no need for a wireless link.

In this case we connect via the UART1 of the two boards. As one board only transmits and the other one only receives, we can achieve the needed communication by connecting the base TX line to the rover RX line. In addition, we connect the ground between the two boards.

The connections needed are summarized in the table below and illustrated in [Figure 19.](#page-23-1)

| Base     | Rover      | Remark                                                                                                                                                                                                                 |
|----------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| J9 pin 2 | J9 pin 1   | Connects base TX line to rover RX line                                                                                                                                                                                 |
| J8 pin 7 | J8 pin 7   | Connects ground between the two boards                                                                                                                                                                                 |
| -        | J18 jumper | Connect a jumper to the jumper header pins marked 4OE_N on the board. This is the<br>second jumper header pin from the top. This jumper is only needed on the rover board,<br>to enable UART1 Rx on the rover ZED-F9P. |

#### **Table 2: C099 UART1 wired connection list.**



Base C099-F9P Rover C099-F9P

#### <span id="page-23-1"></span>**Figure 19: Two C099-F9P application boards connected via UART lines.**

Use the ZED-F9P native USB ports to monitor and log the ZED-F9P modules output.



## <span id="page-24-0"></span>**Related documents**

- <span id="page-24-2"></span>[1] ZED-F9P-02B Data sheet, [UBX-21023276](https://www.u-blox.com/sites/default/files/documents/ZED-F9P-02B_DataSheet_UBX-21023276.pdf)
- <span id="page-24-3"></span>[2] ZED-F9P-04B Data sheet, [UBX-21044850](https://www.u-blox.com/sites/default/files/ZED-F9P-04B_DataSheet_UBX-21044850.pdf)
- <span id="page-24-5"></span>[3] ZED-F9P Integration manual, UBX-18010802
- <span id="page-24-7"></span>[4] HPG1.32 Interface description[, UBX-22008968](https://www.u-blox.com/sites/default/files/documents/u-blox-F9-HPG-1.32_InterfaceDescription_UBX-22008968.pdf)
- <span id="page-24-8"></span>[5] HDG1.13 Interface description, [UBX-19030118](https://content.u-blox.com/sites/default/files/u-blox_ZED-F9H_InterfaceDescription_%28UBX-19030118%29.pdf)
- <span id="page-24-4"></span>[6] ZED-F9H-01B Data sheet, [UBX-21025012](https://www.u-blox.com/sites/default/files/ZED-F9H-01B_DataSheet_UBX-21025012.pdf)
- <span id="page-24-6"></span>[7] ZED-F9H Integration manual, [UBX-19030120](https://www.u-blox.com/sites/default/files/ZED-F9H_IntegrationManual_UBX-19030120.pdf)
- <span id="page-24-10"></span>[8] C099-F9P User guide, [UBX-18063024](https://www.u-blox.com/sites/default/files/documents/C099-F9P-AppBoard_UserGuide_UBX-18063024.pdf)
- [9] ANN-MB Data sheet, [UBX-18049862](https://www.u-blox.com/sites/default/files/documents/ANN-MB_DataSheet_UBX-18049862.pdf)
- <span id="page-24-9"></span>[10] EVK-F9P User guide[, UBX-22038408](https://www.u-blox.com/en/product/evk-f9p?legacy=Current#Documentation-&-resources)
- <span id="page-24-11"></span>[11] [Base ZED-F9P configuration file](https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/F9P%20Base%20moving%20base%20config%20C99.txt)
- <span id="page-24-12"></span>[12] [Rover ZED-F9P configuration file](https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/F9P%20Rover%20config%20C99.txt)
- <span id="page-24-13"></span>[13] Quick guide for downloading the moving base configuration files, [UBX-19046400](https://github.com/u-blox/ublox-C099_F9P-uCS/blob/master/zed-f9p/C099-F9P-Quick-configuration-Moving-base_(UBX-19046400).pdf)
- <span id="page-24-14"></span>[14] [u-center](https://www.u-blox.com/en/product/u-center) evaluation software.

**☞** For regular updates to u-blox documentation and to receive product change notifications, register on our homepage [\(www.u-blox.com\)](http://www.u-blox.com/).

## <span id="page-24-1"></span>**Revision history**

| Revision | Date         | Name | Comments                                                                                                                                                      |
|----------|--------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 16-May-2019  | ghun | Initial release                                                                                                                                               |
| R02      | 05-June-2020 | ghun | Early production information<br>Many updates related to the new firmware, FW 1.00 HPG 1.13                                                                    |
| R03      | 14-Sep-2023  | hdev | Updated sections related to RF link debug and performance. Added section<br>for EVK-F9P moving base application. C099-F9P application board is<br>deprecated. |



## <span id="page-25-0"></span>**Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support.](http://www.u-blox.com/support)