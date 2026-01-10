---
tags:
  - '#bedrock-r8000'
  - '#howto'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [HowTo Guides - Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000.md)

# Running Memtest86

To run Memtest86 you will first need to create a USB bootable drive.  
You can do that with tools like:

- Rufus on windows
- dd on Linux: `dd if=memtest86-usb.img of=/dev/<sda, sdb, sdc> bs=1M status=progress; sync`

  - Note sda, sdb … is the enumeration by your linux system, you can check it with `lsblk`

Plug the USB drive with Memtest86 to your Bedrock device and power it on.  
Wait for the system to boot to Memtest86 or select its boot option from BIOS.

Once booted, select the default scan (option 1):

![image-20250124-083135.png](../../../../../attachments/c034e80a-cb7b-4198-a6ef-98ae30617ffc.png)

Wait for Memtest86 to finish the test (this will take time) and see results.
