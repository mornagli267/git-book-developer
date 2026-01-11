# HummingBoard RZ family Boot options

<a id="introduction"></a>

# Introduction

The following guide will provide different [HummingBoard RZ](https://www.solid-run.com/embedded-industrial-iot/renesas-rz-family/rz-g2lc-som#carrier-boards) family boot options.

- [Introduction](#introduction)
- [Boot from SD card](#boot-from-sd-card)
- [Boot from USB](#boot-from-usb)
- [Boot using TFTP](#boot-using-tftp)
- [Flashing bootloaders and rootfs from Linux](#flashing-bootloaders-and-rootfs-from-linux)
- [Flashing bootloaders over serial](#flashing-bootloaders-over-serial)
- [Pre-programmed SOMs](#pre-programmed-soms)

This guide uses build artifacts from the [SolidRun BSP repository](https://github.com/SolidRun/build_rzg2lc). You need to clone this repo and [build the artifacts](https://github.com/SolidRun/build_rzg2lc#build-with-docker) first.

The RZ HummingBoards have two basic boot modes: SD boot and eMMC boot. The boot process starts with loading the bootloaders to the memory from the SD or eMMC. This article will explain how to boot HummingBoard in different modes and flash bootloaders to the eMMC.

This guide compatible with all the RZ family. For using with a specific device you need to change the path of the image to the correct one (replace all the xxxx).

<a id="boot-from-sd-card"></a>

# Boot from SD card

- Prepare the SD card. Connect the SD card to your PC and flash the image on it.

```
$ sudo dd if=images/rzxxxx_solidrun_buildroot-sd-xxxxxxx.img of=/dev/sdX bs=1M
```

> [!INFO]
> Note: xxxxxxx in the file name is the software revision number that changes over time.

> [!INFO]
> Note: the SD card is assumed to be connected to /dev/sdX device and unmounted. Don’t forget to change X to the actual device letter.

- Set the [S3 DIP switch to “Boot from uSD](../rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md). “
- Connect the USB cable and open the serial terminal. If you have trouble with this step, refer to [the serial connection article](../../../../homepage/other-articles/serial-connection.md).
- Plug the SD card into the HummingBoard and connect the power supply.

After that step, the board will boot automatically.

<a id="boot-from-usb"></a>

# Boot from USB

It’s possible to place the rootfs and boot partitions on the USB drive. This allows us to boot the Linux and get access to the eMMC.

- Prepare the SD card. Connect the SD card to your PC and flash the bootloader image.

```
$ sudo dd if=images/rzxxxx_solidrun-sd-bootloader-xxxxxxx.img of=/dev/sdX bs=1M
```

- Prepare a USB drive with the boot partition and the rootfs partition.

```
$ sudo dd if=images/rzxxxx_solidrun_buildroot-sd-xxxxxxx.img of=/dev/sdX bs=1M
```

> [!INFO]
> Note: the USB drive is assumed to be connected to /dev/sdX device and unmounted. Don’t forget to change X to the actual device letter.

- Set the [S3 DIP switch to “Boot from uSD](../rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md). “
- Connect the USB cable and open the serial terminal. If you have trouble with this step, refer to [the serial connection article](../../../../homepage/other-articles/serial-connection.md).
- Plug the SD card and USB drive into the HummingBoard, and connect the power supply.

After this step, the board will boot. Stop it in the U-Boot command line in your terminal.

> In: serial@1004b800  
> Out: serial@1004b800  
> Err: serial@1004b800  
> Net: EEPROM: TlvInfo v1 len=18  
> eth0: ethernet@11c20000  
> Hit any key to stop autoboot: 2  
> \=>

- Set the bootargs for the USB boot:

```
# setenv bootargs "rw rootwait earlycon root=/dev/sda2"
```

- Load kernel and fdt file from the USB drive:

```
# usb start
# load usb 0:1 $kernel_addr_r boot/Image
# load usb 0:1 $fdt_addr_r boot/rzxxx-hummingboard.dtb
```

> [!INFO]
> Note: make sure to choose the correct dtb file according to your device.

- If you need an eMMC access from Linux:

```
# setenv sdio_select emmc
```

- Boot the Linux kernel:

```
# booti $kernel_addr_r - $fdt_addr_r
```

After that step, the board will boot using the rootfs placed on the second USB drive partition.

<a id="boot-using-tftp"></a>

# Boot using TFTP

U-Boot allows to load the kernel, ramdisk, and fdt over TFTP. In this example, we will use ramdisk for the rootfs.

- Prepare the SD card. Connect the SD card to your PC and flash the bootloader image.

```
$ sudo dd if=images/rzxxxx_solidrun-sd-bootloader-xxxxxxx.img of=/dev/sdX bs=1M
```

- Set the [S3 DIP switch to “Boot from uSD](../rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md). “
- [Prepare the TFTP server.](https://github.com/SolidRun/build_rzg2lc#setting-a-tftp-server-from-a-different-linux-machine-in-the-same-network) Place the following files from the build directory on the server:
  - images/tmp/Image
  - images/tmp/rzxxxx-hummingboard.dtb
  - images/tmp/initrd.img
- Connect the USB cable and open the serial terminal. If you have trouble with this step, refer to [the serial connection article](../../../../homepage/other-articles/serial-connection.md).
- Plug the SD card, USB drive, and Ethernet cable into the HummingBoard, and connect the power supply.

After this step, the board will boot. Stop it in the U-Boot command line in your terminal.

- Set the TFTP server address:

```
# setenv serverip <the.server.ip.addr>
```

> [!INFO]
> the server ip address is the ip of the device that you created the server on.

- Get the IP address:

```
# dhcp
```

- Set the boot args and load boot artifacts:

```
# setenv bootargs "earlycon"
# tftpboot $kernel_addr_r Image
# tftpboot $fdt_addr_r rzxxx-hummingboard.dtb
# tftpboot $ramdisk_addr_r initrd.img
```

- If you need an eMMC access from Linux:

```
# setenv sdio_select emmc
```

- Set the [S3 DIP switch to "Boot from emmc"](../rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md).
- Boot the Linux kernel:

```
# booti $kernel_addr_r $ramdisk_addr_r $fdt_addr_r
```

After that step, the board will boot using the ramdisk rootfs.

> [!INFO]
> Note: since the rootfs is in the RAM, all changes in the filesystem will be lost after reboot.

<a id="flashing-bootloaders-and-rootfs-from-linux"></a>

# Flashing bootloaders and rootfs from Linux

This paragraph assumes you boot Linux using rootfs placed on the USB. And you selected SDIO switch to the eMMC in the u-boot environment before jumping to Linux.

```
# setenv sdio_select emmc
```

Also, you need to copy bootloader files to the rootfs in the USB:

- bl2\_bp-rzxxx-solidrun.bin
- fip-rzxxxx-solidrun.bin
- rzxxx\_solidrun\_buildroot-sd-xxxxxxx.img

Disable eMMC boot partition write protection:

```
$ echo 0 > /sys/block/mmcblk0boot0/force_ro
```

Flash the bootloaders:

```
$ dd if=bl2_bp-rzxxx-solidrun.bin of=/dev/mmcblk0boot0 bs=512 seek=1
$ dd if=fip-rzxxx-solidrun.bin of=/dev/mmcblk0boot0 bs=512 seek=256
```

Enable boot partition:

```
# mmc bootbus set single_backward x1 x8 /dev/mmcblk0
# mmc bootpart enable 1 0 /dev/mmcblk0
```

Flash the bootfs and rootfs:

```
$ dd if=rzxxxx_solidrun_buildroot-sd-xxxxx.img of=/dev/mmcblk0 bs=4M
```

After this step, you can reboot, and the board will start booting from eMMC.

<a id="flashing-bootloaders-over-serial"></a>

# Flashing bootloaders over serial

An RZ/G2LC CPU has a serial downloader mode. With this mode, it’s possible to flash the bootloader to SOM’s eMMC using flash-writer bare-metal software.

Prepare the board:

- Set the [S3 DIP switch to “Serial Downloader Mode. “](../rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md)
- Connect serial cable
- Connect power supply

On your PC terminal go to the flash-writer script dir:

```
$ cd build_scripts/flash-writer/
```

> [!INFO]
> Note: The config.ini file contains all the necessary script configuration, including binaries paths and the serial device. That config sets `/dev/ttyUSB0` as the default serial device. Don’t forget to change the `SERIAL_DEVICE_INTERFACE` variable to the actual device if it’s different in your system.

Flash the bootloaders:

```
$ sudo ./flash_writer_tool.sh config.ini fw
$ sudo ./flash_writer_tool.sh config.ini bl2
$ sudo ./flash_writer_tool.sh config.ini fip
$ sudo ./flash_writer_tool.sh config.ini emmc_config
```

> [!INFO]
> Note: The fw command uploads the flash-writer bare-metal software to the RAM. You can change the order or skip some of the commands if you need, but the fw command should always come first since it uploads the necessary software for the other commands.

Set the [S3 DIP switch to eMMC boot](../rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md) and press reset.

<a id="pre-programmed-soms"></a>

# Pre-programmed SOMs

> [!NOTE]
> - Pre-programmed SOMs (bootloader/custom\_image on eMMC) can be ordered from Solid-Run for high volume (programming will be done during the production test process).
> - It is possible to order SOMs from Solidrun with preprogrammed [General](https://images.solid-run.com/RZ/U-Boot/build_date_20231225-git_rev_cd172f8)/Custom bootloader on eMMC and then you can load the Linux & FS over [USB-Disk](hummingboard-rz-family-boot-options.md#boot-from-usb) / [Ethernet (TFTP/DHCP)](hummingboard-rz-family-boot-options.md#boot-using-tftp) and then program the custom image from Linux…