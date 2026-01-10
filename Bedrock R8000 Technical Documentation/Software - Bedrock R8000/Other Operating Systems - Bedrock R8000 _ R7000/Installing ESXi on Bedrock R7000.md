---
tags:
  - '#bedrock-r8000'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [Other Operating Systems - Bedrock R8000 | R7000](../Other%20Operating%20Systems%20-%20Bedrock%20R8000%20_%20R7000.md)

# Installing ESXi on Bedrock R7000

## **Table of Contents**

- [Test Setup](#test-setup)
- [Installation Process](#installation-process)

  - [Creating a Bootable USB Drive](#creating-a-bootable-usb-drive)
  - [Connecting to Serial Console](#connecting-to-serial-console)
  - [BIOS Boot select](#bios-boot-select)
  - [Installation](#installation)

## Test setup

This installation process has been validated by SolidRun with the following configurations:

- CPU: Ryzen 7 7840U
- A-data 1TB
- ESXi version: 8.0.2
- USB flash disk: Kingston Data Traveler

# Installation process

## Creating bootable USB drive

Please follow instructions at[Creating Bootable USB Drive for Bedrock R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000/Creating%20Bootable%20USB%20Drive%20for%20Bedrock%20R7000.md)  
It is recommended to use the Rufus (windows method for .iso files).

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock](../../../Bedrock%20V3000%20Technical%20Documentation/Software%20-%20Bedrock%20V3000/Using%20serial%20console%20with%20Bedrock.md)

## BIOS Boot select

You need to choose your USB bootable device to start the installation.

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes

## Installation

- Wait until the installer will finishe setting up and prompt you to continue the installation ,(the last part of the loading could take some time, this is fine).
- Press Enter

![](../../../../../attachments/98663439-3811-4724-9413-87c2a4a4826d.png)

- Accept user agreement, press F11

  ![](../../../../../attachments/b0728261-74f0-4d09-ab25-e181b2c98411.png)

- Choose installation disk, press Enter

  ![](../../../../../attachments/a6335c06-cf46-4ae9-a036-956aec460671.png)
- Choose a keyboard layout, press Enter

  ![](../../../../../attachments/61029fe5-2a3f-4962-8d1d-5b03bac7bb75.png)

- Choose root password , choose a password and pres Enter

  ![](../../../../../attachments/6cc23599-a84b-4f8d-bfb6-d7107683ec44.png)
- Confirm destructive action

  ![](../../../../../attachments/8a1cae56-bb2c-487b-80ca-430eff50b308.png)

- Wait until the installation finishes

  ![](../../../../../attachments/1b8abac7-0473-4ffb-a721-282fcfdb8b4c.png)

- Remove the installlation media and reboot the device

  ![](../../../../../attachments/afbee613-2bd2-4d9b-be0e-bf994e2d4f52.png)

- System will reboot, wait for it to power on
- After system boots you will se the following screen

  ![](../../../../../attachments/777b2690-a991-4b5b-995c-2c970887ca91.png)

  You can connect using any of the methods shown in the screen.

- Login to your account

  - username: root
  - Password: \*password you choose during installation\*

    ![](../../../../../attachments/66638c8b-1fc6-4857-9040-17a33517adb7.png)
- Thats it

  ![](../../../../../attachments/b4a8293c-2b80-4df0-a2a1-537227f37762.png)
