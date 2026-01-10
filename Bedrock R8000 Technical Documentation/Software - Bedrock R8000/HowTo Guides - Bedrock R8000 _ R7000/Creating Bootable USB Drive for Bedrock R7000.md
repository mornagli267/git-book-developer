---
tags:
  - '#windows'
  - '#howto'
  - '#linux'
  - '#bedrock-r8000'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [HowTo Guides - Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000.md)

# Creating Bootable USB Drive for Bedrock R7000

- Download the required image

## Using dd (Linux)

- In terminal run:

  - lsblk to see all block devices, your USB drive will be /dev/sdX
  - sudo dd if=your\_image.iso of=/dev/sdX bs=1M status=progress; sync

---

## Using Rufus (Windows)

- [Download Rufus](https://github.com/pbatard/rufus/releases/download/v4.3/rufus-4.3.exe)
- Open rufus

  ![](../../../../../attachments/4a023149-25d1-435e-af92-016b1a912fdd.png)
- Press on the select Button
- Navigate to the .iso file

  ![](../../../../../attachments/03cbe2a8-bcc0-41d9-b6ac-04238ea4673c.png)
- Press start

  ![](../../../../../attachments/4bda1c72-0d4a-436e-99b9-a99b8e09dc2b.png)
- Press ok to confirm the write method (may be different for you) usually no need to change it:

  ![](../../../../../attachments/657f4fc0-4043-4a76-99fa-f19562c5f0de.png)
- Confirm destructive action

  ![](../../../../../attachments/7fae4d8b-c090-4ffd-92f2-791317fac17c.png)
- Wait until it finished and you are good to go
