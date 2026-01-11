# HummingBoard Pulse &  i.MX8M Quad SOM Quick Start Guide

![](./attachments/HummingBoard%20Pulse%20with%20i.MX8%20plus%20sideways%20(small).png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [HummingBoard Pulse](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/hummingboard-m/#pulse2post_typeproduct).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 28 Oct 2021 |     | 1.0 | Initial release |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product specifications](#product-specifications)<br>  - [Block Diagram](#block-diagram)<br>  - [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Boot Select](#boot-select)<br>- [Booting from SD card](#booting-from-sd-card)<br>- [More Features](#more-features)<br>  - [Internet](#internet)<br>    - [WiFi](#wifi)<br>  - [Bluetooth](#bluetooth)<br>  - [Cellular Modem](#cellular-modem)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product specifications

| **Model** | **HummingBoard Pulse** |
| --- | --- |
| SOM Model | NXP i.MX8M Dual / Quad core Arm Cortex A53 up to 1.5GHz (with Arm M4 GPP)<br><br>NXP i.MX8M Mini Single to Quad core Arm Cortex A53 up to 1.8GHz (with Arm M4 GPP) |
| Memory & Storage | Up to 4GB LPDDR4  <br>eMMC  <br>MicroSD |
| Network | 2 x RJ45 |
| Connectivity | 2 x USB 3.0 \*  <br>Mini PCIe  <br>M.2  <br>SIM card slot |
| Media | HDMI 2.0 out \*\*  <br>MIPI-DSI  <br>2 x MIPI-CSI \*\*\*  <br>Digital audio (Riser interface FPC connector)<br><br>Onboard audio codec |
| I/O | 1 x Reset button  <br>1 x Configurable push button  <br>MikroBus click interface  <br>3 x LED indicators  <br>RTC |
| OS Support | Linux |
| Environment | Commercial:  <br>Ambient temp.: 0°C to 70°C  <br>Enclosed ambient temp.: 0°C to 40°C  <br>CPU max die: 105°C<br><br>Industrial:  <br>Ambient temp.: -40°C to 85°C  <br>Enclosed Ambient temp.: -25°C to 65°C  <br>CPU max die: 105°C<br><br>Humidity (non-condensing): 10% – 90% |
| Dimensions | Board: 102mm x 69mm  <br>Enclosed: 141.5 x 78 x 30mm |
| Power | 7V – 28V wide range  <br>PoE sink support |
| Enclosure | Optional extruded aluminum (IP32) enclosure |
|     | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product) |

> [!INFO]
> Supported with i.MX8M SOM. For more detailed information about our SOM-i.MX8M series please visit this user manual : [i.MX8M SOM](https://solidrun.atlassian.net/wiki/pages/resumedraft.action?draftId=287899798) .

> [!NOTE]
> **Please note**
> (\*) Only USB 2.0 supported with the i.MX8M Mini SoC.  
> (\*\*) Only supported with the i.MX8M SoC.  
> (\*\*\*) Only 1 x MIPI-CSI supported with the i.MX8M Mini SoC.

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the i.MX8M Block Diagram.

![](./attachments/HummingBoard%20Pulse%20Block%20Diagram-20211028-085843.png)

<a id="visual-features-overview"></a>

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Pulse.

![](./attachments/image-20211107-114400.png)

Print side connector overview of the HummingBoard Pulse.

![](./attachments/image-20211028-091109.png)

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

- Linux or Windows PC
- HummingBoard Pulse with SOM
- 12V Power adapter (HummingBoard Pulse has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
- Micro USB to USB for console, the HummingBoard Pulse has an onboard FTDI chip.
- IP router or IP switch

<a id="boot-select"></a>

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [HummingBoard Pulse and Ripple Boot Select](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287343073) .

<a id="booting-from-sd-card"></a>

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![](./attachments/image-20211107-114816.png)

> [!INFO]
> Please Note:
> The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from SD card:

**1\. Downloading the Debian image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/Debian/sr-imx8-debian-bullseye-20201020-cli-imx8mq-sdhc-hummingboard-pulse.img.xz
```

- For more Debian releases, please visit [Debian Release for i.MX8](https://images.solid-run.com/IMX8/Debian).

**2\. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc sr-imx8-debian-bullseye-20201020-cli-imx8mq-sdhc-hummingboard-pulse.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

- For more information, please visit Flashing an SD card.

> [!NOTE]
> Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

**3\. SD card insertion**

Please Insert the SD card into your device.

**4\. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5\. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](./attachments/image-20210926-110202.png)

- In order to be able to log in , please insert “debian” as a username and password as follows:

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

- For more detailed information, please refer to [i.MX8M Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr.md) .

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

For Building Newt Nimble BLEHCI firmware, you can follow this page [Building Newt Nimble BLEHCI firmware for the iMX8MQ NINA-B1 Module](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179461) .

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

> [!INFO]
> Please Note:
> In order to use the mini-PCIe, a HummingBoard Pulse must not be combined with a microSOM that has WIFI.
> For more information, please refer to: [mini-PCIe](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr.md#mini-pcie-by-default-not-functional-on-hummingboard-pulse)

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211024-150854.png) | [Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr.md) |
| ![](./attachments/image-20211024-150920.png) | [Buildroot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/286916774) |

<a id="build-from-source"></a>

## Build from source

- [i.MX8M Software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493777)

<a id="documentation"></a>

## Documentation

     

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-ceb6f861-112c-424b-9603-6ec985252772)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard-Pulse-Part-Assembly.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard-Pulse-Part-Assembly.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard-Pulse-Part-Assembly.zip) | ZIP Archive [HummingBoard-Pulse-Part-Assembly.zip](/wiki/download/attachments/266928147/HummingBoard-Pulse-Part-Assembly.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-b5c3e84e-80d0-474f-b4bf-6a53a7759f01)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard+iMX8+Schematics.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard+iMX8+Schematics.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard+iMX8+Schematics.zip) | ZIP Archive [HummingBoard iMX8 Schematics.zip](/wiki/download/attachments/266928147/HummingBoard%20iMX8%20Schematics.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-82ff3547-4b85-4227-a602-11c37718000c)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard+iMX8+Mechanical+Drawings.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip) | ZIP Archive [HummingBoard iMX8 Mechanical Drawings.zip](/wiki/download/attachments/266928147/HummingBoard%20iMX8%20Mechanical%20Drawings.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-bf237681-e48d-4f29-9542-c0326770783d)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard+Puls-REV.2.5-pcb.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard+Puls-REV.2.5-pcb.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard+Puls-REV.2.5-pcb.zip) | ZIP Archive [HummingBoard Puls-REV.2.5-pcb.zip](/wiki/download/attachments/266928147/HummingBoard%20Puls-REV.2.5-pcb.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-bde353b9-c3a0-44fd-a301-4ec29bb8764b)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard+iMX8+PCB.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard+iMX8+PCB.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard+iMX8+PCB.zip) | ZIP Archive [HummingBoard iMX8 PCB.zip](/wiki/download/attachments/266928147/HummingBoard%20iMX8%20PCB.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-9de08daa-1fc9-42d7-8304-bf0bf9540d22)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard+iMX8+Gerbers.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard+iMX8+Gerbers.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard+iMX8+Gerbers.zip) | ZIP Archive [HummingBoard iMX8 Gerbers.zip](/wiki/download/attachments/266928147/HummingBoard%20iMX8%20Gerbers.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-dae990d5-9f28-450e-800e-ea9f3501238d)<br><br>[Preview] [View](/wiki/download/attachments/266928147/HummingBoard+Pulse+Pin+MUX.xlsx?version=1) [Properties](/wiki/pages/editattachment.action?pageId=266928147&fileName=HummingBoard+Pulse+Pin+MUX.xlsx&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=266928147&fileName=HummingBoard+Pulse+Pin+MUX.xlsx) | Microsoft Excel Spreadsheet [HummingBoard Pulse Pin MUX.xlsx](/wiki/download/attachments/266928147/HummingBoard%20Pulse%20Pin%20MUX.xlsx?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |

- Drag and drop to upload or [browse for files] ![](/wiki/images/icons/wait.gif)

Upload file 

File description  

</form> </div> </div> <div> <a class="download-all-link" href="/wiki/download/all\_attachments?pageId=266928147" title="Download all the latest versions of attachments on this content as single zip file.">Download All</a> </div> </div> </div> </div> </div> <div class="columnLayout three-equal" data-layout="three-equal"> <div class="cell normal" data-type="normal"> <div class="innerCell"> <p /></div> </div> <div class="cell normal" data-type="normal"> <div class="innerCell"> <a class="external-link" href="https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&amp;post\_type=product" rel="nofollow" style="display: inline-block;padding: 0 15.0px;height: 32.0px;font-size: 14.0px;line-height: 32.0px;background: rgb(236,63,63);color: rgb(255,255,255);cursor: pointer;border-radius: 2.0px;margin-right: 10.0px;" title=""><style>\[data-colorid=s643wtjmh3\]{color:#0747a6} html\[data-color-mode=dark\] \[data-colorid=s643wtjmh3\]{color:#5999f8}\[data-colorid=zyk6p8jkgd\]{color:#ff5630} html\[data-color-mode=dark\] \[data-colorid=zyk6p8jkgd\]{color:#cf2600}\[data-colorid=yipoonehwq\]{color:#0747a6} html\[data-color-mode=dark\] \[data-colorid=yipoonehwq\]{color:#5999f8}\[data-colorid=outcpwr8mo\]{color:#6554c0} html\[data-color-mode=dark\] \[data-colorid=outcpwr8mo\]{color:#503fab}</style> Buy a Sample Now </a></div> </div> <div class="cell normal" data-type="normal"> <div class="innerCell"> <p /></div> </div> </div> <div class="columnLayout fixed-width" data-layout="fixed-width"> <div class="cell normal" data-type="normal"> <div class="innerCell"> <p /><h2 id="HummingBoardPulse&amp;i.MX8MQuadSOMQuickStartGuide-RelatedArticles">Related Articles</h2><div class="error">Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden</div><p /><p /></div> </div> </div> </div></x-turndown>