# Installing OPNsense

<a id="test-setup"></a>

## Test setup

The installation was validated at SolidRun using the following setup:

- OPNSENSE 23.7  
- Terminal software:
  - Putty
  - Alternatively, Tio can also be used.  
**known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
- USB flash disk: Kingston Data Traveler

<a id="installation-process"></a>

# Installation process

<a id="creating-bootable-usb-drive"></a>

## Creating bootable USB drive

Please follow instructions at [Creating bootable USB drive](https://solidrun.atlassian.net/l/cp/m9Reo11r)

<a id="connecting-serial-console"></a>

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](https://solidrun.atlassian.net/wiki/spaces/developer/pages/472481800)

<a id="bios-settings"></a>

## BIOS settings

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes
- Device will reset and a PFsense boot screen will appear

<a id="after-boot"></a>

## After boot

- When you see the main boot menu:![](./attachments/GetImage%20(12).png)
- Press "esc" or the arrow buttons to go to the boot option shell 
- Set the console redirection (copy to the terminal): 
  - `set hw.uart.console="mm:0xfedc9000,rs:2"`
    - NOTE: the line you paste might look a little weird especially if you type it manually   
example for copy: /K |et hw.uart.console="mm:0xfedc9000,rs:2"   
example for manual typing: \\e|/-\\|/r-\\co|sol/-\\|m:/x-ed\\9|0/-\\|:/"   
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
- Choose keymap![](./attachments/GetImage%20(13).png)

- Choose Partition scheme to be installed  
Select UFS GPT/UEFI Hybrid![](./attachments/GetImage%20(14).png)

- Choose disk![](./attachments/GetImage%20(15).png)
- Decide about swap partition ![](./attachments/GetImage%20(16).png)

- Confirm disk wipe ![](./attachments/GetImage%20(17).png)

- Wait untill installation is complete ![](./attachments/GetImage%20(18).png)

<a id="after-installation"></a>

## After installation

- You will be prompted to change the root users password, change it
- Log in to the root user login and go into a shell
- Create a /boot/loader.conf.local file which will contain our pernmanent console enable, and add: 
  - hw.uart.console="mm:0xfedc9000,rs:2" 
  - console="efi" 
  - Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.