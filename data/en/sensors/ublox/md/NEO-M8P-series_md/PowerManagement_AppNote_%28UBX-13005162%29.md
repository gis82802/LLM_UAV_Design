# **Power Management Considerations for u-blox 7 and M8 GNSS receivers**

**Application Note**

### **Abstract**

This document describes the power management considerations for u-blox 7/M8 module or chipset designs. Low power modes are described with diagrams showing acquisition time vs. estimated power consumption. Where appropriate, differences in performance due to the selection of modes are illustrated.



**www.u-blox.com**

UBX-13005162 - R01





| Document Information |                         |                                                   |  |
|----------------------|-------------------------|---------------------------------------------------|--|
| Title                | Power Management        |                                                   |  |
| Subtitle             |                         | Considerations for u-blox 7 and M8 GNSS receivers |  |
| Document type        | Application Note        |                                                   |  |
| Document number      | UBX-13005162            |                                                   |  |
| Revision and date    | R01                     | 20-Feb-2014                                       |  |
| Document status      | Objective Specification |                                                   |  |
|                      |                         |                                                   |  |

### **Document status explanation**

| Objective Specification      | Document contains target values. Revised and supplementary data will be published later.                 |
|------------------------------|----------------------------------------------------------------------------------------------------------|
| Advance Information          | Document contains data based on early testing. Revised and supplementary data will be published later.   |
| Early Production Information | Document contains data from product verification. Revised and supplementary data may be published later. |
| Production Information       | Document contains the final product specification.                                                       |

### **This document applies to the following products:**

| Name              | Type number            | ROM/FLASH version | PCN reference |
|-------------------|------------------------|-------------------|---------------|
| UBX-G7020-[KT/KA] | UBX-G7020-[KT/KA]-xxx  | all               | N/A           |
| UBX-G7020-CT      | UBX-G7020-CT-xxx       | all               | N/A           |
| EVA-7M-0          | EVA-7M-0-xxx           | all               | N/A           |
| MAX-7C -0         | MAX-7C-0-xxx           | all               | N/A           |
| MAX-7Q-0          | MAX-7Q-0-xxx           | all               | N/A           |
| MAX-7W-0          | MAX-7W-0-xxx           | all               | N/A           |
| NEO-7N-0          | NEO-7N-0-xxx           | all               | N/A           |
| NEO-7M-0          | NEO-7M-0-xxx           | all               | N/A           |
| NEO-7P-0          | NEO-7P-0-xxx           | all               | N/A           |
| PAM-7Q-0          | PAM-7Q-0-xxx           | all               | N/A           |
| UBX-M8030-[KT/KA] | UBX- M8030-[KT/KA]-xxx | all               | N/A           |
| UBX-M8030-CT      | UBX- M8030-CT-xxx      | all               | N/A           |
| MAX-M8C-0         | MAX-M8C-0-xx           | all               | N/A           |
| MAX-M8Q-0         | MAX-M8Q-0-xx           | all               | N/A           |
| MAX-M8W-0         | MAX-M8W-0-xx           | all               | N/A           |
| NEO-M8N-0         | NEO-M8N-0-xx           | all               | N/A           |
| NEO-M8M-0         | NEO-M8M-0-xx           | all               | N/A           |
| NEO-M8Q-0         | NEO-M8Q-0-xx           | all               | N/A           |
| LEA-M8F-0         | LEA-M8F-0-xx           | all               | N/A           |
| LEA-M8S-0         | LEA-M8S-0-xx           | all               | N/A           |
| CAM-M8Q-0         | CAM-M8Q-0-xx           | all               | N/A           |

u-blox reserves all rights to this document and the information contained herein. Products, names, logos and designs described herein may in whole or in part be subject to intellectual property rights. Reproduction, use, modification or disclosure to third parties of this document or any part thereof without the express permission of u-blox is strictly prohibited.

The information contained herein is provided "as is" and u-blox assumes no liability for the use of the information. No warranty, either express or implied, is given, including but not limited, with respect to the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, please visit www.u-blox.com.

Copyright © 2014, u-blox AG

u-blox® is a registered trademark of u-blox Holding AG in the EU and other countries. ARM® is the registered trademark of ARM Limited in the EU and other countries.



<span id="page-2-0"></span>

| Contents3                                        |   |
|--------------------------------------------------|---|
| 1<br>Introduction4                               |   |
| 2<br>Power management options                    | 4 |
| 2.1<br>Hardware options 4                        |   |
| 2.1.1<br>u-blox M8 chips  4                      |   |
| 2.1.2<br>u-blox 7 and M8 modules  4              |   |
| 2.1.3<br>Power optimized circuit 5               |   |
| 2.2<br>Operating modes 6                         |   |
| 2.2.1<br>Continuous Mode  6                      |   |
| 2.2.2<br>Power Save Mode  7                      |   |
| 2.3<br>Operating modes option 9                  |   |
| 2.3.1<br>General considerations using the PSM 9  |   |
| 3<br>Settings and configuration13                |   |
| 3.1<br>Software settings 13                      |   |
| 3.1.1<br>Recommended operating mode settings  13 |   |
| Related documents16                              |   |
| Revision history16                               |   |
| Contact17                                        |   |



# <span id="page-3-0"></span>**1 Introduction**

This application note describes ways of configuring u-blox 7 and M8 GNSS receivers to reduce power consumption while maintaining a high level of performance. These are important design goals for portable systems. u-blox 7 and M8 receivers offer various options for applications with different power requirements by means of its flexible supply voltage and operating mode configuration.

# <span id="page-3-1"></span>**2 Power management options**

# <span id="page-3-2"></span>**2.1 Hardware options**

## <span id="page-3-3"></span>**2.1.1 u-blox M8 chips**

In u-blox M8 chips, internal LDOs generate all the UBX-M8030 internal voltages, thus no external LDOs are required. [Figure 1](#page-3-5) shows the typical supply scheme of the UBX-M8030 Power Management Unit. UBX-M8030 has four separate voltage inputs: Main Supply, I/O supply, Backup Supply and USB Supply.



<span id="page-3-5"></span>

## <span id="page-3-4"></span>**2.1.2 u-blox 7 and M8 modules**

u-blox 7 and M8 positioning modules have up to three power supply pins: For NEO 7 and M8 modules: **VCC**, **V\_BCKP** and **VDD\_USB.** For MAX 7 and M8 modules: **VCC**, **V\_BCKP** and **VCC\_IO.**

The **VCC** pin provides the main supply voltage. During operation, the current drawn by the module can vary by some orders of magnitude, especially if enabling low-power operation modes.



**VCC\_IO** from the host system supplies the digital I/Os. The wide range of VCC\_IO allows seamless interfacing to standard logic voltage levels independent of the **VCC** voltage level. In many applications, the **VCC\_IO** pin is simply connected to the main supply voltage.

**VCC\_IO** supplies all the PIOs, the backup domain, and the clock domain. Thus all the PIOs comply with **VCC\_IO** voltage levels.

The current drawn at **VCC\_IO** depends on the activity and loading of the PIOs plus the crystal or TCXO consumption. When running the firmware from the optional SQI Flash most of the **VCC\_IO** current is consumed by the SQI bus

Without a VCC\_IO supply, the system will remain in reset state.

If there is a power failure on the module supply, the real-time clock (RTC) and battery backed RAM (BBR) are supplied through the **V\_BCKP** pin. Use of valid time and the GNSS orbit data at start-up will improve the GNSS performance, as with hot starts and warm starts. If no backup battery is connected, the module performs a cold start at power up.

- Avoid high resistance on the **V\_BCKP** line: During the switch from main supply to backup supply a short current adjustment peak can cause high voltage drop on the pin with possible malfunctions.
- If no backup supply voltage is available, connect the **V\_BCKP** pin to **VCC**.
- As long as power is supplied to the u-blox M8 module through the **VCC** pin, the backup battery is disconnected from the RTC and the BBR to avoid unnecessary battery drain (see). In this case, **VCC** supplies power to the RTC and BBR.



**Figure 2: Backup battery**

NEO modules have a separate **VDD\_USB** supply but no **VCC\_IO**.

## <span id="page-4-0"></span>**2.1.3 Power optimized circuit**

The lowest power consumption can be achieved by using a chipset design and the following configuration

- 1.4 V supply for the core
- Crystal
- RTC crystal
- UART and DDC interface
- No SQI Flash (ROM only version)
- Passive antenna



The lowest power consumption of any u-blox 7/M8 based module is achieved by MAX-7C/MAX-M8C, which uses ROM, internal DC/DC converter, and crystal.

# <span id="page-5-0"></span>**2.2 Operating modes**

# <span id="page-5-1"></span>**2.2.1 Continuous Mode**

Continuous Mode uses the acquisition engine at full performance resulting in the shortest possible TTFF and the highest sensitivity. It searches for all possible satellites until the almanac is completely downloaded. The receiver then switches to the tracking engine to reduce power consumption.

Thus, a lower tracking current consumption level will be achieved when:

- A valid position is obtained
- The entire almanac has been downloaded
- The ephemeris for each satellite in view is valid
- For best GNSS performance use Continuous Mode.



### <span id="page-5-2"></span>**Figure 3: Current consumption profile**

[Figure 3](#page-5-2) shows the current profile during low power modes.

At cold start, the receiver consumes the most power since the acquisition engine is running and ephemeris download is in progress to obtain initial position fix. In Continuous Mode the receiver then shuts down the acquisition engine and continues to process the signals in track. When new satellite signals are available the search engine is turned back on and new ephemeris are downloaded. Smallest average current consumption is obviously achieved when the update period is long.

In ON/OFF operating mode the receiver shuts down completely between the fixes with the exception of the RTC and Battery Backup RAM powered. This mode provides the lowest average current consumption. In cyclic tracking the minimum current is higher than in ON/OFF operation since parts of the receiver is still running during update period.



# <span id="page-6-0"></span>**2.2.2 Power Save Mode**

u-blox 7 and M8 GNSS receivers include Power Save Mode, which allows reducing the average current consumption in different ways to match the needs of the specific application. This can be set and configured by sending the corresponding UBX messages to the receiver. For more information, see *u-blox M8 Receiver Description including Protocol Specification V15* [\[1\].](#page-15-2)

In Power Save Mode, the supply voltages (**V\_CORE** and **VDD\_IO**) must remain within the operating conditions. The system can shut down an optional external LNA by the **ANT\_ON** signal to optimize the power consumption.

- Using the USB Interface is not recommended with Power Save Mode since the USB standard requires the device to be continuously active. Thus it is not possible to take full advantage of Power Save Mode to reduce current consumption.
- Power Save Mode requires the RTC to be maintained. This can be done by connecting an external RTC crystal or deriving the RTC via the main clock using the "single crystal" feature.
- For ROM/FLASH firmware version 2.01 the Power Save Mode is only available when using GPS-only mode. Power Save Mode is not supported when the receiver is configured for Glonass.
- For more information about supply voltages in Power Save Mode, see the relevant hardware integration manual, as listed in *[Related documents](#page-15-0)*.

Power Save Mode has two modes of operation:

- **Cyclic tracking** operation is used when position fixes are required in short periods of 1 to 10s
- **ON/OFF operation** is used for periods longer than 10s, and can be in the order of minutes, hours or days.

The mode of operation can be configured, and depending on the setting, the receiver demonstrates different behavior: In ON/OFF operation the receiver switches between phases of start-up/navigation and phases with low or almost no system activity. In cyclic tracking the receiver does not shut down completely between fixes, but uses low power tracking instead.

### **2.2.2.1 Long update period – ON/OFF operation**

When the receiver is switched on, it first enters "acquisition" state. If it is able to obtain a valid position fix within the time given by the acquisition timeout, it switches to "tracking" state. Otherwise it enters "inactive for search" state and re-starts after the configured search period (minus a start-up margin). As soon as the receiver gets a valid position fix (one passing the navigation output filters), it enters "tracking" state. Upon entering "tracking" state, the on time is started. Once the on time is over "inactive for update" state is entered and the receiver re-starts according to the configured update grid. If the signal is lost while in "tracking" state, "acquisition" state is entered. If the signal is not found within the acquisition timeout, the receiver enters "inactive for search" state. Otherwise the receiver will re-enter "tracking" state and stay there until the newly started on time is over.





### **Figure 4: ON/OFF operation of the PSM**

### **2.2.2.2 Short update period – cyclic tracking operation**

When the receiver is switched on, it first enters "acquisition" state. If it is able to obtain a position fix within the time given by the acquisition timeout, it switches to "tracking" state. Otherwise, it will enter "inactive for search" state and re-start within the configured search grid. After a valid position fix, "tracking" state is entered and the on time is started. In other words the on time is started with the first valid position fix. Once the on time is over, "POT" state is entered. In "POT" state the receiver continues to output position fixes according to the update period. To have maximum power savings, set the on time to zero. This causes the receiver to enter "POT" state as soon as possible. If the signal becomes weak or is lost during "POT" state, "tracking" state is entered. Once the signal is good again and the newly started on time is over, the receiver will re-enter "POT" state. If the receiver can't get a position fix in the "tracking" state, it enters "acquisition" state. Should the acquisition fail as well, "inactive for search" state is entered.

For more information, consult the *u-blox M8 Receiver Description including Protocol Specification V15* [\[1\].](#page-15-2)







# <span id="page-8-0"></span>**2.3 Operating modes option**

# <span id="page-8-1"></span>**2.3.1 General considerations using the PSM**

As mentioned before, the receiver calculates position fixes at a given period. This period is called the *update period*. Depending on the application, one should first decide if ON/OFF operation or cyclic tracking operation is more suitable. A rule of thumb is that cyclic tracking provides nearly as good performance as Max Performance Mode with a reduction of 60% of power consumption. ON/OFF operation is capable of saving even more power for update periods greater than 30 s, but obviously much fewer position fixes are calculated.

The average current consumption in cyclic tracking mode (1-10 s) is in practice the same regardless of the update period, as the receiver keeps the CPU running between fix calculations.

In ON/OFF mode however, the average current drops significantly when the update period is increased. This is due to the receiver shutting down completely, with the exception of RTC and Battery backup RAM powered.

[Figure 6](#page-8-2) shows the average current consumption of the MAX-M8Q receiver in different low power modes and update periods. PSMCT = Power Save Mode Cyclic Tracking, PSMOO = Power Save Mode ON/OFF.

In a 10s update period it is advantageous from a current consumption point-of-view to use ON/OFF mode instead of cyclic tracking.

<span id="page-8-2"></span>**Figure 6: Average current consumption of a MAX-M8Q receiver in different PSM modes and Update Periods**

[Figure 7](#page-8-3) shows another test result where NEO-M8N and NEO-7M were tested in different urban environments. Again we can see that the longer the update period is, the lower the average current consumption becomes.





<span id="page-8-3"></span>

<sup>0</sup> 1 2 3 4 5 6 7 PSMCT 1s PSMCT 4s PSMCT 7s PSMCT 10s PSMOO 10s PSMOO 30s PSMOO 600s **mA** mA



The 2D r50 error for the same road tests shows that in difficult urban areas, like London or Seoul, the accuracy is slightly degraded.



### **2D r50 error [m]**

### **Figure 8: Average current consumption of NEO-M8N and NEO-7N in urban environments**

The road test plots show that PSM works extremely well in areas with good satellite visibility. The plot on the left is a road test in Zurich (Switzerland) and the plot on the right is from a road test in Korea with multiple short tunnels.



**Figure 9: Road tests in Zurich (left, On-Off mode, update period 15 s) and Korea (right, cyclic tracking, update period 8 s)**

The following plots show PSM results in London downtown and Teheran-ro, Seoul Korea.





**Figure 10: Power Save Mode road test in downtown London (cyclic tracking, 1 s update period)**



**Figure 11: Power Save Mode road test in Teheran-ro, Seoul Korea (On-Off Mode, update period 43 s, on-time 10 s)**





**Figure 12: Power Save Mode road test in Helsinki (1 s cyclic tracking)**



# <span id="page-12-0"></span>**3 Settings and configuration**

# <span id="page-12-1"></span>**3.1 Software settings**

## <span id="page-12-2"></span>**3.1.1 Recommended operating mode settings**

u-blox 7 and M8 products offer the option to change the operating modes via software. The following operating modes can be chosen by using the message CFG-RXM:

- Maximum Performance Mode enables the full capability of u-blox 7 and M8 positioning. Thus it should be used if GPS performance is most important.
- Power Save Mode allows significant reduction in system power consumption with reasonable GPS performance. Cyclic tracking operation is recommended for scenarios with moderate to good signals where position fixes are frequently needed. And ON/OFF operation is recommended for scenarios with strong signals and where position fixes are rarely needed.

For more information, consult the *u-blox M8 Receiver Description including Protocol Specification V15* [\[1\].](#page-15-2)

An example process of configuring a u-blox M8 into PSM using u-Center is described below. First use the UBX-CFG GNSS configuration window and disable Glonass. GPS/SBAS/QZSS can be enabled in PSM.

| Configure - GNSS system configuration      |                          |                              |                                              |                         |                                  |                 | $\begin{array}{c c c c c c} \hline \multicolumn{3}{c }{\mathbf{C}} & \multicolumn{3}{c }{\mathbf{C}} & \multicolumn{3}{c }{\mathbf{X}} \end{array}$ |
|--------------------------------------------|--------------------------|------------------------------|----------------------------------------------|-------------------------|----------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ANT (Antenna Settings)                     |                          |                              | UBX - CFG (Config) - GNSS (GNSS config)      |                         |                                  |                 |                                                                                                                                                     |
| CFG (Configuration)<br>DAT (Datum)         |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| <b>EKF (EKF Settings)</b>                  |                          |                              |                                              |                         | Channels                         |                 |                                                                                                                                                     |
| ESFGWT (Gyro+Wheeltick)                    |                          |                              | GNSS ID configure GNSS name enable           |                         | min<br>max                       | Signals         |                                                                                                                                                     |
| FXN (Fix Now Mode)                         | 0                        | ⊽                            | <b>GPS</b>                                   | ⊽                       | 8<br>255                         |                 |                                                                                                                                                     |
| GNSS (GNSS config)                         | $\mathbf{1}$             | ⊽                            | <b>SBAS</b>                                  | $\overline{\mathbf{v}}$ | $\mathbf 0$<br>3                 |                 |                                                                                                                                                     |
| <b>INF (InfMessages)</b>                   | $\overline{2}$           | п                            | Galileo                                      | г                       | $\overline{0}$<br>$\overline{0}$ |                 |                                                                                                                                                     |
| <b>ITFM (Jamming/Interference Monitor)</b> |                          |                              |                                              | П                       |                                  |                 |                                                                                                                                                     |
| LOGFILTER (Log settings)                   | 3                        | п                            | BeiDou                                       |                         | $\overline{0}$<br>$\overline{0}$ |                 |                                                                                                                                                     |
| MSG (Messages)<br>NAV5 (Navigation 5)      | $\overline{4}$           | п                            | <b>IMES</b>                                  | П                       | $\theta$<br>$\mathbf 0$          |                 |                                                                                                                                                     |
| NAVX5 (Navigation Expert 5)                | 5                        | ⊽                            | QZSS                                         | $\overline{\mathbf{v}}$ | 0<br>3                           |                 |                                                                                                                                                     |
| NMEA (NMEA Protocol)                       | 6                        | ⊽                            | <b>GLONASS</b>                               | п                       | 255<br>4                         |                 |                                                                                                                                                     |
| ODO (Odometer/Low-Speed COG filter)        |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| PM (Power Management)                      |                          | Number of channels available |                                              |                         | 0                                |                 |                                                                                                                                                     |
| PM2 (Extended Power Management)            |                          | Number of channels to use    |                                              |                         | 22                               | $\Box$ Auto set |                                                                                                                                                     |
| PRT (Ports)                                |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| PWR (Power)                                |                          |                              | For specific SBAS configuration use CFG-SBAS |                         |                                  |                 |                                                                                                                                                     |
| RATE (Rates)<br>RINV (Remote Inventory)    |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| RST (Reset)                                |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| RXM (Receiver Manager)                     |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| SBAS (SBAS Settings)                       |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| <b>TMODE</b> (Time Mode)                   |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| TMODE2 (Time Mode 2)                       |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| TP (Timepulse)                             |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| TP5 (Timepulse 5)                          |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| <b>USB</b> (Universal Serial Bus)          |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
|                                            |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |
| m,<br>$\blacktriangleleft$                 | $\overline{\phantom{a}}$ |                              |                                              | Ш                       |                                  |                 | þ                                                                                                                                                   |
| X   issend is Poll   to<br>ā<br>⋒          |                          |                              |                                              |                         |                                  |                 |                                                                                                                                                     |

**Figure 13: GNSS configuration window**



Secondly, use the UBX-CFG PM2 configuration dialog to set the desired operating mode and press "Send". In this example case ON/OFF mode, 10s Update Period.

| Configure - Extended Power Management                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $\begin{array}{c c c c c c c c c c c c c c c c c c c $                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| <b>ANT</b> (Antenna Settings)<br>CFG (Configuration)<br>DAT (Datum)<br><b>EKF (EKF Settings)</b><br>ESFGWT (Gyro+Wheeltick)<br>FXN (Fix Now Mode)<br>GNSS (GNSS config)<br><b>INF (InfMessages)</b><br><b>ITFM (Jamming/Interference Monitor)</b><br>LOGFILTER (Log settings)<br>MSG (Messages)<br>NAV5 (Navigation 5)<br>NAVX5 (Navigation Expert 5)<br>NMEA (NMEA Protocol)<br>ODO (Odometer/Low-Speed COG filter)<br>PM (Power Management)<br>PM2 (Extended Power Management)<br>PRT (Ports)<br>PWR (Power)<br><b>RATE (Rates)</b><br>RINV (Remote Inventory)<br>RST (Reset)<br>RXM (Receiver Manager)<br><b>SBAS (SBAS Settings)</b><br><b>TMODE</b> (Time Mode)<br>TMODE2 (Time Mode 2)<br>TP (Timepulse)<br>TP5 (Timepulse 5) | UBX - CFG (Config) - PM2 (Extended Power Management)<br>Mode of operation<br>C ON/OFF (long update period)<br>C Cyclic tracking (short update period)<br>General settings<br>10<br>Update period [s]<br>10<br>Search period [s]<br>Acquisition timeout [s]<br>0<br>$\overline{2}$<br>On time [s]<br>г<br>Wait for timefix<br>Do not enter 'inactive for search'<br>г<br>state when no fix<br>Update<br>RTC E Eph <b>▽</b><br><b>EXTINT Pin Control</b><br>0 G 1 O<br><b>EXTINT</b><br>EXTINT 'high' keeps awake<br>г.<br>г<br>EXTINT 'low' forces sleep | Ξ |
| <b>USB</b> (Universal Serial Bus)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | ON/OFF operation settings<br>0<br>Grid Offset [s]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |   |
| Ш<br>$\overline{\phantom{a}}$<br>$\mathsf{X} \mid \mathsf{f\!B}$ Send $\mathsf{f\!F}$ Poll $ \mathsf{R}\!\! $<br>⋒                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Peak Current Settings<br>Peak current reduction<br>п<br>Ш<br>$\blacktriangleleft$<br>虛                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |   |

**Figure 14: Power Management Configuration window**

And finally, use the UBX-CFG RXM configuration window to set the power mode to "1 – Power Save Mode". Select the "save configuration" box and press "Send"





**Figure 15: Receiver configuration for PSM**



# <span id="page-15-0"></span>**Related documents**

- <span id="page-15-2"></span>[1] u-blox 7 Receiver Description Including Protocol Specification V14, Docu. No. GPS.G7-SW-12001
- [2] u-blox M8 Receiver Description Including Protocol Specification V15, Docu. No. UBX-13002887
- [3] UBX-G7020 Hardware Integration Manual, Docu. No UBX-13004144
- [4] EVA-7M Hardware Integration Manual, Docu. No. UBX-12003235
- [5] MAX7-NEO7 Hardware Integration Manual, Docu. No. UBX-13003704
- [6] PAM-7Q Hardware Integration Manual, Docu. No. UBX-13003143
- [7] UBX-M8030 Hardware Integration Manual, Docu. No. UBX-13001708
- [8] CAM-M8Q Hardware Integration Manual, Docu. No. UBX-14000014
- [9] MAX-M8 Hardware Integration Manual, Docu. No. UBX-13004876
- [10] NEO-M8 Hardware Integration Manual, Docu. No. UBX-13003557

For regular updates to u-blox documentation and to receive product change notifications, register on our homepage [\(http://www.u-blox.com\)](http://www.u-blox.ch/).

# <span id="page-15-1"></span>**Revision history**

| Revision | Date        | Name | Status / Comments |
|----------|-------------|------|-------------------|
| R01      | 20-Feb-2014 | kkai | Initial release   |



# <span id="page-16-0"></span>**Contact**

For complete contact information visit us at [www.u-blox.com](http://www.u-blox.com/)

### **u-blox Offices**

### **North, Central and South America**

### **u-blox America, Inc.**

| Phone:  | +1 703 483 3180    |
|---------|--------------------|
| E-mail: | info_us@u-blox.com |

### **Regional Office West Coast:**

Phone: +1 408 573 3640 E-mail: [info\\_us@u-blox.com](mailto:info_us@u-blox.com)

### **Technical Support:**

| Phone:  | +1 703 483 3185       |
|---------|-----------------------|
| E-mail: | support_us@u-blox.com |

### **Headquarters Europe, Middle East, Africa**

### **u-blox AG**

| Phone:   | +41 44 722 74 44   |
|----------|--------------------|
| E-mail:  | info@u-blox.com    |
| Support: | support@u-blox.com |

### **Asia, Australia, Pacific**

### **u-blox Singapore Pte. Ltd.**

| Phone:   | +65 6734 3811         |
|----------|-----------------------|
| E-mail:  | info_ap@u-blox.com    |
| Support: | support_ap@u-blox.com |

#### **Regional Office Australia:**

Phone: +61 2 8448 2016 E-mail: info\_anz@u-blox.com Support: support\_ap@u-blox.com

### **Regional Office China (Beijing):**

Phone: +86 10 68 133 545 E-mail: info\_cn@u-blox.com Support: support\_cn@u-blox.com

### **Regional Office China (Shenzhen):**

Phone: +86 755 8627 1083 E-mail: info\_cn@u-blox.com Support: support\_cn@u-blox.com

#### **Regional Office India:**

Phone: +91 959 1302 450 E-mail: info\_in@u-blox.com

Support: support\_in@u-blox.com **Regional Office Japan:**

Phone: +81 3 5775 3850 E-mail: info\_jp@u-blox.com Support: support\_jp@u-blox.com

#### **Regional Office Korea:**

Phone: +82 2 542 0861 E-mail: info\_kr@u-blox.com Support: support\_kr@u-blox.com

#### **Regional Office Taiwan:**

Phone: +886 2 2657 1090 E-mail: info\_tw@u-blox.com Support: support\_tw@u-blox.com