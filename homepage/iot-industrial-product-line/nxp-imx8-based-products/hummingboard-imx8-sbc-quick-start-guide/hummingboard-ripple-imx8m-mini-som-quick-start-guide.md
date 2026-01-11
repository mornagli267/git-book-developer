# HummingBoard Ripple &  i.MX8M Mini SOM Quick Start Guide

![](./attachments/image-20211104-104216.png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [HummingBoard Ripple](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/hummingboard-m/#ripple).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 04 Nov 2021 |     | 1.0 | Initial release |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product specifications](#product-specifications)<br>  - [Model](#model)<br>  - [HumingBoard Ripple](#humingboard-ripple)<br>  - [Block Diagram](#block-diagram)<br>  - [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Boot Select](#boot-select)<br>- [Booting from SD card](#booting-from-sd-card)<br>- [More Features](#more-features)<br>  - [Internet](#internet)<br>    - [WiFi](#wifi)<br>  - [Bluetooth](#bluetooth)<br>  - [GPIO Pins Control](#gpio-pins-control)<br>  - [Cellular Modem](#cellular-modem)<br>  - [GPIO pins Control](#gpio-pins-control)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product specifications

|     |     |
| --- | --- |
| <a id="model"></a><br><br>#### Model | <a id="humingboard-ripple"></a><br><br>#### HumingBoard Ripple |
| SOM Model | NXP i.MX8M Dual / Quad core Arm Cortex A53 up to 1.5GHz (with Arm M4 GPP) |
|     | NXP i.MX8M Mini Single to Quad core Arm Cortex A53 up to 1.8GHz (with Arm M4 GPP) |
| Memory & Storage | Up to 4GB LPDDR4 |
|     | eMMC |
|     | MicroSD |
| Network | 1 x RJ45 |
| Connectivity | 2 x USB 3.0 \* |
|     | Mini PCIe |
|     | SIM card slot |
| Media | Micro-HDMI |
|     | 1 x MIPI-CSI \*\*\* |
| I/O | 1 x Reset button |
|     | 1 x Configurable push button |
|     | MikroBus click interface |
|     | 3 x LED indicators |
|     | RTC |
| OS Support | Linux |
| Environment | Commercial:  <br>Ambient temp.: 0°C to 70°C  <br>Enclosed ambient temp.: 0°C to 40°C  <br>CPU max die: 105°C |
|     | Industrial:  <br>Ambient temp.: -40°C to 85°C  <br>Enclosed Ambient temp.: -25°C to 65°C  <br>CPU max die: 105°C |
|     | Humidity (non-condensing): 10% – 90% |
| Dimensions | Board: 102mm x 69mm |
|     | Enclosed: 141.5 x 78 x 30mm |
| Power | 7V – 28V wide range |
|     | PoE sink support |
| Enclosure | Optional extruded aluminum (IP32) enclosure |
|     | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Ripple%22&post_type=product&_ga=2.89019160.2016484779.1641802897-2012112798.1622706355) |

> [!INFO]
> Supported with i.MX8M-MINI SOM. For more detailed informaiton about our SOM-i.MX8M series please visit our user manual : [i.MX8M Mini SOM Hardware User Manual](../../nxp-imx8-based-products/imx8m-mini-som-hardware-user-manual.md)

> [!NOTE]
> **Please Note**
> (\*) Only USB 2.0 supported with the i.MX8M Mini SoC.  
> (\*\*) Only supported with the i.MX8M SoC.  
> (\*\*\*) Only 1 x MIPI-CSI supported with the i.MX8M Mini SoC.

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the i.MX8M Block Diagram.

![](./attachments/HummingBoard%20Ripple%20block%20diagram%20(1)-20211104-105320.png)

<a id="visual-features-overview"></a>

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Ripple.

![](./attachments/image-20211104-110302.png)

Print side connector overview of the HummingBoard Ripple.

![](./attachments/image-20211104-110340.png)

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

- Linux or Windows PC
- HummingBoard Ripple with SOM
- 12V Power adapter (HummingBoard Ripple has wide range input of 7V-36V, it is recommended to use 12V power adapter).
- Micro USB to USB for console, the HummingBoard Ripple has an onboard FTDI chip.
- IP router or IP switch

<a id="boot-select"></a>

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [HummingBoard Pulse and Ripple Boot Select](../../nxp-imx8-based-products/imx8m-other-articles/hummingboard-pulse-ripple-mate-and-pro-boot-select.md) .

<a id="booting-from-sd-card"></a>

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![](./attachments/image-20211104-141324.png)

> [!INFO]
> Please Note:
> The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from SD card:

1\. Downloading the Debian image

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/Debian/sr-imx8-debian-buster-20210706-cli-imx8mm-sdhc-hummingboard-pulse.img.xz
```

- For more Debian releases, please visit [Debian Releases for i.MX8](https://images.solid-run.com/IMX8/Debian).

2\. Writing the image to the SD card

Use the following commands for writing the image to an SD card:

```
xz -dc sr-imx8-debian-buster-20210706-cli-imx8mm-sdhc-hummingboard-pulse.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync 
```

- For more information, please visit [Flashing an SD Card](../../../../homepage/other-articles/flashing-an-sd-card.md) .

> [!NOTE]
> Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

3\. SD card insertion

Please Insert the SD card into your device.

4\. Power connection

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

5\. Serial Connection

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../../../homepage/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](./attachments/image-20210926-110202.png)

- In order to be able to log in , please insert “root” as a username and password as follows:

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

1\. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

> [!NOTE]
> To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

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

> [!NOTE]
> Check your personal ssids by running : ‘iw dev wlan0 scan’

5\. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

- For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

<a id="bluetooth"></a>

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

<a id="gpio-pins-control"></a>

#### GPIO Pins Control

In order to be able to control the GPIO pins, please refer to [GPIO Pins Control - HummingBoard Ripple/Pulse & i.MX8M Mini SOM](../../nxp-imx8-based-products/imx8m-other-articles/gpio-pins-control-hummingboard-ripple-pulse-imx8m-mini-som.md)

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- For some cellular modules to be connected, please refer to [Cellular Modules](../../../iot-industrial-product-line/nxp-imx6-based-products/imx6-other-articles/cellular-modules.md) .  

<a id="gpio-pins-control"></a>

#### GPIO pins Control

To control on the GPIO pins, please follow this page [GPIO Pins Control - HummingBoard Ripple](../../nxp-imx8-based-products/imx8m-other-articles/gpio-pins-control-hummingboard-ripple-pulse-imx8m-mini-som.md) .

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211024-150854.png) | [Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) |
| ![](./attachments/image-20211024-151110.png) | [i.MX8M Mini Yocto](../../nxp-imx8-based-products/imx8m-plus-mini-nano-software/imx8m-mini-yocto.md) |
| ![](./attachments/image-20211024-150920.png) | [Buildroot](https://github.com/SolidRun/imx8mm_build) |

<a id="build-from-source"></a>

## Build from source

- [i.MX8M Software](https://github.com/SolidRun/imx8mm_build)

<a id="documentation"></a>

## Documentation

      

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-62d60d5d-ae4b-4882-8cd8-5b1f5cab3666)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard+Pulse+Pin+MUX.xlsx?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard+Pulse+Pin+MUX.xlsx&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard+Pulse+Pin+MUX.xlsx) | Microsoft Excel Spreadsheet [HummingBoard Pulse Pin MUX.xlsx](/wiki/download/attachments/267517959/HummingBoard%20Pulse%20Pin%20MUX.xlsx?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-e2ce92dd-9e12-47e7-92ee-02ee8b699c04)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard-Pulse-Part-Assembly.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard-Pulse-Part-Assembly.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard-Pulse-Part-Assembly.zip) | ZIP Archive [HummingBoard-Pulse-Part-Assembly.zip](/wiki/download/attachments/267517959/HummingBoard-Pulse-Part-Assembly.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-9e345556-d5ff-475d-8730-62307b1e1d10)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard+iMX8+Schematics.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard+iMX8+Schematics.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard+iMX8+Schematics.zip) | ZIP Archive [HummingBoard iMX8 Schematics.zip](/wiki/download/attachments/267517959/HummingBoard%20iMX8%20Schematics.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-e1ffe6fe-a57e-46ca-a83e-271152c5f0b9)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard+iMX8+Mechanical+Drawings.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip) | ZIP Archive [HummingBoard iMX8 Mechanical Drawings.zip](/wiki/download/attachments/267517959/HummingBoard%20iMX8%20Mechanical%20Drawings.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-615b67fe-9166-49af-a1ef-40d7abaf6eca)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard+Puls-REV.2.5-pcb.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard+Puls-REV.2.5-pcb.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard+Puls-REV.2.5-pcb.zip) | ZIP Archive [HummingBoard Puls-REV.2.5-pcb.zip](/wiki/download/attachments/267517959/HummingBoard%20Puls-REV.2.5-pcb.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-f89cdeff-9a45-4f56-ad6a-f938edf138ee)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard+iMX8+PCB.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard+iMX8+PCB.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard+iMX8+PCB.zip) | ZIP Archive [HummingBoard iMX8 PCB.zip](/wiki/download/attachments/267517959/HummingBoard%20iMX8%20PCB.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-12d4b185-c0ee-44ed-af5a-2ccef211d3dd)<br><br>[Preview] [View](/wiki/download/attachments/267517959/HummingBoard+iMX8+Gerbers.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=267517959&fileName=HummingBoard+iMX8+Gerbers.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=267517959&fileName=HummingBoard+iMX8+Gerbers.zip) | ZIP Archive [HummingBoard iMX8 Gerbers.zip](/wiki/download/attachments/267517959/HummingBoard%20iMX8%20Gerbers.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |

[Download All](/wiki/download/all_attachments?pageId=267517959)

[ Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Ripple%22&post_type=product&_ga=2.89019160.2016484779.1641802897-2012112798.1622706355)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden