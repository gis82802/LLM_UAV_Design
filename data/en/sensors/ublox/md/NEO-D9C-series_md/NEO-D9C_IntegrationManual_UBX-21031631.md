

# **NEO-D9C**

## **QZSS correction service receiver**

**Integration manual**



#### **Abstract**

This document describes the features and specifications of the NEO-D9C QZSS correction service receiver.

**www.u-blox.com**







# **Document information**

| Title                  | NEO-D9C                          |             |
|------------------------|----------------------------------|-------------|
| Subtitle               | QZSS correction service receiver |             |
| Document type          | Integration manual               |             |
| Document number        | UBX-21031631                     |             |
| Revision and date      | R03                              | 15-Dec-2022 |
| Disclosure restriction | C1-Public                        |             |

This document applies to the following products:

| Type number    | FW version | IN/PCN reference | RN reference |
|----------------|------------|------------------|--------------|
| NEO-D9C-00A-00 | QZS 1.01   | -                | UBX-21030680 |
| NEO-D9C-00B-02 | QZS 1.01   | -                | UBX-21030680 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2022, u-blox AG.



| 1 Integration<br>manual<br>overview                                   | 5  |
|-----------------------------------------------------------------------|----|
| 2 System<br>description6                                              |    |
| 2.1 Overview 6                                                        |    |
| 2.1.1 QZSS L6 augmentation service 6                                  |    |
| 2.2 Architecture8                                                     |    |
| 2.2.1 Block diagram8                                                  |    |
|                                                                       |    |
| 3 Receiver<br>functionality                                           | 9  |
| 3.1 Receiver configuration 9                                          |    |
| 3.1.1 Changing the receiver configuration9                            |    |
| 3.1.2 Default QZSS configuration9                                     |    |
| 3.1.3 Default interface settings 9                                    |    |
| 3.1.4 Basic receiver configuration 10                                 |    |
| 3.1.5 QZSS L6 satellite and message selection10                       |    |
| 3.1.6 QZSS L6 data message output13                                   |    |
| 3.2 Communication interfaces 14                                       |    |
| 3.2.1 UART15                                                          |    |
| 3.2.2 I2C interface16                                                 |    |
| 3.2.3 SPI interface19                                                 |    |
| 3.2.4 USB interface20                                                 |    |
| 3.3 Predefined PIOs21                                                 |    |
| 3.3.1 D_SEL21                                                         |    |
| 3.3.2 RESET_N 21                                                      |    |
| 3.3.3 SAFEBOOT_N21                                                    |    |
| 3.3.4 Extended TX timeout 22                                          |    |
| 3.4 Security 22                                                       |    |
| 3.4.1 Receiver status monitoring 22<br>3.5 Forcing a receiver reset22 |    |
| 3.6 Firmware upload22                                                 |    |
|                                                                       |    |
| 4 Design                                                              | 24 |
| 4.1 Pin assignment24                                                  |    |
| 4.2 Antenna25                                                         |    |
| 4.2.1 Antenna bias27                                                  |    |
| 4.3 Power supply30                                                    |    |
| 4.3.1 VCC: Main supply voltage 30                                     |    |
| 4.3.2 NEO-D9C power supply 30                                         |    |
| 4.4 NEO-D9C minimal design 30                                         |    |
| 4.5 EOS/ESD precautions 31                                            |    |
| 4.5.1 ESD protection measures 31                                      |    |
| 4.5.2 EOS precautions32                                               |    |
| 4.5.3 Safety precautions 32                                           |    |
| 4.6 Electromagnetic interference on I/O lines32                       |    |
| 4.6.1 General notes on interference issues33                          |    |
| 4.6.2 In-band interference mitigation33                               |    |
| 4.6.3 Out-of-band interference 34                                     |    |

| 4.7 Layout34                                      |    |
|---------------------------------------------------|----|
| 4.7.1 Placement34                                 |    |
| 4.7.2 Thermal management 34                       |    |
| 4.7.3 Package footprint, copper and paste mask 35 |    |
| 4.7.4 Layout guidance 36                          |    |
| 4.8 Design guidance38                             |    |
| 4.8.1 General considerations 38                   |    |
| 4.8.2 RF front-end circuit options 38             |    |
| 4.8.3 Antenna/RF input 39                         |    |
| 4.8.4 Ground pads40                               |    |
| 4.8.5 Schematic design 40                         |    |
| 4.8.6 Layout design-in guideline 40               |    |
| 5 Product<br>handling                             | 41 |
| 5.1 ESD handling precautions 41                   |    |
| 5.2 Soldering41                                   |    |
| 5.3 Tapes 45                                      |    |
| 5.4 Reels 46                                      |    |
| 5.5 Moisture sensitivity levels 46                |    |
| Appendix                                          | 47 |
| A Stacked patch antenna47                         |    |
| B Glossary48                                      |    |
| Related<br>documents                              | 50 |
| Revision<br>history51                             |    |
|                                                   |    |



# <span id="page-4-0"></span>**1 Integration manual overview**

This document is an important source of information on all aspects of NEO-D9C QZSS correction service receiver. The purpose of this document is to provide guidelines for a successful integration of the receiver with the customer's end product.



# <span id="page-5-0"></span>**2 System description**

### <span id="page-5-1"></span>**2.1 Overview**

The NEO-D9C receiver supports the QZSS L6 signals, QZSS Centimeter Level Augmentation Service (CLAS) and experimental MADOCA service. The QZSS CLAS service provides high-accuracy augmentation to GNSS receivers. The CLAS service is available over mainland Japan for free.

Combined with other products from u-blox, NEO-D9C builds a complete and stand-alone high precision system providing users with access to free high-accuracy correction services and ultimately centimeter-level GNSS accuracy.

#### <span id="page-5-2"></span>**2.1.1 QZSS L6 augmentation service**

The QZSS L6 signal is available on satellites in a Quasi-Zenith Orbit over the Asia-Pacific region and in geosynchronous orbit above Indonesia.

The QZSS L6 is a signal for augmentation corrections. It is transmitted at a frequency of 1278.75 MHz in the L6/E6 band. This signal provides two systems for corrections:

- CLAS: Centimetre Level Augmentation Service
- MADOCA: Multi-GNSS Advanced Demonstration Tool for Orbit and Clock Analysis

The CLAS service is targeted for less than 10 cm performance while MADOCA is a decimeter correction service. Both these services are SSR corrections services that provide corrections that are usable for a much larger area than what can be provided with the standard OSR corrections such as VRS.



**Figure 1: QZSS coverage area - image QZSS Japan**





#### **Figure 2: QZSS satellite orbits - image QZSS Japan**

The QZSS service transmits signals from the L5 band up to and including the L1 band.

The NEO-D9C requires the QZSS L2C signals as well as the QZSS L6 signal in order to operate. It cannot provide the L6 message data without first acquiring the QZSS L2C signal.

The antenna providing the signal to the NEO-D9C must provide coverage of the L2C band and the L6 band. Any RF circuitry on the PCB must be designed to consider this.



#### **Figure 3: QZSS satellite - image QZSS Japan**

The QZSS performance standard specification (PS-QZSS-001) and interface specification for QZSS L6 (IS-QZSS-L6-001) is available from the QZSS [http://qzss.go.jp/en/technical/ps-is-qzss/ps-is](http://qzss.go.jp/en/technical/ps-is-qzss/ps-is-qzss.html)[qzss.html.](http://qzss.go.jp/en/technical/ps-is-qzss/ps-is-qzss.html)

The MADOCA L6E message specification can be found on the GPAS [http://file.gpas.co.jp/](http://file.gpas.co.jp/L6E_MADOCA_DataFormat_E.pdf) [L6E\\_MADOCA\\_DataFormat\\_E.pdf](http://file.gpas.co.jp/L6E_MADOCA_DataFormat_E.pdf).

The subframe data for the CLAS and MADOCA service is provided in a UBX message: UBX-RXM-QZSSL6.



## <span id="page-7-0"></span>**2.2 Architecture**

The NEO-D9C receiver provides all the necessary RF and baseband processing to enable multiconstellation operation. The block diagram below shows the key functionality.

### <span id="page-7-1"></span>**2.2.1 Block diagram**



#### **Figure 4: NEO-D9C block diagram**

An active antenna is mandatory with the NEO-D9C.



# <span id="page-8-0"></span>**3 Receiver functionality**

This section describes the NEO-D9C operational features and their configuration.

## <span id="page-8-1"></span>**3.1 Receiver configuration**

u-blox positioning receivers are fully configurable with UBX protocol messages. The configuration used by the receiver during normal operation is called the "current configuration". The current configuration can be changed during normal operation by sending UBX configuration messages. On startup, the current configuration held in RAM is built from the default firmware settings plus any settings held in flash memory.

A configuration setting stored in RAM remains effective until power-down or reset. Configuration settings can be saved permanently in flash memory.

Configuration interface settings are held in a database consisting of separate configuration items. An item is made up of a pair consisting of a key ID and a value. Related items are grouped together and identified under a common group name: CFG-GROUP-\*; a convention used in u-center and within this document. Within u-center, a configuration group is identified as "Group name" and the configuration item is identified as the "item name" under the "Generation 9 Configuration View" - "Advanced Configuration" view.

The UBX messages available to change or poll the configurations are UBX-CFG-VALSET, UBX-CFG-VALGET, and UBX-CFG-VALDEL. For more information about these messages and the configuration keys, see the configuration interface section in the applicable interface description [\[2\]](#page-49-1).

#### <span id="page-8-2"></span>**3.1.1 Changing the receiver configuration**

The configuration messages UBX-CFG-VALSET, UBX-CFG-VALGET and UBX-CFG-VALDEL will result in a UBX-ACK-ACK or a UBX-ACK-NAK response.

### <span id="page-8-3"></span>**3.1.2 Default QZSS configuration**

The default QZSS configurations are:

- QZSS L2C
- QZSS L6
- The QZSS L2C reception is always enabled as it is required and is transparent to user. The QZSS L6 reception is configurable for satellite selection and L6D or L6E message selection, or it can be left in an automatic mode. However both messages can be provided simultaneously if required.

The configuration settings can be modified using UBX protocol configuration messages. For more information, see the NEO-D9C Interface description [[2](#page-49-1)].

| QZSS L2C | QZSS L6 |
|----------|---------|
| Enabled  | Enabled |

#### <span id="page-8-4"></span>**3.1.3 Default interface settings**

| Interface | Settings                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| UART      | 9600 baud, 8 bits, no parity bit, 1 stop bit.                                                                               |
|           | Output protocol: UBX. Only the following UBX message (if enabled) will be output if there is valid<br>data: UBX-RXM-QZSSL6. |
|           | Input protocols without need of additional configuration: UBX.                                                              |



| Interface | Settings                                                                    |  |
|-----------|-----------------------------------------------------------------------------|--|
| USB       | Output messages activated as in UART. Input protocols available as in UART. |  |
| I2C       | Output messages activated as in UART. Input protocols available as in UART. |  |
| SPI       | Output messages activated as in UART. Input protocols available as in UART. |  |

#### **Table 1: Default interface settings**

- The boot message is still output using \$GNTXT messages. The messages are output when the NEO-D9C is powered up.
- Refer to the applicable interface description [[2](#page-49-1)] for information about further settings.

#### <span id="page-9-0"></span>**3.1.4 Basic receiver configuration**

This section summarizes the basic receiver configuration most commonly used.

#### **3.1.4.1 Communication interface configuration**

Several configuration items allow operation mode configuration of the various communications interfaces. This includes parameters for the data framing, transfer rate and protocols used. See [Communication](#page-13-0) interfaces for details. The configuration items available for each interface are:

- UART1 interface: CFG-UART1-\*, CFG-UART1INPROT-\*, CFG-UART1OUTPROT-\*
- UART2 interface: CFG-UART2-\*, CFG-UART2INPROT-\*, CFG-UART2OUTPROT-\*
- SPI interface: CFG-SPI-\*, CFG-SPIINPROT-\*, CFG-SPIOUTPROT-\*
- I2C interface: CFG-I2C-\*, CFG-I2CINPROT-\*, CFG-I2COUTPROT-\*
- USB interface: CFG-USB-\*, CFG-USBINPROT-\*, CFG-USBOUTPROT-\*

#### **3.1.4.2 Message output configuration**

The rate of UBX protocol output messages is configurable. If the rate configuration value is zero, then the corresponding message will not be output. Values greater than zero indicate how often the message is output.

For periodic output messages the rate relates to the event the message is related to. If the rate of this message is set to one (1), it will be output for every epoch. If the rate is set to two (2), it will be output every other epoch. The rates of the output messages are individually configurable per communication interface. See the CFG-MSGOUT-\* configuration group.

Some messages, such as UBX-MON-VER, are not periodic and will only be output as the answer to a poll request.

The UBX-INF-\* information messages are non-periodic output messages that do not have a message rate configuration. Instead they can be enabled for each communication interface via the CFG-INFMSG-\* configuration group.

All message output is additionally subject to the protocol configuration of the communication interfaces. Messages of a given protocol will not be output until the protocol is enabled for output on the interface (see previous section).

#### <span id="page-9-1"></span>**3.1.5 QZSS L6 satellite and message selection**

The D9C receivers support tracking up to 6 QZSS satellites in L2 band (L2CM/L2CL) and decoding up to two L6 channels concurrently. As a result, a maximum of two QZSS L6 sat messages can be provided. These messages can be from two different QZSS L6 satellites if needed.

There is no pilot signal on the L6 band, and the tracking parameters must be obtained from the corresponding L2 signal. Therefore, the NEO-D9C needs to receive QZSS L2 signals and QZSS L6



signals in order to operate. Ensure the receiving antenna used supports L2 and L6 signals. It will first acquire the QZSS L2 signals before acquiring the QZSS L6 signals.

The L6 messages can be the L6D and the L6E message at the same time if required. The RXM-QZSSL6 message has two channels, therefore only two possible L6 message streams can be provided. If using two QZSS satellites to provide the L6 message data, only one message stream from each can be the output in the RXM-QZSSL6 message.



**Figure 5: Maximum number of QZSS sats that can be tracked**

As shown below a single QZSS satellite will provide both the L6D and L6E messages.

Satellite QZSS 1 (Block 1) only transmits the L6D message. If manually selected or automatically selected it will be possible only to decode an L6D channel message from this satellite.





#### **Figure 6: QZSS L6 single satellite messages**

Two QZSS satellites can be used as a source for either the L6D or L6E message. Only a maximum of two satellites can be used to provide the L6 messages.



#### **Figure 7: QZSS L6 double satellite messages**

The required QZSS L6 satellite ID and message can be selected using the following configuration keys:

- CFG-QZSS-L6\_SVIDA
- CFG-QZSS-L6\_SVIDB



- CFG-QZSS-L6\_MSGA
- CFG-QZSS-L6\_MSGB

There are two message channels (A-B). Each of these channels can output QZSS L6 message L6D or L6E.

By default the firmware has the SVIDA and SVIDB set to "0". The default selection for MSGA and MSGB is set to L6D message for both channels. With this selection the firmware will acquire the two strongest QZSS satellites and provide the L6D message on both channels.

If SVIDA is set to a SVID rather than the default of "0" it will acquire the SVID selected. SVIDB can remain set to "0" and will acquire the QZSS satellite with the highest C/N0.

In the UBX-RXM-QZSSL6 output message the C/N0 reported will be for the L6 signal level and not for the QZSS L2 signal level.

The NEO-D9C and ZED-F9x should be powered on at the same time to ensure the NEO-D9C receives the messages at the correct time.

In order to ensure a fast startup and reacquisition time the NEO-D9C can be aided by the ZED-F9x. This is done by inputting the following 3 UBX messages.

The three UBX messages that can be enabled on the ZED-F9x and sent into the NEO-D9C are:

- UBX-NAV-PVT
- UBX-NAV-TIMEGPS
- UBX-RXM-SFRBX

```
No other UBX/NMEA messages should be sent into the NEO-D9C.
```

If the ZED-F9x and the NEO-D9C are directly connected by UART, only the three indicated messages should be enabled on the ZED-F9x output interface. No NMEA messages should be enabled.

The USB interfaces of the ZED-F9x and NEO-D9C can be used as host interface. If the host interface is only UART1 for both units, the host application must redirect the three required messages to the NEO-D9C input.

### <span id="page-12-0"></span>**3.1.6 QZSS L6 data message output**

The L6 data is transmitted from the satellites in 250-symbol subframes with duration of 1000 ms. The subframe begins with a 4-symbol fixed preamble pattern 0x1A, 0xCF, 0xFC, 0x1D, followed by 214 data symbols and 32 Reed-Solomon parity symbols. The message structure is the same for both L6D and L6E signals.

|     | DIRECTION OF DATA FLOW FROM SATELLITE; MOST SIGNIFICANT BIT (MSB) TRANSMITTED FIRST<br>2000 BITS-1 SECOND |                                         |
|-----|-----------------------------------------------------------------------------------------------------------|-----------------------------------------|
| I50 |                                                                                                           | 1745                                    |
|     | DATA PART<br><b>1695 BITS</b>                                                                             | REED-SOLOMON<br>CODE<br><b>256 BITS</b> |

#### **Figure 8: QZSS L6 subframe**

The contents of this L6 message are explained in the IS-QZSS-L6-001 specification for the QZSS L6D/E service.

The NEO-D9C is simply a data link layer receiver for the CLAS/MADOCA correction data, and other services transmitted on the QZSS L6 band. It does not parse, assemble or post-process the



message content in any way. The only processing done on the raw subframe-level data is error detection and correction, according to the receiver's configuration.

There are three possible modes of operation:

- **1. No error detection or correction.** The data is sent out as is, framed at the QZSS L6 250-byte boundary.
- **2. Error detection only.** The data is sent out as is, but the frame is accompanied by a meta-data header indicating whether or not the message passed to the Reed-Solomon error detection.
- **3. Error detection and correction.** The received complete subframes are passed to Reed-Solomon error correction. If the data contains any errors, either preamble or payload, error recovery is attempted. If the error correction results in a frame that passes the error detection, the corrected frame is sent out accompanied with a meta-data header indicating how many bytes were corrected. This includes the preamble bytes. Hence, the maximum number of correctable errors is 20 (up to 4 errors in the preamble and up to 16 in the payload in the Reed-Solomon). If the error correction fails, the received data is sent out as is (without applying any correction attempts, including the preamble) and the frame is marked as erroneous.

The NEO-D9C will output the raw QZSS L6 data messages in the UBX-RXM-QZSSL6 message. This message can contain both the L6D and L6E service data if required.

## <span id="page-13-0"></span>**3.2 Communication interfaces**

u-blox receivers are equipped with a communication interface which is multi-protocol capable. The interface ports can be used to transmit GNSS measurements, monitor status information and configure the receiver.

A protocol (e.g. UBX, NMEA) can be assigned to several ports simultaneously, each configured with individual settings (e.g. baud rate, message rates, etc.). More than one protocol (e.g. UBX protocol and NMEA) can be assigned to a single port (multi-protocol capability), which is particularly useful for debugging purposes.

The NEO-D9C provides UART1, UART2, SPI, I2C and USB interfaces for communication with a host CPU. The interfaces are configured via the configuration methods described in the applicable interface description [\[2\]](#page-49-1).

| Port no. | UBX-MON-COMMS portId | Electrical interface |
|----------|----------------------|----------------------|
| 0        | 0x0000               | I2C                  |
| 1        | 0x0100               | UART1                |
| 2        | 0x0200               | UART2                |
| 3        | 0x0300               | USB                  |
| 4        | 0x0400               | SPI                  |
|          |                      |                      |

The following table shows the port numbers reported in the UBX-MON-COMMS messages.

**Table 2: Port number assignment**

It is important to isolate interface pins when VCC is removed. They can be allowed to float or be connected to a high impedance (Float or tri-state: Hi-Z state). Open collector circuits powered by module VCC are also suitable. They must be powered by module VCC to ensure correct pin state when module VCC is removed.

Example isolation circuit is shown below.





**Figure 9: NEO-D9C output isolation**



**Figure 10: NEO-D9C input isolation**

### <span id="page-14-0"></span>**3.2.1 UART**

A Universal Asynchronous Receiver/Transmitter (UART) port consists of an RX and a TX line. Neither handshaking signals nor hardware flow control signals are available. The UART interface protocol and baud rate can be configured but there is no support for setting different baud rates for reception and transmission.

The NEO-D9C includes two UART serial ports. UART1 can be used as a host interface for configuration, monitoring and control.

- UART2 may be used to provide correction data directly to a high precision GNSS receiver from the u-blox F9 platform. To check whether a specific u-blox F9 product supports correction data output by the NEO-D9C, refer to its Integration manual.
- The UART RX interface will be disabled when more than 100 frame errors are detected during a one-second period. This can happen if the wrong baud rate is used or the UART RX pin is grounded. An error message appears when the UART RX interface is re-enabled at the end of the one-second period.

| Baud rate | Data bits | Parity | Stop bits |  |
|-----------|-----------|--------|-----------|--|
| 9600      | 8         | none   | 1         |  |
| 19200     | 8         | none   | 1         |  |
| 38400     | 8         | none   | 1         |  |



| Baud rate | Data bits | Parity | Stop bits |
|-----------|-----------|--------|-----------|
| 57600     | 8         | none   | 1         |
| 115200    | 8         | none   | 1         |
| 230400    | 8         | none   | 1         |
| 460800    | 8         | none   | 1         |
| 921600    | 8         | none   | 1         |

**Table 3: Possible UART interface configurations**

Allow a short time delay of typically 100 ms between sending a baud rate change message and providing input data at the new rate. Otherwise some input characters may be ignored or the port could be disabled until the interface is able to process the new baud rate.

Note that for protocols such as UBX, it does not make sense to change the default word length values (data bits) since these properties are defined by the protocol and not by the electrical interface.

If the amount of data configured is too much for a certain port's bandwidth (e.g. all UBX messages output on a UART port with a baud rate of 9600), the buffer will fill up. Once the buffer space is exceeded, new messages to be sent will be dropped. To prevent message loss, the baud rate and communication speed or the number of enabled messages should be carefully selected so that the expected number of bytes can be transmitted in less than one second.

#### <span id="page-15-0"></span>**3.2.2 I2C interface**

An I2C interface is available for communication with an external host CPU or u-blox cellular modules. The interface can be operated in slave mode only. The I2C protocol and electrical interface are fully compatible with Fast-mode of the I2C industry standard. Since the maximum SCL clock frequency is 400 kHz, the maximum transfer rate is 400 kb/s. The SCL and SDA pins have internal pull-up resistors which should be sufficient for most applications. However, depending on the speed of the host and the load on the I2C lines additional external pull-up resistors may be necessary.

- To use the I2C interface D\_SEL pin must be left open.
- In designs where the host uses the same I2C bus to communicate with more than one ublox receiver, the I2C slave address for each receiver must be configured to a different value. Typically most u-blox receivers are configured to the same default I2C slave address value. To poll or set the I2C slave address, use the CFG-I2C-ADDRESS configuration item (see the applicable interface description [\[2\]](#page-49-1)).

The CFG-I2C-ADDRESS configuration item is an 8-bit value containing the I2C slave address in 7 most significant bits, and the read/write flag in the least significant bit.

#### **3.2.2.1 I2C register layout**

The I2C interface allows 256 registers to be addressed. As shown in [Figure](#page-16-0) 11, only three of these are currently implemented.

The data registers 0 to 252 at addresses 0x00 to 0xFC contain reserved information, the result from their reading is currently undefined. The data registers 0 to 252 are 1 byte wide.

At addresses 0xFD and 0xFE it is possible to read the currently available number of bytes.

The register at address 0xFF allows the data stream to be read. If there is no data awaiting transmission from the receiver, then this register delivers value 0xFF, which cannot be the first byte of a valid message. If the message data is ready for transmission, the successive reads of register 0xFF will deliver the waiting message data.



#### Do not use registers 0x00 to 0xFC. They are reserved for future use and they do not currently provide any meaningful data.

<span id="page-16-0"></span>

#### **Figure 11: I2C register layout**

#### **3.2.2.2 Read access types**

There are two I2C read transfer forms:

- The "random access" form: includes a slave register address and allows any register to be read.
- The "current address" form: omits the register address.

[Figure](#page-17-0) 12 shows the format of the first one, the "random access" form of the request. Following the start condition from the master, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the master transmitter. The receiver answers with an acknowledge (logic low) to indicate that it recognizes the address.

Next, the 8-bit address of the register to be read must be written to the bus. Following the receiver's acknowledgment, the master again triggers a start condition and writes the device address, but this time the RW bit is a logic high to initiate the read access. Now, the master can read 1 to N bytes from the receiver, generating a not-acknowledge and a stop condition after the last byte being read.



<span id="page-17-0"></span>

**Figure 12: I2C random read access**

If the second form, "current address" is used, an address pointer in the receiver is used to determine which register to read. This address pointer will increment after each read unless it is already pointing at register 0xFF, the highest addressable register, in which case it remains unaltered.

The initial value of this address pointer at startup is 0xFF, so by default all current address reads will repeatedly read register 0xFF and receive the next byte of message data (or 0xFF if no message data is waiting).



**Figure 13: I2C current address read access**

#### **3.2.2.3 Write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. Therefore, the register set mentioned in the section Read [access](#page-18-1) is not writeable.

Following the start condition from the master, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the master transmitter. The receiver answers with an acknowledge (logic low) to indicate that it is responsible for the given address.

The master can write 2 to N bytes to the receiver, generating a stop condition after the last byte being written. The number of data bytes must be at least 2 to properly distinguish from the write access to set the address counter in random read accesses.







#### <span id="page-18-0"></span>**3.2.3 SPI interface**

NEO-D9C has an SPI slave interface that can be selected by setting D\_SEL = 0. The SPI slave interface is shared with UART1 and I2C port, the physical pins are same. The SPI pins available are:

- SPI\_MISO (TXD)
- SPI\_MOSI (RXD)
- SPI\_CS\_N
- SPI\_CLK

See more information about communication interface selection from the [D\\_SEL](#page-20-1) section.

The SPI interface is designed to allow communication to a host CPU. The interface can be operated in slave mode only.

#### <span id="page-18-1"></span>**3.2.3.1 Read access**

As the register mode is not implemented for the SPI port, only the UBX/NMEA message stream is provided. This stream is accessed using the back-to-back read and write access (see section [Back](#page-18-2)[to-back](#page-18-2) read and write access below). When no data is available to be written to the receiver, MOSI should be held logic high, i.e. all bytes written to the receiver are set to 0xFF.

To prevent the receiver from being busy parsing incoming data, the parsing process is stopped after 50subsequent bytes containing0xFF.The parsing process is re-enabled with thefirst byte not equal to 0xFF.

If the receiver has no more data to send, it sets MISO to logic high, i.e. all bytes transmitted decode to 0xFF. An efficient parser in the host will ignore all 0xFF bytes which are not part of a message and will resume data processing as soon as the first byte not equal to 0xFF is received.

#### <span id="page-18-2"></span>**3.2.3.2 Back-to-back read and write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. For every byte written to the receiver, a byte will simultaneously be read from the receiver.While the master writes to MOSI, at the same time it needs to read from MISO, as any pending data will be output by the receiver with this access. The data on MISO represents the results from a current address read, returning 0xFF when no more data is available.





**Figure 15: SPI back-to-back read/write access**

#### <span id="page-19-0"></span>**3.2.4 USB interface**

A single USB port is provided for host communication purposes.

The USB 2.0 FS (Full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface.

If the receiver executes code from internal ROM (i.e. when a valid flash firmware image is not detected), the USB behavior can differ compared to executing a firmware image from flash memory. USB host compatibility testing is thus recommended in this scenario.

The NEO-D9C receiver supports only self-powered mode operation in which the receiver is supplied from its own power supply. The V\_USB pin is used to detect the availability of the USB port, i.e. whether the receiver is connected to a USB host.

- USB suspend mode is not supported.
- USB bus-powered mode is not supported.
- It is important to connect V\_USB to ground and leave data lines open when the USB interface is not used in an application.
- The voltage range for V\_USB is specified from 3.0 V to 3.6 V, which differs slightly from the specification for VCC.
- The boot screen is retransmitted on the USB port after enumeration. However, messages generated between receiver startup and USB enumeration are not visible on the USB port.

There are additional hardware requirements if USB is used:

- V\_USB (pin 7) requires 1 uF capacitor mounted adjacent to the pin to ensure correct V\_USB voltage detection
- The V\_USB (Pin 7) voltage should be sourced from an LDO enabled by the module VCC and supplied from the USB host.
- A pull-down resistor is required on the output of this V\_USB LDO
- Pin 5 is USB\_DM. Pin 6 is USB\_DP.
- Apply USB\_DM and USB\_DP series resistors; typically 27 Ω





**Figure 16: NEO-D9C example circuit for USB interface**

R11 = 100 k Ω is recommended

R12, R13 = 27 Ω is recommended

### <span id="page-20-0"></span>**3.3 Predefined PIOs**

In addition to the communication ports, there are some predefined PIOs provided by NEO-D9C to interact with the receiver. These PIOs are described in this section.

If hardware backup mode is used a proper isolation of the interfaces is needed.

#### <span id="page-20-1"></span>**3.3.1 D\_SEL**

The D\_SEL pin can be used to configure the functionality of the combined UART1, I2C, and SPI pins. It is possible to configure the pins as UART1 + I2C, or as SPI. SPI is not available unless D\_SEL pin is set to low. See [Table](#page-20-4) 4 below.

<span id="page-20-4"></span>

| Pin no. | D_SEL == 0 | D_SEL == 1 |
|---------|------------|------------|
| 20      | SPI_MISO   | UART1 TXD  |
| 21      | SPI_MOSI   | UART1 RXD  |
| 18      | SPI_CS_N   | I2C SDA    |
| 19      | SPI_CLK    | I2C SCL    |

**Table 4: D\_SEL configuration**

#### <span id="page-20-2"></span>**3.3.2 RESET\_N**

The NEO-D9C provides the ability to reset the receiver. The RESET\_N pin is an input-only pin with an internal pull-up resistor. Driving RESET\_N low for at least 100 ms will trigger a cold start.

The RESET\_N pin will delete all information and trigger a cold start. It should only be used as a recovery option.

#### <span id="page-20-3"></span>**3.3.3 SAFEBOOT\_N**

The NEO-D9C provides a SAFEBOOT\_N pin that is used to command the receiver safeboot mode.

If this pin is low at power up, the receiver starts in safeboot mode and operation is disabled.

The safeboot mode can be used to recover from situations where the flash content has become corrupted and needs to be restored.

In safeboot mode the receiver runs from a passive oscillator circuit with less accurate timing and hence the receiver is unable to communicate via USB.



In this mode only UART1 communication is possible. For communication via UART1 in safeboot mode, the host must send a training sequence (0x55 0x55 at 9600 baud) to the receiver in order to begin communication. After this the host must wait at least 2 ms before sending any data.

It is recommended to have the possibility to pull the SAFEBOOT\_N pin low in the application. This can be provided using an externally connected test point or a host I/O port.

#### <span id="page-21-0"></span>**3.3.4 Extended TX timeout**

If the host does not communicate over SPI or I2C for more than approximately 2 seconds, the device assumes that the host is no longer using this interface and no more packets are scheduled for this port. This mechanism can be changed by enabling "extended TX timeouts", in which case the receiver delays idling the port until the allocated and undelivered bytes for this port reach 4 kB. This feature is especially useful when using the TX-READY feature with a message output rate of less than once per second, and polling data only when data is available, determined by the TX\_READY pin becoming active.

### <span id="page-21-1"></span>**3.4 Security**

#### <span id="page-21-2"></span>**3.4.1 Receiver status monitoring**

Messages in the UBX class UBX-MON are used to report the status of the parts of the embedded computer system that are not related to the received satellite system specific info.

The main purposes are:

• Hardware and software versions, using UBX-MON-VER.

### <span id="page-21-3"></span>**3.5 Forcing a receiver reset**

The NEO-D9C is not a GNSS receiver and does not operate to the same principles as a standard GNSS. However it does support the standard UBX-CFG-RST command.

Data stored in flash memory is not cleared by any of the options provided by UBX-CFG-RST.

The resetMode must be specified. This is not related to QZSS, but to the way the software restarts the system.

- **Hardware reset (watchdog), immediately** uses the on-chip watchdog, in order to electrically reset the chip. This is an immediate, asynchronous reset. No Stop events are generated.
- **Controlled software reset** terminates all running processes in an orderly manner and, once the system is idle, restarts operation, reloads its configuration and starts to acquire and track QZSS satellites.
- **Hardware reset (watchdog), after shutdown** uses the on-chip watchdog, in order to electrically reset the chip after shutdown.

### <span id="page-21-4"></span>**3.6 Firmware upload**

NEO-D9C is supplied with firmware. u-blox may release updated images containing, for example, security fixes, enhancements, bug fixes, etc. Therefore it is important that customers implement a firmware update mechanism in their system.

A firmware image is a binary file containing the software to be run by the GNSS receiver. A firmware update is the process of transferring a firmware image to the receiver and storing it in non-volatile flash memory.



Contact u-blox for more information on firmware update.



# <span id="page-23-0"></span>**4 Design**

This section provides information to help carry out a successful schematic and PCB design integrating the NEO-D9C.

### <span id="page-23-1"></span>**4.1 Pin assignment**

The pin assignment of the NEO-D9C module is shown in [Figure](#page-23-2) 17. The defined configuration of the PIOs is listed in [Table](#page-23-3) 5.



V\_BCKP functionality (pin 22: Reserved), ANT\_OFF, ANT\_DETECT, ANT\_SHORT\_N are not available.

<span id="page-23-2"></span>

#### **Figure 17: NEO-D9C pin assignment**

<span id="page-23-3"></span>

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



| Pin no. | Name           | I/O | Description                                                       |
|---------|----------------|-----|-------------------------------------------------------------------|
| 12      | GND            | I   | Ground                                                            |
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

**Table 5: NEO-D9C pin assignment**

### <span id="page-24-0"></span>**4.2 Antenna**

An active antenna NEO-D9C is mandatory for operation.

The NEO-D9C needs to receive L2 and L6 signals in order to operate. A combined L1/L2/L6 active antenna is recommended if used with a ZED-F9x.

If a combined L1/L2/L6 active antenna needs to be implemented in an application case, it is recommended that an OEM active antenna module is used that meets our specification. It is not a simple task to implement the required RF circuitry. Sourcing the required components to meet the RTK group delay specification is not a simple process compared to previous L1 only implementations.

- A suitable ground plane is required for the antenna to achieve good performance if a combined L1/L2/L6 antenna is used.
- Location of the antenna is critical for reaching good performance. Even more so if a combined L1/L2/L6 for RTK is used. The application requirements make it unsuitable for under vehicle dash location or rear view mirror location, etc.



**Figure 18: NEO-D9C required signals**





**Figure 19: Typical combined L1 + L2/E5b + L6 active antenna structure**



#### **Figure 20: Typical combined NEO-D9C and ZED-F9x combined RF front end and system**

- UART2 may be used to provide correction data directly to a high precision GNSS receiver from the u-blox F9 platform. To check whether a specific u-blox F9 product supports correction data output by the NEO-D9C, refer to its Integration manual.
- An active antenna is required to provide sufficient low noise gain and ensure any cable loss does not inpact the antenna noise figure.

The complexity and type of RF components of this front end will be dependent on the end requirements such as Automotive for example. A relatively high LNA gain provided from the active antenna will make the RF front end design simpler.

#### **Combined L1 + L2/E5b + L6 active antenna required specifications**

| Parameter    | Specification  |
|--------------|----------------|
| Antenna type | Active antenna |



| Parameter                          | Specification                                                                         |        |
|------------------------------------|---------------------------------------------------------------------------------------|--------|
|                                    | Typical gain                                                                          | 30 dB1 |
| Active antenna recommendations     | Maximum gain                                                                          | 50 dB  |
|                                    | Maximum typical noise figure                                                          | 4 dB   |
| L1 band antenna gain               | 1559 - 1606 MHz: 3 dBic typ.                                                          |        |
| 2<br>L2/E5b/L6 band antenna gain   | 1197 - 1285 MHz: 2 dBic typ.                                                          |        |
| Polarization                       | RHCP                                                                                  |        |
| Axial ratio                        | 2 dB max at zenith                                                                    |        |
| Phase center variation             | <10 mm over elevation/azimuth                                                         |        |
| 3<br>Group delay variation in-band | 10 ns max at each GNSS system bandwidth. Note:<br>Inter-signal requirement 50 ns max. |        |
| 4<br>EMI immunity out-of-band      | 30 V/m                                                                                |        |
| 3 Rejection<br>Out-of-band         | 40 dB typ                                                                             |        |
| ESD circuit protection             | 15 kV human body model air discharge                                                  |        |

**Table 6: Antenna specifications for NEO-D9C modules**

The antenna system should include filtering to ensure adequate protection from nearby transmitters. Care should be taken in the selection of antennas placed close to cellular or Wi-Fi transmitting antennas.

#### <span id="page-26-0"></span>**4.2.1 Antenna bias**

Active antennas have an integrated low-noise amplifier that contributes an additional current of typically 5 to 20 mA to the system's power consumption budget.

If the supply voltage of the NEO-D9C module matches the supply voltage of the antenna (e.g. 3.0 V), you can use the filtered supply voltage VCC\_RF output to supply the antenna. However a current limiting resistor is required to prevent against short circuits destroying the bias-t inductor.

The bias-t inductor must be chosen for multi-band operation, a value of 47 nH ±5% is recommended for the recommended Murata L part. It has a self-resonance frequency of 1 GHz and a high impedance (> 500 Ω) at L-band frequencies.

The recommended bias-t inductor (Murata LQG15HS47NJ02) has a maximum current capacity of 300 mA. Hence the current is limited to 70 mA at 3.3V using an active limiter in the recommended circuit shown in [Figure](#page-27-0) 22 below. A 10 Ω resistor (R2)is provided to measure the current.This resistor power rating must be chosen to ensure reliability in the chosen circuit design.

<span id="page-26-1"></span><sup>1</sup> LNA gain, no cable loss or signal divider loss. 20 dB at module RF\_IN.

<span id="page-26-2"></span><sup>2</sup> Measured with a ground plane d=150 mm

<span id="page-26-3"></span><sup>3</sup> GNSS system bandwidths: 1559… 1563 MHz; 1573… 1578 MHz; 1598… 1606 MHz; 1192… 1212 MHz; 1197… 1217 MHz; 1223… 1231 MHz; 1242… 1249 MHz

<span id="page-26-4"></span><sup>4</sup> Exception L1 and L2 bands +/- 200 MHz, emphasis on cellular bands





#### **Figure 21: NEO-D9C antenna bias inductor impedance**

A recommended circuit design for an active antenna bias is shown below. This example shows an external voltage of 3.3 V with current limiting as described above. An ESD protection diode should also be connected to the input as shown.

<span id="page-27-0"></span>

#### **Figure 22: NEO-D9C reference design for antenna bias**

- L1: Murata LQG15HS47NJ02 0402 47 N 5% 0.30 A -55/+125 C
- D1: TYCO, 0.25PF, PESD0402-140 -55/+125C

#### C3: Murata GRM155R61A104KA01 CER X5R 0402 100N 10% 10V

R2: RES THICK FILM CHIP 1206 10R 5% 0.25W



It is recommended to use active current limiting. If active current limiting is not used, the important points covered below need to be taken into account:



#### **Figure 23: NEO-D9C VCC\_RF antenna bias**

The bias-t inductor and current limiting resistor must be selected to be reliable with a short circuit on the antenna feed if no active current limiter is used. Our recommended part has a limit of 300 mA. A part with a higher current capability will be needed if the short circuit current is as described here. This will also be affected by the voltage level of the antenna bias supply due to power dissipation. Take the current limit capability of the antenna bias supply into consideration. In the case where the module supplies the voltage via VCC\_RF, a higher value resistor will be needed to ensure the module supply inductor is protected. The current should be limited to below 150 mA at the module supply voltage under short circuit conditions. In this case a value of 17 Ω or more is required at a module supply of 3 V to limit short circuit current to 150 mA. The DC resistance of the bias-t inductor is assumed to be 1-2 Ω and the module internal feed inductor is assumed to be 1.2 Ω.

If the VCC\_RF voltage does not match with the supply voltage of the active antenna, use a filtered external supply.

The power dissipation in the resistor and inductor needs to be taken into account based on the supply voltage and short circuit current. The bias-t inductor current capability and the bias resistor value need to be calculated as shown above. The supply voltage for the bias-t and its current capability is part of the calculation.



#### **Figure 24: NEO-D9C external voltage antenna bias**



### <span id="page-29-0"></span>**4.3 Power supply**

The u-blox NEO-D9C module has two power supply pins: VCC and V\_USB.

#### <span id="page-29-1"></span>**4.3.1 VCC: Main supply voltage**

The **VCC** pin is connected to the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude. For this reason, it is important that the supply circuitry be able to support the peak power for a short time (see the applicable data sheet [\[1](#page-49-2)] for specification).

- To reduce peak current during power on, users can employ an LDO that has a built-in current limiter.
- Do not add any series resistance greater than 0.2 Ω to the VCC supply as it will generate input voltage noise due to dynamic current conditions.
- For the NEO-D9C module the equipment must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1.

#### <span id="page-29-2"></span>**4.3.2 NEO-D9C power supply**

The NEO-D9C requires a low-noise, low-dropout voltage, and a very low source impedance power supply of 3.3 V typically. No inductors or ferrite beads should be used from LDO to the module VCC pin. The peak currents need to be taken into account for the source supplying the LDO for the module.

A power supply fed by 5 V is shown in the figure below. This example circuit is intended only for the module supply.



**Figure 25: NEO-D9C power supply**

### <span id="page-29-3"></span>**4.4 NEO-D9C minimal design**

The minimal electrical circuit for NEO-D9C operation using the UART1 interface is shown below:





**Figure 26: Minimal NEO-D9C design**

It is important to connect V\_USB to ground if USB is not used.

UART2 may be used to provide correction data directly to a high precision GNSS receiver from the u-blox F9 platform. To check whether a specific u-blox F9 product supports correction data output by the NEO-D9S, refer to its Integration manual.

### <span id="page-30-0"></span>**4.5 EOS/ESD precautions**

- To avoid overstress damage during production or in the field it is essential to observe strict EOS/ESD/EMI handling and protection measures.
- To prevent overstress damage at the RF\_IN of your receiver, never exceed the maximum input power as specified in the applicable data sheet [\[1\]](#page-49-2).

When integrating receivers into wireless systems, pay special attention to electromagnetic and voltage susceptibility issues. Wireless systems include components which can produce Electrostatic Discharge (ESD), Electrical Overstress (EOS) and Electro-Magnetic Interference (EMI). CMOS devices are more sensitive to such influences because their failure mechanism is defined by the applied voltage, whereas bipolar semiconductors are more susceptible to thermal overstress. The following design guidelines help in designing robust yet cost-effective solutions.

#### <span id="page-30-1"></span>**4.5.1 ESD protection measures**

receivers are sensitive to Electrostatic Discharge (ESD). Special precautions are required when handling. Most defects caused by ESD can be prevented by following strict ESD protection rules for production and handling. When implementing passive antenna patches or external antenna connection points, then additional ESD measures as shown in the figure below can also avoid failures in the field.





**Figure 27: RF ESD precautions**

#### <span id="page-31-0"></span>**4.5.2 EOS precautions**

Electrical overstress (EOS) usually describes situations when the maximum input power exceeds the maximum specified ratings. EOS failure can happen if RF emitters are close to a receiver or its antenna. EOS causes damage to the chip structures. If the RF\_IN is damaged by EOS, it is hard to determine whether the chip structures have been damaged by ESD or EOS.

EOS protection measures as shown in the figure below are recommended for any designs combining wireless communication transceivers (e.g. GSM, GPRS) and in the same design or in close proximity.



**Figure 28: Active antenna EOS protection**

#### <span id="page-31-1"></span>**4.5.3 Safety precautions**

The NEO-D9C must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1. In addition to external limited power source, only Separated or Safety Extra-Low Voltage (SELV) circuits are to be connected to the module including interfaces and antennas.

For more information about SELV circuits see section 2.2 in Safety standard IEC 60950-1.

### <span id="page-31-2"></span>**4.6 Electromagnetic interference on I/O lines**

Any I/O signal line with a length greater than approximately 3 mm can act as an antenna and may pick up arbitrary RF signals transferring them as noise into the receiver. This specifically applies to unshielded lines, in which the corresponding GND layer is remote or missing entirely, and lines close to the edges of the printed circuit board.

If, for example, a cellular signal radiates into an unshielded high-impedance line, it is possible to generate noise in the order of volts and not only distort receiver operation but also damage it permanently. Another type of interference can be caused by noise generated at the PIO pins that



emits from unshielded I/O lines. Receiver performance may be degraded when this noise is coupled into the antenna.

EMI protection measures are particularly useful when RF emitting devices are placed next to the receiver and/or to minimize the risk of EMI degradation due to self-jamming. An adequate layout with a robust grounding concept is essential in order to protect against EMI.

Intended Use: In order to mitigate any performance degradation of a radio equipment under EMC disturbance, system integration shall adopt appropriate EMC design practice and not contain cables over three meters on signal and supply ports.

#### <span id="page-32-0"></span>**4.6.1 General notes on interference issues**

Received signal power at the antenna is very low. At the nominal received signal strength (-128 dBm) it is below the thermal noise floor of -111 dBm. Due to this fact, a receiver is susceptible to interference from nearby RF sources of any kind. Two cases can be distinguished:

- Out-of-band interference: Typically any kind of wireless communications system (e.g. LTE, GSM, CDMA, 3G, WLAN, Bluetooth, etc.) may emit its specified maximum transmit power in close proximity to the receiving antenna, especially if such a system is integrated with the receiver. Even at reasonable antenna selectivity, destructive power levels may reach the RF input of the receiver. Also, larger signal interferers may generate intermodulation products inside the receiver front-end that fall into the band and contribute to in-band interference.
- In-band interference: Although the band is kept free from intentional RF signal sources by radio-communications standards, many devices emit RF power into the band at levels much higher than the signal itself. One reason is that the frequency band above 1 GHz is not well regulated with regards to EMI, and even if permitted, signal levels are much higher than signal power. Notably, all types of digital equipment, such as PCs, digital cameras, LCD screens, etc. tend to emit a broad frequency spectrum up to several GHz of frequency. Also wireless transmitters may generate spurious emissions that fall into band.

As an example, GSM uses power levels of up to 2 W (+33 dBm). The absolute maximum power input at the RF input of the receiver can be +15 dBm. The GSM specification allows spurious emissions for GSM transmitters of up to +36 dBm, while the signal is less than -128 dBm. By simply comparing these numbers it is obvious that interference issues must be seriously considered in any design of a receiver. Different design goals may be achieved through different implementations:

- The primary focus is to prevent damaging the receiver from large input signals. Here the performance under interference conditions is not important and suppression of the signal is permitted. It is sufficient to just observe the maximum RF power ratings of all of the components in the RF input path.
- performance must be guaranteed even under interference conditions. In such a case, not only the maximum power ratings of the components in the receiver RF path must be observed. Further, non-linear effects like gain compression, NF degradation (desensitization) and intermodulation must be analyzed.
- Pulsed interference with a low-duty cycle such as GSM may be destructive due to the high peak power levels.

#### <span id="page-32-1"></span>**4.6.2 In-band interference mitigation**

With in-band interference, the signal frequency is very close to the frequency. Such interference signals are typically caused by harmonics from displays, micro-controller operation, bus systems, etc. Measures against in-band interference include:

- Maintaining a good grounding concept in the design
- Shielding



- Layout optimization
- Low-pass filtering of noise sources, e.g. digital signal lines
- Remote placement of the antenna, far away from noise sources
- Adding an LTE, CDMA, GSM, WCDMA, BT band-pass filter before antenna

#### <span id="page-33-0"></span>**4.6.3 Out-of-band interference**

Out-of-band interference is caused by signal frequencies that are different from the carrier frequency. The main sources are wireless communication systems such as LTE, GSM, CDMA, WCDMA, Wi-Fi, BT, etc.

Measures against out-of-band interference include maintaining a good grounding concept in the design and adding a band-pass filter into the antenna input line to the receiver.

For GSM applications, such as typical handset design, an isolation of approximately 20 dB can be reached with careful placement of the antennas. If this is insufficient, an additional SAW filter is required on the receiver input to block the remaining GSM transmitter energy.

### <span id="page-33-1"></span>**4.7 Layout**

This section details layout and placement requirements of the NEO-D9C QZSS correction service receiver.

#### <span id="page-33-2"></span>**4.7.1 Placement**

signals at the surface of the Earth are below the thermal noise floor. A very important factor in achieving maximum GNSS performance is the placement of the receiver on the PCB. The placement used may affect RF signal loss from antenna to receiver input and enable interference into the sensitive parts of the receiver chain, including the antenna itself. When defining a GNSS receiver layout, the placement of the antenna with respect to the receiver, as well as grounding, shielding and interference from other digital devices are crucial issues and need to be considered very carefully.

Signal loss on the RF connection from antenna to receiver input must be minimized as much as possible. Hence, the connection to the antenna must be kept as short as possible.

Ensure that RF critical circuits are clearly separated from any other digital circuits on the system board. To achieve this, position the receiver digital part closer to the digital section of the system PCB and have the RF section and antenna placed as far as possible away from the other digital circuits on the board.

A proper GND concept shall be followed: The RF section shall not be subject to noisy digital supply currents running through its GND plane.

#### <span id="page-33-3"></span>**4.7.2 Thermal management**

During design-in do not place the receiver near sources of heating or cooling. The receiver oscillator is sensitive to sudden changes in ambient temperature which can adversely impact satellite signal tracking. Sources can include co-located power devices, cooling fans or thermal conduction via the PCB. Take into account the following questions when designing in the receiver.

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?



High temperature drift and air vents can affect the GNSS performance. For best performance, avoid high temperature drift and air vents near the receiver.

#### <span id="page-34-0"></span>**4.7.3 Package footprint, copper and paste mask**

Copper and solder mask dimensioning recommendations for the NEO-D9C module packages are provided in this section.

- The module edge pads are 0.8 mm x 0.9 mm. Implement a pad size on your PCB as a copper pad size of 0.8 mm x 1.8 mm. Solder mask for the same pad is 0.9 mm x 1.9 mm. Paste mask for the same pad is 0.8 mm x 2.1 mm.
- These are recommendations only and not specifications. Consider the paste mask outline when defining the minimal distance to the next component. The exact copper, solder and paste mask geometries, distances, stencil thickness and solder paste volumes must be adapted to the specific production processes (e.g. soldering etc.) of the customer.

Refer to the NEO-D9C data sheet [[1](#page-49-2)] for the mechanical specification.



#### **4.7.3.1 Footprint**

**Figure 29: NEO-D9C suggested footprint (i.e. copper mask)**



#### **4.7.3.2 Paste mask**



#### **Figure 30: NEO-D9C suggested paste mask**

To improve the wetting of the half vias, reduce the amount of solder paste under the module and increase the volume outside of the module by defining the dimensions of the paste mask to form a T-shape (or equivalent) extending beyond the copper mask.

#### <span id="page-35-0"></span>**4.7.4 Layout guidance**

The presented layout guidance reduces the risk of performance issues at design level.

#### **4.7.4.1 RF In trace**

The RF In trace has to work in the combined QZSS L2 + L6 signal band.

For FR-4 PCB material with a dielectric permittivity of for example 4.7, the trace width for the 50 Ω line impedance can be calculated.



#### **Figure 31: Microstrip trace width**

A grounded co-planar RF trace is recommended as it provides the maximum shielding from noise with adequate vias to the ground layer.





**Figure 32: Grounded co-planar RF trace**

The RF trace must be shielded by vias to ground along the entire length of the trace and the NEO-D9C RF\_IN pad should be surrounded by vias as shown in the figure below.



**Figure 33: RF input trace**

The RF\_IN trace on the top layer should be referenced to a suitable ground layer.



#### **4.7.4.2 VCC pad**

The VCC pad for the NEO-D9C QZSS correction service receiver needs to have as low an impedance as possible with large vias to the lower power layer of the PCB. The VCC pad needs a large pad and the decoupling capacitor must be placed as close as possible. This is shown in the figure below.



**Figure 34: VCC pad**

## <span id="page-37-0"></span>**4.8 Design guidance**

#### <span id="page-37-1"></span>**4.8.1 General considerations**

Check power supply requirements and schematic:

- Is the power supply voltage within the specified range and noise-free?
- If USB is not used, connect the V\_USB pin to ground.
- It is recommended to have a separate LDO for V\_USB that is enabled by the module VCC. This is to comply with the USB self-powered specification.
- If USB is used, is there a 1 uF capacitor right near the V\_USB pin? This is just for the V\_USB pin.
- Is there a 1 uF cap right next to the module VCC pin?
- Compare the peak current consumption of the NEO-D9C module with the specification of your power supply.
- receivers require a stable power supply. Avoid series resistance (less than 0.2 Ω) in your power supply line (the line to VCC) to minimize the voltage ripple on VCC. See the NEO-D9C [Power](#page-29-0) [supply](#page-29-0) section in the [Design](#page-23-0) chapter for more information on the power supply requirements.
- All I/O (including UART) must not be pulled high before power ON.
- Any pull ups must be tied to module VCC to ensure they are at the correct state on power ON and OFF.
- Allow all I/O to Float/High impedance (High-Z) when VCC is not applied.

#### <span id="page-37-2"></span>**4.8.2 RF front-end circuit options**

It is mandatory that the RF input is fed by an active antenna meeting the requirements for the NEO-D9C.

The first stages of the signal processing chain are crucial to the overall receiver performance.

When an RF input connector is employed this can provide a conduction path for harmful or destructive electrical signals. If this is a likely factor the RF input should be protected accordingly.

#### **Additional points on the RF input**

- What is the expected quality of the signal source (antenna)?
- What is the external active antenna signal power?
- What is the bandwidth and filtering of the external active antenna?

• Do the combined L1/L2/L6 external antenna and filtering components meet the group delay variation requirements? This is critical for RTK. Any implementation of a PCB mounted L1/L2/ L6 patch antenna and the required RF components should not be attempted without explicit assistance of an antenna manufacturer who has experience in achieving the required group delay variation and bandwidth performance for RTK. u-blox does not have a reference design or recommended components list to achieve this.

Are destructive RF power levels expected to reach the RF input? Is interference from wireless transmitters expected?

- What are the characteristics of these signals (duty cycle, frequency range, power range, spectral purity)?
- What is the expected performance under interference conditions?

Is there a risk of RF input exposure to excessive ESD stress?

- In the field: Can the user access the antenna connector?
- PCB / system assembly: Is there risk that statically charged parts (e.g. patch antennas) may be discharged through the RF input?

The following subsections provide several options addressing the various questions above:

- In some applications, such as cellular transceivers, interference signals may exceed the maximum power rating of the RF\_IN input. To avoid device destruction use of external input protection is mandatory.
- During assembly of end-user devices which contain passive patch antennas, an ESD discharge may occur during production when pre-charged antennas are soldered to the receiver board. In such cases, use of external protection in front of RF\_IN is mandatory to avoid device destruction.

ESD discharge cannot be avoided during assembly and / or field use. Note that SAW filters are susceptible to ESD damage. To provide additional robustness an ESD protection diode may be placed at the antenna RF connector to GND.

### <span id="page-38-0"></span>**4.8.3 Antenna/RF input**

Check RF input requirements and schematic:

- With the NEO-D9C module, an active antenna meeting our antenna requirements is mandatory to achieve the performance values as written in the NEO-D9C data sheet and with a minimum gain of 20 dB being reached at the module RF\_IN pin.
- Implementing your own antenna design with a suitable antenna element (stacked patch or helix) and the required RF components is complex and should not be carried out unless under the strict guidance of the antenna supplier to meet our requirements. The risk in not meeting the required RTK performance is a factor.
- An OEM active antenna module that meets our requirements should be used if there is a need to integrate the antenna.
- The noise figure should be around 2 dB for the antenna assembly itself.
- Ensure active antenna gain is ideally between 30 40 dB gain and that an LNA gain of 20 dB reaches the module RF\_IN pin.
- Make sure the antenna is not placed close to noisy parts of the circuitry and does not face any other noisy elements (for example microcontroller, display).
- If a combined L1/L2/L6 antenna is used, for RTK operation good signals levels above 40 C/ N0 average are required. There is a requirement on the minimum number and type of GNSS/ QZSS satellites being received in a typical environment to achieve fixed RTK performance: Signals above 35 C/N0 (minimum) for a minimum of 6 GPS satellites. The same is true for any single system that is enabled (BeiDou, GLONASS). The same is true if a multi constellation



configuration is used. A single system being received must have 6 satellites at the minimum signal level and quality to achieve RTK fixed status. L2/L6 signals for the NEO-D9C must have similar C/N0 levels.

- If a patch type antenna is used, an antenna ground plane with minimum 100 150 mm diameter is required.
- Ensure the combined antenna is L1 and L2/L6 band specified.
- Ensure the combined antenna element gain is between 2 3 dBic typical for L1 and L2/L6 bands.
- If a combined L1 + L2/L6 antenna is used, ensure the group delay variation including active antenna is 10 ns max at each GNSS system bandwidth. Note: Inter-signal requirement 50 ns max.
- ESD protection on the RF input is mandatory.
- Bias-t inductor must be L1 and L2/L6 band frequency selected.
- Ensure RF trace is tuned for 50 Ω to ensure L1 and L2/L6 bandwidth.

#### <span id="page-39-0"></span>**4.8.4 Ground pads**

Ensure the ground pads of the module are connected to ground.

#### <span id="page-39-1"></span>**4.8.5 Schematic design**

For a **minimal design** with the NEO-D9C modules, consider the following functions and pins:

- Connect the power supply to VCC.
- V\_USB: If USB is used it is recommended V\_USB is to be powered as per USB self-powered mode specification.
- If USB is not used connect V\_USB to ground.
- Ensure an optimal ground connection to all ground pins of the NEO-D9C module.
- Choose the required serial communication interfaces (UART, USB, SPI or I2C) and connect the appropriate pins to your application.
- Antenna bias is required, see NEO-D9C antenna bias section.

#### <span id="page-39-2"></span>**4.8.6 Layout design-in guideline**

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?
- Is the receiver placed as recommended in the [Layout](#page-33-1) and Layout [guidance](#page-35-0)?
- Assure a low serial resistance on the VCC power supply line (choose a line width > 400 um).
- Keep the power supply line as short as possible.
- Add a ground plane underneath the module to reduce interference. This is especially important for the RF input line.
- For improved shielding, add as many vias as possible around the micro strip/co-planar waveguide, around the serial communication lines, underneath the module, etc.



# <span id="page-40-0"></span>**5 Product handling**

## <span id="page-40-1"></span>**5.1 ESD handling precautions**

NEO-D9C contains highly sensitive electronic circuitry and is an Electrostatic Sensitive Device (ESD). Observe precautions for handling! Failure to observe these precautions can result in severe damage to the GNSS receiver!

• Unless there is a galvanic coupling between the local GND (i.e. the work table) and the PCB GND, then the first point of contact when handling the PCB must always be between the local GND and PCB GND.

- Before mounting an antenna patch, connect ground of the device.
- When handling the RF pin, do not come into contact with any charged capacitors and be careful when contacting materials that can develop charges (e.g. patch antenna ~10 pF, coax cable ~50-80 pF/m or soldering iron).
- To prevent electrostatic discharge through the RF input, do not touch any exposed antenna area. If there is any risk that such exposed antenna area is touched in non-ESD protected work area, implement proper ESD protection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, make sure to use an ESD-safe soldering iron (tip)







## <span id="page-40-2"></span>**5.2 Soldering**

#### **Soldering paste**

Use of "no clean" soldering paste is highly recommended, as it does not require cleaning after the soldering process. The paste in the example below meets these criteria.

- Soldering paste: OM338 SAC405 / Nr.143714 (Cookson Electronics)
- Alloy specification: Sn 95.5/ Ag 4/ Cu 0.5 (95.5% tin/ 4% silver/ 0.5% copper)
- Melting temperature: 217 °C
- Stencil thickness: The exact geometry, distances, stencil thicknesses and solder paste volumes must be adapted to the customer's specific production processes (e.g. soldering).

#### **Reflow soldering**

**A convection-type soldering oven is highly recommended** over the infrared-type radiation oven. Convection-heated ovens allow precise control of the temperature, and all parts will heat up evenly, regardless of material properties, thickness of components and surface color.



As a reference, see "IPC-7530 Guidelines for temperature profiling for mass soldering (reflow and wave) processes", published in 2001.

#### **Preheat phase**

During the initial heating of component leads and balls, residual humidity will be dried out. Note that the preheat phase does not replace prior baking procedures.

- Temperature rise rate: max 3 °C/s. If the temperature rise is too rapid in the preheat phase, excessive slumping may be caused
- Time: 60 120 s. If the preheat is insufficient, rather large solder balls tend to be generated. Conversely, if performed excessively, fine balls and large balls will be generated in clusters
- End temperature: 150 200 °C. If the temperature is too low, non-melting tends to be caused in areas containing large heat capacity

#### **Heating - reflow phase**

The temperature rises above the liquidus temperature of 217 °C. Avoid a sudden rise in temperature as the slump of the paste could become worse.

#### **For professional grade modules**

- Limit time above 217 °C liquidus temperature: 40 60 s
- Peak reflow temperature: 245 °C

#### **For automotive grade modules**

- Limit time above 217 °C liquidus temperature: 60 150 s
- Peak reflow temperature: 250 °C

#### **Cooling phase**

A controlled cooling prevents negative metallurgical effects of the solder (solder becomes more brittle) and possible mechanical tensions in the products. Controlled cooling helps to achieve bright solder fillets with a good shape and low contact angle.

#### **For professional grade modules**

• Temperature fall rate: max 4 °C/s

#### **For automotive grade modules**

- Temperature fall rate: max 6 °C/s
- To avoid falling off, the modules should be placed on the topside of the motherboard during soldering.

The final soldering temperature chosen at the factory depends on additional external factors such as the choice of soldering paste, size, thickness and properties of the base board, etc. Exceeding the maximum soldering temperature in the recommended soldering profile may permanently damage the module.





#### **Figure 35: Soldering profile for professional grade NEO-D9C**



**Figure 36: Soldering profile for automotive grade NEO-D9C**

Modules **must not** be soldered with a damp heat process.

#### **Optical inspection**

After soldering the module, consider optical inspection.

#### **Cleaning**

Do not clean with water, solvent, or ultrasonic cleaner:

- Cleaning with water will lead to capillary effects where water is absorbed into the gap between the baseboard and the module. The combination of residues of soldering flux and encapsulated water leads to short circuits or resistor-like interconnections between neighboring pads.
- Cleaning with alcohol or other organic solvents can result in soldering flux residues flowing underneath the module, into areas that are not accessible for post-cleaning inspections. The solvent will also damage the sticker and the printed text.



• Ultrasonic cleaning will permanently damage the module, in particular the quartz oscillators.

The best approach is to use a "no clean" soldering paste and eliminate the cleaning step after the soldering.

#### **Repeated reflow soldering**

Repeated reflow soldering processes or soldering the module upside down are not recommended.

A board that is populated with components on both sides may require more than one reflow soldering cycle. In such a case, the process should ensure the module is only placed on the board submitted for a single final upright reflow cycle. A module placed on the underside of the board may detach during a reflow soldering cycle due to lack of adhesion.

The module can also tolerate an additional reflow cycle for rework purposes.

#### **Wave soldering**

Base boards with combined through-hole technology (THT) components and surface-mount technology (SMT) devices require wave soldering to solder the THT components. Only a single wave soldering process is encouraged for boards populated with modules.

#### **Rework**

We do not recommend using a hot air gun because it is an uncontrolled process and can damage the module.



Use of a hot air gun can lead to overheating and severely damage the module. Always avoid overheating the module.

After the module is removed, clean the pads before reapplying solder paste, placing and reflow soldering a new module.

Never attempt a rework on the module itself, e.g. by replacing individual components. Such actions will immediately void the warranty.

#### **Conformal coating**

Certain applications employ a conformal coating of the PCB using HumiSeal® or other related coating products. These materials affect the RF properties of the GNSS module and it is important to prevent them from flowing into the module. The RF shields do not provide 100% protection for the module from coating liquids with low viscosity. Apply the coating carefully.

Conformal coating of the module will void the warranty.

#### **Casting**

If casting is required, use viscose or another type of silicon pottant. The OEM is strongly advised to qualify such processes in combination with the module before implementing this in the production.

Casting will void the warranty.

#### **Grounding metal covers**

Attempts to improve grounding by soldering ground cables, wick or other forms of metal strips directly onto the EMI covers is done at the customer's own risk. The numerous ground pins should be sufficient to provide optimum immunity to interferences and noise.

u-blox makes no warranty for damages to the module caused by soldering metal cables or any other forms of metal strips directly onto the EMI covers.



#### **Use of ultrasonic processes**

Some components on the module are sensitive to ultrasonic waves. Use of any ultrasonic processes (cleaning, welding etc.) may cause damage to the GNSS receiver.

u-blox offers no warranty against damages to the module caused by ultrasonic processes.

### <span id="page-44-0"></span>**5.3 Tapes**

[Figure](#page-44-1) 37 shows the feed direction and illustrates the orientation of the NEO-D9Cs on the tape:

<span id="page-44-1"></span>

**Figure 37: Orientation of NEO-D9C on the tape**

The dimensions of the tapes for NEO-D9C are specified in [Figure](#page-45-2) 38 (measurements in mm).



<span id="page-45-2"></span>

**Figure 38: NEO-D9C tape dimensions (mm)**

### <span id="page-45-0"></span>**5.4 Reels**

The NEO-D9C receivers are deliverable in quantities of 250 pieces on a reel.The receivers are shipped on reel type B, as specified in the u-blox Package Information Guide [\[3\]](#page-49-3).

### <span id="page-45-1"></span>**5.5 Moisture sensitivity levels**

The moisture sensitivity level (MSL) for NEO-D9C is specified in the table below.

| Package | MSL level                        |
|---------|----------------------------------|
|         | 4 (NEO-D9C-00B), 3 (NEO-D9C-00A) |

**Table 7: MSL level**

For MSL standard see IPC/JEDEC J-STD-020, which can be downloaded from www.jedec.org.

For more information regarding moisture sensitivity levels, labeling, storage and drying, see the u-blox Package Information Guide [\[3\]](#page-49-3).



# <span id="page-46-0"></span>**Appendix**

## <span id="page-46-1"></span>**A Stacked patch antenna**

A typical low cost L1 + L2 + L6 antenna is based on a stacked patch antenna design. This consists of two discrete ceramic patch elements with an L1 patch above an L2/L6 patch.



#### **Figure 39: Stacked patch antenna**

The absolute antenna position for a survey-grade antenna is normally given as the antenna reference point (ARP), usually specified at amechanicalmounting point.The antenna nominal phase center is given by a phase center combination of the L1 and L2/L6 patches. Survey-grade antenna makers provide offset data for phase variation with respect to the ARP.



**Figure 40: Ceramic stack**

When used in an automotive application, the antenna placement can affect the phase center variation owing to the size and shape of the ground plane coupled with the effects of the adjacent structures. A phase center variation calibration is required to check the actual antenna position. A



successful calibration can bemade if the phase variation of a specific antenna is repeatable between samples.

To obtain the best antenna performance in an automotive application, mount the antenna in the center of a conductive car roof without any inclination. The antenna requires good signal levels and as wide a view of the sky as possible. The antenna must not be placed under a dashboard, in the rear view mirror, or on the rear parcel shelf.

An L1 + L2 + L6 stacked patch antenna must have a good band-pass performance from the patch elements with low attenuation from SAW band-pass filtering. An example of the measured frequency characteristics of a low-cost L1 + L2 + L6 antenna is shown below.



**Figure 41: Low cost L1/L2/L6 antenna Band characteristics**

### <span id="page-47-0"></span>**B Glossary**

| Abbreviation | Definition                            |  |
|--------------|---------------------------------------|--|
| ANSI         | American National Standards Institute |  |
| ARP          | Antenna reference point               |  |
| BeiDou       | Chinese navigation satellite system   |  |
| BBR          | Battery-backed RAM                    |  |
| CDMA         | Code-division multiple access         |  |
| EMC          | Electromagnetic compatibility         |  |



| Abbreviation | Definition                                |  |  |
|--------------|-------------------------------------------|--|--|
| EMI          | Electromagnetic interference              |  |  |
| EOS          | Electrical overstress                     |  |  |
| EPA          | Electrostatic protective area             |  |  |
| ESD          | Electrostatic discharge                   |  |  |
| Galileo      | European navigation satellite system      |  |  |
| GLONASS      | Russian navigation satellite system       |  |  |
| GND          | Ground                                    |  |  |
| GNSS         | Global navigation satellite system        |  |  |
| GPS          | Global Positioning System                 |  |  |
| GSM          | Global System for Mobile Communications   |  |  |
| I2C          | Inter-integrated circuit bus              |  |  |
| IEC          | International Electrotechnical Commission |  |  |
| PCB          | Printed circuit board                     |  |  |
| PMP          | Point-to-multipoint transmission          |  |  |
| QZSS         | Quasi-Zenith Satellite System             |  |  |
| RF           | Radio frequency                           |  |  |
| SV           | Space vehicle, a satellite                |  |  |
| UBX          | u-blox                                    |  |  |



# <span id="page-49-0"></span>**Related documents**

- <span id="page-49-2"></span>**[1]** NEO-D9C-00B Data sheet, UBX-17053092
  - NEO-D9C-00A Data sheet C2-Restricted, UBX-20057098
- <span id="page-49-1"></span>**[2]** QZS 1.01 Interface description, UBX-21031777
- <span id="page-49-3"></span>**[3]** Packaging information for u-blox chips, modules, and antennas, [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage [https://www.u-blox.com.](https://www.u-blox.com)



# <span id="page-50-0"></span>**Revision history**

| Revision | Date        | Name | Status / comments                                    |
|----------|-------------|------|------------------------------------------------------|
| R01      | 27-Aug-2021 | dbhu | First issue of the document                          |
| R02      | 16-Dec-2021 | dama | UART2 interface general update                       |
| R03      | 15-Dec-2022 | dbhu | Section 4.7 Layout updated. Overall text improvement |



# **Contact**

#### **u-blox AG**

Address: Zürherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).