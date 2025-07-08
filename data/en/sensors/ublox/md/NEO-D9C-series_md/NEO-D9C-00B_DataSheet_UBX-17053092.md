

# **NEO-D9C-00B**

## **QZSS correction service receiver Professional grade**

**Data sheet**



#### **Abstract**

This data sheet describes the NEO-D9C QZSS L6 receiver for CLAS and MADOCA. This NEO form factor module provides easy integration of QZSS augmentation services and enables GNSS receivers to reach cm-level accuracies.

**www.u-blox.com**



UBX-17053092 - R12 C1-Public



## **Document information**

| Title                  | NEO-D9C-00B                      |             |
|------------------------|----------------------------------|-------------|
| Subtitle               | QZSS correction service receiver |             |
| Document type          | Data sheet                       |             |
| Document number        | UBX-17053092                     |             |
| Revision and date      | R12                              | 29-Mar-2023 |
| Disclosure restriction | C1-Public                        |             |

| Product status                   | Corresponding content status |                                                                                           |
|----------------------------------|------------------------------|-------------------------------------------------------------------------------------------|
| Functional Sample                | Draft                        | For functional testing. Revised and supplementary data will be published<br>later.        |
| In development /<br>prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                    |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be<br>published later.   |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be<br>published later. |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                        |

This document applies to the following products:

| Product name | Type number    | FW version | IN/PCN reference                             | Product status  |
|--------------|----------------|------------|----------------------------------------------|-----------------|
| NEO-D9C      | NEO-D9C-00B-02 | QZS 1.01   | UBX-22003112<br>UBX-22039049<br>UBX-23000084 | Mass production |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2023, u-blox AG.



| 1 Functional<br>description                    | 4 |
|------------------------------------------------|---|
| 1.1 Overview 4                                 |   |
| 1.2 Performance 4                              |   |
| 1.3 Supported GNSS augmentation systems 4      |   |
| 1.3.1 Quasi-Zenith Satellite System (QZSS)4    |   |
| 1.4 Supported protocols5                       |   |
| 2 System<br>description6                       |   |
| 2.1 Block diagram 6                            |   |
| 3 Pin<br>definition                            | 7 |
| 3.1 Pin assignment7                            |   |
| 4 Electrical<br>specification9                 |   |
| 4.1 Absolute maximum ratings 9                 |   |
| 4.2 Operating conditions9                      |   |
| 4.3 Indicative power requirements10            |   |
| 5 Communications<br>interfaces11               |   |
| 5.1 UART11                                     |   |
| 5.2 SPI 11                                     |   |
| 5.3 I2C 12                                     |   |
| 5.4 USB 14                                     |   |
| 5.5 Default interface settings14               |   |
| 6 Mechanical specification<br>15               |   |
| 7 Reliability<br>tests17                       |   |
| 8 Labeling<br>and<br>ordering<br>information18 |   |
| 8.1 Product labeling 18                        |   |
| 8.2 Explanation of product codes 18            |   |
| 8.3 Ordering codes 18                          |   |
| Related<br>documents<br>19                     |   |
| Revision<br>history20                          |   |



## <span id="page-3-0"></span>**1 Functional description**

### <span id="page-3-1"></span>**1.1 Overview**

NEO-D9C-00B is a QZSS L6 receiver that brings QZSS Centimeter Level Augmentation Service (CLAS) support to u-blox GNSS modules, enabling centimeter-level navigation. The receiver can also track the experimental MADOCA service transmitted on the QZSS L6 signal.

When combined with other u-blox products, the NEO-D9C-00B can be used to build a complete and stand-alone high precision system providing users with access to free high accuracy correction services and ultimately centimeter-level GNSS accuracy.

### <span id="page-3-2"></span>**1.2 Performance**

| Parameter                                     |          | Specification                                                 |  |  |  |
|-----------------------------------------------|----------|---------------------------------------------------------------|--|--|--|
| Receiver type                                 |          | u-blox D9 engine QZSS L2C and L6 receiver                     |  |  |  |
| QZSS L2C and L6                               |          | Specification                                                 |  |  |  |
| 1<br>Time to first frame                      |          | Hot start 3 s, Cold start 18 s                                |  |  |  |
| 2<br>Decoding sensitivity                     |          | 90% frame rate at -136 dBm                                    |  |  |  |
| 3<br>Acquisition sensitivity                  |          | Hot start: -154 dBm, Cold start: -137 dBm                     |  |  |  |
| Specification compliance                      |          | PS-QZSS-001                                                   |  |  |  |
| Number of concurrent L6 reception<br>channels |          | 2                                                             |  |  |  |
| Frequency range                               |          | 1227.60 MHz +/- 5 MHz and 1278.75 MHz +/- 5 MHz               |  |  |  |
| Communication interface                       |          | UART/USB/I2C/SPI                                              |  |  |  |
| Communication speed                           |          | Up to 921600 baud UART, USB 2.0, SPI 125 kB/s, I2C 400 kbit/s |  |  |  |
|                                               | Dynamics | ≤ 4 g                                                         |  |  |  |
| Vehicle dynamics                              | Velocity | 500 m/s                                                       |  |  |  |

**Table 1: u-blox NEO-D9C-00B performance**

#### <span id="page-3-3"></span>**1.3 Supported GNSS augmentation systems**

#### <span id="page-3-4"></span>**1.3.1 Quasi-Zenith Satellite System (QZSS)**

The Quasi-Zenith Satellite System (QZSS) is a Japanese satellite positioning system. With satellites in quasi-zenith orbits, three satellites will be visible at all times from locations in the Asia-Oceania region. The QZSS correction stream is provided on the L6 band for free.

|       | QZS1     | QZS2/4   | QZS3     | Service     | Frequency   |
|-------|----------|----------|----------|-------------|-------------|
| Orbit | QZO      | QZO      | GEO      |             |             |
|       | Transmit | Transmit | Transmit | PNT         | 1227.60 MHz |
|       | L6D      | L6D/L6E  | L6D/L6E  | CLAS/MADOCA | 1278.75 MHz |
|       |          |          |          |             |             |

**Table 2: QZSS satellites and signals**

<span id="page-3-5"></span><sup>1</sup> With ZED-F9P aiding messages provided, open sky conditions from QZS-1

<span id="page-3-6"></span><sup>2</sup> Power with respect to single component L6D/L6E using a 20-25 dB external LNA

<span id="page-3-7"></span><sup>3</sup> Success rate of acquiring at least one L2 QZSS signal > 95% using constellation of 4 visible QZSS satellites using a 20-25 dB external LNA



QZS1 only transmits the CLAS L6D message, while QZS2, QZS3 and QZS4 transmit both CLAS L6D and MADOCA L6E messages.

#### <span id="page-4-0"></span>**1.4 Supported protocols**

The NEO-D9C-00B supports the following protocols:

| Protocol | Type                                     |
|----------|------------------------------------------|
| UBX      | Input/output, binary, u-blox proprietary |
|          |                                          |

**Table 3: Supported protocols**

For specification of the protocols, see the Interface description [[2](#page-18-1)].



## <span id="page-5-0"></span>**2 System description**

### <span id="page-5-1"></span>**2.1 Block diagram**



**Figure 1: NEO-D9C-00B block diagram**

An active antenna is mandatory with the NEO-D9C-00B.



## <span id="page-6-0"></span>**3 Pin definition**

#### <span id="page-6-1"></span>**3.1 Pin assignment**

The pin assignment of the NEO-D9C-00B module is shown in [Figure](#page-6-2) 2. The defined configuration of the PIOs is listed in [Table](#page-6-3) 4.

V\_BCKP functionality (pin 22: Reserved), ANT\_OFF, ANT\_DETECT, ANT\_SHORT\_N are not available.

<span id="page-6-2"></span>

**Figure 2: NEO-D9C-00B pin assignment**

<span id="page-6-3"></span>

| Pin no. | Name       | I/O | Description                                                      |
|---------|------------|-----|------------------------------------------------------------------|
| 1       | SAFEBOOT_N | I   | SAFEBOOT_N (used for FW updates and reconfiguration, leave open) |
| 2       | D_SEL      | I   | UART 1 / SPI select. (open or high = UART 1)                     |
| 3       | TXD2       | O   | UART 2 TXD                                                       |
| 4       | RXD2       | I   | UART 2 RXD                                                       |
| 5       | USB_DM     | I/O | USB data (DM)                                                    |
| 6       | USB_DP     | I/O | USB data (DP)                                                    |
| 7       | V_USB      | I   | USB supply                                                       |
| 8       | RESET_N    | I   | RESET (active low)                                               |
| 9       | VCC_RF     | O   | External LNA power                                               |
| 10      | GND        | I   | Ground                                                           |
| 11      | RF_IN      | I   | Active antenna L2/L6 band signal input                           |
| 12      | GND        | I   | Ground                                                           |



| Pin no. | Name           | I/O | Description                                                       |
|---------|----------------|-----|-------------------------------------------------------------------|
| 13      | GND            | I   | Ground                                                            |
| 14      | ANT_OFF        | O   | External LNA disable - default active high                        |
| 15      | ANT_DETECT     | I   | Active antenna detect - default active high                       |
| 16      | ANT_SHORT_N    | O   | Active antenna short detect - default active low                  |
| 17      | EXTINT         | I   | External interrupt pin                                            |
| 18      | SDA / SPI CS_N | I/O | I2C data if D_SEL = VCC (or open); SPI chip select if D_SEL = GND |
| 19      | SCL / SPI SLK  | I/O | I2C clock if D_SEL = VCC (or open); SPI clock if D_SEL = GND      |
| 20      | TXD / SPI MISO | O   | UART1 output if D_SEL = VCC (or open); SPI MISO if D_SEL = GND    |
| 21      | RXD / SPI MOSI | I   | UART1 input if D_SEL = VCC (or open); SPI MOSI if D_SEL = GND     |
| 22      | Reserved       | -   | No connection                                                     |
| 23      | VCC            | I   | Supply voltage                                                    |
| 24      | GND            | I   | Ground                                                            |

**Table 4: NEO-D9C-00B pin assignment**

For detailed information on the pin functions and characteristics see the integration manual[\[1\]](#page-18-2).



## <span id="page-8-0"></span>**4 Electrical specification**

The limiting values given are in accordance with the Absolute Maximum Rating System (IEC 134).

**CAUTION** Operating the device above one or more of the limiting values may cause permanent damage to the device. The values provided in this chapter are stress ratings. Extended exposure to the values outside the limits may effect the device reliability.

Where application information is given, it is advisory only and does not form part of the specification.

#### <span id="page-8-1"></span>**4.1 Absolute maximum ratings**

| Parameter                | Symbol            | Condition                                   | Min  | Max           | Units |
|--------------------------|-------------------|---------------------------------------------|------|---------------|-------|
| Power supply voltage     | VCC               |                                             | -0.5 | 3.6           | V     |
| 4<br>Voltage ramp on VCC |                   |                                             | 20   | 8000          | µs/V  |
| Input pin voltage        | Vin               |                                             | -0.5 | VCC + 0.5     | V     |
| VCC_RF output current    | ICC_RF            |                                             |      | 200           | mA    |
| Supply voltage USB       | V_USB             |                                             | –0.5 | 3.6           | V     |
| USB signals              | USB_DM,<br>USB_DP |                                             | -0.5 | V_USB + 0.5 V |       |
| Input power at RF_IN     | Prfin             | source impedance =<br>50 Ω, continuous wave |      | 10            | dBm   |
| Storage temperature      | Tstg              |                                             | -40  | +85           | °C    |

**Table 5: Absolute maximum ratings**

**CAUTION** Risk of equipment damage. This product is not protected against overvoltage or reversed voltages. Use appropriate protection diodes to avoid voltage spikes exceeding the specified boundaries damaging the equipment.

#### <span id="page-8-2"></span>**4.2 Operating conditions**

The values for the following operating conditions have been specified at 25°C ambient temperature. Extreme operating temperatures can significantly impact the specified values. If an application operates near the min or max temperature limits, ensure the specified values are not exceeded.

| Parameter                                                   | Symbol   | Min       | Typical   | Max | Units | Condition  |
|-------------------------------------------------------------|----------|-----------|-----------|-----|-------|------------|
| Power supply voltage                                        | VCC      | 2.7       | 3.0       | 3.6 | V     |            |
| SW backup current                                           | I_SWBCKP |           | 0.07      |     | mA    |            |
| Input pin voltage range                                     | Vin      | 0         |           | VCC | V     |            |
| Digital IO pin low level input voltage                      | Vil      |           |           | 0.4 | V     |            |
| Digital IO pin high level input voltage                     | Vih      | 0.8 * VCC |           |     | V     |            |
| Digital IO pin low level output voltage                     | Vol      |           |           | 0.4 | V     | Iol = 2 mA |
| Digital IO pin high level output voltage Voh                |          | VCC – 0.4 |           |     | V     | Ioh = 2 mA |
| DC current through any digital I/O pin<br>(except supplies) | Ipin     |           |           | 5   | mA    |            |
| VCC_RF voltage                                              | VCC_RF   |           | VCC - 0.1 |     | V     |            |
| VCC_RF output current                                       | ICC_RF   |           |           | 50  | mA    |            |

<span id="page-8-3"></span>4 Exceeding the ramp speed may permanently damage the device



| Parameter                                 | Symbol | Min | Typical | Max | Units | Condition |
|-------------------------------------------|--------|-----|---------|-----|-------|-----------|
| 5<br>Receiver chain noise figure          | NFtot  |     | 11      |     | dB    |           |
| Recommended LNA gain into module LNA_gain |        |     | 20      |     | dB    |           |
| Operating temperature                     | Topr   | -40 | +25     | +85 | °C    |           |

**Table 6: Operating conditions**

Operation beyond the specified operating conditions can affect the device reliability.

#### <span id="page-9-0"></span>**4.3 Indicative power requirements**

[Table](#page-9-2) 7 provides examples of typical current requirements when using a cold start command. The given values are total system supply current for a possible application including RF and baseband sections.

The actual power requirements vary depending on the FW version used, external circuitry, number of satellites tracked, signal strength, type and time of start, duration, and conditions of test.

<span id="page-9-2"></span>

| Symbol   | Parameter       | Conditions             | QZSS L6 | Unit |
|----------|-----------------|------------------------|---------|------|
| IPEAK    | Peak current    | Acquisition & tracking | 130     | mA   |
| IAVERAGE | Average current | Acquisition & tracking | 55      | mA   |

**Table 7: Currents to calculate the indicative power requirements**

All values in [Table](#page-9-2) 7 are measured at 25 °C ambient temperature.

<span id="page-9-1"></span><sup>5</sup> Only valid for the QZSS L2 band



## <span id="page-10-0"></span>**5 Communications interfaces**

The NEO-D9C-00B has several communications interfaces, including UART, SPI, I2C and USB.

All the inputs have internal pull-up resistors in normal operation and can be left open if not used. All the PIOs are supplied by VCC, therefore all the voltage levels of the PIO pins are related to VCC supply voltage.

### <span id="page-10-1"></span>**5.1 UART**

The UART interfaces support configurable baud rates. See the Integration manual [\[1\]](#page-18-2).

Hardware flow control is not supported.

UART1 is the primary host communications interface.

| Symbol | Parameter              | Min   | Max    | Unit  |
|--------|------------------------|-------|--------|-------|
| Ru     | Baud rate              | 9600  | 921600 | bit/s |
| ΔTx    | Tx baud rate accuracy  | -1%   | +1%    | -     |
| ΔRx    | Rx baud rate tolerance | -2.5% | +2.5%  | -     |

**Table 8: NEO-D9C-00B UART specifications**

#### <span id="page-10-2"></span>**5.2 SPI**

The SPI interface is disabled by default. The SPI interface shares pins with UART and I2C and can be selected by setting D\_SEL = 0. The SPI interface can be operated in slave mode only. The maximum transfer rate using SPI is 125 kB/s and the maximum SPI clock frequency is 5.5 MHz.

The SPI timing parameters for slave operation are defined in [Figure](#page-10-3) 3. Default SPI configuration is CPOL = 0 and CPHA = 0.

<span id="page-10-3"></span>

| Symbol | Parameter                     | Min | Max | Unit |
|--------|-------------------------------|-----|-----|------|
| 1      | CS deassertion hold time      | 23  | -   | ns   |
| 2      | Slave select time (CS to SCK) | 20  | -   | ns   |



| Symbol | Parameter                               | Min | Max | Unit |
|--------|-----------------------------------------|-----|-----|------|
| 3      | SCK rise/fall time                      | -   | 7   | ns   |
| 4      | SCK high time                           | 24  | -   | ns   |
| 5      | SCK low time                            | 24  | -   | ns   |
| 6      | Slave deselect time (SCK falling to CS) | 30  | -   | ns   |
| 7      | Slave deselect time (CS to SCK)         | 30  | -   | ns   |
| 9      | CS high time                            | 32  | -   | ns   |
| 10     | MOSI transition time                    | -   | 7   | ns   |
| 11     | MOSI setup time                         | 16  | -   | ns   |
| 12     | MOSI hold time                          | 24  | -   | ns   |
|        |                                         |     |     |      |

**Table 9: SPI slave input timing parameters 1 - 12**

| Symbol | Parameter                                    | Min | Max | Unit |
|--------|----------------------------------------------|-----|-----|------|
| A      | MISO data valid time (CS)                    | 12  | 40  | ns   |
| B      | MISO data valid time (SCK), weak driver mode | 15  | 40  | ns   |
| C      | MISO data hold time                          | 100 | 140 | ns   |
| D      | MISO rise/fall time, weak driver mode        | 0   | 5   | ns   |
| E      | MISO data disable lag time                   | 15  | 35  | ns   |

**Table 10: SPI slave timing parameters A - E, 2 pF load capacitance**

| Symbol | Parameter                                    | Min | Max | Unit |
|--------|----------------------------------------------|-----|-----|------|
| A      | MISO data valid time (CS)                    | 16  | 55  | ns   |
| B      | MISO data valid time (SCK), weak driver mode | 20  | 55  | ns   |
| C      | MISO data hold time                          | 100 | 150 | ns   |
| D      | MISO rise/fall time, weak driver mode        | 3   | 20  | ns   |
| E      | MISO data disable lag time                   | 15  | 35  | ns   |

**Table 11: SPI slave timing parameters A - E, 20 pF load capacitance**

| Symbol | Parameter                                    | Min | Max | Unit |
|--------|----------------------------------------------|-----|-----|------|
| A      | MISO data valid time (CS)                    | 26  | 85  | ns   |
| B      | MISO data valid time (SCK), weak driver mode | 30  | 85  | ns   |
| C      | MISO data hold time                          | 110 | 160 | ns   |
| D      | MISO rise/fall time, weak driver mode        | 13  | 45  | ns   |
| E      | MISO data disable lag time                   | 15  | 35  | ns   |

**Table 12: SPI slave timing parameters A - E, 60 pF load capacitance**

### <span id="page-11-0"></span>**5.3 I2C**

An I2C interface is available for communication with an external host CPU in I2C Fast-mode. Backwards compatibility with Standard-mode I2C bus operation is not supported. The interface can be operated only in slave mode with a maximum bit rate of 400 kbit/s. The interface can make use of clock stretching by holding the SCL line LOW to pause a transaction. In this case, the bit transfer rate is reduced. The maximum clock stretching time is 20 ms.





|  |  | Figure 4: NEO-D9C-00B I2C slave specification |
|--|--|-----------------------------------------------|
|  |  |                                               |

|         |                                                     | I2C Fast-mode |                     |      |
|---------|-----------------------------------------------------|---------------|---------------------|------|
| Symbol  | Parameter                                           | Min           | Max                 | Unit |
| fSCL    | SCL clock frequency                                 | 0             | 400                 | kHz  |
| tHD;STA | Hold time (repeated) START condition                | 0.6           | -                   | µs   |
| tLOW    | Low period of the SCL clock                         | 1.3           | -                   | µs   |
| tHIGH   | High period of the SCL clock                        | 0.6           | -                   | µs   |
| tSU;STA | Setup time for a repeated START condition           | 0.6           | -                   | µs   |
| tHD;DAT | Data hold time                                      | 0 6           | 7<br>-              | µs   |
| tSU;DAT | Data setup time                                     | 100 8         |                     | ns   |
| tr      | Rise time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| tf      | Fall time of both SDA and SCL signals               | -             | 300 (for C = 400pF) | ns   |
| tSU;STO | Setup time for STOP condition                       | 0.6           | -                   | µs   |
| tBUF    | Bus-free time between a STOP and START<br>condition | 1.3           | -                   | µs   |
| tVD;DAT | Data valid time                                     | -             | 0.9 7               | µs   |
| tVD;ACK | Data valid acknowledge time                         | -             | 0.9 7               | µs   |
| VnL     | Noise margin at the low level                       | 0.1 V_IO      | -                   | V    |
| VnH     | Noise margin at the high level                      | 0.2 V_IO      | -                   | V    |
|         |                                                     |               |                     |      |

**Table 13: NEO-D9C-00B I2C slave timings and specifications**

<span id="page-12-0"></span><sup>6</sup> External device must provide a hold time of at least one transition time (max 300 ns) for the SDA signal (with respect to the min Vih of the SCL signal) to bridge the undefined region of the falling edge of SCL.

<span id="page-12-1"></span><sup>7</sup> The maximum tHD;DAT must be less than the maximum tVD;DAT or tVD;ACK with a maximum of 0.9 µs by a transition time. This maximum must only be met if the device does not stretch the LOW period (tLOW) of the SCL signal. If the clock stretches the SCL, the data must be valid by the set-up time before it releases the clock.

<span id="page-12-2"></span><sup>8</sup> When the I2C slave is stretching the clock, the tSU;DAT of the first bit of the next byte is 62.5 ns.



The I2C interface is only available with the UART default mode. If the SPI interface is selected by using D\_SEL = 0, the I2C interface is not available.

### <span id="page-13-0"></span>**5.4 USB**

The USB 2.0 FS (full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface. The V\_USB pin supplies the USB interface.

#### <span id="page-13-1"></span>**5.5 Default interface settings**

| Settings                                                                                                                    |  |
|-----------------------------------------------------------------------------------------------------------------------------|--|
| 9600 baud, 8 bits, no parity bit, 1 stop bit.                                                                               |  |
| Output protocol: UBX. Only the following UBX message (if enabled) will be output if there is valid<br>data: UBX-RXM-QZSSL6. |  |
| Input protocols without need of additional configuration: UBX.                                                              |  |
| Output messages activated as in UART. Input protocols available as in UART.                                                 |  |
| Output messages activated as in UART. Input protocols available as in UART.                                                 |  |
| Output messages activated as in UART. Input protocols available as in UART.                                                 |  |
|                                                                                                                             |  |

**Table 14: Default interface settings**

The boot message is still output using \$GNTXT messages. The messages are output when the NEO-D9C-00B is powered up.

Refer to the applicable interface description [[2](#page-18-1)] for information about further settings.



## <span id="page-14-0"></span>**6 Mechanical specification**





#### **Figure 5: NEO-D9C-00B mechanical drawing**

| Symbol | Min (mm) | Typical (mm) | Max (mm) |                                                                    |
|--------|----------|--------------|----------|--------------------------------------------------------------------|
| A      | 15.9     | 16.0         | 16.1     |                                                                    |
| B      | 12.1     | 12.2         | 12.3     |                                                                    |
| C      | 2.2      | 2.4          | 2.6      |                                                                    |
| D      | 0.9      | 1.0          | 1.1      |                                                                    |
| E      | 1.0      | 1.1          | 1.2      |                                                                    |
| F      | 2.9      | 3.0          | 3.1      |                                                                    |
| G      | 0.9      | 1.0          | 1.1      |                                                                    |
| H      | -        | 0.82         | -        |                                                                    |
| K      | 0.7      | 0.8          | 0.9      |                                                                    |
| M      | 0.8      | 0.9          | 1.0      |                                                                    |
| N      | 0.4      | 0.5          | 0.6      |                                                                    |
| P*     | 0.0      | -            | 0.5      | The de-paneling residual tabs may be on either<br>side (not both). |
| Weight |          | 1.6 g        |          |                                                                    |

**Table 15: NEO-D9C-00B mechanical dimensions**



- The mechanical picture of the de-paneling residual tabs (P\*) is an approximate representation, shape and position may vary.
- Component keep-out area must consider that the de-paneling residual tabs can be on either side (not both).



## <span id="page-16-0"></span>**7 Reliability tests**

NEO-D9C-00B modules are based on AEC-Q100 qualified GNSS chips.

Tests for product family qualifications are according to ISO 16750 "Road vehicles – environmental conditions and testing for electrical and electronic equipment" , and appropriate standards.



## <span id="page-17-0"></span>**8 Labeling and ordering information**

This section provides information about product labeling and ordering. For information about moisture sensitivity level (MSL), product handling and soldering see the Integration manual [[1\]](#page-18-2).

#### <span id="page-17-1"></span>**8.1 Product labeling**

The labeling of the NEO-D9C-00B modules provides product information and revision information. For more information contact u-blox sales.

### <span id="page-17-2"></span>**8.2 Explanation of product codes**

Three product code formats are used in the NEO-D9C-00B labels. The **Product name** used in documentation such as this data sheet identifies all u-blox products, independent of packaging and quality grade. The **Ordering code** includes options and quality, while the **Type number** includes the hardware and firmware versions.

<span id="page-17-4"></span>

| Format        | Structure      | Product code   |  |
|---------------|----------------|----------------|--|
| Product name  | PPP-TGV        | NEO-D9C        |  |
| Ordering code | PPP-TGV-NNQ    | NEO-D9C-00B    |  |
| Type number   | PPP-TGV-NNQ-XX | NEO-D9C-00B-02 |  |

[Table](#page-17-4) 16 below details these three formats.

**Table 16: Product code formats**

The parts of the product code are explained in [Table](#page-17-5) 17.

<span id="page-17-5"></span>

| Code | Meaning                | Example                                    |
|------|------------------------|--------------------------------------------|
| PPP  | Product family         | NEO                                        |
| TG   | Platform               | D9 = u-blox D9                             |
| V    | Variant                | C = QZSS corrections                       |
| NNQ  | Option / Quality grade | NN: Option [0099]                          |
|      |                        | Q: Grade, A = Automotive, B = Professional |
| XX   | Product detail         | Describes hardware and firmware versions   |

**Table 17: Part identification code**

#### <span id="page-17-3"></span>**8.3 Ordering codes**

| Ordering code | Product | Remark                                                                      |
|---------------|---------|-----------------------------------------------------------------------------|
| NEO-D9C-00B   | NEO-D9C | u-blox D9 correction module QZSS L6<br>receiver for CLAS and MADOCA service |

**Table 18: Product ordering codes**

Product changes affecting form, fit or function are documented by u-blox. For a list of Product Change Notifications (PCNs) see our website at: <https://www.u-blox.com/en/product-resources>.



## <span id="page-18-0"></span>**Related documents**

- <span id="page-18-2"></span>**[1]** NEO-D9C Integration manual, [UBX-21031631](https://www.u-blox.com/docs/UBX-21031631)
- <span id="page-18-1"></span>**[2]** QZS 1.01 Interface description, [UBX-21031777](https://www.u-blox.com/docs/UBX-21031777)

For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



## <span id="page-19-0"></span>**Revision history**

| Revision | Date         | Name      | Status / comments                                                                                                           |
|----------|--------------|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| R01      | 15-Sep-2017  | ghun/jhak | Draft                                                                                                                       |
| R02      | 29-Sep-2017  | ghun/jhak | Draft / updated pins 15 and 16                                                                                              |
| R03      | 29-Apr-2019  | ghun      | Objective Specification                                                                                                     |
| R04      | 23-May-2019  | ghun      | Advance Information                                                                                                         |
| R05      | 27-June-2019 | ghun      | Early Production Information - V_BCKP not used                                                                              |
| R06      | 25-Mar-2020  | jhak/ghun | PCN UBX-19057484 added and module type number updated. Absolute<br>maximum ratings and Operating conditions tables updated. |
| R07      | 27-Oct-2020  | dama      | USB interface section update. UART interface section update. SW backup<br>current update                                    |
| R08      | 15-Sep-2021  | dbhu      | Update average current value. firmware QZS 1.01 update.                                                                     |
| R09      | 17-Dec-2021  | dama      | Overall text improvement and typo corrections.                                                                              |
|          |              |           | Disclosure restriction C1-Public                                                                                            |
| R10      | 09-Feb-2022  | dama      | Production information                                                                                                      |
| R11      | 16-Dec-2022  | dbhu      | Overall text improvement                                                                                                    |
|          |              |           | Updated the section Mechanical specification                                                                                |
| R12      | 29-Mar-2023  | dbhu      | Updated I2C and SPI timing specifications in section Communications<br>interfaces                                           |
|          |              |           | Updated VCC_RF output current in table Absolute maximum ratings                                                             |



## **Contact**

#### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).