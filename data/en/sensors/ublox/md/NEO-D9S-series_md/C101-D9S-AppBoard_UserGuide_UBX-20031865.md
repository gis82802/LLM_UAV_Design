

# **C101-D9S**

### **Application board (rev. C)**

**User guide**



### **Abstract**

This document explains the use of C101-D9S application board. The C101-D9S board enables customers to evaluate L-band GNSS correction services with the NEO-D9S correction data receiver.





### <span id="page-1-0"></span>**Document information**

| Title                  | C101-D9S                   |             |
|------------------------|----------------------------|-------------|
| Subtitle               | Application board (rev. C) |             |
| Document type          | User guide                 |             |
| Document number        | UBX-20031865               |             |
| Revision and date      | R03                        | 17-Jan-2022 |
| Disclosure restriction | C1-Public                  |             |

### This document applies to the following products:

| Product name | Type number   | Firmware version | PCN reference |
|--------------|---------------|------------------|---------------|
| C101-D9S     | C101-D9S-0-00 | PMP 1.04         | N/A           |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.

<span id="page-2-0"></span>

|   | Document information 2            |  |
|---|-----------------------------------|--|
|   | Contents 3                        |  |
| 1 | Introduction4                     |  |
|   | 1.1<br>Package contents 4         |  |
| 2 | C101-D9S product overview5        |  |
|   | 2.1<br>Components5                |  |
|   | 2.2<br>Jumpers6                   |  |
| 3 | C101-D9S standalone operation7    |  |
| 4 | C101-D9S operation with C099-F9P9 |  |
|   | Appendix  11                      |  |
| A | Glossary  11                      |  |
| B | NEO-D9S L-band configurations 11  |  |
| C | L-band antenna specification  12  |  |
| D | C101-D9S schematics 12            |  |
|   | Related documentation 15          |  |
|   | Revision history  15              |  |
|   | Contact 16                        |  |



## <span id="page-3-0"></span>**1 Introduction**

The C101-D9S board is a convenient tool that allows customers to become familiar with the u-blox NEO-D9S L-band correction data receiver. The board provides facilities for evaluating the product and demonstrating its key features.

NEO-D9S is a satellite data receiver for L-band correction broadcasts and can be configured for use with a variety of correction services. Using such correction services enables high precision navigation globally in multiple regions, as well as coverage across continents.

The C101-D9S application board offers:

- NEO-D9S module for use as L-band correction data receiver
- USB connection for communication and power supply
- L-band antenna connection for receiving the satellite data stream
- Arduino shield connection

### <span id="page-3-1"></span>**1.1 Package contents**

The delivered package contains:

- C101-D9S board
- L-band antenna
- Antenna ground plane (12 cm circular)
- USB interconnect cable
- Jumper connectors

Prior to using the board, it is useful to download the appropriate evaluation software and keep handy the documents listed in the Related documents section.



## <span id="page-4-0"></span>**2 C101-D9S product overview**

### <span id="page-4-1"></span>**2.1 Components**

C101-D9S houses the NEO-D9S L-band correction data receiver. The board is powered from the USB cable connection or via Arduino shield. The main components of the board are listed below and shown in [Figure 1](#page-4-2) and [Figure 2:](#page-5-1)

- Native USB port
- FTDI USB bridge
- SMA RF connector and antenna supply capability (L-band)
- UART2 interface through Arduino shield
- NEO-D9S RESET button
- NEO-D9S SAFEBOOT button



<span id="page-4-2"></span>**Figure 1: C101-D9S block diagram**





<span id="page-5-1"></span>**Figure 2: C101-D9S quick start basic overview**

### <span id="page-5-0"></span>**2.2 Jumpers**

The board is delivered with the following default jumpers:

- **J6**: This jumper provides 3.3 V power supply to an external active antenna plugged to the SMA RF connector. The current limit circuit is also enabled up to 60 mA.
- **J8**: This jumper switches the communication from the UART2 of the NEO-D9S to the J2 or J3 connector of the Arduino shield (refer to Appendi[x D](#page-11-1) for further details).

### **Figure 3: C101-D9S jumpers overview**

For further details, see the C101-D9S schematic in Appendix [D.](#page-11-1)



### <span id="page-6-0"></span>**3 C101-D9S standalone operation**

This section provides some quicksteps to enable NEO-D9S standalone operation, and connecting via u-center (see u-center user guide [\[3\]\)](#page-14-2).

- Connect the supplied L-band antenna to the RF SMA connector. Ensure good visibility of the GEO communication satellites.
- Connect the USB to a Windows PC, this will power the board. The FTDI and USB drivers will be installed automatically from Windows Update when the user connects the board for the first time.
- The power LED will turn on in blue.
- Start the Device Manager utility from Windows. Two new ports will be visible under the Ports tab: the USB Serial Device is the Native USB port and the USB Serial Port is the FTDI USB bridge port, as shown in [Figure](#page-6-1) [4.](#page-6-1)



### <span id="page-6-1"></span>**Figure 4: Windows Device Manager Ports identifications**

| USB Serial Device (COM47) Properties                        | × | $\times$<br><b>USB Serial Port (COM48) Properties</b>                    |
|-------------------------------------------------------------|---|--------------------------------------------------------------------------|
| Driver<br><b>Port Settings</b><br>Details Events<br>General |   | General Port Settings Driver<br>Details Events                           |
| USB Serial Device (COM47)<br>e                              |   | USB Serial Port (COM48)<br>s                                             |
| Driver Provider:<br>Microsoft                               |   | Driver Provider:<br>u-blox AG                                            |
| 6/21/2006<br>Driver Date:                                   |   | 2/24/2017<br>Driver Date:                                                |
| 10.0.18362.1<br>Driver Version:                             |   | 2.12.26.0<br>Driver Version:                                             |
| Microsoft Windows<br>Digital Signer:                        |   | Microsoft Windows Hardware Compatibility<br>Digital Signer:<br>Publisher |

**Figure 5: FTDI USB bridge and USB ports properties**

- Start u-center and connect to one of the COM ports. If you are using the FTDI USB bridge, make sure the baud rate in u-center is set to 9600.
- Poll UBX-MON-VER message and check the content as shown i[n Figure](#page-7-0) [6.](#page-7-0)



### <span id="page-7-0"></span>**Figure 6: UBX-MON-VER message**

NEO-D9S needs to be properly configured to receive the L-band signal correction data. See Appendix [B](#page-10-2) for the default NEO-D9S L-band configuration, which can be adapted for other services.

The messages UBX-MON-PMP and UBX-RXM-PMP (see [Figure 7](#page-7-1) and [Figure 8\)](#page-7-2) can be polled or enabled to check respectively the reception of the signal and the decoded correction data.

| locked | frameSync | timeTag | lockTime | centerFrequency | cno | cnoFrac |  |
|--------|-----------|---------|----------|-----------------|-----|---------|--|
|        |           | 6150000 | 2065000  | 1545490434      | 45  | 0.09    |  |
|        |           |         |          |                 |     |         |  |
|        |           |         |          |                 |     |         |  |
|        |           |         |          |                 |     |         |  |

### <span id="page-7-1"></span>**Figure 7: UBX-MON-PMP message**

### <span id="page-7-2"></span>**Figure 8: UBX-RXM-PMP message**



## <span id="page-8-0"></span>**4 C101-D9S operation with C099-F9P**

It is possible to use the C101-D9S board together with C099-F9P[. Figure 9](#page-8-1) shows how to interface the C101-D9S board with the C099-F9P board.



### <span id="page-8-1"></span>**Figure 9: C101-D9S - C099-F9P interfacing scheme**

[Figure 10](#page-8-2) shows the placement of the Arduino connectors on the C101-D9S board and [Figure](#page-9-0) **[11](#page-9-0)** shows how to physically connect the C099-F9P board to the C101-D9S board via the Arduino shield. Jumper J18 on the C099 board is needed for the ZED-F9P to receive the correction data on the UART1 port. See the C099 application board User guid[e \[4\]](#page-14-3) for further details.

<span id="page-8-2"></span>

**Figure 10: C101-D9S Arduino connectors**





**Figure 11: Connecting C101-D9S to C099-F9P**

<span id="page-9-0"></span>Depending on the position of jumper J8 on the C101-D9S board (as shown below) the ZED-F9P housed on the C099-F9P board will receive the correction data on the UART1 or the UART2 port:



The ZED-F9P receives the correction data on UART1 port.



The ZED-F9P receives the correction data on UART2 port.

For further details, see the C101-D9S schematic in Appendix [D.](#page-11-1)

UBX protocol needs to be enabled in output on the UART2 interface of the NEO-D9S to allow the

communication, using the following configuration item:

### **CFG-UART2OUTPROT-UBX=1**

For further details regarding receiver configuration, see the related Interface description [\[5\].](#page-14-4)



## <span id="page-10-0"></span>**Appendix**

## <span id="page-10-1"></span>**A Glossary**

| Abbreviation | Definition                                  |
|--------------|---------------------------------------------|
| FTDI         | Future Technology Device International      |
| GEO          | Geostationary Earth Orbit                   |
| LED          | Light Emitting Diode                        |
| LNA          | Low Noise Amplifier                         |
| RF           | Radio Frequency                             |
| RHCP         | Right Hand Circular Polarized               |
| SMA          | SubMiniature version A                      |
| UART         | Universal Asynchronous Receiver Transmitter |
| USB          | Universal Serial Bus                        |

**Table 1: Explanation of the abbreviations and terms used**

### <span id="page-10-2"></span>**B NEO-D9S L-band configurations**

Correction services from several providers are available via the L-band communication satellites. The service provider will have several correction service specific configurations that need to be configured before the receiver can provide the relevant service provider data such as:

- Service provider service ID
- Service provider frequency based on geographical location
- Service provider data rate

This means that the frequency allocation for a particular service provider could change. Service providers do provide information on any frequency changes when required.

The NEO-D9S default L-band configuration keys are listed below:

- CFG-PMP-CENTER\_FREQUENCY = 1539812500 Hz
- CFG-PMP-SEARCH\_WINDOW = 2200 Hz
- CFG-PMP-USE\_SERVICE\_ID = 1 (true)
- CFG-PMP-SERVICE\_ID = 50821
- CFG-PMP-DATA\_RATE = 2400 (B2400) bps
- CFG-PMP-USE\_DESCRAMBLER = 1 (true)
- CFG-PMP-DESCRAMBLER\_INIT = 23560
- CFG-PMP-USE\_PRESCRAMBLING = 0 (false)
- CFG-PMP-UNIQUE\_WORD = 16238547128276412563

The NEO-D9S correction data receiver is fully compliant with the u-blox configuration concept. The messages UBX-CFG-VALSET, UBX-CFG-VALGET and UBX-CFG-VALDEL are used to configure the above keys. See the NEO-D9S Integration manual [\[1\]](#page-14-5) for further details.



### <span id="page-11-0"></span>**C L-band antenna specification**

The following is an overview of the provided Inpaq L-band antenna, LBAND01D-S6-00:

| <b>Characteristics</b> |                 | <b>Specification</b> |
|------------------------|-----------------|----------------------|
| <b>Frequency Range</b> | 1525~1559 MHz   |                      |
|                        | <b>1525 MHz</b> | 3.8 dBic             |
| Peak Gain              | 1537.5 MHz      | $5.6$ dBic           |
|                        | <b>1550 MHz</b> | $3.8$ dBic           |
|                        | <b>1559 MHz</b> | $1.3$ dBic           |
| Polarization           | <b>RHCP</b>     |                      |
| <b>Axial Ratio</b>     | $3.0$ dB typ.   |                      |
| <b>VSWR</b>            | $2.0$ typ.      |                      |
| Impedance              | 50 ohm          |                      |

| <b>Characteristics</b>             | <b>Specification</b> |                |           |  |
|------------------------------------|----------------------|----------------|-----------|--|
| <b>Frequency Range</b>             | 1525~1559 MHz        |                |           |  |
|                                    | <b>1525 MHz</b>      | 27.0±3.0 dB    |           |  |
| Gain                               | 1537.5 MHz           | 27.0±3.0 dB    |           |  |
|                                    | <b>1550 MHz</b>      | 27.0±3.0 dB    |           |  |
|                                    | <b>1559 MHz</b>      | 26.0±3.0 dB    |           |  |
| Noise Figure                       | $2.0$ dB typ.        |                |           |  |
|                                    | $F_1$ = 1525 MHz     | $F_1$ -50 MHz  | $>65$ dB  |  |
| <b>Filter Out Band Attenuation</b> |                      | $F_1$ -100 MHz | $> 70$ dB |  |
|                                    | $F_2$ = 1559 MHz     | $F2+50$ MHz    | $>65$ dB  |  |
|                                    |                      | $F2+100 MHz$   | > 75 dB   |  |
| <b>Output VSWR</b>                 | 2.0 typ.             |                |           |  |
| <b>Operation Voltage</b>           | $3.0 - 5.0 V$        |                |           |  |
| <b>Current</b>                     | $13.0 \pm 3.0$ mA    |                |           |  |

| <b>Characteristics</b>   |                 | <b>Specification</b>        |
|--------------------------|-----------------|-----------------------------|
| <b>Frequency Range</b>   | 1525~1550 MHz   |                             |
|                          | 1525 MHz        | $30.8 \pm 3.0$ dB           |
| Gain                     | 1537.5 MHz      | $32.6 \pm 3.0 \, \text{dB}$ |
|                          | <b>1550 MHz</b> | 30.8±3.0 dB                 |
|                          | 1559 MHz        | 27.3±3.0 dB                 |
| 'Output VSWR             | $2.0$ typ.      |                             |
| <b>Operation Voltage</b> | $3.0 - 5.0 V$   |                             |
| <b>Current</b>           | 13.0±3.0 mA     |                             |

See the NEO-D9S Integration manual [\[1\]](#page-14-5) for further details.

### <span id="page-11-1"></span>**D C101-D9S schematics**

The following pages show the complete schematics for the C101-D9S evaluation board.











### <span id="page-14-0"></span>**Related documentation**

- <span id="page-14-5"></span>[1] NEO-D9S Integration manual[, UBX-19026111](http://www.u-blox.com/docs/UBX-19026111)
- [2] ZED-F9P Integration manual[, UBX-18010802](http://www.u-blox.com/docs/UBX-18010802)
- <span id="page-14-2"></span>[3] u-center User guide, [UBX-13005250](http://www.u-blox.com/docs/UBX-13005250)
- <span id="page-14-3"></span>[4] C099 application board User guide, UBX- 18063024
- <span id="page-14-4"></span>[5] U-blox D9 PMP 1.04 Interface description, UBX- [21040023](https://dms.u-blox.com/share/proxy/alfresco/api/node/content/workspace/SpacesStore/50aa960a-e94d-40be-85f2-a6f928d33aed/u-blox-D9-PMP-1.04_InterfaceDescription_UBX-21040023.pdf?a=true)

**☞** For product change notifications and regular updates of u-blox documentation, register on our website, [www.u-blox.com.](http://www.u-blox.com/)

### <span id="page-14-1"></span>**Revision history**

| Revision | Date        | Name | Comments                                        |
|----------|-------------|------|-------------------------------------------------|
| R01      | 30-Jul-2020 | dama | Initial release                                 |
| R02      | 24-Jun-2021 | dama | Add chapter 4: C101-D9S operation with C099-F9P |
| R03      | 17-Jan-2022 | dama | Chapter 4 update                                |



### <span id="page-15-0"></span>**Contact**

### For complete contact information, visit us at [www.u-blox.com.](http://www.u-blox.com/)

### **u-blox Offices**

### **North, Central and South America**

#### **u-blox America, Inc.**

Phone: +1 703 483 3180 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Regional Office West Coast:**

Phone: +1 408 573 3640 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Technical Support:**

Phone: +1 703 483 3185 E-mail: [support\\_us@u-blox.com](mailto:support_us@u-blox.com)

### **Headquarters Europe, Middle East, Africa**

#### **u-blox AG**

Phone: +41 44 722 74 44 E-mail: [info@u-blox.com](mailto:info@u-blox.com) Support: [support@u-blox.com](mailto:support@u-blox.com)

#### **Asia, Australia, Pacific**

#### **u-blox Singapore Pte. Ltd.**

Phone: +65 6734 3811 E-mail: [info\\_ap@u-blox.com](mailto:info_ap@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

### **Regional Office Australia:**

Phone: +61 3 9566 7255 E-mail: [info\\_anz@u-blox.com](mailto:info_anz@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

#### **Regional Office China (Beijing):**

Phone: +86 10 68 133 545 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Chongqing):**

Phone: +86 23 6815 1588 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Shanghai):**

Phone: +86 21 6090 4832 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office China (Shenzhen):**

Phone: +86 755 8627 1083 E-mail: [info\\_cn@u-blox.com](mailto:info_cn@u-blox.com) Support: [support\\_cn@u-blox.com](mailto:support_cn@u-blox.com)

#### **Regional Office India:**

Phone: +91 80 405 092 00 E-mail: [info\\_in@u-blox.com](mailto:info_in@u-blox.com) Support: [support\\_in@u-blox.com](mailto:support_in@u-blox.com)

### **Regional Office Japan (Osaka):**

Phone: +81 6 6941 3660 E-mail: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

### **Regional Office Japan (Tokyo):**

Phone: +81 3 5775 3850 E-mail: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

### **Regional Office Korea:**

Phone: +82 2 542 0861 E-mail: [info\\_kr@u-blox.com](mailto:info_kr@u-blox.com) Support: [support\\_kr@u-blox.com](mailto:support_kr@u-blox.com)

### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 E-mail: [info\\_tw@u-blox.com](mailto:info_tw@u-blox.com) Support: [support\\_tw@u-blox.com](mailto:support_tw@u-blox.com)