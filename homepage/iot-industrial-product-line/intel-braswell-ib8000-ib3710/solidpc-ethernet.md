# SolidPC Ethernet

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 19 Apr 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Overview](#overview)<br>- [SolidPCs Ethernet Ports](#solidpcs-ethernet-ports)<br>- [Power over Ethernet Option (POE)](#power-over-ethernet-option-poe) |     |     |

<a id="overview"></a>

## Overview

![](./attachments/image-20220419-143812.png)

Ethernet is a family of computer networking technologies commonly used in local area networks (LANs) and metropolitan area networks (MANs). It was commercially introduced in 1980 and first standardized in 1983 as IEEE 802.3, and has since been refined to support higher bit rates and longer link distances.  
(source wikipedia)

<a id="solidpcs-ethernet-ports"></a>

## SolidPCs Ethernet Ports

![](./attachments/image-20220419-144050.png)

  
The SolidPC got two Ethernet Ports. One NIC is integrated into the MicroSom (#1) one has an external NIC (#2) which is located on the carrierboard. The first NIC (#1) is programmed to be always on and offers the option to be used for wake on lan (wol) and power over ethernet (poe).  
Bot NICs are Realtek RTL8111 (100/1000mbit) and have external magnetics (ATPL-453R, DUAL 100/1000 BASE-TX PoE LAN MAGNETIC).

- For further information please have a look at the schematics: [Intel Braswell IBx Documents](../intel-braswell-ib8000-ib3710/solidpc-q4.md)

<a id="power-over-ethernet-option-poe"></a>

## Power over Ethernet Option (POE)

> [!TIP]
> The SolidPC offers you the option to use a PoE module – which is not assembled!

![](./attachments/image-20220419-144350.png)

On the SolidPC you can find the pinouts for assembling a Power over Ethernet module. Some customers successfully used the Silvertel AG5300 Module.

![](./attachments/image-20220419-144327.png)