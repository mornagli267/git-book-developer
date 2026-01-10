---
tags:
  - '#amd-os'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [Windows - Bedrock R8000 | R7000](../Windows%20-%20Bedrock%20R8000%20_%20R7000.md)

# Installing Windows on Bedrock R7000

SolidRun recommends Windows 11 for Bedrock.

Windows 10 is also supported.

## Preparing Installation Media

- Download the [windows 11 media creation tool](https://www.microsoft.com/software-download/windows11)
- Insert an 8GB+ USB stick to your system
- Launch windows media creation tool
- Accept licence agreement:

  ![](../../../../../attachments/50ce188a-4ba2-4302-a92d-6746dc52278e.png)
- Select edition and language:

  ![](../../../../../attachments/8e4e71b5-4eed-4f3e-8eef-65f8087a4b2a.png)
- Select USB flash drive:

  ![](../../../../../attachments/1c203513-8c5c-4a62-9a85-877f114313fd.png)
- Select your USB drive:

  ![](../../../../../attachments/10269046-5068-4889-ac0b-c5b80bd0ccaf.png)
- Wait for the process to finish, this might take a while depending on your USB drives speed.
- When process is finished, you will see the following screen

  ![](../../../../../attachments/9545d35c-1077-4ce1-bcf3-20ac08c72508.png)

## Windows PE Environment

- Boot into BIOS (insert power supply or reboot and press ‘DEL’ repetitively to enter the BIOS setup menu).

> [!IMPORTANT]
> If you have problems with installation, please disable secure boot in BIOS → boot> security → secure boot-> disable

- In BIOS boot from the USB flash drive from the save & exit menu
- When Windows installer boots select language and keyboard layout

  ![](../../../../../attachments/e7be9bf3-2fa6-4fa3-bcff-fc0026679f96.png)
- Click on install now

  ![](../../../../../attachments/1839ce3f-b71a-4e87-8bce-015f83ecf27c.png)
- If you have a product key type it and click next, if you dont click I don’t have a product key (you will be able to [Windows Activation](Windows%20Activation.md))

  ![](../../../../../attachments/7d6c0f9e-64a2-4436-a50f-7406c8523b4c.png)
- Select which windows you want to install (your list can be different)

  ![](../../../../../attachments/d5704cb8-8b71-4a18-976c-73da98230665.png)
- Accept licence agreement

  ![](../../../../../attachments/dc5d8fe0-47ae-4a94-9a80-8e4e27742c06.png)
- Choose custom installation

  ![](../../../../../attachments/9bcf38e1-a8eb-4a3c-bbc1-2cbd1122d202.png)
- In this case there is only one drive, and its not empty.

  ![](../../../../../attachments/44fd8902-3083-47d9-b75a-ea3168a7ebec.png)
  - We need to clean it before we can install windows on it, we can see all 4 partitions belong to the same drive. (drive 0)
  - For each partition, click on it, and click on delete, to free the space of this partition after which, this partition will be displayed as Unallocated space.
  - In the end you want something like this:

    ![](../../../../../attachments/349bd2e0-be7b-4b3d-8f34-7160742d0dbe.png)

> [!CAUTION]
> If you have multiple drives, make sure you select and clean the correct one, cleaning the wrong drive will probably lead to data loss.

- Click next

  ![](../../../../../attachments/71c3f378-a155-4e48-bdc8-d98c461a2495.png)
- Wait for the installation process to finish

  ![](../../../../../attachments/76a1f5d4-27b4-442a-aed0-666155190bb6.png)
- System will reboot

## Windows Configuration

- Once you boot into this screen you can disconnect your flash drive, select your region and press next

  ![](../../../../../attachments/f2fa1d14-48b8-4bd6-bd04-7d45b6bcf7d4.png)
- Select keyboard layout

  ![](../../../../../attachments/bd2a070f-cac3-4457-8406-54f5f4ffd037.png)
- If you want to add another keyboard layout, press Add leyout, otherwise click Skip

  ![](../../../../../attachments/8fa63fd6-eb9d-4318-af5c-6675f5b265e9.png)
- If you're connected to the internert, windows will check for updates

  ![](../../../../../attachments/8cb024d5-9f6d-447a-b278-86e720eec70a.png)

> [!NOTE]
> Intels i226-IT drivers are not installed by default so you will have to use wifi or a USB → ethernet adapter to be able to update at this point.

- Name your device or skip this step

  ![](../../../../../attachments/8cb0284e-acc9-4f1e-9df3-79ce1e5c110b.png)
- Select the usage of this device

  ![](../../../../../attachments/b6d2e749-32d0-491c-98f4-baf91ec70225.png)
- Now you will need to sign in to your Microsoft account

  ![](../../../../../attachments/18a5d008-d363-4057-a793-fbb1d7857b82.png)

> [!IMPORTANT]
> If you dont want to Sign in, you can choose Sign in options → Offline account

- If you skipped Microsoft will explain what is a Microsoft account, you can just skip it

  ![](../../../../../attachments/6d0ce2dc-c14f-4480-a60b-b83ecf14e093.png)
- Set up the users name and press Next

  ![](../../../../../attachments/64314790-d017-45ea-bd57-899613d8f968.png)
- Choose password, if you dont want a password, just leave empty and press Next

  ![](../../../../../attachments/6450043b-0e08-4d83-9356-e29c16184f51.png)
- Choose privacy settings for your device

  ![](../../../../../attachments/88cb9a3e-f5de-47be-beec-f4ae6f540354.png)

> [!IMPORTANT]
> We recommend turning everything OFF for minimal collection of your data

- Wait while Windows gets things ready for you.
