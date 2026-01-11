# HoneyComb AMD V3000 mini ITX Quick Start Guide

***

![image-20240714-103926.png](../../../.gitbook/assets/image-20240714-103926.png)

## Introduction

The following quick start guide provides background information about the [Honeycomb Ryzen V3000](https://www.solid-run.com/embedded-networking/ryzen-v3000-cx7-com/) products which use the Ryzen V3000 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Revision** | **Notes** |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- |
| 16 Jun 2024       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1.0          |           |
| Table of Contents | <p>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#introduction">Introduction</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#recommended-cables">Recommended Cables</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#booting-the-machine">Booting the machine</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#booting-to-os">Booting to OS</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#sfp-modules">SFP Modules</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#so-dimm-modules">SO-DIMM Modules</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#os-list">OS list</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#documentation">Documentation</a><br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#related-articles">Related Articles</a></p> |              |           |

## Hardware Setup

#### Product Specifications

|                                  | **Honeycomb Ryzen V3000**                                                     |
| -------------------------------- | ----------------------------------------------------------------------------- |
| I/Os                             | <p>3 x USB 2.0<br><br>3 x USB 3.0</p>                                         |
| Networking                       | <p>2 x SFP+ ports (10GbE each)<br>1 x 1GbE copper (RJ45)</p>                  |
| Processor                        | <p>AMD Ryzen Embedded V3C18I<br>8c/16t up to 3.8 GHz</p>                      |
| Memory & Storage                 | <p>Up to 64GB DDR5 4800 MTPs<br>2x SATA interfaces<br>M.2 NVME GEN 4.0 x4</p> |
| Misc.                            | <p>BMC functionality<br>PWM Fan header</p>                                    |
| Development and Debug interfaces | mini USB                                                                      |
| Power                            | ATX standard                                                                  |
| Expansion card I/Os              | PCIe x4 Gen 4.0                                                               |
| Temperature                      | Industrial: -45°C to 85°C                                                     |
| Dimensions                       | PCBA: 170 x 170mm                                                             |

## **Block Diagram**

Coming soon…

## Visual features overview

Please see below the features overview of the HoneyComb AMD V3000 mini ITX

![image-20240714-111209.png](../../../.gitbook/assets/image-20240714-111209.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* HoneyComb AMD V3000 mini ITX
* ATX 60W+
* Mini-USB to USB for console, the HoneyComb Ryzen V3000 has an onboard FTDI chip.
* IP router or IP switch

#### Recommended Cables

Please refer to the [tested SFP modules](../../bedrock-pc/bedrock-v3000-technical-documentation/hardware-bedrock-v3000/sfp-modules-tested-with-bedrock-v3000.md) page

## Booting the machine

Download & install images:

You can use the [Ubuntu server installation instructions](../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/linux-bedrock-v3000/installing-ubuntu-server-using-console.md) page or download [Pre-installed images](../../other-articles/snippets/bedrock-images-info.md).

If using the Pre-installed image, flash it to a USB stick using the following commands:

```
gunzip <image_name.img.gz>
dd if=<image_name.img> of=/dev/sdx bs=1M status=progress; sync
```

> \[!NOTE] NOTE: check the /dev/sdx device you need using the `lsblk` command

## Booting to OS

Insert the USB stick to the device and power it on.

Wait for the device to boot.

> \[!INFO] Very first boot might take a while due to DDR training

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](../../bedrock-pc/bedrock-v3000-technical-documentation/hardware-bedrock-v3000/sfp-modules-tested-with-bedrock-v3000.md) .

## SO-DIMM Modules

For some SO-DIMM modules that work on SolidRun hardware platforms, please refer to [List of tested SO-DIMMs](../../other-articles/snippets/list-of-so-dimm-ram-modules-tested-with-ryzen-v3000-com7.md) .

## OS list

| **OS**                                                                                 |                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-20240429-104614.png](<../../../.gitbook/assets/image-20240429-104614 (1).png>) | <p><a href="https://ubuntu.com/download">Ubuntu</a><br><br><a href="../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/linux-bedrock-v3000/installing-ubuntu-server-using-console.md">Console installation instructions</a></p>       |
| ![image-20240429-100250.png](<../../../.gitbook/assets/image-20240429-100250 (1).png>) | [Fedora](https://fedoraproject.org/)                                                                                                                                                                                                                             |
| ![image-20240429-100554.png](<../../../.gitbook/assets/image-20240429-100554 (1).png>) | [Windows](https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d) (1)                                                                                                                            |
| ![image-20240429-100517.png](<../../../.gitbook/assets/image-20240429-100517 (1).png>) | <p><a href="https://github.com/buildroot/buildroot">Buildroot</a><br><br>A BuildRoot image can be build for x86 platform (ttyS4) should be enabled</p>                                                                                                           |
| ![image-20240429-100852.png](<../../../.gitbook/assets/image-20240429-100852 (1).png>) | <p><a href="https://www.freebsd.org/where/">FreeBSD</a> (2)<br><br><a href="../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/other-operating-systems-bedrock-v3000/installing-freebsd.md">Console installation instructions</a></p> |
| ![image-20240429-100633.png](<../../../.gitbook/assets/image-20240429-100633 (1).png>) | <p><a href="https://www.pfsense.org/download/">PFsense</a><br><br><a href="../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/other-operating-systems-bedrock-v3000/installing-pfsense.md">Console installation instructions</a></p>  |
| ![image-20240429-100713.png](<../../../.gitbook/assets/image-20240429-100713 (1).png>) | <p><a href="https://opnsense.org/download/">OPNsense</a><br><br><a href="../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/other-operating-systems-bedrock-v3000/installing-opnsense.md">Console installation instructions</a></p>   |

> \[!INFO] (1) HoneyComb AMD V3000 by default is headless, installation will require additional hardware to install Windows using a display adapter, or additional kernel parameters to enable ttyS4 on linux.

> \[!INFO] (2) As of JUL 7 2024 (FreeBSD 14.01) the AMD XGBE driver on **FreeBSD** does not fully support SFP, later versions will eventually have the driver fixed.

## Documentation

|                             | File                                               | Modified    |
| --------------------------- | -------------------------------------------------- | ----------- |
| Schematics and Board Layout | [AMD-Honeycomb.pdf](attachments/AMD-Honeycomb.pdf) | 19-JUN-2024 |
| Mechanical files            | To be added                                        |             |

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden

|                                                                                                                                                                                                                                                                                                                                                                                                               | File                                                                                         | Modified                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| <p>Labels<br><br>- No labels<br>- <a href="honeycomb-amd-v3000-mini-itx-quick-start-guide.md#section-e120b7fe-9fdc-48c7-a3d9-584f8e027f40">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/592904196/AMD-Honeycomb.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | PDF File [AMD-Honeycomb.pdf](../../../wiki/download/attachments/592904196/AMD-Honeycomb.pdf) | Jun 19, 2024 by [Lior Jigalo](../../../wiki/people/639882b3f7f0ee492fcea976/) |
