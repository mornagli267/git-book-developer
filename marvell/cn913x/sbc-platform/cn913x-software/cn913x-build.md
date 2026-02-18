# CN913x Build

### Introduction

The main intention of this manual is to provide build scripts that are easy to handle compared to Marvell's build environment and self build for CN913x based products.

```
git clone https://github.com/SolidRun/cn913x_build.git
```

The sources are pulled from:

1. arm-trusted firmware: [GitHub - ARM-software/arm-trusted-firmware](https://github.com/ARM-software/arm-trusted-firmware.git)
2. mv-ddr-marvell: [GitHub - MarvellEmbeddedProcessors/mv-ddr-marvell](https://github.com/MarvellEmbeddedProcessors/mv-ddr-marvell.git)
3. u-boot: currently from marvell SDK
4. linux: [GitHub - torvalds/linux: Linux kernel source tree](https://github.com/torvalds/linux.git)
5. patches are supplied by Solid-Run in the patches/ directory
6. binaries are supplied by Solid-Run in the binaries/ directory\
   The build script builds the u-boot, atf and linux components, integrate it with Ubuntu rootfs bootstrapped with multistrap. Buildroot is also built aside for future use.

### U-Boot based on SDK10

The CN913x u-boot is not public yet, and was taken from Marvell's SDK10

In order to use the script with the SDK's 1186 patches, create a directory in ROOTDIR:

```
mkdir $ROOTDIR/patches-sdk-u-boot/
```

Extract the git-u-boot--.tar.bz2 under the destination folder git-u-boot-- and copy the patches

```
cp <sdk patch directory>/Base_SDK/base-patches-SDK-10.3.3.0-PR8/uboot/git-uboot-2019.10-SDK-10.3.3.0-PR8/*.patch patches-sdk-u-boot/ $ROOTDIR/patches-sdk-u-boot/The script will apply the u-boot patches onto the mainline u-boot.
```

If the SDK patches directory doesn't exist, the script will take by default the u-boot.bin provided in the binaries directory.

#### Run Script

The board can be configured based on the amount of CP# devices and to which carrier board it will fit. There are a few parameters that must be taken to account:

1. CP\_NUM:
2. CP\_NUM=1 - CN9130
3. CP\_NUM=2 - CN9131
4. CP\_NUM=3 - CN9132
5. BOARD\_CONFIG - defines the device tree based on the platform
6. BOARD\_CONFIG=0 - CN9132 CEx7 based on Clearfog Eval Board
7. BOARD\_CONFIG=1 - CN9130 SOM based on Clearfog Base
8. BOARD\_CONFIG=2 - CN9130 SOM based on Clearfog Pro
9. BOARD\_CONFIG=3 - CN9131 based on SolidWan

Note: when defining the BOARD\_CONFIG, the runme.sh script defines correct CP\_NUM related to the platform.

```
BOARD_CONFIG=<#> ./runme
```

The script will generate a ready to use images at ROOTDIR/images:

1. flash\_image.bin for SPI
2. \*.img for eMMC or SD card

#### Boot Select

Before powering up the board  for the first time it is recommended to select the boot media. In order to configure the boot media:

1\. CN9130 SOM base on ClearFog Base / Pro:

|                  | SW1 #1 | SW1 #2 | SW1 #3 | SW1 #4 | SW1 #5 |
| ---------------- | ------ | ------ | ------ | ------ | ------ |
| SPI              | ON     | X      | OFF    | ON     | X      |
| SD               | OFF    | X      | ON     | OFF    | X      |
| eMMC             | OFF    | X      | OFF    | ON     | X      |
| 2.2GHz Core Freq | X      | OFF    | X      | X      | X      |
| 2GHz Core Freq   | X      | ON     | X      | X      | X      |

In Clearfog Pro , the frequency can be reduced to 1.6GHz using SW2

|        | SW1 #2 | SW2 #5 |
| ------ | ------ | ------ |
| 1.6GHz | OFF    | ON     |

2\. CN9132 COM Express Type 7

| BOOT MODE | SW1 #1 | SW1 #2 | SW1 #3 | SW1 #4 | SW1 #5 | SW1 #6 |
| --------- | ------ | ------ | ------ | ------ | ------ | ------ |
| SPI       | OFF    | ON     | ON     | OFF    | ON     | X      |
| SD        | ON     | OFF    | ON     | ON     | OFF    | X      |
| eMMC      | ON     | OFF    | ON     | OFF    | ON     | X      |

| Frequency | SW2 #1 | SW2 #1 |
| --------- | ------ | ------ |
| 2.2GHz    | ON     | OFF    |
| 2GHz      | OFF    | OFF    |
| 1.6GHz    | OFF    | ON     |

3\. CN913x other Platforms (SolidWan and custom platforms)

| BOOT MODE        | SW1 #1 | SW1 #2 | SW1 #3 | SW1 #4 | SW1 #5 | SW1 #6 |
| ---------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| SPI              | ON     | OFF    | ON     | X      | X      | X      |
| SD               | OFF    | ON     | OFF    | X      | X      | X      |
| eMMC             | ON     | OFF    | OFF    | X      | X      | X      |
| 2.2GHz Core Freq | X      | X      | X      | OFF    | ON     | OFF    |
| 2GHz Core Freq   | X      | X      | X      | OFF    | OFF    | OFF    |
| 1.6GHz           | X      | X      | X      | OFF    | OFF    | ON     |

#### DDR Configuration and EEPROM

The atf dram\_port.c supports both CN9132 CEx7 SO-DIMM with SPD and CN9130 SOM with DDRs soldered on board which might have various configurations and are set according to boot straps MPPs\[11:10]. In order to differentiate, it checks the first 196 Bytes of the EEPROM. If programming data on the EEPROM (address 0x53) is requiered, and is not related to the DDR configuration, it must be after the first 196 Bytes. Otherwise, the boot sequence will be corrupted.

#### Burning on SD Card

For SD card bootable images:\
Plug in a micro SD into your machine and run the following, where sdX is the location of the SD card got probed into your machine -

```
sudo dd if=$ROOTDIR/images/<image name>.img of=/dev/sdX status=progress; sync
```

for burning u-boot image only:&#x20;

```
sudo dd if=$ROOTDIR/images/flash-image.bin of=/dev/sdX bs=512 seek=4096 status=progress; sync
```

#### Deploy

Distro boot checks if the SOM’s EEPROM is configured and searches for the SKU. Based on the relevant SKU, it takes the relevant DTB for the platform.

For EEPROM configuration, refer to: [https://github.com/SolidRun/Documentation/blob/bsp/cn913x/tlv-eeprom.md](https://github.com/SolidRun/Documentation/blob/bsp/cn913x/tlv-eeprom.md)

Defalt DTB is based on Clearfog-Pro platfrom

In case EEPROM is not burnt, to continue booting, set environment in u-boot prompt:

```
setenv fdtfile marvell/<dtb file name>.dtb
saveenv
boot
```
