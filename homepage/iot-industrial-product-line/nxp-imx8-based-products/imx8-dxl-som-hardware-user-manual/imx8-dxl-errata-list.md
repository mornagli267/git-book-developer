# i.MX8 DXL Errata List

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| November 4, 2024 | Josua Mayer | 1.0 | Released information |

{% hint style="info" %}
No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.
{% endhint %}


<a id="introduction"></a>

## Introduction

|     |     |     |     |
| --- | --- | --- | --- |
| **Short Description** | **Errata** | **Affected PCB rev** | **Fix or workaround** |
| Boot stuck in U-Boot console without console connected | When using the reference Carrier Board and Adapter Board without microUSB console connected to a PC, the system can get stuck in u-boot console after wrongly detecting noise as a key press. | Adapter Board v1.0 | Resolved by disassembling “R7” from the Adapter Board.<br><br>Fixed in v1.1. |
| Sporadic failure reading eMMC from U-Boot after software reboot | Sporadically after reboot following extended uptime U-Boot may fail reading data from eMMC and fail the boot.<br><br>1. U-Boot and Linux drivers failed to toggle the eMMC reset line<br>2. eMMC did not have reset signal enabled | SoM v2.1 and earlier | Resolved by programming the eMMC internal RST\_n\_FUNCTION efuse to value 1, and apply [patches](https://github.com/SolidRun/imx8dxl_build/commit/b7e275cc63a318e77e213548643cea4dc962b6d5) to U-Boot (and Linux) to toggle reset before use. |