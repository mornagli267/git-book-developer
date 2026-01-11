# ClearFog GTR L8 Quick Start Guide

![](./attachments/image-20220118-094224.png)

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 21 Oct 2021 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Introduction](#introduction)<br>- [Specifications](#specifications)<br>- [Block Diagram](#block-diagram)<br>- [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Recommended Cables](#recommended-cables)<br>- [Boot Select](#boot-select)<br>- [Booting from an eMMC card](#booting-from-an-emmc-card)<br>- [SFP Modules](#sfp-modules)<br>- [SIM Card Slot](#sim-card-slot)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build U-Boot & kernel from sources](#build-u-boot-kernel-from-sources)<br>- [Documentation](#documentation) |     |     |

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [ClearFog GTR L8](https://www.solid-run.com/arm-servers-networking-platforms/clearfog-gtr-a385/#gtr-l8) product.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="specifications"></a>

## Specifications

|     |     |
| --- | --- |
| I/Os | 1 x USB 3.0 |
| Networking | 8 x 1GbE switched LAN supporting 802.3at/af/bt\* (up to type 4) PSE PoE  <br>1 x 1GbE WAN supporting up to 802.3bt type 4 PD PoE  <br>1 x SFP (up to 2.5GbE) |
| Processor | Marvell ARMADA based A385 Dual core Arm Cortex A9 up to 1.3 GHz |
| Memory & Storage | Up to 2GB DDR3  <br>8GB eMMC  <br>MicroSD  <br>2 x 7 pin SATA |
| Display | None |
| Misc. | GPIO header  <br>Indication LEDs  <br>User Push Buttons |
| Development and Debug interfaces | Micro USB |
| Power | 10V – 54V when not enabling PoE PSE \*  <br>48V – 54V when enabling PoE PSE \* |
| Expansion card I/Os | 3 x mPCIe (1 x mPCIe supports LTE with SIM holder) |
| Temperature | Industrial: -40°C to 85°C |
| Dimensions | PCBA: 238 x 130mm  <br>Enclosure : 253 x 132 x 32mm |
| Enclosure | Extruded aluminum |

> [!INFO]
> (\*) 802.3bt supported only on 4 x RJ45 ports (90W each), 802.3at/af is supported on all 8 ports (30W each).

<a id="block-diagram"></a>

## Block Diagram

The following figure describes the **ClearFog GTR L8** Block Diagram.

![](./attachments/image-20220118-094827.png)

<a id="visual-features-overview"></a>

## Visual features overview

Please see below the features overview of the connector side of the ClearFog GTR L8.

![](./attachments/image-20220118-094324.png)

Print side connector overview of the ClearFog GTR L8.

![](./attachments/image-20220118-115832.png)

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up the board:

- Linux or Windows PC
- ClearFog GTR L8
- 48V Power Supply (ClearFog GTR L8 has wide range input of 10V-54V, it is recommended to use 48V)
- Micro USB to USB for console, the ClearFog Pro has an onboard FTDI chip.
- IP router or IP switch

> [!INFO]
> The ClearFog GTR L8 has a wide range of 10V-54V input power supplies:
> - 10V – 54V when not enabling PoE PSE
> - 48V – 54V when enabling PoE PSE

<a id="recommended-cables"></a>

## Recommended Cables

The following is a list of industry-standard cables, sorted by type, with the necessary compliance requirements that have been proven to work well with the ClearFog product family (ClearFog Base / Pro).

These examples are the cables which SolidRun uses for testing, and should provide enough information to source products from your preferred cable vendor.

- Ethernet cable: Monoprice 24AWG Cat6A 500MHz STP
- USB Cable: SuperSpeed USB 3.0 Type A Male to Female Extension Cable in Black
- SFP connector: GigaLite GE-GB-P1RT-E SFP module with Monoprice 24AWG Cat6A 500MHz STP cable

<a id="boot-select"></a>

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [ClearFog GTR Boot Select](https://solidrun.atlassian.net/wiki/spaces/developer/pages/301432842) .

<a id="booting-from-an-emmc-card"></a>

## Booting from an eMMC card

The switches on the boot source selector must be set as follows:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| OFF | OFF | ON  | ON  | ON  |

The following shows how to set the switches on the boot source selector:

![](./attachments/image-20220118-105955.png)

> [!TIP]
> The ClearFog GTR including [U-Boot](https://solid-run-images.sos-de-fra-1.exo.io/A38X/U-Boot/u-boot-clearfog-gtr-mmc.kwb) into eMMC by default.
> **Note:** Here can find the U-Boot Binaries - [SolidRun Images](https://images.solid-run.com/A38X/U-Boot)

Once you set the switches, you can apply the following for booting from an eMMC card.

**1\. Downloading the Debian image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/A38X/Debian/sr-a38x-debian-buster-20200114.img.xz
```

- For more Debian releases, please visit [Debian Releases for Armada 38X](https://images.solid-run.com/A38X/Debian).

**2\. Writing the image to the USB Disk card**

Use the following commands for writing the image to an USB Disk:

```
xz -dc sr-a38x-debian-buster-20200114.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

- For more information, please visit [Flashing an SD Card](https://solidrun.atlassian.net/wiki/spaces/developer/pages/288129025) .

> [!NOTE]
> Note: Plug a USB Disk into your Linux PC, the following assumes that the USB is added as /dev/sdX and all it’s partitions are unmounted.

**3\. USB Disk insertion**

Please Insert the USB Disk into your device.

**4\. Power connection**

Connect your power adapter to the DC jack, and then connect the adapter to mains supply.

**5\. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](./attachments/image-20211212-115306.png)

- In order to be able to log in , please insert “debian” as a username and password as follows:

![](./attachments/image-20211212-115539.png)

<a id="sfp-modules"></a>

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287212203) .

<a id="sim-card-slot"></a>

## SIM Card Slot

It is possible to utilize a Cellular connection by inserting a SIM card into the SIM card slot. Please observe that a GSM Cellular modem needs to be installed utilizing the mini PCIe connection in order to exploit the cellular connection.

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211223-141905.png) | [A38X Buildroot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287277587) |
| ![](./attachments/image-20211223-141939.png) | [Yocto](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287277178) |
| ![](./attachments/image-20220118-112849.png) | [Debian](https://images.solid-run.com/A38X/Debian) |
| ![](./attachments/image-20220119-065742.png) | [OpenWrt](https://solidrun.atlassian.net/wiki/spaces/developer/pages/302055435) |

<a id="build-u-boot-kernel-from-sources"></a>

## Build U-Boot & kernel from sources

- U-Boot Build - [A38X U-Boot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287212134)
- Kernel Build - [A38X Kernel](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287244407)

<a id="documentation"></a>

## Documentation

      

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-e4e9f267-b88f-491d-a618-0ab3a208c4cc)<br><br>[Preview] [View](/wiki/download/attachments/287703150/ClearFog+GTR+L8+Mechanics+Production+Files.rar?version=1) [Properties](/wiki/pages/editattachment.action?pageId=287703150&fileName=ClearFog+GTR+L8+Mechanics+Production+Files.rar&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=287703150&fileName=ClearFog+GTR+L8+Mechanics+Production+Files.rar) | File [ClearFog GTR L8 Mechanics Production Files.rar](/wiki/download/attachments/287703150/ClearFog%20GTR%20L8%20Mechanics%20Production%20Files.rar?api=v2) | Jan 18, 2022 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-42eff9e2-c465-4880-8ece-d23616e2db3b)<br><br>[Preview] [View](/wiki/download/attachments/287703150/ClearFog+GTR+L8+Documentation+Board+%26+Assembly+Models.rar?version=1) [Properties](/wiki/pages/editattachment.action?pageId=287703150&fileName=ClearFog+GTR+L8+Documentation+Board+%26+Assembly+Models.rar&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=287703150&fileName=ClearFog+GTR+L8+Documentation+Board+%26+Assembly+Models.rar) | File [ClearFog GTR L8 Documentation Board & Assembly Models.rar](/wiki/download/attachments/287703150/ClearFog%20GTR%20L8%20Documentation%20Board%20%26%20Assembly%20Models.rar?api=v2) | Jan 18, 2022 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |

[Download All](/wiki/download/all_attachments?pageId=287703150)

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden