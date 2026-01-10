
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Other operating systems - Bedrock V3000](../Other%20operating%20systems%20-%20Bedrock%20V3000.md)

# Installing PFsense

## Test setup

The installation was validated at SolidRun using the following setup:

- PFsense 2.7 community
- Note: versions below 2.7 do not have drivers for intel nics and SFP
- Terminal software:

  - Putty
  - Alternatively, Tio can also be used.  
    **known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
- USB flash disk: Kingston Data Traveler

# Installation process

## Creating bootable USB drive

Please follow instructions at <https://solidrun.atlassian.net/l/cp/m9Reo11r>

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock](../Using%20serial%20console%20with%20Bedrock.md)

## BIOS settings

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes
- Device will reset and a PFsense boot screen will appear

## After boot

- When you see the main boot menu:

![](../../../../../attachments/8c7326a9-9975-4dcb-be75-81bda3924ebe.png)

- Press "esc" or the arrow buttons to go to the boot option shell
- Set the console redirection (copy to the terminal):

  - ```java
    set hw.uart.console="mm:0xfedc9000,rs:2"
    ```

    - NOTE: on older versions, the line you paste might look a little weird especially if you type it manually  
      example for copy: /K |et hw.uart.console="mm:0xfedc9000,rs:2"  
      example for manual type: \e|/-\|/r-\co|sol/-\|m:/x-ed\9|0/-\|:/"  
      THIS IS FINE AS LONG AS THE ACTUAL TEXT WAS TYPED CORRECTLY
- Now run:

  - ```java
    boot
    ```
- You will be prompted with a console type selection, tested on console type vt100

  - NOTE: (it’s the default option so you can just press enter)
- Accept copyright and distribution notice

  ![](../../../../../attachments/ebcfdf5d-a6dc-4f92-ae57-ea1d2537d346.png)
- Choose Install pfSense

  ![](../../../../../attachments/f3a957c0-3f83-422e-872d-eff6981f35c9.png)

- Select keymap

  ![](../../../../../attachments/55b6b9ff-db9c-4813-a122-c7f9d7619e3c.png)

- partitioning:

  - Available options:

    ![](../../../../../attachments/bd9f0759-f999-4e97-9f3d-1c565e93fc8c.png)
  - Guided Root-on-ZFS
  - Auto (UFS) UEFI  Guided Disk Setup using UEFI boot method
  - Auto (UFS) BIOS  Guided Disk Setup using BIOS boot method
  - Manual - Manual Disk Setup (experts)
  - Shell - Open a shell and partition by hand
  - Note: Options 1 and 2 both worked on bedrock
  - Choose entire disk or partition
  - Choose partition scheme
  - Review selections

    ![](../../../../../attachments/a68d21fb-5e62-476f-8901-5bb690ab138b.png)
  - To finish, select finish
  - Commit to selections

    ![](../../../../../attachments/bbc4f576-8dbd-4a1b-8570-92e6515d293e.png)

- Wait until the installation is complete

  ![](../../../../../attachments/93e19b59-c98c-4402-823a-5de743d1b48a.png)
- Select yes because we will need to make the following modifications to enable console:

  - Create the /boot/loader.conf.local file, which will contain our changes and add:

    - hw.uart.console="mm:0xfedc9000,rs:2"
    - console="efi"
    - Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.
  - If you also don’t want to see the boot log, also add:

    - boot\_mute="YES"
- When done type "exit" and reboot the system

![](../../../../../attachments/40467598-bc51-4188-a2d4-d743fe520c6f.png)
