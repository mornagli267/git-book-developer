# LX2162A SOM Errata List

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| November 19, 2022 | Rabeeh Khoury | 1.0 | Released information |
| May 2, 2023 | Rabeeh Khoury | 1.1 | Errata fix |
| Dec 31, 2024 | Josua Mayer | 1.2 | Errata for SPD |

{% hint style="info" %}
No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.
{% endhint %}


<a id="introduction"></a>

## Introduction

|     |     |     |     |
| --- | --- | --- | --- |
| **Short Description** | **Errata** | **Affected PCB rev** | **Fix or workaround** |
| SD1 lane #0 not functional | Due to design bug serdes SD1 lane #0 LX2162 receive are shorted and due to that not functional. The ssignal names are SD1\_RX0\_N and SD1\_RX0\_P on the board to board header. | 1.0 | Fixed and verified in PCB rev 1.1<br><br>~Will be fixed in rev 1.1~ |
| Fan controller PWM not functional. Tachometer and temperature sensors are functional. | Due to design bug, the AMC6821 temperature sensor and fan controller has it’s THERM# signal pulled down permanently, which forces the fan controller to set the RPM to the maximum (PWM signal becomes fixed).<br><br>Notice that the Tachometer is still functional and unrelated to the THERM# signal. | 1.0 | Fixed and verified in PCB rev 1.1<br><br>~Will be fixed in rev 1.1~ |
| System unstable under load when using 16GB DDR size variant of SoM. | Due to a mistake in the SPD eeprom the revision 1.1 16GB size variant of SoM operates sdram beyond specification. 8GB variant is not affected.<br><br>See Update Instructions below. | 1.1 | Units produced in 2025 or later ship with updated SPD. |
| ECC Memory assembled but not active. | SoMs revision 1.1 have the parts for ecc memory assembled but not enabled through SPD eeprom.<br><br>See Update Instructions below. | 1.1 | Units produced in 2025 or later ship with updated SPD. |

<a id="update-rev-11-som-spd-eeprom"></a>

## Update rev. 1.1 SoM SPD EEPROM

The SPD EEPROM on the SoM can be reprogrammed with updated parameters enabling ECC, and ensuring stable oepration of 16GB variant.

1. Download special recovery image according to SoM and program to microSD card:  
\- For 8GB DDR Size: [lx2162a\_rev2\_som\_clearfog\_2000\_650\_2900\_18\_9\_0\_staticmem-8G-716a952.img.xz](https://solidrn-my.sharepoint.com/:u:/g/personal/josua_solid-run_com/Ecy-bz-YjTxPqN3-p01ZvnwBVTI9x6oVKybgNlhrNGiPNw?e=hg168f)  
\- For 16GB DDR Size: [lx2162a\_rev2\_som\_clearfog\_2000\_650\_2900\_18\_9\_0\_staticmem-16G-716a952.img.xz](https://solidrn-my.sharepoint.com/:u:/g/personal/josua_solid-run_com/Ec0Z9-tM141Bh0mGx0Abbf8BcZNzY0pHBH_I7-njPQ9fzw?e=X8Td1r)
2. Seat SoM on LX2162A Clearfog board, set boot-switches for SD ( OFF ON ON ON X )
3. Boot to Linux, login as “root”:”root”, then execute script for updating SPD:  
  
\- For 8GB DDR Size: `./lx2162-som-v11-8gb-spd.sh`  
\- For 16GB DDR Size: `./lx2162-som-v11-16gb-spd.sh`  
  
The script will program and validate SPD. On success it will show: `/sys/bus/i2c/devices/0-0051/eeprom: OK`  
4. Update is complete, any generic image should be bootable now using updated parameters.

Developers may use the update scripts directly, after disabling spd eeprom in device-tree to allow writing: [lx2162-som-v11-8gb-spd.sh](./attachments/lx2162-som-v11-8gb-spd.sh)
 [lx2162-som-v11-16gb-spd.sh](./attachments/lx2162-som-v11-16gb-spd.sh)