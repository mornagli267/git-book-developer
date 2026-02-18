# A388 Buildroot

## Description

Buildroot is a simple, efficient and easy-to-use tool to generate embedded Linux systems through cross-compilation.

This wiki page describes the build of complete minimal SD card image, that\
includes U-Boot, kernel, and filesystem ready to boot.

## Build Instructions

## **1. Download and extract the source of Buildroot version 2018.11:**

```
wget https://buildroot.org/downloads/buildroot-2018.11.tar.bz2
tar xf buildroot-2018.11.tar.bz2
cd buildroot-2018.11/
```

**2. Configure and build the SD card image:**

```
make solidrun_clearfog_defconfig
make
```

At the end of the build, the SD card image file is at `output/images/sdcard.img`.

## Deploy Instructions

1\. Write the image that Buildroot generated to your SD card with the following command as root:

```
dd if=output/images/sdcard.img of=/dev/sdX bs=1M conv=fdatasync
```

{% hint style="info" %}
Note that `/dev/sdX` must match the device node of the SD card on your PC host.
{% endhint %}


2\. Set the Clearfog board DIP switches to boot from SD. See the [ClearFog A388 Boot Select](/homepage/networking-product-line/marvell-a38x-based-products/a388-other-articles/clearfog-a388-boot-select.md)  article for details.

3\. Insert your SD card to the SD card slot, and power up the board.

## Customization and Package Selection

To install other software packages and customize the filesystem image, use the Buildroot configuration menu, and build again:

```
make menuconfig
make clean all
```

* For more details on Buildroot customization options see the [Buildroot user manual](https://buildroot.org/downloads/manual/manual.html).
