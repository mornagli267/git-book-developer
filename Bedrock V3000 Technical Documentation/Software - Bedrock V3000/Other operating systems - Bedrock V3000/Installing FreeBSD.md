
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Other operating systems - Bedrock V3000](../Other%20operating%20systems%20-%20Bedrock%20V3000.md)

# Installing FreeBSD

## Test setup

The installation was validated at SolidRun using the following setup:

- Freebsd 13.2-RELEASE
- Terminal software:

  - Putty
  - Alternatively, Tio can also be used.  
    **known TIO limitation**: in BIOS, the currently selected option is displayed in the same color as the background, which makes it not visible, yet it is still fully functional.
- USB flash disk: Kingston Data Traveler

# Installation process

## Download FreeBSD Image

- Go to: [FreeBDS AMD64 installer download](https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/13.2/FreeBSD-13.2-RELEASE-amd64-disc1.iso)

## Creating bootable USB drive

Please follow instructions at [Creating bootable USB drive](https://solidrun.atlassian.net/l/cp/m9Reo11r)

## Connecting serial console

Please follow instructions at [Using serial console with Bedrock](../Using%20serial%20console%20with%20Bedrock.md)

## BIOS settings

- Insert the USB media to the device
- Turn on Bedrock
- Repetitively press the DEL / ESC key to enter the BIOS setup
- In BIOS go to -> Save & Exit -> <your bootable USB device> -> yes
- Device will reset and a PFsense boot screen will appear

## Boot

When you see the main boot menu:

![](../../../../../attachments/736beb1f-9ef6-4914-966e-6f731408dc12.png)

- Press "esc" or the arrow buttons to go to the boot option shell
- Set the console redirection (copy to the terminal):
- ```java
  set hw.uart.console="mm:0xfedc9000,rs:2"
  boot
  ```
- Kernel messages will start to spill out, wait until you see the following prompt:
- Select console type, press enter for default(VT100):

![](../../../../../attachments/81cf9d1d-a78b-46d6-8f4a-39b7f17913e1.png)

- Choose install:

![](../../../../../attachments/022b57c9-a515-4ab7-958c-a98d7c3bc729.png)

- Choose keymap:

![](../../../../../attachments/b975ec58-fe25-411e-a390-c1b5924a9d8a.png)

- Choose host name for your device:

![](../../../../../attachments/433a3f7b-cb33-43f9-adc3-792b07ac583d.png)

- Choose system components, press enter for default:

![](../../../../../attachments/d32b78af-d65b-49ff-b3c5-22f23463776a.png)

- Select Auto (UFS) Guided UFS Disk Setup:

![](../../../../../attachments/2d928a3f-cf0a-488c-ae78-3e4cca5178a5.png)

- Select installation disk:

![](../../../../../attachments/8ea6f195-07d1-4aed-aee0-e2c0c25b9647.png)

- Select Entire disk:

![](../../../../../attachments/bdc3ff47-1ba5-4643-bc9b-92f3b929f497.png)

- Confirm destructive action:

![](../../../../../attachments/c4631b8b-83e8-49e0-bded-1586641cd582.png)

- Select partition scheme:

![](../../../../../attachments/4cdc76be-260a-4f0a-9b69-1f2cf7128fb0.png)

- Review disk setup and select Finish:

![](../../../../../attachments/67ce1c9d-3283-4a4d-8270-d9222d0c6176.png)

- Confirm destructive action:

![](../../../../../attachments/4b18b7db-c292-44fd-a975-4949ebbbee6e.png)

- Wait for the installation to finish:

![](../../../../../attachments/bed1d93c-f183-4da2-bf97-23a5309e2994.png)![](../../../../../attachments/47421bb4-9667-4899-aa10-c4857c75c860.png)

- Select password:

![](../../../../../attachments/4e71c7e3-7ed2-4e8f-92c9-f748cc1531e4.png)

- Select network interface to configure:

![](../../../../../attachments/abbfe393-654d-4b77-ba74-ebfd684db168.png)

- Follow the istructions to configure the interface.

- Configure resolver, enter for default:

![](../../../../../attachments/5c923976-b93b-408d-91d2-9b26a74f88b2.png)

- Select local time and time zone, select no:

![](../../../../../attachments/ffd42d2a-caba-40a4-871e-ac9be2389708.png)![](../../../../../attachments/25767bd8-1908-41bc-be60-57bb9d7cc731.png)![](../../../../../attachments/4cafb18b-78a5-4791-a63f-ee287a138749.png)![](../../../../../attachments/a5c6a98f-092b-4126-a3fa-50088be3615d.png)

- Configure your system:

![](../../../../../attachments/451a0c45-603f-42dd-9b4f-8874a6b125ff.png)

- Configure system hardening:

![](../../../../../attachments/acd95e00-b8ae-4d8c-9f39-c84643873641.png)

- Add users if needed:  
  Follow the istructions to add a new user

![](../../../../../attachments/b1552ddc-540e-4a3e-928c-082592d054c5.png)

- Apply the configurations and exit the isntaller:

![](../../../../../attachments/60dab7d5-d4f4-49a4-8c32-01e0897e01ea.png)

- Open shell to further configure the system:

![](../../../../../attachments/d958ee2c-a344-4199-8130-5feaac761808.png)

- Select yes because we will need to make the following modifications to enable console:

  - Create the `/boot/loader.conf.local` file, which will contain our changes and add:
  - ```java
    hw.uart.console="mm:0xfedc9000,rs:2" 
    ```

> [!WARNING]
> Note: /boot/loader.conf recreates itself each boot or update, so this will override the changes.

#### Thats it, you can reboot the system and use it.

## Tips

#### Hididng kernel output

- Add to /boot/loader.conf.local:

  - ```java
    boot_mute="YES"
    ```

#### **Disabling Hyperthreading**

- Add to /boot/loader.conf.local:

  - ```java
    machdep.hyperthreading_allowed="0"
    ```
- To verify the change run:

  - ```java
    sysctl machdep.hyperthreading_allowed
    ```
