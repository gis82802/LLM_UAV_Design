# **C101-D9C**

### **Application board (rev. C)**

**User guide**



### **Abstract**

This document explains the use of C101-D9C application board. The C101-D9C board enables customers to evaluate QZSS L6 correction services with the NEO-D9C correction data receiver.





### <span id="page-1-0"></span>**Document information**

| Title                  | C101-D9C                   |             |
|------------------------|----------------------------|-------------|
| Subtitle               | Application board (rev. C) |             |
| Document type          | User guide                 |             |
| Document number        | UBX-21009111               |             |
| Revision and date      | R02                        | 17-Jan-2022 |
| Disclosure restriction | C1-Public                  |             |

### This document applies to the following products:

| Product name | Type number   | Firmware version | PCN reference |
|--------------|---------------|------------------|---------------|
| C101-D9C     | C101-D9C-0-00 | FW QZS 1.01      | N/A           |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.



<span id="page-2-0"></span>

|   | Document information 2                        |  |
|---|-----------------------------------------------|--|
|   | Contents 3                                    |  |
| 1 | Introduction4                                 |  |
|   | 1.1<br>Package contents 4                     |  |
| 2 | C101-D9C product overview5                    |  |
|   | 2.1<br>Components5                            |  |
|   | 2.2<br>Jumpers6                               |  |
| 3 | C101-D9C standalone operation7                |  |
| 4 | C101-D9C operation with C099-F9P9             |  |
|   | 4.1<br>C101-D9C/C099-F9P via Arduino shield10 |  |
|   | Appendix  12                                  |  |
| A | Glossary  12                                  |  |
| B | Antenna specification (L1/L2/E5b/L6) 12       |  |
| C | C101-D9C schematics 13                        |  |
|   | Related documentation 16                      |  |
|   | Revision history  16                          |  |
|   | Contact 17                                    |  |



## <span id="page-3-0"></span>**1 Introduction**

The C101-D9C board is a convenient tool that allows customers to become familiar with the u-blox NEO-D9C QZSS L6 receiver. The board provides facilities for evaluating the product and demonstrating its key features.

NEO-D9C is a QZSS L6 receiver that brings QZSS Centimeter Level Augmentation Service (CLAS) support to u-blox GNSS modules, enabling centimeter-level navigation. The receiver can also track the experimental MADOCA service transmitted on the QZSS L6 signal.

The C101-D9C application board offers:

- NEO-D9C module for use as QZSS L6 correction data receiver
- USB connection for communication and power supply
- L6 antenna connection for receiving the satellite data stream
- Arduino shield connection

### <span id="page-3-1"></span>**1.1 Package contents**

The delivered package contains:

- C101-D9C board
- Multiband antenna (L1/L2/E5b/L6)
- Antenna ground plane (12 cm circular)
- USB interconnect cable
- Jumper connectors

Prior to using the board, it is useful to download the appropriate evaluation software and keep handy the documents listed in the Related documents section.



## <span id="page-4-0"></span>**2 C101-D9C product overview**

### <span id="page-4-1"></span>**2.1 Components**

C101-D9C houses the NEO-D9C QZSS L6 receiver. The board is powered from the USB cable connection or via Arduino shield. The main components of the board are listed below and shown in [Figure 1](#page-4-2) and [Figure 2:](#page-5-1)

- Native USB port
- FTDI USB bridge
- SMA RF connector and antenna supply capability (L-band)
- UART2 interface through Arduino shield
- NEO-D9C RESET button
- NEO-D9C SAFEBOOT button



<span id="page-4-2"></span>**Figure 1: C101-D9C block diagram**





**Figure 2: C101-D9C quick start basic overview**

### <span id="page-5-1"></span><span id="page-5-0"></span>**2.2 Jumpers**

The board is delivered with the following default jumpers:

- **J6**: This jumper provides 3.3 V power supply to an external active antenna plugged to the SMA RF connector. The current limit circuit is also enabled up to 60 mA.
- **J8**: This jumper switches the communication from the UART2 of the NEO-D9C to the UART1 or UART2 of the C099-F9P, when connected via the Arduino shield (refer to section [4.1](#page-9-0) for further details).



**Figure 3: C101-D9C jumpers overview**

For further details, see the C101-D9C schematic in Appendix [C.](#page-12-0)



### <span id="page-6-0"></span>**3 C101-D9C standalone operation**

This section provides some quicksteps to enable NEO-D9C standalone operation and connecting via u-center (see u-center user guide [\[3\]\)](#page-15-2).

- Connect the supplied L6 band antenna to the RF SMA connector.
- Connect the USB to a Windows PC, this will power the board. The FTDI and USB drivers will be installed automatically from Windows Update when you connect the board for the first time.
- The power LED will turn on in blue color.
- Start the Device Manager utility from Windows. Two new ports will be visible under the Ports tab: the USB Serial Device is the Native USB port and the USB Serial Port is the FTDI USB bridge port, as shown in [Figure 5.](#page-6-1)



### **Figure 4: Windows Device Manager Ports identifications**

| USB Serial Device (COM47) Properties | ×                 |   | <b>USB Serial Port (COM48) Properties</b> |                                                       |  |
|--------------------------------------|-------------------|---|-------------------------------------------|-------------------------------------------------------|--|
| Driver<br>General Port Settings      | Details Events    |   | General Port Settings Driver              | Details Events                                        |  |
| USB Serial Device (COM47)            |                   | - | USB Serial Port (COM48)                   |                                                       |  |
| Driver Provider:<br>Microsoft        |                   |   | Driver Provider:                          | u-blox AG                                             |  |
| 6/21/2006<br>Driver Date:            |                   |   | Driver Date:                              | 2/24/2017                                             |  |
| 10.0.18362.1<br>Driver Version:      |                   |   | Driver Version:                           | 2.12.26.0                                             |  |
| Digital Signer:                      | Microsoft Windows |   | Digital Signer:                           | Microsoft Windows Hardware Compatibility<br>Publisher |  |

<span id="page-6-1"></span>**Figure 5: FTDI USB bridge and USB ports properties**

- Start u-center and connect to one of the COM ports. If you are using the FTDI USB bridge, make sure the baud rate in u-center is set to 9600.
- Poll UBX-MON-VER message and check the content as shown in [Figure 6](#page-6-2) .

| EXT CORE 1.00 (d716bf)                                                               |
|--------------------------------------------------------------------------------------|
| Hardware Version                                                                     |
| 100190000                                                                            |
| Extension[s]                                                                         |
| ROM BASE 0x118B2060<br>FWVER=0ZS 1.01<br>PROTVER=26.00<br>MOD=NEO-D9C<br>GPS<br>QZSS |

<span id="page-6-2"></span>**Figure 6: UBX-MON-VER message**



• Poll or enable the UBX-RXM-QZSSL6 message to check the received correction data.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Decoder Ch A                                                                            | Decoder Ch B                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Version:<br>Time Tag [ms]:<br>Error Status:<br>SV-ID:<br>L6 Channel:<br>C/N0 [dBHz]:<br>Message Name:<br>Group Delay [ns]:<br>PRN:<br>Vendor-ID:<br>MGF-ID:<br>Subframe Indicator:<br>Alert:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1<br>726926419<br>Error-free<br>3<br>0<br>38.824<br>L6D<br>3<br>195<br>5<br>1<br>0<br>Ũ | Version:<br>Time Tag [ms]:<br>Error Status:<br>SV-ID:<br>L6 Channel:<br>C/NO [dBHz]:<br>Message Name:<br>Group Delay [ns]:<br>PRN:<br>Vendor-ID:<br>MGF-ID:<br>Subframe Indicator:<br>Alert:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1<br>726926424<br>Error-free<br>2<br>$\mathbf{1}$<br>36.965<br>L6D<br>5<br>194<br>5<br>1<br>$\theta$<br>n |
| QZSS L6 Message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | QZSS L6 Message                                                                                           |
| 0x1A CF FC 1D C3 A8 37 CC 49 15 99 59 7F FF<br>0xFF 70 0B 04 7C BF 83 FF F4 43 43 C8 5A 00<br>0x2B 3F AE F4 7F 7F CC 00 05 50 DB 40 A7 FF<br>0xC0 10 0B BC 7C 3C 44 3C 03 C0 00 5B 7F A3<br>0x00 20 0C 34 04 BF C0 87 BC 4B F3 C4 1A 40<br>0xBB FF 70 08 3B C0 83 BC 43 B8 03 B0 07 DA<br>0x40 D6 FF A0 11 00 08 03 BC CB FC 8B FB C4<br>0x9D 40 45 FF 90 10 00 00 00 3B C3 C7 C0 40<br>0x40 5D 7F 79 FF B0 0B 38 88 00 04 44 00 84<br>0x00 44 1C 40 27 FF 30 09 38 40 C8 40 00 44<br>0x40 3C 84 1D 40 16 FF F0 0F 13 80 7F 40 3F<br>0xBB C0 7F C4 9C 40 FA FF 60 0E 00 C0 BF C0<br>0x7F F8 44 03 84 DC 3F C7 2E EE BC C4 C4 5C<br>0xC8 B5 CC 1B 00 94 3C 04 00 03 F7 87 FB C4<br>0x87 DA 3F 67 07 FF 6C 40 03 48 C8 81 15 1B<br>0x00 04 04 7F AC 8C C3 0C 40 9E AE C8 7E D3<br>0xE5 40 70 2E F8 3B F6 A5 15 7B 21 5B 71 D1<br>0x1C EE 9D 27 9C FE 54 D3 76 25 3D 62 |                                                                                         | 0x1A CF FC 1D C2 A8 37 CC 49 15 99 59 7F FF<br>0xFF 70 0B 04 7C BF 83 FF F4 43 43 C8 5A 00<br>0x2B 3F AE F4 7F 7F CC 00 05 50 DB 40 A7 FF<br>0xC0 10 0B BC 7C 3C 44 3C 03 C0 00 5B 7F A3<br>0x00 20 0C 34 04 BF C0 87 BC 4B F3 C4 1A 40<br>0x40 D6 FF A0 11 00 08 03 BC CB FC 8B FB C4<br>0x9D 40 45 FF 90 10 00 00 00 3B C3 C7 C0 40<br>0x40 5D 7F 79 FF B0 0B 38 88 00 04 44 00 84<br>0x00 44 1C 40 27 FF 30 09 38 40 C8 40 00 44<br>0x40 3C 84 1D 40 16 FF F0 0F 13 80 7F 40 3F<br>0xBB C0 7F C4 9C 40 FA FF 60 0E 00 C0 BF C0<br>0xC8 B5 CC 1B 00 94 3C 04 00 03 F7 87 FB C4<br>0x87 DA 3F 67 07 FF 6C 40 03 48 C8 81 15 1B<br>0x00 04 04 7F AC 8C C3 0C 4A 4F 07 F2 CF 2F<br>0xC8 09 03 1F 85 08 0C F4 C2 3B 22 B7 84 FA<br>0x45 7C AE 59 30 7F B8 EA 5E 4D A2 94 | 0xBB FF 70 08 3B C0 83 BC 43 B8 03 B0 07 DA<br>0x7F F8 44 03 84 DC 3F C7 2E EE BC C4 C4 5C                |

### **Figure 7: UBX-RXM-QZSSL6 message**

For further details regarding the UBX-RXM-QZSSL6 message, see the related Interface description [\[4\].](#page-15-3)



### <span id="page-8-0"></span>**4 C101-D9C operation with C099-F9P**

It is possible to use the C101-D9C board together with C099-F9P. [Figure 9](#page-9-1) shows how to interface the C101-D9C board with the C099-F9P board. Two types of connections are available:

- USB interface (through PC)
- Arduino shield interface (UART2 direct connection)

When the USB connection is used, the corrections are provided through the host computer. Security checks and data conversion are the responsibility of the user application, as well as the forwarding of the corrections to the ZED-F9P.



**Figure 8: C101-D9C - C099-F9P interfacing scheme**

The provided multiband antenna can be used in combination for ZED-F9P and NEO-D9C, RF signal splitter is needed. For further details, see the antenna specification in Appendi[x B.](#page-11-2)



### <span id="page-9-0"></span>**4.1 C101-D9C/C099-F9P via Arduino shield**

[Figure 9](#page-9-1) shows the placement of the Arduino connectors on the C101-D9C board and [Figure 10](#page-9-2) shows how to physically connect the C099-F9P board to the C101-D9C board via the Arduino shield. Jumper J18 on the C099 board is needed for the ZED-F9P to receive the correction data on UART1 port. See the C099 application board User guid[e \[5\]](#page-15-4) for further details.



**Figure 9: C101-D9C Arduino connectors**

<span id="page-9-2"></span><span id="page-9-1"></span>

**Figure 10: Connecting C101-D9C to C099-F9P**



Depending on the position of the jumper J8 on the C101-D9C board (as shown following) the ZED-F9P housed on the C099-F9P board will receive the correction data on the UART1 or UART2:



The ZED-F9P receives the correction data on UART1.



The ZED-F9P receives the correction data on UART2.

For further details, see the C101-D9C schematic in Appendix [C.](#page-12-0)

UBX protocol needs to be enabled in output on the UART2 interface of the NEO-D9C to allow the communication, using the following configuration item:

### **CFG-UART2OUTPROT-UBX=1**

For further details regarding receiver configuration, see the related Interface descriptio[n \[4\].](#page-15-3)



## <span id="page-11-0"></span>**Appendix**

### <span id="page-11-1"></span>**A Glossary**

| Abbreviation | Definition                                  |
|--------------|---------------------------------------------|
| FTDI         | Future Technology Device International      |
| GEO          | Geostationary Earth Orbit                   |
| LED          | Light Emitting Diode                        |
| LNA          | Low Noise Amplifier                         |
| RF           | Radio Frequency                             |
| QZSS         | Quasi Zenith Satellite System               |
| RHCP         | Right Hand Circular Polarized               |
| SMA          | Subminiature version A                      |
| UART         | Universal Asynchronous Receiver Transmitter |
| USB          | Universal Serial Bus                        |
|              |                                             |

**Table 1: Explanation of the abbreviations and terms used**

## <span id="page-11-2"></span>**B Antenna specification (L1/L2/E5b/L6)**

The following is an overview of the provided Inpaq L6 antenna, GPSLX09U8W-S6-07-B:

| <b>Characteristics</b> |                         | <b>Specification</b> |  |
|------------------------|-------------------------|----------------------|--|
|                        | L1: 1561~1610 MHz       |                      |  |
| <b>Frequency Range</b> | L2/L5/L6: 1197~1285 MHz |                      |  |
|                        | <b>1561 MHz</b>         | 5.2 dBic             |  |
|                        | 1575.42 MHz             | 5.7 dBic             |  |
|                        | 1602 MHz                | 3.3 dBic             |  |
| Peak Gain              | <b>1610 MHz</b>         | 2.3 dBic             |  |
|                        | <b>1197 MHz</b>         | 0.7 dBic             |  |
|                        | 1227.6 MHz              | 5.4 dBic             |  |
|                        | 1278.75 MHz             | 3.4 dBic             |  |
|                        | <b>1285 MHz</b>         | 2.9 dBic             |  |
| Polarization           | <b>RHCP</b>             |                      |  |
| <b>Axial Ratio</b>     | 3.0 dB typ.             |                      |  |
| <b>VSWR</b>            | 2.0 typ.                |                      |  |
| Impedance              | 50 ohm                  |                      |  |



| <b>Characteristics</b>             |                                             | <b>Specification</b> |            |
|------------------------------------|---------------------------------------------|----------------------|------------|
| <b>Frequency Range</b>             | L1:1561~1610 MHz<br>L2/L5/L6: 1197~1285 MHz |                      |            |
|                                    | <b>1561 MHz</b>                             | 35.0±3.0 dB          |            |
|                                    | 1575.42 MHz                                 | 37.0±3.0 dB          |            |
|                                    | <b>1602 MHz</b>                             | 35.0±3.0 dB          |            |
| Gain                               | <b>1610 MHz</b>                             | 34.0±3.0 dB          |            |
|                                    | <b>1197 MHz</b>                             | 34.0±3.0 dB          |            |
|                                    | 1227.6 MHz                                  | 34.0±3.0 dB          |            |
|                                    | 1278.75 MHz                                 | 34.0±3.0 dB          |            |
|                                    | 1285 MHz                                    | 34.0±3.0 dB          |            |
| <b>Noise Figure</b>                | $2.0$ dB typ.                               |                      |            |
|                                    | $F_1 = 1561$ MHz                            | $F_1$ -50 MHz        | > 75 dB    |
|                                    |                                             | $F_1$ -100 MHz       | $> 75$ dB  |
|                                    | $F_{2} = 1610 \text{ MHz}$                  | $F2+50$ MHz          | > 65 dB    |
| <b>Filter Out Band Attenuation</b> |                                             | $F2+100 MHz$         | > 65 dB    |
|                                    | $F_{3} = 1197$ MHz                          | $F_3$ -50 MHz        | $> 0.5$ dB |
|                                    |                                             | $F_{3}$ -100 MHz     | $>10$ dB   |
|                                    | $F_4 = 1285$ MHz                            | $F_4 + 50$ MHz       | > 5 dB     |
|                                    |                                             | $F_4$ +100 MHz       | >35 dB     |
| <b>Output VSWR</b>                 | 2.0 typ.                                    |                      |            |
| <b>Operation Voltage</b>           | $3.0 - 5.0 V$                               |                      |            |
| <b>Current</b>                     | 31.0±3.0 mA                                 |                      |            |

| <b>Characteristics</b>   |                         | <b>Specification</b> |  |
|--------------------------|-------------------------|----------------------|--|
|                          | L1:1561~1610 MHz        |                      |  |
| <b>Frequency Range</b>   | L2/L5/L6: 1197~1285 MHz |                      |  |
|                          | 1561 MHz                | 40.2±3.0 dB          |  |
|                          | 1575.42 MHz             | 42.7±3.0 dB          |  |
|                          | 1602 MHz                | 38.3±3.0 dB          |  |
| Gain                     | <b>1610 MHz</b>         | 36.3±3.0 dB          |  |
|                          | <b>1197 MHz</b>         | 34.7±3.0 dB          |  |
|                          | 1227.6 MHz              | 39.4±3.0 dB          |  |
|                          | 1278.75 MHz             | 37.4±3.0 dB          |  |
|                          | 1285 MHz                | 36.9±3.0 dB          |  |
| <b>Output VSWR</b>       | 2.0 typ.                |                      |  |
| <b>Operation Voltage</b> | $3.0 - 5.0V$            |                      |  |
| <b>Current</b>           | 31.0±3.0 mA             |                      |  |

See the NEO-D9C Integration manual [\[1\]](#page-15-5) for further details.

### <span id="page-12-0"></span>**C C101-D9C schematics**

The following pages show the complete schematics for the C101-D9C evaluation board.











### <span id="page-15-0"></span>**Related documentation**

- <span id="page-15-5"></span>[1] NEO-D9C Integration manual, UBX- [21031631](http://www.u-blox.com/docs/UBX-18069679)
- [2] ZED-F9P Integration manual[, UBX-18010802](http://www.u-blox.com/docs/UBX-18010802)
- <span id="page-15-2"></span>[3] u-center User guide, [UBX-13005250](http://www.u-blox.com/docs/UBX-13005250)
- <span id="page-15-3"></span>[4] u-blox D9 QZS 1.01 Interface description, UBX- [21031777](https://www.u-blox.com/en/docs/UBX-17058272)
- <span id="page-15-4"></span>[5] C099 AppBoard User guide, UBX[-18055649](https://www.u-blox.com/en/docs/UBX-18055649)

**☞** For product change notifications and regular updates of u-blox documentation, register on our website, [www.u-blox.com.](http://www.u-blox.com/)

### <span id="page-15-1"></span>**Revision history**

| Revision | Date        | Name | Comments                                                                                                                                |
|----------|-------------|------|-----------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 20-Apr-2021 | dama | Initial release                                                                                                                         |
| R02      | 17-Jan-2022 | dama | C1-Public disclosure restriction<br>Firmware name update<br>Chapter 4 general update regarding UART2<br>Related document section update |



### <span id="page-16-0"></span>**Contact**

### For complete contact information, visit us at [www.u-blox.com.](http://www.u-blox.com/)

### **u-blox Offices**

### **North, Central and South America**

#### **u-blox America, Inc.**

Phone: +1 703 483 3180 Email: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Regional Office West Coast:**

Phone: +1 408 573 3640 Email: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Technical Support:**

Phone: +1 703 483 3185 Email: [support\\_us@u-blox.com](mailto:support_us@u-blox.com)

### **Headquarters Europe, Middle East, Africa**

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

### **Regional Office Japan (Osaka):**

Phone: +81 6 6941 3660 Email: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

### **Regional Office Japan (Tokyo):**

Phone: +81 3 5775 3850 Email: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

### **Regional Office Korea:**

Phone: +82 2 542 0861 Email: [info\\_kr@u-blox.com](mailto:info_kr@u-blox.com) Support: [support\\_kr@u-blox.com](mailto:support_kr@u-blox.com)

### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 Email: [info\\_tw@u-blox.com](mailto:info_tw@u-blox.com) Support: [support\\_tw@u-blox.com](mailto:support_tw@u-blox.com)