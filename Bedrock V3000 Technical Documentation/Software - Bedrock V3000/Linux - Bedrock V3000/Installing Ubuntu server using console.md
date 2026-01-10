---
tags:
  - '#amd-os'
  - '#amd-images'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Linux - Bedrock V3000](../Linux%20-%20Bedrock%20V3000.md)

# Installing Ubuntu server using console

Bedrock V3000 lacks an integrated display adapter. Consequently, to install Ubuntu, users must connect Bedrock to a host PC using a console, facilitated by serial over USB.

This document describes Ubuntu installation process on Bedrock V3000.

## **Table of Contents**

- [Test Setup](#test-setup)
- [Installation Process](#installation-process)

  - [Creating a Bootable USB Drive](#creating-a-bootable-usb-drive)
  - [Connecting to Serial Console](#connecting-to-serial-console)
  - [BIOS Boot select](#bios-boot-select)
  - [Configuring Grub](#configuring-grub)
  - [Live USB Settings](#live-usb-settings)
  - [Enable ttyS4 Service](#enable-ttys4-service)

## Test setup

This installation process has been validated by SolidRun with the following configurations:

- Ubuntu versions:

  - Ubuntu server 22.04
  - Ubuntu server 23.04
  - Ubuntu server 24.04
- Terminal software:

  - Putty
- USB flash disk: Kingston Data Traveler

# Installation process Creating bootable USB drive

Please follow instructions at <https://solidrun.atlassian.net/l/cp/m9Reo11r>

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock](../Using%20serial%20console%20with%20Bedrock.md)

## BIOS Boot select

You need to choose your USB bootable device to start the installation.

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes
- Device will reset and a grub menu screen will appear

  - If you dont see a grub menu, reboot and press the “arrow down” key repetitively right after you pressed enter to boot from BIOS

## Configure grub

At the grub menu (displaying "try or install Ubuntu"),Press ‘e’ to set the boot parameters.

- You'll encounter a window resembling:

  ```java
  setparams 'Install Ubuntu Server'
  set gfxpayload=keep
  linux        /casper/vmlinuz   quiet  --- 
  initrd        /casper/initrd
  ```
- Remove the quiet parameter and change the entry that starts with ‘linux’ to look as follows:
- ```java
  linux /casper/vmlinuz console=tty1 console=ttyS4,115200n8 systemd.wants=serial-getty@ttyS4 —
  ```
- Wait for the live USB to boot

> [!IMPORTANT]
> **might take some time for the installer to run, so just give it some time**

## Live USB settings

- After live USB boots
- Run `sudo subiquity`

  - NOTE: On newer Ubuntu versions the installer might run automatically, so you can skip this step.
- If you see a “waiting for cloud init” message, wait until it times out and opens the installer (could take some time since some services should finish starting in the background).
- Proceed with your preferred installation settings and await completion
- Wait until installation is complete
- When prompted, remove the installation media and press enter
- Device will be rebooted

## Enable ttyS4 service

> [!IMPORTANT]
> On Ubuntu 24+ this step is not required, installer does this on its own.

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
    - ```java
      linux        /boot/vmlinuz-6.2.0-27-generic root=UUID=1dfc1a94-6289-4b15-9f4f-0fb36c083841 ro
      ```
    - to this:

      - ```java
        linux        /boot/vmlinuz-6.2.0-27-generic root=UUID=1dfc1a94-6289-4b15-9f4f-0fb36c083841 ro
        console=tty1 console=ttyS4,115200n8 systemd.wants=serial-getty@ttyS4 quiet
        ```
      - Note: if you want to see the boot logs remove the `quiet` argumentPress ctrl+x to boot
- Type to enable the ttyS4 service automatically when you boot: `systemctl enable serial-getty@ttyS4`
- edit grub config file: `nano /etc/default/grub`

  - add the console redirection to the grub default options (same as above):  
    on line: `GRUB_CMDLINE_LINUX_DEFAULT` add the following

    ```java
    GRUB_CMDLINE_LINUX_DEFAULT="quiet console=tty1 console=ttyS4,115200n8"
    ```
  - save the file and run: `update-grub`
