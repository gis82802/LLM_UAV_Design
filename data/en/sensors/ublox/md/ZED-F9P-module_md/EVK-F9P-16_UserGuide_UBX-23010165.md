

# **EVK-F9P-16**

### **Evaluation kit**

**User guide**



#### **Abstract**

This document describes the structure and use of the EVK-F9P evaluation kit and provides information for evaluating and testing u-blox F9 high precision positioning technology.





### <span id="page-1-0"></span>**Document information**

| Title                  | EVK-F9P-16     |            |
|------------------------|----------------|------------|
| Subtitle               | Evaluation kit |            |
| Document type          | User guide     |            |
| Document number        | UBX-23010165   |            |
| Revision and date      | R02            | 7-Nov-2023 |
| Disclosure restriction | C1- Public     |            |

| Product status                   | Corresponding content status |                                                                                        |  |  |
|----------------------------------|------------------------------|----------------------------------------------------------------------------------------|--|--|
| In development /<br>Prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                 |  |  |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be published later.   |  |  |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be published later. |  |  |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                     |  |  |

#### This document applies to the following products:

| Product name<br>Ordering code |               | Application version<br>Firmware version |  | PCN reference | Product status     |
|-------------------------------|---------------|-----------------------------------------|--|---------------|--------------------|
| EVK-F9P-16                    | EVK-F9P-16-00 | HPG 1.40 L1L5                           |  | N/A           | Initial production |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.



<span id="page-2-0"></span>

|   |     | Document information2                 |  |
|---|-----|---------------------------------------|--|
|   |     | Contents 3                            |  |
| 1 |     | Product description 5                 |  |
|   | 1.1 | Overview5                             |  |
|   | 1.2 | Kit contents5                         |  |
|   | 1.3 | Software and documentation5           |  |
|   | 1.4 | System requirements 5                 |  |
| 2 |     | Specifications 6                      |  |
|   | 2.1 | Safety precautions 6                  |  |
|   |     | 2.1.1<br>Certifications6              |  |
| 3 |     | Getting started7                      |  |
|   | 3.1 | Installing u-center software7         |  |
|   | 3.2 | Installing hardware 7                 |  |
|   | 3.3 | Default interface settings8           |  |
| 4 |     | Device description9                   |  |
|   | 4.1 | Interface connection and measurement9 |  |
|   | 4.2 | Active antenna9                       |  |
|   |     | 4.2.1<br>Passive antenna9             |  |
|   | 4.3 | Evaluation unit10                     |  |
|   |     | 4.3.1<br>Antenna connector (RF IN) 10 |  |
|   |     | 4.3.2<br>USB connector10              |  |
|   |     | 4.3.3<br>DB9 connector (RS232)10      |  |
|   |     | 4.3.4<br>RST button10                 |  |
|   |     | 4.3.5<br>Safe boot button11           |  |
|   |     | 4.3.6<br>Slide switch11               |  |
|   |     | 4.3.7<br>Pin header11                 |  |
|   |     | 4.3.8<br>LED12                        |  |
|   |     | 4.3.9<br>BB RAM Functionality12       |  |
| 5 |     | Measuring current 13                  |  |
| 6 |     | RTK setup 14                          |  |
|   | 6.1 | Setting up NTRIP client in u-center14 |  |
|   | 6.2 | Setting up MQTT client in u-center15  |  |
|   | 6.3 | Monitoring RTK status 16              |  |
| 7 |     | Block diagram  18                     |  |
| 8 |     | Board layout 19                       |  |
|   | 8.1 | PCB version B19                       |  |
|   | 8.2 | Dimensions20                          |  |
| 9 |     | Component list  21                    |  |
|   |     | 10 Schematic  23                      |  |
|   |     | 11 Troubleshooting 25                 |  |



| 12 Common evaluation pitfalls  27 |  |
|-----------------------------------|--|
| Related documentation  28         |  |
| Revision history 28               |  |
| Contact 28                        |  |



### <span id="page-4-0"></span>**1 Product description**

### <span id="page-4-1"></span>**1.1 Overview**

The EVK-F9P evaluation kit simplifies the evaluation of the more efficient u-blox F9 high precision positioning products. The built-in USB interface provides both power supply and high-speed data transfer and eliminates the need for an external power supply. The u-blox evaluation kits are compact, and their user-friendly interface and power supply make them ideally suited for use in laboratories, vehicles, and outdoor locations. Furthermore, they can be used with a PC, making them the perfect companion through all stages of design-in process.

| Evaluation Kit | Description                                                    | Suitable for             |
|----------------|----------------------------------------------------------------|--------------------------|
| EVK-F9P-16     | u-blox F9 high accuracy positioning module with<br>L1/L5 bands | NEO-F9P-15B, ZED-F9P-15B |

<span id="page-4-2"></span>**Table 1: List of products supported by EVK-F9P evaluation kit.**

### **1.2 Kit contents**

The delivered package contains:

- Compact EVK-F9P evaluation unit.
- 14-pin front connector breakout cable
- ANN-MB1 multi-band (L1/L5) active GNSS antenna with 5m cable
- Antenna ground plane
- USB-A to USB-C cable
- EVK Welcome card
- <span id="page-4-3"></span>• Promotional PointPerfect Service trial

### **1.3 Software and documentation**

The product evaluation software includes u-center, an interactive tool for configuration, testing, visualization, and data analysis of GNSS receivers. It provides useful assistance during all phases of system integration. Use the latest software version available for F9 products.

<span id="page-4-4"></span>The product evaluation software and documentation are available on the u-blox web site.

### **1.4 System requirements**

- PC with USB interface (compatible with USB 2.0)
- Operating system: Microsoft Windows 10 onwards (x86 and x64 versions)
- Internet connection for the first-time use



## <span id="page-5-0"></span>**2 Specifications**

| Parameter                    | Specification                                                          |
|------------------------------|------------------------------------------------------------------------|
| Serial interfaces            | 1 USB Type-C                                                           |
|                              | 1 RS232, max baud rate 230400 baud                                     |
|                              | DB9 +/- 12 V level                                                     |
|                              | 14 pin – 3.3 V logic                                                   |
|                              | 1 DDC (I2C compatible) max 400 kHz                                     |
|                              | 1 SPI – clock signal max 5,5 MHz – SPI DATA max 1 Mbit/s               |
| Interfaces                   | 1 RTK state output                                                     |
|                              | 1 TXD/MISO, can act as either TXD or MISO depending on usage (I2C/SPI) |
|                              | 1 RXD/MOSI, can act as either RXD or MOSI depending on usage (I2C/SPI) |
|                              | 1 LED, device status indicator                                         |
|                              | 1 time pulse output through 14-pin connector                           |
|                              | 1 external interrupt input                                             |
| Dimensions                   | 105 x 64 x 26 mm                                                       |
| Power supply                 | 5 V via USB or powered via external power supply pin 14.               |
|                              | (V5_IN) and pin 13 (GND)                                               |
| Normal operating temperature | –40 °C to +65 °C                                                       |

**Table 2: EVK-F9P specifications**

### <span id="page-5-1"></span>**2.1 Safety precautions**

EVK-F9P must be supplied by a PS1 class limited power source. See section 6.2.2.4 of IEC 62368- 1:2018 [\[5\]](#page-27-3) for more information on the PS1 class.

In addition to a limited power source, only ES1 class circuits are to be connected to the EVK-F9P, including interfaces and antennas. See section 5.2.1.1 of IEC 62368-1:2018 [\[5\]](#page-27-3) for more information on the ES1 class.

### <span id="page-5-2"></span>**2.1.1 Certifications**

EVK-F9P is designed to comply with the essential requirements and other relevant provisions of Radio Equipment Directive (RED) 2014/53/EU.

EVK-F9P complies with the Directive 2011/65/EU (EU RoHS 2) and its amendment Directive (EU) 2015/863 (EU RoHS 3).

Declaration of Conformity (DoC) is available on the [u-blox website.](https://www.u-blox.com/)



### <span id="page-6-0"></span>**3 Getting started**

### <span id="page-6-1"></span>**3.1 Installing u-center software**

u-center, the u-blox interactive evaluation software tool is required for configuration, testing, visualization, and data analysis of u-blox GNSS receivers as well as EVKs. The provided user guide together with the evaluation tool provide useful assistance during all phases of a system integration project.

- 1. Download the u-center software from [http://www.u-blox.com/product/u-center.](http://www.u-blox.com/product/u-center)
- 2. Once the zipped installer file is downloaded, unzip it and double-click the exe file. The u-center software will be installed on your system and placed under the "u-blox" folder in the "Start > Programs" menu. You can alternatively choose the destination folder for the program installation.
- 3. After a successful installation, start the u-center from the **Start** menu (All Programs > u-blox > u-center > u-center).

For more information on using u-center, refer to the u-center User guide [\[4\]](#page-27-4).

The required Microsoft CDC-ACM driver for Windows 10 USB interface is available from the Microsoft Windows Update service. The Windows system driver search mechanism downloads and install the USB driver automatically from the Microsoft Windows Update service. To evaluate with the Windows 10 operating system, use the u-blox GNSS standard driver (x64bit) available in the u-center package.

### <span id="page-6-2"></span>**3.2 Installing hardware**

- 1. Before connecting the interface cable to the EVK, select the interface that you are using for the connection by sliding the interface switch to the correct position:
  - USB-C: Connect via USB-C connector.
  - UART: Connect via RS-232. Set the slide switch to I2C.
  - SPI / I2C compliant DDC: Connect the corresponding pins (see Table 5 for pin description). Set the slide switch accordingly to SPI or I2C.
- **⚠ CAUTION** Changing the interface switch position while the EVK is powered on may damage the GNSS receiver chip. Power off the EVK before changing the interface switch setting.
  - 2. Power the device on, either via USB on the back or through the V5\_IN input on the front of the EVK.
  - 3. Connect the GNSS antenna to the RF IN SMA jack and place the antenna in a location with good sky view.
  - 4. Start the u-center GNSS Evaluation Software and select the corresponding COM port and baud rate.
- **☞** Refer to the u-center User Guide [\[4\]](#page-27-4) for more information.



<span id="page-7-0"></span>

| Parameter           | Specification                                                                                                                                                                                                                                                                       |  |  |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| UART Port 1, input  | 38400 baud, 8 bits, no parity bit, 1 stop bit.<br>UBX, NMEA and RTCM 3.3 input protocols are enabled by default.<br>SPARTN input protocol is enabled by default.                                                                                                                    |  |  |
| UART Port 1, output | 38400 baud, 8 bits, no parity bit, 1 stop bit.<br>NMEA protocol with GGA, GLL, GSA, GSV, RMC, VTG, TXT messages are output<br>by default.<br>UBX and RTCM 3.3 protocols are enabled by default, but no output messages are<br>enabled by default.                                   |  |  |
| UART2, input        | 38400 baud, 8 bits, no parity bit, 1 stop bit.<br>UBX protocol is enabled by default.<br>RTCM 3.3 protocol is enabled by default.<br>SPARTN protocol is enabled by default.<br>NMEA protocol is disabled by default.                                                                |  |  |
| UART2, output       | 38400 baud, 8 bits, no parity bit, 1 stop bit.<br>UBX protocol is disabled by default.<br>RTCM 3.3 protocol is enabled by default, but no output messages are enabled by<br>default.<br>NMEA protocol is disabled by default.                                                       |  |  |
| USB                 | Default messages activated as in UART1.<br>Input/output protocols available as in UART1.                                                                                                                                                                                            |  |  |
| I2C                 | Compatible with the I2C industry standard, available for communication with an<br>external host CPU or u-blox cellular modules, operated in slave mode only. Default<br>messages activated as in UART1. Input/output protocols available as in UART1.<br>Maximum bit rate 400 kb/s. |  |  |
| SPI                 | Allow communication to a host CPU, operated in slave mode only. Default<br>messages activated as in UART1. Input/output protocols available as in UART1.                                                                                                                            |  |  |

SPI is not available unless D\_SEL pin is set to low.

### **3.3 Default interface settings**

**Table 3: Default configuration**



**☞** Refer to the NEO-F9P Integration manual [\[3\]](#page-27-5) for more information.



### <span id="page-8-0"></span>**4 Device description**

### <span id="page-8-1"></span>**4.1 Interface connection and measurement**

To connect the EVK to a PC, use the USB-C cable included in the kit. Alternatively, use a standard SUB DB-9 cable. Additional measurement equipment can be connected to the front connector.



<span id="page-8-2"></span>**Figure 1: Connecting the unit for power supply and communication.**

### **4.2 Active antenna**

EVK-F9P evaluation kits include an [ANN-MB1](https://www.u-blox.com/en/product/ann-mb1-antenna) multi-band (L1/L5) active GNSS antenna with a 5 meter cable and an SMA connector.

The recommended maximum antenna supply current for active antennas is 15 mA.

### <span id="page-8-3"></span>**4.2.1 Passive antenna**

EVK-F9P-16 can also be used with multi-band (L1/L5) passive GNSS antenna with an additional DC blocker connected.

**⚠ CAUTION** EVK-F9P-16 supplies 3.3V DC to the antenna. If you are using a passive antenna, use a DC blocker to avoid any antenna damage, as shown in [Figure 2.](#page-8-4)



**in the RF path while using passive antenna**

<span id="page-8-4"></span>**Figure 2: Connecting DC blocker** 



### <span id="page-9-0"></span>**4.3 Evaluation unit**

[Figure 3](#page-9-5) shows the front and the rear panels of the EVK-F9P evaluation unit.



<span id="page-9-5"></span>**Figure 3: EVK-F9P evaluation unit front and rear panels**

### <span id="page-9-1"></span>**4.3.1 Antenna connector (RF IN)**

**⚠ CAUTION** Risk of equipment damage. Connecting this equipment to cable distribution systems may damage the EVK. Use the connector only with a GNSS antenna or simulator.

An SMA female jack is available on the front side of the evaluation unit for connecting an active GNSS antenna (see [Figure 3\)](#page-9-5). A DC voltage of 3.3 V is provided to power the active antenna, and the RF input is 3.3 V. The internal short circuit protection limits the maximum current to 60 mA. Note that the 15 mA maximum supply current for the active antenna stays the same. This pin is also ESD protected.

### <span id="page-9-2"></span>**4.3.2 USB connector**

A USB port is featured for data communication and power supply. It is connected to a USB hub and two FTDIs, which enable the user to communicate with the module's UART1 via USB and send correction data through UART2 simultaneously. The user can utilize the USB interface to connect directly to UART1 or UART2. For configuration details, see the Interface description [\[2\]](#page-27-6).

### <span id="page-9-3"></span>**4.3.3 DB9 connector (RS232)**

The evaluation unit includes an RS232 serial communication port which is compatible with PC serial ports. The DB9 connector can be used as an alternative to the UART1 input if the user prefers not to use UART1 from USB.

Connect a straight RS232 serial cable with male and female connectors to the port on your PC. The maximum cable length is 3 meters. To configure the RS232 port, use the CFG-UART1 command in the u-center application. The maximum operating baud rate is 230400 baud. If you are using a USB to RS232 adaptor cable, you can connect it directly to the evaluation kit RS232 port.

| Pin Nr. | Assignment                                             |
|---------|--------------------------------------------------------|
| 1       | Time pulse 1 output (RS232 levels)                     |
| 2       | TXD, GNSS Transmit Data, SPI/MISO                      |
| 3       | RXD, GNSS Receive Data, serial data from DTE, SPI/MOSI |
| 4       | EXTINT (External Interrupt)                            |
| 5       | GND                                                    |
| 6       | Time pulse 1 output (RS232 levels)                     |
| 7       | Not connected                                          |
| 8, 9    | not connected                                          |
|         |                                                        |

The 9-pin D-SUB female connector is assigned as listed in [Table 4](#page-9-6) and diagram fro[m schematic:](#page-27-7)

<span id="page-9-6"></span>**Table 4: SUB-DB9 connector pin description for EVK-F9P** 

#### <span id="page-9-4"></span>**4.3.4 RST button**

The RST button on the front panel resets the unit.



- **⚠ CAUTION** Risk of data loss. The RST button deletes all information from the volatile memory and triggers a cold start. Reset the system only as a recovery option.

### <span id="page-10-0"></span>**4.3.5 Safe boot button**

This is used to set the unit in safe boot mode. In this mode, the receiver executes only minimal functionality, such as updating new firmware into the flash memory. To set the receiver in the safe boot mode:

- 1. Press the BOOT button and keep holding it down.
- 2. Press the RST button.
- 3. Release the RST button.
- 4. Release the BOOT button.
- 5. If the UART interface is used, send a training sequence to the receiver. The training sequence is a transmission of 0x55 0x55 at 9600 baud. Wait for at least 100 milliseconds before the interface is ready to accept commands.

### <span id="page-10-1"></span>**4.3.6 Slide switch**

Use the slide switch on the front panel to choose between I2C (and UART) and SPI communication ports. You must reset the unit by pressing the RST button when the slide switch has been changed.

- **⚠ CAUTION** Risk of data loss. The RESET pin deletes all information from the volatile memory and triggers a cold start. Reset the system only as a recovery option.
  - I2C In this selection the EVK operates with the UART (RS232 DB9 rear panel or the 3.3 V level TxD (MISO), RxD (MOSI) at the front panel). Also, the communication via 3.3 V DDC interface (I2C) is selected.
  - SPI In this selection the EVK operates only with the SPI interface. The RS232 (DB9) port is switched off.

### <span id="page-10-2"></span>**4.3.7 Pin header**

This 14-pin test-connector provides additional functionality to the EVK, allowing access to the interface pins and an ability to measure the current used by the NEO-F9P module. All pins are ESD protected.

| Pin no. | Name        | I/O | Level         | Description                                                                                                                                                                                 |  |
|---------|-------------|-----|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 14      | V5_IN       | I   | 4.75 - 5.25 V | Power input – can be used instead of USB                                                                                                                                                    |  |
| 13      | GND         | -   | -             | Common ground pin                                                                                                                                                                           |  |
| 12      | CUR GPS1    | O   | 5.0 V         | Supply current measurement (Module current consumption) node 1. Current is<br>measured over a 1Ω 1% tolerance resistor between pins 12 and 11. Pin 12<br>(CUR_GPS1) is at higher potential. |  |
| 11      | CUR GPS2    | O   | 5.0 V         | Supply current measurement (Module current consumption) node 2. See<br>description for pin 12.                                                                                              |  |
| 10      | TxD 2       | O   | -             | Correction UART output                                                                                                                                                                      |  |
| 9       | RxD 2       | I   |               | Correction UART input                                                                                                                                                                       |  |
| 8       | TIMEPULSE 1 | O   | 3.3V          | Output signal for the timepulse1 signal                                                                                                                                                     |  |
| 7       | EXTINT      | I   | 3.3 V         | External interrupt or time-mark input (connected directly to the module pins)                                                                                                               |  |
| 6       | RTK status  | O   | 3.3 V         | RTK status:<br>0 = RTK/PPP-RTK fixed<br>blinking = receiving and using corrections<br>1 = no corrections                                                                                    |  |
| 5       | SDA / CS    | I/O | 3.3 V         | If slide switch on I2C, the DDC interface is selected; Function: data input /<br>output.                                                                                                    |  |



|   |            |     |       | If slide switch on SPI, the SPI interface is selected; chip select input – LOW<br>ACTIVE                                                                            |
|---|------------|-----|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4 | SCL / CLK  | I/O | 3.3 V | Clock input / output (signals are pulled up and then straight to the module)                                                                                        |
| 3 | TxD / MISO | O   | 3.3 V | If slide switch on I2C, the DDC interface is selected / UART TxD (3.3 V level)<br>If slide switch on SPI, the SPI interface is selected; Master in Slave out (MISO) |
| 2 | RxD / MOSI | I   | 3.3 V | If slide switch on I2C, the DDC interface is selected / UART RxD (3.3V Level)<br>If slide switch on SPI, the SPI interface is selected; Master out Slave in (MOSI)  |
| 1 | GND        | -   | -     | Common ground pin                                                                                                                                                   |

<span id="page-11-3"></span>**Table 5: Connector pin description for EVK-F9P (pins numbered from right to left on the front panel)**

For accurate measurements, use a max 1 m cable. [Figure 4](#page-11-2) shows an example of a power supply connected to the test connector by using standard adapter cables manufactured by Hirschmann. [Table 5](#page-11-3) shows an example for overall current measurement. When connecting the 3.3 V RS232, SPI and DDC digital interfaces to your application, use a max 25 cm cable.



<span id="page-11-2"></span>**Figure 4: Example 5V DC power supply**

### <span id="page-11-0"></span>**4.3.8 LED**

On the front panel of the EVK unit, there is a single blue LED with the following functionality:

| LED           | Description                                                                           |  |
|---------------|---------------------------------------------------------------------------------------|--|
| Solid blue    | The device is powered on with no GNSS fix.                                            |  |
| Flashing blue | The LED flashes one pulse per second during a GNSS fix.                               |  |
|               | The time pulse signal is configurable, see the Interface description [2] for details. |  |

**Table 6: LED description**

### <span id="page-11-1"></span>**4.3.9 BB RAM Functionality**

A battery is not included in the EVK-F9P kit. To use the Battery Backup RAM functionality, open the unit and insert a Lithium coin battery (CR2032, 3V).



### <span id="page-12-0"></span>**5 Measuring current**

The receiver starts up in the acquisition state to search for available satellites and download GNSS orbital data, i.e. ephemeris and almanac. After downloading the data, the receiver switches to the tracking mode and typically stays in it during continuous operation, reducing the current consumption. The time required to enter the tracking mode can be reduced by downloading aiding data from the AssistNow™ Online service.

To measure the total GNSS supply current with EVK-F9P, follow these steps:

- 1. Place the EVK in clear sky view and perform the test with good signals to ensure that the receiver can acquire the satellite signals.
- 2. Power up EVK-F9P.
- 3. Connect a true RMS voltmeter across CUR GPS1 (pin 12) and CUR GPS2 (pin 11) of the 14-pin connector.
- 4. For accurate measurements, use a max 1 m cable.
- 5. When connecting the 3.3 V RS232, SPI and DDC digital interfaces to your application, use a max 25 cm cable
- 6. Read the voltage (and average if necessary) on the voltmeter and convert to current (1 mV equals 1 mA).
- **☞** The total GNSS current includes the internal LNA, SPI flash and TCXO.

For more details, see the schematic i[n Figure 15.](#page-22-1)





Hirschmann Part No.: 934160100

**Figure 5: Example of tracking current measurement.**





### <span id="page-13-0"></span>**6 RTK setup**

To achieve accurate RTK performance, the receiver needs a constant stream of correction data, which can be obtained from correction data providers via NTRIP or MQTT protocols. Application software is needed to fetch the data from the provider's server and send it to the receiver through serial ports. This chapter explains how to use NTRIP and MQTT client on u-center to monitor the RTK status of the receiver.

### <span id="page-13-1"></span>**6.1 Setting up NTRIP client in u-center**

There are paid and free NTRIP services. [RTK2go](http://rtk2go.com/) is a free community NTRIP service that hobbyists and early prototyping can use, as it provides correction data streams from other users. However, for commercial or production-grade applications, it is recommended to use more reliable commercial NTRIP services.

Start using the u-center NTRIP client with the following steps:

- 1. Open u-center and connect to the receiver via **Receiver > Connection.**
- 2. Open the NTRIP client settings from **Receiver > NTRIP Client.**
- 3. Fill in the NTRIP caster settings fields.
- 4. To fetch the available mount points from the service, click the **Update source table** button.
- 5. Select the correct mount point from the dropdown menu.
- 6. Press **OK** to start the NTRIP client.

| NTRIP client settings      |                                                     |  |
|----------------------------|-----------------------------------------------------|--|
| NTRIP caster settings      |                                                     |  |
| Address:                   |                                                     |  |
| Port:                      |                                                     |  |
| Username:                  |                                                     |  |
| Password:                  |                                                     |  |
| NTRIP stream               |                                                     |  |
|                            | Request Interval (sec)<br>Update source table<br>10 |  |
| NTRIP mount point:         | Mount point details<br>$\blacktriangledown$         |  |
| $\Box$ Use manual position |                                                     |  |
| Longitude (deg):           | $\bf{0}$                                            |  |
| Latitude (deg):            | 0                                                   |  |
| Altitude (m):              | $\overline{0}$                                      |  |
| Geoid sep. (m):            | 0                                                   |  |
|                            | Cancel<br>OK                                        |  |

**Figure 6: u-center NTRIP client**



The status bar at the bottom of the u-center window shows the service status for monitoring and debugging. The connection symbol turns green when authentication is successful, and the service is connected.

| $\blacktriangleleft$ NTRIP client: | <b>40 MOTT client: Not connected</b> | $ u-b $ Generation 9 $ \mathbf{a} - \mathbf{b} $ COM20 460800 No file open |  | <b>UBX</b> | 00:39:40 17:08:07 |
|------------------------------------|--------------------------------------|----------------------------------------------------------------------------|--|------------|-------------------|
|                                    |                                      |                                                                            |  |            |                   |

**Figure 7: u-center status bar**

To see more information about the NTRIP client's operation, click the connection symbol. This will open the NTRIP Log window.

| NTRIP Log<br>×                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 18:24:57 Data received from server (1023bytes).<br>18:24:57 Data received from server (359bytes).<br>18:24:57 Data received from server (203bytes).<br>18:24:58 Data received from server (100bytes).<br>18:24:58 Data received from server (1023bytes).<br>18:24:58 Data received from server (359bytes).<br>18:24:58 Data received from server (186bytes).<br>18:24:59 Data received from server (1023bytes).<br>18:24:59 Data received from server (459bytes).<br>18:24:59 Data received from server (176bytes).<br>18:25:00 Data received from server (100bytes).<br>18:25:00 Data received from server (1023bytes).<br>18:25:00 Data received from server (359bytes).<br>18:25:00 Data received from server (186bytes).<br>18:25:01 Data received from server (100bytes).<br>18:25:01 Data received from server (1023bytes).<br>18:25:01 Data received from server (359bytes).<br>18:25:01 Data received from server (186bytes).<br>18:25:02 Data received from server (100bytes).<br>18:25:02 Data received from server (1023bytes).<br>18:25:0 |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |
| Clear Log<br>Copy log to clipboard<br>ОК                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |

**Figure 8: NTRIP client log**

### <span id="page-14-0"></span>**6.2 Setting up MQTT client in u-center**

An OASIS standard messaging protocol for the Internet of Things (IoT), MQTT provides a reliable, robust, and secure messaging protocol for the IoT devices and applications. It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. (Source: [https://mqtt.org/\)](https://mqtt.org/)

PointPerfect is a GNSS augmentation service that utilizes the industry standard SPARTN messaging format to enable high accuracy with high precision GNSS receivers. The SPARTN format facilitates the transfer of GNSS correction data with exceptional efficiency.

MQTT serves as the fundamental transport mechanism for various components of the service including authentication, ancillary services (such as AssistNow), service key delivery, and the service itself. To support this, u-center incorporates an MQTT client.

Start using the u-center MQTT client with the following steps:

1. Open u-center and connect to the receiver via **Receiver > Connection**.



- 2. Open the MQTT client settings from **Receiver > MQTT Client.**
- 3. In the Thingstream portal, download the u-center config file associated with your device and region of operation and add it as the "JSON config file". For more information on how to sign in to Thingstream to get the u-center configuration file, visit [PointPerfect getting started guide](https://developer.thingstream.io/guides/location-services/pointperfect-getting-started)
- 4. Check the box to "Subscribe to key topic".
- 5. Check the box to "Subscribe to AssistNow topic".
- 6. Check the box to "Subscribe to data topic".
- 7. Select the data topic using the drop-down menu suitable for the region of operation.
- 8. Press **OK** to start the MQTT client.

The status bar at the bottom of the u-center window provides information on the status of the service for monitoring and debugging purposes. When the authentication is successful and the service is connected, the connection symbol turns green.

| Figure 9: Bottom Status bar of u-center |  |  |  |
|-----------------------------------------|--|--|--|

To view more details of the MQTT client's operation, click the connection symbol. The MQTT Log window is displayed.

| MQTT Log                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ×  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| 17:53:00 ERROR: Error sending data to serial port<br>17:53:05 MQTT data message received of size 195 on topic /pp/Lb/eu<br>17:53:10 MQTT data message received of size 203 on topic /pp/Lb/eu<br>17:53:10 SUCCESS: Sent data to serial port.<br>17:53:15 MQTT data message received of size 267 on topic /pp/Lb/eu<br>17:53:15 SUCCESS: Sent data to serial port.<br>17:53:16 MQTT data message received of size 7689 on topic /pp/Lb/eu<br>17:53:18 SUCCESS: Sent data to serial port.<br>17:53:18 MQTT data message received of size 863 on topic /pp/Lb/eu<br>17:53:18 SUCCESS: Sent data to serial port.<br>17:53:20 MQTT data message received of size 195 on topic /pp/Lb/eu<br>17:53:20 SUCCESS: Sent data to serial port.<br>17:53:25 MQTT data message received of size 203 on topic /pp/Lb/eu<br>17:53:25 SUCCESS: Sent data to serial port.<br>17:53:30 MQTT data message received of size 195 on topic /pp/Lb/eu<br>17:53:30 SUCCESS: Sent data to serial port.<br>17:53:35 MQTT data message received of size 195 on topic /pp/Lb/eu<br>17:53:35 SUCCESS: Sent data to serial port.<br>17:53:40 MOTT data message received of size 203 on topic /pp/Lb/eu<br>17:53:40 SUCCESS: Sent data to serial port. |    |
| ∢                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |    |
| Copy log to clipboard<br>Clear Log                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | OK |

<span id="page-15-0"></span>**Figure 10: MQTT client log**

### **6.3 Monitoring RTK status**

Make sure the receiver is getting correction data by monitoring the RTK status in u-center (see Figure 11):

- In the general information view (**View > Docking Windows > Data**), the RTK status is shown in the Fix status field as "Float" or "Fixed" if RTK is used.
- Alternatively, in the UBX-NAV-PVT message view, the RTK status is shown in the Carrier Range Status field as "Float" or "Fixed" if RTK is used.



| 2 COM20 @ 460800 - u-center 22.07 - [UBX-NAV-PVT 0 s]                                                                        |                                                                                                      |                                      |                        |                                    | ×                        |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------|------------------------|------------------------------------|--------------------------|
| <b>D</b> File Edit View Player Receiver Tools Window Help                                                                    |                                                                                                      |                                      |                        |                                    | $   \in$ $\infty$        |
|                                                                                                                              | 0861588888888888888888888888888888888888                                                             |                                      |                        |                                    |                          |
|                                                                                                                              | Ŀ₩∥▼₩▼★∥∥●│△┊ �� �� �� ▓ ▓ ¤ @ �� @ j\{{\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\                            |                                      |                        |                                    |                          |
| PVAT (Navigation PVAT Soluti ^                                                                                               | Param                                                                                                | Value                                | <b>Linits</b>          |                                    |                          |
| PVT (Navigation PVT Solution)                                                                                                | GPS Time Tag                                                                                         | 493328.600                           | [s]                    | Longitude                          | $-0.07483137$            |
| <b>RELPOSNED (Relative Position)</b>                                                                                         | UTC Date and Time                                                                                    | 28/ 4/ 2023 17:01:50 +599872095      |                        | Latitude<br>Altitude               | 52.22273696<br>128.392 m |
| RESETODO (Reset Odometer)                                                                                                    | UTC Date and Time Confirmation Status<br>UTC Time Accuracy                                           | Date: CONFIRMED, Time: CONFIRM<br>21 | [ns]                   | Altitude [msl]                     | 82.638 m                 |
| <b>SAT (Satellite Information)</b>                                                                                           | Position Fix Tupe                                                                                    | 3D Fix                               |                        | TTFF                               | 26.895                   |
| - SBAS (SBAS Status)                                                                                                         | Fix Flags                                                                                            | <b>FixOK DGNSS</b>                   |                        | Fix Mode<br>10.03<br>3D Acc. [m] 0 | 3D/DGNSS/FIXEI           |
| SIG (Signal Information)                                                                                                     | PSM state                                                                                            | n/a                                  |                        | 10.02<br>2D Acc. [m] 0             |                          |
| - SLAS (QZSS SLAS Status)                                                                                                    | Position Latitude, Longitude, Height, MSL                                                            | 52.2227370. - 0.0748313. 128.4. 82.6 | [deg.deg.m.m]          | PDOP                               | $\mathbf{H}$ .0          |
| -SOL (Navigation Solution)                                                                                                   | Invalid Position Latitude, Longitude, Height, MSL<br>Position Accuracy Estimate Horizontal, Vertical | No.<br>0.0, 0.0                      | [m,m]                  | HDOP<br>10.5<br><b>Satellites</b>  |                          |
| - STATUS (Navigation Status)                                                                                                 | Velocity North, East, Down                                                                           | $0.003.0.006. -0.001$                | [m/s,m/s,m/s]          |                                    |                          |
| SVIN (Survey-in)                                                                                                             | Velocity, Heading Accuracy Estimate                                                                  | 0.054, 180.0                         | [m/s,deg]              |                                    |                          |
| SVINFO (SV Information)                                                                                                      | Speed over Ground                                                                                    | 0.006                                | [m/s]                  |                                    |                          |
| TIMEBDS (BDS Time)                                                                                                           | Heading of Motion, Heading of Vehicle<br>Magnetic Declination, Declination Accuracy Estim            | 0.0, n/a<br>n/a, n/a                 | [deg.deg]<br>[deg,deg] |                                    |                          |
|                                                                                                                              | PDOP                                                                                                 | 1.00                                 |                        |                                    |                          |
|                                                                                                                              | #SVs Used                                                                                            | 31                                   |                        |                                    |                          |
|                                                                                                                              |                                                                                                      |                                      |                        |                                    |                          |
|                                                                                                                              |                                                                                                      |                                      |                        |                                    |                          |
|                                                                                                                              |                                                                                                      |                                      |                        |                                    |                          |
| TIMEGAL (Galileo Time)<br>TIMEGLO (GLO Time)<br>TIMEGPS (GPS Time)<br>TIMELS (Leap Second Informal<br>TIMENAVIC (NavIC Time) | Carrier Range Status<br>Age of the most recently received differential corr                          | Fixed<br>$5 \leq$ age $\leq 10$      | [sec]                  |                                    |                          |

**Figure 11: RTK status in u-center**

In open sky scenarios, if the receiver achieves a fixed state in less than two minutes, it indicates that the receiver, antenna, and correction service are compatible and functioning properly.



### <span id="page-17-0"></span>**7 Block diagram**

[Figure 12](#page-17-1) shows the main interfaces and internal connections of the evaluation kit for the NEO-F9P-15B module:



<span id="page-17-1"></span>**Figure 12: EVB-F9P block diagram**



### <span id="page-18-0"></span>**8 Board layout**

### <span id="page-18-1"></span>**8.1 PCB version B**

The PCB for EVK-F9P-16 is showing in [Figure](#page-18-2) 13



<span id="page-18-2"></span>**Figure 13: EVB-F9P-16 PCB**





### <span id="page-19-0"></span>**8.2 Dimensions**

[Figure 14](#page-19-1) shows the EVK-F9P board layout. See [Table 7](#page-21-0) for the component list of the EVB.



#### <span id="page-19-1"></span>**Figure 14: EVB-F9P layout**



### <span id="page-20-0"></span>**9 Component list**

| Regular Components                                                                                         | Description                                                                  |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| A1                                                                                                         | GNSS RECEIVER U-BLOX NEO-F9P-15B -40/+85C                                    |
| C1 C2 C3 C11 C27 C31 C33                                                                                   | CAP CER X5R 0402 1U0 10% 6.3V                                                |
| C4 C5 C6 C10                                                                                               | CAP CER X5R 0402 10U 20% 10V                                                 |
| C7 C8 C16 C23 C24 C25 C26<br>C28 C29 C30 C32 C34 C35<br>C38 C39 C40 C41 C43 C44<br>C45 C46 C47 C48 C49 C50 | CAP CER X5R 0402 100N 10% 50V                                                |
| C9 C21 C22 C42                                                                                             | CAP CER X5R 0603 4U7 10% 6.3V                                                |
| C15                                                                                                        | CAP CER COG 0402 47P 5% 25V                                                  |
| C17 C18 C19 C20                                                                                            | CAP CER COG 0201 47P 2% 50V                                                  |
| C36 C37                                                                                                    | CAP CER COG 0201 18P 5% 50V -55/+125C                                        |
| D1 D2                                                                                                      | SURFACE MOUNT SCHOTTKY BARRIER RECTIFIER SS14 1A -<br>55/+125C               |
| D3 D4 D5 D6 D7 D8 D9 D10<br>D11 D12 D13 D15                                                                | VARISTOR BOURNS MLE SERIES CG0402MLE-18G 18V                                 |
| D14                                                                                                        | ESD PROTECTION FOR HIGH-SPEED LINES, TYCO, 0.25PF,<br>PESD0402-140 -55/+125C |
| D16 D17                                                                                                    | DIODE SCHOTTKY SOD923 30V 0.1A -55/+125C                                     |
| DS1                                                                                                        | LED CHIP 0603 LOW CURRENT BLUE 3V 0.005A                                     |
| J1                                                                                                         | 14PIN 90° 2.54MM PITCH DISCONNECTABLE CRIMP CONNECTOR<br>-40/+85C            |
| J2                                                                                                         | CON SMA SMD STRAIGHT JACK 11.4MM HEIGHT WITHOUT<br>WASHER AND NUT            |
| J3                                                                                                         | 9 POLE SUBD CONNECTOR FEMALE                                                 |
| L1                                                                                                         | IND MURATA LQW15A 0402 120N 5% 0.11A -55/+125C                               |
| Q1                                                                                                         | MBT3906DW1T1G DUAL GENERAL PURPOSE TRANSISTOR 0.2A<br>0.15W -40/+125C        |
| R1                                                                                                         | RES THICK FILM CHIP 0402 CURRENT SENSE 1R 1% 1.1V -<br>55/+125C              |
| R2                                                                                                         | RES THICK FILM CHIP 0402 25PPM 1K8 0.1% 0.063W -55/+155C                     |
| R3                                                                                                         | RES THICK FILM CHIP 0402 51R 1% 0.1W -55/+155C                               |
| R4 R5 R22 R41 R43                                                                                          | RES THICK FILM CHIP 0402 10K 5% 0.1W                                         |
| R6 R7 R18 R19                                                                                              | RES THICK FILM CHIP 0201 0R 0 0.5A                                           |
| R8                                                                                                         | RES THICK FILM CHIP 0402 220R 5% 0.1W                                        |
| R9                                                                                                         | RES THICK FILM CHIP 1206 10R 5% 0.25W                                        |
| R10                                                                                                        | RES THICK FILM CHIP 0402 2K2 5% 0.1W                                         |
| R11                                                                                                        | RES THICK FILM CHIP 0402 100R 5% 0.1W                                        |
| R12 R13                                                                                                    | RES THICK FILM CHIP 0402 56K 5% 0.1W                                         |



| Regular Components                                 | Description                                                            |
|----------------------------------------------------|------------------------------------------------------------------------|
| R14 R15 R16 R17                                    | RES THICK FILM CHIP 0402 27R 5% YAGEO 27R 5% 0.063W -<br>55/+155C      |
| R23                                                | RES THICK FILM CHIP 0201 51K 1% 0.05W                                  |
| R24 R25 R26 R27 R28 R29<br>R30 R31 R32 R33 R34 R39 |                                                                        |
| R40 R42                                            | RES THICK FILM CHIP 0402 100K 1% 0.063W                                |
| R35 R36                                            | RES THICK FILM CHIP 0201 22R 5% 0.05W                                  |
| R37                                                | RES THICK FILM CHIP 0201 12K 1% 0.05W                                  |
| R38                                                | RES THICK FILM CHIP 0201 1M0 5% 0.05W                                  |
| U1 U9                                              | TINY LOGIC UHS BUFFER OE_N ACTIVE LOW FAIRCHILD<br>NC7SZ125 SC70       |
| U2 U3 U4                                           | LOW DROPOUT REGULATOR ON SEMI NCV8705 WDFN6 0.5A<br>3.3V               |
| U5                                                 | BATTERY HOLDER CR2032 3V -40/+105C                                     |
| U6 U7                                              | SWITCH SPST ON 1POL TYCO -40/+85C                                      |
| U8                                                 | 2 WAY SUB-MINIATURE SLIDE SWITCH SMD JS SERIES - SPDT -<br>40/+85C     |
| U10                                                | CON USB 3.1 TYPE C RECEPTACLE 24P                                      |
| U11 U12                                            | USB INTERFACE IC USB TO BASIC SERIAL UART -40/+85C                     |
| U13                                                | USB DATA LINE PROTECTION ST USBLC6-2SC6 SOT23-6                        |
| U14 U15                                            | TINY LOGIC ULP-A 2-INPUT AND GATE 1.45X1.0 6-LEAD<br>MICROPAK -40/+85C |
| U16                                                | TINY LOGIC ULP DUAL 2-INPUT AND GATE FAIRCHILD NC7WP08<br>MICROPAK     |
| U17                                                | TINY LOGIC UHS BUFFER OE ACTIVE HIGH FAIRCHILD NC7SZ126<br>SOT23-5     |
| U18                                                | SMSC USB 2.0 HI-SPEED HUB CONTROLLER -40/+85C                          |
| U19                                                | RS-232 TRANSCEIVER 250KBIT 3-5.5V QFN20 5.5V 0/+70C                    |
| Y1                                                 | CRYSTAL CL=6PF MURATA XRCGB_F_H 24MHZ 10PPM -40/+85C                   |
| Additional Component                               | PCB FOR EVK-F9P VERSION D -40/+85                                      |
| Additional Component                               | SOLDER PASTE OM338 SAC405                                              |

<span id="page-21-0"></span>**Table 7: EVB-F9P component list**



### <span id="page-22-0"></span>**10 Schematic**



<span id="page-22-1"></span>**Figure 15 Schematic EVK-F9P: GNSS, Power Supply RF path and Antenna supply**





**Figure 16: Schematic EVK-F9P: Connectors**



### <span id="page-24-0"></span>**11 Troubleshooting**

#### • **My application (e.g. u-center) does not receive anything.**

- o Check that the EVK is in clear sky view or the antenna cable is connected.
- o Check that the slide switch on the front panel of the EVK is set to the communication port that you are using.
- o Check the LED is on the front panel of the EVK. A solid blue LED indicates the EVK is powered on. If it is not on, connect the power source either via USB on the back or through the V5\_IN input on the front of the EVK.

#### • **My application (e.g. u-center) does not receive all messages.**

When using UART, make sure the baud rate is sufficient. If the baud rate is insufficient, GNSS receivers based on u-blox F9 GNSS technology will skip excessive messages. Some serial port cards/adapters (i.e., USB to RS232 converter) frequently generate errors. If a communication error occurs while u-center receives a message, the message will be discarded.

#### • **My application (e.g. u-center) loses the connection to the GNSS receiver.**

u-blox F9 positioning technology and u-center both have an autobauding feature. If frequent communication errors occur (e.g., due to problems with the serial port), the connection may be lost. This happens because u-center and the GNSS receiver both autonomously try to adjust the baud rate. Do not enable the u-center autobauding if the GNSS receiver has the autobauding flag enabled.

#### **The COM port does not send any messages.**

Make sure that the slide switch on the front panel is set to I2C and not SPI. In the SPI mode, the RS232 pins on the DB9 connector are switched off and the RxD and TxD output at the front panel are used for SPI (MISO, MOSI).

**⚠ CAUTION** Changing the interface switch position while the EVK is powered on may damage the GNSS receiver chip. Power off the EVK before changing the interface switch setting.

#### • **Some COM ports are not shown in the port list of my application (e.g. u-center)**

Only the COM ports that are available on your computer will show up in the COM port drop-down list. If a COM Port is gray, another application running on the computer is using it.

#### • **The position is off by a few dozen meters.**

u-blox F9 GNSS technology starts up with the WGS84 standard GNSS datum. If your application expects a different datum, you will most likely find the positions to be off by a few dozen meters. Do not forget to check the calibration of u-center map files.

#### • **The position is off by hundreds of meters.**

Position drift may also occur when almanac navigation is enabled. The satellite orbit information retrieved from an almanac is much less accurate than the information retrieved from the ephemeris. With an almanac only solution, the position will only have an accuracy of a few kilometers, but it may start up faster or still navigate in areas with obscured visibility when the ephemeris from one or several satellites have not yet been received. The almanac information is NOT used for calculating a position, if valid ephemeris information is present, regardless of the setting of this flag.

In NMEA protocol, position solutions with high deviation (e.g., due to enabling almanac navigation) can be filtered with the Position Accuracy Mask. UBX protocol does not directly support this since it provides a position accuracy estimation, which allows the user to filter the position according to his requirements. However, the 'Position within Limits' flag of the UBX-NAV-STATUS message indicates whether the configured thresholds (i.e., P Accuracy Mask and PDOP) are exceeded.



#### • **TTFF times at start-up are much longer than specified.**

At startup (after the first position fix), the GNSS receiver performs an RTC calibration to have an accurate internal time source. A calibrated RTC is required to achieve minimal startup time.

Before shutting down the receiver externally, check the status in MON-HW in field 'Real Time Clock Status'. Do not shut down the receiver if the RTC is not calibrated.

#### • **The EVK-F9P does not meet the TTFF specification.**

Make sure the antenna has a good sky view. An obstructed view leads to prolonged startup times. In a well-designed system, the average of the C/N0 ratio of high elevation satellites should be in the range of 40 dBHz to about 50 dBHz. With a standard off-the-shelf active antenna, 47 dBHz should easily be achieved. Low C/N0 values lead to a prolonged startup time.

#### • **The EVK-F9P does not preserve the configuration in case of reset.**

u-blox F9 GNSS technology uses a slightly different concept than most other GNSS receivers do. Settings are initially stored in the volatile memory. To save them permanently, sending a second command is required. This allows testing the new settings and reverting to the old settings by resetting the receiver if the new settings are not good. This provides safety, as it is no longer possible to accidentally program a bad configuration (e.g. disabling the main communication port).

For configuration details, see the Interface description [\[2\]](#page-27-6).

#### • **The EVK-F9P does not work properly when connected with a GNSS simulator.**

When using an EVK together with a GNSS simulator, pay attention to proper handling of the EVK. A GNSS receiver is designed for real-life use, (i.e. time is always moving forward). When using a GNSS simulator scenario, the scenario time can be in the past, causing the receiver to jump backwards in time. This affects the receiver performance. The solution is to configure the GPS week rollover to 1200, which corresponds to Jan 2003. Then, issue the cold start command before every simulator test to avoid receiver confusion due to the time jumps.

#### • **Power save mode and USB**

For communication in power save mode, use the RS232.



### <span id="page-26-0"></span>**12 Common evaluation pitfalls**

- A parameter may have the same name but a different definition. GNSS receivers may have a similar size, price, and power consumption, but can still have different functionalities (e.g., no support for passive antennas, different temperature range). Also, the definitions of hot, warm, and cold start times may differ between suppliers.
- Verify design-critical parameters; do not base a decision on unconfirmed numbers from data sheets.
- Try to use identical or at least similar settings when comparing the GNSS performance of different receivers.
- Data that has not been recorded at the same time and the same place should not be compared. The satellite constellation, the number of visible satellites, and the sky view might have been different.
- Do not compare momentary measurements. GNSS is a non-deterministic system. The satellite constellation changes constantly. Atmospheric effects (i.e., dawn and dusk) have an impact on signal travel time. The position of the GNSS receiver is typically not the same between two tests. Comparative tests should therefore be conducted in parallel by using one antenna and a signal splitter; statistical tests shall be run for 24 hours.
- Monitor the carrier-to-noise ratio. The average C/N0 ratio of the high elevation satellites should be between 40 dBHz and about 50 dBHz. A low C/N0 ratio will result in a prolonged TTFF and more position drift.
- When comparing receivers, make sure that all receivers have the same signal levels. The best way to achieve this is by using a signal splitter. Comparing results measured with different antenna types (with different sensitivity) will lead to incorrect conclusions.
- Try to feed the same signal to all receivers in parallel (i.e., through a splitter); the receivers will not have the same sky view otherwise. Even small differences can have an impact on the accuracy. One additional satellite can lead to a lower DOP and less position drift.
- When doing reacquisition tests, cover the antenna to block the sky view. Do not unplug the antenna since the u-blox F9 positioning technology continuously performs a noise calibration on idle channels.



### <span id="page-27-0"></span>**Related documentation**

- [1] NEO-F9P-15B Data sheet, [UBX-22021920](https://content.u-blox.com/sites/default/files/documents/NEO-F9P-15B_DataSheet_UBX-22021920.pdf)
- <span id="page-27-6"></span>[2] u-blox F9 HPG L1L5 1.40 Interface description, [UBX-23006991](https://content.u-blox.com/sites/default/files/documents/u-blox-F9-HPG-L1L5-1.40_InterfaceDescription_UBX-23006991.pdf)
- <span id="page-27-5"></span>[3] NEO-F9P Integration manual, [UBX-22028362](https://content.u-blox.com/sites/default/files/documents/NEO-F9P_IntegrationManual_UBX-22028362.pdf)
- <span id="page-27-4"></span>[4] u-center User guide, [UBX-13005250](https://www.u-blox.com/docs/UBX-13005250)
- <span id="page-27-3"></span>[5] Information technology equipment – [Safety Standard IEC 62368-1:2018](https://webstore.iec.ch/publication/27412)

**☞** For product change notifications and regular updates of u-blox documentation, register on our website, [www.u-blox.com.](http://www.u-blox.com/)

### <span id="page-27-1"></span>**Revision history**

| Revision | Date        | Comments           |
|----------|-------------|--------------------|
| R01      | 09-Aug-2023 | Engineering Sample |
| R02      | 07-Nov-2023 | Initial production |

### <span id="page-27-2"></span>**Contact**

Address: u-blox AG Zürcherstrasse 68 8800 Thalwil Switzerland

<span id="page-27-7"></span>For further support and contact information, visit us a[t www.u-blox.com/support.](http://www.u-blox.com/support)