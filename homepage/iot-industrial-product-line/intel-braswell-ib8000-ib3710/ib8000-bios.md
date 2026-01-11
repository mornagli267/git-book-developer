# IB8000 BIOS

## AMI BIOS

AMI provides a number of support options for its BIOS products, both for its Developer Customers and End Users of AMI’s BIOS and UEFI firmware solutions.

## Shortcuts

Entering the BIOS is achieved by ESC or DEL

BOOT OVERRIDE MENU is via F7

## Issues

### Black Screen after Bios Logo:

_This is due to the default configuration. The BIOS currently has CSM enabled (which provides legacy boot options) and the video policy is set to UEFI (which runs the UEFI driver and not the legacy one). This means there will be no video available for legacy boot options. What is happening is the system runs out of UEFI bootable options, and falls through to the legacy boot options. Since there is no video driver for legacy, this is why you’re getting no video. If you’re only going to be booting UEFI boot devices, you can disable CSM in setup (Advanced > CSM Configuration). Then when the system runs out of boot options, it will just fall back into setup by default._

### Switch to “UEFI ONLY” Mode:

1. Press “F2” or “DEL” during after powering the device on.
2. Go to “Advanced” tab, choose “CSM Configuration”,
3. Change “Boot Option Filter” to “UEFI ONLY”.
4. Save and Reboot.

![](../../../.gitbook/assets/sr-bios-uefi-only-01.jpg)

![](../../../.gitbook/assets/sr-bios-uefi-only-02.jpg)

## Bios Upgrade

Either you use the Headers and a flashing device to upgrade the BIOS, the AMI Software tools or EFI Shell.

### Software

* AFU for DOS, Windows, and EFI Shell available freely on AMI website: [AMI Firmware Update Utility](https://ami.com/?Aptio_V_AMI_Firmware_Update_Utility.zip)
* [EFI Shell](https://developer.solid-run.com/knowledge-base/ibx-bios-ami-bios/?preview_id=1533\&preview_nonce=b0b91567d2\&preview=true#efi-shell)

Latest Bios-Versions:

| Name     | Version | Date       | Link                                                                                                                                                                                                                                            |
| -------- | ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IBx Bios | 0.381   | 2021-08-09 | [PRODUCTION\_TXE\_8MB\_BIOSv38-fixed-spd-2Gb-4Gb-dvfs-disbled-2n-rh-autodetected-disabled-rx-tx-power-disabled.bin](attachments/PRODUCTION_TXE_8MB_BIOSv38-fixed-spd-2Gb-4Gb-dvfs-disbled-2n-rh-autodetected-disabled-rx-tx-power-disabled.bin) |
| IBx Bios | 0.38    | 2018-06-28 | [sr-ibx-ami-bios-v38.zip](attachments/sr-ibx-ami-bios-v38.zip)                                                                                                                                                                                  |

### Hardware

![](../../../.gitbook/assets/sr-ibx-flash03.png)

For flashing the bios via the headers, you can tools like [DediProg SF600Plus](http://www.dediprog.com/pd/spi-flash-solution/sf600plus) and connect it to the Header of the SolidPC Carrierboard.

### Schematics

#### BIOS Flashing 8 pin 100mil header

* Notice that R7 must never be assembled since it shorts to V1P8A.
* It’s here only for debug purposes.
* Typically it is used to power the SPI flash on the uSOM when the rest of the uSOM is powered down; but in this case the uSOM must be powered on and the reset signal will hold it from using the SPI flash.

**Notice that the programmer must drive 1.8v signals; otherwise the main processor might get damaged**

![](../../../.gitbook/assets/sr-ibx-solidpc-bios-flashing-header.webp)

**D0 = MOSI**\
**D1 = MISO**

### Bios Chip

The Solid-Run Intel MicroSom got a **Macronix MX25U6435F** onboard.

MX25U6435F is 64Mb bits serial Flash memory, which is configured as 8,388,608 x 8 internally. When it is in two or four I/O mode, the structure becomes 33,554,432 bits x 2 or 16,777,216 bits x 4. MX25U6435F feature a serial peripheral interface and software protocol allowing operation on a simple 3-wire bus while it is in single I/O mode. The three bus signals are a clock input (SCLK), a serial data input (SI), and a serial data output (SO). Serial access to the device is enabled by CS# input.\
The MX25U6435F utilizes Macronix’s proprietary memory cell, which reliably stores memory contents even after 100,000 program and erase cycles.\
(source: macronix datasheet)\
The Datasheet of the Bios-chip can be found [**here**](https://developer.solid-run.com/wp-content/uploads/2018/10/mx25u6435f.pdf)**.**

### Bios Reset

Either you can short the RTC battery on the bottom side of the SolidPC carrierboard (disconnect the whole board from power before!) or remove the MicroSom for few minutes.

![](../../../.gitbook/assets/rtc-short.webp)

## EFI Shell

### Starting EFI Shell

The EFI Shell is not preinstalled on the bios chip.

![](../../../.gitbook/assets/sr-ibs-bios-efi-shell.webp)

o install it manually on a external drive(fat32), you can get the _Shell\_Full.efi_ from the tianocore github: [https://github.com/tianocore/edk2/blob/master/EdkShellBinPkg/FullShell/X64/Shell\_Full.efi](https://github.com/tianocore/edk2/blob/master/EdkShellBinPkg/FullShell/X64/Shell_Full.efi)

Just rename it to _BOOTx64.efi_ and put it in the _/EFI/BOOT_ folder on a USB flash drive\
(full path: _/EFI/BOOT/BOOTx64.EFI_).

Press F7 during boot and choose your external device as boot device – the Shell will automatically load.

### Flashing Bios EFI Shell

1. You need the additional AfuEfix64.efi file for flashing the latest bios.
2. Place this and the bios file (.bin or .rom) onto the same device like the uefi shell in the same folder like the AfuEfix64.efi.
3. After the efi shell boots up – it show all available devices (fs0, fs1 etc)
4. Search for your usb device and type ‘fs1:’ to switch into this device.
5. Now search for the AfueEfix64.efi and you bin file and type ‘AfuEfix64.efi YOURBIOSFILE.bin /p /b /n’
6. Wait until its done
7. Type ‘reset’ to reboot your computer

Already prepared zip file (EFI Shell and AfuEfix64) which just need to be extracted on a fat32 device can be found [here](https://developer.solid-run.com/wp-content/uploads/2018/10/sr-ibx-efishell-flashbios.zip)

### Automatically Power on

If you want that the Som powers automatically on when connected to the power adapter, please changes these settings:

Bios Menu→Chipset→South Bridge→Restore AC Power Loss

## Links

* [AMI Website](https://ami.com)
* [Macronix Website](http://www.macronix.com)
* [Dediprog Website](http://www.dediprog.com)
