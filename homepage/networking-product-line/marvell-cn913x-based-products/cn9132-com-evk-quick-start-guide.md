# CN9132 COM EVK Quick Start Guide

![](<../../../.gitbook/assets/ClearFog CN sideways (small).png>)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Revision** | **Notes**       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 07 Dec 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.0          | Initial release |
| Table of Contents | <p>- <a href="cn9132-com-evk-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#introduction">Introduction</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#whats-in-the-box">What’s in the box?</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#recommended-cables">Recommended Cables</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#booting-from-an-spi-card">Booting from an SPI card</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#sfp-modules">SFP Modules</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#sim-card-slot">SIM Card Slot</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#documentation">Documentation</a><br>- <a href="cn9132-com-evk-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Introduction

The following quick start guide provides background information about the [CN9132 EVK](https://www.solid-run.com/embedded-networking/marvell-octeon-tx2-family/cex7-cn913x-com/#evaluation-board) product which use the CN9132 Computer on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Hardware Setup

#### Product Specifications

|                                  | CN9132 EVALUATION BOARD                                                                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I/Os                             | <p>3 x USB 3.0<br>3 x USB 2.0</p>                                                                                                                                                                                                                        |
| Networking                       | <p>1 x SFP+ 10GbE<br>1 x 5GbE RJ45 (with PoE PD)<br>1 x 5GbE RJ45 (with PoE PSE)<br>1 x 1GbE RJ45 MDI<br>ETH SW with 4x 1GbE RJ45 ports – Optional</p>                                                                                                   |
| Processor                        | Marvell OCTEON based CN9132 Quad core Arm Cortex A72 up to 2.2 GHz                                                                                                                                                                                       |
| Memory & Storage                 | <p>Dual Channel SO-DIMM DDR4; up to 32GB at 2400MT/s<br><br>(16GB for each channel)<br><br>MicroSD<br>8GB eMMC</p>                                                                                                                                       |
| Display                          | None                                                                                                                                                                                                                                                     |
| Misc.                            | <p>GPIO header<br>Indication LEDs<br>User Push Buttons</p>                                                                                                                                                                                               |
| Development and Debug interfaces | <p>MicroUSB<br>MicroUSB to STM32 for management</p>                                                                                                                                                                                                      |
| Power                            | <p>12V DC Jack<br>PoE PD</p>                                                                                                                                                                                                                             |
| Expansion card I/Os              | <p>2 x SATA (Gen 3.0)<br>Up to 3 x M.2 Key-M 2240/2280 PCIe x1 (Gen 3.0)<br>1 x M.2 Key-M 2240/2280 PCIe x2 (Gen 3.0)<br>1 x PCIe x4 (Gen 3.0) Add-in<br>2 x M.2 Key-E 2230/5760 for WiFi Modules<br>1 x mPCIe<br>1 x M.2 Key-B 3042/3052 for LTE/5G</p> |
| Temperature                      | Commercial: 0°C to 70°C                                                                                                                                                                                                                                  |
| Dimensions                       | PCBA: 172 x 214mm                                                                                                                                                                                                                                        |
| Enclosure                        | None                                                                                                                                                                                                                                                     |

{% hint style="info" %}
(\*) Configurable [SERDESs](cn9132-com-hardware-user-manual.md#serdes-muxing) based on Marvell CN913x processor specifications.
{% endhint %}


{% hint style="info" %}
Supported with CN9132 COM. For more detailed information about our CN9132 COM series please visit this user manual : [CN9132 COM Hardware User Manual](/homepage/networking-product-line/marvell-cn913x-based-products/cn9132-com-hardware-user-manual.md) .
{% endhint %}


## **Block Diagram**

The following figure describes the CN913x Block Diagram.

![](../../../.gitbook/assets/image-20220118-202201.png)

## Visual features overview

Please see below the features overview of the connector side of the CN9132 EVK.

![](<../../../.gitbook/assets/Evaluation Board CN9132 layout (Front).png>)

Print side connector overview of the CN9132 EVK.

![](<../../../.gitbook/assets/Evaluation Board CN9132 layout (Back).png>)

## What’s in the box?

* CN9132 EVK (ClearFog CX CN931x)
* 16GB Micro SD card (Optional)
* Heatsink
* Wall mount Power supply 12V@2.5A or 12V@5A (Optional)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* CN9132 EVK (ClearFog CX CN931x )
* DDR4 SO-DIMM Memory
* 12V Power adapter
* Micro USB to USB for console, the CN9132 EVK has an onboard FTDI chip.
* IP router or IP switch

{% hint style="info" %}
**Please Note** For Application using CN9132 COM express with multiple M.2 modules, SATAs and PCIe add-in card , a power supply 12V@5A is required.\
For Applications using CN9130 with few additional interfaces, a power supply of 12V@2.5A is sufficient.
{% endhint %}


## Recommended Cables

The following is a list of industry-standard cables, sorted by type, with the necessary compliance requirements that have been proven to work well with the CN913x product family.

These examples are the cables which SolidRun uses for testing, and should provide enough information to source products from your preferred cable vendor.

* Ethernet cable: Monoprice 24AWG Cat6A 500MHz STP
* USB Cable: SuperSpeed USB 3.0 Type A Male to Female Extension Cable in Black
* SFP connector: GigaLite GE-GB-P1RT-E SFP module with Monoprice 24AWG Cat6A 500MHz STP cable

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [CN913x COM Boot Select](/homepage/networking-product-line/marvell-cn913x-based-products/cn913x-other-articles/cn913x-com-boot-select.md) .

## Booting from an SPI card

The switches on the boot source selector must be set as follows:

|          |          |          |          |          |
| -------- | -------- | -------- | -------- | -------- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| OFF      | ON       | ON       | OFF      | ON       |

The following shows how to set the switches on the boot source selector:

![](../../../.gitbook/assets/image-20220112-142644.png)

Once you set the switches, you can apply the following for booting from an **SPI** card and loading the Ubuntu from an **SD** card.

{% hint style="warning" %}
**Please Note:** The **SPI** including U-Boot by default.
{% endhint %}


**1. Downloading the Ubuntu 20.04 image**

```
wget https://solid-run-images.sos-de-fra-1.exo.io/CN913x/cn9130-cex7_config_0_ubuntu-4cbe176.img.xz 
```

* For more Ubuntu releases, please visit [Ubuntu Releases for CN913x](https://images.solid-run.com/CN913x).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc cn9130-cex7_config_0_ubuntu-4cbe176.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync
```

* For more information, please visit [Flashing an SD Card](/homepage/other-articles/flashing-an-sd-card.md) .

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adapter to the DC jack, and then connect the adapter to mains supply.

**5. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](/homepage/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

In u-boot prompt, to continue booting from SD card, run the following:

```
setenv get_images "load mmc 1:1 $kernel_addr_r boot/Image; \
load mmc 1:1 $fdt_addr_r boot/cn9132-cex7.dtb; \
setenv root 'root=/dev/mmcblk1p1 rootwait rw'; setenv ramdisk_addr_r -"
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

**7. Final stages**

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

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](/homepage/networking-product-line/marvell-a38x-based-products/a388-other-articles/sfp-modules.md) .

## SIM Card Slot

It is possible to utilize a Cellular connection by inserting a SIM card into the SIM card slot. Please observe that a GSM Cellular modem needs to be installed utilizing the mini PCIe connection in order to exploit the cellular connection.

{% hint style="warning" %}
**Please Note** If you your ClearFog has dual SIM card slots, an additional cellular modem will need to be installed in the mini PCIe connection in order to utilize the 2nd SIM connection.
{% endhint %}


## Build from source

* CN913x Build - [CN913x Build - Script](/homepage/networking-product-line/marvell-cn913x-based-products/cn913x-software/cn913x-build.md)
* U-Boot, Atf and Mv-ddr-marvel Build - [CN913x u-boot, atf and mv-ddr-marvell - Self Build](/homepage/networking-product-line/marvell-cn913x-based-products/cn913x-other-articles/cn9132-com-on-honeycomb-lx2.md)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                               | File                                                                                                                           | Modified                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| <p>Labels<br><br>- No labels<br>- <a href="cn9132-com-evk-quick-start-guide.md#section-04eb52a3-ab64-4d15-95be-67478f7b6c7c">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493948/ClearFog+CX+CN9K+Schematics.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | PDF File [ClearFog CX CN9K Schematics.pdf](../../../wiki/download/attachments/197493948/ClearFog%20CX%20CN9K%20Schematics.pdf) | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="cn9132-com-evk-quick-start-guide.md#section-b5c15f65-a02f-476b-a279-5db4daabfa39">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493948/ClearFog+CN9-v1.2-Assy.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>      | ZIP Archive [ClearFog CN9-v1.2-Assy.zip](../../../wiki/download/attachments/197493948/ClearFog%20CN9-v1.2-Assy.zip)            | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="cn9132-com-evk-quick-start-guide.md#section-f36bd63f-4ee5-49ba-9f66-fd07f83d5cdb">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493948/ClearFog+CX+CN9K+3D.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>         | ZIP Archive [ClearFog CX CN9K 3D.zip](../../../wiki/download/attachments/197493948/ClearFog%20CX%20CN9K%203D.zip)              | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |

[Download All](../../../wiki/download/all_attachments)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
