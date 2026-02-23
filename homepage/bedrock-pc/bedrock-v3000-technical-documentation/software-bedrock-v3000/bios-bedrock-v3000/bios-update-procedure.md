# BIOS Update procedure

## Download utility

Download the [AFU Utility from AMI](https://www.ami.com/bios-uefi-utilities/)'s website, select APTIO V AMI FIRMWARE UPDATE UTILITY

## Option 1: Update From BIOS Setup (easy)

Newer BIOS images support updating the BIOS from the BIOS Setup utility to do so, follow the next steps:

* Put the BIOS file you want to update to on a USB stick and insert in to one of the USB ports on the device.
* Connect power to the device then press (DEL / ESC) continuously until BIOS screen shows up.
* In BIOS menu go to the Firmware update screen:

<figure><img src="../../../../../.gitbook/assets/image (1).png" alt="" width="563"><figcaption></figcaption></figure>

* Select your USB stick that has the BIOS Image file:

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="563"><figcaption></figcaption></figure>

* Select the BIOSimage file you want to update to:

<figure><img src="../../../../../.gitbook/assets/image (4).png" alt="" width="563"><figcaption></figcaption></figure>

* BIOS Image will be loaded
* Select: "Update image"

<figure><img src="../../../../../.gitbook/assets/image (6).png" alt="" width="563"><figcaption></figcaption></figure>

* Wait for the BIOS to finish updating



## Option 2: Update from windows GUI (easy)

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

## Option 3: Update from windows cmd

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

## Option 4: USB Drive using UEFI (advanced)

* Copy the files to the USB Drive you created in the [Create EFI shell bootable USB drive](how-to-create-an-efi-shell-bootable-usb-drive.md) section
* Boot Bedrock to EFI shell
* Identify your drive as FS#: (where # could be 1,2,3,…..)
* Select the correct drive using:
  * FS#:
* You can navigate to your files using: 'dir' and 'cd' (if you chose to place in a different directory)
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
