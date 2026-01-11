# HummingBoard IIOT & RZ/G2L SOM Quick Start Guide

![IIOT Sideways.png](<../../../.gitbook/assets/IIOT Sideways (1).png>)

## Introduction

The following quick start guide provides background information about the HummingBoard IIOT.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Revision** | **Notes**       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 29 Sep 2024       | Yazan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1.0          | Initial release |
| Table of Contents | <p>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#product-specifications">Product specifications</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#hummingboard-rz-g2l-iiot-sbc">HUMMINGBOARD RZ/G2L IIOT SBC</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#booting-from-sd-card">Booting from SD card</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#wifi">WiFi</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#cellular-modem">Cellular Modem</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#spi">SPI</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#tlv-eeprom-support">TLV EEPROM Support</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-iiot-rz-g2l-som-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Hardware Setup

#### Product specifications

| **Model**        | <p><br><br>#### HUMMINGBOARD RZ/G2L IIOT SBC</p>                                                                                                                                                                                        |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SOM Model        | <p>Renesas RZ/G2L Solo / Dual core Arm Cortex A55<br>Up to 1.2GHz (With Arm M33)</p>                                                                                                                                                    |
| Memory & Storage | <p>Up to 2GB DDR4<br>Up to 128GB eMMC<br>MicroSD</p>                                                                                                                                                                                    |
| Network          | <p>2 x Ethernet RJ45 10/100/1000<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4/5 GHz)</p>                                                                                                                                            |
| Connectivity     | <p>3 x USB3.0 ( Host)<br>M.2 B-Key LTE modem (eSIM, NanoSim)<br>M.2 M-Key<br>Additional addon cards are supported*<br>SIM card slot</p>                                                                                                 |
| Media            | <p>MIPI-DSI<br>The Evaluation kit comes with 7” touch display MIPI-DSI<br>MIPI-CSI 4 lanes</p>                                                                                                                                          |
| I/O              | <p>2 x USB2.0<br>2 x CAN-FD<br>2x RS232 or 2x RS485, or RS232 + RS485 (SW Configuration)<br>1 x I/O Digital Input<br>1 x I/O Digital output<br>1 x Reset button<br>1 x ON/OFF button<br>1 x Configurable push button<br>1 x RGB LED</p> |
| Misc             | <p>TPM2.0<br>GPIO<br>RTC<br>EEPROM</p>                                                                                                                                                                                                  |
| OS Support       | Linux                                                                                                                                                                                                                                   |
| Environment      | <p>Commercial: 0°C to 70°C<br>Industrial: -40°C to 85°C</p>                                                                                                                                                                             |
| Dimensions       | <p>PCBA: 88 x 135 mm<br>Enclosure :</p>                                                                                                                                                                                                 |
| Power            | <p>7V – 28V wide range<br>PoE sink support 802.3af Class 0<br>Reverse polarity support</p>                                                                                                                                              |
| Enclosure        | Optional extruded aluminum (IP32) enclosure                                                                                                                                                                                             |
|                  | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+iiot%22\&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)                                                                                         |

> \[!INFO] Supported with RZ/G2L SOM. For more detailed information about our SOM RZ/G2L series please visit this user manual : [RZ/G2L SOM Hardware User Manual](rz-g2l-and-rz-v2l-som-hardware-user-manual.md) .

#### Block Diagram

The following figure describes the RZ/G2L Block Diagram.

![image-20250115-103930.png](../../../.gitbook/assets/image-20250115-103930.png)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard IIOT & RZ/G2L SOM.

![HummingBoard RZ\_G2L IIOT SBC Layout .png](<../../../.gitbook/assets/HummingBoard RZ_G2L IIOT SBC Layout .png>)

Print side connector overview of the HummingBoard IIOT & RZ/G2L SOM.

![image-20240929-120103.png](<../../../.gitbook/assets/image-20240929-120103 (1).png>)

![image-20241215-105449.png](../../../.gitbook/assets/image-20241215-105449.png)

**Power Input Polarity \[J1]:**

* **Connector Type**: Green two-terminal connector \[J1].
* **Voltage Range**: 7V to 32V.
* **Polarity**:
  * **+ (Positive)**: Left terminal (as marked in the image).
  * **- (Negative)**: Right terminal (as marked in the image).

> \[!NOTE] Plug for connector **J1** : 2 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm).

**J5004** {2x RS485, 2x CAN-FD, 2x RS232, DIG\_IN, DIG\_OUT}

![image-20241013-104136.png](../../../.gitbook/assets/image-20241013-104136.png)

![image-20241121-134703.png](<../../../.gitbook/assets/image-20241121-134703 (1).png>)

> \[!NOTE] Plug for connector **J5004** : 20 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm) like [this](https://www.digikey.com/en/products/detail/phoenix-contact/1738885/3606115).

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard IIOT with SOM
* 12V Power adapter (HummingBoard IIOT has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
* Type-C to USB for console, the HummingBoard IIOT has an onboard FTDI chip.
* IP router or IP switch

## Boot Select

![image-20240901-112851.png](<../../../.gitbook/assets/image-20240901-112851 (1).png>)

Before powering up the board for the first time it is recommended to select the boot media using onboard DIP switch **S5**:

| **Switch**            | <p><strong>1</strong><br>(MD0)</p> | <p><strong>2</strong><br>(MD1)</p> | <p><strong>3</strong><br>(MD2)</p> | <p><strong>4</strong><br>(SD0_DEV_SEL)</p> | <p><strong>5</strong><br>(VDD_1.8V)</p> | <p><strong>6</strong><br>(VDD_3.3V)</p> |
| --------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ------------------------------------------ | --------------------------------------- | --------------------------------------- |
| **uSD**               | OFF                                | OFF                                | OFF                                | OFF                                        | OFF                                     | **ON**                                  |
| **eMMC**              | **ON**                             | OFF                                | OFF                                | **ON**                                     | OFF                                     | **ON**                                  |
| **Serial Dowanloder** | **ON**                             | OFF                                | **ON**                             | OFF                                        | OFF                                     | **ON**                                  |

> \[!INFO] **MDx** = BOOT\_MODEx, **VDD\_BOOT** = 1.8V **or** 3.3V (Select S5\[5] **or** S5\[6]) .\
> **Note** that **MD1** and **MD0** have been swapped between PCB version 1.1 and PCB version 1.0.

## Booting from SD card

## Boot Select

Here is the correct DIP switch position for SD boot:

![image-20240929-162042.png](../../../.gitbook/assets/image-20240929-162042.png)

> \[!INFO] Note: The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from an SD card.

1. **Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/RZ/Debian/build_date_20240529-git_rev_f22483f/rzg2l-solidrun-sd-debian-f22483f.img.xz
```

* For more Debian releases, please visit [Debian Releases for RZ/G2L](https://images.solid-run.com/RZ/rzg2lc_build/).

2. **Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc rzg2l-solidrun-sd-debian-f22483f.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync 
```

* For more information, please visit [Flashing an SD Card](../../other-articles/flashing-an-sd-card.md) .

> \[!NOTE] Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

3. **SD card insertion**

Please Insert the SD card into your device.

4. **Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

5. **Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](<../../../.gitbook/assets/image-20210926-110202 (4).png>)

* In order to be able to log in , please insert “**root**” as a username and password as follows:

![](<../../../.gitbook/assets/image-20210926-110919 (4).png>)

## More Features

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).\
Models HummingBoard with WiFi, can be connected via [WiFi](../nxp-imx8-based-products/cubox-m-quick-start-guide.md#wifi) or wired Ethernet.

* Please check you Ethernet connection.
* Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

* For more detailed information, please refer to [i.MX8M Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) .

**WiFi**

* You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

> \[!NOTE] To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

2. Install the wpa\_supplicant package:

```
apt-get install wpasupplicant 
```

3. Edit network interfaces file :

At the bottom of the file, add the following lines to allow wlan as a network connection:

```
cat <<EOF > /etc/network/interfaces.d/wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

EOF
```

4. Create a configuration file with the relevant ssid:

```
cat <<EOF > /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=/run/wpa_supplicant
update_config=1

network={
    ssid="MYSSID"
    psk="passphrase" 
}

EOF
```

> \[!NOTE] Check your personal ssids by running : ‘iw dev wlan0 scan’

5. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

* For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

#### Bluetooth

1. For showing all Bluetooth devices, run the following:

```
apt-get install bluez
hciconfig -a
```

2. Choose a device, and turn it on:

```
 hciconfig hci0 up
```

3. Set up the Bluetooth name:

```
hciconfig hci0 name 'SolidRun_Ble'
```

4. Make your Bluetooth detectable by other devices:

```
hciconfig hci0 piscan
```

5. If you want to connect to other devices:

* Start by scanning for other Bluetooth devices:

```
hcitool scan
```

* Choose a MAC address and connect :

```
rfcomm connect 0  $MAC 10 & 
```

* You can check the communication between the devices by writing :

```
l2ping -c 4  $MAC
```

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

* For some cellular modules to be connected, please refer to [Cellular Modules](../nxp-imx6-based-products/imx6-other-articles/cellular-modules.md) .

#### SPI

For testing you serial peripheral interface - SPI, please see this documentation [SPI from Linux with spidev](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/321880065?draftShareId=ac699b08-ef2b-4682-9832-b012e01aeef0).

**GUI On Debian**

There is an option with the **Debian** image, up to the user, to work with a GUI like Weston, GNOME and etc.\
For applying this option do the following steps:

First, connect your device to a screen using the working output (HDMI / uHDMI).

For working with **Weston** GUI:

1. Install the Weston package.

```
$ sudo apt install weston
```

2. Make a directory for the output of the Weston GUI.

```
$ mkdir /your/directory/location
```

3. Give permissions to this directory.

```
 $ chmod 0700 /your/directory/location
```

4. Set the XDG\_RUNTIME\_DIR env param to your directory.

```
$ export XDG_RUNTIME_DIR=/your/directory/location
```

5. Run Weston.

```
$ weston
```

For working with **GNOME** GUI on top of Xorg:

1. Install Xorg.

```
$ sudo apt install xorg
```

2. Install your desired gnome.

```
$ sudo apt install gnome-session
```

NOTE: ‘gnome-session’ is an example of gnome that we can work with, you can replace the ‘session' with another GNOME extention. 3. Start your GNOME GUI.

```
$ sudo systemctl start gdm
```

* For logging in you need a user on your device to log into it. You can create one before step 3 by this command (replace the ‘username’ with name that you want) :

```
$ sudo adduser username
```

* You can jump between GUIs that you install (like gnome-session) by the setting button that locates in the down right corner of the home screen.

## TLV EEPROM Support

RZ/G2L SoMs are being programmed with identifying information such as the product name, MAC Address and SKUs to allow for programmatic identification of hardware.

## List Of Supported OS

| **OS**                                                        |                                                                      |
| ------------------------------------------------------------- | -------------------------------------------------------------------- |
| ![](<../../../.gitbook/assets/image-20211024-150854 (2).png>) | [Debian](https://github.com/SolidRun/build_rzg2lc)                   |
| ![](<../../../.gitbook/assets/image-20211024-151110 (3).png>) | [RZ/G2L Yocto](https://github.com/SolidRun/meta-solidrun-arm-rzg2lc) |
| ![](<../../../.gitbook/assets/image-20211024-150920 (2).png>) | [Buildroot](https://github.com/SolidRun/build_rzg2lc)                |

## Build from source

* [https://github.com/SolidRun/build\_rzg2lc](https://github.com/SolidRun/build_rzg2lc)

## Documentation

|   | File | Modified |
| - | ---- | -------- |

No files shared here yet.

* Drag and drop to upload or \[browse for files]&#x20;

Upload file

File description

[ Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22\&post\\_type=product&\\_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)

### Related Articles <a href="#hummingboardiiot-and-rz-g2lsomquickstartguide-relatedarticles" id="hummingboardiiot-and-rz-g2lsomquickstartguide-relatedarticles"></a>

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
