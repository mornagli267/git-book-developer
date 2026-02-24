# Installing ESXi on Bedrock R7000

## Installing ESXi on Bedrock R7000

### **Table of Contents**

* [Test Setup](installing-esxi-on-bedrock-r7000.md#setup)
* [Installation Process](installing-esxi-on-bedrock-r7000.md#process)
  * [Creating a Bootable USB Drive](installing-esxi-on-bedrock-r7000.md#bootable)
  * [Connecting to Serial Console](installing-esxi-on-bedrock-r7000.md#console)
  * [BIOS Boot select](installing-esxi-on-bedrock-r7000.md#bselect)
  * [Installation](installing-esxi-on-bedrock-r7000.md#install)

### Test setup

This installation process has been validated by SolidRun with the following configurations:

* CPU: Ryzen 7 7840U
* A-data 1TB
* ESXi version: 8.0.2
* USB flash disk: Kingston Data Traveler

## Installation process

### Creating bootable USB drive

Please follow instructions at[Creating Bootable USB Drive for Bedrock R7000](../howto-guides-bedrock-r8000-r7000/creating-bootable-usb-drive-for-bedrock-r7000.md)\
It is recommended to use the Rufus (windows method for .iso files).

### Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](../../../../../v3000/sbc-platform/bedrock-v3000-technical-documentation/software-bedrock-v3000/using-serial-console-with-bedrock.md)

### BIOS Boot select

You need to choose your USB bootable device to start the installation.

* Insert the USB media to the device
* Turn on Bedrock
* Repetitively press the DEL / ESC key to enter the BIOS setup
* In BIOS go to -> Save & Exit -> -> yes

### Installation

* Wait until the installer will finishe setting up and prompt you to continue the installation ,(the last part of the loading could take some time, this is fine).
* Press Enter
* Accept user agreement, press F11
* Choose installation disk, press Enter
* Choose a keyboard layout, press Enter
* Choose root password , choose a password and pres Enter
* Confirm destructive action
* Wait until the installation finishes
* Remove the installlation media and reboot the device
* System will reboot, wait for it to power on
* After system boots you will se the following screen You can connect using any of the methods shown in the screen.
* Login to your account
  * username: root
  * Password: \*password you choose during installation\*
* Thats it
