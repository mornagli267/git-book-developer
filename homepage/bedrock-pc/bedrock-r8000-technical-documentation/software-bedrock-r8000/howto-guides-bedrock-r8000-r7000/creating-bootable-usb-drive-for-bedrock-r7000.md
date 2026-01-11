# Creating Bootable USB Drive for Bedrock R7000

* Download the required image

## Using dd (Linux)

* In terminal run:
  * lsblk to see all block devices, your USB drive will be /dev/sdX
  * sudo dd if=your\_image.iso of=/dev/sdX bs=1M status=progress; sync

***

## Using Rufus (Windows)

* [Download Rufus](https://github.com/pbatard/rufus/releases/download/v4.3/rufus-4.3.exe)
* Open rufus![](../../../../../.gitbook/assets/image-20231217-162242.png)
* Press on the select Button
* Navigate to the .iso file![](../../../../../.gitbook/assets/image-20231217-162419.png)
* Press start![](../../../../../.gitbook/assets/image-20231217-162444.png)
* Press ok to confirm the write method (may be different for you) usually no need to change it:![](../../../../../.gitbook/assets/image-20231217-162604.png)
* Confirm destructive action![](../../../../../.gitbook/assets/image-20231217-162648.png)
* Wait until it finished and you are good to go
