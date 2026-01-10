
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Other operating systems - Bedrock V3000](../Other%20operating%20systems%20-%20Bedrock%20V3000.md)

# Installing OPNsense

## Test setup

The installation was validated at SolidRun using the following setup:

- OPNSENSE 23.7
- Terminal software:

  - Putty
  - Alternatively, Tio can also be used.  
    **known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
- USB flash disk: Kingston Data Traveler

# Installation process

## Creating bootable USB drive

Please follow instructions at [Creating bootable USB drive](https://solidrun.atlassian.net/l/cp/m9Reo11r)

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

  ![](../../../../../attachments/b5bc6212-37ae-4548-bd6e-5bdb4cabfdc5.png)
- Press "esc" or the arrow buttons to go to the boot option shell
- Set the console redirection (copy to the terminal):

  - `set hw.uart.console="mm:0xfedc9000,rs:2"`

    - NOTE: the line you paste might look a little weird especially if you type it manually  
      example for copy: /K |et hw.uart.console="mm:0xfedc9000,rs:2"  
      example for manual typing: \e|/-\|/r-\co|sol/-\|m:/x-ed\9|0/-\|:/"  
      **THIS IS FINE AS LONG AS THE ACTUAL INPUT TEXT IS CORRECT**
  - Type `boot`
- After the system has booted you are prompted with a login

  - To use it as a live system you can login as:

    - Username: root
    - Password: opnsense
  - To install OPNsense login as:

    - Username: installer
    - Password: opnsense
    - From here on, I will reffer to the installer option:
- Choose keymap

  ![](../../../../../attachments/ae79e2bb-2031-4f82-8e1a-6491962f2f7f.png)

- Choose Partition scheme to be installed  
  Select UFS GPT/UEFI Hybrid

  ![](../../../../../attachments/4e178708-6077-4ac9-b60f-929e6cc5f434.png)

- Choose disk

  ![](../../../../../attachments/453f40c2-e5c2-486f-bce0-f562dc92a970.png)
- Decide about swap partition

  ![](../../../../../attachments/4a927f1b-0d27-4929-b6ca-39e09c44cac6.png)

- Confirm disk wipe

  ![](../../../../../attachments/1b1854a1-4120-4f34-86dc-208f8064b092.png)

- Wait untill installation is complete

  ![](../../../../../attachments/b4626b3c-654f-489f-89d6-fd96bdf9aaa4.png)

## After installation

- You will be prompted to change the root users password, change it
- Log in to the root user login and go into a shell
- Create a /boot/loader.conf.local file which will contain our pernmanent console enable, and add:

  - hw.uart.console="mm:0xfedc9000,rs:2"
  - console="efi"
  - Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.
