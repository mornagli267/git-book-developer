# Installing Ubuntu server using console

Bedrock V3000 lacks an integrated display adapter. Consequently, to install Ubuntu, users must connect Bedrock to a host PC using a console, facilitated by serial over USB.

This document describes Ubuntu installation process on Bedrock V3000.

<a id="table-of-contents"></a>

## **Table of Contents**

- [Test Setup](installing-ubuntu-server-using-console.md#setup)
- [Installation Process](installing-ubuntu-server-using-console.md#installation)
  - [Creating a Bootable USB Drive](installing-ubuntu-server-using-console.md#bootable)
  - [Connecting to Serial Console](installing-ubuntu-server-using-console.md#serial)
  - [BIOS Boot select](installing-ubuntu-server-using-console.md#bios)
  - [Configuring Grub](installing-ubuntu-server-using-console.md#grub)
  - [Live USB Settings](installing-ubuntu-server-using-console.md#live)
  - [Enable ttyS4 Service](installing-ubuntu-server-using-console.md#ttys4)

<a id="test-setup"></a>

## Test setup

This installation process has been validated by SolidRun with the following configurations:

- Ubuntu versions:
  - Ubuntu server 22.04
  - Ubuntu server 23.04
  - Ubuntu server 24.04
- Terminal software:
  - Putty
- USB flash disk: Kingston Data Traveler

<a id="installation-process-creating-bootable-usb-drive"></a>

# Installation process  
Creating bootable USB drive

Please follow instructions at [/amd/v3000/sbc-platform/bedrock-v3000-technical-documentation/software-bedrock-v3000/creating-bootable-usb-drive-for-bedrock-v3000.md](/amd/v3000/sbc-platform/bedrock-v3000-technical-documentation/software-bedrock-v3000/creating-bootable-usb-drive-for-bedrock-v3000.md)

<a id="connecting-serial-console"></a>

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](../../software-bedrock-v3000/using-serial-console-with-bedrock.md)

<a id="bios-boot-select"></a>

## BIOS Boot select

You need to choose your USB bootable device to start the installation.

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes
- Device will reset and a grub menu screen will appear
  - If you dont see a grub menu, reboot and press the “arrow down” key repetitively right after you pressed enter to boot from BIOS

<a id="configure-grub"></a>

## Configure grub

At the grub menu (displaying "try or install Ubuntu"),Press ‘e’ to set the boot parameters.

- You'll encounter a window resembling:
```
setparams 'Install Ubuntu Server'
set gfxpayload=keep
linux        /casper/vmlinuz   quiet  --- 
initrd        /casper/initrd
```
- Remove the quiet parameter and change the entry that starts with ‘linux’ to look as follows:
- ```
linux /casper/vmlinuz console=tty1 console=ttyS4,115200n8 systemd.wants=serial-getty@ttyS4 —
```
- Wait for the live USB to boot

{% hint style="info" %}
**might take some time for the installer to run, so just give it some time**
{% endhint %}


<a id="live-usb-settings"></a>

## Live USB settings

- After live USB boots
- Run `sudo subiquity`
  - NOTE: On newer Ubuntu versions the installer might run automatically, so you can skip this step.
- If you see a “waiting for cloud init” message, wait until it times out and opens the installer (could take some time since some services should finish starting in the background).
- Proceed with your preferred installation settings and await completion
- Wait until installation is complete
- When prompted, remove the installation media and press enter
- Device will be rebooted

<a id="enable-ttys4-service"></a>

## Enable ttyS4 service

{% hint style="info" %}
On Ubuntu 24+ this step is not required, installer does this on its own.
{% endhint %}


Enable the ttyS4 console to be able to interact with the system.

- Boot into BIOS
- Boot from the disk you installed linux on
- If you don't get a grub menu automatically, press the “arrow down” key repetitively right after you pressed enter to boot from BIOS
  - If you dont get the grub menu after pressing shift, connect a keyboard to the device and hold shift on the connected keyboard when booting
- In the grub menu choose:
  - Advanced options for Ubuntu
  - Select the line that says recovery mode
  - Press ’e’
  - In the line that says: linux        /boot/vmlinuz-5.15.0-43-generic root=UUID=4c58e5aa-6443-4fb2-84e7-4ac2265a7b9e ro recovery nomodeset dis\_ucode\_ldr
  - Add the console parameters to grub after the ‘ro’ parameter
    - from this:
    - ```
linux        /boot/vmlinuz-6.2.0-27-generic root=UUID=1dfc1a94-6289-4b15-9f4f-0fb36c083841 ro
```
    - to this:
      - ```
linux        /boot/vmlinuz-6.2.0-27-generic root=UUID=1dfc1a94-6289-4b15-9f4f-0fb36c083841 ro
console=tty1 console=ttyS4,115200n8 systemd.wants=serial-getty@ttyS4 quiet
```
      - Note: if you want to see the boot logs remove the `quiet` argumentPress ctrl+x to boot
- Type to enable the ttyS4 service automatically when you boot: `systemctl enable serial-getty@ttyS4`
- edit grub config file: `nano /etc/default/grub`
  - add the console redirection to the grub default options (same as above):  
on line: `GRUB_CMDLINE_LINUX_DEFAULT` add the following
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet console=tty1 console=ttyS4,115200n8"
```
  - save the file and run: `update-grub`