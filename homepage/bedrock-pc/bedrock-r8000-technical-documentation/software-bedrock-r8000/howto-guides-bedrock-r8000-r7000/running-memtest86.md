# Running Memtest86

To run Memtest86 you will first need to create a USB bootable drive.\
You can do that with tools like:

* Rufus on windows
* dd on Linux: `dd if=memtest86-usb.img of=/dev/<sda, sdb, sdc> bs=1M status=progress; sync`
  * Note sda, sdb … is the enumeration by your linux system, you can check it with `lsblk`

Plug the USB drive with Memtest86 to your Bedrock device and power it on.\
Wait for the system to boot to Memtest86 or select its boot option from BIOS.

Once booted, select the default scan (option 1):

![image-20250124-083135.png](../../../../../.gitbook/assets/image-20250124-083135.png)

Wait for Memtest86 to finish the test (this will take time) and see results.
