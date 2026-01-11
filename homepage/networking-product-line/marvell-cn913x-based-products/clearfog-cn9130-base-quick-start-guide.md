# ClearFog CN9130 Base Quick Start Guide

![](./attachments/ClearFog%20CN%20sideways.png)

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 07 Dec 2021 |     | 1.0 | Initial release |
| 12 Nov 2024 | Yazan Shhady | 1.1 | Updated the block diagram to reflect the uSIM connection within the M.2 module. |
| 28 Nov 2024 | Yazan Shhady | 1.2 | Add Clearfog-Base CN9130 schematics rev 1.4 |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Introduction](#introduction)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product Specifications](#product-specifications)<br>- [Block Diagram](#block-diagram)<br>- [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Recommended Cables](#recommended-cables)<br>- [Boot Select](#boot-select)<br>- [Booting from an SPI card](#booting-from-an-spi-card)<br>- [Install to eMMC](#install-to-emmc)<br>- [SFP Modules](#sfp-modules)<br>- [SIM Card Slot](#sim-card-slot)<br>- [TLV EEPROM Support](#tlv-eeprom-support)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [ClearFog Base](https://www.solid-run.com/embedded-networking/marvell-octeon-tx2-family/clearfog-cn9130/#base) product which use the CN9130 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product Specifications

|     |     |
| --- | --- |
| **SOM CPU** | OCTEON CN9130 |
| **Processor** | 64-bit Cortex A72 |
| **Core Frequency** | up to 2.2GHz |
| **Memory & Storage** | 64bit DDR4 W/O ECC, Up to 8GB at 2400MT/s |
|     | M.2\*\* |
|     | MicroSD and 8GB eMMC (Optional)\*\*\* |
| **Connectivity** | 1 x mPCIE PCIe X1 Gen3.0 |
|     | 1 x USB 3.0 port |
|     | 2 x Port dedicated Ethernet |
|     | 1 x SFP+ 10GbE |
| **I/O & Misc.** | mikroBUS |
|     | Indication LEDs |
|     | User Push Buttons |
|     | PoE expansion header |
|     | RTC Battery |
|     | FTDI (Console Only) |
| **OS Support** | Linux, OpenWrt/LEDE, Yocto |
| **Power** | Wide range 9V-32V |
| **Dimensions** | 103mm x 75mm (PCBA) |
|     | 125mm x 80mm x 31mm (enclosed) |
| **Enclosure** | Optional Metal Enclosure |
|     | [Buy Now](https://shop.solid-run.com/?s=ClearFog+Base+CN9130&post_type=product) |

> [!NOTE]
> **Please Note :**
> (\*\*) M.2 includes USB 3.0, SATA, GNSS, 3G modules support (in carrier Base only)  
> (\*\*\*) Assembly option on the SOM

> [!INFO]
> Supported with CN9130 SOM. For more detailed information about our CN9130 SOM series please visit this user manual : [CN9130 SOM Hardware User Manual](../marvell-cn913x-based-products/cn9130-som-hardware-user-manual.md) .

<a id="block-diagram"></a>

## **Block Diagram**

The following figure describes the ClearFog Base Block Diagram.

![image-20241222-135621.png](./attachments/image-20241222-135621.png)

<a id="visual-features-overview"></a>

## Visual features overview

Please see below the features overview of the connector side of the ClearFog Base (CN9130 SoM assembled).

![](./attachments/image-20211207-173924.png)

Print side connector overview of the ClearFog Base.

![image-20241222-135815.png](./attachments/image-20241222-135815.png)

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up the board:

- Linux or Windows PC
- ClearFog Base with SOM
- 12V Power adapter (ClearFog Base has wide range input of 9V-32V, it is recommended to use 12V power adapter)
- Micro USB to USB for console, the ClearFog Base has an onboard FTDI chip.
- IP router or IP switch

<a id="recommended-cables"></a>

## Recommended Cables

The following is a list of industry-standard cables, sorted by type, with the necessary compliance requirements that have been proven to work well with the ClearFog product family (ClearFog Base / Pro).

These examples are the cables which SolidRun uses for testing, and should provide enough information to source products from your preferred cable vendor.

- Ethernet cable: Monoprice 24AWG Cat6A 500MHz STP
- USB Cable: SuperSpeed USB 3.0 Type A Male to Female Extension Cable in Black
- SFP connector: GigaLite GE-GB-P1RT-E SFP module with Monoprice 24AWG Cat6A 500MHz STP cable

<a id="boot-select"></a>

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [ClearFog CN9130 Boot Select](../marvell-cn913x-based-products/cn913x-other-articles/clearfog-cn9130-boot-select.md) .

<a id="booting-from-an-spi-card"></a>

## Booting from an SPI card

The switches on the boot source selector must be set as follows:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| ON  | X   | OFF | ON  | X   |

  
The following shows how to set the switches on the boot source selector:

![](./attachments/image-20211212-131232.png)

Once you set the switches, you can apply the following for booting from an **SPI** card and loading the Ubuntu from an **SD** card.

> [!WARNING]
> **Please Note:**
> The **SPI** including U-Boot by default.

**1\. Downloading the Ubuntu 20.04 image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/CN913x/cn913x_build/20240603-f591a0b/ubuntu-cn9130-cf-base-mmc:1:0.img.xz
```

- For more Ubuntu releases, please visit [Ubuntu Releases for CN913x](https://images.solid-run.com/CN913x).

**2\. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc ubuntu-cn9130-cf-base-mmc:1:0.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

- For more information, please visit [Flashing an SD Card](../../../homepage/other-articles/flashing-an-sd-card.md).

> [!NOTE]
> Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

**3\. SD card insertion**

Please Insert the SD card into your device.

**4\. Power connection**

Connect your power adapter to the DC jack, and then connect the adapter to mains supply.

**5\. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../../homepage/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

In u-boot prompt, to continue booting from SD card, run the following:

```
setenv get_images "load mmc 1:1 $kernel_addr_r boot/Image /
load mmc 1:1 $fdt_addr_r boot/cn9130-cf-base.dtb /
setenv root 'root=/dev/mmcblk1p1 rootwait rw' /
setenv ramdisk_addr_r -"
saveenv
boot
```

> [!WARNING]
> **Please Note:**
> Boot is made from SPI by default, so in order to continue booting from an SD card, the above commands should be run only once (in the fist boot).

Once you installed the necessary serial connection software and ran the above commands , you should be able to see the following:

![](./attachments/image-20211216-145327.png)

- In order to be able to log in , please insert “root” as a username and password as follows:

![](./attachments/image-20211216-145039.png)

**6\. Final stages**

The following stages need to be done in order to finalise the imaging:

1. Run `fdisk /dev/mmcblk1` if using SD, or run if using `fdisk /dev/mmcblk0` eMMC.
2. Recreate the first partition by deleting it and then creating a new partition that starts at block 131072 and extends to the end of the drive (or less depending on your needs).
3. Write the new partition, when prompt about ‘Do you want to remove the signature?’ then answer with yes.
4. Run `resize2fs /dev/mmcblk1p1` if using SD Card, or Run `resize2fs /dev/mmcblk0p1` if using eMMC.
5. In this stage the root partition should be big enough to start populating it; but first update the RTC clock.
6. Connect the RJ45 to your network with internet access (and DHCP server); and then run `dhclient` .
7. Update the RTC clock by running `ntpdate pool.ntp.org` and then `hwclock -w`.
8. Run `apt-update` and then populate the root filesystem as you wish.

Please see below an example of resizing the filesystem :

![](./attachments/image-20211216-153422.png)

<a id="install-to-emmc"></a>

## Install to eMMC

The switches on the boot source selector must be set as follows:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| OFF | X   | OFF | ON  | X   |

**1\. Downloading the Ubunto image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/CN913x/cn9130-cf-base_config_1_ubuntu-4cbe176.img.xz
```

**2\. Writing the image to eMMC**

```
xz -dc cn9130-cf-base_config_1_ubuntu-4cbe176.img.xz | dd of=/dev/mmcblk0 bs=4k conv=sync
```

**3\. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to the main supply.

**4\. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../../homepage/other-articles/serial-connection.md) for installing the necessary serial connection software in Linux/Windows.

**5\. Set the boot command to load the image from the eMMC device:**

In U-boot prompt, run the following commands only in the first boot:

```
setenv get_images "load mmc 0:1 $kernel_addr_r boot/Image /
load mmc 0:1 $fdt_addr_r boot/cn9130-cf-pro.dtb /
setenv root 'root=/dev/mmcblk0p1 rootwait rw' /
setenv ramdisk_addr_r -"; saveenv; boot
```

- Use ‘root’ as a username and password to be able to log in.

**6\. Final stages**

The following stages need to be done in order to finalize the imaging:

1. Run `fdisk /dev/mmcblk1` if using SD, or run if using `fdisk /dev/mmcblk0` eMMC.
2. Recreate the first partition by deleting it and then creating a new partition that starts at block 131072 and extends to the end of the drive (or less depending on your needs).
3. Write the new partition, when prompt about ‘Do you want to remove the signature?’ then answer with yes.
4. Run `resize2fs /dev/mmcblk1p1` if using SD Card, or Run `resize2fs /dev/mmcblk0p1` if using eMMC.
5. In this stage the root partition should be big enough to start populating it; but first update the RTC clock.
6. Connect the RJ45 to your network with internet access (and DHCP server); and then run `dhclient` .
7. Update the RTC clock by running `ntpdate pool.ntp.org` and then `hwclock -w`.
8. Run `apt-update` and then populate the root filesystem as you wish.

Please see below an example of resizing the filesystem :

![](./attachments/image-20211216-153422.png)

<a id="sfp-modules"></a>

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](../../networking-product-line/marvell-a38x-based-products/a388-other-articles/sfp-modules.md).

<a id="sim-card-slot"></a>

## SIM Card Slot

It is possible to utilize a Cellular connection by inserting a SIM card into the SIM card slot. Please observe that a GSM Cellular modem needs to be installed utilizing the mini PCIe connection in order to exploit the cellular connection.

> [!WARNING]
> **Please Note**
> If you your ClearFog has dual SIM card slots, an additional cellular modem will need to be installed in the mini PCIe connection in order to utilize the 2nd SIM connection.

<a id="tlv-eeprom-support"></a>

## TLV EEPROM Support

Starting from April 01. 2022, the EEPROMs on Carriers, SoMs and COM-Express Modules are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. Check our [CN913x EEPROM documentation](../marvell-cn913x-based-products/cn913x-other-articles/cn913x-eeprom-programming-tlv.md) for additional information.

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211024-150854.png) | [https://github.com/SolidRun/Documentation/tree/bsp/cn913x](https://github.com/SolidRun/Documentation/tree/bsp/cn913x) |
| Debian Image  <br>Builder | [https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79](https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79) |
| ![](./attachments/image-20220403-092027.png) | [https://github.com/SolidRun/cn913x\_build](https://github.com/SolidRun/cn913x_build) |

<a id="build-from-source"></a>

## Build from source

- CN913x Build - [CN913x Build - Script](https://developer.resources.solid-run.com/wiki/spaces/developer/pages/201097229/CN913x+Build+-+Script)
- U-Boot, Atf and Mv-ddr-marvel Build - [CN913x u-boot, atf and mv-ddr-marvell - Self Build](https://developer.resources.solid-run.com/wiki/spaces/developer/pages/200769556/CN913x+u-boot+atf+and+mv-ddr-marvell+-+Self+Build)
- Debian Image Builder - [GitHub - SolidRun/debian-builder](https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79)

<a id="documentation"></a>

## Documentation

      

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-afe6a6fd-f129-47a5-ba22-024add874c97)<br><br>[Preview] [View](/wiki/download/attachments/197493959/clearfog_base-cn9130-rev1.1-mtbf.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=clearfog_base-cn9130-rev1.1-mtbf.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=clearfog_base-cn9130-rev1.1-mtbf.pdf) | PDF File [clearfog\_base-cn9130-rev1.1-mtbf.pdf](/wiki/download/attachments/197493959/clearfog_base-cn9130-rev1.1-mtbf.pdf?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-e11ccea3-d44c-49b3-ba5c-d4f9a5ed1639)<br><br>[Preview] [View](/wiki/download/attachments/197493959/clearfog_base-cn9130-rev1.2-pcb-layout.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=clearfog_base-cn9130-rev1.2-pcb-layout.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=clearfog_base-cn9130-rev1.2-pcb-layout.zip) | ZIP Archive [clearfog\_base-cn9130-rev1.2-pcb-layout.zip](/wiki/download/attachments/197493959/clearfog_base-cn9130-rev1.2-pcb-layout.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-19d09fb4-c23c-4ae0-9f60-38f12b08075b)<br><br>[Preview] [View](/wiki/download/attachments/197493959/mikrobus_specification-rev2.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=mikrobus_specification-rev2.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=mikrobus_specification-rev2.pdf) | PDF File [mikrobus\_specification-rev2.pdf](/wiki/download/attachments/197493959/mikrobus_specification-rev2.pdf?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-0de49c8e-fdf4-418b-bee0-a2c1bba3637f)<br><br>[Preview] [View](/wiki/download/attachments/197493959/clearfog_base-cn9130-enclosure-rev2.5.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=clearfog_base-cn9130-enclosure-rev2.5.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=clearfog_base-cn9130-enclosure-rev2.5.zip) | ZIP Archive [clearfog\_base-cn9130-enclosure-rev2.5.zip](/wiki/download/attachments/197493959/clearfog_base-cn9130-enclosure-rev2.5.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-faf73301-83df-4e4a-9dc7-440cd5a044b6)<br><br>[Preview] [View](/wiki/download/attachments/197493959/ClearFog+Base+CN9130+BOM+rev+1.2.4.xlsx?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=ClearFog+Base+CN9130+BOM+rev+1.2.4.xlsx&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=ClearFog+Base+CN9130+BOM+rev+1.2.4.xlsx) | Microsoft Excel Spreadsheet [ClearFog Base CN9130 BOM rev 1.2.4.xlsx](/wiki/download/attachments/197493959/ClearFog%20Base%20CN9130%20BOM%20rev%201.2.4.xlsx?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-47095d54-c5d5-480d-90d4-7a7a2a3991ce)<br><br>[Preview] [View](/wiki/download/attachments/197493959/ClearFog-Base-CN9130-Assy-Files.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=ClearFog-Base-CN9130-Assy-Files.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=ClearFog-Base-CN9130-Assy-Files.zip) | ZIP Archive [ClearFog-Base-CN9130-Assy-Files.zip](/wiki/download/attachments/197493959/ClearFog-Base-CN9130-Assy-Files.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-88e8746e-bf20-4b8d-b7fe-159abe30d0bc)<br><br>[Preview] [View](/wiki/download/attachments/197493959/ClearFog-Base-CN9130-Schematics.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=ClearFog-Base-CN9130-Schematics.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=ClearFog-Base-CN9130-Schematics.zip) | ZIP Archive [ClearFog-Base-CN9130-Schematics.zip](/wiki/download/attachments/197493959/ClearFog-Base-CN9130-Schematics.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-d8e512c7-407a-48cf-a305-c39135a37d03)<br><br>[Preview] [View](/wiki/download/attachments/197493959/clearfog_base-cn9130-rev.1.2-gerber.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=clearfog_base-cn9130-rev.1.2-gerber.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=clearfog_base-cn9130-rev.1.2-gerber.zip) | ZIP Archive [clearfog\_base-cn9130-rev.1.2-gerber.zip](/wiki/download/attachments/197493959/clearfog_base-cn9130-rev.1.2-gerber.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-8aacaa63-33c8-4745-af22-62ac9c0e3bde)<br><br>[Preview] [View](/wiki/download/attachments/197493959/clearfog-base-cn9130-schematics-rev1.4.pdf?version=3) [Properties](/wiki/pages/editattachment.action?pageId=197493959&fileName=clearfog-base-cn9130-schematics-rev1.4.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493959&fileName=clearfog-base-cn9130-schematics-rev1.4.pdf) | PDF File [clearfog-base-cn9130-schematics-rev1.4.pdf](/wiki/download/attachments/197493959/clearfog-base-cn9130-schematics-rev1.4.pdf?api=v2) | Nov 28, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |

[Download All](/wiki/download/all_attachments?pageId=197493959)

[ Buy a Sample Now](https://shop.solid-run.com/?s=ClearFog+Base+CN9130&post_type=product)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden