# Installing Ubuntu on Bedrock R8000 | R7000

Installation was tested on:

- Ubuntu 22.04
- Ubuntu 23.04
- Ubuntu 24.04

> [!INFO]
> Ubuntu **20.04** does not have intel i226 \[igc\] driver on kernel **5.4**

<a id="create-bootable-usb-drive-software-bedrock-r8000-howto-guides-bedrock-r8000-r7000-creating-bootable-usb-drive-for-bedrock-r7000md"></a>

## [Create bootable usb drive](../../software-bedrock-r8000/howto-guides-bedrock-r8000-r7000/creating-bootable-usb-drive-for-bedrock-r7000.md)

<a id="boot"></a>

## Boot

- Connect power to bedrock
- Press 'DEL' repetitively to enter BIOS setup
- Go to the save & exit tab and boot from your USB flash drive

> [!INFO]
> If you have problems with installation, please disable secure boot in BIOS → boot> security → secure boot-> disable

<a id="installation"></a>

## Installation

- A grub menu will open, choose “try or install ubuntu”![](./attachments/image-20231017-072854.png)
- After the system boots, an installer window will open, at this point if you want to try ubuntu, you can close this window and use ubuntu as a live environment, to install ubuntu, just proceed with the installer and select your language.![](./attachments/image-20231017-073031.png)
- Select keyboard layout![](./attachments/image-20231017-073127.png)
- Select updates and software, if you dont know what to choose, just press Continue![](./attachments/image-20231017-073221.png)
- Choose installation type, Ubuntu supports multiple installation types:
  - Erase disk and install Ubuntu (easiest option)
  - Install Ubutnu alongside windows (will be visible only if ubuntu detects that you have windows installed) choose only if you want to dualboot windows and Ubuntu.
  - Something else (custom partitioning)

![](./attachments/image-20231017-074102.png)

- Press Install Now
- choose your region![](./attachments/image-20231017-074029.png)
- Choose computer name, username and password and press Continue![](./attachments/image-20231017-074215.png)
- wait for the isntallation to finish![](./attachments/image-20231017-074314.png)
- After the installation is finished press Restart now![](./attachments/image-20231017-074359.png)
- System will restart and you’re done