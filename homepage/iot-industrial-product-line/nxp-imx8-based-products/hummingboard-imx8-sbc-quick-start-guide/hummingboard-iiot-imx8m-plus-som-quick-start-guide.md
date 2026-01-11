# HummingBoard IIOT & i.MX8M Plus SOM Quick Start Guide

![IIOT Sideways.png](./attachments/IIOT%20Sideways.png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the HummingBoard IIOT.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 21 Jan 2024 | Yazan Shhady | 1.0 | Initial release |
| 03 Dec 2024 | Yazan Shhady | 1.1 | Add instructions to program eMMC |
| 31 Dec 2024 | Yazan Shhady | 1.2 | Provide more detailed instructions for programming MAC addresses. |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product specifications](#product-specifications)<br>  - [HummingBoard IIOT](#hummingboard-iiot)<br>  - [Block Diagram](#block-diagram)<br>  - [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Boot Select](#boot-select)<br>- [Booting from SD card](#booting-from-sd-card)<br>- [Boot Select](#boot-select)<br>  - [Final stages](#final-stages)<br>- [Programming eMMC](#programming-emmc)<br>- [More Features](#more-features)<br>  - [Internet](#internet)<br>    - [WiFi](#wifi)<br>  - [Bluetooth](#bluetooth)<br>  - [Cellular Modem](#cellular-modem)<br>  - [SPI](#spi)<br>  - [Basler Camera](#basler-camera)<br>- [TLV EEPROM Support](#tlv-eeprom-support)<br>- [MAC Address](#mac-address)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product specifications

| **Model** | <a id="hummingboard-iiot"></a><br><br>#### HummingBoard IIOT |
| --- | --- |
| SOM Model | NXP i.MX8M Plus Dual / Quad core Arm Cortex A53 up to 1.8GHz (with Arm M7 GPP) |
| Memory & Storage | Up to 4GB LPDDR4  <br>eMMC  <br>MicroSD |
| Network | 2 x Ethernet RJ45 10/100/1000  <br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4/5 GHz) |
| Connectivity | 1 x USB3.0 (OTG)  <br>2 x USB3.0 ( Host)  <br>M.2 B-Key LTE modem (eSIM, NanoSim)  <br>M.2 M-Key - NVMe or AI accelerator  <br>Additional addon cards are supported\*  <br>SIM card slot |
| Media | LVDS  <br>MIPI-DSI  <br>2x MIPI-CSI 4 lanes  (1 MIPI-CSI on the SoM, 2 on the carrier) |
| I/O | 1 x Reset button  <br>1 x ON/OFF button  <br>1 x Configurable push button  <br>1 x RGB LED  <br>2 x CAN-FD  <br>2x RS232 or 2x RS485, or RS232 + RS485 (SW Configuration)  <br>1 x I/O Digital Input  <br>1 x I/O Digital output |
| Misc | TPM2.0  <br>RTC  <br>EEPROM |
| OS Support | Linux |
| Environment | Commercial: 0°C to 70°C  <br>Industrial: -40°C to 85°C |
| Dimensions | PCBA: 140 x 90mm  <br>Enclosure : **<TBD>** |
| Power | 7V – 28V wide range  <br>PoE sink support 802.3af Class 0 |
| Enclosure | Optional extruded aluminum (IP32) enclosure |
|     | [ Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355) |

> [!INFO]
> Supported with i.MX8M-PLUS SOM. For more detailed information about our SOM-i.MX8M series please visit this user manual : [i.MX8M Plus SOM Hardware User Manual](../../nxp-imx8-based-products/imx8m-plus-som-hardware-user-manual.md) .

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the i.MX8M Pro Block Diagram.

![image-20250115-103843.png](./attachments/image-20250115-103843.png)

<a id="visual-features-overview"></a>

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard IIOT.

![HummingBoard  i.MX8M IIOT Layout 2024.png](./attachments/HummingBoard%20%20i.MX8M%20IIOT%20Layout%202024.png)

Print side connector overview of the HummingBoard IIOT.

![image-20240929-120103.png](./attachments/image-20240929-120103.png)

![image-20241215-110714.png](./attachments/image-20241215-110714.png)

**Power Input Polarity \[J1\]:**

- **Connector Type**: Green two-terminal connector \[J1\].
- **Voltage Range**: 7V to 32V.
- **Polarity**:
  - **\+ (Positive)**: Left terminal (as marked in the image).
  - **\- (Negative)**: Right terminal (as marked in the image).

> [!NOTE]
> Plug for connector **J1** : 2 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm).

**J5004** {2x RS485, 2x CAN-FD, 2x RS232, DIG\_IN, DIG\_OUT}

![image-20241013-104553.png](./attachments/image-20241013-104553.png)

![image-20241121-134703.png](./attachments/image-20241121-134703.png)

> [!NOTE]
> Plug for connector **J5004** : 20 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm) like [this](https://www.digikey.com/en/products/detail/phoenix-contact/1738885/3606115).

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

- Linux or Windows PC
- HummingBoard IIOT with SOM
- 12V Power adapter (HummingBoard IIOT has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
- Type-C to USB for console, the HummingBoard IIOT has an onboard FTDI chip.
- IP router or IP switch

<a id="boot-select"></a>

## Boot Select

![image-20240901-112851.png](./attachments/image-20240901-112851.png)

Before powering up the board for the first time it is recommended to select the boot media using onboard DIP switch **S5**:

| **Switch** | **1**  <br>(MD0) | **2**  <br>(MD1) | **3**  <br>(MD2) | **4**  <br>(MD3) | **5**  <br>(VDD\_1.8V) | **6**  <br>(VDD\_3.3V) |
| --- | --- | --- | --- | --- | --- | --- |
| **uSD** | **ON** | **ON** | OFF | OFF | **ON** | OFF |
| **eMMC** | OFF | **ON** | OFF | OFF | **ON** | OFF |
| **USB OTG** | **ON** | OFF | OFF | OFF | **ON** | OFF |
| **Internal Fuses** | OFF | OFF | OFF | OFF | **ON** | OFF |

> [!INFO]
> **MDx** = BOOT\_MODEx, **VDD\_BOOT** = 1.8V **or** 3.3V (Select S5\[5\] **or** S5\[6\]) .  
> **Note** that **MD1** and **MD0** have been swapped between PCB version 1.1 and PCB version 1.0.

<a id="booting-from-sd-card"></a>

## Booting from SD card

<a id="boot-select"></a>

## Boot Select

Here is the correct DIP switch position for SD boot:

![image-20240901-120609.png](./attachments/image-20240901-120609.png)

> [!INFO]
> Note: The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from an SD card.

1. **Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/lf-6.6.52-2.2.0/2025-12-10_68e87c8/debian-bootimg-68e87c8.img.xz
```

- For more Debian releases, please visit [Debian Release for i.MX8](https://images.solid-run.com/IMX8/imx8mp_build).

2. **Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc debian-bootimg-68e87c8.img.xz | sudo dd of=/dev/sdX bs=4k conv=fdatasync status=progress
```

- For more information, please visit [Flashing an SD Card](../../../../homepage/other-articles/flashing-an-sd-card.md) .

> [!NOTE]
> Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

3. **SD card insertion**

Please Insert the SD card into your device.

4. **Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

5. **Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../../../homepage/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](./attachments/image-20210926-110202.png)

- In order to be able to log in , please insert “**root**” as a username and password as follows:

![](./attachments/image-20210926-110919.png)

<a id="final-stages"></a>

### **Final stages**

The following stages need to be done in order to finalise the imaging:

1. Run `fdisk /dev/mmcblk1` if using SD and `fdisk /dev/mmcblk2`if using eMMC.
2. Recreate the rootfs partition (mostly the second partition) by deleting it and then creating a new partition that starts at the next sector after the first one and extends to the end of the drive (or less depending on your needs).
3. Write the new partition, when prompt about ‘Do you want to remove the signature?’ then answer with Yes.
4. Run `resize2fs /dev/mmcblk1p2` if using SD Card and `resize2fs /dev/mmcblk2p2`if using eMMC.
5. In this stage the root partition should be big enough to start populating it; but first update the RTC clock.
6. Connect the RJ45 to your network with internet access (and DHCP server); and then run `dhclient`.
7. Update the RTC clock by running `ntpdate pool.ntp.org` and then `hwclock -w`.
8. Run apt-update commands below and then populate the root filesystem as you wish.

```
apt-get update && apt-get upgrade -y
```

Here is an example of the same process in the HB-IIOT device until step 4 (include):

![image-20241203-154508.png](./attachments/image-20241203-154508.png)

![image-20241203-154758.png](./attachments/image-20241203-154758.png)

![image-20241203-154958.png](./attachments/image-20241203-154958.png)

In the end you should see with “lsblk” that the partition size is in the required size.

<a id="programming-emmc"></a>

## Programming eMMC

Boot Linux from uSD and follow the Instructions bellow to Program the eMMC

1. **Programming the Bootloader on eMMC Boot Partition:**
```
# Download the bootloader binary (u-boot-mmc:2:1.bin) from https://images.solid-run.com/IMX8/imx8mp_build:
wget http://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/build_date_20241110-rev_9d040a0/u-boot-mmc:2:1-9d040a0.bin
# Disable write protection:
echo 0 > /sys/class/block/mmcblk2boot0/force_ro
# Write the bootloader to the boot partition:
dd if=u-boot-mmc:2:1-9d040a0.bin of=/dev/mmcblk2boot0 conv=sync
# Re-enable write protection:
echo 1 > /sys/class/block/mmcblk2boot0/force_ro
# Enable the eMMC boot partition:
mmc bootpart enable 1 1 /dev/mmcblk2
```
2. **Programming the Debian Image on the eMMC Main Partition:**  
```
# Download the Debian Image from https://images.solid-run.com/IMX8/imx8mp_build:
wget http://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/build_date_20240806-rev_449b768/imx8mp-sdhc-debian-449b768.img.xz
# Write the Yocto image to the eMMC main partition:
xz -dc imx8mp-sdhc-debian-449b768.img.xz | dd of=/dev/mmcblk2 bs=4k conv=fdatasync
```
3. Set the boot select to boot from eMMC as documented [here](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/868188181#boot-select) and do reset to boot from eMMC.

<a id="more-features"></a>

## More Features

<a id="internet"></a>

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).  
Models HummingBoard with WiFi, can be connected via [WiFi](https://solidrun.atlassian.net/wiki/spaces/developer/pages/200015887/CuBox-M+Quick+Start+Guide#wifi) or wired Ethernet.

- Please check you Ethernet connection.
- Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

- For more detailed information, please refer to [i.MX8M Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) .

<a id="wifi"></a>

##### WiFi

- You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

> [!NOTE]
> To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

2. Install the wpa\_supplicant package:

```
apt-get install wpasupplicant 
```

3. Edit network interfaces file :

At the bottom of the file, add the following lines to allow wlan as a network connection:

```
cat <<EOF > /etc/network/interfaces.d/wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

EOF
```

4. Create a configuration file with the relevant ssid:

```
cat <<EOF > /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=/run/wpa_supplicant
update_config=1

network={
    ssid="MYSSID"
    psk="passphrase" 
}

EOF
```

> [!NOTE]
> Check your personal ssids by running : ‘iw dev wlan0 scan’

5. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

- For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

<a id="bluetooth"></a>

#### Bluetooth

1. For showing all Bluetooth devices, run the following:

```
apt-get install bluez
hciconfig -a
```

2. Choose a device, and turn it on:

```
 hciconfig hci0 up
```

3. Set up the Bluetooth name:

```
hciconfig hci0 name 'SolidRun_Ble'
```

4. Make your Bluetooth detectable by other devices:

```
hciconfig hci0 piscan
```

5. If you want to connect to other devices:

- Start by scanning for other Bluetooth devices:

```
hcitool scan
```

- Choose a MAC address and connect :

```
rfcomm connect 0  $MAC 10 & 
```

- You can check the communication between the devices by writing :

```
l2ping -c 4  $MAC
```

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- For some cellular modules to be connected, please refer to [Cellular Modules](../../../iot-industrial-product-line/nxp-imx6-based-products/imx6-other-articles/cellular-modules.md) .

<a id="spi"></a>

#### SPI

For testing you serial peripheral interface - SPI, please see this documentation [SPI from Linux with spidev](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/321880065?draftShareId=ac699b08-ef2b-4682-9832-b012e01aeef0).

**GUI On Debian**

There is an option with the **Debian** image, up to the user, to work with a GUI like Weston, GNOME and etc.  
For applying this option do the following steps:

First, connect your device to a screen using the working output (HDMI / uHDMI).

For working with **Weston** GUI:

1. Install the Weston package.
```
$ sudo apt install weston
```
2. Make a directory for the output of the Weston GUI.
```
$ mkdir /your/directory/location
```
3. Give permissions to this directory.
```
 $ chmod 0700 /your/directory/location
```
4. Set the XDG\_RUNTIME\_DIR env param to your directory.
```
$ export XDG_RUNTIME_DIR=/your/directory/location
```
5. Start weston from the **PHYSICAL TERMINAL** (not remote or serial session):
```
$ weston
```

For working with **GNOME** GUI on top of Xorg:

1. Install Xorg.
```
$ sudo apt install xorg
```
2. Install your desired gnome.
```
$ sudo apt install gnome-session
```
NOTE: ‘gnome-session’ is an example of gnome that we can work with, you can replace the ‘session' with another GNOME extention.
3. Start your GNOME GUI.
```
$ sudo systemctl start gdm
```
  - For logging in you need a user on your device to log into it. You can create one before step 3 by this command (replace the ‘username’ with name that you want) :
```
$ sudo adduser username
```
  - You can jump between GUIs that you install (like gnome-session) by the setting button that locates in the down right corner of the home screen.

<a id="basler-camera"></a>

#### Basler Camera

For getting started with the Camera Module on your board, please see this documentation [Basler Camera Quick Start Guide](../hummingboard-imx8-sbc-quick-start-guide/hummingboard-pulse-imx8m-plus-som-quick-start-guide/hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md).

<a id="tlv-eeprom-support"></a>

## TLV EEPROM Support

Starting from April 01. 2022, the EEPROMs on Carriers, i.MX8M Plus SoMs are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. Check our [iMXMP EEPROM documentation](../../nxp-imx8-based-products/imx8m-other-articles/imx8mp-eeprom-programming-tlv.md) for additional information.

<a id="mac-address"></a>

## MAC Address

There are two options for storing MAC addresses on the i.MX8MP platform:

1. **Store the MAC address in OTP eFuses**
  - This is a **non-reversible action**, as the eFuse is permanently programmed.
2. **Store the MAC address in EEPROM using TLV format** (Recommended)
  - This method allows flexibility and is the preferred approach.
  - [Guidelines](https://solidrun.atlassian.net/wiki/spaces/developer/pages/344883516/iMX8MP+EEPROM+Programming+-+TLV#progammring-mac-address) for Programming a MAC Address in TLV Format

**Default Configuration**

- By default, the MAC address is stored in the SOM's TLV EEPROM.
- All SOMs are pre-flashed with SolidRun's default MAC address range in the TLV EEPROM.

**Custom MAC Address Option**

- There is an option to provide a custom MAC address range.
- SolidRun can program the custom MAC addresses into the TLV EEPROM upon request.

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211024-150854.png) | [Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) |
| ![](./attachments/image-20211024-151110.png) | [Yocto](https://github.com/SolidRun/meta-solidrun-arm-imx8/tree/zeus-imx8mp) |
| ![](./attachments/image-20211024-150920.png) | [Buildroot](https://github.com/SolidRun/imx8mp_build) |

<a id="build-from-source"></a>

## Build from source

- [i.MX8M Software](../../nxp-imx8-based-products/imx8m-plus-mini-nano-software.md)

<a id="documentation"></a>

## Documentation

     

|     | File | Modified |
| --- | --- | --- |

No files shared here yet.

- Drag and drop to upload or [browse for files] ![](/wiki/images/icons/wait.gif)

Upload file 

File description  

[ Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden