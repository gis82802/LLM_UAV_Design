

# **NEO-D9S and ZED-F9 configuration**

**SPARTN L-band correction data reception Application Note**

### **Abstract**

This document explains how to configure the NEO-D9S correction data receiver together with ZED-F9 high precision modules in order to receive and use SPARTN L-band correction data.





## <span id="page-1-0"></span>**Document information**

| Title                  | NEO-D9S and ZED-F9 configuration        |             |  |
|------------------------|-----------------------------------------|-------------|--|
| Subtitle               | SPARTN L-band correction data reception |             |  |
| Document type          | Application note                        |             |  |
| Document number        | UBX- 22008160                           |             |  |
| Revision and date      | R02                                     | 27-Jul-2022 |  |
| Disclosure restriction | C1-Public                               |             |  |

**☞** Check if the ZED-F9 product that you are using supports the SPARTN protocol and the related configurations.

u-blox or third parties may hold intellectual property rights in the products, names, logos, and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only. The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability, and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.

<span id="page-2-0"></span>

| Document information2                                   |  |
|---------------------------------------------------------|--|
| Contents 3                                              |  |
| 1<br>Introduction4                                      |  |
| 2<br>NEO-D9S configuration6                             |  |
| 2.1<br>L-band point to multipoint (PMP) configuration 6 |  |
| 2.2<br>Interface configuration 6                        |  |
| 2.3<br>Functional check 7                               |  |
| 3<br>ZED-F9 configurations8                             |  |
| 3.1<br>L-band configuration8                            |  |
| 3.2<br>Interface configuration 8                        |  |
| 3.3<br>Dynamic keys 9                                   |  |
| 3.4<br>Functional check 9                               |  |
| 4<br>Example configuration for PointPerfect 11          |  |
| 4.1<br>NEO-D9S L-band configuration 11                  |  |
| 4.2<br>Setting ZED-F9 keys 11                           |  |
| A<br>Glossary  16                                       |  |
| Related documentation  17                               |  |
| Revision history 17                                     |  |
| Contact 17                                              |  |



# <span id="page-3-0"></span>**1 Introduction**

The ZED-F9 high precision modules have integrated multiband PPP-RTK technology for centimeterlevel accuracy using SPARTN [\[8\]](#page-16-3) State Space Representation (SSR) type of correction.

SSR services rely on a GNSS reference station network to model key errors (such as satellite or atmospheric errors) over large geographical regions and provide corrections to the rover via broadcast link such as internet or satellite L-band, all receivers receive the same data over a large area.

**☞** Check if the ZED-F9 product that you are using supports the SPARTN L-band stream formatted as UBX-RXM-PMP messages, and the related configurations.



[Figure 1](#page-3-1) represents how NEO-D9S and ZED-F9 work together:

<span id="page-3-1"></span>**Figure 1: NEO-D9S and ZED-F9 scenario** 

NEO-D9S is a satellite data receiver for L-band correction broadcasts, which can be configured to work with a variety of correction services. This document provides instructions on how to configure NEO-D9S for this purpose and provides configuration examples for the PointPerfect service, SPARTN L-band correction, and ZED-F9 receivers. [Figure 2](#page-3-2) represents the NEO-D9S and ZED-F9 connection:



#### <span id="page-3-2"></span>**Figure 2: NEO-D9S and ZED-F9 connection**

The NEO-D9S and ZED-F9 receivers follow the u-blox configuration concept. The UBX-CFG-VALSET, UBX-CFG-VALGET, and UBX-CFG-VALDEL messages can be used to configure the SPARTN L-band correction data reception. See the D9 PMP 1.04 Interface description [\[4\]](#page-16-4) and the F9 HPG 1.32 Interface description [\[5\]](#page-16-5) for further details.

For the correction data, NEO-D9S and ZED-F9 can be connected via their respective UART2 interfaces, as shown in [Figure 2.](#page-3-2) The UART2 connection is commonly used and recommended for customer designs, while The UART1 can be used as the main host interface for configuration,



monitoring, and control. The USB interface is provided for host communication purposes and can be used for monitoring or logfiles collection.

[Figure 3](#page-4-0) shows the series of actions to be done:



#### <span id="page-4-0"></span>**Figure 3: ZED-F9 and NEO-D9S configuration sequence diagram**

Configuration strings are provided in the following sections of the document for each configuration item. If you are using u-center, the strings can be sent via a custom message:

| <b>D</b> CUSTOM-??? [-]                             | $\mathbf{x}$<br>$\Box$<br><b>- 11</b>                                                                                                                                                                                                                                                                          |  |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| □ NMEA<br>向 NMEA-NAV2<br><sup>¶</sup> ⊞ RTCM3       | Custom Messages<br>$\frac{1}{2}$<br>$F$ Hex                                                                                                                                                                                                                                                                    |  |
| <b>E</b> -UBX<br><b>L. UNKNOWN</b>                  | $C$ Text                                                                                                                                                                                                                                                                                                       |  |
| <b>CUSTOM</b>                                       | b5 62 06 8a 3f<br>e0 cb 1a 5c 16 00 b1<br>55 55 13 00 b1<br>.nn<br>10<br>00 17 00 b1<br>-30<br>. nn<br>00<br>00<br>b1 40<br>. NO 01<br>-11<br>59 69 12 00 b1 30 98 08 1a 00 b1 50 93 e8 5a e1 93 e8 5a e1<br>130<br>60<br>30<br>00<br>ъ1<br>-09<br>-15<br>10<br>01<br>.nn<br>Ъ1.<br>14<br>18 00 b1 20 04 5e 88 |  |
|                                                     | $\lambda_{\rm{eff}}$                                                                                                                                                                                                                                                                                           |  |
| B<br>改相要同属<br>$\frac{1}{\lambda_1}$<br>$B$ $\times$ |                                                                                                                                                                                                                                                                                                                |  |

#### **Figure 4: Send Custom message with u-center**

For more details, see the u-center user guid[e \[3\].](#page-16-6)

The easiest way to test how to configure the NEO-D9S and ZED-F9 receivers is to make use of the C099-F9P and C101-D9S application boards. See the related user guides [\[6\]](#page-16-7) and [\[7\],](#page-16-8) and in particular Chapter 4 of the C101-D9S User Guide.



# <span id="page-5-0"></span>**2 NEO-D9S configuration**

NEO-D9S needs to be configured to receive SPARTN L-band correction data and forward these, encapsulated in UBX-RXM-PMP messages, to the ZED-F9 receiver via UART2.

### <span id="page-5-1"></span>**2.1 L-band point to multipoint (PMP) configuration**

[Table 1](#page-5-3) lists the NEO-D9S L-band default configuration values, which will vary depending on the service provider. Once the related values have been obtained from the service provider, they can be set accordingly with the UBX-CFG-VALSET configuration messages (see the interface description [\[4\]](#page-16-4) for further details).

| Configuration item        | Value              |
|---------------------------|--------------------|
| CFG-PMP-CENTER_FREQUENCY  | 1539812500 Hz      |
| CFG-PMP-SEARCH_WINDOW     | 2200 Hz            |
| CFG-PMP-USE_SERVICE_ID    | 1 (true)           |
| CFG-PMP-SERVICE_ID        | 50821              |
| CFG-PMP-DATA_RATE         | 2400 (B2400) bps   |
| CFG-PMP-USE_DESCRAMBLER   | 1 (true)           |
| CFG-PMP-DESCRAMBLER_INIT  | 23560              |
| CFG-PMP-USE_PRESCRAMBLING | 0 (false)          |
| CFG-PMP-UNIQUE_WORD       | 0xe15ae893e15ae893 |

<span id="page-5-3"></span>**Table 1: NEO-D9S L-band default configuration values**

Sectio[n 4](#page-10-0) outlines how to obtain the L-band configuration values for the PointPerfect service.

### <span id="page-5-2"></span>**2.2 Interface configuration**

[Table 2](#page-5-4) shows the configuration items needed to configure the UART2 interface of NEO-D9S so that it can communicate with the ZED-F9.

| Configuration item   | Value    |
|----------------------|----------|
| CFG-UART2OUTPROT-UBX | 1 (true) |
| CFG-UART2-BAUDRATE   | 38400    |

#### <span id="page-5-4"></span>**Table 2: NEO-D9S UART2 configuration items**

To facilitate the configuration, examples of the configuration strings for **RAM** and **Flash** layers are shown here:

#### **RAM layer configuration string:**

**b5 62 06 8a 11 00 00 01 00 00 01 00 53 40 00 96 00 00 01 00 76 10 01 54 ef**

### **Flash layer configuration string:**

### **b5 62 06 8a 11 00 00 04 00 00 01 00 53 40 00 96 00 00 01 00 76 10 01 57 1f**

When sending Flash layer configuration strings, the receiver needs to be restarted to apply them in RAM.

The UBX-RXM-PMP message is enabled by default in the output to the NEO-D9S UART2 interface.



### <span id="page-6-0"></span>**2.3 Functional check**

Firstly, some initial functional checks are required to verify that NEO-D9S is operating correctly:

- NEO-D9S communication has been established (e.g., via u-center) through UART1 or USB
- The L-band antenna is plugged in
- The L-band and interface configurations have been sent
- The UBX-RXM-PMP message can be used to check the received correction data [\(Figure 5\)](#page-6-1)
- The UBX-MON-TXBUF message can be used to check the data sent via UART2 [\(Figure 6\)](#page-6-2)

[Figure 5](#page-6-1) and [Figure 6](#page-6-2) show the messages as they appear in u-center.



<span id="page-6-1"></span>**Figure 5: UBX-RXM-PMP message in u-center**



<span id="page-6-2"></span>**Figure 6: UBX-MON-TXBUF message in u-center**



# <span id="page-7-0"></span>**3 ZED-F9 configurations**

ZED-F9 needs to be configured to receive and use the SPARTN L-band correction stream, in the form of UBX-RXM-PMP messages from NEO-D9S.

### <span id="page-7-1"></span>**3.1 L-band configuration**

The CFG-SPARTN-USE\_SOURCE configuration key needs be set to LBAND:

| Configuration item                                              | Value     |
|-----------------------------------------------------------------|-----------|
| CFG-SPARTN-USE_SOURCE                                           | 1 - LBAND |
| Table 3: ZED-F9 configurations for SPARTN L-band data reception |           |

The configuration strings for **RAM** and **Flash** layers are:

**RAM layer configuration string:**

**b5 62 06 8a 09 00 00 01 00 00 01 00 a7 20 01 63 6c**

**Flash layer configuration string:**

### **b5 62 06 8a 09 00 00 04 00 00 01 00 a7 20 01 66 84**

When sending Flash layer configuration strings, the receiver needs to be restarted to apply them in RAM.

### <span id="page-7-2"></span>**3.2 Interface configuration**

The UBX protocol needs to be enabled on the ZED-F9 UART2 input:

| Configuration item  | Value    |
|---------------------|----------|
| CFG-UART2INPROT-UBX | 1 (true) |

**Table 4: ZED-F9 UART2 configuration item**

**☞** For some ZED-F9 receivers, the UBX input protocol is already enabled by default on UART2. For example, it is enabled by default on ZED-F9P with firmware HPG 1.32. Check the default interface configuration for your ZED-F9 receiver in the related interface description.

The configuration strings for **RAM** and **Flash** layers are:

**RAM layer configuration string:**

**b5 62 06 8a 09 00 00 01 00 00 01 00 75 10 01 21 b6**

**Flash layer configuration string:**

**b5 62 06 8a 09 00 00 04 00 00 01 00 75 10 01 24 ce**

When sending Flash layer configuration strings, the receiver needs to be restarted to apply them in RAM.



### <span id="page-8-0"></span>**3.3 Dynamic keys**

ZED-F9 may require proper keys to decrypt a SPARTN data stream. Once the key or keys are obtained from the correction service provider, the UBX-RXM-SPARTNKEY message needs to be formatted and sent to the ZED-F9 receiver. The following is an example of a UBX-RXM-SPARTNKEY construction for the PointPerfect service. For more details, read about UBX-RXM-SPARTNKEY in the interface description [\[5\].](#page-16-5)

The following shows a UBX-RXM-SPARTNKEY construction example for PointPerfect:

### b5 62 02 36 00 2c 01 02 00 00 00 10 88 08 4d 82 04 00 00 10 88 08 ce 29 05 00 XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX de 77

**☞** The keys are not stored in non-volatile memory and will be deleted on every module reset or restart. In such cases, the keys need to be re-entered.

### <span id="page-8-1"></span>**3.4 Functional check**

Firstly, some initial functional checks are required to verify that ZED-F9 is operating correctly:

- ZED-F9 communication has been established (e.g., via u-center) through UART1 or USB
- The GNSS antenna is plugged in
- The L-band and interface configurations have been sent, as well as the dynamic keys
- The ZED-F9 UART2 has been connected to the NEO-D9S UART2

Then, the UBX-MON-COMMS message can be enabled to verify that UBX messages are received on the ZED-F9 UART2, including UBX-RXM-PMP:

| memAllocError  | No                    |                  |             |         |           |             |
|----------------|-----------------------|------------------|-------------|---------|-----------|-------------|
| txBufFullError | No                    |                  |             |         |           |             |
| Port (PortId)  |                       | Total(B)         | Pending (B) | Usage   | PeakUsage | OverrunErrs |
| UART1 (0x01)   | Тx                    | 1456080          | O           | 15%     | 16%       |             |
| USB (0x03)     | Тx                    | 0                | 0           | $0\%$   | 19%       |             |
| UART2 (0x12)   | Тx                    | n                | Ū           | $0\%$   | $0\%$     |             |
| UART1 (0x01)   | <b>Bx</b>             | 371              | Ū           | O%      | $1\%$     | 0           |
| USB (0x03)     | <b>Bx</b>             | 0                | 0           | $0\%$   | 0%        | 0           |
| UART2 (0x12)   | <b>Bx</b>             | 177416           | Ū           | Ū%      | $8\%$     | 0           |
| Port (PortId)  |                       | $0$ -UB $\times$ | 1-NMEA      | 5-RTCM3 | 6-SPARTN  | skipped (B) |
| UART1 (0x01)   | <b>Bx</b>             | 23               | Ω           | Ω       | n         | Ω           |
| TICD (0.02)    | D.L<br><b>Bandary</b> | $\Omega$         | Ū           | Ū       | n         | 0           |
| UART2 (0x12)   | <b>Bx</b>             | 331              | 0           | 0       | n         | 0           |

**Figure 7: UBX-MON-COMMS message in u-center**



The UBX-RXM-COR message can be enabled to check if SPARTN corrections, encapsulated in UBX-RXM-PMP messages, are being received, decrypted, and used (in the red square) by the ZED-F9 receiver:

| UBX-RXM-COR1s    |                |            |              |                |                  |                       |           |           |                 |
|------------------|----------------|------------|--------------|----------------|------------------|-----------------------|-----------|-----------|-----------------|
| Protocol         | Type - Subtype | Can handle | Used         | Error Status   | Correction ID    | Type - Subtype        | Encrypted | Decrypted | Eb/N0 (2^-3 dB) |
| UBX-RXM-PMP (29) | $0 - 2$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes(2)    | 106             |
| UBX-RXM-PMP (29) | $0 - 1$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $0-0$          | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $0 - 2$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (0xFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes(2)    | 105             |
| UBX-RXM-PMP (29) | $0 - 1$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 105             |
| UBX-RXM-PMP (29) | $0 - 0$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes(2)    | 112             |
| UBX-RXM-PMP (29) | $1 - 2$        | Yes(1)     | Not used [1] | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 111             |
| UBX-RXM-PMP (29) | $1 - 1$        | Yes(1)     | Not used (1) | Error-free (1) | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 111             |
| UBX-RXM-PMP (29) | $1 - 1$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 111             |
| UBX-RXM-PMP (29) | $0 - 2$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $0 - 1$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $0-0$          | Yes(1)     | Used (2)     | Error-free (1) | Unknown (0xFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $1 - 0$        | Yes(1)     | Not used (1) | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes(2)    | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $1 - 0$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 106             |
| UBX-RXM-PMP (29) | $1 - 0$        | Yes(1)     | Not used (1) | Error-free (1) | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes(2)    | 109             |
| UBX-RXM-PMP (29) | $0 - 2$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (OxFFFF) | Valid [1] - Valid [1] | Yes [2]   | Yes(2)    | 102             |
| UBX-RXM-PMP (29) | $0 - 1$        | Yes(1)     | Used[2]      | Error-free [1] | Unknown (0xFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 109             |
| UBX-RXM-PMP (29) | $0 - 0$        | Yes(1)     | Used [2]     | Error-free [1] | Unknown (OxFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 109             |
| UBX-RXM-PMP (29) | $1 - 2$        | Yes(1)     | Used (2)     | Error-free [1] | Unknown (0xFFFF) | Valid (1) - Valid (1) | Yes [2]   | Yes [2]   | 109             |

#### **Figure 8: UBX-RXM-COR message in u-center**

If all these checks pass, the ZED-F9 receiver should go into an RTK fix or float solution depending on the satellite visibility and environmental condition:

|                                                                    | ×                                                   |
|--------------------------------------------------------------------|-----------------------------------------------------|
| Longitude<br>Latitude<br>Altitude<br>Altitude (msl)<br><b>TTFF</b> | 8,56530350<br>47.28520200<br>548.100 m<br>500.800 m |
| Fix Mode                                                           | 3D/DGNSS/FIXED                                      |
| 3D Acc. [m]                                                        |                                                     |
| 2D Acc. [m]                                                        |                                                     |
| PDOP                                                               | 1.1<br>О                                            |
| HDOP                                                               | 0.6                                                 |
| <b>Satellites</b>                                                  | .                                                   |
|                                                                    |                                                     |
|                                                                    |                                                     |
|                                                                    |                                                     |
|                                                                    |                                                     |
|                                                                    |                                                     |

**Figure 9: Position and status visualization windows in u-center**



# <span id="page-10-0"></span>**4 Example configuration for PointPerfect**

To create a Thingstream account and a PointPerfect Thing, use the following link:

<https://developer.thingstream.io/guides/location-services/pointperfect-getting-started>

PointPerfect L-band SPARTN service is only available to qualified customers. The service is not available for consumer customers.

### <span id="page-10-1"></span>**4.1 NEO-D9S L-band configuration**

Contact the Thingstream support at [support@thingstream.io](mailto:support@thingstream.io) to obtain the NEO-D9S PointPerfect L-band configuration keys value for your region.

The configuration should be applied as mentioned at section [2.1.](#page-5-1)

### <span id="page-10-2"></span>**4.2 Setting ZED-F9 keys**

The keys should be in the following format:

| L-band + IP Dynamic Keys |                                 | thingstream                 |   |
|--------------------------|---------------------------------|-----------------------------|---|
| <b>Current Key</b>       | bfdbXXXXXXXXXXXXXXXXXXXXXXXXXXX | Expires: 01:59 Apr 09, 2022 | m |
| Next Key                 | e928XXXXXXXXXXXXXXXXXXXXXXXXXXX | Expires: 01:59 May 07, 2022 | 冋 |
|                          |                                 |                             |   |

#### <span id="page-10-3"></span>**Figure 10: PointPerfect SPARTN Keys**

Once the keys have been obtained from the PointPerfect account, the UBX-RXM-SPARTNKEY message needs to be formatted and sent to the ZED-F9 receiver, as shown in section [3.](#page-7-0)

ZED-F9 will first use the "Current key", and when it expires the "Next key" will be used. Users should take care to download new keys periodically and update accordingly.

### **Setting the keys via the u-center MQTT client**

From your Thingstream account and after the PointPerfect Thing has been created for the L-band service, it will be possible to download the u-center config file (JSON file) and save it in your u-center working folder:

| <b>MQTT Credentials</b>        | thingstream |
|--------------------------------|-------------|
| <b>Client Key</b>              |             |
| <b>Client Certificate</b>      |             |
| <b>Amazon Root Certificate</b> | M           |
| <b>U-Center Config</b>         | ∸           |
|                                |             |

**Figure 11: PointPerfect MQTT credentials and u-center configuration file**



Connect u-center, version 22.05 or newer, to the F9 receiver and open the MQTT client dialog box from the Receiver menu. Browse for the JSON file from the u-center working folder, tick the key topic box, and select the OK button. Then the keys will be loaded in the F9 receiver.

| Receiver | Tools Window Help                    |                                |                           |                                                                                         |
|----------|--------------------------------------|--------------------------------|---------------------------|-----------------------------------------------------------------------------------------|
|          | Connection                           | $\rightarrow$                  | <mark>は 16</mark>   田 HHH | 188888888881<br>中空后位 台湾 计异中心                                                            |
|          | Baudrate                             | $\rightarrow$                  | 美  大 饼     ≙              | <b>マゆ 4 D H</b>                                                                         |
|          | * UDP Server                         |                                |                           |                                                                                         |
|          | * TCP Server                         |                                |                           |                                                                                         |
|          | NTRIP Server/Caster                  |                                |                           |                                                                                         |
|          | NTRIP Client                         |                                |                           |                                                                                         |
|          | MQTT Client                          |                                |                           |                                                                                         |
|          | Autobauding                          |                                |                           | $\times$<br><b>MQTT</b> client settings                                                 |
|          | Debug Messages                       |                                |                           | -MQTT settings                                                                          |
|          | Generation<br><b>Protocol Filter</b> | $\rightarrow$<br>$\rightarrow$ |                           | JSON config file<br>C:\Users\dama\Desktop\u-center\device-c3672316-75f2-4457-91a4-c00 - |
|          |                                      |                                |                           |                                                                                         |
| Action   | Differential GNSS Interface          | $\rightarrow$                  |                           | $\nabla$ Subscribe to key topic                                                         |
|          |                                      |                                |                           | □ Subscribe to AssistNow topic                                                          |
|          | Epoch detection                      |                                |                           |                                                                                         |
|          |                                      |                                |                           | $\Box$ Subscribe to data topic                                                          |
|          |                                      |                                |                           | Select data topic                                                                       |
|          |                                      |                                |                           |                                                                                         |
|          |                                      |                                |                           | OK<br>Cancel                                                                            |
|          |                                      |                                |                           |                                                                                         |
|          |                                      |                                |                           |                                                                                         |
|          |                                      |                                |                           |                                                                                         |

**Figure 12: u-center MQTT client and key topic**

The MQTT client dialog windows also include topics for providing data to the receiver via an IP connection – AssistNow for GNSS assistance and the SPARTN correction data.

### **Settings the keys manually via u-center**

The UBX-RXM-SPARTNKEY message can be formatted, for example, using u-center [\[3\].](#page-16-6) [Figure 14](#page-11-0) shows the UBX-RXM-SPARTNKEY message view in u-center:

| $\Box$ Key 1 | Encryption<br>algorithm<br>$0 - AES$ - | Key<br>length | Valid from WNO                | Valid from TOW |
|--------------|----------------------------------------|---------------|-------------------------------|----------------|
| Key          |                                        |               |                               |                |
|              | Encryption<br>algorithm                | Key<br>length | Valid from WNO Valid from TOW |                |
| $\Box$ Key 2 | $0 - AES$ $\rightarrow$                |               |                               |                |
| Key          |                                        |               |                               |                |

<span id="page-11-0"></span>**Figure 13: UBX-RXM-SPARTNKEY message view in u-center**



"Key 1" in the message view represents the Current Key received form the PointPerfect Thing as shown in [Figure 11,](#page-10-3) and "Key 2" represents the Next Key.

For each key, the related fields should be filled in as follows:

- Encryption algorithm = 0 AES
- Key length = 16 (Bytes)

For Key 1, the fields "Valid from WNO" and "Valid from TOW" can be filled in with the current date expressed in GNSS data format, while for Key 2 these fields can be filled in using the Key 1 expiration date.

As an example, consider 22 March 2022 as the current date (you could use a GNSS online data translator, e.g., [http://navigationservices.agi.com/GNSSWeb\)](http://navigationservices.agi.com/GNSSWeb) and fill in the fields as shown below:



#### **Figure 14: Example of current date in GNSS data format**

WNO and TOW can be used to fill the related fields in the UBX-RXM-SPARTNKEY message, as shown in [Figure 16.](#page-13-0)



| UBX-RXM-SPARTNKEY 36 s                                                    |                         |                                                    |    |                                                            |                |    |                     |         |    |                                 |    |    |    |    |                          |    |    |    |
|---------------------------------------------------------------------------|-------------------------|----------------------------------------------------|----|------------------------------------------------------------|----------------|----|---------------------|---------|----|---------------------------------|----|----|----|----|--------------------------|----|----|----|
|                                                                           | $\overline{\vee}$ Key 1 |                                                    |    | Encryption<br>algorithm<br>$0 - AES$ $\blacktriangleright$ |                |    | Key<br>length<br>16 |         |    | Valid from WNO<br>2202          |    |    |    |    | Valid from TOW<br>172800 |    |    |    |
|                                                                           |                         | Key                                                |    |                                                            |                |    |                     |         |    | BFDBXXXXXXXXXXXXXXXXXXXXXXXXXXX |    |    |    |    |                          |    |    |    |
|                                                                           | $\Box$ Key 2            | Key                                                |    | Encryption<br>algorithm<br>$0 - AES$ -                     |                |    | Key<br>length       |         |    | Valid from WNO                  |    |    |    |    | Valid from TOW           |    |    |    |
| 0000<br>0012                                                              | <b>B5</b>               | 62<br>BF DB XX XX XX XX XX XX XX XX XX XX XX XX XX | 02 | 36                                                         | 1 <sup>C</sup> | 00 | 01                  | $_{01}$ | 00 | 00                              | 00 | 10 | 9Ά | 08 | 00                       | AЗ | 02 | 00 |
| $\left \mathbf{S}\right \times \mathbf{B} $ 华文国团团团团团团 ) Chip number $[0]$ |                         |                                                    |    |                                                            |                |    |                     |         |    |                                 |    |    |    |    |                          |    | 镼  |    |

<span id="page-13-0"></span>**Figure 15: UBX-RXM-SPARTNKEY with Current Key entered**

The UBX-RXM-SPARTANKEY message is shown within the red outline in [Figure 16.](#page-13-0) This can be sent to the connected receiver by clicking Send, or it can be copied and sent separately (e.g., from the customer host processor).

The Next Key can also be updated, and it will automatically be used instead of the Current key when the latter expires.

From the example in [Figure 11,](#page-10-3) the Current Key expiration date is 01:59 Apr 09, 2022. As previously stated, you can use the GNSS data translator to convert it to the appropriate GNSS data format:

| <b>March</b>               |                                |                                 | <b>April 2022</b>               |                            |                                 | May                             |
|----------------------------|--------------------------------|---------------------------------|---------------------------------|----------------------------|---------------------------------|---------------------------------|
| <b>Sun</b>                 | Mon                            | <b>Tue</b>                      | Wed                             | Thu                        | Fri                             | Sat                             |
| 3<br>2204:0<br>156:0<br>93 | 4<br>2204:1<br>156:86400<br>94 | 5<br>2204:2<br>156:172800<br>95 | 6<br>2204:3<br>156:259200<br>96 | 2204:4<br>156:345600<br>97 | 8<br>2204:5<br>156:432000<br>98 | 9<br>2204:6<br>156:518400<br>99 |

**Figure 16: Example of expiration date in GNSS data format**

518400 is the TOW at 00:00 Apr 09, 2022.

In the current example (Current Key expiration date: 01:59 Apr 09, 2022):

TOW = 518400 + 7200 (2 hours) = 525600

The figure below shows the related UBX-RXM-SPARTNKEY message:



| UBX-RXM-SPARTNKEY 56 s                                                           |                                                                              |                                        |                                                       |                      |                        |          |                               |       |  |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------|-------------------------------------------------------|----------------------|------------------------|----------|-------------------------------|-------|--|
| $\nabla$ Key 1                                                                   |                                                                              | Encryption<br>algorithm<br>$0 - AES$ - | Key<br>16                                             | length               | Valid from WNO<br>2202 |          | Valid from TOW<br>172800      |       |  |
|                                                                                  | BFDBXXXXXXXXXXXXXXXXXXXXXXXXXXX<br>Key                                       |                                        |                                                       |                      |                        |          |                               |       |  |
|                                                                                  | Valid from WNO<br>Valid from TOW<br>Encryption<br>Key<br>algorithm<br>length |                                        |                                                       |                      |                        |          |                               |       |  |
| <b>2204</b><br>525600<br>$0 - AES$ $\blacktriangleright$<br>16<br>$\nabla$ Key 2 |                                                                              |                                        |                                                       |                      |                        |          |                               |       |  |
| E928XXXXXXXXXXXXXXXXXXXXXXXXXXX<br>Kev                                           |                                                                              |                                        |                                                       |                      |                        |          |                               |       |  |
| 0000<br>0011                                                                     | B5<br>62<br>00<br>00                                                         | 02<br>36 34<br>9C 08<br>10             | 00<br>$_{01}$<br>20<br>05                             | 02<br>00<br>08<br>00 | 00<br>00<br>ΒF<br>DB   | 9А<br>10 | 08<br>00<br>XX XX XX XX XX XX | A3 02 |  |
| 0022                                                                             |                                                                              |                                        | XX XX XX XX XX XX XX XX XX E9 28 XX XX XX XX XX XX XX |                      |                        |          |                               |       |  |
|                                                                                  |                                                                              |                                        | × 1 画書 文 目 面 由 面隔                                     |                      |                        |          |                               | E.    |  |

**Figure 17: UBX-RXM-SPARTNKEY with Current and Next Keys entered**

As mentioned previously, this can be sent to the receiver by clicking Send, or it can be copied and sent separately (e.g., from the customer host processor).



# <span id="page-15-0"></span>**Appendix**

# **A Glossary**

| Abbreviation | Definition                                            |  |  |  |  |  |
|--------------|-------------------------------------------------------|--|--|--|--|--|
| GNSS         | Global Navigation Satellite System                    |  |  |  |  |  |
| HPG          | High Precision                                        |  |  |  |  |  |
| RAM          | Random Access Memory                                  |  |  |  |  |  |
| SPARTN       | Secure Position Augmentation for Real Time Navigation |  |  |  |  |  |
| RTK          | Real Time Kinematic                                   |  |  |  |  |  |
| SSR          | State Space Representation                            |  |  |  |  |  |
| TOW          | Time Of Week                                          |  |  |  |  |  |
| UART         | Universal Asynchronous Receiver Transmitter           |  |  |  |  |  |
| USB          | Universal Serial Bus                                  |  |  |  |  |  |
| WNO          | Week Number                                           |  |  |  |  |  |

**Table 5: Explanation of the abbreviations and terms used**



# <span id="page-16-0"></span>**Related documentation**

- [1] NEO-D9S Integration manual, [UBX-19026111](http://www.u-blox.com/docs/UBX-19026111)
- [2] ZED-F9P Integration manual, [UBX-18010802](http://www.u-blox.com/docs/UBX-18010802)
- <span id="page-16-6"></span>[3] u-center User guide[, UBX-13005250](http://www.u-blox.com/docs/UBX-13005250)
- <span id="page-16-4"></span>[4] u-blox D9 PMP 1.04 Interface description, UBX- [21040023](https://dms.u-blox.com/share/proxy/alfresco/api/node/content/workspace/SpacesStore/50aa960a-e94d-40be-85f2-a6f928d33aed/u-blox-D9-PMP-1.04_InterfaceDescription_UBX-21040023.pdf?a=true)
- <span id="page-16-5"></span>[5] u-blox F9 HPG 1.32 Interface description, [UBX-22008968](https://dms.u-blox.com/share/proxy/alfresco/api/node/content/workspace/SpacesStore/675fea02-17ee-487b-8475-dcbcef9bf19f/u-blox-F9-HPG-1.32_InterfaceDescription_UBX-22008968.pdf?a=true)
- <span id="page-16-7"></span>[6] C099-F9P application board User guide, UBX- 18063024
- <span id="page-16-8"></span>[7] C101-D9S application board User guide, UBX-20031865
- <span id="page-16-3"></span>[8] Secure Position Augmentation for Real-Time Navigation (SPARTN) Interface Control Document, Version 2.0.1, September 2021.

**☞** For product change notifications and regular updates of u-blox documentation, register on our website, [www.u-blox.com.](http://www.u-blox.com/)

# <span id="page-16-1"></span>**Revision history**

| Revision | Date        | Name | Comments            |
|----------|-------------|------|---------------------|
| R01      | 13-Jun-2022 | dama | Initial release     |
| R02      | 27-Jul-2022 | dama | Section 2.3 updated |

# <span id="page-16-2"></span>**Contact**

For further support and contact information, visit us at [www.u-blox.com/support.](http://www.u-blox.com/support)