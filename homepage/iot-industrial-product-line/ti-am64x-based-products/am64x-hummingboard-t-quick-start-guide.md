# AM64x HummingBoard-T Quick Start Guide

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Revision** | **Notes**          |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------ |
| 26/10/2021        | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.0          | Initial release    |
| 26/06/2023        | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.1          | Production release |
| Table of Contents | <p>- <a href="am64x-hummingboard-t-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#purpose">Purpose</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#connections">Connections</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#console">Console</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#prepare-bootable-microsd-card">Prepare bootable microSD Card</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#first-steps-with-debian-reference-system">First Steps with Debian reference system</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#log-in">Log-In</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#networking">Networking</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#log-in-via-ssh">Log-In via SSH</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#expand-root-filesystem">Expand Root Filesystem</a><br>- <a href="am64x-hummingboard-t-quick-start-guide.md#additional-information">Additional Information</a></p> |              |                    |

## Purpose

This guide provides basic instructions for operating the SolidRun AM64 HummingBoard-T and booting into Linux. Advanced usage scenarios are covered by separate technical documentation.

## Hardware Setup

### Connections

* 12V DC Power Adapter (12V recommended, HummingBoard-T supports 9V-36V)
* microUSB cable for serial console
* microSD card for storing bootable SW

![](<../../../.gitbook/assets/TI AM64X Quick Guide 2023 Front (1).jpg>)

![](<../../../.gitbook/assets/TI AM64X Quick Guide 2023.jpg>)

### Boot Select

Configure the boot-mode for microSD using onboard DIP switch S1:

| Switch                  | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------------------- | - | - | - | - | - | - |
| microSD (FAT partition) | 0 | 0 | 0 | 1 | 0 | 1 |
| microSD (RAW)           | 1 | 0 | 0 | 0 | 1 | 1 |
| eMMC                    | 1 | 0 | 0 | 1 | X | X |

> \[!INFO] **Note:** 0 = OFF, 1 = ON, X = don't care.

### Console

Start an application for serial console - such as [PuTTY](https://www.putty.org/) or [tio](https://github.com/tio/tio). Configure it for baud rate 115200 and the COMx or ttyUSBy interface representing the micro-USB console connection. For details also see [Serial Connection](../../other-articles/serial-connection.md).

## Software Setup

#### Prepare bootable microSD Card

1. Download prebuilt sdcard image based on debian: [microsd-41a660b-debian-bookworm-sr1](https://solid-run-images.sos-de-fra-1.exo.io/AM64X/ti_am64x_build/20240530-41a660b/microsd-41a660b-debian-bookworm-sr1.img.xz)
2. uncompress downloaded image file
3. write image file to microSD card to create a byte-for-byte copy. [https://etcher.io/](https://etcher.io/) is recommended, professionals may use unix “dd” command.

> \[!NOTE] **Attention:** The AM64x SOM modules are programmed with critical identifying information, including the product name and SKU, stored in an EEPROM at I2C bus 0, address 0x50. This data is structured according to the [ONIE TLV](https://opencomputeproject.github.io/onie/design-spec/hw_requirements.html#board-eeprom-information-format) standard and is essential for initializing the product and aligning the software accordingly. The `tlv_eeprom` command in U-Boot can be used to read this data. **Important:** If this information is deleted or becomes corrupted, it will impact the correct initialization and functionality of the product. In such cases, please contact SolidRun support immediately for assistance.

## First Steps with Debian reference system

### Log-In

After inserting the programmed microSD card in the HummingBoard-T and after (re-)connecting the 12V power, the system should automatically boot to a login prompt displayed on the serial console:

```
Debian GNU/Linux 11 3f60b4ebfc7f ttyS2

3f60b4ebfc7f login: root
Linux 3f60b4ebfc7f 5.10.168-00011-g0f54435fab1c #1 SMP PREEMPT Sun May 21 16:21:43 UTC 2023 aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@3f60b4ebfc7f:~# 
```

Log in with user-name “root”, no password.

### Networking

By default networking is not configured. For advanced or persistent configurations please refer to the [Debian Documentation](https://wiki.debian.org/NetworkConfiguration).

For connecting the first RJ45 port (next to power connector) using automatic configuration, execute:

```
root@3f60b4ebfc7f:~# dhclient eth0
root@3f60b4ebfc7f:~# ip addr show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 34:88:de:e3:c0:17 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.225/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 552sec preferred_lft 552sec
    inet 192.168.1.226/24 brd 192.168.1.255 scope global secondary dynamic eth0
       valid_lft 552sec preferred_lft 552sec
    inet6 fe80::3688:deff:fee3:c017/64 scope link 
       valid_lft forever preferred_lft forever
```

### Log-In via SSH

To log in via SSH, an ssh key must be installed first. Copy your favourite public key, e.g. from `~/.ssh/id_ed25519.pub`, into a new file in the root users home directory at `~/.ssh/authorized_keys`:

```
root@e7c450f97e59:~# mkdir .ssh
root@e7c450f97e59:~# cat > .ssh/authorized_keys << EOF
ssh-ed25519 AAAAinsertyour pubkey@here
EOF
```

### Expand Root Filesystem

After flashing the root filesystem is smaller than the eMMC. To utilize all space, resize both the rootfs partition - and then the filesystem:

1. inspect partitions:Using fdisk, view the current partitions. Take note of the start sector for partition 2!

```
root@3f60b4ebfc7f:~# fdisk /dev/mmcblk1
Welcome to fdisk (util-linux 2.36.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): p
Disk /dev/mmcblk1: 7.42 GiB, 7969177600 bytes, 15564800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xff9ddf85
Device         Boot  Start     End Sectors  Size Id Type
/dev/mmcblk1p1        8192  131071  122880   60M  c W95 FAT32 (LBA)
/dev/mmcblk1p2      131072 2048000 1916929  936M 83 Linux
Command (m for help):
```

2. resize partition 1:Drop and re-create partition 2 at the same starting sector noted before, keeping the ext4 signature when prompted:

```
Command (m for help): d
Partition number (1,2, default 2): 2
Partition 2 has been deleted.
Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (2-4, default 2): 2
First sector (2048-15564799, default 2048): 131072
Last sector, +/-sectors or +/-size{K,M,G,T,P} (131072-15564799, default 15564799): 
Created a new partition 2 of type 'Linux' and of size 7.4 GiB.
Partition #2 contains a ext4 signature.
Do you want to remove the signature? [Y]es/[N]o: N
Command (m for help): p
Disk /dev/mmcblk1: 7.42 GiB, 7969177600 bytes, 15564800 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xff9ddf85
Device         Boot  Start      End  Sectors  Size Id Type
/dev/mmcblk1p1        8192   131071   122880   60M  c W95 FAT32 (LBA)
/dev/mmcblk1p2      131072 15564799 15433728  7.4G 83 Linux
Command (m for help): w
The partition table has been altered.
Syncing disks.
```

3. resize root filesystem:Linux supports online-resizing for the ext4 filesystem. Invoke `resize2fs` on partition 1 to do so:

```
root@3f60b4ebfc7f:~# resize2fs /dev/mmcblk1p2
```

## Additional Information

* [Developer documentation for reference image](https://github.com/SolidRun/ti_am64x_build)
