

# **Windows Drivers**

## **u-blox GNSS drivers for Microsoft Windows systems**

**Application Note**

**Abstract**

This document describes the installation and use of u-blox GNSS drivers for the Windows operating system to use with u-blox GNSS receivers.

**www.u-blox.com**

UBX-19005821 - R01





## **Document Information**

| Title                  | Windows Drivers                                   |             |
|------------------------|---------------------------------------------------|-------------|
| Subtitle               | u-blox GNSS drivers for Microsoft Windows systems |             |
| Document type          | Application Note                                  |             |
| Document number        | UBX-19005821                                      |             |
| Revision and date      | R01                                               | 16-Apr-2019 |
| Disclosure restriction | Production Information                            |             |

u-blox reserves all rights to this document and the information contained herein. Products, names, logos and designs described herein may in whole or in part be subject to intellectual property rights. Reproduction, use, modification or disclosure to third parties of this document or any part thereof without the express permission of u-blox is strictly prohibited.

The informationcontainedhereinis provided "as is" and u-blox assumesno liability for the use of the information. Nowarranty, either express or implied, is given with respect to, including but not limited to, the accuracy, correctness, reliability and fitness for a particular purpose of the information. This document may be revised by u-blox at any time. For most recent documents, please visit www.u blox.com.

Copyright © 2019, u-blox AG.

u-blox is a registered trademark of u-blox Holding AG in the EU and other countries.

UBX-19005821 - R01 Page 2 of 28 Production Information



## **Contents**

| 1 Introduction4                                                                |    |
|--------------------------------------------------------------------------------|----|
| 1.1 Scope4                                                                     |    |
| 2 GNSS<br>drivers<br>for<br>Windows<br>105                                     |    |
| 2.1 u-blox universal GNSS driver for Windows 10 5                              |    |
| 2.1.1 Universal GNSS driver architecture6                                      |    |
| 2.2 Microsoft CDC-ACM driver for Windows 10 7                                  |    |
| 3 u-blox<br>GNSS<br>drivers<br>for<br>Windows<br>7<br>and<br>Windows<br>89     |    |
| 3.1 u-blox CDC-ACM driver for Windows 7 and Windows 8 9                        |    |
| 4 GNSS<br>driver<br>selection<br>for<br>u-blox<br>receivers10                  |    |
| 5 Installing<br>and<br>uninstalling<br>drivers                                 | 11 |
| 5.1 Installing/uninstalling drivers on Windows 10 11                           |    |
| 5.1.1 Getting the Microsoft default CDC-ACM driver for Windows 10 11           |    |
| 5.1.2 Getting the u-blox Universal GNSS driver for Windows 1011                |    |
| 5.1.3 Installing the u-blox Universal GNSS driver with the setup file12        |    |
| 5.1.4 Uninstalling the u-blox Universal GNSS driver 14                         |    |
| 5.1.5 Uninstalling the legacy Sensor driver from Windows 10 15                 |    |
| 5.1.6 Uninstalling the legacy VCP driver from Windows 10 16                    |    |
| 5.2 Installing/uninstalling drivers on Windows 7 and 8.x 18                    |    |
| 5.2.1 Getting the u-blox CDC-ACM driver for Windows 7 and Windows 8.x18        |    |
| 5.2.2 Uninstalling the u-blox CDC-ACM driver from Windows 7 and Windows 8.x 20 |    |
| 5.2.3 Uninstalling the legacy sensor driver from Windows 7 and Windows 8.x21   |    |
| 5.2.4 Uninstalling the legacy VCP driver from Windows 7 and Windows 8.x 22     |    |
| Related<br>documents                                                           | 26 |
| Revision<br>history27                                                          |    |



# <span id="page-3-0"></span>**1 Introduction**

## <span id="page-3-1"></span>**1.1 Scope**

This application note provides a comprehensive reference for customers integrating a u-blox GNSS (Global Navigation Satellite System) receiver into a Windows-operating system. u-blox and Microsoft provide USB (Universal Serial Bus) drivers to speed up the integration of u-blox GNSS products into customer's portable devices.



# <span id="page-4-0"></span>**2 GNSS drivers for Windows 10**

This section describes the drivers for the Windows 10 operating system available from u-blox and Microsoft.

### <span id="page-4-1"></span>**2.1 u-blox universal GNSS driver for Windows 10**

In Windows 10, Microsoft has introduced the new Universal GNSS driver model for GNSS driver interfaces. This driver model enabled u-blox to build a universal GNSS driver that runs on Windows 10 Intel platforms.

Modern drivers should aim to comply with Microsoft's four design principles of Declarative, Componentized, Hardware Supported Application and Universal (D/C/H/U). The u-blox GNSS driver uses the UMDF (User Mode Driver Framework) 2.0 model and complies with the D/C/H principles.

This driver supports applications that use the Windows 10 location service. This new location service does not support the sensor platform, thus, existing sensor platform applications will not work with this driver.

For more information on Sensor and Location platform of Windows, visit [Introduction](https://docs.microsoft.com/en-us/windows/desktop/SensorsAPI/introduction-to-the-sensor-and-location-platform-in-windows) to the Sensor and Location Platform in [Windows](https://docs.microsoft.com/en-us/windows/desktop/SensorsAPI/introduction-to-the-sensor-and-location-platform-in-windows)





**Figure 1: Standard driver application**

### <span id="page-5-0"></span>**2.1.1 Universal GNSS driver architecture**

The following high-level component block diagram from [Microsoft](https://docs.microsoft.com/en-us/windows-hardware/drivers/gnss/gnss-driver-architecture) shows the architectural layers of the various components of Universal GNSS UMDF 2.0 driver architecture and I/O considerations depicting how the GNSS UMDF 2.0 driver integrates with the Windows 10 platform.





**Figure 2: Universal GNSS driver architecture**

For more information about the Universal GNSS driver architecture, visit [Microsoft](https://docs.microsoft.com/en-us/windows-hardware/drivers/gnss/gnss-driver-architecture) docs [page.](https://docs.microsoft.com/en-us/windows-hardware/drivers/gnss/gnss-driver-architecture)

## <span id="page-6-0"></span>**2.2 Microsoft CDC-ACM driver for Windows 10**

Windows 10 provides support as standard for USB to COM (CDC-ACM) straight out of the box. As Microsoft CDC (Communication Device Class)-ACM (Abstract Control Model) driver is the delivered driver, it does not need to be downloaded from Windows Update. The first time a USB device is connected, and without need of an Internet connection, the CDC-ACM driver will load automatically. Applications can then access the COM port and directly communicate with u-blox receivers as defined in the Receiver Description. See the u-blox 8/M8 Receiver Description and Protocol Specification [[2](#page-25-1)]

Only supports Windows 10.





| <b>Standard Applications (COM Port)</b>                                                                                                                                                                               |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| <b>E</b> Windows 10<br>$-$ - - - - - - - - - - - - - - - - - - -<br>i indonezia<br>1999 - Angola Amerika eta Luza<br>1991 - Angola Maria eta Luza<br><b>RANGE PASSAGERING</b><br>TAUTHORITA<br>接 (名)<br>Harry Charles |  |
| Microsoft <b>CDC-ACM</b>                                                                                                                                                                                              |  |
| le)e                                                                                                                                                                                                                  |  |
| <b>TOblex</b><br>EVK-MBN<br><b>U-Nov Att (2NSS Everlation Ay)</b><br>an abuddha XI                                                                                                                                    |  |

**Figure 3: Standard driver application**

The u-blox Universal GNSS driver and the Microsoft CDC-ACM driver cannot be used at the same time in the same machine.



# <span id="page-8-0"></span>**3 u-blox GNSS drivers for Windows 7 and Windows 8**

This section explains about the available drivers for Windows 7 and 8 operating system from u-blox.

### <span id="page-8-1"></span>**3.1 u-blox CDC-ACM driver for Windows 7 and Windows 8**

USB CDC-ACM driver emulates UART interface serial ports over USB. This is the only Windows USB driver solution from u-blox that is developed in Kernel Mode Driver Framework (KMDF).

The main purpose of this driver is to evaluate u-blox receivers with u-center and to integrate devices with custom applications accessing the receiver directly over COM port.

Only supports Windows XP up to Windows 8.1.



**Figure 4: Standard driver application**



## <span id="page-9-0"></span>**4 GNSS driver selection for u-blox receivers**

The table below summarizes which driver to use for which use-case in specific Windows operating system versions.

| Windows Versions | GNSS developer (engineer)/<br>User application               | Customer Specific Product Windows Location Framework/<br>User application      |
|------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------|
| 7                | CDC-ACM (u-blox)/u-center                                    | N/A                                                                            |
| 8.x              | CDC-ACM (u-blox)/u-center                                    | N/A                                                                            |
| 10               | CDC-ACM (Windows)/u-center<br>Windows 10 preinstalled driver | Universal GNSS Driver (u-blox)/Universal Windows Platform<br>GNSS Applications |



## <span id="page-10-0"></span>**5 Installing and uninstalling drivers**

### <span id="page-10-1"></span>**5.1 Installing/uninstalling drivers on Windows 10**

This section explains the procedure to install and uninstall u-blox GNSS drivers on the Windows 10 operating system.

### <span id="page-10-2"></span>**5.1.1 Getting the Microsoft default CDC-ACM driver for Windows 10**

As the Microsoft CDC-ACM driver is the the delivered driver, it does not need to be downloaded from Windows Update. The first time a USB device is connected, and without need of an Internet connection, the CDC-ACM driver will load automatically.

When the Windows 10 delivered CDC-ACM driver is loaded, the u-blox device appears in the device manager with the name "USB Serial Device (COMx)"



**Figure 5: Loaded CDC-ACM driver in Windows 10**

### <span id="page-10-3"></span>**5.1.2 Getting the u-blox Universal GNSS driver for Windows 10**

To get the u-blox Universal GNSS driver from the Windows Update, follow the instructions below:

- Inform your u-blox sales contact that you would like to evaluate the Universal GNSS driver for Windows 10. See the Contacts section at the end of this document for more information on contacting u-blox.
- Install the received u-blox Universal GNSS driver to the desired device (see [Installing](#page-11-0) the u-blox [Universal](#page-11-0) GNSS driver with the setup file)
- Once the functionality of the driver has been accepted, request to add the product's Computer Hardware ID (CHID) to the Windows Update Universal GNSS driver products list by providing the following information:
  - CHID (Computer Hardware ID).
  - Make and Model of the product.
- Once the request is accepted, the CHID will be added to Windows Update by u-blox.
- Restart the device with an Internet connection to get the Universal GNSS driver from the Windows Update.



### <span id="page-11-0"></span>**5.1.3 Installing the u-blox Universal GNSS driver with the setup file**

This section explains the installation of the u-blox Universal GNSS Driver with the internally provided setup file. This is only be needed to evaluate and test before requesting for the deployment to the Windows Update.

- Open the folder for desired system type, i.e., x64 or x86.
- Right click on the INF file named "ubloxGnssUsb" and click "Install".



**Figure 6: Installing with the setup file**

- INF default installation window will pop-up to ask for the confirmation, click "Yes".
- The installation of the Universal GNSS Driver is now finished and you can click "OK" to quit the installer.



**Figure 7: Universal GNSS driver installed**

- Now connect a u-blox GNSS receiver to any USB port.
- The installed driver appears in the Device Manager as in the figure below:



**Figure 8: Device Manager**



• The Location service from "Settings->Privacy->Location" should be on to use the location of the device for applications i.e., Microsoft Maps.

| Settings                      |                                                                                                                                             | ×<br>□                                                        |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| દ્રે છે.<br>Home              | Location                                                                                                                                    |                                                               |
| Q<br>Find a setting           | Location                                                                                                                                    | Know your privacy options                                     |
| Privacy                       | If location is on, each person using this device can choose their<br>own location settings.                                                 | Learn how this setting impacts your<br>privacy.<br>Learn more |
| Α<br>General                  | Location for this device is on                                                                                                              |                                                               |
| ሖ.<br>Location                | Change                                                                                                                                      | Have a question?<br>Get help                                  |
| ි Camera                      | If the location service is on, Windows, apps, and services can use<br>your location, but you can still turn off location for specific apps. | Make Windows better.                                          |
| ⊕<br>Microphone               | Location service                                                                                                                            | <b>Give us feedback</b>                                       |
| Notifications<br>∟⊥           | $\bullet$ On                                                                                                                                |                                                               |
| Speech, inking, & typing<br>阻 | If an app is using your location, you'll see this icon: $\odot$                                                                             |                                                               |
| <b>RE</b> Account info        | Default location                                                                                                                            |                                                               |
| ρR<br>Contacts                | Windows, apps, and services can use this when we can't detect a<br>more exact location on this PC.                                          |                                                               |
| ▥<br>Calendar                 | Set default                                                                                                                                 |                                                               |
| O<br>Call history             |                                                                                                                                             |                                                               |
| $\square$ Email               | Location history                                                                                                                            |                                                               |
| 闓<br>Tasks                    | If location is on, your location history is stored for a limited time on<br>the device, and can be used by apps that use your location.     |                                                               |
| Messaging<br>◡                | Clear history on this device                                                                                                                |                                                               |
| 'A'<br>Radios                 | Clear                                                                                                                                       |                                                               |
| Other devices<br>石            | Learn more about location settings                                                                                                          |                                                               |
| Feedback & diagnostics<br>لہؤ | Manage my location info that's stored in the cloud                                                                                          |                                                               |
| Background apps               | <b>Privacy Statement</b>                                                                                                                    |                                                               |

**Figure 9: Location service Dialog Windows 10**





**Figure 10: Maps with Location service**

### <span id="page-13-0"></span>**5.1.4 Uninstalling the u-blox Universal GNSS driver**

To uninstall the manually installed u-blox Universal GNSS driver from the device, follow the instructions below:

- Open the Device Manager and right click on "Sensors->u-blox Universal GNSS".
- From the menu window, click "Uninstall device".







• From the pop-up Uninstall device window, select the "Delete the driver software for this device" option.



**Figure 12: Selection to delete all the driver files for the device**

- Click "Uninstall".
- A System Settings Change pop-up window will appear to ask if you want to restart. Click "Yes" to restart and remove the device driver.



- **Figure 13: Restart the computer to remove the device driver**
- Open the Device Manager to check that the Universal GNSS driver has been properly uninstalled.

| Device Manager                                    | □ | X |
|---------------------------------------------------|---|---|
| File Action View<br>Help                          |   |   |
| $? \Box$<br>$\Rightarrow$<br>۱LC<br>¢<br>ार       |   |   |
| <b>A</b> FI-ESP-LT-033<br>◡                       |   |   |
| Audio inputs and outputs<br>$\rightarrow$         |   |   |
| <b>Batteries</b><br>$\mathcal{L}$                 |   |   |
| <b>8</b> Bluetooth<br>$\mathcal{P}$               |   |   |
| Computer                                          |   |   |
| <b>ControlVault Device</b>                        |   |   |
| <b>Disk drives</b>                                |   |   |
| <b>Display adapters</b>                           |   |   |
| Firmware                                          |   |   |
| Human Interface Devices<br>$\rightarrow$          |   |   |
| in Imaging devices<br>$\rightarrow$               |   |   |
| Intel(R) Dynamic Platform and Thermal Framework   |   |   |
| $\angle$ $\equiv$ Keyboards                       |   |   |
| > Memory technology devices                       |   |   |
| Mice and other pointing devices<br>Ш              |   |   |
| <b>Monitors</b>                                   |   |   |
| Network adapters<br>$\mathcal{P}$                 |   |   |
| Ports (COM & LPT)<br>₩<br>$\rightarrow$           |   |   |
| <b>Fill Print queues</b><br>$\mathcal{L}$         |   |   |
| Processors                                        |   |   |
| <b>Security devices</b>                           |   |   |
| Smart card readers<br>$\mathcal{L}$               |   |   |
| Software devices<br>$\rightarrow$                 |   |   |
| i Sound, video and game controllers               |   |   |
| Storage controllers<br>$\rightarrow$              |   |   |
| > System devices                                  |   |   |
| Universal Serial Bus controllers<br>$\rightarrow$ |   |   |
|                                                   |   |   |
|                                                   |   |   |
|                                                   |   |   |
|                                                   |   |   |
|                                                   |   |   |
|                                                   |   |   |
|                                                   |   |   |
|                                                   |   |   |

**Figure 14: Check Device Manager to check that the Universal GNSS device driver is uninstalled successfully**

### <span id="page-14-0"></span>**5.1.5 Uninstalling the legacy Sensor driver from Windows 10**

To uninstall the u-blox legacy Sensor driver from Windows 10, remember to log in as an administrator and follow the instructions below:

• Connect the u-blox GNSS receiver, open the Device Manager, and right click "Sensors->u-blox GNSS Location Sensor".



• From the menu window, click "Uninstall device".



- **Figure 15: Uninstalling legacy Sensor driver from Device Manager**
- From the pop-up "Uninstall Device" window, select the "Delete the driver software for this device" option.

| <b>Uninstall Device</b>                                          | ×      |
|------------------------------------------------------------------|--------|
| u-blox GNSS Location Sensor                                      |        |
| Waming: You are about to uninstall this device from your system. |        |
| $\vee$ Delete the driver software for this device.               |        |
| Uninstall                                                        | Cancel |

**Figure 16: Selection to delete all the driver files for the device**

- Click "Uninstall" to start uninstalling the driver.
- Open the Device Manager to check that the Sensor driver has been properly uninstalled.



**Figure 17: Check Device Manager to check that the legacy Sensor driver is uninstalled successfully**

#### <span id="page-15-0"></span>**5.1.6 Uninstalling the legacy VCP driver from Windows 10**

To uninstall the u-blox legacy VCP driver from Windows 10, remember to log in as an administrator. The GNSS receiver should be disconnected from the PC and the driver should be uninstalled both from the "Control Panel->Programs->Programs and Features" and the "Device Manager". To uninstall from the "Device Manager", follow the instructions below:

• Open the Device Manager and right click "Ports->u-blox Virtual COM Port (COMxx)".



• From the menu window, click "Uninstall device".



- **Figure 18: Uninstalling legacy VCP driver from Device Manager**
- From the pop-up "Uninstall Device" window, select the "Delete the driver software for this device" option.

| <b>Uninstall Device</b><br>×                                     |
|------------------------------------------------------------------|
| u-blox Virtual COM Port (COM90)                                  |
| Waming: You are about to uninstall this device from your system. |
| $\vee$ Delete the driver software for this device.               |
| Cancel<br>Uninstall                                              |

**Figure 19: Selection to delete all the driver files for the device**

- Click "Uninstall" to start uninstalling the driver.
- Open the Device Manager to check that the VCP driver is uninstalled properly and the u-blox device will be detected as other device.



#### **Figure 20: Check the legacy VCP driver is uninstalled successfully**

To uninstall from the "Control Panel->Programs->Programs and Features", follow the instructions below:

• Open the "Control Panel->Programs->Programs and Features" and right click "u-blox GNSS VCP Device Driver for Windows".



• click "Uninstall".

| Programs and Features<br>$\Box$<br>$\times$<br>$\overline{\phantom{a}}$<br>> Control Panel > Programs > Programs and Features<br>$\vee$ 0<br>Search Pr P<br>$\leftarrow$<br><b>Control Panel Home</b><br>Uninstall or change a program<br>View installed updates<br>To uninstall a program, select it from the list and then click Uninstall, Change, or Repair.<br>Turn Windows features on or<br>off<br>BEE -<br>Uninstall<br>Organize $\blacktriangledown$<br>o<br>Install a program from the<br>$\wedge$<br>Version<br>Installed On Size<br>Publisher<br>Name<br>network<br>Thu-blox GNSS VCP Device Driver for Windows<br>u-blox<br>05-Feb-19<br>3,10,0.0<br>Uninstall<br>$Qu$ -center v19.01<br>28.9 MB 19.01<br>u-blox<br>29-Jan-19<br>Die Update for Windows 10 for x64-based Systems (KB4023057)<br><b>Microsoft Corporation</b><br>09-Feb-18<br>1.33 MB<br>2.12.0.0<br>$\blacksquare$ u-start v18.10<br>30-Nov-18<br>137 MB 18.10<br>u-blox.<br><b>Qu-start v18.12</b><br>139 MB<br>18.12<br>u-blox<br>31-Jan-19<br>Vidyo Desktop 3.6.9 - (msul)<br>Vidyo Inc.<br>07-Mar-18<br>3.6.9<br><b>DC</b> Visual Studio Community 2017<br>1.89 GB 15.9.28307.344<br><b>Microsoft Corporation</b><br>28-Jan-19<br>123 MB 2.2.6<br>VLC media player<br>VideoLAN<br>15-Aug-17<br>With the Pup Time Libraries 10.220<br><b>London Inc.</b><br>14 Aug 17<br>166340 10220<br>u-blox Product version: 3.10.0.0<br>Support link: http://www.u-blox.com<br>Help link: http://www.u-blox.com |  |  |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |  |

**Figure 21: Uninstalling legacy VCP driver from Programs and Features**

• The driver will be uninstalled as shown in the screenshot below.

| <b>CD</b> u-blox GNSS VCP Device Driver for Windows Uninstall |  | п | $\times$ |
|---------------------------------------------------------------|--|---|----------|
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
| Completed                                                     |  |   |          |
|                                                               |  |   |          |
| Show details                                                  |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |
|                                                               |  |   |          |

**Figure 22: Uninstallation complete window**

### <span id="page-17-0"></span>**5.2 Installing/uninstalling drivers on Windows 7 and 8.x**

This section explains the procedure to install and uninstall u-blox GNSS drivers for Windows 7 and Windows 8x operating systems.

### <span id="page-17-1"></span>**5.2.1 Getting the u-blox CDC-ACM driver for Windows 7 and Windows 8.x**

The u-blox CDC-ACM Driver for x64 bit version of Windows 7 and 8.x is deployed to Windows Update, so connecting the PC to the Internet and connecting the u-blox GNSS receiver will get the driver automatically from the Windows Update.

If it does not update automatically, follow the steps below to update from the Internet:

• Right click on the undetected u-blox GNSS device.



• From the menu window, select "Update Driver Software ...".



#### **Figure 23: Getting CDC-ACM driver from Windows Update**

• From the "Update Driver Software" window, select the "Search automatically for updated driver software" option and it will search via the Windows Update to get the deployed CDC-ACM driver from u-blox.

|  |                                                                                                                                                                                                                                                      | X      |
|--|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
|  | Update Driver Software - u-blox GNSS receiver                                                                                                                                                                                                        |        |
|  | How do you want to search for driver software?                                                                                                                                                                                                       |        |
|  | $\rightarrow$ Search automatically for updated driver software<br>Windows will search your computer and the Internet for the latest driver software<br>for your device, unless you've disabled this feature in your device installation<br>settings. |        |
|  | Browse my computer for driver software<br>Locate and install driver software manually.                                                                                                                                                               |        |
|  |                                                                                                                                                                                                                                                      | Cancel |

#### **Figure 24: Searching CDC-ACM driver from Windows Update**





• When the driver is successfully updated, the device will appear in the Device Manager, as shown in Figure 25.



**Figure 25: Updated CDC-ACM driver from Windows Update**

#### <span id="page-19-0"></span>**5.2.2 Uninstalling the u-blox CDC-ACM driver from Windows 7 and Windows 8.x**

To uninstall the u-blox CDC-ACM driver from the device, follow the instructions below:

- Open the Device Manager and right click on the "Ports->u-blox GNSS Receiver (COMxx)".
- From the menu window, click "Uninstall device".

| <b>Device Manager</b>                                                                                                                                                                                                                       |                                                                                                                                          | $\mathbf{x}$<br>▣<br>$\Box$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Action<br>View<br>Help<br><b>File</b>                                                                                                                                                                                                       |                                                                                                                                          |                             |
| 哈嘎帽<br>Ġ<br><b>IQ</b>                                                                                                                                                                                                                       |                                                                                                                                          |                             |
| Microsoft Virtual WiFi Miniport Adapter #2<br>Shrew Soft Virtual Adapter<br>VirtualBox Host-Only Ethernet Adapter                                                                                                                           |                                                                                                                                          |                             |
| <b>D</b> Portable Devices                                                                                                                                                                                                                   |                                                                                                                                          |                             |
| Ports (COM & LPT)<br>com0com - serial port emulator (COM91)<br>com0com - serial port emulator (COM92)<br>1 T<br><b>ECP Printer Port (LPT1)</b><br>19<br>Intel(R) Active Management Technology - SOL (COM3)<br>u-blox GNSS Receiver (COM105) | Dell Wireless 5570 HSPA+ (42Mbps) Mobile Broadband DM Port (COM6)<br>Dell Wireless 5570 HSPA+ (42Mbps) Mobile Broadband NMEA Port (COM4) |                             |
| Processors<br>Smart card readers                                                                                                                                                                                                            | Update Driver Software<br><b>Disable</b>                                                                                                 |                             |
| <b>Broadcom Usbccid Smartcard Re</b>                                                                                                                                                                                                        | Uninstall                                                                                                                                |                             |
| Sound, video and game controllers<br>Storage controllers                                                                                                                                                                                    | Scan for hardware changes                                                                                                                |                             |
| System devices<br>Universal Serial Bus controllers                                                                                                                                                                                          | <b>Properties</b>                                                                                                                        |                             |
| Uninstalls the driver for the selected device.                                                                                                                                                                                              |                                                                                                                                          |                             |

**Figure 26: Uninstall the CDC-ACM driver from Device Manager**



• From the pop-up Uninstall Device window, select the "Delete the driver software for this device" option.



#### **Figure 27: Selection to delete all the driver files for the device**

- Click "Uninstall".
- Once the driver is uninstalled, the Device Manager window will be refreshed and the "u-blox GNSS Receiver (COMxx)" port will be uninstalled and the u-blox device will be detected as another device.



**Figure 28: Check the CDC-ACM device driver is uninstalled successfully**

#### <span id="page-20-0"></span>**5.2.3 Uninstalling the legacy sensor driver from Windows 7 and Windows 8.x**

To uninstall the u-blox legacy sensor driver from Windows 7 and 8.x, remember to log in as an administrator and follow the instructions below:

• Connect the u-blox GNSS receiver, open the Device Manager and right click on "Sensors->u-blox GNSS Location Sensor".



• From the menu window, click "Uninstall".



#### **Figure 29: Uninstalling legacy Sensor driver from Device Manager**

• From the "Confirm Device Uninstall" window, select the "Delete the driver software for this device" option.

| <b>Confirm Device Uninstall</b>                                  |
|------------------------------------------------------------------|
| u-blox GNSS Location Sensor                                      |
| Waming: You are about to uninstall this device from your system. |
| V Delete the driver software for this device.                    |
| Cancel<br>OK                                                     |

**Figure 30: Selection to delete all the driver files for the device**

- Click "OK" to start uninstalling the driver.
- Open the Device Manager to check that the sensor driver is uninstalled properly.



**Figure 31: Check Device Manager to check that the legacy Sensor driver is uninstalled successfully**

### <span id="page-21-0"></span>**5.2.4 Uninstalling the legacy VCP driver from Windows 7 and Windows 8.x**

To uninstall the u-blox legacy VCP driver from Windows 7 and 8.x, remember to log in as an administrator. The GNSS receiver should be disconnected from the PC and the driver should be



uninstalled both from the "Control Panel->All Control Panel Items-Programs and Features" and the "Device Manager". To uninstall from the "Device Manager", follow the instructions below:

- Open the Device Manager and right click on "Ports->u-blox Virtual COM Port (COMxx)".
- From the menu window, click "Uninstall".



- **Figure 32: Uninstalling legacy VCP driver from Device Manager**
- From the pop-up Confirm Device Uninstall window, select the "Delete the driver software for this device" option.



**Figure 33: Selection to delete all the driver files for the device**

• Click "OK" to start uninstalling the driver.



• Open the Device Manager to check that the VCP driver is uninstalled properly and the u-blox device will be detected as another device.



**Figure 34: Check the legacy VCP driver is uninstalled successfully**

To uninstall from the "Control Panel->All Control Panel Items-Programs and Features", follow the instructions below:

- Open the "Control Panel->All Control Panel Items-Programs and Features" and right click on "ublox GNSS VCP Device Driver for Windows".
- Click "Uninstall".

| <b>Control Panel Home</b><br>Uninstall or change a program<br>View installed updates<br>To uninstall a program, select it from the list and then click Uninstall, Change, or Repair.<br>Turn Windows features on or<br>off<br>Uninstall<br>Organize $\blacktriangledown$<br>Install a program from the<br>Publisher<br>Installed On<br>Version<br>Size<br>Name<br>network<br>TortoiseSVN 1.5.10.16879 (64 bit)<br><b>TortoiseSVN</b><br>20,7 MB 1.5.16879<br>21.5.2014<br>Thu-blox GNSS VCP Device Driver for Windows<br>22.1.2018<br>3.10.0.0<br><b>Uninstall</b><br>UC232A Win 7 64bit<br>Ltd.<br>9.9.2014<br>1.0.078<br>$\mathbf{u}$ u-center_v8.22<br>u-blox<br>6.10.2016<br>8.22<br>tu-center_v8.28<br>9.1.2018<br>8.28<br>$u - bl$ ox<br>USBIyzer - USB Protocol Analyzer<br>30.11.2017<br>2.2 Build 100<br>V Vagrant<br>1.11.2016<br>561 MB 1.8.6<br>HashiCorp<br><b>ILE WCE RIA Services V1 0 SP2</b><br>Microsoft Corporation<br>23.6.2016<br>691 MR 41628120 |  | > Control Panel > All Control Panel Items > Programs and Features |  | $-14$ | Search Programs and Features |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|-------------------------------------------------------------------|--|-------|------------------------------|--|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |                                                                   |  |       |                              |  |

**Figure 35: Uninstalling legacy VCP driver from Programs and Features**



• The driver will be uninstalled as shown in the screenshot below.

| Th u-blox GNSS VCP Device Driver for Windows Uninstall |          | $\overline{\mathbf{z}}$<br>e. |
|--------------------------------------------------------|----------|-------------------------------|
|                                                        |          |                               |
| Completed                                              |          |                               |
| Show details                                           |          |                               |
|                                                        |          |                               |
|                                                        |          |                               |
|                                                        |          |                               |
|                                                        | $<$ Back | Close<br>Cancel               |

**Figure 36: Uninstallation complete window**



## <span id="page-25-0"></span>**Related documents**

- **[1]** [Introduction](https://docs.microsoft.com/en-us/windows/desktop/SensorsAPI/introduction-to-the-sensor-and-location-platform-in-windows) to the Sensor and Location Platform in Windows
- <span id="page-25-1"></span>**[2]** u-blox 8 / u-blox M8 Receiver Description Including Protocol [Specification](https://www.u-blox.com/docs/UBX-13003221) (Public version)



## <span id="page-26-0"></span>**Revision history**

| Revision | Date        | Name | Status / Comments |
|----------|-------------|------|-------------------|
| R01      | 16-Apr-2019 | msul | Initial release   |



## **Contact**

For complete contact information visit us at [www.u-blox.com.](https://www.u-blox.com)

#### **u-blox Offices**

#### **North, Central and South America Headquarters Asia, Australia, Pacific**

#### **Europe, Middle East, Africa**

|         | u-blox America, Inc. | u-blox AG           |                                       |                     | u-blox Singapore Pte. Ltd.                  |
|---------|----------------------|---------------------|---------------------------------------|---------------------|---------------------------------------------|
| Phone:  | +1 703 483 3180      | Phone:              | +41 44 722 74 44                      | Phone:              | +65 6734 3811                               |
| E-mail: | info_us@u-blox.com   | E-mail:<br>Support: | info@u-blox.com<br>support@u-blox.com | E-mail:<br>Support: | info_ap@u-blox.com<br>support_ap@u-blox.com |

| Regional Office West Coast                                           | Documentation Feedback |                               | Regional Office Australia                                       |  |
|----------------------------------------------------------------------|------------------------|-------------------------------|-----------------------------------------------------------------|--|
| Phone:<br>+1 408 573 3640<br>Email:<br>E-mail:<br>info_us@u-blox.com | docsupport@u-blox.com  | Phone:<br>E-mail:<br>Support: | +61 2 8448 2016<br>info_anz@u-blox.com<br>support_ap@u-blox.com |  |

**Technical Support Regional Office China (Beijing)** Phone: +1 703 483 3185 Phone: +86 10 68 133 545 E-mail: support\_us@u-blox.com E-mail: info\_cn@u-blox.com Support: support\_cn@u-blox.com

**Regional Office China (Chongqing)**

| Phone:   | +86 23 6815 1588      |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

**Regional Office China (Shanghai)**

| Phone:   | +86 21 6090 4832      |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

**Regional Office China (Shenzhen)**

| Phone:   | +86 755 8627 1083     |
|----------|-----------------------|
| E-mail:  | info_cn@u-blox.com    |
| Support: | support_cn@u-blox.com |

#### **Regional Office India**

Phone: +91 80 4050 9200 E-mail: info\_in@u-blox.com Support: support\_in@u-blox.com

#### **Regional Office Japan (Osaka)**

Phone: +81 6 6941 3660 E-mail: info\_jp@u-blox.com

Support: support\_jp@u-blox.com

#### **Regional Office Japan (Tokyo)**

Phone: +81 3 5775 3850

E-mail: info\_jp@u-blox.com Support: support\_jp@u-blox.com

**Regional Office Korea** Phone: +82 2 542 0861

E-mail: info\_kr@u-blox.com Support: support\_kr@u-blox.com

#### **Regional Office Taiwan**

| Phone:   | +886 2 2657 1090      |
|----------|-----------------------|
| E-mail:  | info_tw@u-blox.com    |
| Support: | support_tw@u-blox.com |