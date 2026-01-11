# HoneyComb / ClearFog CX LX2 Errata List

<a id="revisions-and-notes"></a>

## **Revisions and Notes**

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 13 Nov 2019 | Rabeeh Khoury | 1.0 | Released information |
| Table of Contents | - [Revisions and Notes](#revisions-and-notes)<br>- [Introduction](#introduction)<br>  - [HoneyComb / ClearFog CX Errata](#honeycomb-clearfog-cx-errata) |     |     |

**Disclaimer**

> [!INFO]
> No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.

<a id="introduction"></a>

## Introduction

The intention of this document is to list erratas of HoneyComb / ClearFog CX mini ITX carrier board.

HoneyComb and ClearFog CX shares the same PCB design and the difference is in assembly options where ClearFog CX adds the QSFP28 interface

<a id="honeycomb-clearfog-cx-errata"></a>

#### HoneyComb / ClearFog CX Errata

| **Short Description** | **Errata** | **Affected PCB rev** | **Fix or workaround** |
| --- | --- | --- | --- |
| QSFP28 ModSel# signal is floating | ModSel# signal is used to select the QSFP module inserted in the cage thus enabling it to respond to I2C transactions. QSFP28 connector (J23 in the schematics) is assembled only on the ClearFog CX sku. As a workaround all boards boards rev 1.1 sent to partners and customers includes a touch-up wire that connects TP121 (ModSel# signal) to GND. | 1.1 | Issue will be fixed in rev 1.2 |
| USB 3.0 RX and TX p/n are swapped | Upper USB 3.0 on the combo dual USB 3.0 connector has TX p/n and RX p/n swapped.<br><br>The lower USB 3.0 on the combo connector is fully functional.<br><br>No workaround is available for this. | 1.1 | Issue will be fixed in rev 1.2 |