# i.MX6 Kernel

### Description

This page describes how to build a linux kernel that works on all i.MX6 based SolidRun devices.

We recommend using the SolidRun fork of linux version 4.9.x. This version works with all of our boards and enables all features of the hardware, including accelerated video de- and encoding and accelerated OpenGL-ES.

However we understand that sometimes there are reasons for using the upstream version of Linux. While a lot of work has gone into upstreaming support for our boards, it is not yet a drop-in replacement. Generally speaking if your application requires video processing or rendering, mainline is not ready.

### Getting a Cross-Compiler

For building the latest (>= 2018.01) versions of U-Boot a recent version of GCC is required. U-Boot specifically requires version 6 as a minimum.

Cross-Compilers can be acquired from various sources:

* crosstool-ng
* Linaro
* **your distro of choice:**

```
# Debian (Stretch or later):
sudo apt install crossbuild-essential-armhf
export CROSS_COMPILE=arm-linux-gnueabihf-

# openSUSE (15.0 or later):
sudo zypper install cross-arm-gcc7
export CROSS_COMPILE=arm-suse-linux-gnueabi-
```

### Build Instructions 4.9.y

To build the kernel perform the following on a Linux PC

* git clone –branch solidrun-imx\_4.9.x\_1.0.0\_ga [https://github.com/SolidRun/linux-fslc.git](https://github.com/SolidRun/linux-fslc.git)
* export CROSS\_COMPILE=\<External ARM toolchain prefix, e.g. arm-linux-gnueabihf→
* export ARCH=arm
* make imx\_v7\_cbi\_hb\_defconfig
* \# optionally modify the default configuration
* make zImage dtbs modules

A successful build produces both a kernel image and DeviceTree Binaries:

* arch/arm/zImage
* arch/arm/boot/dts/\*.dtb

{% hint style="info" %}
The standard configuration should suffice general use. We only recommend making changes if custom hardware or esoteric filesystems are being used.
{% endhint %}


### Build Instructions Mainline (>= 4.16)

To build the kernel perform the following on a Linux PC

* git clone –branch master [https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git)
* export ARCH=arm CROSS\_COMPILE=\<External ARM toolchain prefix, e.g. arm-linux-gnueabihf→
* make imx\_v6\_v7\_defconfig
* \# optionally modify the default configuration
* make zImage dtbs modules

A successful build produces both a kernel image and DeviceTree Binaries:

* arch/arm/zImage
* arch/arm/boot/dts/\*.dtb

{% hint style="warning" %}
The standard configuration is very minimal, you will want to add additional features such as file systems, PCI device drivers and Control-Group support for systemd! For more information about systemd, refer to [the corresponding wiki page of the Gentoo project](https://wiki.gentoo.org/wiki/Systemd#kernel).
{% endhint %}


### Build Instructions 3.14.y (Legacy)

To build the kernel perform the following on a Linux PC

* git clone –branch 3.14-1.0.x-mx6-sr-next [https://github.com/SolidRun/linux-fslc.git](https://github.com/SolidRun/linux-fslc.git)
* export CROSS\_COMPILE=
* export ARCH=arm
* make imx\_v7\_cbi\_hb\_defconfig
* \# optionally modify the default configuration
* make zImage dtbs modules

A successful build produces both a kernel image and DeviceTree Binaries:

* arch/arm/zImage
* arch/arm/boot/dts/\*.dtb

{% hint style="info" %}
The standard configuration should suffice general use. We only recommend making changes if custom hardware or esoteric filesystems are being used.
{% endhint %}


### Archived Versions

* 3.0.35
* 3.10.y

### Booting a kernel

Please refer to [i.MX6 U-Boot](/homepage/iot-industrial-product-line/nxp-imx6-based-products/imx6-software/imx6-u-boot.md)  on our U-Boot page.
