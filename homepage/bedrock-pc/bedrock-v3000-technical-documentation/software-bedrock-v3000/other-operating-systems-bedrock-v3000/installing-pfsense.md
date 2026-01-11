# Installing PFsense

<a id="test-setup"></a>

## Test setup

The installation was validated at SolidRun using the following setup:

- PFsense 2.7 community
- Note: versions below 2.7 do not have drivers for intel nics and SFP
- Terminal software:
  - Putty
  - Alternatively, Tio can also be used.  
**known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
- USB flash disk: Kingston Data Traveler

<a id="installation-process"></a>

# Installation process

<a id="creating-bootable-usb-drive"></a>

## Creating bootable USB drive

Please follow instructions at [https://solidrun.atlassian.net/l/cp/m9Reo11r](https://solidrun.atlassian.net/l/cp/m9Reo11r)

<a id="connecting-serial-console"></a>

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](../../software-bedrock-v3000/using-serial-console-with-bedrock.md)

<a id="bios-settings"></a>

## BIOS settings

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes
- Device will reset and a PFsense boot screen will appear

<a id="after-boot"></a>

## After boot

- When you see the main boot menu: 

![](./attachments/GetImage%20(2).png)

- Press "esc" or the arrow buttons to go to the boot option shell 
- Set the console redirection (copy to the terminal): 
  - ```
set hw.uart.console="mm:0xfedc9000,rs:2"
```
    - NOTE: on older versions, the line you paste might look a little weird especially if you type it manually  
example for copy: /K |et hw.uart.console="mm:0xfedc9000,rs:2"   
example for manual type: \\e|/-\\|/r-\\co|sol/-\\|m:/x-ed\\9|0/-\\|:/"   
THIS IS FINE AS LONG AS THE ACTUAL TEXT WAS TYPED CORRECTLY
- Now run:
  - ```
boot
```
- You will be prompted with a console type selection, tested on console type vt100
  - NOTE: (it’s the default option so you can just press enter) 
- Accept copyright and distribution notice ![](./attachments/GetImage%20(3).png)
- Choose Install pfSense![](./attachments/GetImage%20(4).png)

- Select keymap![](./attachments/GetImage%20(5).png)

- partitioning: 
  - Available options: ![](./attachments/GetImage%20(6).png)
  - Guided Root-on-ZFS 
  - Auto (UFS) UEFI  Guided Disk Setup using UEFI boot method 
  - Auto (UFS) BIOS  Guided Disk Setup using BIOS boot method 
  - Manual - Manual Disk Setup (experts) 
  - Shell - Open a shell and partition by hand 
  - Note: Options 1 and 2 both worked on bedrock 
  - Choose entire disk or partition 
  - Choose partition scheme 
  - Review selections ![](./attachments/GetImage%20(7).png)
  - To finish, select finish 
  - Commit to selections ![](./attachments/GetImage%20(8).png)

- Wait until the installation is complete ![](./attachments/GetImage%20(10).png)
- Select yes because we will need to make the following modifications to enable console: 
  - Create the /boot/loader.conf.local file, which will contain our changes and add: 
    - hw.uart.console="mm:0xfedc9000,rs:2" 
    - console="efi" 
    - Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes. 
  - If you also don’t want to see the boot log, also add: 
    - boot\_mute="YES"  
- When done type "exit" and reboot the system

![](./attachments/GetImage%20(11).png)