

# **NEO-D9S**

# **Correction data receiver**

**Integration manual**



## **Abstract**

This document describes the features and specifications of the u-blox D9 correction data receiver.

**www.u-blox.com**

UBX-19026111 - R09 C1-Public





# **Document information**

| Title                  | NEO-D9S                  |  |
|------------------------|--------------------------|--|
| Subtitle               | Correction data receiver |  |
| Document type          | Integration manual       |  |
| Document number        | UBX-19026111             |  |
| Revision and date      | R09<br>26-Feb-2024       |  |
| Disclosure restriction | C1-Public                |  |

This document applies to the following products:

| Type number    | FW version | IN/PCN reference | RN reference |
|----------------|------------|------------------|--------------|
| NEO-D9S-00B-00 | PMP 1.04   | -                | UBX-20006297 |
| NEO-D9S-00A-01 | PMP 1.06   | UBX-22039058     | UBX-22039051 |

u-blox or third parties may hold intellectual property rights in the products, names, logos and designs included in this document. Copying, reproduction, or modification of this document or any part thereof is only permitted with the express written permission of u-blox. Disclosure to third parties is permitted for clearly public documents only.

The information contained herein is provided "as is" and u-blox assumes no liability for its use. No warranty, either express or implied, is given, including but not limited to, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information.This document may be revised by u-blox at any time without notice. For the most recent documents, visit www.u-blox.com.

Copyright © 2024, u-blox AG.



| 1 Integration<br>manual<br>overview                     | 5  |  |
|---------------------------------------------------------|----|--|
| 2 System<br>description6                                |    |  |
| 2.1 Overview 6                                          |    |  |
| 2.1.1 Satellite L-band GNSS error corrections6          |    |  |
| 2.2 Architecture7                                       |    |  |
| 2.2.1 Block diagram7                                    |    |  |
| 3 Receiver<br>functionality                             | 8  |  |
| 3.1 Receiver configuration 8                            |    |  |
| 3.1.1 Changing the receiver configuration8              |    |  |
| 3.1.2 Default L-band configuration8                     |    |  |
| 3.1.3 Default interface settings 8                      |    |  |
| 3.1.4 Basic receiver configuration9                     |    |  |
| 3.1.5 L-band service selection 9                        |    |  |
| 3.1.6 Power management10                                |    |  |
| 3.2 Communication interfaces 11                         |    |  |
| 3.2.1 UART12                                            |    |  |
| 3.2.2 I2C interface13                                   |    |  |
| 3.2.3 SPI interface16                                   |    |  |
| 3.2.4 USB interface17                                   |    |  |
| 3.3 Predefined PIOs18                                   |    |  |
| 3.3.1 D_SEL18                                           |    |  |
| 3.3.2 RESET_N 18                                        |    |  |
| 3.3.3 SAFEBOOT_N18                                      |    |  |
| 3.3.4 TX_READY 19                                       |    |  |
| 3.3.5 EXTINT19                                          |    |  |
| 3.4 Antenna supervisor 20                               |    |  |
| 3.4.1 Antenna voltage control - ANT_OFF21               |    |  |
| 3.4.2 Antenna short detection - ANT_SHORT_N 21          |    |  |
| 3.4.3 Antenna short detection auto recovery22           |    |  |
| 3.4.4 Antenna open circuit detection - ANT_DETECT 22    |    |  |
| 3.5 Security 23                                         |    |  |
| 3.5.1 Receiver status monitoring 23                     |    |  |
| 3.6 Forcing a receiver reset23<br>3.7 Firmware upload23 |    |  |
| 4 Design                                                | 24 |  |
| 4.1 Pin assignment24                                    |    |  |
| 4.2 Antenna25                                           |    |  |
| 4.2.1 Antenna bias27                                    |    |  |
| 4.3 Power supply30                                      |    |  |
| 4.3.1 VCC: Main supply voltage 30                       |    |  |
| 4.3.2 NEO-D9S power supply 30                           |    |  |
| 4.4 NEO-D9S minimal design 31                           |    |  |
| 4.5 EOS/ESD precautions 31                              |    |  |
| 4.5.1 ESD protection measures 32                        |    |  |
|                                                         |    |  |

| 4.5.2 EOS precautions32                           |    |
|---------------------------------------------------|----|
| 4.5.3 Safety precautions 33                       |    |
| 4.6 Electromagnetic interference on I/O lines33   |    |
| 4.6.1 General notes on interference issues33      |    |
| 4.6.2 In-band interference mitigation34           |    |
| 4.6.3 Out-of-band interference 34                 |    |
| 4.7 Layout35                                      |    |
| 4.7.1 Placement35                                 |    |
| 4.7.2 Thermal management 35                       |    |
| 4.7.3 Package footprint, copper and paste mask 35 |    |
| 4.7.4 Layout guidance 36                          |    |
| 4.8 Design guidance39                             |    |
| 4.8.1 General considerations 39                   |    |
| 4.8.2 RF front-end circuit options 39             |    |
| 4.8.3 Antenna/RF input 40                         |    |
| 4.8.4 Schematic design 40                         |    |
| 4.8.5 Layout design-in guideline 40               |    |
| 5 Product<br>handling                             | 41 |
| 5.1 ESD handling precautions 41                   |    |
| 5.2 Soldering42                                   |    |
| 5.3 Tapes 45                                      |    |
| 5.4 Reels 46                                      |    |
| 5.5 Moisture sensitivity levels 46                |    |
| Appendix                                          | 48 |
| A Stacked patch antenna48                         |    |
| B Glossary49                                      |    |
| Related<br>documents                              | 51 |
| Revision<br>history52                             |    |
|                                                   |    |



# <span id="page-4-0"></span>**1 Integration manual overview**

This document is an important source of information on all aspects of u-blox D9 correction data receiver. The purpose of this document is to provide guidelines for a successful integration of the receiver with the customer's end product.



# <span id="page-5-0"></span>**2 System description**

# <span id="page-5-1"></span>**2.1 Overview**

NEO-D9S is a satellite data receiver for L-band correction broadcast. The receiver be configured for use with a variety of correction services. It decodes the satellite transmission and outputs a correction stream, enabling a high precision GNSS receiver to reach accuracy down to centimeter level.

# <span id="page-5-2"></span>**2.1.1 Satellite L-band GNSS error corrections**

Wide area correction services from several service providers are available via the L-band communication satellites. These satellites cover the bulk of the globe's populated surface. However, each error correction service provider using the L-band channel will possibly have spot beams coveringonly the relevant area forwhichtheir corrections are valid.This ensures that their correction coverage area is accessible via a satellite and not simply broadcast over large areas of the earth with no feasible use.

Each service provider will be allocated a correction service ID and a frequency for a particular part of the globe. In addition the service provider will have a data bit rate for their data stream.

This means that the frequency allocation for a particular service provider could change. It is important that any deployed system can be reconfigured if necessary. Service providers do provide information on any frequency changes when required.



# <span id="page-6-0"></span>**2.2 Architecture**

The NEO-D9Sreceiver provides all the necessary RFand baseband processing to enable multi-band, multi-constellation operation. The block diagram below shows the key functionality.

# <span id="page-6-1"></span>**2.2.1 Block diagram**



#### **Figure 1: NEO-D9S block diagram**

An active antenna is mandatory with the NEO-D9S.



# <span id="page-7-0"></span>**3 Receiver functionality**

This chapter describes the NEO-D9S operational features and their configuration.

# <span id="page-7-1"></span>**3.1 Receiver configuration**

u-blox positioning receivers are fully configurable with UBX protocol messages. The configuration used by the receiver during normal operation is called the "current configuration". The current configuration can be changed during normal operation by sending UBX configuration messages. On startup, the current configuration held in RAM is built from the default firmware settings plus any settings held in flash memory.

Configuration interface settings are held in a database consisting of separate configuration items. An item is made up of a pair consisting of a key ID and a value. Related items are grouped together and identified under a common group name: CFG-GROUP-\*; a convention used in u-center and within this document. Within u-center, a configuration group is identified as "Group name" and the configuration item is identified as the "item name" under the "Generation 9 Configuration View" - "Advanced Configuration" view.

The UBX messages available to change or poll the configurations are UBX-CFG-VALSET, UBX-CFG-VALGET, and UBX-CFG-VALDEL. For more information about these messages and the configuration keys, see the configuration interface section in the applicable Interface description [[2\]](#page-50-1).

# <span id="page-7-2"></span>**3.1.1 Changing the receiver configuration**

The configuration messages UBX-CFG-VALSET, UBX-CFG-VALGET and UBX-CFG-VALDEL will result in a UBX-ACK-ACK or a UBX-ACK-NAK response.

# <span id="page-7-3"></span>**3.1.2 Default L-band configuration**

The default L-band configuration is:

- CFG-PMP-CENTER\_FREQUENCY = 1539812500 Hz
- CFG-PMP-SEARCH\_WINDOW = 2200 Hz
- CFG-PMP-USE\_SERVICE\_ID = 1 (true)
- CFG-PMP-SERVICE\_ID = 50821
- CFG-PMP-DATA\_RATE = 2400 (B2400) bps
- CFG-PMP-USE\_DESCRAMBLER = 1 (true)
- CFG-PMP-DESCRAMBLER\_INIT = 23560
- CFG-PMP-UWERRT = 4
- CFG-PMP-USE\_PRESCRAMBLING = 0 (false)
- CFG-PMP-UNIQUE\_WORD = 0xe15ae893e15ae893

The configuration settings can be modified using UBX protocol configuration messages. For more information, see the applicable Interface description [\[2\]](#page-50-1).

## <span id="page-7-4"></span>**3.1.3 Default interface settings**

| Interface | Settings                                      |  |
|-----------|-----------------------------------------------|--|
| UART      | 9600 baud, 8 bits, no parity bit, 1 stop bit. |  |
|           | Output protocol: UBX.                         |  |

The required satellite center frequency and service data rate might need changing based on the receiver global location to aid acquisition of the required satellite/service (service ID).



| Interface | Settings                                                                    |  |
|-----------|-----------------------------------------------------------------------------|--|
|           | Input protocols without need of additional configuration: UBX.              |  |
| USB       | Output messages activated as in UART. Input protocols available as in UART. |  |
| I2C       | Output messages activated as in UART. Input protocols available as in UART. |  |
| SPI       | Output messages activated as in UART. Input protocols available as in UART. |  |

**Table 1: Default interface settings**

The boot message is still output using \$GNTXT messages. The messages are output when the NEO-D9S is powered up.

Refer to the applicable interface description [[2](#page-50-1)] for information about further settings.

## <span id="page-8-0"></span>**3.1.4 Basic receiver configuration**

This section summarizes the basic receiver configuration most commonly used.

### <span id="page-8-2"></span>**3.1.4.1 Communication interface configuration**

Several configuration groups allow operation mode configuration of the various communication interfaces. These include parameters for the data framing, transfer rate and enabled input/output protocols. See [Communication](#page-10-0) interfaces section for details. The configuration groups available for each interface are:

| Interface | Configuration groups                               |
|-----------|----------------------------------------------------|
| UART1     | CFG-UART1-*, CFG-UART1INPROT-*, CFG-UART1OUTPROT-* |
| UART2     | CFG-UART2-*, CFG-UART2INPROT-*, CFG-UART2OUTPROT-* |
| USB       | CFG-USB-*, CFG-USBINPROT-*, CFG-USBOUTPROT-*       |
| I2C       | CFG-I2C-*, CFG-I2CINPROT-*, CFG-I2COUTPROT-*       |
| SPI       | CFG-SPI-*, CFG-SPIINPROT-*, CFG-SPIOUTPROT-*       |

**Table 2: Interface configurations**

#### **3.1.4.2 Message output configuration**

The rate of the supported output messages is configurable.

If the rate configuration value is zero, then the corresponding message will not be output. Values greater than zero indicate how often the message is output.

For periodic output messages the rate relates to the event the message is related to. The rates of the output messages are individually configurable per communication interface. See the CFG-MSGOUT-\* configuration group.

Some messages, such as UBX-MON-VER, are non-periodic and will only be output as an answer to a poll request.

The UBX-INF-\* information messages are non-periodic output messages that do not have a message rate configuration. Instead they can be enabled for each communication interface via the CFG-INFMSG-\* configuration group.

All message output is additionally subject to the protocol configuration of the communication interfaces.Messages of a givenprotocolwillnot be output until the protocol is enabled for output on the interface (see [Communication](#page-8-2) interface configuration).

## <span id="page-8-1"></span>**3.1.5 L-band service selection**

Any particular service provider will have several requirements that need to be configured before the receiver will provide the relevant service provider data:



- Service provider service ID
- Service provider frequency based on geographical location
- Service provider data rate
- The service provider will provide the information on the frequency required per geographical location.

All relevant configurations are done via the CFG-PMP message.

The main settings are shown below:

- CFG-PMP-SERVICE\_ID Example, 50821
- CFG-PMP-CENTER\_FREQUENCY Can be set from 1525000000 to 1559000000 Hz
- CFG-PMP-DATA\_RATE Can be set from 600 bps to 4800 bps

There may be additional settings required that can be configured from the information supplied by the service provider.

The receiver will output raw L-band correction data when a service provider satellite data frame is received. This will be output in the UBX-RXM-PMP message. This message is not output at a fixed rate.

If no selected service provider data frame is detected, no UBX-RXM-PMP message is sent. The output rate of the UBX-RXM-PMP message depends on the data rate of the satellite data stream (600 bps - 4800 bps). The validity of the data frame must be verified by the host software. For frame verification, quality indicators included in this message can be used.

For more information see the Configuration Interface section in the applicable Interface description [\[2](#page-50-1)].



#### **Figure 2: L-band SESTB-28A data frame**

### <span id="page-9-0"></span>**3.1.6 Power management**

u-blox D9 correction data receiver supports two different externally controlled power modes.

- External cycling of the receiver main power supply with the receiver in continuous mode when powered
- Instruct the receiver to turn on/off into software backup mode (with main power still applied) via the UBX-RXM-PMREQ message

#### **3.1.6.1 Continuous mode**

u-blox receivers use dedicated signal processing engines optimized for signal acquisition and tracking.The acquisitionenginedelivers rapidsignal searchesduringcoldstarts orwheninsufficient signals are available for data download. The tracking engine delivers signal measurements for message decoding.



#### **3.1.6.2 Power on/off command - software backup**

With message UBX-RXM-PMREQ the receiver can be forced to enter *Inactive* state (software backup mode) with main power still applied. It will stay in *Inactive* state for the time specified in the message or until it is woken up by activity on the RXD1, NRESET pin or EXTINT pin.

#### **3.1.6.2.1 Wake up**

The receiver can be woken up by generating an edge on one of the following pins:

- Rising or falling edge on one of the EXTINT pins
- Rising or falling edge on the RXD1 pin
- Rising edge on NRESET pin

All wake-up signals are interpreted as an acquisition request, where the receiver wakes up and tries to obtain the satellite.Wake-up signals have no effect if the receiver is already in*Acquisition*, *Tracking* state.

#### **3.1.6.2.2 Behavior while USB host connected**

As long as the receiver is connected to a USB host, it will not enter the lowest possible power state. This is because it must retain a small level of CPU activity to avoid breaching requirements of the USB specification. The drawback, however, is that power consumption is higher.

Wake up by N\_RESET, EXTINT pin or UART RX is possible even if the receiver is connected to a USB host. In this case the state of the pin must be changed for a duration longer than one millisecond.

# <span id="page-10-0"></span>**3.2 Communication interfaces**

u-blox receivers are equipped with a communication interface which is multi-protocol capable. The interface ports can be used to transmit GNSS measurements, monitor status information and configure the receiver.

A protocol (e.g. UBX, NMEA) can be assigned to several ports simultaneously, each configured with individual settings (e.g. baud rate, message rates, etc.). More than one protocol (e.g. UBX protocol and NMEA) can be assigned to a single port (multi-protocol capability), which is particularly useful for debugging purposes.

The NEO-D9S provides UART1, UART2, SPI, I2C and USB interfaces for communication with a host CPU. The interfaces are configured via the configuration methods described in the applicable interface description [\[2\]](#page-50-1).

It is important to isolate interface pins when VCC is removed. They can be allowed to float or be connected to a high impedance (Float or tri-state: Hi-Z state). Open collector circuits powered by module VCC are also suitable. They must be powered by module VCC to ensure correct pin state when module VCC is removed.

Example isolation circuit is shown below.





**Figure 3: NEO-D9S output isolation**



**Figure 4: NEO-D9S input isolation**

# <span id="page-11-0"></span>**3.2.1 UART**

A Universal Asynchronous Receiver/Transmitter (UART) port consists of an RX and a TX line. Neither handshaking signals nor hardware flow control signals are available. The UART interface protocol and baud rate can be configured but there is no support for setting different baud rates for reception and transmission.

The NEO-D9S includes two UART serial ports. UART1 can be used as a host interface for configuration, monitoring and control.

- UART2 may be used to provide correction data directly to a high precision GNSS receiver from the u-blox F9 platform. To check whether a specific u-blox F9 product supports correction data output by the NEO-D9S, refer to its Integration manual.
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

## <span id="page-12-0"></span>**3.2.2 I2C interface**

An I2C interface is available for communication with an external host CPU or u-blox cellular modules in peripheral mode only. The I2C protocol and electrical interface supports the Fast-mode of the I2C industry standard with a maximum SCL clock frequency of 400 kHz. Backwards compatibility with Standard-mode I2C bus operation is not supported.

The SCL and SDA pins have internal pull-up resistors which should be sufficient for most applications. However, depending on the speed of the host and the load on the I2C lines additional external pull-up resistors may be necessary.

- To use the I2C interface D\_SEL pin must be left open.
- In designs where the host uses the same I2C bus to communicate with more than one u-blox receiver, the I2C peripheral address for each receiver must be configured to a different value. Typically most u-blox receivers are configured to the same default I2C peripheral address value. To poll or set the I2C peripheral address, use the CFG-I2C-ADDRESS configuration item (see the applicable interface description [[2](#page-50-1)]).

The CFG-I2C-ADDRESS configuration item is an 8-bit value that includes the I2C peripheral address in the 7 most significant bits and the read/write flag in the least significant bit. In RAM, the default value is 0x86 / 134 (10000110), representing a standard 7-bit I2C peripheral address of 0x43 (1000011). In ROM, the default value is 0x84 / 132 (10000100), indicating a standard 7-bit I2C peripheral address of 0x42 (1000010).

#### **3.2.2.1 I2C register layout**

The I2C interface allows 256 registers to be addressed. As shown in [Figure](#page-13-0) 5, only three of these are currently implemented.

The data registers 0 to 252 at addresses 0x00 to 0xFC contain reserved information, the result from their reading is currently undefined. The data registers 0 to 252 are 1 byte wide.

At addresses 0xFD and 0xFE it is possible to read the currently available number of bytes.



The register at address 0xFF allows the data stream to be read. If there is no data awaiting transmission from the receiver, then this register delivers value 0xFF, which cannot be the first byte of a valid message. If the message data is ready for transmission, the successive reads of register 0xFF will deliver the waiting message data.

Do not use registers 0x00 to 0xFC. They are reserved for future use and they do not currently provide any meaningful data.

<span id="page-13-0"></span>

#### **Figure 5: I2C register layout**

#### **3.2.2.2 Read access types**

There are two I2C read transfer forms:

- The "random access" form: includes a peripheral register address and allows any register to be read.
- The "current address" form: omits the register address.

[Figure](#page-14-0) 6 shows the format of the first one, the "random access" form of the request. Following the start condition from the controller, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the controller transmitter. The receiver answers with an acknowledge (logic low) to indicate that it recognizes the address.

Next, the 8-bit address of the register to be read must be written to the bus. Following the receiver's acknowledgment, the controller again triggers a start condition and writes the device address, but this time the RW bit is a logic high to initiate the read access. Now, the controller can read 1 to N bytes from the receiver, generating a not-acknowledge and a stop condition after the last byte being read.



<span id="page-14-0"></span>

#### **Figure 6: I2C random read access**

If the second form, "current address" is used, an address pointer in the receiver is used to determine which register to read. This address pointer will increment after each read unless it is already pointing at register 0xFF, the highest addressable register, in which case it remains unaltered.

The initial value of this address pointer at startup is 0xFF, so by default all current address reads will repeatedly read register 0xFF and receive the next byte of message data (or 0xFF if no message data is waiting).



**Figure 7: I2C current address read access**

#### **3.2.2.3 Write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. Therefore, the register set mentioned in the section Read [access](#page-15-1) is not writeable.

Following the start condition from the controller, the 7-bit device address and the RW bit (which is a logic low for write access) are clocked onto the bus by the controller transmitter. The receiver answers with an acknowledge (logic low) to indicate that it is responsible for the given address.

The controller can write 2 to N bytes to the receiver, generating a stop condition after the last byte being written. The number of data bytes must be at least 2 to properly distinguish from the write access to set the address counter in random read accesses.







## <span id="page-15-0"></span>**3.2.3 SPI interface**

NEO-D9S has an SPI peripheral interface that can be selected by setting D\_SEL = 0. The SPI peripheral interface is shared with UART1 and I2C port, the physical pins are same. The SPI pins available are:

- SPI\_SDO (TXD)
- SPI\_SDI (RXD)
- SPI\_CS\_N
- SPI\_CLK

See more information about communication interface selection from the [D\\_SEL](#page-17-1) section.

The SPI interface is designed to allow communication to a host CPU. The interface can be operated in peripheral mode only.

#### <span id="page-15-1"></span>**3.2.3.1 Read access**

As the register mode is not implemented for the SPI port, only the UBX/NMEA message stream is provided. This stream is accessed using the back-to-back read and write access (see section [Back](#page-15-2)[to-back](#page-15-2) read and write access below). When no data is available to be written to the receiver, SDI should be held logic high, i.e. all bytes written to the receiver are set to 0xFF.

To prevent the receiver from being busy parsing incoming data, the parsing process is stopped after 50subsequent bytes containing0xFF.The parsing process is re-enabled with thefirst byte not equal to 0xFF.

If the receiver has no more data to send, it sets SDO to logic high, i.e. all bytes transmitted decode to 0xFF. An efficient parser in the host will ignore all 0xFF bytes which are not part of a message and will resume data processing as soon as the first byte not equal to 0xFF is received.

#### <span id="page-15-2"></span>**3.2.3.2 Back-to-back read and write access**

The receiver does not provide any write access except for writing UBX and NMEA messages to the receiver, such as configuration or aiding data. For every byte written to the receiver, a byte will simultaneously be read from the receiver. While the controller writes to SDI of the peripheral, at the same time it needs to read from SDO of the peripheral, as any pending data will be output by the receiver with this access. The data on SDO represents the results from a current address read, returning 0xFF when no more data is available.





**Figure 9: SPI back-to-back read/write access**

### <span id="page-16-0"></span>**3.2.4 USB interface**

A single USB port is provided for host communication purposes.

The USB 2.0 FS (Full speed, 12 Mbit/s) interface can be used for host communication. Due to the hardware implementation, it may not be possible to certify the USB interface.

If the receiver executes code from internal ROM (i.e. when a valid flash firmware image is not detected), the USB behavior can differ compared to executing a firmware image from flash memory. USB host compatibility testing is thus recommended in this scenario.

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





**Figure 10: NEO-D9S example circuit for USB interface**

R11 = 100 k Ω is recommended

R12, R13 = 27 Ω is recommended

# <span id="page-17-0"></span>**3.3 Predefined PIOs**

In addition to the communication ports, there are some predefined PIOs provided by NEO-D9S to interact with the receiver. These PIOs are described in this section.

If hardware backup mode is used a proper isolation of the interfaces is needed.

## <span id="page-17-1"></span>**3.3.1 D\_SEL**

The D\_SEL pin can be used to configure the functionality of the combined UART1, I2C, and SPI pins. It is possible to configure the pins as UART1 + I2C, or as SPI. SPI is not available unless D\_SEL pin is set to low. See [Table](#page-17-4) 4 below.

<span id="page-17-4"></span>

| Pin no. | D_SEL == 0 | D_SEL == 1 |
|---------|------------|------------|
| 20      | SPI_SDO    | UART1 TXD  |
| 21      | SPI_SDI    | UART1 RXD  |
| 18      | SPI_CS_N   | I2C SDA    |
| 19      | SPI_CLK    | I2C SCL    |

**Table 4: D\_SEL configuration**

### <span id="page-17-2"></span>**3.3.2 RESET\_N**

The NEO-D9S provides the ability to reset the receiver. The RESET\_N pin is an input-only pin with an internal pull-up resistor. Driving RESET\_N low for at least 100 ms will trigger a cold start.

The RESET\_N pin will delete all information and trigger a cold start. It should only be used as a recovery option.

## <span id="page-17-3"></span>**3.3.3 SAFEBOOT\_N**

The NEO-D9S provides a SAFEBOOT\_N pin that is used to command the receiver safeboot mode.

If this pin is low at power up, the receiver starts in safeboot mode and L-band operation is disabled.

The safeboot mode can be used to recover from situations where the flash content has become corrupted and needs to be restored.

In safeboot mode the receiver runs from a passive oscillator circuit with less accurate timing and hence the receiver is unable to communicate via USB.



In this mode UART1 communication is possible. For communication via UART1 in safeboot mode, the host must send a training sequence (0x55 0x55 at 9600 baud) to the receiver in order to begin communication. After this the host must wait at least 2 ms before sending any data.

It is recommended to have the possibility to pull the SAFEBOOT\_N pin low in the application. This can be provided using an externally connected test point or a host I/O port.

# <span id="page-18-0"></span>**3.3.4 TX\_READY**

This feature enables each port to define a corresponding pin, which indicates if bytes are ready to be transmitted. A listener can wait on the TX-READY signal instead of polling the I2C or SPI interfaces. The CFG-TXREADY message lets you configure the polarity and the number of bytes in the buffer before the TX-READY signal goes active. By default, this feature is disabled. For USB, this feature is configurable but might not behave as described below due to a different internal transmission mechanism. If the number of pending bytes reaches the threshold configured for this port, the corresponding pin will become active (configurable active-low or active-high), and stay active until the last bytes have been transferred from software to hardware.

This is not necessarily equal to all bytes transmitted, i.e. after the pin has become inactive, up to 16 bytes might still need to be transferred to the host.

The TX\_READY pin can be selected from all PIOs which are not in use (see UBX-MON-HW3 in the applicable interface description [\[2\]](#page-50-1) for a list of the PIOs and their mapping). Each TX\_READY pin is exclusively associated to one port and cannot be shared. If PIO is invalid or already in use, only the configuration for the specific TX\_READY pin is ignored, the rest of the port configuration is applied if valid. The acknowledge message does not indicate if the TX-READY configuration is successfully set, it only indicates the successful configuration of the port. To validate successful configuration of the TX\_READY pin, the port configuration should be read back and the settings of TX-READY feature verified (will be set to disabled/all zero if the settings are invalid).

The threshold when TX\_READY is asserted should not be set above 2 kB as it is possible that the internal message buffer limit is reached before this. This results in the TX\_READY pin never being set as the messages are discarded before the threshold is reached.

### **3.3.4.1 Extended TX timeout**

If the host does not communicate over SPI or I2C for more than approximately 2 seconds, the device assumes that the host is no longer using this interface and no more packets are scheduled for this port. This mechanism can be changed by enabling "extended TX timeouts", in which case the receiver delays idling the port until the allocated and undelivered bytes for this port reach 4 kB. This feature is especially useful when using the TX-READY feature with a message output rate of less than once per second, and polling data only when data is available, determined by the TX\_READY pin becoming active.

# <span id="page-18-1"></span>**3.3.5 EXTINT**

Leave open if unused, this function is disabled by default.

EXTINT is an external interrupt pin with fixed input voltage thresholds with respect to VCC. It is used in software backup mode to wake the module. Leave open if unused, this function is disabled by default.



# <span id="page-19-0"></span>**3.4 Antenna supervisor**

An active antenna supervisor provides the means to check the antenna for open and short circuits and to shut off the antenna supply if a short circuit is detected. Once enabled, the active antenna supervisor produces status messages, reporting in NMEA and/or UBX protocol.

The antenna supervisor can be configured through the CFG-HW-ANT\_\* configuration items. The current configuration of the active antenna supervisor can also be checked by polling the related CFG-HW\_ANT\_\* configuration items.

The current active antenna status can be determined by polling the UBX-MON-RF message. If an antenna is connected, the initial state after power-up is "Active Antenna OK" in the UBX-MON-RF message in the u-center "Message View".

An active antenna supervisor circuit is connected to the ANT\_DET, ANT\_OFF, ANT\_SHORT\_N pins. For an example the open circuit detection circuit using ANT\_DET, "high" = Antenna detected (antenna consumes current); "low" = Antenna not detected (no current drawn).

The following schematic details the required circuit and the sections following it explain how to enable and monitor each feature:



#### **Figure 11: NEO-D9S antenna supervisor**

- Use a bias-T inductor for multi-band operation. The recommeded Murata part requires 47 nH ±5%, with the current limited below its 300 mA rating. For additional information, see [Antenna](#page-26-0) [bias.](#page-26-0)
- The circuit shows a buffer [U4]. It is not strictly necessary to have a buffer when the current is supplied from the VCC. It is only required when supplying antenna voltage that is not obtained from the module VCC or VCC\_RF, or controlled by these.

The ESD diode is not shown in the image above, it is mounted close to the PCB RF connector.

| Part | Recommendation           | Comment                                |
|------|--------------------------|----------------------------------------|
| L1   | Murata LQG15HS47NJ02/47N | 300mA and >500 Ω at L-band frequencies |



| Part | Recommendation                       | Comment                          |
|------|--------------------------------------|----------------------------------|
| C2   | Murata GRM033R71C103KE14             | CAP CER X7R 0402 10N 10% 16V     |
|      | TYCO, 0.25PF, PESD0402-140 -55/+125C | ESD protection diode on RF trace |

**Table 5: Recommended components for antenna supervisor**

### <span id="page-20-0"></span>**3.4.1 Antenna voltage control - ANT\_OFF**

Antenna status (as reported in UBX-MON-RF and UBX-INF-NOTICE messages) is not reported unless the antenna voltage control has been enabled.

Enable the antenna voltage control by setting the configuration item CFG-HW-ANT\_CFG\_VOLTCTRL to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF pin = active high to turn antenna off therefore the pin is low to enable an external antenna.

Start-up message at power up if configuration stored:

```
$GNTXT,01,01,02,ANTSUPERV=AC *00
```

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC indicates antenna control is activated

### <span id="page-20-1"></span>**3.4.2 Antenna short detection - ANT\_SHORT\_N**

Enable the antenna short detection by setting the configuration item CFG-HW-ANT\_CFG\_SHORTDET to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high to disable an external antenna therefore the pin is low to enable an external antenna.
- ANT\_SHORT\_N = active low to detect a short therefore the pin is high (PIO pull up enabled to be pulled low if shorted)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD \*37

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD (Antenna control and short detection activated)

Then if shorted (ANT\_SHORT\_N pulled low):

• UBX-MON-RF in u-center "Message View": Antenna status = SHORT. Antenna power status = ON (Antenna power control power down when short has not been enabled = off by default).

\$GNTXT,01,01,02,ANTSTATUS=SHORT\*73

• ANT\_OFF = active high therefore still low (still enabled as auto power down is not enabled)



After a detected antenna short, the reported antenna status will keep on being reported as shorted. If the antenna short detection auto recovery is enabled, then the antenna status can recover after a timeout. To recover the antenna status immediately, a power cycle is required or configuring the antenna short detection functionality off and on.

### <span id="page-21-0"></span>**3.4.3 Antenna short detection auto recovery**

Enable the antenna short detection auto recovery by setting the configuration item CFG-HW-ANT\_CFG\_RECOVER to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high there for the PIO is low to enable an external antenna
- ANT\_SHORT\_N = high (PIO pull up enabled to be pulled low if shorted)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD PDoS SR\*3E

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD PDoS SR (indicates short circuit recovery added - SR)

Then if antenna is shorted (ANT\_SHORT\_N pulled low):

- \$GNTXT,01,01,02,ANTSTATUS=SHORT\*73
- UBX-MON-RF in u-center "Message View": Antenna status = SHORT. Antenna power status = OFF
- ANT\_OFF = high (to disable active high)

After a time out period receiver will retest the short condition by enabling ANT\_OFF = LOW

If a short is not present it will report antenna condition is OK:

\$GNTXT,01,01,02,ANTSTATUS=OK\*25

UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON

### <span id="page-21-1"></span>**3.4.4 Antenna open circuit detection - ANT\_DETECT**

Enable the antenna open circuit detection by setting the configuration item CFG-HW-ANT\_CFG\_OPENDET to true (1).

Result:

- UBX-MON-RF in u-center "Message View": Antenna status = OK. Antenna power status = ON
- ANT\_OFF = active high therefore PIO is low to enable external antenna
- ANT\_SHORT\_N = active low therefore PIO is high (PIO pull up enabled to be pulled low if shorted)
- ANT\_DETECT = active high therefore PIO is high (PIO pull up enabled to be pulled low if antenna not detected)

Start-up message at power up if configuration is stored:

\$GNTXT,01,01,02,ANTSUPERV=AC SD OD PDoS SR\*15

\$GNTXT,01,01,02,ANTSTATUS=INIT\*3B



\$GNTXT,01,01,02,ANTSTATUS=OK\*25

ANTSUPERV=AC SD OD PDoS SR (indicates open circuit detection added - OD)

Then if ANT\_DETECT is pulled low to indicate no antenna:

\$GNTXT,01,01,02,ANTSTATUS=OPEN\*35

Then if ANT\_DETECT is left floating or it is pulled high to indicate antenna connected:

```
$GNTXT,01,01,02,ANTSTATUS=OK*25
```

# <span id="page-22-0"></span>**3.5 Security**

## <span id="page-22-1"></span>**3.5.1 Receiver status monitoring**

Messages in the UBX class UBX-MON are used to report the status of the parts of the embedded computer system that are not related to the received satellite system specific info.

The main purposes are:

• Hardware and software versions, using UBX-MON-VER.

# <span id="page-22-2"></span>**3.6 Forcing a receiver reset**

The NEO-D9S is not a GNSS receiver and does not operate to the same principles as a standard GNSS. However it does support the standard UBX-CFG-RST command.

Data stored in flash memory is not cleared by any of the options provided by UBX-CFG-RST.

The resetMode must be specified.This is not related to L-band, but to the way the software restarts the system.

- **Hardware reset (watchdog), immediately** uses the on-chip watchdog, to electrically reset the chip. This is an immediate, asynchronous reset. No Stop event is generated.
- **Controlled software reset** terminates all running processes in an orderly manner and, once the system is idle, restarts operation, reloads its configuration and starts to acquire and track Lband satellites.
- **Hardware reset (watchdog), after shutdown** uses the on-chip watchdog, in order to electrically reset the chip after shutdown.

# <span id="page-22-3"></span>**3.7 Firmware upload**

NEO-D9S is supplied with firmware. u-blox may release updated images containing, for example, security fixes, enhancements, bug fixes, etc. Therefore it is important that customers implement a firmware update mechanism in their system.

A firmware image is a binary file containing the software to be run by the GNSS receiver. A firmware update is the process of transferring a firmware image to the receiver and storing it in non-volatile flash memory.

Contact u-blox for more information on firmware update.



# <span id="page-23-0"></span>**4 Design**

This section provides information to help carry out a successful schematic and PCB design integrating the NEO-D9S.

# <span id="page-23-1"></span>**4.1 Pin assignment**

The pin assignment of the NEO-D9S module is shown in [Figure](#page-23-2) 12. The defined configuration of the PIOs is listed in [Table](#page-23-3) 6.

<span id="page-23-2"></span>

#### **Figure 12: NEO-D9S pin assignment**

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
| 11      | RF_IN      | I   | Active antenna L-band signal input                               |
| 12      | GND        | I   | Ground                                                           |
| 13      | GND        | I   | Ground                                                           |



| Pin no. | Name           | I/O | Description                                                       |
|---------|----------------|-----|-------------------------------------------------------------------|
| 14      | ANT_OFF        | O   | External LNA disable - default active high                        |
| 15      | ANT_DETECT     | I   | Active antenna detect - default active high                       |
| 16      | ANT_SHORT_N    | O   | Active antenna short detect - default active low                  |
| 17      | EXTINT         | I   | External interrupt pin                                            |
| 18      | SDA / SPI CS_N | I/O | I2C data if D_SEL = VCC (or open); SPI chip select if D_SEL = GND |
| 19      | SCL / SPI SLK  | I/O | I2C clock if D_SEL = VCC (or open); SPI clock if D_SEL = GND      |
| 20      | TXD / SPI SDO  | O   | UART1 output if D_SEL = VCC (or open); SPI SDO if D_SEL = GND     |
| 21      | RXD / SPI SDI  | I   | UART1 input if D_SEL = VCC (or open); SPI SDI if D_SEL = GND      |
| 22      | V_BCKP         | I   | Connect to VCC or leave it open                                   |
| 23      | VCC            | I   | Supply voltage                                                    |
| 24      | GND            | I   | Ground                                                            |

**Table 6: NEO-D9S pin assignment**

# <span id="page-24-0"></span>**4.2 Antenna**

An active antenna is mandatory with the NEO-D9S. The NEO-D9S needs to receive L-band signals in order to operate.

- A separate L-band antenna should be used to meet the requirement of +4 dBic patch element gain.
- A suitable ground plane is required for the antenna to achieve good performance for the L-band antenna.
- Location of the antenna is critical for reaching good performance.



**Figure 13: Typical L-band active antenna structure**





#### **Figure 14: Typical recommended separate NEO-D9S and ZED-F9x RF front end and system**

L-band refers to the operating frequency range of 1–2 GHz in the radio spectrum. However in this case we are referring to a corrections receiver that can operate at 1525.0 - 1559.0 MHz. An active antenna is required to provide sufficient low noise gain at the required correction service frequency and ensure any cable loss does not impact the antenna noise figure.

UART2 may be used to provide correction data directly to a high precision GNSS receiver from the u-blox F9 platform. To check whether a specific u-blox F9 product supports correction data output by the NEO-D9S, refer to its Integration manual.

#### **Recommended single L-band antenna required specifications**

| Parameter                      | Specification                                                        |       |
|--------------------------------|----------------------------------------------------------------------|-------|
| Antenna type                   | Active antenna                                                       |       |
|                                | Typical gain                                                         | 30 dB |
| Active antenna recommendations | Maximum gain                                                         | 40 dB |
|                                | Maximum noise figure                                                 | 3 dB  |
| 1<br>L-band antenna gain       | 2<br>4 dBic typical<br>1525 MHz - 1559 MHz (NEO-D9S-00A/NEO-D9S-00B) |       |
| Polarization                   | RHCP                                                                 |       |
| Axial ratio                    | 2 dB max at zenith                                                   |       |
| 3<br>EMI immunity out-of-band  | 30 V/m                                                               |       |

<span id="page-25-0"></span><sup>1</sup> Measured with a ground plane d=150 mm

<span id="page-25-1"></span><sup>2</sup> The recommended gain is important for good performance

<span id="page-25-2"></span><sup>3</sup> Exception L1 and L2 bands +/- 200 MHz, emphasis on cellular bands



| Parameter                  | Specification                        |
|----------------------------|--------------------------------------|
| 4<br>Out-of-band rejection | 40 dB typ (NEO-D9S-00A/NEO-D9S-00B)  |
| ESD circuit protection     | 15 kV human body model air discharge |

**Table 7: Antenna specifications for NEO-D9S modules**

It is not recommended to use a combined antenna due to limitations of combined patch element gain for L-band. However if this is still a consideration the combined required specification is detailed below:

| Combined L1 + L2 + L-band active antenna required specifications |  |
|------------------------------------------------------------------|--|
|------------------------------------------------------------------|--|

| Parameter                          | Specification                                                                         |                |
|------------------------------------|---------------------------------------------------------------------------------------|----------------|
| Antenna type                       |                                                                                       | Active antenna |
|                                    | Typical gain                                                                          | 30 dB          |
| Active antenna recommendations     | Maximum gain                                                                          | 40 dB          |
|                                    | Maximum noise figure                                                                  | 2 dB           |
| 1<br>L1/L-band band antenna gain   | 2<br>4 dBic typ<br>1525 MHz - 1606 MHz (NEO-D9S-00A/NEO-D9S-00B)                      |                |
| 1<br>L2/E5b band antenna gain      | 1197 - 1249 MHz: 2 dBic typ.                                                          |                |
| Polarization                       | RHCP                                                                                  |                |
| Axial ratio                        | 2 dB max at zenith                                                                    |                |
| Phase center variation             | <10 mm over elevation/azimuth                                                         |                |
| 5<br>Group delay variation in-band | 10 ns max at each GNSS system bandwidth. Note:<br>Inter-signal requirement 50 ns max. |                |
| 3<br>EMI immunity out-of-band      | 30 V/m                                                                                |                |
| 5 Rejection<br>4<br>Out-of-band    | 40 dB typ (NEO-D9S-00A/NEO-D9S-00B)                                                   |                |
| ESD circuit protection             | 15 kV human body model air discharge                                                  |                |

**Table 8: Antenna specifications for NEO-D9S modules**

#### **Recommended L-band C/N0 levels**

| Baud rate | Target C/N0 level | Target optimized<br>C/N0 level |
|-----------|-------------------|--------------------------------|
| 600       | 37 dBHz           | 40 dBHz                        |
| 1200      | 40 dBHz           | 43 dBHz                        |
| 2400      | 43 dBHz           | 46 dBHz                        |

**Table 9: C/N0 specifications for NEO-D9S modules**

The antenna system should include filtering to ensure adequate protection from nearby transmitters. Care should be taken in the selection of antennas placed close to cellular or Wi-Fi transmitting antennas.

### <span id="page-26-0"></span>**4.2.1 Antenna bias**

The bias-T inductor must be chosen for multi-band operation, a value of 47 nH ±5% is recommended for the recommended Murata L part. It has a self-resonance frequency of 1 GHz and a high impedance (> 500 Ω) at L-band frequencies.

<span id="page-26-1"></span><sup>4</sup> - 50 MHz from lower and + 50 MHz from upper frequency bandwith limits

<span id="page-26-2"></span><sup>5</sup> GNSS system bandwidths: 1559… 1563 MHz; 1573… 1578 MHz; 1598… 1606 MHz; 1192… 1212 MHz; 1197… 1217 MHz; 1223… 1231 MHz; 1242… 1249 MHz



The recommended bias-T inductor (Murata LQG15HS47NJ02) has a maximum current capacity of 300 mA. Hence the current is limited to 70 mA at 3.3V using an active limiter in the recommended circuit shown in [Figure](#page-27-0) 16 below. A 10 Ω resistor (R2)is provided to measure the current.This resistor power rating must be chosen to ensure reliability in the chosen circuit design.



#### **Figure 15: NEO-D9S antenna bias inductor impedance**

A recommended circuit design for an active antenna bias is shown below. This example shows an external voltage of 3.3 V with current limiting as described above. An ESD protection diode should also be connected to the input as shown.

<span id="page-27-0"></span>

#### **Figure 16: NEO-D9S reference design for antenna bias**

L1: Murata LQG15HS47NJ02 0402 47 N 5% 0.30 A -55/+125 C



#### D1: TYCO, 0.25PF, PESD0402-140 -55/+125C

#### C3: Murata GRM155R61A104KA01 CER X5R 0402 100N 10% 10V

R2: RES THICK FILM CHIP 1206 10R 5% 0.25W

It is recommended to use active current limiting. If active current limiting is not used, the important points covered below need to be taken into account:



#### **Figure 17: NEO-D9S VCC\_RF antenna bias**

The bias-T inductor and current limiting resistor must be selected to be reliable with a short circuit on the antenna feed if no active current limiter is used. Our recommended part has a limit of 300 mA. A part with a higher current capability will be needed if the short circuit current is as described here. This will also be affected by the voltage level of the antenna bias supply due to powerdissipation.Take the current limit capability of the antennabias supply into consideration. In the case where the module supplies the voltage via VCC\_RF, a higher value resistor will be needed to ensure themodule supply inductor is protected.The current should be limited to below 150 mA at the module supply voltage under short circuit conditions. In this case a value of 17 Ω or more is required at a module supply of 3 V to limit short circuit current to 150 mA. The DC resistance of the bias-T inductor is assumed to be 1-2 Ω and the module internal feed inductor is assumed to be 1.2 Ω.

If the VCC\_RF voltage does not match with the supply voltage of the active antenna, use a filtered external supply.

The power dissipation in the resistor and inductor needs to be taken into account based on the supply voltage and short circuit current. The bias-T inductor current capability and the bias resistor value need to be calculated as shown above. The supply voltage for the bias-T and its current capability is part of the calculation.





**Figure 18: NEO-D9S external voltage antenna bias**

# <span id="page-29-0"></span>**4.3 Power supply**

The u-blox NEO-D9S module has two power supply pins: VCC and V\_USB.

# <span id="page-29-1"></span>**4.3.1 VCC: Main supply voltage**

The **VCC** pin is connected to the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude. For this reason, it is important that the supply circuitry be able to support the peak power for a short time (see the applicable data sheet [\[1](#page-50-2)] for specification).

- To reduce peak current during power on, users can employ an LDO that has a built-in current limiter.
- Do not add any series resistance greater than 0.2 Ω to the VCC supply as it will generate input voltage noise due to dynamic current conditions.
- For the NEO-D9S module the equipment must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1.

# <span id="page-29-2"></span>**4.3.2 NEO-D9S power supply**

The NEO-D9S requires a low-noise, low-dropout voltage, and a very low source impedance power supply of 3.3 V typically. No inductors or ferrite beads should be used from LDO to the module VCC pin. The peak currents need to be taken into account for the source supplying the LDO for the module.

A power supply fed by 5 V is shown in the figure below. This example circuit is intended only for the module supply.





#### **Figure 19: NEO-D9S power supply**

# <span id="page-30-0"></span>**4.4 NEO-D9S minimal design**

The minimal electrical circuit for NEO-D9S operation using the UART1 interface is shown below:



#### **Figure 20: Minimal NEO-D9S design**

- It is important to connect V\_USB to ground if USB is not used.
- Connect the power supply to VCC.
- UART2 may be used to provide correction data directly to a high precision GNSS receiver from the u-blox F9 platform. To check whether a specific u-blox F9 product supports correction data output by the NEO-D9S, refer to its Integration manual.

# <span id="page-30-1"></span>**4.5 EOS/ESD precautions**

To avoid overstress damage during production or in the field it is essential to observe strict EOS/ ESD/EMI handling and protection measures.



To prevent overstress damage at the RF\_IN of your receiver, never exceed the maximum input power as specified in the applicable Data sheet [\[1\]](#page-50-2).

When integrating L-band receivers into wireless systems, pay special attention to electromagnetic and voltage susceptibility issues. Wireless systems include components which can produce Electrostatic Discharge (ESD), Electrical Overstress (EOS) and Electro-Magnetic Interference (EMI). CMOS devices are more sensitive to such influences because their failure mechanism is defined by the applied voltage, whereas bipolar semiconductors are more susceptible to thermal overstress. The following design guidelines help in designing robust yet cost-effective solutions.

### <span id="page-31-0"></span>**4.5.1 ESD protection measures**

L-band receivers are sensitive to Electrostatic Discharge (ESD).Special precautions are required when handling. Most defects caused by ESD can be prevented by following strict ESD protection rules for production and handling. When implementing passive antenna patches or external antenna connection points, then additional ESD measures as shown in the figure below can also avoid failures in the field.



**Figure 21: RF ESD precautions**

## <span id="page-31-1"></span>**4.5.2 EOS precautions**

Electrical overstress (EOS) usually describes situations when the maximum input power exceeds the maximum specified ratings. EOS failure can happen if RF emitters are close to a L-band receiver or its antenna. EOS causes damage to the chip structures. If the RF\_IN is damaged by EOS, it is hard to determine whether the chip structures have been damaged by ESD or EOS.

EOS protection measures as shown in the figure below are recommended for any designs combining wireless communication transceivers (e.g. GSM, GPRS) and L-band in the same design or in close proximity.





**Figure 22: Active antenna EOS protection**

## <span id="page-32-0"></span>**4.5.3 Safety precautions**

The NEO-D9S must be supplied by an external limited power source in compliance with the clause 2.5 of the standard IEC 60950-1. In addition to external limited power source, only Separated or Safety Extra-Low Voltage (SELV) circuits are to be connected to the module including interfaces and antennas.

For more information about SELV circuits see section 2.2 in Safety standard IEC 60950-1.

# <span id="page-32-1"></span>**4.6 Electromagnetic interference on I/O lines**

Any I/O signal line with a length greater than approximately 3 mm can act as an antenna and may pick up arbitrary RF signals transferring them as noise into the receiver. This specifically applies to unshielded lines, in which the corresponding GND layer is remote or missing entirely, and lines close to the edges of the printed circuit board.

If, for example, a cellular signal radiates into an unshielded high-impedance line, it is possible to generate noise in the order of volts and not only distort receiver operation but also damage it permanently. Another type of interference can be caused by noise generated at the PIO pins that emits from unshielded I/O lines. Receiver performance may be degraded when this noise is coupled into the L-band antenna.

EMI protection measures are particularly useful when RF emitting devices are placed next to the L-band receiver and/or to minimize the risk of EMI degradation due to self-jamming. An adequate layout with a robust grounding concept is essential in order to protect against EMI.

Intended Use: Inorder tomitigate any performance degradationof a radio equipment underEMC disturbance, system integration shall adopt appropriate EMC design practice and not contain cables over three meters on signal and supply ports.

## <span id="page-32-2"></span>**4.6.1 General notes on interference issues**

Received L-band signal power at the antenna is very low. At the nominal received signal strength (-128 dBm) it is below the thermal noise floor of -111 dBm. Due to this fact, a L-band receiver is susceptible to interference from nearby RF sources of any kind. Two cases can be distinguished:

• Out-of-band interference: Typically any kind of wireless communications system (e.g. LTE, GSM, CDMA, 3G, WLAN, Bluetooth, etc.) may emit its specified maximum transmit power in close proximity to the L-band receiving antenna, especially if such a system is integrated with the L-band receiver. Even at reasonable antenna selectivity, destructive power levels may reach the RF input of the L-band receiver. Also, larger signal interferers may generate intermodulation products inside the L-band receiver front-end that fall into the L-band band and contribute to in-band interference.



• In-band interference: Although the L-band band is kept free from intentional RF signal sources by radio-communications standards, many devices emit RF power into the L-band band at levels much higher than the L-band signal itself. One reason is that the frequency band above 1 GHz is not well regulated with regards to EMI, and even if permitted, signal levels are much higher than L-band signal power. Notably, all types of digital equipment, such as PCs, digital cameras, LCD screens, etc. tend to emit a broad frequency spectrum up to several GHz of frequency. Also wireless transmitters may generate spurious emissions that fall into L-band band.

As an example, GSM uses power levels of up to 2 W (+33 dBm). The absolute maximum power input at the RF input of the L-band receiver can be +15 dBm. The GSM specification allows spurious emissions for GSM transmitters of up to +36 dBm, while the L-band signal is less than -128 dBm. By simply comparing these numbers it is obvious that interference issues must be seriously considered in any design of a L-band receiver. Different design goals may be achieved through different implementations:

- The primary focus is to prevent damaging the receiver from large input signals. Here the Lband performance under interference conditions is not important and suppression of the signal is permitted. It is sufficient to just observe the maximum RF power ratings of all of the components in the RF input path.
- L-band performance must be guaranteed even under interference conditions. In such a case, not only the maximum power ratings of the components in the receiver RF path must be observed. Further, non-linear effects like gain compression, NF degradation (desensitization) and intermodulation must be analyzed.
- Pulsed interference with a low-duty cycle such as GSM may be destructive due to the high peak power levels.

# <span id="page-33-0"></span>**4.6.2 In-band interference mitigation**

With in-band interference, the signal frequency is very close to the L-band frequency. Such interference signals are typically caused by harmonics fromdisplays,micro-controller operation, bus systems, etc. Measures against in-band interference include:

- Maintaining a good grounding concept in the design
- Shielding
- Layout optimization
- Low-pass filtering of noise sources, e.g. digital signal lines
- Remote placement of the L-band antenna, far away from noise sources
- Adding an LTE, CDMA, GSM, WCDMA, BT band-pass filter before antenna

## <span id="page-33-1"></span>**4.6.3 Out-of-band interference**

Out-of-band interference is caused by signal frequencies that are different from the L-band carrier frequency. The main sources are wireless communication systems such as LTE, GSM, CDMA, WCDMA, Wi-Fi, BT, etc.

Measures against out-of-band interference include maintaining a good grounding concept in the design and adding a L-band band-pass filter into the antenna input line to the receiver.

For GSM applications, such as typical handset design, an isolation of approximately 20 dB can be reached with careful placement of the antennas. If this is insufficient, an additional SAW filter is required on the L-band receiver input to block the remaining GSM transmitter energy.



# <span id="page-34-0"></span>**4.7 Layout**

This section details layout and placement requirements of the u-blox D9 correction data receiver.

# <span id="page-34-1"></span>**4.7.1 Placement**

L-band signals at the surface of the Earth are below the thermal noise floor. A very important factor in achieving maximum GNSS performance is the placement of the receiver on the PCB. The placement used may affect RF signal loss from antenna to receiver input and enable interference into the sensitive parts of the receiver chain, including the antenna itself. When defining a GNSS receiver layout, the placement of the antenna with respect to the receiver, as well as grounding, shielding and interference from other digital devices are crucial issues and need to be considered very carefully.

Signal loss on the RF connection from antenna to receiver input must be minimized as much as possible. Hence, the connection to the antenna must be kept as short as possible.

Ensure that RF critical circuits are clearly separated from any other digital circuits on the system board. To achieve this, position the receiver digital part closer to the digital section of the system PCB and have the RF section and antenna placed as far as possible away from the other digital circuits on the board.

A proper GND concept shall be followed: The RF section shall not be subject to noisy digital supply currents running through its GND plane.

## <span id="page-34-2"></span>**4.7.2 Thermal management**

During design-in do not place the receiver near sources of heating or cooling. The receiver oscillator is sensitive to sudden changes in ambient temperature which can adversely impact satellite signal tracking. Sources can include co-located power devices, cooling fans or thermal conduction via the PCB. Take into account the following questions when designing in the receiver.

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?

High temperature drift and air vents can affect the GNSS performance. For best performance, avoid high temperature drift and air vents near the receiver.

## <span id="page-34-3"></span>**4.7.3 Package footprint, copper and paste mask**

Copper and solder mask dimensioning recommendations for the NEO-D9S module packages are provided in this section.

- The module edge pads are 0.8 mm x 0.9 mm. Implement a pad size on your PCB as a copper pad size of 0.8 mm x 1.8 mm. Solder mask for the same pad is 0.9 mm x 1.9 mm. Paste mask for the same pad is 0.8 mm x 2.1 mm.
- These are recommendations only and not specifications. Consider the paste mask outline when defining the minimal distance to the next component. The exact copper, solder and paste mask geometries, distances, stencil thickness and solder paste volumes must be adapted to the specific production processes (e.g. soldering etc.) of the customer.

Refer to the NEO-D9S data sheet [[1\]](#page-50-2) for the mechanical specification.



### **4.7.3.1 Footprint**



**Figure 23: NEO-D9S suggested footprint (i.e. copper mask)**

#### **4.7.3.2 Paste mask**



**Figure 24: NEO-D9S suggested paste mask**

To improve the wetting of the half vias, reduce the amount of solder paste under the module and increase the volume outside of the module by defining the dimensions of the paste mask to form a T-shape (or equivalent) extending beyond the copper mask.

## <span id="page-35-0"></span>**4.7.4 Layout guidance**

The presented layout guidance reduces the risk of performance issues at design level.

### **4.7.4.1 RF In trace**

The RF In trace has to work in the middle L-band frequencies.



For FR-4 PCB material with a dielectric permittivity of for example 4.7, the trace width for the 50 Ω line impedance can be calculated.



#### **Figure 25: Microstrip trace width**

A grounded co-planar RF trace is recommended as it provides the maximum shielding from noise with adequate vias to the ground layer.



**Figure 26: Grounded co-planar RF trace**

The RF trace must be shielded by vias to ground along the entire length of the trace and the NEO-D9S RF\_IN pad should be surrounded by vias as shown in the figure below.





**Figure 27: RF input trace**

The RF\_IN trace on the top layer should be referenced to a suitable ground layer.

#### **4.7.4.2 VCC pad**

The VCC pad for the u-blox D9 correction data receiver needs to have as low an impedance as possible with large vias to the lower power layer of the PCB. The VCC pad needs a large pad and the decoupling capacitor must be placed as close as possible. This is shown in the figure below.



**Figure 28: VCC pad**



# <span id="page-38-0"></span>**4.8 Design guidance**

# <span id="page-38-1"></span>**4.8.1 General considerations**

Check power supply requirements and schematic:

- Is the power supply voltage within the specified range and noise-free?
- If USB is not used, connect the V\_USB pin to ground.
- It is recommended to have a separate LDO for V\_USB that is enabled by the module VCC. This is to comply with the USB self-powered specification.
- If USB is used, is there a 1 uF capacitor right near the V\_USB pin? This is just for the V\_USB pin.
- Is there a 1 uF cap right next to the module VCC pin?
- Connect the power supply to VCC.
- Compare the peak current consumption of the NEO-D9S L-band module with the specification of your power supply.
- L-band receivers require a stable power supply. Avoid series resistance (less than 0.2 Ω) in your power supply line (the line to VCC) to minimize the voltage ripple on VCC. See the NEO-D9S Power [supply](#page-29-0) section in the [Design](#page-23-0) chapter for more information on the power supply requirements.
- All I/O (including UART) must not be pulled high before power ON.
- Any pull ups must be tied to module VCC to ensure they are at the correct state on power ON and OFF.
- Allow all I/O to Float/High impedance (High-Z) when VCC is not applied.

### <span id="page-38-2"></span>**4.8.2 RF front-end circuit options**

It is mandatory that the RF input is fed by an active antenna meeting the requirements for the NEO-D9S.

The first stages of the signal processing chain are crucial to the overall receiver performance.

When an RF input connector is employed this can provide a conduction path for harmful or destructive electrical signals. If this is a likely factor the RF input should be protected accordingly.

#### **Additional points on the RF input**

- What is the expected quality of the signal source (antenna)?
- What is the external active antenna signal power?
- What is the bandwidth and filtering of the external active antenna?
- Does the L-band external antenna meet the recommended +4 dBic patch element gain for the 1525 MHz - 1559 MHz band?

Are destructive RF power levels expected to reach the RF input? Is interference from wireless transmitters expected?

- What are the characteristics of these signals (duty cycle, frequency range, power range, spectral purity)?
- What is the expected L-band performance under interference conditions?

Is there a risk of RF input exposure to excessive ESD stress?

- In the field: Can the user access the antenna connector?
- PCB / system assembly: Is there risk that statically charged parts (e.g. patch antennas) may be discharged through the RF input?

The following subsections provide several options addressing the various questions above:



- In some applications, such as cellular transceivers, interference signals may exceed the maximum power rating of the RF\_IN input. To avoid device destruction use of external input protection is mandatory.
- During assembly of end-user devices which contain passive patch antennas, an ESD discharge may occur during production when pre-charged antennas are soldered to the L-band receiver board. In such cases, use of external protection in front of RF\_IN is mandatory to avoid device destruction.

ESD discharge cannot be avoided during assembly and / or field use. Note that SAW filters are susceptible to ESD damage. To provide additional robustness an ESD protection diode may be placed at the antenna RF connector to GND.

# <span id="page-39-0"></span>**4.8.3 Antenna/RF input**

Check RF input requirements and schematic:

- With the NEO-D9S L-band module, an active antenna meeting our antenna requirements is mandatory to achieve the performance values as written in the NEO-D9S data sheet and with a minimum gain of 20 dB being reached at the module RF\_IN pin.
- The total maximum noise figure including external LNA (or the LNA in the active antenna) should be around 3 dB.
- Ensure active antenna gain is ideally between 30 40 dB gain.
- Make sure the antenna is not placed close to noisy parts of the circuitry and does not face any other noisy elements (for example microcontroller, display).
- ESD protection on the RF input is mandatory.
- Bias-t inductor must be L-band frequency selected
- Ensure RF trace is tuned for 50 Ω to ensure L-band bandwidth

## <span id="page-39-1"></span>**4.8.4 Schematic design**

For a **minimal design** with the NEO-D9S L-band modules, consider the following functions and pins:

- Connect the power supply to VCC.
- V\_USB: If USB is used it is recommended V\_USB is to be powered as per USB self-powered mode specification.
- If USB is not used connect V\_USB to ground.
- Ensure an optimal ground connection to all ground pins of the NEO-D9S L-band module.
- Choose the required serial communication interfaces (UART, USB, SPI or I2C) and connect the appropriate pins to your application.
- Antenna bias is required, see NEO-D9S antenna bias section.

### <span id="page-39-2"></span>**4.8.5 Layout design-in guideline**

- Is the receiver placed away from heat sources?
- Is the receiver placed away from air-cooling sources?
- Is the receiver shielded by a cover/case to prevent the effects of air currents and rapid environmental temperature changes?
- Is the receiver placed as recommended in the [Layout](#page-34-0) and Layout [guidance](#page-35-0)?
- Assure a low serial resistance on the VCC power supply line (choose a line width > 400 um).
- Keep the power supply line as short as possible.
- Add a ground plane underneath the module to reduce interference. This is especially important for the RF input line.
- For improved shielding, add as many vias as possible around the micro strip/co-planar waveguide, around the serial communication lines, underneath the module, etc.



# <span id="page-40-0"></span>**5 Product handling**

# <span id="page-40-1"></span>**5.1 ESD handling precautions**

CAUTION! Risk of electrostatic discharge (ESD) damage. u-blox chips and modules are electrostatic sensitive devices containing highly sensitive electronic circuitry. A discharge of static electricity may damage the device or reduce the life expectancy of the device. To avoid ESD damage, adhere to the standard guidelines for handling ESD devices.

Consider the following:

### **Preventing electrostatic discharge**

- Keep components in their original packages during transport.
- Open the package within an ESD-protected area (EPA), as in [Figure](#page-41-1) 29.
- At a workstation, store components in an EPA.
- PlaceESD sensitive devices inside of shielding packaging or containers when transported outside of an EPA.
- Use protective clothing and proper personnel grounding at all necessary points when touching electrostatic sensitive device or assembly. For instance, wear ESD-safe clothing and shoes and wear an ESD wrist strap connected to a grounded workstation. Use heel straps when standing on conductive floors or dissipating floor mats.
- Hold the devices by the edges and avoid touching component contacts, pins, or circuitry

#### **Product handling**

- When handling RF transceivers and patch antennas, work in an EPA.
- When connecting test equipment or any other electronics to the module (as a standalone or PCBmounted device), the first point of contact must always be between the local ground and the PCB ground.
- Before mounting a ceramic patch antenna, connect the device to ground.
- When handling the RF pin, do not touch any charged capacitors. Be especially careful when handling materials like patch antennas (~10 pF), coaxial cables (~50-80 pF/m), soldering irons, or any other materials that can develop charges.
- If there is any risk of touching an exposed antenna area in a non-ESD protected work area, implement proper ESD protection measures in the design.
- When soldering RF connectors and patch antennas to the receiver's RF pin, use an ESD-safe soldering iron (tip)



<span id="page-41-1"></span>



# <span id="page-41-0"></span>**5.2 Soldering**

### **Soldering paste**

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



**Figure 30: Soldering profile for professional grade NEO-D9S**





#### **Figure 31: Soldering profile for automotive grade NEO-D9S**

Modules **must not** be soldered with a damp heat process.

#### **Optical inspection**

After soldering the module, consider optical inspection.

#### **Cleaning**

Do not clean with water, solvent, or ultrasonic cleaner:

- Cleaning with water will lead to capillary effects where water is absorbed into the gap between the baseboard and the module. The combination of residues of soldering flux and encapsulated water leads to short circuits or resistor-like interconnections between neighboring pads.
- Cleaning with alcohol or other organic solvents can result in soldering flux residues flowing underneath the module, into areas that are not accessible for post-cleaning inspections. The solvent will also damage the sticker and the printed text.
- Ultrasonic cleaning will permanently damage the module, in particular the quartz oscillators.

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

# <span id="page-44-0"></span>**5.3 Tapes**

[Figure](#page-45-2) 32 shows the feed direction and illustrates the orientation of the NEO-D9Ss on the tape:



<span id="page-45-2"></span>

**Figure 32: Orientation of NEO-D9S on the tape**

The dimensions of the tapes for NEO-D9S are specified in [Figure](#page-45-3) 33 (measurements in mm).

<span id="page-45-3"></span>

**Figure 33: NEO-D9S tape dimensions (mm)**

# <span id="page-45-0"></span>**5.4 Reels**

The NEO-D9S receivers are deliverable in quantities of 250 pieces on a reel. The receivers are shipped on reel type B, as specified in the u-blox Package Information Guide [\[3\]](#page-50-3).

# <span id="page-45-1"></span>**5.5 Moisture sensitivity levels**

The moisture sensitivity level (MSL) for NEO-D9S is specified in the table below.



| Package | MSL level                        |
|---------|----------------------------------|
| LCC     | 4 (NEO-D9S-00B), 3 (NEO-D9S-00A) |

**Table 10: MSL level**

For MSL standard see IPC/JEDEC J-STD-020, which can be downloaded from www.jedec.org.

For more information regarding moisture sensitivity levels, labeling, storage and drying, see the u-blox Package Information Guide [\[3\]](#page-50-3).



# <span id="page-47-0"></span>**Appendix**

# <span id="page-47-1"></span>**A Stacked patch antenna**

A typical low cost L1 + L2 + L-band antenna is based on a stacked patch antenna design. This consists of two discrete ceramic patch elements with an L1/ L-band patch above an L2 patch.



**Figure 34: Ceramic stack**

When used in an automotive application, the antenna placement can affect the phase center variation owing to the size and shape of the ground plane coupled with the effects of the adjacent structures. A phase center variation calibration is required to check the actual antenna position. A successful calibration can bemade if the phase variation of a specific antenna is repeatable between samples.

To obtain the best antenna performance in an automotive application, mount the antenna in the center of a conductive car roof without any inclination. The antenna requires good signal levels and as wide a view of the sky as possible. The antenna must not be placed under a dashboard, in the rear view mirror, or on the rear parcel shelf.

An L1 + L2 or L5 + L-band stacked patch antenna must have a good band-pass performance from the patch elements with low attenuation from SAW band-pass filtering. An example of the measured frequency characteristics of a low-cost L1 + L2 + L-band antenna is shown below.







**Figure 35: Low cost L1/L2/L-band antenna band characteristics**

In the above test the L-band antenna patch gain and pass band roll off is not to the required specification and is included purely as an example.

# <span id="page-48-0"></span>**B Glossary**

| Abbreviation | Definition                            |
|--------------|---------------------------------------|
| ANSI         | American National Standards Institute |
| ARP          | Antenna reference point               |
| BeiDou       | Chinese navigation satellite system   |
| BBR          | Battery-backed RAM                    |
| CDMA         | Code-division multiple access         |
| EMC          | Electromagnetic compatibility         |
| EMI          | Electromagnetic interference          |
| EOS          | Electrical overstress                 |
| EPA          | Electrostatic protective area         |
| ESD          | Electrostatic discharge               |
| Galileo      | European navigation satellite system  |
| GLONASS      | Russian navigation satellite system   |
| GND          | Ground                                |





| Abbreviation | Definition                                |
|--------------|-------------------------------------------|
| GNSS         | Global navigation satellite system        |
| GPS          | Global Positioning System                 |
| GSM          | Global System for Mobile Communications   |
| I2C          | Inter-integrated circuit bus              |
| IEC          | International Electrotechnical Commission |
| PCB          | Printed circuit board                     |
| PMP          | Point-to-multipoint transmission          |
| QZSS         | Quasi-Zenith Satellite System             |
| RF           | Radio frequency                           |
| SV           | Space vehicle, a satellite                |
| UBX          | u-blox                                    |



# <span id="page-50-0"></span>**Related documents**

- <span id="page-50-2"></span>**[1]** NEO-D9S-00B Data sheet, UBX-18012996
- NEO-D9S-00A Data sheet, UBX-21008859
- <span id="page-50-1"></span>**[2]** PMP 1.04 Interface description [UBX-21040023](https://www.u-blox.com/docs/UBX-21040023) PMP 1.06 Interface description [UBX-22038891](https://www.u-blox.com/docs/UBX-22038891)
- <span id="page-50-3"></span>**[3]** Packaging information for u-blox chips, modules, and antennas, [UBX-14001652](https://www.u-blox.com/docs/UBX-14001652)
- For regular updates to u-blox documentation and to receive product change notifications please register on our homepage <https://www.u-blox.com>.



# <span id="page-51-0"></span>**Revision history**

| Revision | Date         | Status / comments                                                                                                                                                 |
|----------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01      | 04-July-2019 | NEO-D9S-00B: Objective Specification                                                                                                                              |
| R02      | 17-Dec-2019  | NEO-D9S-00B: Advance Information - V_BCKP pin connect to VCC. I2C, SPI, antenna<br>supervisor, EXTINT, TX-READY, extended TX timeout, software backup mode added. |
| R03      | 04-Feb-2020  | NEO-D9S-00B: Early production information - I2C address changed.                                                                                                  |
| R04      | 19-Feb-2020  | NEO-D9S-00B: Early production information - Tape dimension picture updated, missing<br>tape picture added.                                                        |
| R05      | 13-Oct-2020  | USB interface section update. Add C/N0 specification in antenna section. Add C/N0 levels<br>limits in production testing section                                  |
| R06      | 22-Oct-2021  | NEO-D9S-00A and NEO-D9S-01A: Advance information                                                                                                                  |
| R07      | 24-Jan-2022  | UART2 interface general update. V_BCKP general update.                                                                                                            |
|          |              | NEO-D9S-00B: Production information                                                                                                                               |
|          |              | NEO-D9S-00A: Early production information                                                                                                                         |
| R08      | 05-Jan-2023  | Mechanical specification from section 4.7 moved to Data sheet                                                                                                     |
|          |              | Update for NEO-D9S-00A-01 and NEO-D9S-01A-01                                                                                                                      |
|          |              | Overall text improvement                                                                                                                                          |
| R09      | 26-Feb-2024  | End of life for NEO-D9S-00A-00 with PMP 1.04 FW                                                                                                                   |
|          |              | End of life for NEO-D9S-01A-00 with PMP 1.04 FW                                                                                                                   |
|          |              | End of life for NEO-D9S-01A-01 with PMP 1.06 FW                                                                                                                   |
|          |              | Overall text improvement                                                                                                                                          |



# **Contact**

### **u-blox AG**

Address: Zürcherstrasse 68 8800 Thalwil Switzerland

For further support and contact information, visit us at [www.u-blox.com/support](https://www.u-blox.com/support).