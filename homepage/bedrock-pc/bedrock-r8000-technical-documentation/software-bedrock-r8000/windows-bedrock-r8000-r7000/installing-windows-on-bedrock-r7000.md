# Installing Windows on Bedrock R7000

SolidRun recommends Windows 11 for Bedrock.

Windows 10 is also supported.

<a id="preparing-installation-media"></a>

## Preparing Installation Media

- Download the [windows 11 media creation tool](https://www.microsoft.com/software-download/windows11)
- Insert an 8GB+ USB stick to your system
- Launch windows media creation tool
- Accept licence agreement:![](./attachments/image-20231017-054031.png)
- Select edition and language:![](./attachments/image-20231017-054118.png)
- Select USB flash drive:![](./attachments/image-20231017-054207.png)
- Select your USB drive:![](./attachments/image-20231017-054335.png)
- Wait for the process to finish, this might take a while depending on your USB drives speed.
- When process is finished, you will see the following screen![](./attachments/image-20231017-061719.png)
  

<a id="windows-pe-environment"></a>

## Windows PE Environment

- Boot into BIOS (insert power supply or reboot and press ‘DEL’ repetitively to enter the BIOS setup menu).

> [!INFO]
> If you have problems with installation, please disable secure boot in BIOS → boot> security → secure boot-> disable

- In BIOS boot from the USB flash drive from the save & exit menu
- When Windows installer boots select language and keyboard layout![](./attachments/image-20231017-055056.png)
- Click on install now![](./attachments/image-20231017-055128.png)
- If you have a product key type it and click next, if you dont click I don’t have a product key (you will be able to [activate later](../windows-bedrock-r8000-r7000/windows-activation.md))![](./attachments/image-20231017-055320.png)
- Select which windows you want to install (your list can be different)![](./attachments/image-20231017-055503.png)
- Accept licence agreement![](./attachments/image-20231017-055756.png)
- Choose custom installation![](./attachments/image-20231017-055930.png)
- In this case there is only one drive, and its not empty.  
![](./attachments/image-20231017-060121.png)
  - We need to clean it before we can install windows on it, we can see all 4 partitions belong to the same drive. (drive 0)
  - For each partition, click on it, and click on delete, to free the space of this partition after which, this partition will be displayed as Unallocated space.
  - In the end you want something like this:![](./attachments/image-20231017-060310.png)

> [!CAUTION]
> If you have multiple drives, make sure you select and clean the correct one, cleaning the wrong drive will probably lead to data loss.

- Click next![](./attachments/image-20231017-060648.png)
- Wait for the installation process to finish![](./attachments/image-20231017-060801.png)
- System will reboot

<a id="windows-configuration"></a>

## Windows Configuration

- Once you boot into this screen you can disconnect your flash drive, select your region and press next![](./attachments/image-20231017-061014.png)
- Select keyboard layout![](./attachments/image-20231017-061124.png)
- If you want to add another keyboard layout, press Add leyout, otherwise click Skip![](./attachments/image-20231017-061240.png)
- If you're connected to the internert, windows will check for updates  
![](./attachments/image-20231017-061532.png)

> [!NOTE]
> Intels i226-IT drivers are not installed by default so you will have to use wifi or a USB → ethernet adapter to be able to update at this point.

- Name your device or skip this step![](./attachments/image-20231017-061610.png)
  
- Select the usage of this device![](./attachments/image-20231017-061649.png)
- Now you will need to sign in to your Microsoft account![](./attachments/image-20231017-061813.png)

> [!INFO]
> If you dont want to Sign in, you can choose Sign in options → Offline account

- If you skipped Microsoft will explain what is a Microsoft account, you can just skip it![](./attachments/image-20231017-062135.png)
- Set up the users name and press Next![](./attachments/image-20231017-062208.png)
- Choose password, if you dont want a password, just leave empty and press Next![](./attachments/image-20231017-062316.png)
- Choose privacy settings for your device![](./attachments/image-20231017-062353.png)

> [!INFO]
> We recommend turning everything OFF for minimal collection of your data

- Wait while Windows gets things ready for you.