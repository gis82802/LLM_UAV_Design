

# **NEO-M8P**

## **u-blox M8 high precision GNSS modules**

**Hardware integration manual**



### **Abstract**

This document provides design-in and feature information for the high-accuracy NEO-M8P modules. Base and rover module variants together provide a high precision centimeter-level real time kinematics (RTK) position solution. Each module contains the u-blox M8 concurrent GNSS engine for concurrent reception of GPS, GLONASS and BeiDou signals.



**[www.u-blox.com](http://www.u-blox.com/)** UBX-15028081 - R09 C1-Public



## <span id="page-1-0"></span>**Document information**

| Title                  | NEO-M8P                               |             |  |
|------------------------|---------------------------------------|-------------|--|
| Subtitle               | u-blox M8 high precision GNSS modules |             |  |
| Document type          | Hardware integration manual           |             |  |
| Document number        | UBX-15028081                          |             |  |
| Revision and date      | R09                                   | 19-Aug-2021 |  |
| Disclosure restriction | C1-Public                             |             |  |

#### **European Union regulatory compliance**

NEO-M8P complies with all relevant requirements for RED 2014/53/EU. The NEO-M8P Declaration of Conformity (DoC) is available at www.u-blox.com within Support > Product resources > Conformity Declaration.

| Product status                   | Corresponding content status |                                                                                        |  |  |  |
|----------------------------------|------------------------------|----------------------------------------------------------------------------------------|--|--|--|
| In development /<br>Prototype    | Objective specification      | Target values. Revised and supplementary data will be published later.                 |  |  |  |
| Engineering sample               | Advance information          | Data based on early testing. Revised and supplementary data will be published later.   |  |  |  |
| Initial production               | Early production information | Data from product verification. Revised and supplementary data may be published later. |  |  |  |
| Mass production /<br>End of life | Production information       | Document contains the final product specification.                                     |  |  |  |

#### This document applies to the following products:

| Product name | Type number  | ROM/FLASH version    | PCN reference    |
|--------------|--------------|----------------------|------------------|
| NEO-M8P      | NEO-M8P-0-11 | FLASH FW3.01 HPG1.40 | PCN UBX-20013367 |
| NEO-M8P      | NEO-M8P-2-11 | FLASH FW3.01 HPG1.40 | PCN UBX-20013367 |
| NEO-M8P      | NEO-M8P-0-12 | FLASH FW3.05 HPG1.43 | PCN UBX-21035324 |
| NEO-M8P      | NEO-M8P-2-12 | FLASH FW3.05 HPG1.43 | PCN UBX-21035324 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, modification or disclosure to third parties of this document or any part thereof is only permitted with the express written permission of u-blox.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © u-blox AG.



<span id="page-2-0"></span>

|     | Document information2                                                |  |
|-----|----------------------------------------------------------------------|--|
|     | Contents 3                                                           |  |
| 1   | Hardware description4                                                |  |
| 1.1 | Overview4                                                            |  |
| 1.2 | Configuration 4                                                      |  |
| 1.3 | Connecting power 4                                                   |  |
| 1.4 | Communication interfaces 5                                           |  |
| 1.5 | I/O pins7                                                            |  |
| 2   | Design9                                                              |  |
| 2.1 | Pin description9                                                     |  |
| 2.2 | Minimal design10                                                     |  |
| 2.3 | Layout: Footprint and paste mask10                                   |  |
| 2.4 | Antenna11                                                            |  |
| 2.5 | Layout design-in: Thermal management14                               |  |
| 3   | Product handling 15                                                  |  |
| 3.1 | Packaging, shipping, storage, and moisture preconditioning 15        |  |
| 3.2 | Soldering15                                                          |  |
| 3.3 | EOS/ESD/EMI precautions18                                            |  |
| 3.4 | Applications with cellular modules21                                 |  |
|     | Appendix  23                                                         |  |
| A   | Recommended parts  23                                                |  |
| B   | Recommended antennas  24                                             |  |
| C   | Design-in recommendations in combination with cellular operation  25 |  |
|     | Related documents  26                                                |  |
|     | Revision history 26                                                  |  |
|     | Contact 27                                                           |  |



## <span id="page-3-0"></span>**1 Hardware description**

### <span id="page-3-1"></span>**1.1 Overview**

The NEO-M8P modules combine the high-performance u-blox M8 positioning engine with u-blox's real time kinematic (RTK) technology. NEO-M8P provides centimeter-level GNSS performance designed to meet the needs of unmanned vehicles and other machine control applications requiring accurate guidance.

u-blox's RTK technology introduces the concept of a "rover" (NEO-M8P-0) and a "base" (NEO-M8P-2) on the M8 platform. The base module sends corrections via the RTCM protocol to the rover module via a communication link enabling the rover to output its position relative to the base at centimeterlevel accuracies.

Available in the industry standard form factor in leadless chip carrier (LCC) packages, the modules are easy to integrate, and they combine exceptional positioning performance with highly flexible power, design, and connectivity options. SMT pads allow fully automated assembly with standard pick and place and reflow-soldering equipment for a cost-efficient, high-volume production for short timeto-market.

**☞** For all product features, see NEO-M8P Data sheet [\[1\].](#page-25-2)

### <span id="page-3-2"></span>**1.2 Configuration**

The configuration settings can be modified using UBX protocol configuration messages, see u-blox 8 / u-blox M8 Receiver Description including Protocol Specification [\[2\].](#page-25-3) The modified settings remain effective until power-down or reset. If these settings have been stored in the BBR (battery-backed RAM), the modified configuration will be retained, as long as the backup battery supply is not interrupted.

For the NEO-M8P module, the configuration can be saved permanently in SQI flash.

### <span id="page-3-3"></span>**1.3 Connecting power**

The NEO-M8P high precision GNSS modules have up to three power supply pins: **VCC**, **V\_BCK and VDD\_USB**.

### **1.3.1 VCC: Main supply voltage**

The **VCC** pin provides the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude. For this reason, it is important that the supply circuitry be able to support the peak power for a short time (see NEO-M8P Data sheet [\[1\]](#page-25-2) for specification).

**☞** When switching from backup mode to normal operation or at startup, u-blox M8 modules must charge the internal capacitors in the core domain. In certain situations, this can result in a significant current draw. For low-power applications using power save and/or backup modes, it is important that the power supply or low ESR capacitors at the module input can deliver this current/charge.

**☞** Use a proper GND concept. Do not use any resistors or inductors in the power line.

### **1.3.2 V\_BCKP: Backup supply voltage**

If the module supply has a power failure, the **V\_BCKP** pin supplies the real-time clock (RTC) and battery backed RAM (BBR). Use of valid time and the GNSS orbit data at startup improves the GNSS



performance of hot or warm starts. If no backup battery is connected, the module performs a cold start at power up.

**☞** Avoid high resistance on the **V\_BCKP** line: During the switch from main supply to backup supply, a short current adjustment peak can cause high voltage drop on the pin with possible malfunctions.



<span id="page-4-1"></span>**Figure 1: Backup battery and voltage (for exact pin orientation, see NEO-M8P Data sheet [1])**

- **☞** If no backup supply voltage is available, connect the **V\_BCKP** pin to **VCC**.
- **☞** While power is supplied to the NEO-M8P module through the **VCC** pin, the backup battery is disconnected from the RTC and the BBR to avoid unnecessary battery drain (see [Figure 1\)](#page-4-1). In this case, **VCC** supplies power to the RTC and BBR.

### **1.3.3 VDD\_USB**: **USB interface power supply**

**VDD\_USB** supplies the USB interface. If the USB interface is not used, the **VDD\_USB** pin must be connected to GND. For more information about correctly handling the **VDD\_USB** pin, see sectio[n 1.4.](#page-4-0)

### **1.3.4 VCC\_RF: Output voltage RF**

The **VCC\_RF** pin can supply an active antenna or an external LNA. For more information, see section [2.4.](#page-10-0)

### <span id="page-4-0"></span>**1.4 Communication interfaces**

The following interfaces are used for command and control using the UBX proprietary binary protocol and for reception and transmission of a RTCM message stream when operating in RTK mode.

### **1.4.1 UART**

NEO-M8P positioning modules include a Universal Asynchronous Receiver Transmitter (UART) serial interface **RXD/TXD** supporting configurable baud rates. The baud rates supported are specified in ublox 8 / u-blox M8 Receiver Description including Protocol Specification [\[2\].](#page-25-3)

The signal output and input levels are 0 V to **VCC**. An interface based on RS232 standard levels (+/- 12 V) can be implemented using level shifters such as a Maxim MAX3232. Hardware handshake signals and synchronous operation are not supported.

### **1.4.2 USB**

A USB version 2.0 FS (Full Speed, 12 Mb/s) compatible interface is available for communication as an alternative to the UART. The **USB\_DP** integrates a pull-up resistor to signal a full-speed device to the host. The **VDD\_USB** pin supplies the USB interface.



u-blox provides Microsoft® certified USB drivers for Windows operating systems (Vista, Windows 7, 8 and 10). These drivers are available for download from our website: [www.u-blox.com.](http://www.u-blox.com/)

### **1.4.2.1 USB external components**

The USB interface requires some external components to implement the physical characteristics required by the USB 2.0 specification. These external components are shown in [Figure 2](#page-5-0) and listed in [Table 1.](#page-5-1)

To comply with USB specifications, VBUS must be connected through an LDO (U1) to pin **VDD\_USB** on the module.

In USB **self-powered** mode, the power supply (**VCC**) can be turned off and the digital block is not powered. In this case, since VBUS is still available, the USB host still receives a signal indicating that the device is present and ready to communicate. This should be avoided by disabling the LDO (U1) using the enable signal (EN) of the VCC-LDO or the output of a voltage supervisor. Depending on the characteristics of the LDO (U1) it is recommended to add a pull-down resistor (R11) at its output to ensure **VDD\_USB** is not floating if the LDO (U1) is disabled or the USB cable is not connected, that is, VBUS is not supplied.

**☞** USB bus-powered mode is not supported.



<span id="page-5-0"></span>**Figure 2: USB interface**

| Name     | Component                       | Function                                                    | Comments                                                                                                |
|----------|---------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| U1       | LDO                             | Regulates VBUS (4.4 …5.25 V) down<br>to a voltage of 3.3 V. | Almost no current requirement (~1 mA) if the GNSS<br>receiver is operated as a USB self-powered device. |
| C23, C24 | Capacitors                      |                                                             | Required according to the specification of LDO U1                                                       |
| D2       | Protection diodes               | Protect circuit from overvoltage / ESD<br>when connecting.  | Use low-capacitance ESD protection such as ST<br>Microelectronics USBLC6-2.                             |
| R4, R5   | Serial termination<br>resistors | Establish a full-speed driver<br>impedance of 28…44 Ω       | A value of 27 Ω is recommended.                                                                         |
| R11      | Resistor                        |                                                             | 100 kΩ is recommended.                                                                                  |

<span id="page-5-1"></span>**Table 1: Summary of USB external components**

### **1.4.3 Display Data Channel (DDC)**

An I2C-compatible Display Data Channel (DDC) interface is available with NEO-M8P modules for serial communication with an external host CPU. The interface operates in slave mode only (master mode is not supported). The DDC protocol and electrical interface are fully compatible with the Fast mode of the I2C industry standard. DDC pins **SDA** and **SCL** have internal pull-up resistors.

For more information about the DDC implementation, see u-blox 8 / u-blox M8 Receiver Description Including Protocol Specification [\[2\].](#page-25-3) For bandwidth information, see NEO-M8P Data sheet [\[1\].](#page-25-2)

**☞** The NEO-M8P DDC interface supports serial communication with u-blox cellular modules. See the specification of the applicable cellular module to confirm compatibility.



### **1.4.4 SPI**

An SPI interface is optionally available for communication to a host CPU.

**☞** SPI is not available in the default configuration, because its pins are shared with the UART and DDC interfaces. The SPI interface can be enabled by connecting **D\_SEL** to ground. For speed and clock frequency, see NEO-M8P Data sheet [\[1\].](#page-25-2)

### **1.4.5 TX Ready signal**

The TX Ready signal indicates that the receiver has data to transmit. A listener can wait on the TX Ready signal instead of polling the DDC or SPI interfaces. The UBX-CFG-PRT message enables configuration of signal polarity and buffer threshold (in bytes) before the TX Ready signal goes active. The TX Ready signal can be mapped to UART TXD (PIO 06). The TX Ready function is disabled by default.

**☞** The TX Ready functionality can be enabled and configured by AT commands sent to the u-blox cellular module supporting the feature. For more information, see GPS Implementation and Aiding Features in u-blox wireless modules [\[4\].](#page-25-4)

### <span id="page-6-0"></span>**1.5 I/O pins**

### **1.5.1 RESET\_N: reset input**

Driving **RESET\_N** low activates a hardware reset of the system. Use this pin only to reset the module. Do not use **RESET\_N** to turn the module on and off, since the reset state increases power consumption. With NEO-M8P module **RESET\_N** is an input only.

### **1.5.2 EXTINT: external interrupt input**

**EXTINT** is an external interrupt pin with fixed input voltage thresholds with respect to **VCC** (see NEO-M8P Data sheet [\[1\]](#page-25-2) for more information). It can be used for functions such as accurate external frequency aiding and ON/OFF control. Leave open if unused, this function is disabled by default.

### **1.5.3 SAFEBOOT\_N: input**

If the **SAFEBOOT\_N** pin is "low" at power up, the NEO-M8P module starts in safe boot mode and does not begin GNSS operation. The safe boot mode can be used to recover from situations where the flash has become corrupted.

### **1.5.4 D\_SEL: input**

The **D\_SEL** pin selects the available interfaces between SPI and UART/DDC operation.

If open, the UART and DDC ports are active. If pulled low, the SPI interface is available. See NEO-M8P Data sheet [\[1\].](#page-25-2)

### **1.5.5 LNA\_EN: antenna ON (LNA enable), output**

In power save mode, the system can turn on/off an optional external LNA using the LNA\_EN signal to optimize power consumption.

### **1.5.6 TIMEPULSE: output**

A configurable time pulse signal is available with NEO-M8P modules. The time pulse signal is configured as one pulse per second by default. For more information on programming this function, see u-blox 8 / u-blox M8 Receiver Description including Protocol Specification [\[2\].](#page-25-3)



### **1.5.7 RTK\_STAT: output**

The **RTK\_STAT** pin provides an indication of the RTK positioning status. At start up this pin is set high. When receiving a valid stream of RTCM 3 messages the pin alternates between high and low at the navigation rate, for example, the default rate is 1 Hz. It is set into a continuous low output when the receiver is operating in RTK fixed mode.

### **1.5.8 GEOFENCE\_STAT: output**

This pin indicates the current geofence status, if activated. The pin active polarity and geofence locations are preset using the UBX-NAV-GEOFENCE message allowing up to four circular areas to be defined. Once activated, the receiver continuously compares its current position with the preset geofenced areas. The pin state reflects the current geofence status as to whether the receiver is inside any of the active areas. See u-blox 8 / u-blox M8 Receiver Description including Protocol Specification [\[2\]](#page-25-3) for more information.

### **1.5.9 Electromagnetic interference on I/O lines**

Any I/O signal line with a length greater than a ~3 mm can act as an antenna and may pick up arbitrary RF signals transferring them as noise into the GNSS receiver. This specifically applies to unshielded lines, in which the corresponding GND layer is remote or missing entirely, or lines close to the edges of the printed circuit board.

If, for example, a cellular signal radiates into an unshielded I/O line, it is possible to generate noise of the order of many volts which not only distorts the receiver operation but can also damage it permanently.

On the other hand, noise generated at the I/O pins will emit from unshielded I/O lines. Receiver performance can be degraded when this noise is coupled into the GNSS antenna (see [Figure 14\)](#page-20-1).

To avoid interference through improperly shielded lines, it is recommended to use series resistors (for example, R>20 Ω), ferrite beads (for example, BLM15HD102SN1) or inductors (for example, LQG15HS47NJ02) in the I/O lines. These components affect the signal rise times and hence should be chosen with some care.

[Figure 3](#page-7-0) shows an example of EMI protection measures on the RX/TX line using a ferrite bead. More information is given in section [3.3.](#page-17-0)



<span id="page-7-0"></span>**Figure 3: EMI protection measures**



## <span id="page-8-0"></span>**2 Design**

### <span id="page-8-1"></span>**2.1 Pin description**

| Function | Pin            | No.              | I/O | Description                       | Remarks                                                                                                                                                           |  |  |  |
|----------|----------------|------------------|-----|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| Power    | VCC            | 23               |     | Supply voltage                    | Provide a clean and stable supply.                                                                                                                                |  |  |  |
|          | GND            | 10,12,<br>13, 24 |     | Ground                            | Assure a good GND connection to all GND pins of the<br>module, preferably with a large ground plane.                                                              |  |  |  |
|          | V_BCKP         | 22               |     | Backup supply<br>voltage          | It is recommended to connect a backup supply voltage to<br>V_BCKP to enable warm and hot start features on the<br>positioning modules. Otherwise, connect to VCC. |  |  |  |
|          | VDD_USB        | 7                |     | USB power supply                  | To use the USB interface, connect this pin to 3.0 – 3.6 V.<br>If no USB serial port is used, connect to GND.                                                      |  |  |  |
| Antenna  | RF_IN          | 11<br>I          |     | GNSS signal input<br>from antenna | The connection to the antenna must be routed on the PCB.<br>Use a controlled impedance of 50 Ω to connect RF_IN to<br>the antenna or the antenna connector.       |  |  |  |
|          | VCC_RF         | 9                | O   | Output voltage RF<br>section      | VCC_RF can be used to power an external active antenna.                                                                                                           |  |  |  |
| UART     | TXD /SPI MISO  | 20<br>O          |     | Serial port/ SPI<br>MISO          | Communication interface.<br>Can be programmed as TX Ready for DDC interface.<br>If pin 2 low => SPI MISO.                                                         |  |  |  |
|          | RXD / SPI MOSI | 21<br>I          |     | Serial port / SPI<br>MOSI         | Serial input. Internal pull-up resistor to VCC. Leave open if<br>not used.<br>If pin 2 low => SPI MOSI.                                                           |  |  |  |
| USB      | USB_DM         | 5                | I/O | USB I/O line                      | USB bidirectional communication pin. Leave open if not                                                                                                            |  |  |  |
|          | USB_DP         | 6                | I/O | USB I/O line                      | used.                                                                                                                                                             |  |  |  |
| System   | TIMEPULSE      | 3                | O   | Timepulse signal                  | Configurable timepulse 1 signal (one pulse per second by<br>default). Leave open if not used.                                                                     |  |  |  |
|          | SAFEBOOT_N     | 1                | I   |                                   | SAFEBOOT_N (for future service, updates and<br>reconfiguration, normally leave open)                                                                              |  |  |  |
|          | EXTINT         | 4                | I   | External interrupt<br>0           | External interrupt pin.<br>Internal pull-up resistor to VCC. Leave open if not used.<br>Function is disabled by default.                                          |  |  |  |
|          | RTK_STAT       | 15               | O   | RTK status                        | Shows current RTK position status                                                                                                                                 |  |  |  |
|          | GEOFENCE_STAT  | 16               | O   | Geofence status                   | Active if enabled, polarity programmable                                                                                                                          |  |  |  |
|          | SDA /SPI CS_N  | 18               | I/O | DDC Data / SPI<br>CS_N            | DDC data.<br>If pin 2 low => SPI chip select.                                                                                                                     |  |  |  |
|          | SCL /SPI CLK   | 19               | I   | DDC clock / SPI<br>SCK            | DDC clock.<br>If pin 2 low => SPI clock.                                                                                                                          |  |  |  |
|          | LNA_EN         | 14               | O   | ANT_ON                            | LNA enable can be used to turn an optional external LNA<br>or active antenna on and off                                                                           |  |  |  |
|          | RESET_N        | 8                | I   | Reset input                       | Reset input                                                                                                                                                       |  |  |  |
|          | D_SEL          | 2                | I   | Selects the<br>interface          | Allow selecting UART/DDC or SPI<br>open-> UART/DDC; low->SPI                                                                                                      |  |  |  |
|          | RESERVED       | 17               | -   | Reserved                          | Leave open                                                                                                                                                        |  |  |  |

**Table 2: NEO-M8P pinout** 

### **2.1.1 Pin name changes**

Selected pin names were updated to agree with a common naming convention across u-blox modules. The pins have not changed their operation and are the same physical hardware but with updated names. The table below lists the pins that have a changed name along with their old and new names.



| No. | Previous name | New name          |
|-----|---------------|-------------------|
| 14  | ANT_ON        | LNA_EN            |
| 20  | TxD           | TXD /<br>SPI MISO |
| 21  | RxD           | RXD /<br>SPI MOSI |

**Table 3: NEO-M8P module pin renaming**

### <span id="page-9-0"></span>**2.2 Minimal design**

This is a minimal design for a NEO-M8P GNSS receiver.



**Figure 4: NEO-M8P passive antenna design**

### <span id="page-9-1"></span>**2.3 Layout: Footprint and paste mask**

[Figure 5](#page-10-1) describes the footprint and provides recommendations for the paste mask for NEO-M8P LCC modules. These are recommendations only and not specifications. Note that the copper and solder masks have the same size and position.

To improve the wetting of the half vias, reduce the amount of solder paste under the module and increase the volume outside of the module by defining the dimensions of the paste mask to form a Tshape (or equivalent) extending beyond the copper mask. For the stencil thickness, see section [3.2.](#page-14-2)

**☞** Consider the paste mask outline when defining the minimal distance to the next component. The exact geometry, distance, stencil thickness and solder paste volumes must be adapted to the customer's specific production processes (for example, soldering).





<span id="page-10-1"></span>**Figure 5: NEO-M8P paste mask / NEO-M8P footprint**

### <span id="page-10-0"></span>**2.4 Antenna**

With RTK operation, the antenna and its placement are critical system factors, both for the base and rover. The minimum receiver signal strengths to track the signal phase are higher than conventional GNSS receivers, at about 34 dBHz, and require good antenna efficiency with a stable phase center. Hence, use of a relatively large ceramic patch, that is, 25 mm square or greater will provide reasonable performance in terms of efficiency and accuracy vs. cost.

For a base station antenna installation, try to mitigate the effects of multi-path reception from nearby objects or buildings. Using a ground plane minimizes the effects of ground reflections and enhance the antenna efficiency.

For the rover, using a ground plane with a minimum diameter of 10 centimeter is recommended. It is also recommended to position the rover antenna away from any potential reflectors on the vehicle to get the best overall results. Exercize care with rover vehicles that emit RF energy from, for example, motors, as interference may extend into the GNSS band and couple into the GNSS antenna suppressing the wanted signal.

### **2.4.1 Antenna design with passive antenna**

A design using a passive antenna requires more attention to the layout of the RF section. Typically, a passive antenna is located near electronic components; therefore, make sure to reduce electrical noise that may interfere with the antenna performance. Passive antennas do not require a DC bias voltage and can be directly connected to the RF input pin **RF\_IN**. Sometimes, they may also need a passive matching network to match the impedance to 50 Ω.

[Figure 6](#page-11-0) shows a minimal setup for a design with a good GNSS patch antenna.





<span id="page-11-0"></span>

**☞** Use an antenna that has sufficient bandwidth to receive all GNSS constellations. See Appendix [B.](#page-23-0)

[Figure](#page-11-1) 7 shows a design using an external LNA to increase the sensitivity for best performance with passive antenna.



<span id="page-11-1"></span>**Figure 7: Module design with passive antenna and external LNA (for exact pin orientation see NEO-M8P Data sheet [\[1\]\)](#page-25-2)**

The **LNA\_EN** pin (LNA enable) can be used to turn an optional external LNA on and off.

The **VCC\_RF** output can be used to supply the LNA with a filtered supply voltage.

- **☞** Ensure the LNA has enough bandwidth to amplify all the required satellite signals.
- **☞** An external LNA is only required if the antenna is far away. In that case the LNA must be placed close to the passive antenna.
- **☞** Add a SAW filter before or after the LNA to prevent any blocking issues from out-of-band signals.

### **2.4.2 Active antenna design**

Active antennas have an integrated low-noise amplifier. Active antennas require a power supply that contributes to the total GNSS system power consumption budget with additional 5 to 20 mA typically.

If the supply voltage of the NEO-M8 receiver matches the supply voltage of the antenna (for example, 3.0 V), use the filtered supply voltage available at pin **VCC\_RF** as shown in [Figure 8.](#page-12-0)



#### **Active antenna design using VCC\_RF pin to supply the active antenna**



<span id="page-12-0"></span>**Figure 8: Active antenna design, external supply from VCC\_RF (for exact pin orientation see NEO-M8P Data sheet [1])**

The L,C passive component values and recommended types are given in Appendix [B.](#page-23-0) If the **VCC\_RF** voltage does not match with the supply voltage of the active antenna, use a filtered external supply as shown in [Figure 9.](#page-12-1) To ensure that the maximum DC input voltage at the LNA input is not exceeded, use a DC blocking capacitor (value C).

#### **Active antenna design powered from external supply**



<span id="page-12-1"></span>**Figure 9: Active antenna design, direct external supply (for exact pin orientation see NEO-M8P Data sheet [1])**

**☞** The circuit shown i[n Figure 9](#page-12-1) works with all u-blox M8 modules, also with modules without **VCC\_RF** output.



### <span id="page-13-0"></span>**2.5 Layout design-in: Thermal management**

During design-in do not place the module near sources of heating or cooling. The receiver oscillator is sensitive to sudden changes in ambient temperature which can adversely impact satellite signal tracking. Sources can include co-located power devices, cooling fans or thermal conduction via the PCB. Take into account the following questions when designing in the module.

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?
- **⚠** High temperature drift and air vents can affect the GNSS performance. For best performance, avoid high temperature drift and air vents near the module.



## <span id="page-14-0"></span>**3 Product handling**

### <span id="page-14-1"></span>**3.1 Packaging, shipping, storage, and moisture preconditioning**

For information pertaining to reels and tapes, moisture sensitivity levels (MSL), shipment and storage information, as well as drying for preconditioning, see NEO-M8P Data sheet [\[1\].](#page-25-2)

#### **Population of modules**

**☞** When populating the modules, make sure that the pick and place machine is aligned to the copper pins of the module and not on the module edge.

### <span id="page-14-2"></span>**3.2 Soldering**

#### **Soldering paste**

Use of "no clean" soldering paste is highly recommended, as it does not require cleaning after the soldering process has taken place. The paste in the example below meets these criteria.

| Soldering paste:     | OM338 SAC405 / Nr.143714 (Cookson Electronics)            |
|----------------------|-----------------------------------------------------------|
| Alloy specification: | Sn 95.5/ Ag 4/ Cu 0.5 (95.5% Tin/ 4% Silver/ 0.5% Copper) |
| Melting temperature: | 217 °C                                                    |
| Stencil thickness:   | See section 2.3                                           |

The final choice of the soldering paste depends on the approved manufacturing procedures.

The paste-mask geometry for applying soldering paste must meet the recommendations.

**☞** The quality of the solder joints on the connectors ('half vias') should meet the appropriate IPC specification.

#### **Reflow soldering**

**A convection-type soldering oven is highly recommended** over the infrared-type radiation oven. Convection heated ovens allow precise control of the temperature, and all parts heat up evenly, regardless of material properties, thickness of components and surface color.

As a reference, see IPC-7530 Guidelines for temperature profiling for mass soldering (reflow and wave) processes, published in 2001.

#### **Preheat phase**

During the initial heating of component leads and balls, residual humidity will be dried out. Note that this preheat phase will not replace prior baking procedures.

- Temperature rise rate: max. 3 °C/s. If the temperature rise is too rapid in the preheat phase it may cause excessive slumping.
- Time: 60 120 s. If the preheat is insufficient, rather large solder balls tend to generate. Conversely, if performed excessively, fine balls and large balls will be generated in clusters.
- End temperature: 150 200 °C. If the temperature is too low, non-melting tends to be caused in areas containing large heat capacity.

#### **Heating/ Reflow phase**

The temperature rises above the liquidus temperature of 217 °C. Avoid a sudden rise in temperature as the slump of the paste could become worse.

- Limit time above 217 °C liquidus temperature: 40 60 s
- Peak reflow temperature: 245 °C



#### **Cooling phase**

A controlled cooling avoids negative metallurgical effects of the solder (solder becomes more brittle) and possible mechanical tensions in the products. Controlled cooling helps to achieve bright solder fillets with a good shape and low contact angle.

- Temperature fall rate: max 4 °C/s
- **☞** To avoid falling off, place the NEO-M8P modules on the topside of the motherboard during soldering.

The final soldering temperature chosen at the factory depends on additional external factors like choice of soldering paste, size, thickness, and properties of the base board, and so on. Exceeding the maximum soldering temperature in the recommended soldering profile may permanently damage the module.



**Figure 10: Recommended soldering profile**

**☞** NEO-M8P modules **must not** be soldered with a damp heat process.

#### **Optical inspection**

After soldering the NEO-M8P module, consider an optical inspection step to check whether:

- The module is properly aligned and centered over the pads
- All pads are properly soldered
- No excess solder has created contacts to neighboring pads, or possibly to pad stacks and vias nearby

#### **Cleaning**

In general, cleaning the populated modules is strongly discouraged. Residues underneath the modules cannot be easily removed with a washing process.

- Cleaning with water will lead to capillary effects where water is absorbed in the gap between the baseboard and the module. The combination of residues of soldering flux and encapsulated water leads to short circuits or resistor-like interconnections between neighboring pads.
- Cleaning with alcohol or other organic solvents can result in soldering flux residues flooding into the two housings, areas that are not accessible for post-wash inspections. The solvent will also damage the sticker and the ink-jet printed text.
- Ultrasonic cleaning will permanently damage the module, in particular the quartz oscillators.



The best approach is to use a "no clean" soldering paste and eliminate the cleaning step after the soldering.

#### **Repeated reflow soldering**

Only single reflow soldering processes are recommended for boards populated with NEO-M8P modules. To avoid upside-down orientation during the second reflow cycle, do not submit NEO-M8P modules to two reflow cycles on a board populated with components on both sides in order. In such a case, always place the module on the side of the board which is submitted into the last reflow cycle. This is because there is a risk of the module falling off due to the significantly higher weight in relation to other components.

Two reflow cycles can be considered by excluding the above-described upside-down scenario and taking into account the rework conditions described in this section.

**☞** Repeated reflow soldering processes and soldering the module upside down are not recommended.

#### **Wave soldering**

Base boards with combined through-hole technology (THT) components and surface-mount technology (SMT) devices require wave soldering to solder the THT components. Only a single wave soldering process is encouraged for boards populated with NEO-M8P modules.

#### **Hand soldering**

Hand soldering is allowed. Use a soldering iron temperature setting equivalent to 350 °C. Place the module precisely on the pads. Start with a cross-diagonal fixture soldering (for example, pins 1 and 15), and then continue from left to right.

#### **Rework**

The NEO-M8P module can be unsoldered from the baseboard using a hot air gun. When using a hot air gun for unsoldering the module, a maximum of one reflow cycle is allowed. In general, we do not recommend using a hot air gun because this is an uncontrolled process and might damage the module.

**⚠** Attention: use of a hot air gun can lead to overheating and severely damage the module. Always avoid overheating the module.

After the module is removed, clean the pads before placing and hand soldering a new module.

**⚠** Never attempt a rework on the module itself, for example, replacing individual components. Such actions immediately terminate the warranty.

In addition to the two reflow cycles, manual rework on particular pins by using a soldering iron is allowed. Manual rework steps on the module can be done several times.

#### **Conformal coating**

Certain applications employ a conformal coating of the PCB using HumiSeal® or other related coating products. These materials affect the HF properties of the GNSS module and it is important to prevent them from flowing into the module. The RF shields do not provide 100% protection for the module from coating liquids with low viscosity; take care when applying the coating.



**☞** Conformal coating of the module will void the warranty.



#### **Casting**

If casting is required, use viscose or another type of silicon pottant. The OEM is strongly advised to qualify such processes in combination with the NEO-M8P module before implementing it in the production.



### **Grounding metal covers**

Attempts to improve grounding by soldering ground cables, wick or other forms of metal strips directly onto the EMI covers is done at the customer's own risk. The numerous ground pins should be sufficient to provide optimum immunity to interferences and noise.

**☞** u-blox makes no warranty for damages to the NEO-M8P module caused by soldering metal cables or any other forms of metal strips directly onto the EMI covers.

#### **Use of ultrasonic processes**

Some components on the NEO-M8P module are sensitive to ultrasonic waves. Use of any ultrasonic processes (cleaning, welding, and so on) may cause damage to the GNSS receiver.

**☞** u-blox offers no warranty against damages to the NEO-M8P module caused by any ultrasonic processes.

### <span id="page-17-0"></span>**3.3 EOS/ESD/EMI precautions**

When integrating GNSS positioning modules into wireless systems, consider the electromagnetic and voltage susceptibility issues carefully. Wireless systems include components that can produce electrical overstress (EOS) and electro-magnetic interference (EMI). CMOS devices are more sensitive to such influences because their failure mechanism is defined by the applied voltage, whereas bipolar semiconductors are more susceptible to thermal overstress. The following design guidelines are provided to help in designing robust yet cost-effective solutions.

- **⚠** To avoid overstress damage during production or in the field it is essential to observe strict EOS/ESD/EMI handling and protection measures.
- **⚠** To prevent overstress damage at the RF\_IN of your receiver, never exceed the maximum input power (see NEO-M8P Data sheet [\[1\]\)](#page-25-2).

#### **Electrostatic discharge (ESD)**

Electrostatic discharge (ESD) is the sudden and momentary electric current that flows between two objects at different electrical potentials caused by direct contact or induced by an electrostatic field. The term is usually used in the electronics and other industries to describe momentary unwanted currents that may cause damage to electronic equipment.



#### **ESD handling precautions**

ESD prevention is based on establishing an electrostatic protective area (EPA). The EPA can be a small work station or a large manufacturing area. The main principle of an EPA is that there are no highly charged materials near ESD-sensitive electronics, all conductive materials are grounded, workers are grounded, and charge build-up on ESD sensitive electronics is prevented. International standards are used to define typical EPA and can be obtained for example from the International Electrotechnical Commission (IEC) or American National Standards Institute (ANSI).

GNSS positioning modules are sensitive to ESD and require special precautions when handling. Take particular care when handling patch antennas, due to the risk of electrostatic charges. In addition to



standard ESD safety practices, take the following measures into account whenever handling the receiver.

- Unless there is a galvanic coupling between the local GND (i.e. the work table) and the PCB GND, the first point of contact when handling the PCB must always be between the local GND and PCB GND.
- Ground a patch antenna before mounting.
- When handling the RF pin, do not come into contact with any charged capacitors and be careful when contacting materials that can develop charges (e.g. patch antenna ~10 pF, coax cable ~50 – 80 pF/m, soldering iron).
- To prevent electrostatic discharge through the RF input, do not touch any exposed antenna area. If there is any risk that such exposed antenna area is touched in a non-ESD protected work area, implement proper ESD protection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, make sure to use an ESD safe soldering iron (tip).



**⚠** Failure to observe these precautions can severely damage the GNSS module!

#### **ESD protection measures**

- **⚠** GNSS positioning modules are sensitive to electrostatic discharge (ESD). Special precautions are required when handling.
- **☞** For more robust designs, employ additional ESD protection measures. Using an LNA with appropriate ESD rating can provide enhanced GNSS performance with passive antennas and increase ESD protection.

Most defects caused by ESD can be prevented by following strict ESD protection rules for production and handling. When implementing passive antenna patches or external antenna connection points, additional ESD measures can also avoid failures in the field as shown in [Figure 11.](#page-18-0)



#### <span id="page-18-0"></span>**Figure 11: ESD precautions**

**☞** Protection measure A is preferred because it offers the best GNSS performance and best level of ESD protection.

#### **Electrical overstress (EOS)**

Electrical overstress (EOS) usually describes situations when the maximum input power exceeds the maximum specified ratings. EOS failure can happen if RF emitters are close to a GNSS receiver or its



antenna. EOS causes damage to the chip structures. If the RF\_IN circuitry is damaged by EOS, it is hard to determine whether the chip structures have been damaged by ESD or EOS.

#### **EOS protection measures**

**☞** For designs with GNSS positioning modules and wireless transceivers (for example, GSM/GPRS) in close proximity, ensure sufficient isolation between the wireless and GNSS antennas. If the wireless power output causes the specified maximum power input at the GNSS RF\_IN to be exceeded, employ EOS protection measures to prevent overstress damage.

For robustness, EOS protection measures as shown in [Figure 12](#page-19-0) are recommended for designs combining wireless communication transceivers (for example, GSM, GPRS) and GNSS in the same design or in close proximity.



<span id="page-19-0"></span>

#### **Electromagnetic interference (EMI)**

Electromagnetic interference (EMI) is the addition or coupling of energy causing a spontaneous reset of the GNSS receiver or resulting in unstable performance. In addition to EMI degradation due to selfjamming (see section [1.5\)](#page-6-0) any electronic device near the GNSS receiver can emit noise that can lead to EMI disturbances or damage.

The following elements are critical regarding EMI:

- Unshielded connectors (for example, pin rows)
- Weakly shielded lines on PCB (for example, on top or bottom layer and especially at the border of a PCB)
- Weak GND concept (for example, small and/or long ground line connections)

EMI protection measures are recommended when RF emitting devices are near the GNSS receiver. To minimize the effect of EMI a robust grounding concept is essential. To achieve electromagnetic robustness follow the standard EMI suppression techniques.

#### <http://www.murata.com/products/emc/knowhow/index.html> <http://www.murata.com/products/emc/knowhow/pdf/4to5e.pdf>

Improved EMI protection can be achieved by inserting a resistor, or better yet, a ferrite bead or an inductor (see [Table 4\)](#page-22-2) into any unshielded PCB lines connected to the GNSS receiver. Place the resistor as close to the GNSS receiver pin as possible.

Alternatively, feed-through capacitors with good GND connection can be used to protect, for example, the **VCC** supply pin against EMI. A selection of feed-through capacitors is listed in [Table 4.](#page-22-2)



#### **Intended use**

**☞** To mitigate any performance degradation of a radio equipment under EMC disturbance, system integration shall adopt appropriate EMC design practice and not contain cables over three meters on signal and supply ports.

### <span id="page-20-0"></span>**3.4 Applications with cellular modules**

GSM terminals transmit power levels up to 2 W (+33 dBm) peak, 3G and LTE up to 250 mW continuous. Consult the corresponding product data sheet listed in the Related documents section for the absolute maximum power input at the GNSS receiver.

**☞** See GPS Implementation and Aiding Features in u-blox wireless modules [\[4\].](#page-25-4)

#### **Isolation between GNSS and GSM antenna**

In a handheld design, an antenna isolation of approximately 20 dB can be reached with careful placement of the antennas. If this isolation factor cannot be achieved, for example, in the case of an integrated GSM/GNSS antenna, an additional input filter is required on the GNSS side to reduce the energy coupled from the GSM transmitter. Examples of these filters are SAW Filters from Epcos (B9444 or B7839) or Murata.

#### **Increasing interference immunity**

Interference signals come from in-band and out-of-band frequency sources.

#### **In-band interference**

With in-band interference, the signal frequency is very close to the GNSS constellation frequency used, for example, GPS frequency of 1575 MHz (see [Figure 13\)](#page-20-2). Such interference signals are typically caused by harmonics emitted from displays, micro-controller, data-bus systems, and so on.



<span id="page-20-2"></span>

<span id="page-20-1"></span>**Figure 14: In-band interference sources**



Measures against in-band interference include:

- Maintaining a good grounding concept in the design
- Shielding
- Layout optimization
- Filtering
- Placement of the GNSS antenna
- Adding a CDMA, GSM, WCDMA band pass filter before handset antenna

#### **Out-of-band interference**

Out-of-band interference is caused by signal frequencies that are different from the GNSS carrier (see [Figure 15\)](#page-21-0). The main sources are wireless communication systems such as GSM, CDMA, WCDMA, Wi-Fi, BT, and so on.



#### <span id="page-21-0"></span>**Figure 15: Out-band interference signals**

Measures against out-band interference include maintaining a good grounding concept in the design and adding a SAW or band pass ceramic filter (as recommend in section [3\)](#page-14-0) into the antenna input line to the GNSS receiver (see [Figure 16\)](#page-21-1).



#### <span id="page-21-1"></span>**Figure 16: Measures against out-band interference**

**☞** For design-in recommendations in combination with cellular operation see the Appendix.

**☞** See GPS Implementation and Aiding Features in u-blox wireless modules [\[4\].](#page-25-4)



## <span id="page-22-0"></span>**Appendix**

## <span id="page-22-1"></span>**A Recommended parts**

Recommended parts are selected on a data sheet basis only. Other components may also be used.

| Part                           | Manufacturer Part ID |                          | Remarks                       | Parameters to consider                             |  |
|--------------------------------|----------------------|--------------------------|-------------------------------|----------------------------------------------------|--|
| Diode                          | ON                   | ESD9R3.3ST5G             | Standoff voltage>3.3 V        | Low capacitance < 0.5 pF                           |  |
| semiconductor                  |                      | ESD9L3.3ST5G             | Standoff voltage>3.3 V        | Standoff voltage > Voltage for active<br>antenna   |  |
|                                |                      | ESD9L5.0ST5G             | Standoff voltage>5 V          | Low inductance                                     |  |
| SAW                            | TDK/ EPCOS           | B8401: B39162-B8401-P810 | GPS+GLONASS                   | High attenuation                                   |  |
|                                | TDK/ EPCOS           | B3913: B39162B3913U410   | GPS+GLONASS+BeiDou            | For automotive application                         |  |
|                                | TDK/ EPCOS           | B4310: B39162B4310P810   | GPS+GLONASS                   | Compliant to the AEC-Q200 standard                 |  |
|                                | ReyConns             | NDF9169                  | GPS+GLONASS                   | Low insertion loss, only for mobile<br>application |  |
|                                | Murata               | SAFFB1G56KB0F0A          | GPS+GLONASS+BeiDou            | Low insertion loss, only for mobile<br>application |  |
|                                | Murata               | SAFEA1G58KB0F00          | GPS+GLONASS                   | Low insertion loss, only for mobile<br>application |  |
|                                | Murata               | SAFEA1G58KA0F00          | GPS+GLONASS                   | High attenuation, only for mobile<br>application   |  |
|                                | Murata               | SAFFB1G58KA0F0A          | GPS+GLONASS                   | High attenuation, only for mobile<br>application   |  |
|                                | Murata               | SAFFB1G58KB0F0A          | GPS+GLONASS                   | Low insertion loss, only for mobile<br>application |  |
|                                | TAI-SAW              | TA1573A                  | GPS+GLONASS                   | Low insertion loss                                 |  |
|                                | TAI-SAW              | TA1343A                  | GPS+GLONASS+BeiDou            | Low insertion loss                                 |  |
|                                | TAI-SAW              | TA0638A                  | GPS+GLONASS+BeiDou            | Low insertion loss                                 |  |
| LNA                            | JRC                  | NJG1143UA2               | LNA                           | Low noise figure, up to 15 dBm RF<br>input power   |  |
| Inductor                       | Murata               | LQG15HS27NJ02            | L, 27 nH                      | Impedance at freq. GPS > 500 Ω                     |  |
| Capacitor                      | Murata               | GRM1555C1E470JZ01        | C, 47 pF                      | DC-block                                           |  |
| Ferrite<br>bead                | Murata               | BLM15HD102SN1            | FB                            | High IZI at fGSM                                   |  |
| Feed-through<br>capacitor      | Murata               | NFL18SP157X1A3           | Monolithic type<br>Array type | Load capacitance appropriate to<br>signal rate     |  |
| for signal                     |                      | NFA18SL307V1A45          |                               |                                                    |  |
| Feed -<br>through<br>capacitor | Murata               | NFM18PC ….<br>NFM21P….   | 0603 2A<br>0805 4A            | Rs < 0.5 Ω                                         |  |
| Resistor                       |                      | 10 Ω ± 10%, min 0.250 W  | Rbias                         |                                                    |  |
|                                |                      | 560 Ω ± 5%               | R2                            |                                                    |  |
|                                |                      | 100 kΩ ± 5%              | R3, R4                        |                                                    |  |

<span id="page-22-2"></span>**Table 4: Recommended parts**



## <span id="page-23-0"></span>**B Recommended antennas**

| Manufacturer                                          | Order no.       | Comments                                                            |
|-------------------------------------------------------|-----------------|---------------------------------------------------------------------|
| Tallysman (www.tallysman.com)                         | TW3400/TW3402   | GPS+GLONASS, 2.5-16 V active, good phase center<br>variation        |
| Tallysman (www.tallysman.com)                         | TW3710          | GPS+BeiDou+GLONASS, 2.5-16 V active, good phase center<br>variation |
| Taoglas (www.taoglas.com )                            | A.40.A.301111   | GPS+GLONASS, 2.5-5.5 V active, good axial ratio                     |
| Hirschmann (www.hirschmann-car.com)                   | GLONASS 9 M     | GPS+GLONASS active                                                  |
| Taoglas (www.taoglas.com )                            | AA.160.301111   | 36 x 36 x 4 mm, 3-5 V 30 mA active                                  |
| Taoglas (www.taoglas.com )                            | AA.161.301111   | 36 x 36 x 3 mm, 1.8 to 5.5 V / 10 mA at 3 V active                  |
| INPAQ (www.inpaq.com.tw)                              | B3G02G-S3-01-A  | 2.7 to 3.9 V / 10 mA active                                         |
| Amotech (www.amotech.co.kr)                           | B35-3556920-2J2 | 35 x 35 x 3 mm GPS+GLONASS passive                                  |
| Additional antenna manufacturer: Allis Communications |                 |                                                                     |

**Table 5: Recommend antennas**



<span id="page-24-0"></span>**C Design-in recommendations in combination with cellular operation**

| Product    |         |         | Receiver chain |         | Cellular and GNSS<br>simultaneous operation |                            |             |                         |          |             |
|------------|---------|---------|----------------|---------|---------------------------------------------|----------------------------|-------------|-------------------------|----------|-------------|
|            |         |         |                |         |                                             |                            |             | Passive GNSS<br>antenna | antenna  | Active GNSS |
| mily<br>Fa | Variant | Antenna | W LNA<br>SA    | W<br>SA | On-chip LNA                                 | (chip-external)<br>W<br>SA | 2G cellular | 3G/4G cellular          | 2G/3G/4G | cellular    |
| MAX-6      | Any     |         |                |         | •                                           | •                          |            |                         |         |            |
| NEO-6      | Any     |         |                |         | •                                           | •                          |            |                         |         |            |
| LEA-6      | Any     |         |                |         | •                                           | •                          |            |                         |         |            |
| EVA-7      | M       |         |                |         | •                                           |                            |             |                         |         |            |
|            | C       |         |                |         | •                                           |                            |            |                         |         |            |
| MAX-7      | W       |         |                |         | •                                           |                            |            |                         |         |            |
|            | Q       |         |                |         | •                                           |                            |            |                         |         |            |
|            | N       |         | •              |         | •                                           |                            |            |                        |         |            |
| NEO-7      | M       |         |                |         | •                                           |                            |            |                         |         |            |
|            | P       |         |                | •       | •                                           |                            |            |                        |         |            |
| EVA-M8     | M       |         |                |         | •                                           |                            |             |                         |         |            |
|            | C       |         |                |         | •                                           |                            |            |                         |         |            |
| MAX-M8     | W       |         |                |         | •                                           |                            |            |                         |         |            |
|            | Q       |         |                |         | •                                           |                            |            |                         |         |            |
|            | N       |         | •              |         | •                                           |                            |            |                        |         |            |
|            | M       |         |                |         | •                                           |                            |            |                         |         |            |
| NEO-M8     | Q       |         | •              |         | •                                           |                            |            |                        |         |            |
|            | T       |         | •              |         | •                                           |                            |            |                        |         |            |
|            | P       |         | •              |         | •                                           |                            |            |                        |         |            |
|            | S       |         |                | •       | •                                           |                            |            |                        |         |            |
| LEA-M8     | T       |         |                | •       | •                                           |                            |            |                        |         |            |
| PAM-7      | Q       | •       | •              | •       | •                                           |                            |            |                        |         |            |
|            | C       | •       | •              |         | •                                           |                            |            |                        |         |            |
| CAM-M8     | Q       | •       | •              |         | •                                           |                            |            |                        |         |            |

**• = integrated = optimal performance**

**Table 6: Combinations of u-blox GNSS modules with different cellular technologies (2G/3G/4G)**

**☞** See GPS Implementation and Aiding Features in u-blox wireless modules [\[4\].](#page-25-4)



## <span id="page-25-0"></span>**Related documents**

- <span id="page-25-2"></span>[1] NEO-M8P data sheet[, UBX-15016656](https://www.u-blox.com/docs/UBX-15016656)
- <span id="page-25-3"></span>[2] u-blox 8 / u-blox M8 Receiver Description including Protocol Specification (Public version)[, UBX-](https://www.u-blox.com/docs/UBX-13003221)[13003221](https://www.u-blox.com/docs/UBX-13003221)
- [3] GNSS Antennas application note, [UBX-15030289](https://www.u-blox.com/docs/UBX-15030289)
- <span id="page-25-4"></span>[4] GPS Implementation and Aiding Features in u-blox wireless modules, [UBX-13001849](https://www.u-blox.com/docs/UBX-13001849)

**☞** For regular updates to u-blox documentation and to receive product change notifications, register on our homepage [\(www.u-blox.com\)](http://www.u-blox.com/).

## <span id="page-25-1"></span>**Revision history**

| Revision | Date        | Name | Comments                                                                                                                                                                                                                                                                                |
|----------|-------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 25-Feb-2016 | byou | Advance Information (ES phase I)                                                                                                                                                                                                                                                        |
| R02      | 07-Jun-2016 | byou | Advance Information for Flash FW 3.01 HPG 1.11 (ES phase II)                                                                                                                                                                                                                            |
| R03      | 27-Sep-2016 | byou | Advance Information for Flash FW3.01 HPG 1.20 (ES Phase III)                                                                                                                                                                                                                            |
| R04      | 20-Jan-2016 | byou | Early Production Information for Flash FW3.01 HPG 1.30 (IP)                                                                                                                                                                                                                             |
| R05      | 26-May-2017 | byou | Early Production Information for Flash FW3.01 HPG 1.40 (IP)                                                                                                                                                                                                                             |
| R06      | 25-Oct-2017 | msul | Information on RED DoC added in European Union regulatory compliance section;<br>Intended use case for EMI is added in section 3.3 EOS/ESD/EMI precautions; Legal<br>statement changes done; Updated Contacts with feedback e-mail.<br>Production Information for Flash FW3.01 HPG 1.40 |
| R07      | 07-Feb-2020 | smos | Updated style of document to current CI. M                                                                                                                                                                                                                                              |
| R08      | 26-May-2020 | mala | Updated type number and PCN reference page 2, added section 2.5 Layout design<br>in: Thermal management.                                                                                                                                                                                |
| R09      | 19-Aug-2021 | dama | Updated type number, FW and PCN reference on page 2                                                                                                                                                                                                                                     |



## <span id="page-26-0"></span>**Contact**

#### For complete contact information, visit us at [www.u-blox.com.](http://www.u-blox.com/)

#### **u-blox Offices**

#### **North, Central and South America**

#### **u-blox America, Inc.**

Phone: +1 703 483 3180 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Regional Office West Coast:**

Phone: +1 408 573 3640 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

#### **Technical Support:**

Phone: +1 703 483 3185 E-mail: [support@u-blox.com](mailto:support@u-blox.com)

#### **Headquarters Europe, Middle East, Africa**

**u-blox AG**  Phone: +41 44 722 74 44 E-mail: [info@u-blox.com](mailto:info@u-blox.com) Support: [support@u-blox.com](mailto:support@u-blox.com)

#### **Asia, Australia, Pacific**

#### **u-blox Singapore Pte. Ltd.**

Phone: +65 6734 3811 E-mail: [info\\_ap@u-blox.com](mailto:info_ap@u-blox.com) Support: [support\\_ap@u-blox.com](mailto:support_ap@u-blox.com)

#### **Regional Office Australia:**

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

#### **Regional Office Japan (Osaka):**

Phone: +81 6 6941 3660 E-mail: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

#### **Regional Office Japan (Tokyo):**

Phone: +81 3 5775 3850 E-mail: [info\\_jp@u-blox.com](mailto:info_jp@u-blox.com) Support: [support\\_jp@u-blox.com](mailto:support_jp@u-blox.com)

#### **Regional Office Korea:**

Phone: +82 2 542 0861 E-mail: [info\\_kr@u-blox.com](mailto:info_kr@u-blox.com) Support: [support\\_kr@u-blox.com](mailto:support_kr@u-blox.com)

#### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 E-mail: [info\\_tw@u-blox.com](mailto:info_tw@u-blox.com) Support: [support\\_tw@u-blox.com](mailto:support_tw@u-blox.com)