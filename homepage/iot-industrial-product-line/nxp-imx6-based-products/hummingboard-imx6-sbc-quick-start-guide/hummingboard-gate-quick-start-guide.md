# HummingBoard Gate Quick Start Guide

![](<../../../../.gitbook/assets/HummingBoard Gate with new i.MX6.png>)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Revision** | **Notes**       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 26 Sep 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.0          | Initial release |
| Table of Contents | <p>- <a href="hummingboard-gate-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-gate-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-gate-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-gate-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="hummingboard-gate-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-gate-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-gate-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-gate-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-gate-quick-start-guide.md#booting-form-an-sd-card">Booting form an SD card</a><br>- <a href="hummingboard-gate-quick-start-guide.md#install-to-emmc">Install to eMMC</a><br>- <a href="hummingboard-gate-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-gate-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-gate-quick-start-guide.md#wi-fi">Wi-fi</a><br>- <a href="hummingboard-gate-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-gate-quick-start-guide.md#cellular-modem">Cellular Modem</a><br>- <a href="hummingboard-gate-quick-start-guide.md#gpio-pins-control">GPIO pins Control</a><br>- <a href="hummingboard-gate-quick-start-guide.md#mikrobus">MikroBus</a><br>- <a href="hummingboard-gate-quick-start-guide.md#install-gui-support">Install GUI Support</a><br>- <a href="hummingboard-gate-quick-start-guide.md#wayland">Wayland</a><br>- <a href="hummingboard-gate-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-gate-quick-start-guide.md#build-u-boot-kernel-from-sources">Build U-Boot &#x26; Kernel from sources</a><br>- <a href="hummingboard-gate-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-gate-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Introduction

The following quick start guide provides background information about the [HummingBoard Gate](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx6-family/hummingboard/#gate) product which use the i.MX6 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Hardware Setup

#### Product Specifications

|                      |                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **SOM Model**        | NXP i.MX6 based Solo to Quad Core SOM                                                                                            |
| **Memory & Storage** | Up to 2GB DDR3\*                                                                                                                 |
|                      | uSD                                                                                                                              |
| **Connectivity**     | 1xRJ-45\*\*                                                                                                                      |
|                      | 4\*USB 2.0                                                                                                                       |
|                      | Mini-PCIe with SIM card holder                                                                                                   |
| **Media**            | HDMI-Out                                                                                                                         |
|                      | MIPI-CSI-2 and MIPI-DSI                                                                                                          |
|                      | Parallel Camera                                                                                                                  |
| **I/O**              | Reset Button                                                                                                                     |
|                      | 36 pins GPIO Header                                                                                                              |
|                      | RTC with Battery                                                                                                                 |
|                      | mikroBUS click interface                                                                                                         |
| **OS Support**       | Linux                                                                                                                            |
| **Dimensions**       | 102mmx69mm                                                                                                                       |
| **Power**            | 7V-36V, 5.5mm in (Twist and Lock mechanism)                                                                                      |
| **Environment**      | Optional metal enclosure                                                                                                         |
|                      | [Buy Now](https://shop.solid-run.com/product-tag/hummingboard-gate/?_ga=2.164059708.2016484779.1641802897-2012112798.1622706355) |

> \[!INFO] Supported with i.MX6 SOM. For more detailed information about our SOM-i.MX6 series please visit this user manual : [i.MX6 SOM Hardware User Manual](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493466) .

#### Block Diagram

The following figure describes the HummingBoard Gate Block Diagram.

![](../../../../.gitbook/assets/image-20210914-095253.png)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Gate.

![](../../../../.gitbook/assets/image-20211111-101229.png)

Print side connector overview of the HummingBoard Gate.

![](../../../../.gitbook/assets/image-20210914-095337.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* HummingBoard Gate with SOM
* 12V Power adapter (HummingBoard Gate has wide range input of 9V-36V, it is recommended to use 12V power adapter)
* USB to UART cable
* IP router or IP switch

## Booting form an SD card

On the HummingBoard Gate it is possible to boot from different media.

For Booting from an SD card, jumpers need to be setup at J5005 as follows:

![](../../../../.gitbook/assets/image-20211114-094820.png)

> \[!NOTE] Before you set the boot jumpers, please refer to [HummingBoard Edge/Gate Boot Jumpers](../imx6-other-articles/hummingboard-edge-gate-boot-jumpers.md) for more information about J5005.

Once you setup the jumpers, you can apply the following for booting from an SD card.

**1. Downloading the Yocto image**

Download the Yocto image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX6/meta-solidrun-arm-imx6/2024-07-05_ab67695/core-image-weston-sdk-imx6qdlcubox.wic.gz
```

* For more Yocto releases, please visit [Yocto Release](https://solid-run-images.sos-de-fra-1.exo.io/IMX6/meta-solidrun-arm-imx6/).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
gzip -dc core-image-weston-sdk-imx6qdlcubox.wic.gz | dd of=/dev/sdX bs=4M conv=fsync
```

* For more information, please visit [Flashing an SD Card](https://solidrun.atlassian.net/wiki/spaces/developer/pages/288129025) .

> \[!NOTE] Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5. Serial Connection**

Please connect the UART cable to the pins on connector J25 as shown in the below picture, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

![](../../../../.gitbook/assets/image-20211128-114236.png)

> \[!INFO] For more information about J25 connector, please refer to [HummingBoard Gate/Edge UART console](../imx6-other-articles/hummingboard-gate-edge-uart-console.md) .

Once you installed the necessary serial connection software, you should be able to see the following:

![](../../../../.gitbook/assets/image-20210926-110202.png)

* In order to be able to log in , please insert “Yocto” as a username and password as follows:

![](../../../../.gitbook/assets/image-20210926-110919.png)

## Install to eMMC

* You can follow this document [Install to eMMC](https://github.com/SolidRun/documentation/blob/bsp/imx6/debian-11_sr1.md#install-to-emmc) to install Yocto to an eMMC device.

## More Features

#### Internet

* Please check you Ethernet connection.
* Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

* For more detailed information, please refer to [i.MX6 Debian](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287277717) .

**Wi-fi**

* You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1\. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

> \[!NOTE] To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

2\. Install the wpa\_supplicant package:

```
apt-get install wpasupplicant 
```

3\. Edit network interfaces file :

At the bottom of the file, add the following lines to allow wlan as a network connection:

```
cat <<EOF > /etc/network/interfaces.d/wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

EOF
```

4\. Create a configuration file with the relevant ssid:

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

5\. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

* For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

#### Bluetooth

1\. For showing all Bluetooth devices, run the following:

```
apt-get install bluez
hciconfig -a
```

2\. Choose a device, and turn it on:

```
 hciconfig hci0 up
```

3\. Set up the Bluetooth name:

```
hciconfig hci0 name 'SolidRun_Ble'
```

4\. Make your Bluetooth detectable by other devices:

```
hciconfig hci0 piscan
```

5\. If you want to connect to other devices:

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

* For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

#### GPIO pins Control

In order to be able to control the GPIO pins, please refer to [HummingBoard Edge/Gate/CBi GPIO Pins Control](../imx6-other-articles/hummingboard-edge-gate-cbi-gpio-pins-control.md) .

#### MikroBus

For standard use of mikroBUS please refer to [i.MX6 mikroBUS](https://solidrun.atlassian.net/wiki/spaces/developer/pages/286949444) .

External use of mikroBUS:

* SPI
* UART
* I2C

#### Install GUI Support

> \[!NOTE] Note that HDMI doesn’t display anything by default.

**Wayland**

1\. Install weston :

```
  sudo apt install weston
```

* Connect your HDMI cable and you should be able to see the following :

![](../../../../.gitbook/assets/IMG-6928-20211014-134838.jpg)

> \[!NOTE] `By default one application is available, the terminal emulator, at the upper left corner.`

2\. Start weston FROM A PHYSICAL TERMINAL (from the above terminal, not remote or serial session):

```
  weston-launch -- --backend=drm-backend.so
```

> \[!WARNING] Make sure to run the above without sudo.

This will bring up the following:

![](../../../../.gitbook/assets/IMG-6920-20211014-132727.jpg)

* For more applications, you can refer to [GUI Support](https://github.com/SolidRun/documentation/blob/bsp/imx6/debian-11_sr1.md#wayland) to install X11, OpenGL-ES, GStreamer, or you can follow this page [Gnome](https://linuxhint.com/install_gnome_debian_10_minimal_server/) for installing Gnome desktop.

## List Of Supported OS

| **OS**                                                     |                                                                                         |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| ![](../../../../.gitbook/assets/image-20211223-104106.png) | [i.MX6 Debian](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287277717)    |
| ![](../../../../.gitbook/assets/image-20211223-104124.png) | [Yocto for i.MX6](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287277558) |
| ![](../../../../.gitbook/assets/image-20211223-104144.png) | [i.MX6 Archlinux](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179285) |
| ![](../../../../.gitbook/assets/image-20211223-104259.png) | [XBian for i.MX6](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287212021) |

## Build U-Boot & Kernel from sources

* Build a Linux kernel -  [i.MX6 Kernel](https://solidrun.atlassian.net/wiki/spaces/developer/pages/286916713)
* Build a U-Boot - [i.MX6 U-Boot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179374)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                                                        | File                                                                                                                                                                | Modified                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-9d561afc-3b19-4519-bcfe-070e4be1cb22">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard+Gate+BOM++rev+1.4.2.xlsx">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>        | Microsoft Excel Spreadsheet [HummingBoard Gate BOM rev 1.4.2.xlsx](../../../../wiki/download/attachments/269975555/HummingBoard%20Gate%20BOM%20%20rev%201.4.2.xlsx) | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-e5ac9e66-0c08-4202-93ac-23586e44f7da">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/mikrobus_specification-rev2.pdf">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>              | PDF File [mikrobus\_specification-rev2.pdf](../../../../wiki/download/attachments/269975555/mikrobus_specification-rev2.pdf)                                        | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-20b494cb-cf42-4868-8e70-d5e022e8bb71">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard2-v1.4-layout_pcb.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>            | ZIP Archive [HummingBoard2-v1.4-layout\_pcb.zip](../../../../wiki/download/attachments/269975555/HummingBoard2-v1.4-layout_pcb.zip)                                 | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-623587d3-d096-46c5-8d5a-3555035ceed2">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard2-gerber-rev1.2.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>              | ZIP Archive [HummingBoard2-gerber-rev1.2.zip](../../../../wiki/download/attachments/269975555/HummingBoard2-gerber-rev1.2.zip)                                      | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-cb232133-2475-4b33-b4d3-3f172375c8c4">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/rtc-datasheet-onboard.pdf">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                    | PDF File [rtc-datasheet-onboard.pdf](../../../../wiki/download/attachments/269975555/rtc-datasheet-onboard.pdf)                                                     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-3426c6c3-5619-49f3-821b-327012a11360">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard2+PCB+parts+assembly+Rev+1.4.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | ZIP Archive [HummingBoard2 PCB parts assembly Rev 1.4.zip](../../../../wiki/download/attachments/269975555/HummingBoard2%20PCB%20parts%20assembly%20Rev%201.4.zip)  | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-f2eec1de-1d39-4a84-ab93-b2dcb95766a9">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard2+Schematics.pdf">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                 | PDF File [HummingBoard2 Schematics.pdf](../../../../wiki/download/attachments/269975555/HummingBoard2%20Schematics.pdf)                                             | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-e9a950bf-c514-415c-a785-a8b78198d608">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard2+Assembly-Files.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>             | ZIP Archive [HummingBoard2 Assembly-Files.zip](../../../../wiki/download/attachments/269975555/HummingBoard2%20Assembly-Files.zip)                                  | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-gate-quick-start-guide.md#section-6aebe2f0-f713-4d43-91a3-eb37dcbb8b27">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/269975555/HummingBoard2+Enclosure-Files.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>            | ZIP Archive [HummingBoard2 Enclosure-Files.zip](../../../../wiki/download/attachments/269975555/HummingBoard2%20Enclosure-Files.zip)                                | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |

[Download All](../../../../wiki/download/all_attachments)

[Buy a Sample Now](https://shop.solid-run.com/product-tag/hummingboard-gate/?_ga=2.164059708.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
