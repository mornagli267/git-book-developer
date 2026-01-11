# HoneyComb AMD R8000 mini ITX Quick Start Guide

* * *

![HoneyComb R8000 AMD Ryzen CoM6 sideways (with Heatsink and fan).png](./attachments/HoneyComb%20R8000%20AMD%20Ryzen%20CoM6%20sideways%20(with%20Heatsink%20and%20fan).png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [Honeycomb AMD R8000](https://www.solid-run.com/embedded-industrial-iot/honeycomb-ryzen-r8000/) products which use the Ryzen R8000 COM.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 16 Jun 2024 |     | 1.0 |     |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product Specifications](#product-specifications)<br>- [Block Diagram](#block-diagram)<br>- [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Booting the machine](#booting-the-machine)<br>- [Booting to OS](#booting-to-os)<br>- [SO-DIMM Modules](#so-dimm-modules)<br>- [OS list](#os-list)<br>- [Documentation](#documentation) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product Specifications

|     | **Honeycomb Ryzen V3000** |
| --- | --- |
| I/Os | 3 x USB 2.0<br><br>3 x USB 3.0<br><br>2x Mini-DPs<br><br>1x HDMI |
| Networking | 2 x 2.5 GbE (Intel I226) |
| Processor | Hawk Point 8840U - 8 Cores  <br>Strix Point HX370 - 12 Cores |
| Memory & Storage | Up to 64GB DDR5 4800 MT/s  <br>2x SATA interfaces  <br>M.2 NVME GEN 4.0 x4 |
| Misc. | BMC Functionality  <br>PWM Fan header |
| Development and Debug interfaces | Micro USB |
| Power | ATX standard |
| Expansion card I/Os | PCIe x4 Gen 4.0 |
| Temperature | Industrial: -45°C to 85°C |
| Dimensions | PCBA: 170 x 170mm |

<a id="block-diagram"></a>

## **Block Diagram**

Coming soon…

<a id="visual-features-overview"></a>

## Visual features overview

Please see below the features overview of the HoneyComb AMD R8000 mini ITX

![image-20260108-150901.png](./attachments/image-20260108-150901.png)

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up the board:

- Linux or Windows PC
- HoneyComb AMD R8000 mini ITX
- ATX 60W+
- Mini-USB to USB for console, the HoneyComb R8000 has an onboard FTDI chip.
- IP router or IP switch

<a id="booting-the-machine"></a>

## Booting the machine

Download & install images:

You can use the [Ubuntu server installation instructions](../../../homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/linux-bedrock-v3000/installing-ubuntu-server-using-console.md) page or download [Pre-installed images](../../../homepage/other-articles/snippets/bedrock-images-info.md).

If using the Pre-installed image, flash it to a USB stick using the following commands:

```
gunzip <image_name.img.gz>
dd if=<image_name.img> of=/dev/sdx bs=1M status=progress; sync
```

> [!NOTE]
> NOTE: check the /dev/sdx device you need using the `lsblk` command

<a id="booting-to-os"></a>

## Booting to OS

Insert the USB stick to the device and power it on.

Wait for the device to boot.

> [!INFO]
> Very first boot might take a while due to DDR training

<a id="so-dimm-modules"></a>

## SO-DIMM Modules

For some SO-DIMM modules that work on SolidRun hardware platforms, please refer to [List of tested SO-DIMMs](../../../homepage/other-articles/snippets/list-of-so-dimm-ram-modules-tested-with-ryzen-v3000-com7.md) .

<a id="os-list"></a>

## OS list

| **OS** |     |
| --- | --- |
| ![image-20240429-104614.png](./attachments/image-20240429-104614.png) | [Ubuntu](https://ubuntu.com/download)<br><br>[Console installation instructions](../../../homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/linux-bedrock-v3000/installing-ubuntu-server-using-console.md) |
| ![image-20240429-100250.png](./attachments/image-20240429-100250.png) | [Fedora](https://fedoraproject.org/) |
| ![image-20240429-100554.png](./attachments/image-20240429-100554.png) | [Windows](https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d) (1) |
| ![image-20240429-100517.png](./attachments/image-20240429-100517.png) | [Buildroot](https://github.com/buildroot/buildroot)<br><br>A BuildRoot image can be build for x86 platform (ttyS4) should be enabled |
| ![image-20240429-100852.png](./attachments/image-20240429-100852.png) | [FreeBSD](https://www.freebsd.org/where/) (2)<br><br>[Console installation instructions](../../../homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/other-operating-systems-bedrock-v3000/installing-freebsd.md) |
| ![image-20240429-100633.png](./attachments/image-20240429-100633.png) | [PFsense](https://www.pfsense.org/download/)<br><br>[Console installation instructions](../../../homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/other-operating-systems-bedrock-v3000/installing-pfsense.md) |
| ![image-20240429-100713.png](./attachments/image-20240429-100713.png) | [OPNsense](https://opnsense.org/download/)<br><br>[Console installation instructions](../../../homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/other-operating-systems-bedrock-v3000/installing-opnsense.md) |

> [!INFO]
> (1) HoneyComb AMD R8000 can be used in headless mode with no displays connected, installation will require monitors to be connected to install Windows.

> [!INFO]
> (2) As of JUL 7 2024 (FreeBSD 14.01) the AMD XGBE driver on **FreeBSD** does not fully support SFP, later versions will eventually have the driver fixed.

<a id="documentation"></a>

## Documentation

|     | File | Modified |
| --- | --- | --- |
| Schematics and Assy Files | [amd-mitx-cex6-1.0.0.pdf](./attachments/amd-mitx-cex6-1.0.0.pdf)<br><br>[AMD-MITX-CEX6-Assy.zip](./attachments/AMD-MITX-CEX6-Assy.zip) | 07-JAN-2026 |
| Mechanical files | [AMD-MITX-CEX6-dxf.zip](./attachments/AMD-MITX-CEX6-dxf.zip)<br><br>[AMD-MITX-CEX6-STEP.zip](./attachments/AMD-MITX-CEX6-STEP.zip) | 07-JAN-2026 |