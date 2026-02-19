# ClearFog CN9130 Base Quick Start Guide

![](<../../../.gitbook/assets/ClearFog CN sideways.png>)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Revision** | **Notes**                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------- |
| 07 Dec 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 1.0          | Initial release                                                                 |
| 12 Nov 2024       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1.1          | Updated the block diagram to reflect the uSIM connection within the M.2 module. |
| 28 Nov 2024       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1.2          | Add Clearfog-Base CN9130 schematics rev 1.4                                     |
| Table of Contents | <p>- <a href="clearfog-cn9130-base-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#introduction">Introduction</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#recommended-cables">Recommended Cables</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#booting-from-an-spi-card">Booting from an SPI card</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#install-to-emmc">Install to eMMC</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#sfp-modules">SFP Modules</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#sim-card-slot">SIM Card Slot</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#tlv-eeprom-support">TLV EEPROM Support</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#documentation">Documentation</a><br>- <a href="clearfog-cn9130-base-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                                                                                 |

## Introduction

The following quick start guide provides background information about the [ClearFog Base](https://www.solid-run.com/embedded-networking/marvell-octeon-tx2-family/clearfog-cn9130/#base) product which use the CN9130 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Hardware Setup

#### Product Specifications

|                      |                                                                                  |
| -------------------- | -------------------------------------------------------------------------------- |
| **SOM CPU**          | OCTEON CN9130                                                                    |
| **Processor**        | 64-bit Cortex A72                                                                |
| **Core Frequency**   | up to 2.2GHz                                                                     |
| **Memory & Storage** | 64bit DDR4 W/O ECC, Up to 8GB at 2400MT/s                                        |
|                      | M.2\*\*                                                                          |
|                      | MicroSD and 8GB eMMC (Optional)\*\*\*                                            |
| **Connectivity**     | 1 x mPCIE PCIe X1 Gen3.0                                                         |
|                      | 1 x USB 3.0 port                                                                 |
|                      | 2 x Port dedicated Ethernet                                                      |
|                      | 1 x SFP+ 10GbE                                                                   |
| **I/O & Misc.**      | mikroBUS                                                                         |
|                      | Indication LEDs                                                                  |
|                      | User Push Buttons                                                                |
|                      | PoE expansion header                                                             |
|                      | RTC Battery                                                                      |
|                      | FTDI (Console Only)                                                              |
| **OS Support**       | Linux, OpenWrt/LEDE, Yocto                                                       |
| **Power**            | Wide range 9V-32V                                                                |
| **Dimensions**       | 103mm x 75mm (PCBA)                                                              |
|                      | 125mm x 80mm x 31mm (enclosed)                                                   |
| **Enclosure**        | Optional Metal Enclosure                                                         |
|                      | [Buy Now](https://shop.solid-run.com/?s=ClearFog+Base+CN9130\&post_type=product) |

{% hint style="info" %}
**Please Note :** (\*\*) M.2 includes USB 3.0, SATA, GNSS, 3G modules support (in carrier Base only)\
(\*\*\*) Assembly option on the SOM
{% endhint %}


{% hint style="info" %}
Supported with CN9130 SOM. For more detailed information about our CN9130 SOM series please visit this user manual : [CN9130 SOM Hardware User Manual](cn9130-som-hardware-user-manual.md) .
{% endhint %}


## **Block Diagram**

The following figure describes the ClearFog Base Block Diagram.

![image-20241222-135621.png](../../../.gitbook/assets/image-20241222-135621.png)

## Visual features overview

Please see below the features overview of the connector side of the ClearFog Base (CN9130 SoM assembled).

![](../../../.gitbook/assets/image-20211207-173924.png)

Print side connector overview of the ClearFog Base.

![image-20241222-135815.png](../../../.gitbook/assets/image-20241222-135815.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* ClearFog Base with SOM
* 12V Power adapter (ClearFog Base has wide range input of 9V-32V, it is recommended to use 12V power adapter)
* Micro USB to USB for console, the ClearFog Base has an onboard FTDI chip.
* IP router or IP switch

## Recommended Cables

The following is a list of industry-standard cables, sorted by type, with the necessary compliance requirements that have been proven to work well with the ClearFog product family (ClearFog Base / Pro).

These examples are the cables which SolidRun uses for testing, and should provide enough information to source products from your preferred cable vendor.

* Ethernet cable: Monoprice 24AWG Cat6A 500MHz STP
* USB Cable: SuperSpeed USB 3.0 Type A Male to Female Extension Cable in Black
* SFP connector: GigaLite GE-GB-P1RT-E SFP module with Monoprice 24AWG Cat6A 500MHz STP cable

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [ClearFog CN9130 Boot Select](cn913x-other-articles/clearfog-cn9130-boot-select.md) .

## Booting from an SPI card

The switches on the boot source selector must be set as follows:

|          |          |          |          |          |
| -------- | -------- | -------- | -------- | -------- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| ON       | X        | OFF      | ON       | X        |

The following shows how to set the switches on the boot source selector:

![](<../../../.gitbook/assets/image-20211212-131232 (1).png>)

Once you set the switches, you can apply the following for booting from an **SPI** card and loading the Ubuntu from an **SD** card.

{% hint style="warning" %}
**Please Note:** The **SPI** including U-Boot by default.
{% endhint %}


**1. Downloading the Ubuntu 20.04 image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/CN913x/cn913x_build/20240603-f591a0b/ubuntu-cn9130-cf-base-mmc:1:0.img.xz
```

* For more Ubuntu releases, please visit [Ubuntu Releases for CN913x](https://images.solid-run.com/CN913x).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc ubuntu-cn9130-cf-base-mmc:1:0.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

* For more information, please visit [Flashing an SD Card](../../other-articles/flashing-an-sd-card.md).

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adapter to the DC jack, and then connect the adapter to mains supply.

**5. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

In u-boot prompt, to continue booting from SD card, run the following:

```
setenv get_images "load mmc 1:1 $kernel_addr_r boot/Image /
load mmc 1:1 $fdt_addr_r boot/cn9130-cf-base.dtb /
setenv root 'root=/dev/mmcblk1p1 rootwait rw' /
setenv ramdisk_addr_r -"
saveenv
boot
```

{% hint style="warning" %}
**Please Note:** Boot is made from SPI by default, so in order to continue booting from an SD card, the above commands should be run only once (in the fist boot).
{% endhint %}


Once you installed the necessary serial connection software and ran the above commands , you should be able to see the following:

![](<../../../.gitbook/assets/image-20211216-145327 (1).png>)

* In order to be able to log in , please insert “root” as a username and password as follows:

![](<../../../.gitbook/assets/image-20211216-145039 (1).png>)

**6. Final stages**

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

![](<../../../.gitbook/assets/image-20211216-153422 (1).png>)

## Install to eMMC

The switches on the boot source selector must be set as follows:

|          |          |          |          |          |
| -------- | -------- | -------- | -------- | -------- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| OFF      | X        | OFF      | ON       | X        |

**1. Downloading the Ubunto image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/CN913x/cn9130-cf-base_config_1_ubuntu-4cbe176.img.xz
```

**2. Writing the image to eMMC**

```
xz -dc cn9130-cf-base_config_1_ubuntu-4cbe176.img.xz | dd of=/dev/mmcblk0 bs=4k conv=sync
```

**3. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to the main supply.

**4. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing the necessary serial connection software in Linux/Windows.

**5. Set the boot command to load the image from the eMMC device:**

In U-boot prompt, run the following commands only in the first boot:

```
setenv get_images "load mmc 0:1 $kernel_addr_r boot/Image /
load mmc 0:1 $fdt_addr_r boot/cn9130-cf-pro.dtb /
setenv root 'root=/dev/mmcblk0p1 rootwait rw' /
setenv ramdisk_addr_r -"; saveenv; boot
```

* Use ‘root’ as a username and password to be able to log in.

**6. Final stages**

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

![](<../../../.gitbook/assets/image-20211216-153422 (1).png>)

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](../marvell-a38x-based-products/a388-other-articles/sfp-modules.md).

## SIM Card Slot

{% file src="../../../.gitbook/assets/clearfog-base-schematics-rev1.4.pdf" %}

[clearfog-base-schematics-rev1.4.pdf](../../../.gitbook/assets/clearfog-base-schematics-rev1.4.pdf)

\[ClearFogCX CN9K Schematics.pdf]\(attachments/ClearFog CX CN9K Schematics.pdf)

It is possible to utilize a Cellular connection by inserting a SIM card into the SIM card slot. Please observe that a GSM Cellular modem needs to be installed utilizing the mini PCIe connection in order to exploit the cellular connection.

{% hint style="warning" %}
**Please Note** If you your ClearFog has dual SIM card slots, an additional cellular modem will need to be installed in the mini PCIe connection in order to utilize the 2nd SIM connection.
{% endhint %}


## TLV EEPROM Support

Starting from April 01. 2022, the EEPROMs on Carriers, SoMs and COM-Express Modules are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. Check our [CN913x EEPROM documentation](cn913x-other-articles/cn913x-eeprom-programming-tlv.md) for additional information.

## List Of Supported OS

| **OS**                                                        |                                                                                                                                                                                      |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](<../../../.gitbook/assets/image-20211024-150854 (3).png>) | [https://github.com/SolidRun/Documentation/tree/bsp/cn913x](https://github.com/SolidRun/Documentation/tree/bsp/cn913x)                                                               |
| <p>Debian Image<br>Builder</p>                                | [https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79](https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79) |
| ![](../../../.gitbook/assets/image-20220403-092027.png)       | [https://github.com/SolidRun/cn913x\_build](https://github.com/SolidRun/cn913x_build)                                                                                                |

## Build from source

* CN913x Build - [CN913x Build - Script](cn913x-software/cn913x-build.md)
* U-Boot, Atf and Mv-ddr-marvel Build - [CN913x u-boot, atf and mv-ddr-marvell - Self Build](https://developer.resources.solid-run.com/wiki/spaces/developer/pages/200769556/CN913x+u-boot+atf+and+mv-ddr-marvell+-+Self+Build)
* Debian Image Builder - [GitHub - SolidRun/debian-builder](https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79)

## Documentation

{% file src="attachments/clearfog_base-cn9130-rev1.1-mtbf.pdf" %}
{% file src="attachments/clearfog_base-cn9130-rev1.2-pcb-layout.zip" %}
{% file src="attachments/mikrobus_specification-rev2.pdf" %}
{% file src="attachments/clearfog_base-cn9130-enclosure-rev2.5.zip" %}
{% file src="attachments/ClearFog%20Base%20CN9130%20BOM%20rev%201.2.4.xlsx" %}
{% file src="attachments/ClearFog-Base-CN9130-Assy-Files.zip" %}
{% file src="attachments/ClearFog-Base-CN9130-Schematics.zip" %}
{% file src="attachments/clearfog_base-cn9130-rev.1.2-gerber.zip" %}
{% file src="attachments/clearfog-base-cn9130-schematics-rev1.4.pdf" %}



[Buy a Sample Now](https://shop.solid-run.com/?s=ClearFog+Base+CN9130\&post_type=product)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
