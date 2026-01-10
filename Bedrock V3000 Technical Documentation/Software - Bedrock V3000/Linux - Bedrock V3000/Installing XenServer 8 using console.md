
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Linux - Bedrock V3000](../Linux%20-%20Bedrock%20V3000.md)

# Installing XenServer 8 using console

Bedrock V3000 lacks an integrated display adapter. Consequently, to install Xen server 8, users must connect Bedrock to a host PC using a console, facilitated by serial over USB.

This document describes Xen server 8 installation process on Bedrock V3000.

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

- Xen versions:

  - XenServer 8
- Terminal software:

  - Putty
- USB flash disk: Kingston Data Traveler

# Installation process

## Creating bootable USB drive

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

At the grub menu (displaying "install", “no-serial“, …),Press ‘e’ over the ”install” option to set the boot parameters.

- You'll encounter a window resembling:

  ```java
  setparams 'install'                                                         
  	multiboot2 /boot/xen.gz dom0_max_vcpus=1-16 dom0_mem=max:8192M com1=115200,8n1 console=com1,vga                                                    │
  	module2 /boot/vmlinuz console=hvc0 console=tty0
  	module2 /install.img
  ```
- Change the entry that starts with ‘module2 /boot/vmlinuz’ to look as follows:
- ```java
  module2 /boot/vmlinuz console=hvc0 console=tty0 console=ttyS4,115200n8
  ```
- Wait for the live USB to boot to the installer

> [!IMPORTANT]
> **might take some time for the installer to run, so just give it some time**

## Live USB settings

- After live USB boots, the installer will start

![image-20241117-084728.png](../../../../../attachments/3f6a14d4-51bc-47ed-89e4-c06777996092.png)

- Select your Desired keymap

![image-20241117-084815.png](../../../../../attachments/b08ad130-f6db-442b-b090-ed4392d5aac4.png)

- Press OK to cuntinue with installation
- Accept EUA

![image-20241117-085031.png](../../../../../attachments/5dc5af6b-33d7-4fb2-b85a-b12c0a457818.png)

- Choose if you want to install or upgrade Xen in this case well select “Perform clean installation”

![image-20241117-085055.png](../../../../../attachments/1496d871-79b9-46d8-acca-b6f55af626a6.png)

- Select installation drive

![image-20241117-085136.png](../../../../../attachments/3795a2a6-a28c-42d7-b960-c2d8f83fec7d.png)

- Select VM storage location

![image-20241117-085218.png](../../../../../attachments/e1e3b577-ead8-49d7-a2f5-f3dc6e8aa3e2.png)

- Enable thin provisioning if required

![image-20241117-085308.png](../../../../../attachments/c14c22cb-4134-489d-a631-e54a1379017d.png)

- Select installation media source, in this case were using a USB drive so we select Local media

![image-20241117-085400.png](../../../../../attachments/2c0c7eca-6284-4687-b9f7-dce0517cf506.png)![image-20241117-085519.png](../../../../../attachments/05eab8f1-dc2f-4736-aa94-f0fb95a3a10c.png)![image-20241117-085554.png](../../../../../attachments/98c81f5c-c34c-4f6a-b8dd-5729b1d2883e.png)

- Verify installation source

![image-20241117-085621.png](../../../../../attachments/5db0b3d1-75c4-4c80-aab6-97474537e47d.png)

- Select password

![image-20241117-085722.png](../../../../../attachments/5c6ca6c7-204d-414e-ad98-3186ac2d95d2.png)

- Choose which network interface will be used to connect to the management server

![image-20241117-085826.png](../../../../../attachments/833f8ceb-2f8f-4230-a261-c4da7740853d.png)![image-20241117-085840.png](../../../../../attachments/2b4c380a-f35a-46fe-a401-bc24b6ea9807.png)

- Configure networking settings

![image-20241117-090115.png](../../../../../attachments/79d30eec-e481-4569-b8a1-7efe36a6738c.png)![image-20241117-090143.png](../../../../../attachments/7a8997e5-64a0-4fba-964b-c415fc32dc6b.png)

- Select time zone

![image-20241117-090256.png](../../../../../attachments/ec906f82-79cf-4495-a786-e8c701da4060.png)

- Select system time settings

![image-20241117-090338.png](../../../../../attachments/8b263b4d-b3c7-432d-b766-fe050f0e1dd6.png)

- Confirm installation

![image-20241117-090413.png](../../../../../attachments/b6919e7f-d91e-4ac2-9134-0b626068d045.png)

- Wait until installation is complete

![image-20241117-090536.png](../../../../../attachments/895b7bdf-8b8d-49ea-abf5-0a8e17b978cb.png)

- Select supplemental packages if required

![image-20241117-090843.png](../../../../../attachments/e817913e-5ff5-496a-b48e-877cf95975b6.png)

- When prompted, remove the installation media and press enter
- Device will be rebooted

## Enable ttyS4 service

Enable the ttyS4 console to be able to interact with the system.

- Boot into BIOS
- Boot from the disk you installed Xen on
- If you don't get a grub menu automatically, press the “arrow down” key repetitively right after you pressed enter to boot from BIOS

  - If you dont get the grub menu after pressing shift, connect a keyboard to the device and hold shift on the connected keyboard when booting
- In the grub menu choose:

  - \*XenServer (Serial)
  - Press ’e’

```java
setparams 'XenServer (Serial)'
        search --label --set root root-umnjnb
        multiboot2 /boot/xen.gz com1=115200,8n1 console=com1,vga dom0_mem=1808M,max:1808M watchdog ucode=scan dom0_max_vcpus=1-4 crashkernel=256M,below=4G
        module2 /boot/vmlinuz-4.19-xen root=LABEL=root-umnjnb ro nolvm hpet =disable console=tty0 console=hvc0
		module2 /boot/initrd-4.19-xen.img
```

- In the line that says: `module2 /boot/vmlinuz-4.19-xen`
- Add the console parameters to grub after the `console=hvc0` parameter

  - from this:
  - ```java
    module2 /boot/vmlinuz-4.19-xen root=LABEL=root-umnjnb ro nolvm hpet =disable console=tty0 console=hvc0
    ```
  - to this:
  - ```java
    module2 /boot/vmlinuz-4.19-xen root=LABEL=root-umnjnb ro nolvm hpet =disable console=tty0 console=hvc0 console=ttyS4,115200n8 systemd.wants=serial-getty@ttyS4
    ```
- Type to enable the ttyS4 service persistently for future boots: `systemctl enable serial-getty@ttyS4`
- Edit grub config file: `nano /etc/grub-efi.cfg`

  - Add the console parameter to the file from this:

    ```java
    menuentry 'XenServer (Serial)' {
            search --label --set root root-umnjnb
            multiboot2 /boot/xen.gz com1=115200,8n1 console=com1,vga dom0_mem=1808M$
            module2 /boot/vmlinuz-4.19-xen root=LABEL=root-umnjnb ro nolvm hpet=dis$
            module2 /boot/initrd-4.19-xen.img
    ```
  - To this:

    ```java
    menuentry 'XenServer (Serial)' {
            search --label --set root root-umnjnb
            multiboot2 /boot/xen.gz com1=115200,8n1 console=com1,vga dom0_mem=1808M$
            module2 /boot/vmlinuz-4.19-xen root=LABEL=root-umnjnb ro nolvm hpet=dis$ console=ttyS4,115200n8
            module2 /boot/initrd-4.19-xen.img
    ```
- Reboot, the console should start automatically when you choose the `XenServer (Serial)` option.
