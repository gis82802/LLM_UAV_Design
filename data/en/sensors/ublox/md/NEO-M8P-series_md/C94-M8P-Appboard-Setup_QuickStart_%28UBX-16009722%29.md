#### **C94-M8P Application Board Setup Guide**

locate, communicate, accelerate



## **C94-M8P Board Connections and Interfaces**



- J1: RS232 UART M8P/Radio
- J2: USB M8P
- J3: External battery / DC connector
- J6: Debugger interface for radio module
- J8: UART & GNSS features
  - Geofence and RTK status
  - Interface to e.g. u-blox C027
- J9: Indicator LEDs



## **Setting up the C94-M8P**

Two C94-M8P boards – the "Base" and the "Rover" – need to be set up:

- 1. Connect the UHF whip antenna to the SMA connector "UHF"
- 2. Connect the GNSS patch antenna to the SMA connector "GNSS"
- 3. Connect the USB port on the board to a PC (for power and configuration)





## **Preparing to Configure the C94-M8P**

To configure your C94-M8P kit you need to first:

• Download the latest u-center from <https://www.u-blox.com/en/product/u-center-windows>



# **Updating firmware on C94-M8P**

Before starting the evaluation, check that the application boards are using the latest firmware (currently HPG 1.40). Information on the latest firmware is published on the u-blox web site. To update the firmware, follow the steps described in the u-center User Guide, chapter 8.1, Firmware update.

See<https://www.u-blox.com/en/product/u-center-windows>.

- All the changes in configuration are lost when application boards are updated. The Base and Rover must be re-configured after updating.
- Do not have more than one application board connected to your computer while updating.



## **Configuring the Base Station**

*The two boards are identical. Select one board to act as a "Base Station".* 

*The next slides will guide you through the steps needed to configure the Base Station*

There are three steps to configure the Base Station:

- 1. Set the position, by having the Base Station do one of the following:
  - a) survey-in its coordinates
  - b) be configured with pre-surveyed coordinates
- 2. Set-up the port for the Radio Link for Port configuration
- 3. Select RTCM messages for transmission



# **Step 1 – The Base Station Coordinates**

#### Use **UBX-CFG-TMODE3** to:

- Begin a self survey
  - Use, for example, 5 minutes and 2 meters as targets.
  - With a good antenna in a friendly multipath environment you can reach 1 meter with a 10-15 min observation time.
- Or, provide a fixed position estimate





## **Step 1 – The Base Station Coordinates**



## **Step 2 – Base Station Radio Link**

• Use UBX-CFG-PRT to specify that only RTCM3 data is output on UART1.

| Messages - UBX - CFG (Config) - PRT (Ports)                                                                                                                                                                                              |                                                   |                                                                                         | $\Sigma$<br>$\Box$<br>$\qquad \qquad \blacksquare$ |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------|
| E-RTCM3<br>白 UBX<br>릐<br>由 ACK (Acknowledge)<br>向 AID (GPS Aiding)<br>□ CFG (Config)<br>- ANT (Antenna Settings)<br>BATCH (Batch mode output)<br>CFG (Configuration)<br>--- DAT (Datum)<br>DGNSS (Differential GNSS configuratic         | Target<br>Protocol in<br>Protocol out<br>Baudrate | UBX - CFG (Config) - PRT (Ports)<br>1 - UART1<br>  none <br>$ 5 - R$ TCM3<br>19200<br>▼ | 티                                                  |
| DOSC (Disciplined Oscillator)<br>DYNSEED (Dynamic Seed)<br>- FKF (FKF Settings)<br>m.<br>-1<br>$\mathbf{X}$   and $\mathbb{R}$   $\mathbb{R}$   $\mathbb{R}$   $\mathbb{E}$   $\mathbb{E}$   $\mathbb{E}$   $\mathbb{E}$  <br>$\bigcirc$ |                                                   |                                                                                         |                                                    |



## **Step 3 – Selecting RTCM messages**

- Use UBX-CFG-MSG to specify that these three RTCM3 messages are output on UART1.
  - 1005 (Station coordinates)
  - 1077 (GPS observations), and
  - 1087 (GLONASS observations)
  - 1230 (GLONASS code-phase biases)

| UBX - CFG (Config) - MSG (Messages) |                                           | UBX - CFG (Config) - MSG (Messages) |                         | UBX - CFG (Config) - MSG (Messages) |                         | UBX - CFG (Config) - MSG (Messages) |                                            |
|-------------------------------------|-------------------------------------------|-------------------------------------|-------------------------|-------------------------------------|-------------------------|-------------------------------------|--------------------------------------------|
| Message                             | $\vert \cdot \vert$<br>F5-05 RTCM3.2 1005 | Message                             | F5-4D RTCM3.2 1077<br>▼ | Message                             | F5-57 RTCM3.2 1087<br>− | Message                             | F5-E6 RTCM3.2 1230<br>$\blacktriangledown$ |
| I <sub>2C</sub>                     | 0 <br>$\Box$ On .                         | I <sub>2C</sub>                     | $\sqsupset$ On.<br>ю    | I <sub>2C</sub>                     | $\Box$ On $\Box$ 0      | 12C                                 | $\Box$ On $\Box$                           |
| UART1                               | $\overline{V}$ On                         | UART1                               | $\overline{V}$ On       | UART1                               | $\overline{v}$ On 1     | UART1                               | $\overline{M}$ On 10                       |
| UART2                               | $\Box$ On $\ket{0}$                       | UART2                               | 10<br>$\Box$ On $\Box$  | UART <sub>2</sub>                   | $\Box$ On $\Box$        | UART2                               | $\Box$ On $\Box$                           |
| <b>USB</b>                          | $\mathbf{10}$<br>$\square$ On             | <b>USB</b>                          | $\Box$ On<br>10         | USB                                 | $\Box$ On $\Box$        | USB                                 | $\Box$ On $\Box$                           |
| SPI                                 | $\Box$ On<br>$ 0\rangle$                  | SPI                                 | $\Box$ On<br>10.        | SPI                                 | $\Box$ On $\Box$        | SPI                                 | $\Box$ On $\Box$                           |
| SDCard                              | $\sqsupset$ On .<br>-10                   | SDCard                              | $\sqsupset$ On .<br>10  | SDCard                              | $\Box$ On $ 0\rangle$   | SDCard                              | $\Box$ On $\Box$                           |
|                                     |                                           |                                     |                         |                                     |                         |                                     |                                            |

For a GPS/BeiDou setup or moving baseline applications, refer to the User Guide ([UBX-15031066](https://www.u-blox.com/sites/default/files/C94-M8P-AppBoard_UserGuide_(UBX-15031066).pdf)).



### **Rover Setup Overview**

- Steps needed to set up the Rover
  - 1. Configure radio link

*A Rover that receives RTCM messages will automatically go into RTK operational mode, and no further configurations are needed.*



## **Step 1 – Rover end Radio Link**

• Use UBX-CFG-PRT to ensure that UART1 is set up to receive RTCM3 corrections, and that no data is sent out (Protocol out: "none").

| Messages - UBX - CFG (Config) - PRT (Ports)                                                                                                                                                                    |                          | $\Box$ math>                                             |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|----------------------------------------------------------|--|
| 田· NMEA<br>向·RTCM3<br>E<br>' ⊟ · UBX<br>向 ACK (Acknowledge)<br>□ AID (GPS Aiding)<br>□ CFG (Config)                                                                                                            | Target<br>Protocol in    | UBX - CFG (Config) - PRT (Ports)<br>1 - UART1<br>5-RTCM3 |  |
| - ANT (Antenna Settings)<br>BATCH (Batch mode output)<br>CFG (Configuration)<br>-- DAT (Datum)<br>DGNSS (Differential GNSS configuration<br>DOSC (Disciplined Oscillator)<br>DYNSEED (Dynamic Seed).<br>m<br>∢ | Protocol out<br>Baudrate | none <br>19200<br>▼                                      |  |
| X   1 Send APPoll &   6   6   1   1   1<br>A.                                                                                                                                                                  |                          |                                                          |  |



## **Rover Operation**

- A Rover that receives RTCM corrections will automatically apply these and will:
  - 1. Immediately go into an RTK FLOAT mode
  - 2. Go into RTK FIXED mode once it has resolved the carrier ambiguities





## **Important Note on Antennas**

- RTK technology depends on continuous carrier phase tracking, and therefore it is most important that:
  - Rover and Base antennas use ground planes
    - The roof of a car can serve as an excellent ground plane when the patch antenna is placed in the middle of the roof
  - Base antennas are placed in unobstructed environments
    - Also rover antenna placement options should be carefully examined for each application
- Working in difficult environments and/or without ground planes will make convergence times long
- See White Paper *"Centimeter Navigation with Low Cost Antennas"* (UBX-16010559) published on the u-blox website for more information





### **Notes on Usage**

The C94-M8P kit contains **two boards** configured to **work as a pair**



• The default radio configuration supports one Base station transmitting to one Rover, and no other Base stations must be transmitting in the area. For other setups, please refer to the User Guide.



## **Notes on the LEDs**



- Blue LED is blinking when there is a GNSS position fix (TIMEPULSE)
  - If there is no GNSS fix, the LED will light up without flashing
- Green LED indicates the RTK status.
  - LED flashes in float mode and stays on in fix mode.
  - The LED is off when there is no RTK fix.



## **More Information**

- Product website:<https://www.u-blox.com/en/product/c94-m8p>
- C94-M8P User Guide (UBX-15031066)
  - C94-M8P-1-10/11 for China (433 MHz)
  - C94-M8P-2-10 /11for USA and Canada (915 MHz)
  - C94-M8P-3-10/11 for Europe (433 MHz)
  - C94-M8P-4-10/11 for Japan (920 Mhz)
- Note that the connectors differ from the older -00 variants. Please refer to the last two slides for more connector information.



## **C94-M8P-B Board Connections and Interfaces**



- J1: RS232 UART M8P/Radio
- J2: USB M8P
- J3: External battery / DC connector
- J4: UART interface
- J6: Debugger interface for radio module
- J8:Test & Production interface
- J9: Geofence and RTK status



## **C94-M8P-B Notes on the LEDs**



- Red LED blinking when the radio module is transmitting
- Green LED blinking when radio module ready to receive and on when link established

- Blue LED blinking when there is a GNSS position fix (TIMEPULSE)
- Yellow LED indicates RTK status:
  - blinking indicates Float
  - on indicates Fixed ambiguity states

