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

Please follow instructions at [Using serial console with Bedrock V3000](../../../bedrock-v3000-technical-documentation/software-bedrock-v3000/using-serial-console-with-bedrock.md)

### BIOS Boot select

You need to choose your USB bootable device to start the installation.

* Insert the USB media to the device
* Turn on Bedrock
* Repetitively press the DEL / ESC key to enter the BIOS setup
* In BIOS go to -> Save & Exit -> -> yes

### Installation

* Wait until the installer will finishe setting up and prompt you to continue the installation ,(the last part of the loading could take some time, this is fine).
* Press Enter

![](../../../../../.gitbook/assets/image-20231217-151103.png)

* Accept user agreement, press F11![](../../../../../.gitbook/assets/image-20231217-151246.png)
* Choose installation disk, press Enter![](../../../../../.gitbook/assets/image-20231217-153144.png)
* Choose a keyboard layout, press Enter![](../../../../../.gitbook/assets/image-20231217-154235.png)
* Choose root password , choose a password and pres Enter![](../../../../../.gitbook/assets/image-20231217-154539.png)
* Confirm destructive action![](../../../../../.gitbook/assets/image-20231217-155134.png)
* Wait until the installation finishes![](../../../../../.gitbook/assets/image-20231217-155213.png)
* Remove the installlation media and reboot the device![](../../../../../.gitbook/assets/image-20231217-161213.png)
* System will reboot, wait for it to power on
* After system boots you will se the following screen![](../../../../../.gitbook/assets/image-20231217-161430.png) You can connect using any of the methods shown in the screen.
* Login to your account
  * username: root
  * Password: \*password you choose during installation\*![](../../../../../.gitbook/assets/image-20231217-161731.png)
* Thats it![](../../../../../.gitbook/assets/image-20231217-161834.png)
