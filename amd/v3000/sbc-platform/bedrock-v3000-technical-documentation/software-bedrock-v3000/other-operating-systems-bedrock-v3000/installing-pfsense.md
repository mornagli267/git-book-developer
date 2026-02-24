# Installing PFsense

## Installing PFsense

### Test setup

The installation was validated at SolidRun using the following setup:

* PFsense 2.7 community
* Note: versions below 2.7 do not have drivers for intel nics and SFP
* Terminal software:
  * Putty
  * Alternatively, Tio can also be used.\
    **known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
* USB flash disk: Kingston Data Traveler

## Installation process

### Creating bootable USB drive

Please follow instructions at [/amd/v3000/sbc-platform/bedrock-v3000-technical-documentation/software-bedrock-v3000/creating-bootable-usb-drive-for-bedrock-v3000.md](../creating-bootable-usb-drive-for-bedrock-v3000.md)

### Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](../using-serial-console-with-bedrock.md)

### BIOS settings

* Insert the USB media to the device
* Turn on Bedrock
* Repetitively press the DEL / ESC key to enter the BIOS setup
* In BIOS go to -> Save & Exit -> -> yes
* Device will reset and a PFsense boot screen will appear

### After boot

* When you see the main boot menu:
* Press "esc" or the arrow buttons to go to the boot option shell
* Set the console redirection (copy to the terminal):
  * ```
    ```

set hw.uart.console="mm:0xfedc9000,rs:2"

````
    - NOTE: on older versions, the line you paste might look a little weird especially if you type it manually  
example for copy: /K |et hw.uart.console="mm:0xfedc9000,rs:2"   
example for manual type: \\e|/-\\|/r-\\co|sol/-\\|m:/x-ed\\9|0/-\\|:/"   
THIS IS FINE AS LONG AS THE ACTUAL TEXT WAS TYPED CORRECTLY
- Now run:
  - ```
boot
````

* You will be prompted with a console type selection, tested on console type vt100
  * NOTE: (it’s the default option so you can just press enter)
* Accept copyright and distribution notice&#x20;
* Choose Install pfSense
* Select keymap
* partitioning:
  * Available options:&#x20;
  * Guided Root-on-ZFS
  * Auto (UFS) UEFI Guided Disk Setup using UEFI boot method
  * Auto (UFS) BIOS Guided Disk Setup using BIOS boot method
  * Manual - Manual Disk Setup (experts)
  * Shell - Open a shell and partition by hand
  * Note: Options 1 and 2 both worked on bedrock
  * Choose entire disk or partition
  * Choose partition scheme
  * Review selections&#x20;
  * To finish, select finish
  * Commit to selections&#x20;
* Wait until the installation is complete&#x20;
* Select yes because we will need to make the following modifications to enable console:
  * Create the /boot/loader.conf.local file, which will contain our changes and add:
    * hw.uart.console="mm:0xfedc9000,rs:2"
    * console="efi"
    * Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.
  * If you also don’t want to see the boot log, also add:
    * boot\_mute="YES"
* When done type "exit" and reboot the system
