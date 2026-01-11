# HummingBoard EU205 & RZ/G2L/G2LC SoM Quick Start Guide

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Revision** | **Notes**                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ------------------------ |
| 04/04/2025        | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 0            | draft                    |
| 22/05/2025        | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1            | Release (updated photos) |
| Table of Contents | <p>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#purpose">Purpose</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#connections">Connections</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#console">Console</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#prepare-bootable-microsd-card">Prepare bootable microSD Card</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#first-steps-with-buildroot-reference-system">First Steps with Buildroot reference system</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#log-in">Log-In</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#networking">Networking</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#log-in-via-ssh">Log-In via SSH</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#first-steps-with-debian-reference-system">First Steps with Debian reference system</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#log-in">Log-In</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#networking">Networking</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#log-in-via-ssh">Log-In via SSH</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#advanced-steps-with-debian-buildroot-reference-system">Advanced Steps with Debian/Buildroot reference system</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#expand-root-filesystem">Expand Root Filesystem</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#install-to-emmc">Install to eMMC</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#accessing-sensors-ports-and-peripherals">Accessing Sensors, Ports and Peripherals</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#rgb-led">RGB LED</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#accelerometer">Accelerometer</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#temperature-humidity-sensor">Temperature / Humidity Sensor</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#ambient-light-sensor">Ambient Light Sensor</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#air-quality-sensor">Air Quality Sensor</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#gps">GPS</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#uart">UART</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#i2c">I2C</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#rs485">RS485</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#can">CAN</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#digital-io">Digital IO</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#wifi">WiFi</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#lte-nb-iot-m1-cellular-modem">LTE NB-IoT/M1 Cellular Modem</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#access-at-interface">Access AT Interface</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#sim-select">SIM Select</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#cat-m1-nb-iot-select">Cat-M1 / NB-IoT Select</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#automatic-power-on">Automatic Power-On</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#data-connection">DATA Connection</a><br>- <a href="hummingboard-eu205-rz-g2l-g2lc-som-quick-start-guide.md#clpd-motor-driver-slg47115">CLPD Motor Driver (SLG47115)</a></p> |              |                          |

## Purpose

This guide provides basic instructions for operating the SolidRun HummingBoard-EU205 with RZ-G2L SoM and booting into Linux. Advanced usage scenarios are covered by separate technical documentation.

## Hardware Setup

### Connections

* 12V DC Power Adapter (12V recommended, supports up to 48V)
* Type-C USB Cable for serial console
* microSD Card
* Ethernet
* Configuration Jumpers
  * for G2L SoM: J5016 (4 pieces), J5026, J5027
  * for G2LC SoM: J5017, J5015, J5024, J5018, J5026, J5027

![EU205 Layout Front.png](<../../../.gitbook/assets/EU205 Layout Front.png>)

![EU205 Layout Back.png](<../../../.gitbook/assets/EU205 Layout Back.png>)

![EU205 Layout I\_Os no background.png](<../../../.gitbook/assets/EU205 Layout I_Os no background.png>)

### Boot Select

Configure the boot-mode for microSD using onboard DIP switches S3 & S4:

| G2L SoM         | **S3-1 (MD0)** | **S3-2 (MD1)** | **S4-1 (MD2)** | **S4-2 (SD\_DEV\_SEL)** |
| --------------- | -------------- | -------------- | -------------- | ----------------------- |
| microSD         | 0              | 0              | 0              | 0                       |
| eMMC            | 1              | 0              | 0              | 1                       |
| Serial Download | 1              | 0              | 1              | X                       |

| G2LC SoM        | **S3-1 (MD0)** | **S3-2 (MD1)** | **S4-1 (MD2)** | **S4-2 (SD\_DEV\_SEL)** |
| --------------- | -------------- | -------------- | -------------- | ----------------------- |
| microSD         | 0              | 0              | 0              | 1                       |
| eMMC            | 1              | 0              | 0              | 0                       |
| Serial Download | 1              | 0              | 1              | X                       |

> \[!INFO] **Note:** 0 = OFF, 1 = ON, X = don't care.

### Console

Start an application for serial console - such as [PuTTY](https://www.putty.org/) or [tio](https://github.com/tio/tio). Configure it for baud rate 115200 and the COMx or ttyUSBy interface representing the micro-USB console connection. For details also see [Serial Connection](../../other-articles/serial-connection.md).

Note that the serial device only appears after powering up the board. On first use it is recommended to follow below procedure:

1. connect console cable
2. connect power
3. find and connect to COMx / ttyUSBy interface with terminal application
4. push in microSD
5. press reset button

### Software Setup

#### Prepare bootable microSD Card

1. Download prebuilt sdcard image based on either [Buildroot](https://images.solid-run.com/RZ/Buildroot) or [Debian](https://images.solid-run.com/RZ/Debian):\
   `rzg2l-solidrun-sd-debian-<hash>.img.xz`\
   `rzg2l-solidrun-sd-buildroot-<hash>.img.xz`
2. uncompress downloaded image file
3. write image file to microSD card to create a byte-for-byte copy. [https://etcher.io/](https://etcher.io/) is recommended, professionals may use unix “dd” command.

> \[!NOTE] **Attention:** The SoM modules and carrier boards are programmed with critical identifying information, including the product name and SKU, stored in an EEPROMs at I2C bus 0, addresses 0x50 and 0x57. This data is structured according to the [ONIE TLV](https://opencomputeproject.github.io/onie/design-spec/hw_requirements.html#board-eeprom-information-format) standard and is essential for initializing the product and aligning the software accordingly. The `tlv_eeprom` command in U-Boot can be used to read this data. **Important:** If this information is deleted or becomes corrupted, it will impact the correct initialization and functionality of the product. In such cases, please contact SolidRun support for assistance.

## First Steps with Buildroot reference system

### Log-In

On power-on with valid software on microSD the system should automatically boot to a login prompt displayed on the serial console:

```
Welcome to Buildroot
rzg2l-solidrun login: 
```

Log in with user-name “root”, password “root”.

### Networking

Network interfaces are set to configure automatically using DHCP as soon as an ethernet link has been established.

`ping`, `curl` and `wget` are functional out of the box when connecting to a standard home network.

Show assigned IP:

```
# ip addr show dev eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
...
    inet 192.168.1.181/24 brd 192.168.1.255 scope global dynamic noprefixroute eth0
...
# ip addr show dev eth1
...
```

### Log-In via SSH

SSH Log-In is active by default using the same insecure username and password.

## First Steps with Debian reference system

### Log-In

On power-on with valid software on microSD the system should automatically boot to a login prompt displayed on the serial console:

```
Debian GNU/Linux 12 rzg2l-solidrun ttySC0
rzg2l-solidrun login: 
```

Log in with user-name “root”, no password.

### Networking

By default networking is not configured. For advanced or persistent configurations please refer to the [Debian Documentation](https://wiki.debian.org/NetworkConfiguration).

For connecting the first RJ45 port (next to power connector) using automatic configuration, execute:

```
root@rzg2l-solidrun:~# dhclient end0
root@rzg2l-solidrun:~# ip addr show end0
2: end0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether d0:63:b4:05:81:94 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.183/24 brd 192.168.1.255 scope global dynamic end0
       valid_lft 43195sec preferred_lft 43195sec
    inet6 fd78:1be0:f231:0:d263:b4ff:fe05:8194/64 scope global dynamic mngtmpaddr 
       valid_lft forever preferred_lft forever
    inet6 fe80::d263:b4ff:fe05:8194/64 scope link 
       valid_lft forever preferred_lft forever
```

### Log-In via SSH

To log in via SSH, an ssh key must be installed first. Copy your favourite public key, e.g. from `~/.ssh/id_ed25519.pub`, into a new file in the root users home directory at `~/.ssh/authorized_keys`:

```
root@rzg2l-solidrun:~# mkdir .ssh
root@rzg2l-solidrun:~# cat > .ssh/authorized_keys << EOF
ssh-ed25519 AAAAinsertyour pubkey@here
EOF
```

## Advanced Steps with Debian/Buildroot reference system

### Expand Root Filesystem

After flashing the root filesystem is smaller than the eMMC. To utilize all space, resize both the rootfs partition - and then the filesystem:

1. inspect partitions:Using fdisk, view the current partitions. Take note of the start sector for partition 2!

```
root@rzg2l-solidrun:~# fdisk /dev/mmcblk0
Welcome to fdisk (util-linux 2.38.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.
Command (m for help): p
Disk /dev/mmcblk0: 14.68 GiB, 15758000128 bytes, 30777344 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xa98926ac
Device         Boot Start     End Sectors  Size Id Type
/dev/mmcblk0p1 *    16384   38911   22528   11M  c W95 FAT32 (LBA)
/dev/mmcblk0p2 *    38912 1730559 1691648  826M 83 Linux
Command (m for help):
```

2. resize partition 2:Drop and re-create partition 2 at the same starting sector noted before, keeping the ext4 signature when prompted and re-adding the bootable flag:

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
First sector (2048-30777343, default 2048): 38912
Last sector, +/-sectors or +/-size{K,M,G,T,P} (38912-30777343, default 30777343): 
Created a new partition 2 of type 'Linux' and of size 14.7 GiB.
Partition #2 contains a ext4 signature.
Do you want to remove the signature? [Y]es/[N]o: N
Command (m for help): a
Partition number (1,2, default 2): 2
The bootable flag on partition 2 is enabled now.
Command (m for help): p
Disk /dev/mmcblk0: 14.68 GiB, 15758000128 bytes, 30777344 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xa98926ac
Device         Boot Start      End  Sectors  Size Id Type
/dev/mmcblk0p1 *    16384    38911    22528   11M  c W95 FAT32 (LBA)
/dev/mmcblk0p2 *    38912 30777343 30738432 14.7G 83 Linux
Command (m for help): w
The partition table has been altered.
Syncing disks.
```

3. resize root filesystem:Linux supports online-resizing for the ext4 filesystem. Invoke `resize2fs` on partition 1 to do so:

```
root@rzg2l-solidrun:~# resize2fs /dev/mmcblk0p2
```

### Install to eMMC

eMMC and microSD are not usable at the same time but selected first by boot-select switches and then by software during boot.

Installation of software to the eMMC requires a special procedure:

1. Download a prebuilt sdcard image based on either [Buildroot](https://images.solid-run.com/RZ/Buildroot) and create a bootable microSD card.
2. Format a USB flash drive with FAT32 (or ext4), and place on it the images that are to be installed to the eMMC, both Bootloader and OS - e.g.:\
   \- `rzg2l-solidrun-sd-debian-<hash>.img.xz`\
   \- `rzg2l-solidrun-mmc-bootloader-<hash>.img`
3. Insert microSD, set boot-select switches for microSD, then power-on the board and stop in u-boot at the timeout prompt by pressing any key:

```
...
Hit any key to stop autoboot:  0
=> 
```

4. Select eMMC and boot into a small rootfs in initramfs:

```
=> setenv sdio_select mmc
=> boot
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Found /extlinux/extlinux.conf
Retrieving file: /extlinux/extlinux.conf
303 bytes read in 1 ms (295.9 KiB/s)
RZ/G2* boot options
1:      mmc boot
2:      initrd boot
Enter choice: 
```

Quickly type the number “2”, then press return:

```
Enter choice: 2
2:      initrd boot
Retrieving file: /initrd.img
48479777 bytes read in 4013 ms (11.5 MiB/s)
...
Welcome to Buildroot
buildroot login: 
```

5. Log-in with user “root”, password “root”
6. Confirm eMMC is available:

```
# lsblk
NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
mmcblk0      179:0    0 14.7G  0 disk 
mmcblk0boot0 179:8    0    4M  1 disk 
mmcblk0boot1 179:16   0    4M  1 disk 
zram0        253:0    0    0B  0 disk
```

When the list includes “mmcblk0boot0” eMMC has been selected successfully. 7. Connect USB flash drive, then find the images and install them to eMMC:

```
#
[  165.516448] usb 2-1: new high-speed USB device number 2 using ehci-platform
[  165.691720] usb-storage 2-1:1.0: USB Mass Storage device detected
[  165.698778] scsi host0: usb-storage 2-1:1.0
[  166.726993] scsi 0:0:0:0: Direct-Access     TOSHIBA  TransMemory      5.00 PQ: 0 ANSI: 0 CCS
[  168.358467] sd 0:0:0:0: [sda] 2013184 512-byte logical blocks: (1.03 GB/983 MiB)
[  168.366454] sd 0:0:0:0: [sda] Write Protect is off
[  168.371981] sd 0:0:0:0: [sda] No Caching mode page found
[  168.377329] sd 0:0:0:0: [sda] Assuming drive cache: write through
[  168.405783]  sda: sda1
[  168.411371] sd 0:0:0:0: [sda] Attached SCSI removable disk
#
# mount /dev/sda1 /mnt
# cd /mnt
# ls
 rzg2l-solidrun-mmc-bootloader-<hash>.img
 rzg2l-solidrun-sd-debian-<hash>.img.xz
 # # remove write-protection on boot partition
 # echo 0 > /sys/devices/platform/soc/11c00000.mmc/mmc_host/mmc0/mmc0:0001/block/mmcblk0/mmcblk0boot0/force_ro
 #
 # # write bootloader image
 # dd if=rzg2l-solidrun-mmc-bootloader-<hash>.img of=/dev/mmcblk0boot0
 #
 # Ensure boot partition is configured
 # mmc bootpart enable 1 0 /dev/mmcblk0
 # 
 # # write OS image
 # xzcat rzg2l-solidrun-sd-debian-0bf2343.img.xz | dd of=/dev/mmcblk0 bs=4M conv=fsync
```

8. power-off the board, remove microSD and change boot select switches for eMMC.

On next power-on the system will boot from eMMC.

## Accessing Sensors, Ports and Peripherals

See below some minimal examples making use of various board features:

### RGB LED

The 3-colour LED D7 is controlled using the [Linux LED Framework](https://docs.kernel.org/leds/leds-class.html). Each colour is controlled separately supporting On, Off and triggers. E.g.:

```
echo heartbeat > /sys/class/leds/d7:blue/trigger
echo 1 > /sys/class/leds/d7:green/brightness
echo 0 > /sys/class/leds/d7:red/brightness
```

### Accelerometer

The accelerometer is using the [Linux IIO Framework](https://www.kernel.org/doc/html/v4.16/driver-api/iio/index.html). Sensor data can be accessed using [libIIO](https://wiki.analog.com/resources/tools-software/linux-software/libiio).

### Temperature / Humidity Sensor

The temperature and humidity sensor has no Linux driver at this time. Sensor data can be read out from userspace 2ith i2c cli utilities:

```
# measure humidity and temperature
i2ctransfer -y 0 w1@0x54 0xf5

# read measurement results: 2 byte humidity, 2 byte temperature, 1 byte crc
i2ctransfer -y 0 r5@0x54
```

For further information see [HS4003](https://www.renesas.com/hs4003) product page.

### Ambient Light Sensor

The light sensor has no Linux driver at this time. Sensor data can be read out from userspace with i2c cli utilities:

```
# setup sensor
i2ctransfer -y 0 w2@0x44 0x00 0x80; i2ctransfer -y 0 w2@0x44 0x01 0x08

# read data: 2 byte lux, 2 byte timer
i2ctransfer -y 0 w1@0x44 0x04 r4
```

For further information see [ISL76683](https://www.renesas.com/isl76683) product page.

### Air Quality Sensor

The ZMOD4410 has no Linux driver at this time. See [ZMOD4410](https://www.renesas.com/zmod4410) and [ZMOD4410](https://www.renesas.com/zmod4410-evk) Evaluation Kit product pages for further information.\
The device responds on I2C Bus 0 at chip address 0x32.

### GPS

#### UART

> Note: Available only with G2L SoM

Raw NMEA records can be accessed directly via `/dev/gnss0` device:

```
cat /dev/gnss0
```

Alternatively for a more friendly UI the [gpsd](https://gpsd.gitlab.io/gpsd/) package and its utilities may be used after configuring it to use `/dev/gnss0` at 38400 baud (see e.g. [/etc/default/gpsd](https://github.com/SolidRun/imx8dxl_build/blob/develop/overlay/etc/default/gpsd)).

#### I2C

> Note: Available only with G2LC SoM
>
> There is no Linux driver for I2C interface of U-Blox MIA-M10Q. Data may be polled at bus 1 chip 0x42 address 0xFD-0xFE (length) and 0xFF (data).\
> The access protocol should be implemented in a kernel driver as a single transaction must read 0xFD-0xFE plus N additional bytes or abort with a NAK.
>
> For details see MIA-M10Q Integration Manual.

### RS485

A Half-Duplex (2-wire) RS485 is available on J26-2 (A), J26-1 (B).

Normally the host should automatically switch the transceiver between RX and TX as needed, i.e. RX normally and TX while transmitting data. This is not (currently) supported by the Renesas G2L/C Linux uart driver, users must switch manually from userspace:

1. Acquire TX/RX control GPIO:

```
# for G2L only
echo 144 > /sys/class/gpio/export
cd /sys/class/gpio/P3_0
# for G2LC only
echo 442 > /sys/class/gpio/export
cd /sys/class/gpio/P40_2
# Both
echo out > direction
echo 0 > value
```

2. Set UART speed as needed:

```
# e.g. 9600 baud
stty -F /dev/ttySC3 9600
```

3. Transmit a message:

```
echo 1 > value
echo "Hello, World" > /dev/ttySC3
echo 0 > value
```

4. Receive messages:

```
cat /dev/ttySC3
```

### CAN

> Note: Available only with G2L SoM

Two full-duplex CAN interfaces are available on J26: J26-12 (CAN0H), J26-14 (CAN0L), J26-11 (CAN1L), J26-13 (CAN1H)

1. configure interface:

```
ip link set can0 up type can bitrate 125000 sample-point 0.75 dbitrate 1000000 dsample-point 0.8 fd on
```

2. Transmit a message:

```
cansend can0 "123#1234"
```

3. Receive messages:

```
candump -i can0
```

For second interface substitute `can0` with `can1`.

### Digital IO

Two digital inputs and two digital outputs operating at externally supplied voltage are available on J26: J26-5 (DIG\_IN1), J26-7 (DIG\_IN2), J26-6 (DIG\_OUT1), J26-8 (DIG\_OUT2)

The signals can be accessed using [libgpiod](https://libgpiod.readthedocs.io/en/latest/) example utilities:

```
# read inputs
gpioget $(gpiofind bDIG_IN1)
gpioget $(gpiofind bDIG_IN2)

# set outputs low
gpioset $(gpiofind DIG_OUT1)=0
gpioset $(gpiofind DIG_OUT2)=0

# set outputs high
gpioset $(gpiofind DIG_OUT1)=1
gpioset $(gpiofind DIG_OUT2)=1
```

Note: The inputs are inverting, i.e. reading a 1 means logical 0 on the line.

### WiFi

The Linux driver for DA16200 WiFi does not load automatically, but must be loaded manually after boot:

```
modprobe rswlan
rfkill unblock phy0
```

After unblocking with `rfkill` the new `wlan0` interface is operated like any standard Linux wifi device, see e.g. the [Debian WiFi/HowToUse](https://wiki.debian.org/WiFi/HowToUse#using_ifupdown_and_wireless-tools) page.

### Bluetooth

The DA14531 Bluetooth module is available by default as `hci0` and may be used after unblocking using the standard [bluez](https://www.bluez.org/) stack, e.g.:

```
rfkill unblock hci0
hciconfig hci0
hcitool -i hci0 lescan
```

### LTE NB-IoT/M1 Cellular Modem

The LTE Module is not currently supported by ModemManager. Instead it should be operated manually or scripted using AT commands.

#### Access AT Interface

The AT interface is available at `/dev/ttySC2` with hardware flow-control at 1843200 baudrate. It can be accessed using any serial terminal, for example `picocom`:

```
picocom -b 1843200 -y none -d 8 -p 1 -f h /dev/ttySC2
```

By default commands are not echoed but the terminal can be configured into a nicer mode with echo, auto-complete and history by executing `AT+SMART=1`.

To leave picocom press ctrl+a, then ctrl+x.

#### SIM Select

The Board supports either physical SIM via connector J3, and a soldered-on eSIM. The modem can switch between them using AT commands:

```
# first power off radio
AT+CFUN=0

# select SIM 1 (removable)
AT+CSUS=0

# select SIM 2 (eSIM)
AT+CSUS=1

# return two either airplane mode (CFUN=4) or normal operation (CFUN=1)
AT+CFUN=1
```

#### Cat-M1 / NB-IoT Select

The LTE module supports both Cat-M1 and NB-IoT. The choice is made in modem power-off state (`AT+CFUN=0`) using AT command `AT+SQNMODEACTIVE` (value 1 = LTE-M, value 2 = NB-IoT) followed with reset:

```
AT+CFUN=0
AT+SQNMODEACTIVE=1
AT^RESET
```

#### Automatic Power-On

Normally the modem radio stays off after boot (CFUN=0). It can be reconfigured for connecting to a network automatically (CFUN=1) using AT commands:

```
AT+SQNAUTOCONNECT=1
```

#### DATA Connection

Create file `/etc/ppp/options`:

```
/dev/ttySC2
1843200
nodetach
noauth
local
noipdefault
defaultroute
usepeerdns
crtscts
lock
debug
dump
-chap
connect "/usr/sbin/chat -t6 -f /etc/chatscripts/connect"
disconnect "/usr/sbin/chat -t6 -f /etc/chatscripts/disconnect"
```

Create file `/etc/chatscripts/connect`:

```
ABORT "NO CARRIER"
TIMEOUT 30
ABORT ERROR
 "" AT
OK AT+CGDATA="PPP",1
CONNECT ""
```

Create file `/etc/chatscripts/disconnect`:

```
"" "\d\d\d+++\c"
```

Ensure the modem is registering to a network, i.e. `AT+CFUN=1` or automatic power-on above.

Finally execute `ppp` application to connect:

```
pppd
```

> Note: pppd version 2.5.2 or later is required, older versions can' t cope with the non-standard `1843200` baudrate (“speed 1843200 not supported“).

### CLPD Motor Driver (SLG47115)

> Note: I2C Interface available only with G2LC SoM

The SLG47115 has no Linux driver at this time and comes unprogrammed. It responds on I2C Bus 1 at chip address 0x00.

For further information see [SLG47115](https://www.renesas.com/slg47115) product page.
