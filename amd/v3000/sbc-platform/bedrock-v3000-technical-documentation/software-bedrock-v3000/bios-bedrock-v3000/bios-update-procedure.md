# BIOS Update procedure

## Download utility

Download the [AFU Utility from AMI](https://www.ami.com/bios-uefi-utilities/)'s website, select APTIO V AMI FIRMWARE UPDATE UTILITY

## Option 1: Update from windows GUI (easiest)

* In AMI utilities directory go to:
  * afu\afuwin\64\\
  * Unzip the afuwin64.zip file and enter the extracted directory
* Run AFUWINGUIx64.exe
* Press Open and navigate to the BIOS\_image\_file
* Go to the setup tab and set the following options:
  * program all blocks
  * restart after programming
* Press Flash
* System will reboot and the new BIOS will be installed

{% hint style="warning" %}
Do not power off or unplug your device during the update process, doing so may result in bricking and RMA.
{% endhint %}


* After the update is finished, press any key to reboot the system
* After the update, the device can reset upt to 3 times, this is OK.

## Option 2: Update from windows cmd

* In AMI utilities directory go to:
  * afu\afuwin\64\\
  * Unzip the afuwin64.zip file and enter the extracted directory
* Open cmd and navigate to the directory where you extracted afuwin
* Run:
  * AFUWINx64 \<YOUR\_BIOS\_IMAGE> /P /B /K /N /L /REBOOT
    * It is recommended to paste the BIOS image in the same directory
* System will reboot and the new BIOS will be installed

{% hint style="info" %}
If you get: …\
…\
Erasing Main Block ………………………………………. 0x01000000 (0%)\
43 - Error: Problem erasing flash. Add the **/CAPSULE** parameter to the command
{% endhint %}


{% hint style="warning" %}
Do not power off or unplug your device during the update process, doing so may result in bricking and RMA.
{% endhint %}


* When disconnecting power from the device for the firtst time after update, you might need to press the power button in order to turn on the device.
* After the update, the device can reset upt to 3 times, this is OK.

## Option 3: USB Drive using UEFI (advanced)

* Copy the files to the USB Drive you created in the [Create EFI shell bootable USB drive](how-to-create-an-efi-shell-bootable-usb-drive.md) section
* Boot Bedrock to EFI shell&#x20;
* Identify your drive as FS#: (where # could be 1,2,3,…..)
* Select the correct drive using:&#x20;
  * FS#:&#x20;
* You can navigate to your files using: 'dir' and 'cd'  (if you chose to place in a different directory)
* Run:
  * AfuEfix64.efi \<YOUR\_BIOS\_IMAGE> /P /B /K /N /L /REBOOT
* System will reboot and the new BIOS will be installed

{% hint style="info" %}
If you get: …\
…\
Erasing Main Block ………………………………………. 0x01000000 (0%)\
43 - Error: Problem erasing flash. Add the **/CAPSULE** parameter to the command
{% endhint %}


{% hint style="warning" %}
Do not power off or unplug your device during the update process, doing so may result in bricking and RMA.
{% endhint %}


* When disconnecting power from the device for the firtst time after update, you might need to press the power button in order to turn on the device.
* After the update, the device can reset upt to 3 times, this is OK.
