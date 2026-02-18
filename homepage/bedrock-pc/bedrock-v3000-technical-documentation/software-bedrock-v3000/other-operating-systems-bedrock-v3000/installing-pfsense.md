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

Please follow instructions at [/homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/creating-bootable-usb-drive-for-bedrock-v3000.md](/homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/creating-bootable-usb-drive-for-bedrock-v3000.md)

### Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](../using-serial-console-with-bedrock.md)

### BIOS settings

* Insert the USB media to the device
* Turn on Bedrock
* Repetitively press the DEL / ESC key to enter the BIOS setup
* In BIOS go to -> Save & Exit -> -> yes
* Device will reset and a PFsense boot screen will appear

### After boot

* When you see the main boot menu:&#x20;

![](<../../../../../.gitbook/assets/GetImage (2).png>)

* Press "esc" or the arrow buttons to go to the boot option shell&#x20;
* Set the console redirection (copy to the terminal):&#x20;
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
  * NOTE: (it’s the default option so you can just press enter)&#x20;
* Accept copyright and distribution notice ![](<../../../../../.gitbook/assets/GetImage (3).png>)
* Choose Install pfSense![](<../../../../../.gitbook/assets/GetImage (4).png>)
* Select keymap![](<../../../../../.gitbook/assets/GetImage (5).png>)
* partitioning:&#x20;
  * Available options: ![](<../../../../../.gitbook/assets/GetImage (6).png>)
  * Guided Root-on-ZFS&#x20;
  * Auto (UFS) UEFI  Guided Disk Setup using UEFI boot method&#x20;
  * Auto (UFS) BIOS  Guided Disk Setup using BIOS boot method&#x20;
  * Manual - Manual Disk Setup (experts)&#x20;
  * Shell - Open a shell and partition by hand&#x20;
  * Note: Options 1 and 2 both worked on bedrock&#x20;
  * Choose entire disk or partition&#x20;
  * Choose partition scheme&#x20;
  * Review selections ![](<../../../../../.gitbook/assets/GetImage (7).png>)
  * To finish, select finish&#x20;
  * Commit to selections ![](<../../../../../.gitbook/assets/GetImage (8).png>)
* Wait until the installation is complete ![](<../../../../../.gitbook/assets/GetImage (10).png>)
* Select yes because we will need to make the following modifications to enable console:&#x20;
  * Create the /boot/loader.conf.local file, which will contain our changes and add:&#x20;
    * hw.uart.console="mm:0xfedc9000,rs:2"&#x20;
    * console="efi"&#x20;
    * Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.&#x20;
  * If you also don’t want to see the boot log, also add:&#x20;
    * boot\_mute="YES" &#x20;
* When done type "exit" and reboot the system

![](<../../../../../.gitbook/assets/GetImage (11).png>)
