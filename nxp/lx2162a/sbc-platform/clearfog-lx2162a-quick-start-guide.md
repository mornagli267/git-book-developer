# ClearFog LX2162A Quick Start Guide

***

![](<../../../.gitbook/assets/LX2162 Clearfog side no shodow.png>)

## Introduction

The following quick start guide provides background information about the [ClearFog LX2162A](https://www.solid-run.com/embedded-networking/nxp-lx2160a-family/lx2162a-som/) products which use the LX2162A System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Revision** | **Notes** |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- |
| 08 Nov 2022       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1.0          |           |
| Table of Contents | <p>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#introduction">Introduction</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#revision-and-notes">Revision and Notes</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#hardware-setup">Hardware Setup</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#product-specifications">Product Specifications</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#block-diagram">Block Diagram</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#visual-features-overview">Visual features overview</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#software-setup">Software Setup</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#recommended-cables">Recommended Cables</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#boot-select">Boot Select</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#booting-from-an-sd-card">Booting from an SD card</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#sfp-modules">SFP Modules</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#packet-generator-using-dpdk">Packet Generator using DPDK</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#tips">Tips</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#example-to-install-gentoo-from-the-ubuntu">Example to install Gentoo from the Ubuntu</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#build-from-source">Build From Source</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#documentation">Documentation</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/199131187/ClearFog+LX2162A+Quick+Start+Guide#related-articles">Related Articles</a>e</p> |              |           |

## Hardware Setup

#### Product Specifications

|                                  | **ClearFog LX2162A**                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------------- |
| I/Os                             | <p>1 x USB 2.0<br><br>1 x USB 3.0 (RunBMC)</p>                                               |
| Networking                       | <p>2 x SFP28 ports (25GbE each)<br>2 x SFP+ ports (10GbE each)<br>8 x 1GbE copper (RJ45)</p> |
| Processor                        | NXP Layerscape LX2162A 16-core Arm Cortex A72 up to 2GHz                                     |
| Memory & Storage                 | <p>Up to 32GB DDR4<br>8GB eMMC<br>MicroSD</p>                                                |
| Misc.                            | <p>USB to STM32 for remote management<br>RunBMC compliant socket</p>                         |
| Development and Debug interfaces | <p>mini USB<br>JTAG</p>                                                                      |
| Power                            | <p>12V DC Jack<br>ATX standard</p>                                                           |
| Expansion card I/Os              | \*2 x mPCIe x1 Gen 3.0                                                                       |
| Temperature                      | Commercial: 0°C to 70°C                                                                      |
| Dimensions                       | PCBA: 170 x 137mm                                                                            |

## **Block Diagram**

The following figure describes the ClearFog LX2162A Block Diagram.

![](<../../../.gitbook/assets/ClearFog - LX2162A Block Diagram (1).jpg>)

{% hint style="info" %}
* Serdes-1 lanes are routed to the 2x SFP28 (via TI retimer) and 2x SFP+ connector
* Serdes-2 lanes are routed to 8x 1GbE RJ-45 ports trough Marvell Octal PHY \*or 6x 1GbE RJ-45 ports trough Marvell Octal PHY and 2 mPCIe x1 Gen 3.0
{% endhint %}


## Visual features overview

Please see below the features overview of the connector side of the ClearFog LX2162A

![](<../../../.gitbook/assets/Copy of ClearFog LX2-Lite layout.jpg>)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* ClearFog LX2162A
* Power adapter 5A@12V or ATX 60W+
* Mini-USB to USB for console, the ClearFog LX2162A has an onboard FTDI chip.
* IP router or IP switch

## Recommended Cables

The following is a list of industry-standard cables, sorted by type, with the necessary compliance requirements that have been proven to work well with the ClearFog product family.

These examples are the cables which SolidRun uses for testing, and should provide enough information to source products from your preferred cable vendor.

* Ethernet cable: Monoprice 24AWG Cat6A 500MHz STP
* USB Cable: SuperSpeed USB 3.0 Type A Male to Female Extension Cable in Black
* SFP connector: GigaLite GE-GB-P1RT-E SFP module with Monoprice 24AWG Cat6A 500MHz STP cable

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to the following DIP switch:

|            |          |          |          |          |          |
| ---------- | -------- | -------- | -------- | -------- | -------- |
| Boot media | Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| SD         | OFF      | ON       | ON       | ON       | X        |
| eMMC       | OFF      | ON       | ON       | OFF      | X        |
| SPI        | OFF      | OFF      | OFF      | OFF      | X        |

The following shows how to set the switches on the boot source selector:

![](<../../../.gitbook/assets/image-20220112-164117 (2).png>)

## Booting from an SD card

The switches on the boot source **SW1** selector must be set as follows:

|          |          |          |          |          |
| -------- | -------- | -------- | -------- | -------- |
| Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| OFF      | ON       | ON       | ON       | X        |

The following shows how to set the switches on the boot source selector:

![](<../../../.gitbook/assets/image-20220112-164117 (2).png>)

Once you set the switches, you can apply the following for booting from an SD card.

1. Downloading the image

Download a pre-built image from [images.solid-run.com](https://images.solid-run.com/LX2k/lx2160a_build)

Those images are organised by branch, build date and commit ID from [github.com/SolidRun/lx2160a\_build](https://github.com/SolidRun/lx2160a_build)  project that you can clone and build by yourself. Image filenames are generated with boot media, serdes protocol, module and board names.

For example -

```
ls-5.15.71-2.2.0/2024-11-01_c61a32e/lx2162a_rev2_som_clearfog_2000_650_2900_18_9_0-c61a32e.img.xz
```

was created from commit `c61a32e` on November 1. 2024, targeting LX2162A SoM on Clearfog Board with SerDes protocols 18 and 9 (SFPs at 10/25Gbps, RJ45 at 1Gbps).

1. Writing the image to the SD card

Use the following commands for writing the image to an SD card:

```
xz -dc lx2160a_....img.xz | dd of=/dev/sdX bs=4M conv=fsync
```

* For more information, please visit [Flashing an SD Card](../../other-articles/flashing-an-sd-card.md) .

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


1. SD card insertion\
   Please Insert the SD card into your device.
2. Serial Connection\
   Please insert the miniUSB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.
3. Power connection\
   Connect your DC power , and then connect the adaptor to mains supply.

The default images are designed to simplify installation of rootfs to eMMC, booting only into a minimal initramfs. For access to a full featured rootfs, install the contained image to either eMMC or the very same microSD:

Stop the u-boot count down by clicking any key –

![](<../../../.gitbook/assets/image-20220112-165255 (2).png>)

To flash to eMMC run the following commands (it will wipe your data on the eMMC device).

```
load mmc 0:1 0xa4000000 ubuntu-core.img
mmc dev 1
mmc write 0xa4000000 0 0xd2000
```

Alternatively flash to the same microSD card used to boot:

```
load mmc 0:1 0xa4000000 ubuntu-core.img
mmc dev 0
mmc write 0xa4000000 0 0xd2000
```

{% hint style="warning" %}
**Please Note:**\
After programming to eMMC **and** removing microSD, the Boot Select switch must be changed to “eMMC” as shown in the table above.
{% endhint %}


![](<../../../.gitbook/assets/image-20220112-165616 (2).png>)

{% hint style="warning" %}
**Please Note:** The above commands should be run only once (in the fist boot), or when a new image is to be used.
{% endhint %}


Boot the machine by running ‘**boot**’ in u-boot.

Once you installed the necessary serial connection software and ran the above commands , you should be able to see the following:

![](<../../../.gitbook/assets/image-20211216-145327 (3).png>)

* In order to be able to log in , please insert “**root**” as a username and password as follows:

![](<../../../.gitbook/assets/image-20211216-145039 (3).png>)

{% hint style="warning" %}
**Please note** If you are willing to use a similar image in production you must change this password, or completely disable root login.
{% endhint %}


1. Final stages

The following stages need to be done in order to finalize the system:

1. Run `fdisk /dev/mmcblk0` if using SD, or run if using `fdisk /dev/mmcblk1` eMMC.
2. Recreate the first partition by deleting it and then creating a new partition that starts at block 131072 and extends to the end of the drive (or less depending on your needs).
3. Write the new partition, when prompt about ‘Do you want to remove the signature?’ then answer with No.
4. Run `resize2fs /dev/mmcblk0p1` if using SD Card, or Run `resize2fs /dev/mmcblk1p1` if using eMMC.
5. In this stage the root partition should be big enough to start populating it; but first update the RTC clock.
6. Activate Network Interfaces\
   The native NICs of the SoC currently are enabled automatically at boot time. Their numbering follows the numerical order of `dpmac` (LX2160 native NICs) starting from 0 , please find a mapping of the mac numbers to physical connectors in the picture below.\
   ![](../../../.gitbook/assets/ClearFOG_LX2162A_Port_mapping.jpg) For example the RJ45 bottom port at the end of the PCB (dpmac8) is `eth11`.
7. Connect the RJ45 to your network with internet access (and DHCP server); and then run `dhclient` .
8. Update the RTC clock by running `ntpdate pool.ntp.org` and then `hwclock -w`.
9. Run `apt-update` and then populate the root filesystem as you wish.

Please see below an example of resizing the filesystem :

![](<../../../.gitbook/assets/image-20211216-153422 (3).png>)

## SFP Modules

For some SFP modules that work on SolidRun networking hardware platforms, please refer to [SFP Modules](../marvell-a38x-based-products/a388-other-articles/sfp-modules.md) .

## Packet Generator using DPDK

Following is an example instructions that demonstrates using the DPDK framework that is built in the lx2160a\_build project under build/dpdk/ directory –

1. Make sure that the kernel is booted with the following variables in the command line –

```
default_hugepagesz=1024m hugepagesz=1024m hugepages=2 isolcpus=1-15 iommu.passthrough=1
```

If using the above installation of Ubuntu then the /extlinux/extlinux.conf file should look as follows (the default installation with the addition of isolcpus=1-15 iommu.passthrough=1) –

```
  TIMEOUT 30
  DEFAULT linux
  MENU TITLE linux-lx2160a boot options
  LABEL primary
  MENU LABEL primary kernel
  LINUX /boot/Image
    FDT /boot/fsl-lx2160a-cex7.dtb
    APPEND console=ttyAMA0,115200 earlycon=pl011,mmio32,0x21c0000 default_hugepagesz=1024m hugepagesz=1024m hugepages=2 isolcpus=1-15 iommu.passthrough=1 pci=pcie_bus_perf root=PARTUUID=30303030-01 rw rootwait
```

2. From build/dpdk directory under the lx2160a\_build project, search for dynamic\_dpl.sh and testpmd files and copy them over to the LX2160A Ubuntu root filesystem
3. After boot unbind the linux network interfaces (`ethX`)
4. Run the following that will generate 10Gbps traffic on dpmac.10 using only a single core. Can be used to generate traffic on dpmac.1 and other interfaces –

```
dynamic_dpl.sh dpmac.10
export DPRC=dprc.2
testpmd -c 0x3 -n 1 -- --txd=1500 --txpkts=1500 --tx-first --auto-start --forward-mode=txonly --stats-period=10

```

Notice that DPRC variable in this case holds the output of dynamic\_dpl.sh

An alternative way to run testpmd in interactive mode is as follows –

```
dynamic_dpl.sh dpmac.10
export DPRC=dprc.2
testpmd -c 0x3 -n 1 -- --txd=1500 -i
set fwd txonly
set txpkts 1500
show port info 0
show config txpkts
start


```

## Tips

1. sshd is disabled by default for root access. Edit /etc/ssh/sshd\_config and set ‘PermitRootLogin yes’
2. ssh to the machine might take long time after boot. To accelerate that install ‘rng-tools’ where it’s main daemon increases the kernel’s entropy and accelerates random number key generation (which used by libssl and sshd afterwards).

## Example to install Gentoo from the Ubuntu

Gentoo is a free and open-source distribution with a rolling-release model.\
The bootloader and kernel provided are recent enough to install Gentoo from the eMMC Ubuntu to the NVMe or SATA device.

```
 apt install btrfs-progs
 mkfs.btrfs /dev/nvme0n1p1
 mount /dev/nvme0n1p1 /mnt
 cd /mnt
# change 20200609 with what's available here http://distfiles.gentoo.org/experimental/arm64/
 wget http://distfiles.gentoo.org/experimental/arm64/stage3-arm64-20200609.tar.bz2
 mount --rbind /dev dev
 mount --make-rslave dev
 mount -t proc /proc proc
 mount --rbind /sys sys
 mount --make-rslave sys
 mount --rbind /tmp tmp
 cp /etc/resolv.conf etc
 chroot . /bin/bash
 env-update && . /etc/profile
 emerge-webrsync
 emerge superadduser openssh vim
# Set the root password
 passwd 
# enable root login
 vim /etc/ssh/sshd_config 
# or create your user
 superadduser your_user
 ln -s /etc/init.d/net.{lo,eth0}
 rc-update add sshd default
 reboot

```

{% hint style="warning" %}
**Please note**
* In the same way, can install Debian or another Linux arm64 distribution.
{% endhint %}


{% hint style="warning" %}
**Please note**
* The default bootcmd probes every device and looks for a /extlinux/extlinux.conf
* The kernel command line uses the PARTUUID to boot the right drive can editing the root in the extlinux.conf to use directly root=/dev/nvme0n1p1 or  root=/dev/sdx .
{% endhint %}


## Build From Source

* You can build your own image using the script in here – [GitHub - SolidRun/lx2160a\_build](https://github.com/SolidRun/lx2160a_build)

{% hint style="success" %}
* Download a pre-built snapshot image based on Ubuntu 20.04 from here [SolidRun Images](https://images.solid-run.com/LX2k/lx2160a_build)
{% endhint %}


## Documentation

* ClearFog-LX2162A_Rev1.1.zip?api=v2 — _file not found in repository_
* ClearFog-LX2162A_Mech_Rev1.1.zip?api=v2 — _file not found in repository_


## Related Articles

* Page:[LX2162A SOM vs LX2160A COM Differences](lx2162a-other-articles/lx2162a-som-vs-lx2160a-com-differences.md)
  * [lx2160a-com](https://solidrun.atlassian.net/wiki/label/lx2160a-com)
  * [lx2162a-som](https://solidrun.atlassian.net/wiki/label/lx2162a-som)
* Page:[Flashing an SD Card](../../other-articles/flashing-an-sd-card.md)
  * [flash-sd-card](https://solidrun.atlassian.net/wiki/label/flash-sd-card)
* Page:[Serial Connection](../../other-articles/serial-connection.md)
  * [serial-connection](https://solidrun.atlassian.net/wiki/label/serial-connection)

Related pages

[LX2160A COM Hardware User Manual](../nxp-lx2160a-based-products/lx2160a-com-hardware-user-manual.md)LX2162A COM Hardware User Manual[Developer Center](https://developer.resources.solid-run.com/wiki/spaces/developer)Often read together

[LX2162A Software](lx2162a-software.md)LX2160A Software[Developer Center](https://developer.resources.solid-run.com/wiki/spaces/developer)


{% file src="attachments/ClearFog%20LX2162%20STEP.zip" %}
{% file src="attachments/PRELIMINARY%20ClearFog-LX2162A%20Simplified%20Schematics%20Rev1.0.pdf" %}
{% file src="attachments/ClearFog-LX2162A_Rev1.1.zip" %}
{% file src="attachments/ClearFog-LX2162A_Mech_Rev1.1.zip" %}


