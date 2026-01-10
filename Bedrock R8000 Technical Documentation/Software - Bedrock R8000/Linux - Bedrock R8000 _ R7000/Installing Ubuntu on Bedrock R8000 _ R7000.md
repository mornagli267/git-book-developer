---
tags:
  - '#amd-os'
  - '#bedrock-r8000'
  - '#linux'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [Linux - Bedrock R8000 | R7000](../Linux%20-%20Bedrock%20R8000%20_%20R7000.md)

# Installing Ubuntu on Bedrock R8000 | R7000

Installation was tested on:

- Ubuntu 22.04
- Ubuntu 23.04
- Ubuntu 24.04

> [!IMPORTANT]
> Ubuntu **20.04** does not have intel i226 [igc] driver on kernel **5.4**

## [Creating Bootable USB Drive for Bedrock R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000/Creating%20Bootable%20USB%20Drive%20for%20Bedrock%20R7000.md)

## Boot

- Connect power to bedrock
- Press 'DEL' repetitively to enter BIOS setup
- Go to the save & exit tab and boot from your USB flash drive

> [!IMPORTANT]
> If you have problems with installation, please disable secure boot in BIOS → boot> security → secure boot-> disable

## Installation

- A grub menu will open, choose “try or install ubuntu”

  ![](../../../../../attachments/c8d9dcbd-5972-4be1-a779-7168ace59589.png)
- After the system boots, an installer window will open, at this point if you want to try ubuntu, you can close this window and use ubuntu as a live environment, to install ubuntu, just proceed with the installer and select your language.

  ![](../../../../../attachments/0a1ae724-3610-46ba-b9dd-980f0e5f1ba5.png)
- Select keyboard layout

  ![](../../../../../attachments/e0884718-888d-409e-8d20-9fa0e2d9e107.png)
- Select updates and software, if you dont know what to choose, just press Continue

  ![](../../../../../attachments/cb60c3e3-adaa-43c0-ae61-fa1be210129e.png)
- Choose installation type, Ubuntu supports multiple installation types:

  - Erase disk and install Ubuntu (easiest option)
  - Install Ubutnu alongside windows (will be visible only if ubuntu detects that you have windows installed) choose only if you want to dualboot windows and Ubuntu.
  - Something else (custom partitioning)

![](../../../../../attachments/4571bdd7-4cd0-460f-a392-bba9dfe347e3.png)

- Press Install Now
- choose your region

  ![](../../../../../attachments/1858122c-7371-46a2-bf36-78f6e7da04cb.png)
- Choose computer name, username and password and press Continue

  ![](../../../../../attachments/28e983dc-7c85-46d6-b411-152fa837f3ec.png)
- wait for the isntallation to finish

  ![](../../../../../attachments/72af8cb9-464a-4c0f-a6ad-a3b14d059bc0.png)
- After the installation is finished press Restart now

  ![](../../../../../attachments/3ecd6167-31cd-4cb7-b770-f501cddbea52.png)
- System will restart and you’re done
