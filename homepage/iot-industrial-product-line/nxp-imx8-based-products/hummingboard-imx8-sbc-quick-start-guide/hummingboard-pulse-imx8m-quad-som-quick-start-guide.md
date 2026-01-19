# HummingBoard Pulse & i.MX8M Quad SOM Quick Start Guide

![](<../../../../.gitbook/assets/HummingBoard Pulse with i.MX8 plus sideways (small).png>)

## Introduction

The following quick start guide provides background information about the [HummingBoard Pulse](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/hummingboard-m/#pulse2post_typeproduct).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Revision** | **Notes**       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 28 Oct 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1.0          | Initial release |
| Table of Contents | <p>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#product-specifications">Product specifications</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#booting-from-sd-card">Booting from SD card</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#wifi">WiFi</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#cellular-modem">Cellular Modem</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Hardware Setup

#### Product specifications

| **Model**        | **HummingBoard Pulse**                                                                                                                                                                                                                                                      |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SOM Model        | <p>NXP i.MX8M Dual / Quad core Arm Cortex A53 up to 1.5GHz (with Arm M4 GPP)<br><br>NXP i.MX8M Mini Single to Quad core Arm Cortex A53 up to 1.8GHz (with Arm M4 GPP)</p>                                                                                                   |
| Memory & Storage | <p>Up to 4GB LPDDR4<br>eMMC<br>MicroSD</p>                                                                                                                                                                                                                                  |
| Network          | 2 x RJ45                                                                                                                                                                                                                                                                    |
| Connectivity     | <p>2 x USB 3.0 *<br>Mini PCIe<br>M.2<br>SIM card slot</p>                                                                                                                                                                                                                   |
| Media            | <p>HDMI 2.0 out **<br>MIPI-DSI<br>2 x MIPI-CSI ***<br>Digital audio (Riser interface FPC connector)<br><br>Onboard audio codec</p>                                                                                                                                          |
| I/O              | <p>1 x Reset button<br>1 x Configurable push button<br>MikroBus click interface<br>3 x LED indicators<br>RTC</p>                                                                                                                                                            |
| OS Support       | Linux                                                                                                                                                                                                                                                                       |
| Environment      | <p>Commercial:<br>Ambient temp.: 0°C to 70°C<br>Enclosed ambient temp.: 0°C to 40°C<br>CPU max die: 105°C<br><br>Industrial:<br>Ambient temp.: -40°C to 85°C<br>Enclosed Ambient temp.: -25°C to 65°C<br>CPU max die: 105°C<br><br>Humidity (non-condensing): 10% – 90%</p> |
| Dimensions       | <p>Board: 102mm x 69mm<br>Enclosed: 141.5 x 78 x 30mm</p>                                                                                                                                                                                                                   |
| Power            | <p>7V – 28V wide range<br>PoE sink support</p>                                                                                                                                                                                                                              |
| Enclosure        | Optional extruded aluminum (IP32) enclosure                                                                                                                                                                                                                                 |
|                  | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22\&post_type=product)                                                                                                                                                                                        |

{% hint style="info" %}
Supported with i.MX8M SOM. For more detailed information about our SOM-i.MX8M series please visit this user manual : [i.MX8M SOM](https://solidrun.atlassian.net/wiki/pages/resumedraft.action?draftId=287899798) .
{% endhint %}


{% hint style="info" %}
**Please note** (\*) Only USB 2.0 supported with the i.MX8M Mini SoC.\
(\*\*) Only supported with the i.MX8M SoC.\
(\*\*\*) Only 1 x MIPI-CSI supported with the i.MX8M Mini SoC.
{% endhint %}


#### Block Diagram

The following figure describes the i.MX8M Block Diagram.

![](<../../../../.gitbook/assets/HummingBoard Pulse Block Diagram-20211028-085843.png>)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Pulse.

![](../../../../.gitbook/assets/image-20211107-114400.png)

Print side connector overview of the HummingBoard Pulse.

![](../../../../.gitbook/assets/image-20211028-091109.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard Pulse with SOM
* 12V Power adapter (HummingBoard Pulse has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
* Micro USB to USB for console, the HummingBoard Pulse has an onboard FTDI chip.
* IP router or IP switch

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [HummingBoard Pulse and Ripple Boot Select](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287343073) .

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![](../../../../.gitbook/assets/image-20211107-114816.png)

{% hint style="info" %}
Please Note: The black rectangle represents the switch position.
{% endhint %}


Once you set the switches, you can apply the following for booting from SD card:

**1. Downloading the Debian image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/Debian/sr-imx8-debian-bullseye-20201020-cli-imx8mq-sdhc-hummingboard-pulse.img.xz
```

* For more Debian releases, please visit [Debian Release for i.MX8](https://images.solid-run.com/IMX8/Debian).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc sr-imx8-debian-bullseye-20201020-cli-imx8mq-sdhc-hummingboard-pulse.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

* For more information, please visit Flashing an SD card.

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](<../../../../.gitbook/assets/image-20210926-110202 (3).png>)

* In order to be able to log in , please insert “debian” as a username and password as follows:

![](<../../../../.gitbook/assets/image-20210926-110919 (3).png>)

## More Features

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).\
Models HummingBoard with WiFi, can be connected via [WiFi](../cubox-m-quick-start-guide.md#wifi) or wired Ethernet.

* Please check you Ethernet connection.
* Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

* For more detailed information, please refer to [i.MX8M Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr.md) .

**WiFi**

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

For Building Newt Nimble BLEHCI firmware, you can follow this page [Building Newt Nimble BLEHCI firmware for the iMX8MQ NINA-B1 Module](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179461) .

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

* For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

{% hint style="info" %}
Please Note: In order to use the mini-PCIe, a HummingBoard Pulse must not be combined with a microSOM that has WIFI. For more information, please refer to: [mini-PCIe](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr.md#mini-pcie-by-default-not-functional-on-hummingboard-pulse)
{% endhint %}


## List Of Supported OS

| **OS**                                                           |                                                                                   |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| ![](<../../../../.gitbook/assets/image-20211024-150854 (1).png>) | [Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr.md) |
| ![](<../../../../.gitbook/assets/image-20211024-150920 (1).png>) | [Buildroot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/286916774) |

## Build from source

* [i.MX8M Software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493777)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                                                                     | File                                                                                                                                                     | Modified                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-ceb6f861-112c-424b-9603-6ec985252772">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard-Pulse-Part-Assembly.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>      | ZIP Archive [HummingBoard-Pulse-Part-Assembly.zip](../../../../wiki/download/attachments/266928147/HummingBoard-Pulse-Part-Assembly.zip)                 | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-b5c3e84e-80d0-474f-b4bf-6a53a7759f01">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard+iMX8+Schematics.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>          | ZIP Archive [HummingBoard iMX8 Schematics.zip](../../../../wiki/download/attachments/266928147/HummingBoard%20iMX8%20Schematics.zip)                     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-82ff3547-4b85-4227-a602-11c37718000c">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard+iMX8+Mechanical+Drawings.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | ZIP Archive [HummingBoard iMX8 Mechanical Drawings.zip](../../../../wiki/download/attachments/266928147/HummingBoard%20iMX8%20Mechanical%20Drawings.zip) | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-bf237681-e48d-4f29-9542-c0326770783d">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard+Puls-REV.2.5-pcb.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>         | ZIP Archive [HummingBoard Puls-REV.2.5-pcb.zip](../../../../wiki/download/attachments/266928147/HummingBoard%20Puls-REV.2.5-pcb.zip)                     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-bde353b9-c3a0-44fd-a301-4ec29bb8764b">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard+iMX8+PCB.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                 | ZIP Archive [HummingBoard iMX8 PCB.zip](../../../../wiki/download/attachments/266928147/HummingBoard%20iMX8%20PCB.zip)                                   | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-9de08daa-1fc9-42d7-8304-bf0bf9540d22">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard+iMX8+Gerbers.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>             | ZIP Archive [HummingBoard iMX8 Gerbers.zip](../../../../wiki/download/attachments/266928147/HummingBoard%20iMX8%20Gerbers.zip)                           | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-quad-som-quick-start-guide.md#section-dae990d5-9f28-450e-800e-ea9f3501238d">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/266928147/HummingBoard+Pulse+Pin+MUX.xlsx">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>           | Microsoft Excel Spreadsheet [HummingBoard Pulse Pin MUX.xlsx](../../../../wiki/download/attachments/266928147/HummingBoard%20Pulse%20Pin%20MUX.xlsx)     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |

* Drag and drop to upload or \[browse for files]&#x20;

Upload file

File description

[Download All](../../../../wiki/download/all/_attachments)[ Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22\&post\\_type=product)

### Related Articles <a href="#hummingboardpulse-and-i.mx8mquadsomquickstartguide-relatedarticles" id="hummingboardpulse-and-i.mx8mquadsomquickstartguide-relatedarticles"></a>

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
