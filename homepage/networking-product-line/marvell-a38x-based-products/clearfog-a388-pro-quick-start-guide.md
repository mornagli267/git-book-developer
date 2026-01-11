# ClearFog A388 Pro Quick Start Guide

![](<../../../.gitbook/assets/ClearFog Pro sideways (large).png>)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Revision** | **Notes**       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | --------------- |
| 07 Dec 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1.0          | Initial release |
| Table of Contents | <p>- <a href="clearfog-a388-pro-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#introduction">Introduction</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#specifications">Specifications</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#recommended-cables">Recommended Cables</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#booting-from-an-sd-card">Booting from an SD card</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#gpio-pins-control">GPIO pins Control</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#sfp-modules">SFP Modules</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#sim-card-slot">SIM Card Slot</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#build-u-boot-kernel-from-sources">Build U-Boot &#x26; kernel from sources</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#documentation">Documentation</a><br>- <a href="clearfog-a388-pro-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Introduction

The following quick start guide provides background information about the [ClearFog Pro](https://www.solid-run.com/embedded-networking/marvell-armada-family/clearfog/#pro) product which use the A388 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

For CN9130 SOM Software, please refrer to the following link:[CN913x Build](../marvell-cn913x-based-products/cn913x-software/cn913x-build.md)

## Specifications

|                      |                                                                                                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SOM Model**        | ARMADA based A388                                                                                                                                                       |
| **Processor**        | 32-bit Cortex A9                                                                                                                                                        |
| **Core Frequency**   | up to 1.6GHz                                                                                                                                                            |
| **Memory & Storage** | 32bit DDR3 W/ ECC, Up to 2GB at 1600MT/s                                                                                                                                |
|                      | M.2                                                                                                                                                                     |
|                      | uSD or 8GB eMMC (Optional)                                                                                                                                              |
| **Connectivity**     | 2 x mSATA/mPCIE                                                                                                                                                         |
|                      | 1 x USB 3.0 port                                                                                                                                                        |
|                      | 1 x Port dedicated Ethernet                                                                                                                                             |
|                      | 5 x Port switched Ethernet                                                                                                                                              |
|                      | 1 x SFP 2.5GbE                                                                                                                                                          |
| **I/O & Misc.**      | Analog Audio/TDM module support                                                                                                                                         |
|                      | GPIO Header (mikroBUS)                                                                                                                                                  |
|                      | Indication LEDs                                                                                                                                                         |
|                      | User Push Buttons                                                                                                                                                       |
|                      | PoE expansion header                                                                                                                                                    |
|                      | RTC Battery                                                                                                                                                             |
|                      | FTDI (Console Only)/Debug Header                                                                                                                                        |
|                      | JTAG Header                                                                                                                                                             |
| **OS Support**       | Linux Kernel 4.x, OpenWRT/LEDE, Yocto                                                                                                                                   |
| **Power**            | Wide range 9V- 32V                                                                                                                                                      |
|                      | Advanced Power Control                                                                                                                                                  |
|                      | Fan Control                                                                                                                                                             |
| **Dimensions**       | 225mm x 100mm (PCBA)                                                                                                                                                    |
|                      | 226mm x 104mm x 33mm (Enclosed)                                                                                                                                         |
| **Enclosure**        | Optional metal enclosure                                                                                                                                                |
|                      | [Buy Now](https://shop.solid-run.com/product-category/embedded-computers/marvell-family/clearfog-base-pro/?_ga=2.126128654.2016484779.1641802897-2012112798.1622706355) |

> \[!INFO] Supported with A388 SOM. For more detailed information about our A388 SOM series please visit this user manual : [A388 SOM Hardware User Manual](a388-som-hardware-user-manual.md) .

## **Block Diagram**

The following figure describes the ClearFog Pro Block Diagram.

![](<../../../.gitbook/assets/ClearFog A388 Pro block diagram-20211207-164435.png>)

## Visual features overview

Please see below the features overview of the connector side of the ClearFog Pro (A388 SOM assembled).

![](../../../.gitbook/assets/image-20211207-164524.png)

Print side connector overview of the ClearFog Pro.

![](../../../.gitbook/assets/image-20211207-164539.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* ClearFog Pro with SOM
* 12V Power adapter (ClearFog Pro has wide range input of 9V-32V, it is recommended to use 12V power adapter)
* Micro USB to USB for console, the ClearFog Pro has an onboard FTDI chip.
* IP router or IP switch

## Recommended Cables

The following is a list of industry-standard cables, sorted by type, with the necessary compliance requirements that have been proven to work well with the ClearFog product family (ClearFog Base / Pro).

These examples are the cables which SolidRun uses for testing, and should provide enough information to source products from your preferred cable vendor.

* Ethernet cable: Monoprice 24AWG Cat6A 500MHz STP
* USB Cable: SuperSpeed USB 3.0 Type A Male to Female Extension Cable in Black
* SFP connector: GigaLite GE-GB-P1RT-E SFP module with Monoprice 24AWG Cat6A 500MHz STP cable

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [ClearFog A388 Boot Select](a388-other-articles/clearfog-a388-boot-select.md) .

## Booting from an SD card

The switches on the boot source selector must be set as follows:

|          |          |          |          |          |
| -------- | -------- | -------- | -------- | -------- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| OFF      | OFF      | ON       | ON       | ON       |

The following shows how to set the switches on the boot source selector:

![](../../../.gitbook/assets/image-20211212-131839.png)

Once you set the switches, you can apply the following for booting from an SD card.

**1. Downloading the Debian image**

```
wget https://images.solid-run.com/A38X/Debian/sr-a38x-debian-bullseye-20220427.img.xz
```

* For more Debian releases, please visit [Debian Releases for Armada 38X](https://images.solid-run.com/A38X/Debian).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc sr-a38x-debian-bullseye-20220427.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

* For more information, please visit [Flashing an SD Card](../../other-articles/flashing-an-sd-card.md) .

> \[!NOTE] Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

**3. U-Boot installation**

```
wget https://images.solid-run.com/A38X/U-Boot/u-boot-clearfog-pro-sdhc.kwb
```

**4. Writing U-Boot to the SD card**

```
dd if=u-boot-clearfog-pro-sdhc.kwb of=/dev/sdX bs=512 seek=1 conv=sync status=progress
```

* For more information, you can refer to [A38x U-Boot](a388-software/a38x-u-boot.md) .

**5. SD card insertion**

Please Insert the SD card into your device.

**6. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**7. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](../../../.gitbook/assets/image-20211212-115306.png)

* In order to be able to log in , please insert “debian” as a username and password as follows:

![](../../../.gitbook/assets/image-20211212-115539.png)

## GPIO pins Control

To control on the GPIO pins, please follow this page [ClearFog Base/Pro GPIO Pins Control](a388-other-articles/clearfog-base-pro-gpio-pins-control.md) .

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](a388-other-articles/sfp-modules.md) .

## SIM Card Slot

It is possible to utilize a Cellular connection by inserting a SIM card into the SIM card slot. Please observe that a GSM Cellular modem needs to be installed utilizing the mini PCIe connection in order to exploit the cellular connection.

> \[!WARNING] **Please Note** If you your ClearFog has dual SIM card slots, an additional cellular modem will need to be installed in the mini PCIe connection in order to utilize the 2nd SIM connection.

## List Of Supported OS

| **OS**                                                  |                                                                               |
| ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![](../../../.gitbook/assets/image-20211223-141905.png) | [A388 Buildroot](a388-software/a388-buildroot.md)                             |
| ![](../../../.gitbook/assets/image-20211223-141939.png) | [Yocto for Clearfog Platforms](a388-software/yocto-for-clearfog-platforms.md) |
| ![](../../../.gitbook/assets/image-20220119-065742.png) | [OpenWrt](a388-software/a388-openwrt.md)                                      |
| ![](../../../.gitbook/assets/image-20220118-112849.png) | [SolidRun Images](https://images.solid-run.com/A38X/Debian)                   |

## Build U-Boot & kernel from sources

* U-Boot Build - [A38X U-Boot](a388-software/a38x-u-boot.md)
* Kernel Build - [A388 Kernel](a388-software/a388-kernel.md)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                                                         | File                                                                                                                                                                        | Modified                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-9c59edfb-e9bf-4c67-b128-e7b7b005b83e">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/rtc-datasheet-onboard.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                              | PDF File [rtc-datasheet-onboard.pdf](../../../wiki/download/attachments/197493369/rtc-datasheet-onboard.pdf)                                                                | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-a2bbc78a-ea78-488d-aabb-04968c316079">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/ClearFog+Pro+BOM+rev+2.1.4.xlsx">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                        | Microsoft Excel Spreadsheet [ClearFog Pro BOM rev 2.1.4.xlsx](../../../wiki/download/attachments/197493369/ClearFog%20Pro%20BOM%20rev%202.1.4.xlsx)                         | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-514ab311-0bb2-4c6c-8903-ab5fa62eaba7">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/clearfog_pro-rev.2.1-gerber.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                        | ZIP Archive [clearfog\_pro-rev.2.1-gerber.zip](../../../wiki/download/attachments/197493369/clearfog_pro-rev.2.1-gerber.zip)                                                | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-2a76360a-2c6e-49b5-8996-72df449bceaf">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/clearfog_pro-rev2.1-pcb-layout.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                     | ZIP Archive [clearfog\_pro-rev2.1-pcb-layout.zip](../../../wiki/download/attachments/197493369/clearfog_pro-rev2.1-pcb-layout.zip)                                          | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-1c67a91c-097a-461b-9298-b2a65dc21f95">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/clearfog-schematics-2.1.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                            | PDF File [clearfog-schematics-2.1.pdf](../../../wiki/download/attachments/197493369/clearfog-schematics-2.1.pdf)                                                            | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-ba97ae5f-b2fa-4737-bf99-50a9b548df9c">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/ClearFog-Pro-Enclosure-Files.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                       | ZIP Archive [ClearFog-Pro-Enclosure-Files.zip](../../../wiki/download/attachments/197493369/ClearFog-Pro-Enclosure-Files.zip)                                               | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-6d3cc898-1c92-4c9c-b34f-1f6bd3cd4ff1">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/ARMADA-A388-SOM-Heatsink.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                           | ZIP Archive [ARMADA-A388-SOM-Heatsink.zip](../../../wiki/download/attachments/197493369/ARMADA-A388-SOM-Heatsink.zip)                                                       | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-5e42820d-279b-42ae-a36c-04b2fd6078fe">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/clearfog_pro-rev.2.1-mechanical_assembly-3dpdf-pdf.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | ZIP Archive [clearfog\_pro-rev.2.1-mechanical\_assembly-3dpdf-pdf.zip](../../../wiki/download/attachments/197493369/clearfog_pro-rev.2.1-mechanical_assembly-3dpdf-pdf.zip) | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="clearfog-a388-pro-quick-start-guide.md#section-54f8e6de-b006-400f-a4ba-5ac7221b6626">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493369/clearfo-pro-schematics-rev2.2.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                      | PDF File [clearfo-pro-schematics-rev2.2.pdf](../../../wiki/download/attachments/197493369/clearfo-pro-schematics-rev2.2.pdf)                                                | Jan 30, 2025 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/)                |

[Download All](../../../wiki/download/all_attachments)

[Buy a Sample Now](https://shop.solid-run.com/product-category/embedded-computers/marvell-family/clearfog-base-pro/?_ga=2.126128654.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
