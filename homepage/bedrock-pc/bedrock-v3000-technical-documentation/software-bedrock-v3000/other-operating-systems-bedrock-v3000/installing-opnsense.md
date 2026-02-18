# Installing OPNsense

## Installing OPNsense

### Test setup

The installation was validated at SolidRun using the following setup:

* OPNSENSE 23.7
* Terminal software:
  * Putty
  * Alternatively, Tio can also be used.\
    **known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
* USB flash disk: Kingston Data Traveler

## Installation process

### Creating bootable USB drive

Please follow instructions at [Creating bootable USB drive](/homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/creating-bootable-usb-drive-for-bedrock-v3000.md)

### Connecting serial console

Please follow instructions at [Using serial console with Bedrock V3000](/homepage/bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/using-serial-console-with-bedrock.md)

### BIOS settings

* Insert the USB media to the device
* Turn on Bedrock
* Repetitively press the DEL / ESC key to enter the BIOS setup
* In BIOS go to -> Save & Exit -> -> yes
* Device will reset and a PFsense boot screen will appear

### After boot

* When you see the main boot menu:![](<../../../../../.gitbook/assets/GetImage (12).png>)
* Press "esc" or the arrow buttons to go to the boot option shell&#x20;
* Set the console redirection (copy to the terminal):&#x20;
  * `set hw.uart.console="mm:0xfedc9000,rs:2"`
    * NOTE: the line you paste might look a little weird especially if you type it manually \
      example for copy: /K |et hw.uart.console="mm:0xfedc9000,rs:2" \
      example for manual typing: \e|/-\\|/r-\co|sol/-\\|m:/x-ed\9|0/-\\|:/" \
      **THIS IS FINE AS LONG AS THE ACTUAL INPUT TEXT IS CORRECT**&#x20;
  * Type `boot`&#x20;
* After the system has booted you are prompted with a login&#x20;
  * To use it as a live system you can login as:&#x20;
    * Username: root&#x20;
    * Password: opnsense&#x20;
  * To install OPNsense login as:&#x20;
    * Username: installer&#x20;
    * Password: opnsense&#x20;
    * From here on, I will reffer to the installer option:&#x20;
* Choose keymap![](<../../../../../.gitbook/assets/GetImage (13).png>)
* Choose Partition scheme to be installed\
  Select UFS GPT/UEFI Hybrid![](<../../../../../.gitbook/assets/GetImage (14).png>)
* Choose disk![](<../../../../../.gitbook/assets/GetImage (15).png>)
* Decide about swap partition ![](<../../../../../.gitbook/assets/GetImage (16).png>)
* Confirm disk wipe ![](<../../../../../.gitbook/assets/GetImage (17).png>)
* Wait untill installation is complete ![](<../../../../../.gitbook/assets/GetImage (18).png>)

### After installation

* You will be prompted to change the root users password, change it
* Log in to the root user login and go into a shell
* Create a /boot/loader.conf.local file which will contain our pernmanent console enable, and add:&#x20;
  * hw.uart.console="mm:0xfedc9000,rs:2"&#x20;
  * console="efi"&#x20;
  * Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.
