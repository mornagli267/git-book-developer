# Installing and booting an image on i.MX6 SOM eMMC

<a id="background"></a>

#### Background

The instructions below can be used to install the SolidRun provided Debian image on the i.MX6 SOM eMMC as an example. Customer can use these instructions to install any other Linux image.

- Set the boot select jumpers to boot from SDHC, please see [HummingBoard Edge/Gate Boot Jumpers](../imx6-other-articles/hummingboard-edge-gate-boot-jumpers.md) article for more information.
- Boot from SDHC
- Download the Debian image :

```
wget https://images.solid-run.com/IMX6/Debian/sr-imx6-debian-stretch-cli-20180916.img.xz
```

-  As root write the image to the eMMC:

```
xz -dc sr-imx6-debian-stretch-cli-20180916.img.xz | dd of=/dev/mmcblk2 bs=4M conv=fsync
```

- Download bootloader images:

```
wget https://images.solid-run.com/IMX6/U-Boot/v2018.01/spl-imx6-sdhc.bin
wget https://images.solid-run.com/IMX6/U-Boot/v2018.01/u-boot-imx6-sdhc.img
```

- As root write the bootloader images to the eMMC:

```
dd if=spl-imx6-sdhc.bin of=/dev/mmcblk2 bs=1K seek=1 conv=fdatasync
dd if=u-boot-imx6-sdhc.img of=/dev/mmcblk2 bs=1K seek=69 conv=fdatasync
```

- Shut the system down with the ‘poweroff’ command
- Disconnect power source
- Set the boot select jumpers to eMMC boot
- Boot the system from eMMC