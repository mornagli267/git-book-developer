# SolidPC Ethernet

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                               | **Revision** | **Notes**       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 19 Apr 2022       |                                                                                                                                                                                                                                                                                                                                         | 1.0          | Initial release |
| Table of Contents | <p>- <a href="solidpc-ethernet.md#revision-and-notes">Revision and Notes</a><br>- <a href="solidpc-ethernet.md#overview">Overview</a><br>- <a href="solidpc-ethernet.md#solidpcs-ethernet-ports">SolidPCs Ethernet Ports</a><br>- <a href="solidpc-ethernet.md#power-over-ethernet-option-poe">Power over Ethernet Option (POE)</a></p> |              |                 |

## Overview

![](../../../.gitbook/assets/image-20220419-143812.png)

Ethernet is a family of computer networking technologies commonly used in local area networks (LANs) and metropolitan area networks (MANs). It was commercially introduced in 1980 and first standardized in 1983 as IEEE 802.3, and has since been refined to support higher bit rates and longer link distances.\
(source wikipedia)

## SolidPCs Ethernet Ports

![](../../../.gitbook/assets/image-20220419-144050.png)

The SolidPC got two Ethernet Ports. One NIC is integrated into the MicroSom (#1) one has an external NIC (#2) which is located on the carrierboard. The first NIC (#1) is programmed to be always on and offers the option to be used for wake on lan (wol) and power over ethernet (poe).\
Bot NICs are Realtek RTL8111 (100/1000mbit) and have external magnetics (ATPL-453R, DUAL 100/1000 BASE-TX PoE LAN MAGNETIC).

* For further information please have a look at the schematics: [Intel Braswell IBx Documents](solidpc-q4.md)

## Power over Ethernet Option (POE)

> \[!TIP] The SolidPC offers you the option to use a PoE module – which is not assembled!

![](../../../.gitbook/assets/image-20220419-144350.png)

On the SolidPC you can find the pinouts for assembling a Power over Ethernet module. Some customers successfully used the Silvertel AG5300 Module.

![](../../../.gitbook/assets/image-20220419-144327.png)
