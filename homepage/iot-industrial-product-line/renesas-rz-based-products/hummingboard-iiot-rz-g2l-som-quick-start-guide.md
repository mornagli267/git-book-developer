# HummingBoard IIOT & RZ/G2L SOM Quick Start Guide

![IIOT Sideways.png](./attachments/IIOT%20Sideways.png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the HummingBoard IIOT.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 29 Sep 2024 | Yazan | 1.0 | Initial release |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product specifications](#product-specifications)<br>  - [HUMMINGBOARD RZ/G2L IIOT SBC](#hummingboard-rz-g2l-iiot-sbc)<br>  - [Block Diagram](#block-diagram)<br>  - [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Boot Select](#boot-select)<br>- [Booting from SD card](#booting-from-sd-card)<br>- [Boot Select](#boot-select)<br>- [More Features](#more-features)<br>  - [Internet](#internet)<br>    - [WiFi](#wifi)<br>  - [Bluetooth](#bluetooth)<br>  - [Cellular Modem](#cellular-modem)<br>  - [SPI](#spi)<br>- [TLV EEPROM Support](#tlv-eeprom-support)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product specifications

| **Model** | <a id="hummingboard-rz-g2l-iiot-sbc"></a><br><br>#### HUMMINGBOARD RZ/G2L IIOT SBC |
| --- | --- |
| SOM Model | Renesas RZ/G2L Solo / Dual core Arm Cortex A55  <br>Up to 1.2GHz (With Arm M33) |
| Memory & Storage | Up to 2GB DDR4  <br>Up to 128GB eMMC  <br>MicroSD |
| Network | 2 x Ethernet RJ45 10/100/1000  <br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4/5 GHz) |
| Connectivity | 3 x USB3.0 ( Host)  <br>M.2 B-Key LTE modem (eSIM, NanoSim)  <br>M.2 M-Key  <br>Additional addon cards are supported\*  <br>SIM card slot |
| Media | MIPI-DSI  <br>The Evaluation kit comes with 7” touch display MIPI-DSI  <br>MIPI-CSI 4 lanes |
| I/O | 2 x USB2.0  <br>2 x CAN-FD  <br>2x RS232 or 2x RS485, or RS232 + RS485 (SW Configuration)  <br>1 x I/O Digital Input  <br>1 x I/O Digital output  <br>1 x Reset button  <br>1 x ON/OFF button  <br>1 x Configurable push button  <br>1 x RGB LED |
| Misc | TPM2.0  <br>GPIO  <br>RTC  <br>EEPROM |
| OS Support | Linux |
| Environment | Commercial: 0°C to 70°C  <br>Industrial: -40°C to 85°C |
| Dimensions | PCBA: 88 x 135 mm  <br>Enclosure : **<TBD>** |
| Power | 7V – 28V wide range  <br>PoE sink support 802.3af Class 0  <br>Reverse polarity support |
| Enclosure | Optional extruded aluminum (IP32) enclosure |
|     | [ Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+iiot%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355) |

> [!INFO]
> Supported with RZ/G2L SOM. For more detailed information about our SOM RZ/G2L series please visit this user manual : [RZ/G2L SOM Hardware User Manual](../renesas-rz-based-products/rz-g2l-and-rz-v2l-som-hardware-user-manual.md) .

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the RZ/G2L Block Diagram.

![image-20250115-103930.png](./attachments/image-20250115-103930.png)

<a id="visual-features-overview"></a>

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard IIOT & RZ/G2L SOM.

![HummingBoard RZ_G2L IIOT SBC Layout .png](./attachments/HummingBoard%20RZ_G2L%20IIOT%20SBC%20Layout%20.png)

Print side connector overview of the HummingBoard IIOT & RZ/G2L SOM.

![image-20240929-120103.png](./attachments/image-20240929-120103.png)

![image-20241215-105449.png](./attachments/image-20241215-105449.png)

**Power Input Polarity \[J1\]:**

- **Connector Type**: Green two-terminal connector \[J1\].
- **Voltage Range**: 7V to 32V.
- **Polarity**:
  - **\+ (Positive)**: Left terminal (as marked in the image).
  - **\- (Negative)**: Right terminal (as marked in the image).

> [!NOTE]
> Plug for connector **J1** : 2 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm).

**J5004** {2x RS485, 2x CAN-FD, 2x RS232, DIG\_IN, DIG\_OUT}

![image-20241013-104136.png](./attachments/image-20241013-104136.png)

![image-20241121-134703.png](./attachments/image-20241121-134703.png)

> [!NOTE]
> Plug for connector **J5004** : 20 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm) like [this](https://www.digikey.com/en/products/detail/phoenix-contact/1738885/3606115).

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

- Linux or Windows PC
- HummingBoard IIOT with SOM
- 12V Power adapter (HummingBoard IIOT has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
- Type-C to USB for console, the HummingBoard IIOT has an onboard FTDI chip.
- IP router or IP switch

<a id="boot-select"></a>

## Boot Select

![image-20240901-112851.png](./attachments/image-20240901-112851.png)

Before powering up the board for the first time it is recommended to select the boot media using onboard DIP switch **S5**:

| **Switch** | **1**  <br>(MD0) | **2**  <br>(MD1) | **3**  <br>(MD2) | **4**  <br>(SD0\_DEV\_SEL) | **5**  <br>(VDD\_1.8V) | **6**  <br>(VDD\_3.3V) |
| --- | --- | --- | --- | --- | --- | --- |
| **uSD** | OFF | OFF | OFF | OFF | OFF | **ON** |
| **eMMC** | **ON** | OFF | OFF | **ON** | OFF | **ON** |
| **Serial Dowanloder** | **ON** | OFF | **ON** | OFF | OFF | **ON** |

> [!INFO]
> **MDx** = BOOT\_MODEx, **VDD\_BOOT** = 1.8V **or** 3.3V (Select S5\[5\] **or** S5\[6\]) .  
> **Note** that **MD1** and **MD0** have been swapped between PCB version 1.1 and PCB version 1.0.

<a id="booting-from-sd-card"></a>

## Booting from SD card

<a id="boot-select"></a>

## Boot Select

Here is the correct DIP switch position for SD boot:

![image-20240929-162042.png](./attachments/image-20240929-162042.png)

> [!INFO]
> Note: The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from an SD card.

1. **Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/RZ/Debian/build_date_20240529-git_rev_f22483f/rzg2l-solidrun-sd-debian-f22483f.img.xz
```

- For more Debian releases, please visit [Debian Releases for RZ/G2L](https://images.solid-run.com/RZ/rzg2lc_build/).

2. **Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc rzg2l-solidrun-sd-debian-f22483f.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync 
```

- For more information, please visit [Flashing an SD Card](../../../homepage/other-articles/flashing-an-sd-card.md) .

> [!NOTE]
> Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

3. **SD card insertion**

Please Insert the SD card into your device.

4. **Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

5. **Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../../homepage/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](./attachments/image-20210926-110202.png)

- In order to be able to log in , please insert “**root**” as a username and password as follows:

![](./attachments/image-20210926-110919.png)

<a id="more-features"></a>

## More Features

<a id="internet"></a>

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).  
Models HummingBoard with WiFi, can be connected via [WiFi](https://solidrun.atlassian.net/wiki/spaces/developer/pages/200015887/CuBox-M+Quick+Start+Guide#wifi) or wired Ethernet.

- Please check you Ethernet connection.
- Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

- For more detailed information, please refer to [i.MX8M Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) .

<a id="wifi"></a>

##### WiFi

- You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

> [!NOTE]
> To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

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

> [!NOTE]
> Check your personal ssids by running : ‘iw dev wlan0 scan’

5. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

- For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

<a id="bluetooth"></a>

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

- Start by scanning for other Bluetooth devices:

```
hcitool scan
```

- Choose a MAC address and connect :

```
rfcomm connect 0  $MAC 10 & 
```

- You can check the communication between the devices by writing :

```
l2ping -c 4  $MAC
```

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- For some cellular modules to be connected, please refer to [Cellular Modules](../../iot-industrial-product-line/nxp-imx6-based-products/imx6-other-articles/cellular-modules.md) .

<a id="spi"></a>

#### SPI

For testing you serial peripheral interface - SPI, please see this documentation [SPI from Linux with spidev](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/321880065?draftShareId=ac699b08-ef2b-4682-9832-b012e01aeef0).

**GUI On Debian**

There is an option with the **Debian** image, up to the user, to work with a GUI like Weston, GNOME and etc.  
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
NOTE: ‘gnome-session’ is an example of gnome that we can work with, you can replace the ‘session' with another GNOME extention.
3. Start your GNOME GUI.
```
$ sudo systemctl start gdm
```
  - For logging in you need a user on your device to log into it. You can create one before step 3 by this command (replace the ‘username’ with name that you want) :
```
$ sudo adduser username
```
  - You can jump between GUIs that you install (like gnome-session) by the setting button that locates in the down right corner of the home screen.

<a id="tlv-eeprom-support"></a>

## TLV EEPROM Support

RZ/G2L SoMs are being programmed with identifying information such as the product name, MAC Address and SKUs to allow for programmatic identification of hardware.

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211024-150854.png) | [Debian](https://github.com/SolidRun/build_rzg2lc) |
| ![](./attachments/image-20211024-151110.png) | [RZ/G2L Yocto](https://github.com/SolidRun/meta-solidrun-arm-rzg2lc) |
| ![](./attachments/image-20211024-150920.png) | [Buildroot](https://github.com/SolidRun/build_rzg2lc) |

<a id="build-from-source"></a>

## Build from source

- [https://github.com/SolidRun/build\_rzg2lc](https://github.com/SolidRun/build_rzg2lc)

<a id="documentation"></a>

## Documentation

     

|     | File | Modified |
| --- | --- | --- |

No files shared here yet.

- Drag and drop to upload or [browse for files] ![](/wiki/images/icons/wait.gif)

Upload file 

File description  

</form> </div> </div> <div> </div> </div> </div> </div> </div> <div class="columnLayout three-equal" data-layout="three-equal"> <div class="cell normal" data-type="normal"> <div class="innerCell"> <p /></div> </div> <div class="cell normal" data-type="normal"> <div class="innerCell"> <p><a class="external-link" href="https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&amp;post\_type=product&amp;\_ga=2.156269240.2016484779.1641802897-2012112798.1622706355" rel="nofollow" style="display: inline-block;padding: 0 15.0px;height: 32.0px;font-size: 14.0px;line-height: 32.0px;background: rgb(236,63,63);color: rgb(255,255,255);cursor: pointer;border-radius: 2.0px;margin-right: 10.0px;" title=""><style>\[data-colorid=bh0vnwsz7m\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=bh0vnwsz7m\]{color:#796bcd}\[data-colorid=zzvebim85a\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=zzvebim85a\]{color:#796bcd}\[data-colorid=to0ctugtgz\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=to0ctugtgz\]{color:#796bcd}\[data-colorid=r4ubabq7gv\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=r4ubabq7gv\]{color:#ff6640}\[data-colorid=ewknsb380q\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=ewknsb380q\]{color:#796bcd}\[data-colorid=oiis6qsd87\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=oiis6qsd87\]{color:#796bcd}\[data-colorid=z53t0asbog\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=z53t0asbog\]{color:#796bcd}\[data-colorid=c4jrii326f\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=c4jrii326f\]{color:#796bcd}\[data-colorid=q9yj906iv5\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=q9yj906iv5\]{color:#ff6640}\[data-colorid=i4f6m3oj0i\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=i4f6m3oj0i\]{color:#796bcd}\[data-colorid=ovy9p2vqev\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=ovy9p2vqev\]{color:#ff6640}\[data-colorid=oexv1vlho3\]{color:#0747a6} html\[data-color-mode=dark\] \[data-colorid=oexv1vlho3\]{color:#5999f8}\[data-colorid=r8jxsxpmmy\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=r8jxsxpmmy\]{color:#ff6640}\[data-colorid=zrr4e63c4z\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=zrr4e63c4z\]{color:#ff6640}\[data-colorid=jvdc0ylubp\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=jvdc0ylubp\]{color:#796bcd}\[data-colorid=mnwq8t4rqq\]{color:#0747a6} html\[data-color-mode=dark\] \[data-colorid=mnwq8t4rqq\]{color:#5999f8}\[data-colorid=lnuvs2bw89\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=lnuvs2bw89\]{color:#796bcd}\[data-colorid=jttg2wda7y\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=jttg2wda7y\]{color:#ff6640}\[data-colorid=gaqw6um1dl\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=gaqw6um1dl\]{color:#796bcd}\[data-colorid=pc2akdrcyy\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=pc2akdrcyy\]{color:#796bcd}\[data-colorid=fu3678v9ki\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=fu3678v9ki\]{color:#ff6640}\[data-colorid=krflzinfha\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=krflzinfha\]{color:#ff6640}\[data-colorid=ty7ob1ye55\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=ty7ob1ye55\]{color:#796bcd}\[data-colorid=uthjmmgrj0\]{color:#0747a6} html\[data-color-mode=dark\] \[data-colorid=uthjmmgrj0\]{color:#5999f8}\[data-colorid=t991wzv3iz\]{color:#bf2600} html\[data-color-mode=dark\] \[data-colorid=t991wzv3iz\]{color:#ff6640}\[data-colorid=wdn7l4ma5o\]{color:#0747a6} html\[data-color-mode=dark\] \[data-colorid=wdn7l4ma5o\]{color:#5999f8}\[data-colorid=t8uni9okah\]{color:#403294} html\[data-color-mode=dark\] \[data-colorid=t8uni9okah\]{color:#796bcd}</style> Buy a Sample Now </a></p></div> </div> <div class="cell normal" data-type="normal"> <div class="innerCell"> <p /></div> </div> </div> <div class="columnLayout fixed-width" data-layout="fixed-width"> <div class="cell normal" data-type="normal"> <div class="innerCell"> <h2 id="HummingBoardIIOT&amp;RZ/G2LSOMQuickStartGuide-RelatedArticles">Related Articles</h2><div class="error">Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden</div><p /><p /></div> </div> </div> </div></x-turndown>