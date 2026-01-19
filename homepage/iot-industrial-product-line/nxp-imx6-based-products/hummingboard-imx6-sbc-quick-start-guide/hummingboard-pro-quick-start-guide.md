# HummingBoard Pro Quick Start Guide

![](<../../../../.gitbook/assets/HummingBoard Pro sideways(large).png>)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Revision** | **Notes**       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | --------------- |
| 14 Nov 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.0          | Initial release |
| Table of Contents | <p>- <a href="hummingboard-pro-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-pro-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-pro-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-pro-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="hummingboard-pro-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-pro-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-pro-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-pro-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-pro-quick-start-guide.md#booting-form-an-sd-card">Booting form an SD card</a><br>- <a href="hummingboard-pro-quick-start-guide.md#install-to-emmc">Install to eMMC</a><br>- <a href="hummingboard-pro-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-pro-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-pro-quick-start-guide.md#wi-fi">Wi-fi</a><br>- <a href="hummingboard-pro-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-pro-quick-start-guide.md#gpio-pins-control">GPIO pins Control</a><br>- <a href="hummingboard-pro-quick-start-guide.md#serial-uart-port-access">Serial UART port access</a><br>- <a href="hummingboard-pro-quick-start-guide.md#install-gui-support">Install GUI Support</a><br>- <a href="hummingboard-pro-quick-start-guide.md#wayland">Wayland</a><br>- <a href="hummingboard-pro-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-pro-quick-start-guide.md#build-u-boot-kernel-from-sources">Build U-Boot &#x26; Kernel from sources</a><br>- <a href="hummingboard-pro-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-pro-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Introduction

The following quick start guide provides background information about the [HummingBoard Pro](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx6-family/hummingboard/#pro) product which use the i.MX6 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Hardware Setup

#### Product Specifications

|                      |                                       |
| -------------------- | ------------------------------------- |
| **SOM Model**        | NXP i.MX6 based Solo to Quad Core SOM |
| **Memory & Storage** | Up to 2GB DDR3\*                      |
|                      | uSD, mSATA\*\*                        |
| **Connectivity**     | 1xRJ-45\*\*\*                         |
|                      | 2xHost USB 2.0                        |
|                      | 2xHeader USB 2.0                      |
|                      | Mini-PCIe- half size                  |
| **Media**            | HDMI-Out                              |
|                      | LVDS                                  |
|                      | SPDIF                                 |
|                      | Analog Audio                          |
|                      | MIPI- CSI-2 Camera                    |
| **I/O**              | Reset Button                          |
|                      | 26 pins GPIO Header                   |
|                      | RTC                                   |
|                      | IR                                    |
| **OS Support**       | Linux                                 |
| **Dimensions**       | 85mmx56mm                             |
| **Power**            | 5V, uUSB                              |
| **Environment**      | No enclosure                          |

{% hint style="info" %}
Supported with i.MX6 SOM. For more detailed information about our SOM-i.MX6 series please visit this user manual : [i.MX6 SOM Hardware User Manual](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493466).
{% endhint %}


{% hint style="info" %}
**Please Note** (\*) RAM type and speed dependent on SOM\
(\*\*) Supported with SOM i.MX6 Dual and above\
(\*\*\*) 1000 Mbps link is limited to 470Mbps actual bandwidth due to internal chip buses
{% endhint %}


#### **Block Diagram**

The following figure describes the Hummingboard Pro Block Diagram.

![](<../../../../.gitbook/assets/HummingBoard Pro block diagram-20211118-135646.png>)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Pro.

![](../../../../.gitbook/assets/image-20211118-140416.png)

Print side connector overview of the HummingBoard Pro

![](../../../../.gitbook/assets/image-20211118-140500.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* HummingBoard Base/Pro with SOM
* 5V mirco USB power adapter
* USB to UART cable
* IP router or IP switch

## Booting form an SD card

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

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5. Serial connection**

Please connect the UART cable to your device pins, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

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

{% hint style="info" %}
To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).
{% endhint %}


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

{% hint style="info" %}
Check your personal ssids by running : ‘iw dev wlan0 scan’
{% endhint %}


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

#### GPIO pins Control

In order to be able to control the GPIO pins, please refer to [HummingBoard Pro/Base GPIOs](../imx6-other-articles/hummingboard-pro-base-gpios.md) .

### Serial UART port access

![](../../../../.gitbook/assets/image-20211209-085945.png)

The UART port for debug can be accessed on the 26 pin header as follows –

Pin 6/9/14/20/25 GND\
Pin 1 3.3V\
Pin 8 buffered i.MX6 UART TX – pulled up to 3.3v\
Pin 10 buffered i.MX6 UART RX – pulled up to 3.3v

{% hint style="info" %}
Notice that the pin number starts as pin #1 on the edge of the board, then number #2 is the one towards the corner of the board.
{% endhint %}


#### Install GUI Support

{% hint style="info" %}
Note that HDMI doesn’t display anything by default.
{% endhint %}


**Wayland**

1\. Install weston :

```
  sudo apt install weston
```

* Connect your HDMI cable and you should be able to see the following :

![](../../../../.gitbook/assets/IMG-6928-20211014-134838.jpg)

{% hint style="info" %}
By default one application is available, the terminal emulator, at the upper left corner.
{% endhint %}


2\. Start weston FROM A PHYSICAL TERMINAL (from the above terminal, not remote or serial session):

```
  weston-launch -- --backend=drm-backend.so
```

{% hint style="warning" %}
Make sure to run the above without sudo.
{% endhint %}


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

|                                                                                                                                                                                                                                                                                                                                                                                                                                  | File                                                                                                                                                           | Modified                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pro-quick-start-guide.md#section-0fe53e19-1e0a-4dd4-a12a-5ee7d114759c">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/270631039/HummingBoard-BasePro-Assembly-Files.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | ZIP Archive [HummingBoard-BasePro-Assembly-Files.zip](../../../../wiki/download/attachments/270631039/HummingBoard-BasePro-Assembly-Files.zip)                 | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pro-quick-start-guide.md#section-648e88e6-869f-444e-b05c-7207623a2dc6">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/270631039/hummingboard-pro-rev-3.5-layout.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>     | ZIP Archive [hummingboard-pro-rev-3.5-layout.zip](../../../../wiki/download/attachments/270631039/hummingboard-pro-rev-3.5-layout.zip)                         | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pro-quick-start-guide.md#section-29090707-f50e-496c-9b92-cf630f45a08b">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/270631039/HummingBoard-BasePro-Gerbers.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>        | ZIP Archive [HummingBoard-BasePro-Gerbers.zip](../../../../wiki/download/attachments/270631039/HummingBoard-BasePro-Gerbers.zip)                               | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pro-quick-start-guide.md#section-0d680cfb-5d23-489e-8c3e-2593ba828e58">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/270631039/HummingBoard+Pro+BOM+Rev+3.5.1.xlsx">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>     | Microsoft Excel Spreadsheet [HummingBoard Pro BOM Rev 3.5.1.xlsx](../../../../wiki/download/attachments/270631039/HummingBoard%20Pro%20BOM%20Rev%203.5.1.xlsx) | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pro-quick-start-guide.md#section-e6bbc6c9-e8c2-4427-8634-3ea659436cab">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/270631039/HummingBoard-BasePro-Schematics.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>     | ZIP Archive [HummingBoard-BasePro-Schematics.zip](../../../../wiki/download/attachments/270631039/HummingBoard-BasePro-Schematics.zip)                         | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |

[Download All](../../../../wiki/download/all_attachments)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
