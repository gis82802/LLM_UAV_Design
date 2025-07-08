

# **NEO-M8P**

## **u-blox M8 high precision GNSS modules**

**Data sheet**



### **Abstract**

The NEO-M8P module provides centimeter-level GNSS positioning for the mass market with integrated real time kinematics (RTK) for fast time-to-market. This small, light, and energy-efficient RTK module is a complete and versatile solution thanks to its base and rover variants and moving baseline technology for attitude-sensing and follow-me applications.



**[www.u-blox.com](http://www.u-blox.com/)**

UBX-15016656–R11 C1-Public



## <span id="page-1-0"></span>**Document information**

| Title                  | NEO-M8P                               |             |  |  |  |
|------------------------|---------------------------------------|-------------|--|--|--|
| Subtitle               | u-blox M8 high precision GNSS modules |             |  |  |  |
| Document type          | Data sheet                            |             |  |  |  |
| Document number        | UBX-15016656                          |             |  |  |  |
| Revision and date      | R11                                   | 16-Dec-2022 |  |  |  |
| Disclosure restriction | C1-Public                             |             |  |  |  |

| Product status                   | Corresponding content status |                                                                                        |
|----------------------------------|------------------------------|----------------------------------------------------------------------------------------|
| In development /<br>Prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                 |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                     |

#### This document applies to the following products:

| Product<br>name | Type number  | ROM/FLASH version    | PCN/IN reference                     | Content Status         |
|-----------------|--------------|----------------------|--------------------------------------|------------------------|
| NEO-M8P         | NEO-M8P-0-11 | FLASH FW3.01 HPG1.40 | PCN UBX-20013367,<br>IN UBX-22039049 | Production Information |
| NEO-M8P         | NEO-M8P-2-11 | FLASH FW3.01 HPG1.40 | PCN UBX-20013367,<br>IN UBX-22039049 | Production Information |
| NEO-M8P         | NEO-M8P-0-12 | FLASH FW3.05 HPG1.43 | PCN UBX-21035324,<br>IN UBX-22039049 | Production Information |
| NEO-M8P         | NEO-M8P-2-12 | FLASH FW3.05 HPG1.43 | PCN UBX-21035324,<br>IN UBX-22039049 | Production Information |

u-blox or third parties may hold intellectual property rights in the products, names, logos, and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability, and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com. Copyright © u-box AG.



<span id="page-2-0"></span>

| Document information 2                  |  |
|-----------------------------------------|--|
| Contents 3                              |  |
| 1<br>Functional description5            |  |
| 1.1<br>Overview5                        |  |
| 1.2<br>Product features 5               |  |
| 1.3<br>Performance6                     |  |
| 1.4<br>Block diagram 7                  |  |
| 1.5<br>GNSS7                            |  |
| 1.5.1<br>GPS 7                          |  |
| 1.5.2<br>BeiDou 7                       |  |
| 1.5.3<br>GLONASS7                       |  |
| 1.6<br>RTK operation8                   |  |
| 1.6.1<br>Rover navigation modes8        |  |
| 1.6.2<br>Base station mode (NEO-M8P-2)9 |  |
| 1.6.3<br>RTCM message requirements10    |  |
| 1.7<br>Raw data 11                      |  |
| 1.8<br>Assisted GNSS (A-GNSS)11         |  |
| 1.8.1<br>AssistNowTM Online 11          |  |
| 1.9<br>Augmentation systems11           |  |
| 1.9.1<br>Differential GNSS (DGNSS)11    |  |
| 1.10Data logging 12                     |  |
| 1.11Host interface signature 12         |  |
| 1.12Geofencing13                        |  |
| 1.13TIMEPULSE13                         |  |
| 1.14Protocols and interfaces 13         |  |
| 1.15Interfaces14                        |  |
| 1.15.1 UART 14                          |  |
| 1.15.2 USB 14                           |  |
| 1.15.3 SPI 14                           |  |
| 1.15.4 Display Data Channel (DDC)14     |  |
| 1.16EXTINT: External interrupt14        |  |
| 1.17Clock generation14                  |  |
| 1.17.1 Oscillators 14                   |  |
| 1.17.2 Real-time clock (RTC) 15         |  |
| 1.18Power management 15                 |  |
| 1.18.1 Power control15                  |  |
| 1.19Antenna15                           |  |
| 2<br>Pin definition 16                  |  |
| 2.1<br>Pin assignment16                 |  |
| 2.2<br>Pin name changes17               |  |



| 3 | Configuration management 18               |  |  |  |  |  |
|---|-------------------------------------------|--|--|--|--|--|
|   | 3.1<br>Interface selection (D_SEL) 18     |  |  |  |  |  |
| 4 | Electrical specification 19               |  |  |  |  |  |
|   | 4.1<br>Absolute maximum rating19          |  |  |  |  |  |
|   | 4.2<br>Operating conditions19             |  |  |  |  |  |
|   | 4.3<br>Indicative current requirements 20 |  |  |  |  |  |
|   | 4.4<br>SPI timing diagrams 20             |  |  |  |  |  |
|   | 4.4.1<br>Timing recommendations21         |  |  |  |  |  |
|   | 4.5<br>DDC timing 21                      |  |  |  |  |  |
| 5 | Mechanical specifications 22              |  |  |  |  |  |
| 6 | Reliability tests and approvals 23        |  |  |  |  |  |
|   | 6.1<br>Reliability tests23                |  |  |  |  |  |
|   | 6.2<br>Approvals23                        |  |  |  |  |  |
| 7 | Product handling and soldering 24         |  |  |  |  |  |
|   | 7.1<br>Packaging 24                       |  |  |  |  |  |
|   | 7.1.1<br>Reels 24                         |  |  |  |  |  |
|   | 7.1.2<br>Tapes24                          |  |  |  |  |  |
|   | 7.2<br>Shipment, storage, and handling 25 |  |  |  |  |  |
|   | 7.2.1<br>Moisture sensitivity levels 25   |  |  |  |  |  |
|   | 7.2.2<br>Reflow soldering25               |  |  |  |  |  |
|   | 7.2.3<br>ESD handling precautions 25      |  |  |  |  |  |
| 8 | Default messages  26                      |  |  |  |  |  |
| 9 | Labeling and ordering information  27     |  |  |  |  |  |
|   | 9.1<br>Product labeling27                 |  |  |  |  |  |
|   | 9.2<br>Explanation of codes 27            |  |  |  |  |  |
|   | 9.3<br>Ordering codes27                   |  |  |  |  |  |
|   | Appendix  28                              |  |  |  |  |  |
| A | Glossary  28                              |  |  |  |  |  |
|   | Related documents  29                     |  |  |  |  |  |
|   | Revision history  29                      |  |  |  |  |  |
|   | Contact 30                                |  |  |  |  |  |



## <span id="page-4-0"></span>**1 Functional description**

### <span id="page-4-1"></span>**1.1 Overview**

The NEO-M8P modules combine the high-performance u-blox M8 positioning engine with u-blox's real time kinematic (RTK) technology. NEO-M8P provides centimeter-level GNSS performance designed to meet the needs of unmanned vehicles and other machine control applications requiring accurate guidance.

u-blox's RTK technology introduces the concept of a "rover" (NEO-M8P-0) and a "base" (NEO-M8P-2) on the M8 platform for cm-level accuracy in clear-sky environments. The base module sends corrections via the RTCM protocol to the rover module via a communication link, enabling the rover to output its position relative to the base at centimeter-level accuracies. The NEO-M8P is ideal for applications requiring vehicles to move faster and more accurately, operate more efficiently, and automatically return to base platforms. Such applications include UAV, unmanned vehicles (for example, robotic lawn mowers), and Precision Agriculture guidance.

The NEO-M8P modules enable the system integrator to access u-blox's complete end-to-end RTK solution including the stationary "survey-in" functionality that is designed to reduce the setup time and increase the flexibility of the application. The NEO‑M8P includes moving baseline (MB) support, allowing both base and rover to move while computing a centimeter-level accurate position between them. A moving baseline is ideal for UAV applications where the UAV is programmed to follow its owner, or to land on a moving platform. It is also well suited to attitude sensing applications where both base and rover modules are mounted on the same moving platform and the relative position is used to derive attitude information for the vehicle or tool.

NEO-M8P modules are compatible with a wide range of communication technologies (Cellular, Wi-Fi, Bluetooth, UHF) enabling the user to select the communication link best suited to their application. With u‑blox's RTK technology, integration and software development efforts can be reduced, ensuring a minimal cost of ownership.

The u-blox M8 modules use GNSS chips qualified according to AEC‑Q100, they are manufactured in ISO/TS 16949 certified sites, and they are fully tested on a system level. Qualification tests are performed as stipulated in the ISO16750 standard: "Road vehicles – Environmental conditions and testing for electrical and electronic equipment".

The u-blox AssistNow services supply aiding information, such as ephemeris, almanac, and time, reducing the time to first fix significantly. The NEO-M8P operates with the AssistNow Online service which provides current GNSS constellation orbit data to allow a time-to-first-fix in seconds.

| Model     |                         | Category            |                |        | GNSS       |         |         |        |                              | Supply        |      | Interfaces |     |                     | Features             |              |                    |                |           |                         |                             |           | Grade    |              |            |
|-----------|-------------------------|---------------------|----------------|--------|------------|---------|---------|--------|------------------------------|---------------|------|------------|-----|---------------------|----------------------|--------------|--------------------|----------------|-----------|-------------------------|-----------------------------|-----------|----------|--------------|------------|
|           | Standard Precision GNSS | High Precision GNSS | Dead Reckoning | Timing | GPS / QZSS | GLONASS | Galileo | BeiDou | Number of concurrent<br>GNSS | 2.7 V – 3.6 V | UART | USB        | SPI | DDC (I2C-compliant) | Programmable (flash) | Data logging | W<br>Additional SA | Additional LNA | RTK rover | Moving baseline support | Base station with survey-in | Timepulse | Standard | Professional | Automotive |
| NEO-M8P-0 |                         | ●                   |                |        | ●          | ●       |         | ●      | 2                            | ●             | ●    | ●          | ●   | ●                   | ●                    | ●            | ●                  | ●              | ●         | ●                       |                             | 1         |          | ●            |            |
| NEO-M8P-2 |                         | ●                   |                |        | ●          | ●       |         | ●      | 2                            | ●             | ●    | ●          | ●   | ●                   | ●                    | ●            | ●                  | ●              | ●         | ●                       | ●                           | 1         |          | ●            |            |

## <span id="page-4-2"></span>**1.2 Product features**



**☞** Quasi-Zenith Satellite System (QZSS) satellites are tracked and included in raw data output but are not used in navigation or real time kinematics (RTK).

## <span id="page-5-0"></span>**1.3 Performance**

| Parameter                     | Specification             |                                                                    |                                  |              |          |
|-------------------------------|---------------------------|--------------------------------------------------------------------|----------------------------------|--------------|----------|
| Receiver type                 |                           | 72-channel u-blox M8 engine<br>GPS L1C/A, GLONASS L1OF, BeiDou B1I |                                  |              |          |
| Accuracy of timepulse signal  | RMS<br>99%                | 30 ns<br>60 ns                                                     |                                  |              |          |
| Frequency of timepulse signal |                           |                                                                    | 0.25 Hz…10 MHz (configurable)    |              |          |
| Operational limits 1          | Dynamics                  | ≤ 4 g                                                              |                                  |              |          |
|                               | Altitude                  | 50,000 m                                                           |                                  |              |          |
|                               | Velocity                  | 500 m/s                                                            |                                  |              |          |
| Velocity accuracy             |                           | 0.05 m/s                                                           |                                  |              |          |
| Dynamic heading accuracy      |                           | 0.3° 2,3                                                           |                                  |              |          |
|                               |                           |                                                                    | GPS & GLONASS                    | GPS & BeiDou | GPS      |
| Time-to-first-fix 3           | Cold start                |                                                                    | 26 s                             | 28 s         | 29 s     |
|                               | Hot start                 |                                                                    | 1 s                              | 1 s          | 1 s      |
|                               | Aided starts 4            |                                                                    | 2 s                              | 3 s          | 2 s      |
| Sensitivity 5                 | Tracking & Navigation 6   |                                                                    | –160 dBm                         | -160 dBm     | –160 dBm |
|                               | Reacquisition             |                                                                    | –160 dBm                         | -160 dBm     | –160 dBm |
|                               | Cold start                |                                                                    | –148 dBm                         | -148 dBm     | –148 dBm |
|                               | Hot start                 |                                                                    | –157 dBm                         | -157 dBm     | –157 dBm |
| Max navigation update rate    | RTK                       |                                                                    | 5 Hz                             | 5 Hz         | 8 Hz     |
|                               | Moving baseline RTK       |                                                                    | 4 Hz                             | 4 Hz         | 4 Hz     |
|                               | PVT                       |                                                                    | 5 Hz                             | 5 Hz         | 10 Hz    |
|                               | RAW                       |                                                                    | 10 Hz                            | 10 Hz        | 10 Hz    |
| Convergence time7             | RTK                       |                                                                    | <60 s8                           | <60 s8       | 3.5 min8 |
| Horizontal position accuracy  | Standalone 9<br>RTK 6, 10 |                                                                    | 2.5 m CEP<br>0.025 m + 1 ppm CEP |              |          |

**Table 1: NEO-M8P performance in different GNSS modes (default: concurrent reception of GPS and GLONASS)**

<span id="page-5-8"></span>8 Measured with 1 km baseline, patch antennas with ground planes; GPS + BeiDou measured in Singapore

<span id="page-5-9"></span>9 CEP, 50%, 24 hours static, -130 dBm, > 6 SVs

<span id="page-5-10"></span>10 ppm limited to baselines up to 10 km

<span id="page-5-1"></span><sup>1</sup> Assuming Airborne < 4 g platform

<span id="page-5-2"></span><sup>2 50%</sup> at 30 m/s for dynamic operation or assuming a 1 m baseline in MB mode

<span id="page-5-3"></span><sup>3</sup> All satellites at -130 dBm

<span id="page-5-4"></span><sup>4</sup> Dependent on aiding data connection speed and latency

<span id="page-5-5"></span><sup>5</sup> Demonstrated with a good external LNA

<span id="page-5-6"></span><sup>6</sup> Limited by FW for best performance

<span id="page-5-7"></span><sup>7</sup> Depends on atmospheric conditions, baseline length, GNSS antenna, multipath conditions, satellite visibility and geometry



### <span id="page-6-0"></span>**1.4 Block diagram**





## <span id="page-6-1"></span>**1.5 GNSS**

The NEO-M8P positioning modules are concurrent GNSS receivers that can receive and track multiple GNSS systems. NEO-M8P receivers are by default configured for concurrent GPS and GLONASS reception. A combination of GPS and BeiDou can also be used. If RTK update rate is a key factor, the receiver should be configured to use only GPS.

### <span id="page-6-2"></span>**1.5.1 GPS**

The NEO-M8P positioning modules are designed to receive and track the L1C/A signals provided at 1575.42 MHz by the Global Positioning System (GPS).

### <span id="page-6-3"></span>**1.5.2 BeiDou**

The NEO-M8P modules can receive and process the B1I signals broadcast at 1561.098 MHz from the BeiDou Navigation Satellite System. The ability to receive and track BeiDou signals in conjunction with GPS results in higher coverage, improved reliability, and better accuracy.

### <span id="page-6-4"></span>**1.5.3 GLONASS**

The NEO-M8P positioning modules can receive and process GLONASS concurrently with GPS. The NEO-M8P modules are designed to receive and track the L1OF signals GLONASS provides at 1602 MHz + k\*562.5 kHz, where k is the satellite's frequency channel number (k = –7,-6, ..., 5, 6). The ability to receive and track GLONASS L1OF satellite signals allows design of GLONASS receivers where required by regulations.



### <span id="page-7-0"></span>**1.6 RTK operation**



**Figure 2: The M8P modules work as a pair, where the base provides a stream of RTCM messages to the rover**

Under RTK operation, the M8P modules operate as a pair consisting of a rover and a base. The rover needs access to a stream of RTCM 3 messages before it can enter RTK mode and before centimeterlevel accuracies can be reached. The various concepts are explained in detail below.

### <span id="page-7-1"></span>**1.6.1 Rover navigation modes**

In its default configuration the NEO-M8P rover attempts to provide the best positioning accuracy depending on the received correction data. It will enter RTK Float mode as soon as it receives an input stream of RTCM 3 messages. Once the rover has resolved the carrier phase ambiguities, it enters RTK Fixed mode. When the rover is in RTK Fixed mode, it can be expected that the relative accuracies are correct to the cm-level.

It will typically take less than 60 s before the rover has been able to solve the carrier ambiguities and go from RTK Float mode to RTK Fixed mode. The length of this time is referred to as the convergence time.

The rover will attempt to provide RTK fixed mode when 5 or more ambiguities can be estimated. For single-constellation receivers, this means that at least 6 satellites with continuous phase lock need to be visible above the elevation mask (default 10°). Adding satellites from an additional constellation requires at least 2 satellites to form the double difference measurement. Hence, with dual GPS and GLONASS operation, a minimum would consist of 7 satellites (for example, 5 GPS + 2 GLONASS). However, use with additional BeiDou satellites would require 8 satellites (for example, 5 GPS + 3 BeiDou) owing to the two different BeiDou satellite variants.

The rover drops back to RTK Float mode if it loses carrier phase lock on the minimum number of signals needed to maintain RTK Fixed mode. The rover continues to attempt to resolve carrier ambiguities and go back to the RTK Fixed mode once the minimum number of signals has been restored.

If RTCM 3 corrections become unavailable, the rover will run as a standalone standard precision receiver.

The command UBX-CFG-DGNSS can be used to specify that the receiver should stay in RTK Float mode and that it should not attempt to fix integer ambiguities.

The current operation mode is indicated by relevant NMEA and UBX-NAV messages; see u-blox 8 / ublox M8 Receiver Description Including Protocol Specification [\[2\].](#page-28-2)



#### **1.6.1.1 Relative and absolute position**

In RTK mode the rover calculates its position relative to the location of the base position. The relative accuracy can at best be correct to the centimeter level. To get an accuracy that is optimal in an absolute sense, the accuracy of the base station position must be optimized. In the UBX-NAV-RELPOSNED message, the relative position is described in the form of an NED vector.

The absolute accuracy of the base station position will be transferred to the absolute accuracy of a rover operating in differential mode. The NEO-M8P-2 base station module comes with functionalities to ensure the best possible absolute accuracy as described in sectio[n 1.6.2.](#page-8-0)

### <span id="page-8-0"></span>**1.6.2 Base station mode (NEO-M8P-2)**

The NEO-M8P-2 can be set up to operate either as a static or as a mobile base station using the appropriate configuration messages. Prior to use, the NEO-M8P-2 must be configured to produce the required RTCM messages using UBX-CFG-MSG. For static operation, the user has a choice of providing a set of position coordinates explicitly, or by commanding the receiver to produce its own via a self-survey-in function. When either mode is set correctly with a valid position, RTCM reference position messages will be enabled for transmission. When setting for a moving base station mode, the base receiver must ensure that the fixed location mode is disabled and the reference transmits the RTCM 4072 message.

#### **1.6.2.1 Static mode**

The NEO-M8P-2 can be set to use previously surveyed coordinates of the base antenna position. Assuming such coordinates are of highest quality, this method ensures the best absolute accuracy for the rover units. The device outputs RTCM 3 messages when successfully configured in this mode.

This mode is set by using the command UBX-CFG-TMODE3 with receiver mode flag "Fixed Mode". The input WGS84 coordinates can be given in LAT/LON/ALT or ECEF format. Once set, the base station monitors its position to detect any position change from its designated position. Position changes larger than 100 m are reported via a warning message.

The NEO-M8P-2 is capable of self-surveying-in its coordinates in situations where the base antenna is not surveyed using other means. When this mode is employed, the user provides constraints on accuracy and a minimum observation time. The receiver will average its position estimates and output any configured RTCM 3 observation messages until both constraints are met. After this, it will begin operating in static mode and outputs a configured RTCM 3 reference station message.

This mode is set by using the command UBX-CFG-TMODE3 with the mode flag "Survey In" set. The input WGS84 coordinates can be given in LAT/LON/ALT or ECEF format.

#### **1.6.2.2 Moving baseline mode**

The moving baseline (MB) mode differs from the standard RTK operation in that the base station is no longer stationary at a pre-determined location. Both the reference station and rover receivers are allowed to move while computing an accurate vector between the receiver's antennas. To ensure operation in this mode, use the message UBX-CFG-TMODE3 with the mode flag "disabled" set, and ensure that the RTCM 4072 message has been enabled.

This mode enables the calculation of heading on dynamic or static platforms, plus provides a centimeter level accurate 3D vector for use in dynamic positioning examples, for example, the UAV "follow me" feature.

#### **1.6.2.3 Attitude sensing**

Using the moving baseline functionality with fixed base and rover antenna positions on a platform gives the means to estimate the baseline angle with respect to the local datum via the relative position information. This derived angular error will then be proportional to the baseline length[. Figure](#page-9-1) 



[3](#page-9-1) below provides the trend for baseline lengths up to 1 m for a typical (1 sigma) relative position error of 0.8 cm.

**☞** When using similar low-cost patch antennas, it is best to match their orientation to ensure the best error estimate.



**Angle Error vs Baseline length (m)**

<span id="page-9-1"></span>**Figure 3: Estimated angular error for fixed baseline with a typical 1 sigma (0.08 cm) relative position error** 

### <span id="page-9-0"></span>**1.6.3 RTCM message requirements**

In static mode, it is critical that the RTCM observation messages (for example, RTCM 1077 and RTCM 1087, or RTCM 1077 and RTCM 1127) be generated from the same navigation epoch. This might not be the case when the messages are enabled individually at a lower rate than the navigation rate. For this reason, the user should configure the navigation rate of the reference station to be the same as the desired RTCM observation message rate. For this mode, the RTCM standard recommends using 1 Hz.

In moving baseline mode, it is critical that the base sends the position (RTCM 4072) and observation (RTCM 1077 and RTCM 1087, or RTCM 1077 and RTCM 1127) messages at the same rate as its navigation rate. Additionally, to ensure optimal performance, the base and rover receiver should use the same navigation rate.

To ensure GLONASS ambiguity fixing, the reference station must be configured to output RTCM message 1230. This message can be sent at a rate lower than the observation messages as the bias values will be held until a new version of the message is received.

The communication link from the base to the rover must be reliable. Breaks in this communication will result in the rover solution degrading, and eventually falling back to an independent navigation fix, dependent on configuration setting. The RTCM messages output from the base are by default configured to the recommended 1-Hz output rate. Corrections from a static base for GPS/GLONASS (or GPS/BeiDou) at this navigation rate will amount to a load of approximately 500 bytes/s, assuming an update rate of 1 Hz using MSM7 corrections for 20 GPS/GLONASS (or GPS/BeiDou) satellites.

**☞** To reduce the load in static mode it is possible to use MSM4 instead of MSM7 messages. In this case, the load will reduce to approximately 300 bytes/s.

For a base operating at 4-Hz in moving baseline mode, assuming 20 GPS/GLONASS (or GPS/BeiDou) satellites, the load will increase to approximately 2 kB/s.



**☞** In moving baseline mode, it is not possible to use MSM4 messages.

When the module receives a valid stream of RTCM 3 messages, the **RTK\_STAT** status pin is set into an alternating, blinking mode. The **RTK\_STAT** status pin is set active low when the rover module is operating in RTK Fixed mode. The message UBX-RXM-RTCM will echo basic information about received RTCM input messages and can be used to monitor the quality of the communication link.

**☞** For more details, see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specificatio[n \[2\].](#page-28-2)

## <span id="page-10-0"></span>**1.7 Raw data**

The NEO-M8P modules provide raw measurement data for civil L1 band GPS, GLONASS and BeiDou signals including pseudo-range and carrier phase, carrier Doppler frequency and message payloads. The data contained in the UBX-RXM-RAWX message follows the conventions of a multi-GNSS RINEX 3 observation file and includes pseudo-range, carrier phase and Doppler measurements along with measurement quality data. The UBX-RXM-SFRBX message provides the demodulated, paritychecked navigation and signaling message bits for each satellite currently tracked by the receiver.

Raw measurement data are available once the receiver has established data bit synchronization and time-of-week. Message data are available for all signals tracked at a sufficient level to achieve data bit and frame synchronization. For more information, see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\].](#page-28-2)

## <span id="page-10-1"></span>**1.8 Assisted GNSS (A-GNSS)**

Supply of aiding information, such as ephemeris, almanac, approximate position, and time, will reduce the time to first fix significantly and improve the acquisition sensitivity. The NEO-M8P products support the u-blox AssistNow Online and are OMA SUPL-compliant.

### <span id="page-10-2"></span>**1.8.1 AssistNowTM Online**

With AssistNow Online, an internet-connected GNSS device downloads assistance data from u-blox's AssistNow Online Service at system startup. AssistNow Online is network operator-independent and globally available. Devices can be configured to request only ephemeris data for the satellites currently visible at their location, thus minimizing the amount of data transferred.

**☞** For more details, see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\]](#page-28-2) and MGA Services user guide [\[5\].](#page-28-3)

### <span id="page-10-3"></span>**1.9 Augmentation systems**

### <span id="page-10-4"></span>**1.9.1 Differential GNSS (DGNSS)**

When operating in RTK mode RTCM version 3 messages are required and NEO-M8P supports DGNSS according to RTCM 10403.2 [\[6\].](#page-28-4) The RTCM implementation in the rover and base station variants provides decoding of the following RTCM 3.2 messages:

| Message type | Description                 |
|--------------|-----------------------------|
| 1001         | GPS L1 observations         |
| 1002         | GPS L1 observations         |
| 1003         | GPS L1/L2 observations      |
| 1004         | GPS L1/L2 observations      |
| 1005         | Station coordinates         |
| 1006         | Station coordinates         |
| 1007         | Station antenna information |
|              |                             |



| Message type | Description                                             |
|--------------|---------------------------------------------------------|
| 1009         | GLONASS L1 observations                                 |
| 1010         | GLONASS L1 observations                                 |
| 1011         | GLONASS L1/L2 observations                              |
| 1012         | GLONASS L1/L2 observations                              |
| 1074         | MSM4 GPS observations                                   |
| 1075         | MSM5 GPS observations                                   |
| 1077         | MSM7 GPS observations                                   |
| 1084         | MSM4 GLONASS observations                               |
| 1085         | MSM5 GLONASS observations                               |
| 1087         | MSM7 GLONASS observations                               |
| 1124         | MSM4 BeiDou observations                                |
| 1125         | MSM5 BeiDou observations                                |
| 1127         | MSM7 BeiDou observations                                |
| 1230         | GLONASS code-phase biases                               |
| 4072         | Reference station PVT (u-blox proprietary RTCM Message) |

#### <span id="page-11-2"></span>**Table 2: Supported decoding of RTCM 3.2 messages**

The RTCM implementation in the base station (NEO-M8P-2) generates the following RTCM 3.2 output messages:

| Message type | Description                                             |
|--------------|---------------------------------------------------------|
| 1005         | Station coordinates                                     |
| 1074         | MSM4 GPS observations                                   |
| 1077         | MSM7 GPS observations                                   |
| 1084         | MSM4 GLONASS observations                               |
| 1087         | MSM7 GLONASS observations                               |
| 1124         | MSM4 BeiDou observations                                |
| 1127         | MSM7 BeiDou observations                                |
| 1230         | GLONASS code-phase biases                               |
| 4072         | Reference station PVT (u-blox proprietary RTCM Message) |

<span id="page-11-3"></span>**Table 3: Supported encoding of RTCM 3.2 messages**

### <span id="page-11-0"></span>**1.10 Data logging**

The u-blox NEO-M8P receivers can be used in data logging applications. The data logging feature enables continuous storage of position, velocity, and time information to an onboard SQI flash memory. It can also log distance from an odometer function. The logged data can be downloaded from the receiver later for further analysis or for conversion to a mapping tool. For more information, see ublox 8 / u-blox M8 Receiver Description Including Protocol Specificatio[n \[2\].](#page-28-2)

**☞** Note that the location information stored is standard precision only.

### <span id="page-11-1"></span>**1.11 Host interface signature**

The host interface signature mechanism provides protection against unauthorized tampering of the message data sent from the receiver to its host. This increases the robustness of the system against alteration of position and/or time information sent from the receiver (UART). Nominated messages are effectively 'signed' by the receiver using a hashing algorithm to generate a signature message for subsequent checking at the host. A dynamic 'seeding' of the algorithm can be used to detect time



shifted replay attacks on the received message data. See u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\]](#page-28-2) for more information.

## <span id="page-12-0"></span>**1.12 Geofencing**

The geofencing feature allows for the configuration of up to four circular areas (geofences) on the earth's surface. The receiver will then evaluate for each of these areas whether the current position lies within the area or not and signal the state via UBX messaging and PIO toggling. Geofencing can be configured using the UBX-CFG-GEOFENCE message; the geofence evaluation is active whenever there is at least one geofence configured.

The NEO-M8P module uses pin 16 as the **GEOFENCE\_STAT** status pin. This is asserted active low to indicate any position within the combined geofence areas.



**Figure 4: Illustration of the geofence boundary**

### <span id="page-12-1"></span>**1.13 TIMEPULSE**

A configurable timepulse signal is available with the NEO-M8P modules.

The TIMEPULSE output generates pulse trains synchronized with a GPS or UTC time grid with intervals configurable over a wide frequency range. Thus it may be used as a low-frequency time synchronization pulse or as a high-frequency reference signal.

**☞** The NEO-M8P timepulse output is configured using messages for "TIMEPULSE2." This pin has a secondary function during startup (initiation of "SAFEBOOT" mode for firmware recovery) and should not normally be held LO during start-up.

By default the time pulse signal is disabled and, if required, can be activated using UBX-CFG-TP5. For more information, see u-blox 8 / u-blox M8 Receiver Description including Protocol Specification [\[2\].](#page-28-2)

## <span id="page-12-2"></span>**1.14 Protocols and interfaces**

| Protocol                           | Type                                     |
|------------------------------------|------------------------------------------|
| NMEA 0183 V4.0                     | Input/output, ASCII                      |
| (V2.1, V2.3 and V4.1 configurable) |                                          |
| UBX                                | Input/output, binary, u-blox proprietary |
| RTCM 3.2                           | Input, for RTK                           |
| RTCM 3.2                           | Output (NEO-M8P-2 only)                  |

#### **Table 4: Available protocols**

All protocols are available on UART, USB, DDC (I2C-compliant) and SPI. For specification of the various protocols see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\].](#page-28-2)

**☞** When the NMEA protocol is used, version V4.1 is needed to provide all the related RTK information flags.



## <span id="page-13-0"></span>**1.15 Interfaces**

Several interfaces are provided either for data communication or memory access. The embedded firmware uses these interfaces according to their respective protocol specifications.

### <span id="page-13-1"></span>**1.15.1 UART**

The NEO-M8P modules include one UART interface, which can be used for communication to a host. It supports configurable baud rates. For supported baud rates, the u-blox 8 / u-blox M8 Receiver Description Including Protocol Specificatio[n \[2\].](#page-28-2)

**☞** Designs must allow access to the UART and the **SAFEBOOT\_N** function pin for future service, updates, and reconfiguration.

### <span id="page-13-2"></span>**1.15.2 USB**

A USB version 2.0 FS-compatible interface can be used for communication as an alternative to the UART. The pull-up resistor on pin **USB\_DP** is integrated to signal a full-speed device to the host. The **VDD\_USB** pin supplies the USB interface.

u-blox offers USB drivers for use with Windows operating systems. For Windows 7, 8 and 10, there is a sensor driver for users who wish to connect to the Windows sensor platform. For users who wish to connect multiple devices or require a virtual com port, Windows 10 users can use the built-in driver, otherwise u-blox provide a standard USB driver (CDC-ACM) for Windows Vista and Windows 7 and 8. Windows drivers can be downloaded from the u-blox.com web site.

### <span id="page-13-3"></span>**1.15.3 SPI**

The SPI interface is designed to allow communication to a host CPU. The interface can be operated in slave mode only. The maximum transfer rate using SPI is 125 kB/s and the maximum SPI clock frequency is 5.5 MHz. Note that SPI is not available in the default configuration because its pins are shared with the UART and DDC interfaces. The SPI interface can be enabled by connecting **D\_SEL** (pin 2) to ground (see sectio[n 3.1\)](#page-17-1).

### <span id="page-13-4"></span>**1.15.4 Display Data Channel (DDC)**

An I2C-compliant DDC interface is available for communication with an external host CPU or u-blox cellular modules. The interface can be operated in slave mode only. The DDC protocol and electrical interface are fully compatible with Fast-Mode of the I2C industry standard. Since the maximum SCL clock frequency is 400 kHz, the maximum transfer rate is 400 kbit/s.

### <span id="page-13-5"></span>**1.16 EXTINT: External interrupt**

**EXTINT** is an external interrupt pin with fixed input voltage thresholds with respect to VCC. It can be used for control of the receiver or for aiding.

For more information about how to implement and configure these features, see u-blox 8 / u-blox M8 Receiver Description including Protocol Specification [\[2\]](#page-28-2) and the NEO-M8P Hardware Integration Manua[l \[1\].](#page-28-5)

### <span id="page-13-6"></span>**1.17 Clock generation**

### <span id="page-13-7"></span>**1.17.1 Oscillators**

The NEO-M8P GNSS modules incorporate a TCXO for accelerated weak signal acquisition, faster start, and reacquisition. These TCXOs are carefully selected and screened for stability and against frequency perturbations across the full operating range (–40 °C to +85 °C).



### <span id="page-14-0"></span>**1.17.2 Real-time clock (RTC)**

The RTC is driven by a 32-kHz oscillator using an RTC crystal. If the main supply voltage fails, and a battery is connected to V\_BCKP, parts of the receiver switch off, but the RTC still runs providing a timing reference for the receiver. This operating mode is called hardware backup mode, which enables all relevant data to be saved in the backup RAM to allow a hot or warm start later.

### <span id="page-14-1"></span>**1.18 Power management**

u-blox M8 technology offers a power-optimized architecture with built-in autonomous power saving functions to minimize power consumption at any given time. In addition, a high efficiency DC-DC converter is integrated for lower power consumption and reduced power dissipation.

**☞** For more details, see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specificatio[n \[2\].](#page-28-2)

### <span id="page-14-2"></span>**1.18.1 Power control**

A separate battery backup voltage may be applied to the module to retain the current state of the receiver and sustain a low power real-time clock (RTC) while the main supply is removed. This enables faster acquisition and navigation upon start-up.

Alternatively, a configuration command (UBX-CFG-PWR) can be issued to stop the receiver in a similar way to hardware backup mode (see also [1.17.2](#page-14-0) above) while the main supply remains active. This mode is referred to as software backup mode; current consumption in this mode is slightly higher than in hardware backup mode. The receiver will then restart on the next edge received at its UART interface (there will be a delay before any communications are possible).

Se[e Table 11](#page-19-2) for current consumption in backup modes.

### <span id="page-14-3"></span>**1.19 Antenna**

u-blox recommends using an active antenna[11](#page-14-4) or an external LNA with this module to achieve the best performance.

| Parameter                      | Specification        |                                               |  |  |
|--------------------------------|----------------------|-----------------------------------------------|--|--|
| Antenna type                   |                      | Active or passive antenna                     |  |  |
| Active antenna recommendations | Minimum gain         | 15 dB (to compensate signal loss in RF cable) |  |  |
|                                | Maximum gain         | 50 dB                                         |  |  |
|                                | Maximum noise figure | 1.5 dB                                        |  |  |

**Table 5: Antenna specifications for the NEO-M8P modules**

The antenna system should include filtering to ensure adequate protection from nearby transmitters. Take care when selecting antennas placed closed to cellular or Wi-Fi transmitting antennas.

**☞** For guidance on antenna selection, see the NEO-M8P Hardware integration manual [\[1\].](#page-28-5)

<span id="page-14-4"></span><sup>11</sup> For information on using active antennas with NEO-M8P modules, see the NEO-M8P Hardware integration manua[l\[1\].](#page-28-5)



## <span id="page-15-0"></span>**2 Pin definition**

### <span id="page-15-1"></span>**2.1 Pin assignment**

| 13<br>GND                                     | 12<br><b>GND</b>                            |
|-----------------------------------------------|---------------------------------------------|
| 14 LNA EN                                     | RF IN<br>11                                 |
| <b>RTK STAT</b><br>15                         | GND<br>10                                   |
| 16<br><b>GEOFENCE_STAT</b>                    | VCC_RF<br>9                                 |
| <b>NEO-M8P</b><br>17 <sub>2</sub><br>Reserved | 8<br><b>RESET N</b>                         |
| <b>TOP VIEW</b>                               |                                             |
| 18 SDA / SPICS N                              | 7<br><b>VDD_USB</b>                         |
| 19 SCL / SPI CLK                              | USB_DP<br>6                                 |
| 20 TXD / SPI MISO                             | USB_DM<br>-5                                |
| <b>RXD / SPI MOSI</b><br>21                   | <b>EXTINT</b><br>4                          |
| 22 V BCKP                                     | $\overline{\mathbf{3}}$<br><b>TIMEPULSE</b> |
| <b>VCC</b><br>23                              | <b>D_SEL</b><br>$\overline{2}$              |
| 24<br><b>GND</b>                              | SAFEBOOT_N                                  |
|                                               |                                             |

#### **Figure 5: Pin assignment**

| No. | Name              | I/O | Description                                                               |
|-----|-------------------|-----|---------------------------------------------------------------------------|
| 1   | SAFEBOOT_N        | I   | SAFEBOOT_N (for future service, updates, and reconfiguration, leave OPEN) |
| 2   | D_SEL             | I   | Interface select                                                          |
| 3   | TIMEPULSE         | O   | Timepulse (1PPS)                                                          |
| 4   | EXTINT            | I   | External interrupt pin                                                    |
| 5   | USB_DM            | I/O | USB data                                                                  |
| 6   | USB_DP            | I/O | USB data                                                                  |
| 7   | VDD_USB           | I   | USB supply                                                                |
| 8   | RESET_N           | I   | RESET_N                                                                   |
| 9   | VCC_RF            | O   | Output voltage RF section                                                 |
| 10  | GND               | I   | Ground                                                                    |
| 11  | RF_IN             | I   | GNSS signal input                                                         |
| 12  | GND               | I   | Ground                                                                    |
| 13  | GND               | I   | Ground                                                                    |
| 14  | LNA_EN            | O   | Antenna / External LNA power control                                      |
| 15  | RTK_STAT          | O   | RTK status: 0 – Fixed, blinking – receiving RTCM data, 1 – No corrections |
| 16  | GEOFENCE_STAT     | O   | Geofence status, user-defined                                             |
| 17  | Reserved          | -   | Reserved                                                                  |
| 18  | SDA /<br>SPI CS_N | I/O | DDC data if D_SEL =1 (or open)<br>SPI chip select if D_SEL = 0            |
| 19  | SCL /<br>SPI CLK  | I/O | DDC clock if D_SEL =1(or open)<br>SPI clock if D_SEL = 0                  |
| 20  | TxD /<br>SPI MISO | O   | Serial port if D_SEL =1(or open)<br>SPI MISO if D_SEL = 0                 |
| 21  | RxD /<br>SPI MOSI | I   | Serial port if D_SEL =1(or open)<br>SPI MOSI if D_SEL = 0                 |
| 22  | V_BCKP            | I   | Backup voltage supply                                                     |
| 23  | VCC               | I   | Supply voltage                                                            |
| 24  | GND               | I   | Ground                                                                    |

**Table 6: Pinout**





**☞** Do not use pins designated "Reserved". For more information about pinouts, see the NEO-M8P Hardware integration manual [\[1\].](#page-28-5)

### <span id="page-16-0"></span>**2.2 Pin name changes**

Selected pin names have been updated to agree with a common naming convention across u-blox modules. The pins have not changed their operation and are the same physical hardware but with updated names. The table below lists the pins that have a changed name along with their old and new names.

| No. | Previous name   | New name          |
|-----|-----------------|-------------------|
| 14  | ANT_ON          | LNA_EN            |
| 20  | TxD<br>SPI MISO | TXD /<br>SPI MISO |
| 21  | RxD<br>SPI MOSI | RXD /<br>SPI MOSI |

**Table 7: NEO-M8P module pin renaming**



## <span id="page-17-0"></span>**3 Configuration management**

Configuration settings can be modified with UBX configuration messages. The modified settings remain effective until power-down or reset. Settings can also be saved in battery-backed RAM, flash, or both, using the UBX-CFG-CFG message. If the settings have been stored in battery-backed RAM, the modified configuration will be retained as long as the backup battery supply at **V\_BCKP** is not interrupted. Settings stored in flash memory will remain effective even after power down and do not require a backup battery supply.

## <span id="page-17-1"></span>**3.1 Interface selection (D\_SEL)**

At startup, pin 2 (**D\_SEL**) determines which data interfaces are used for communication. If **D\_SEL** is set high or left open, UART and DDC become available. If **D\_SEL** is set low, that is, connected to ground, the NEO-M8P module can communicate to a host via SPI.

| D_SEL="1"<br>(left open) | D_SEL ="0"<br>(connected to GND) |
|--------------------------|----------------------------------|
| UART TX                  | SPI MISO                         |
| UART RX                  | SPI MOSI                         |
| DDC SCL                  | SPI CLK                          |
| DDC SDA                  | SPI CS_N                         |
|                          |                                  |

**Table 8: Data interface selection by D\_SEL**



## <span id="page-18-0"></span>**4 Electrical specification**

**☞** The limiting values given are in accordance with the Absolute Maximum Rating System (IEC 134). Stress above one or more of the limiting values may cause permanent damage to the device. These are stress ratings only and operation of the device at these or at any other conditions above those given in the characteristics sections of the specification is not implied. Exposure to these limits for extended periods may affect device reliability.

**☞** Where application information is given, it is advisory only and does not form part of the specification. For more information see, the NEO-M8P Hardware integration manual [\[1\].](#page-28-5)

| Parameter                                                  | Symbol  | Condition                                   | Min  | Max     | Units |
|------------------------------------------------------------|---------|---------------------------------------------|------|---------|-------|
| Power supply voltage                                       | VCC     |                                             | –0.5 | 3.6     | V     |
| Backup battery voltage                                     | V_BCKP  |                                             | –0.5 | 3.6     | V     |
| USB supply voltage                                         | VDD_USB |                                             | –0.5 | 3.6     | V     |
| Input pin voltage                                          | VIN     |                                             | –0.5 | 3.6     | V     |
|                                                            | VIN_USB |                                             | –0.5 | VDD_USB | V     |
|                                                            | VRFIN   |                                             | 0    | 6       | V     |
| DC current trough any digital I/O pin<br>(except supplies) | IPIN    |                                             |      | 10      | mA    |
| VCC_RF output current                                      | ICC_RF  |                                             |      | 100     | mA    |
| Input power at RF_IN                                       | PRFIN   | source impedance =<br>50 Ω, continuous wave |      | 15      | dBm   |
| Storage temperature                                        | TSTG    |                                             | –40  | 85      | °C    |

### <span id="page-18-1"></span>**4.1 Absolute maximum rating**

**Table 9: Absolute maximum ratings**

**⚠** Stressing the device beyond the "Absolute Maximum Ratings" may cause permanent damage. These are stress ratings only. The product is not protected against overvoltage or reversed voltages. If necessary, voltage spikes exceeding the power supply voltage specification, given in the table above, must be limited to values within the specified boundaries by using appropriate protection diodes.

## <span id="page-18-2"></span>**4.2 Operating conditions**

**☞** All specifications are at an ambient temperature of +25 °C. Extreme operating temperatures can significantly impact specification values. Applications operating near the temperature limits should be tested to ensure the specification.

| Parameter                               | Symbol   | Min     | Typical | Max     | Units | Condition                    |
|-----------------------------------------|----------|---------|---------|---------|-------|------------------------------|
| Power supply voltage                    | VCC      | 2.7     | 3.0     | 3.6     | V     |                              |
| Supply voltage USB                      | VDD_USB  | 3.0     | 3.3     | 3.6     | V     |                              |
| Backup battery voltage                  | V_BCKP   | 1.4     |         | 3.6     | V     |                              |
| Backup battery current                  | I_BCKP   |         | 15      |         | µA    | V_BCKP = 1.8 V,<br>VCC = 0 V |
| SW backup current                       | I_SWBCKP |         | 30      |         | µA    | VCC = 3 V                    |
| Input pin voltage range                 | VIN      | 0       |         | VCC     | V     |                              |
| Digital IO pin low level input voltage  | VIL      | 0       |         | 0.2*VCC | V     |                              |
| Digital IO pin high level input voltage | VIH      | 0.7*VCC |         | VCC     | V     |                              |



| Parameter                                | Symbol | Min     | Typical | Max                                             | Units | Condition  |
|------------------------------------------|--------|---------|---------|-------------------------------------------------|-------|------------|
| Digital IO pin low level output voltage  | VOL    |         |         | 0.4                                             | V     | IOL = 4 mA |
| Digital IO pin high level output voltage | VOH    | VCC–0.4 |         |                                                 | V     | IOH = 4 mA |
| Pull-up resistor for RESET_N             | RPU    |         | 11      |                                                 | kΩ    |            |
| USB_DM, USB_DP                           | VINU   |         |         | Compatible with USB with 27 Ω series resistance |       |            |
| VCC_RF voltage                           | VCC_RF |         | VCC–0.1 |                                                 | V     |            |
| VCC_RF output current                    | ICC_RF |         |         | 50                                              | mA    |            |
| Receiver Chain Noise Figure12            | NFTOT  |         | 3       |                                                 | dB    |            |
| Operating temperature                    | TOPR   | –40     |         | 85                                              | °C    |            |

**Table 10: Operating conditions**

**☞** Operation beyond the specified operating conditions can affect device reliability.

## <span id="page-19-0"></span>**4.3 Indicative current requirements**

[Table 11](#page-19-2) lists examples of the total system supply current for a possible application.

**☞** Values in [Table 11](#page-19-2) are provided for customer information only as an example of typical power requirements. Values are characterized on samples, actual power requirements can vary depending on firmware version used, external circuitry, number of satellites tracked, signal strength, type of start as well as time, duration, and conditions of test.

| Parameter                     | Symbol                            | Typical<br>GPS & GLONASS | Typical<br>GPS | Max | Units | Condition        |
|-------------------------------|-----------------------------------|--------------------------|----------------|-----|-------|------------------|
| Max. supply current 13        | ICCP                              |                          |                | 67  | mA    |                  |
| Average supply current 14, 15 | ICC Acquisition16                 | 35                       | 27             |     | mA    | Estimated at 3 V |
|                               | ICC Tracking<br>(continuous mode) | 33                       | 25             |     | mA    | Estimated at 3 V |

<span id="page-19-2"></span>**Table 11: Indicative power requirements at 3.0 V**

- **☞** For more information about power requirements, see the NEO-M8P Hardware Integration Manual [\[1\].](#page-28-5)
- **☞** For more information on how to noticeably reduce current consumption, see the Power Management Application Not[e \[4\].](#page-28-6)

## <span id="page-19-1"></span>**4.4 SPI timing diagrams**

To avoid incorrect operation of the SPI, the user needs to comply with certain timing conditions. Consider the following signals for timing constraints:

| Symbol          | Description         |
|-----------------|---------------------|
| SPI CS_N (SS_N) | Slave select signal |
| SPI CLK (SCK)   | Slave clock signal  |

**Table 12: Symbol description**

<span id="page-19-5"></span><sup>14</sup> Use this figure to determine required battery capacity.

<span id="page-19-3"></span><sup>12</sup> Only valid for the GPS band.

<span id="page-19-4"></span><sup>13</sup> Use this figure to dimension maximum current capability of power supply. Measure this parameter with 1-Hz bandwidth.

<span id="page-19-6"></span><sup>15</sup> Simulated GNSS constellation using power levels of -130 dBm. VCC = 3.0 V.

<span id="page-19-7"></span><sup>16</sup> Average current from startup until the first fix.





**Figure 6: SPI timing diagram**

### <span id="page-20-0"></span>**4.4.1 Timing recommendations**

The recommendations below are based on a firmware running from flash memory.

| Parameter | Description         | Recommendation                     |
|-----------|---------------------|------------------------------------|
| tINIT     | Initialization time | >10 µs                             |
| tDES      | Deselect time       | 1 ms                               |
| tbit      | Minimum bit time    | 180 ns (5.5 MHz max bit frequency) |
| tbyte     | Minimum byte period | 8 µs (125 kHz max byte frequency)  |

<span id="page-20-2"></span>**Table 13: SPI timing recommendations**

**☞** The values in [Table 13](#page-20-2) result from the requirement of an error-free transmission. For more information, see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\].](#page-28-2)

### <span id="page-20-1"></span>**4.5 DDC timing**

The DDC interface is I2C Fast Mode compliant. For timing parameters, see the I2C standard.

**☞** The maximum bit rate is 400 kbit/s. The interface stretches the clock when slowed down when serving interrupts, so real bit rates may be slightly lower.



## <span id="page-21-0"></span>**5 Mechanical specifications**



#### **Figure 7 NEO-M8P mechanical drawing**

| Symbol | Min [mm] | Typ. [mm] | Max [mm] |                                                                |
|--------|----------|-----------|----------|----------------------------------------------------------------|
| A      | 15.9     | 16.0      | 16.1     |                                                                |
| B      | 12.1     | 12.2      | 12.3     |                                                                |
| C      | 2.2      | 2.4       | 2.6      |                                                                |
| D      | 0.9      | 1.0       | 1.1      |                                                                |
| E      | 1.0      | 1.1       | 1.2      |                                                                |
| F      | 2.9      | 3.0       | 3.1      |                                                                |
| G      | 0.9      | 1.0       | 1.1      |                                                                |
| H      | -        | 0.82      | -        |                                                                |
| K      | 0.7      | 0.8       | 0.9      |                                                                |
| M      | 0.8      | 0.9       | 1.0      |                                                                |
| N      | 0.4      | 0.5       | 0.6      |                                                                |
| P*     | 0.0      | -         | 0.5      | The de-paneling residual tabs may be on either side (not both) |
| Weight |          | 1.6 g     |          |                                                                |

#### **Table 14 NEO-M8P mechanical dimensions**

- **☞** The mechanical picture of the de-paneling residual tabs (P\*) is an approximate representation. The shape and position of the residual tab may vary.
- **☞** When designing the component keep-out area, note that the de-paneling residual tabs can be on either side of the module (not both).
- **☞** For information about the paste mask and footprint, see the NEO-M8P Hardware integration manua[l \[1\].](#page-28-5)



## <span id="page-22-0"></span>**6 Reliability tests and approvals**

## <span id="page-22-1"></span>**6.1 Reliability tests**

**☞** The NEO-M8P modules are based on AEC-Q100 qualified GNSS chips.

Tests for product family qualifications are according to ISO 16750 "Road vehicles – environmental conditions and testing for electrical and electronic equipment", and appropriate standards.

## <span id="page-22-2"></span>**6.2 Approvals**

Products marked with this lead-free symbol on the product label comply with the "Directive 2002/95/EC of the European Parliament and the Council on the Restriction of Use of certain Hazardous Substances in Electrical and Electronic Equipment" (RoHS).

All u-blox M8 GNSS modules are RoHS compliant.



## <span id="page-23-0"></span>**7 Product handling and soldering**

## <span id="page-23-1"></span>**7.1 Packaging**

To enable efficient production, production lot setup and teardown, the NEO-M8P GNSS modules are delivered as hermetically sealed, reeled tapes. For more information, see the u-blox package information reference [\[3\].](#page-28-7)

### <span id="page-23-2"></span>**7.1.1 Reels**

The NEO-M8P GNSS modules are deliverable in quantities of 250 pieces on a reel. The NEO-M8P receivers are shipped on Reel Type B, as specified i[n \[3\].](#page-28-7)

### <span id="page-23-3"></span>**7.1.2 Tapes**

The dimensions and orientations of the tapes for NEO-M8P GNSS modules are specified in [Figure 8.](#page-23-4)





<span id="page-23-4"></span>**Figure 8: Dimensions and orientation for NEO-M8P modules on tape**



## <span id="page-24-0"></span>**7.2 Shipment, storage, and handling**

For important information regarding shipment, storage, and handling, see the u-blox package information reference [\[3\].](#page-28-7)

#### <span id="page-24-1"></span>**7.2.1 Moisture sensitivity levels**

The moisture sensitivity level (MSL) relates to the packaging and handling precautions required. The NEO-M8P modules are rated at MSL level 4.

**☞** For MSL standard see IPC/JEDEC J-STD-020, which can be downloaded fro[m www.jedec.org.](http://www.jedec.org/)

**☞** For more information regarding MSL, see the u-blox package information reference [\[3\].](#page-28-7)

### <span id="page-24-2"></span>**7.2.2 Reflow soldering**

Reflow profiles are to be selected according to u-blox recommendations (see the NEO-M8P Hardware integration manua[l \[1\]\)](#page-28-5).

### <span id="page-24-3"></span>**7.2.3 ESD handling precautions**

**⚠** NEO-M8P modules are Electrostatic Sensitive Devices (ESD). Observe precautions for handling! Failure to observe these precautions can result in severe damage to the GNSS receiver!

GNSS receivers are Electrostatic Sensitive Devices (ESD) and require special precautions when handling. Exercise particular care when handling patch antennas, due to the risk of electrostatic charges. In addition to standard ESD safety practices, take the following measures into account whenever handling the receiver:

- Unless there is a galvanic coupling between the local GND (work desk) and the PCB GND, the first point of contact when handling the PCB must always be between the local GND and PCB GND.
- Before mounting an antenna patch, connect ground of the device.
- When handling the RF pin, do not come into contact with any charged capacitors and be careful when contacting materials that can develop charges (e.g. patch antenna ~10 pF, coax cable ~50-80 pF/m, soldering iron).
- To prevent electrostatic discharge through the RF input, do not touch any exposed antenna area. If there is any risk that such exposed antenna area is touched in a non-ESD protected work area, implement proper ESD protection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, make sure to use an ESD safe soldering iron (tip).







## <span id="page-25-0"></span>**8 Default messages**

| Interface   | Settings                                                                                                                                                                                                                                                                                                    |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UART output | 9600 baud, 8 bits, no parity bit, 1 stop bit<br>Configured to transmit both NMEA and UBX protocols, but only the following NMEA (and no<br>UBX) messages have been activated at start-up:<br>GGA, GLL, GSA, GSV, RMC, VTG, TXT                                                                              |
| USB output  | Configured to transmit both NMEA and UBX protocols, but only the following NMEA (and no<br>UBX) messages have been activated at start-up:<br>GGA, GLL, GSA, GSV, RMC, VTG, TXT<br>USB power mode: bus-powered                                                                                               |
| UART input  | 9600 baud, 8 bits, no parity bit, 1 stop bit, autobauding disabled<br>Automatically accepts following protocols without need of explicit configuration:<br>UBX, NMEA, RTCM<br>The GNSS receiver supports interleaved UBX and NMEA messages                                                                  |
| USB input   | Automatically accepts following protocols without need of explicit configuration:<br>UBX, NMEA<br>The GPS receiver supports interleaved UBX and NMEA messages<br>USB power mode: bus-powered                                                                                                                |
| DDC         | Fully compatible with the I2C industry standard, available for communication with an external<br>host CPU or u-blox cellular modules, operated in slave mode only. Default messages activated.<br>NMEA and UBX are enabled as input messages, only NMEA as output messages.<br>Maximum bit rate 400 kbit/s. |
| SPI         | Allow communication to a host CPU, operated in slave mode only. Default messages activated.<br>SPI is not available in the default configuration.                                                                                                                                                           |
| TIMEPULSE   | Disabled                                                                                                                                                                                                                                                                                                    |

#### **Table 15: Default messages**

**☞** For information about further settings, refer to u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\].](#page-28-2)



## <span id="page-26-0"></span>**9 Labeling and ordering information**

## <span id="page-26-1"></span>**9.1 Product labeling**

The labeling of u-blox M8 GNSS modules includes important product information. The location of the NEO-M8P product type number is shown i[n Figure 9.](#page-26-4)



<span id="page-26-4"></span>**Figure 9: Location of product type number on the u-blox NEO-M8P module label**

## <span id="page-26-2"></span>**9.2 Explanation of codes**

Three different product code formats are used. The **Product Name** is used in documentation such as this data sheet and identifies all u-blox M8 products, independent of packaging and quality grade. The **Ordering Code** includes options and quality, while the **Type Number** includes the hardware and firmware versions. [Table 16](#page-26-5) shows the structure of these three different formats.

| Format        | Structure    |
|---------------|--------------|
| Product Name  | PPP-TGV      |
| Ordering Code | PPP-TGV-N    |
| Type Number   | PPP-TGV-N-XX |

<span id="page-26-5"></span>**Table 16: Product code formats**

The parts of the product code are explained i[n Table 17.](#page-26-6)

| Code | Meaning                | Example                                                                                           |
|------|------------------------|---------------------------------------------------------------------------------------------------|
| PPP  | Product Family         | NEO                                                                                               |
| TG   | Platform               | M8 = u-blox M8                                                                                    |
| V    | Variant                | Function set (A-Z), T = Timing, R = DR, etc.                                                      |
| N    | Option / Quality Grade | Describes standardized functional element or quality grade<br>0 = Default variant, A = Automotive |
| XX   | Product Detail         | Describes product details or options such as hard- and software revision, cable length, etc.      |

<span id="page-26-6"></span>**Table 17: Part identification code**

## <span id="page-26-3"></span>**9.3 Ordering codes**

| Ordering code | Product                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------|
| NEO-M8P-0     | u-blox M8 GNSS RTK module with rover functionality, 12.2x16 mm, 250 pcs/reel                  |
| NEO-M8P-2     | u-blox M8 GNSS RTK module with rover and base station functionality, 12.2x16 mm, 250 pcs/reel |

**Table 18: Product ordering codes for NEO-M8P professional grade modules**

**☞** Product changes affecting form, fit or function are documented by u-blox. For a list of Product Change Notifications (PCNs), see our website.



## <span id="page-27-0"></span>**Appendix**

## <span id="page-27-1"></span>**A Glossary**

| Abbreviation | Definition                                               |
|--------------|----------------------------------------------------------|
| AEC          | Automotive Electronics Council                           |
| BeiDou       | Chinese satellite navigation system                      |
| CDMA         | Code Division Multiple Access                            |
| DDC          | Display Data Channel                                     |
| EMC          | Electromagnetic Compatibility                            |
| EMI          | Electromagnetic Interference                             |
| EOS          | Electrical Overstress                                    |
| EPA          | Electrostatic Protective Area                            |
| ESD          | Electrostatic Discharge                                  |
| GLONASS      | Russian satellite navigation system                      |
| GND          | Ground                                                   |
| GNSS         | Global Navigation Satellite System                       |
| GPS          | Global Positioning System                                |
| GSM          | Global System for Mobile Communications                  |
| I2C          | Inter-Integrated Circuit interconnect                    |
| IEC          | International Electrotechnical Commission                |
| ISO          | International Standards Organization for Standardization |
| MB           | Moving Baseline                                          |
| NED          | North East Down local Cartesian coordinates              |
| NMEA         | National Marine Electronics Association                  |
| PCB          | Printed Circuit Board                                    |
| PCN          | Product Change Notification                              |
| QZSS         | Quasi-Zenith Satellite System                            |
| RF           | Radio Frequency                                          |
| RTCM         | Radio Technical Commission for Maritime Services         |
| RTK          | Real Time Kinematic                                      |
| SPI          | Serial Peripheral Interface                              |
| TCXO         | Temperature Compensated Crystal Oscillator               |
| UART         | Universal Asynchronous Receiver/Transmitter              |
| UAV          | Unmanned Aerial Vehicle                                  |
| USB          | Universal Serial Bus                                     |

**Table 19: Explanation of the abbreviations and terms used**



## <span id="page-28-0"></span>**Related documents**

- <span id="page-28-5"></span>[1] NEO-M8P Hardware integration manual, [UBX-15028081](https://www.u-blox.com/docs/UBX-15028081)
- <span id="page-28-2"></span>[2] u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification (Public version), [UBX-13003221](https://www.u-blox.com/docs/UBX-13003221)
- <span id="page-28-7"></span>[3] u-blox package information for chips, modules, and antennas, reference, [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- <span id="page-28-6"></span>[4] Power Management Application Note, [UBX-13005162](https://www.u-blox.com/docs/UBX-13005162)
- <span id="page-28-3"></span>[5] Multi-GNSS Assistance User guide[, UBX-13004360](https://www.u-blox.com/docs/UBX-13004360)
- <span id="page-28-4"></span>[6] RTCM 10403.2, Differential GNSS Services - Version 3 (February 2013)

**☞** For regular updates to u-blox documentation and to receive product change notifications, register on our homepage [\(www.u-blox.com\)](http://www.u-blox.com/).

## <span id="page-28-1"></span>**Revision history**

| Revision | Date        | Name      | Comments                                                                                                                                                                                                                                            |
|----------|-------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 15-Oct-2015 | mstr      | Objective Specification                                                                                                                                                                                                                             |
| R02      | 15-Feb-2016 | byou/mstr | Advance Information, updated to reflect FW3.01 HPG 1.00 status                                                                                                                                                                                      |
| R03      | 30-May-2016 | byou/mstr | Updated to reflect FW3.01 HPG 1.11 status                                                                                                                                                                                                           |
| R04      | 27-Sep-2016 | byou      | Updated to reflect FW3.01 HPG1.20 status                                                                                                                                                                                                            |
| R05      | 19-Jan-2017 | byou      | Early Production Information, updated to reflect FW3.01 HPG1.30 status,<br>updated section 1.6.3 (added statements for GLONASS ambiguity fixing<br>and MSM4 messages), added MSM4 and GLONASS code-phase biases<br>messages in Table 2 and Table 3. |
| R06      | 16-May-2017 | byou      | Early Production Information, updated to reflect FW3.01 HPG1.40 status.<br>Updated section 1.6 - MB mode information and messages.                                                                                                                  |
| R07      | 2-Nov-2017  | byou      | Production Information.                                                                                                                                                                                                                             |
| R08      | 09-Mar-2020 | smos/mala | Updated style to current CI.<br>Added information on QZSS in section Product features.<br>Reintroduced timepulse for NEO-M8P-0 (rover) in the Product features<br>table.                                                                            |
| R09      | 19-Aug-2021 | mala/dama | Updated type number, FW and PCN reference on page 2                                                                                                                                                                                                 |
| R10      | 28-Feb-2022 | dbhu      | Production information                                                                                                                                                                                                                              |
| R11      | 16-Dec-2022 | skar      | Chapter Mechanical specifications updated with information on de-paneling<br>residual tabs                                                                                                                                                          |



## <span id="page-29-0"></span>**Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support.](http://www.u-blox.com/support)