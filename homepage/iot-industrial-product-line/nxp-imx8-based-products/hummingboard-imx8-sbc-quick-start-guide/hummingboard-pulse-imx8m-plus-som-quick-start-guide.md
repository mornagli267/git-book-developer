# HummingBoard Pulse & i.MX8M Plus SOM Quick Start Guide

![](./attachments/HummingBoard%20Pulse%20with%20i.MX8%20plus%20sideways%20(small).png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [HummingBoard Pulse](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/hummingboard-m/#pulse).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 28 Oct 2021 | Yazan Shhady | 1.0 | Initial release |
| 04 Dec 2023 | Yazan Shhady | 1.1 | Add More Features |
| 29 Dec 2024 | Yazan Shhady | 1.2 | Provide more detailed instructions for programming MAC addresses. |
| 31 Dec 2024 | Yazan Shhady | 1.3 | Add instructions for programming the eMMC. |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product specifications](#product-specifications)<br>  - [HummingBoard Pulse](#hummingboard-pulse)<br>  - [Block Diagram](#block-diagram)<br>  - [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Boot Select](#boot-select)<br>- [Booting from SD card](#booting-from-sd-card)<br>- [Programming eMMC](#programming-emmc)<br>  - [Final stages](#final-stages)<br>- [More Features](#more-features)<br>  - [Internet](#internet)<br>    - [WiFi](#wifi)<br>  - [Bluetooth](#bluetooth)<br>  - [GPIO Pins Control](#gpio-pins-control)<br>  - [Enable the MINI-PCIe slot ‘J20’](#enable-the-mini-pcie-slot-j20)<br>  - [Cellular Modem](#cellular-modem)<br>  - [Enable the M.2 slot ‘M1’](#enable-the-m2-slot-m1)<br>  - [SPI](#spi)<br>  - [Audio](#audio)<br>  - [Basler Camera](#basler-camera)<br>- [TLV EEPROM Support](#tlv-eeprom-support)<br>- [MAC Address](#mac-address)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product specifications

| **Model** | <a id="hummingboard-pulse"></a><br><br>#### HummingBoard Pulse |
| --- | --- |
| SOM Model | NXP i.MX8M Dual / Quad core Arm Cortex A53 up to 1.5GHz (with Arm M4 GPP)<br><br>NXP i.MX8M Mini Single to Quad core Arm Cortex A53 up to 1.8GHz (with Arm M4 GPP) |
| Memory & Storage | Up to 4GB LPDDR4  <br>eMMC  <br>MicroSD |
| Network | 2 x RJ45 |
| Connectivity | 2 x USB 3.0 \*  <br>Mini PCIe  <br>M.2  <br>SIM card slot |
| Media | HDMI 2.0 out \*\*  <br>MIPI-DSI  <br>2 x MIPI-CSI \*\*\*  <br>Digital audio (Riser interface FPC connector)<br><br>Onboard audio codec |
| I/O | 1 x Reset button  <br>1 x Configurable push button  <br>MikroBus click interface  <br>3 x LED indicators  <br>RTC |
| OS Support | Linux |
| Environment | Commercial:  <br>Ambient temp.: 0°C to 70°C  <br>Enclosed ambient temp.: 0°C to 40°C  <br>CPU max die: 105°C<br><br>Industrial:  <br>Ambient temp.: -40°C to 85°C  <br>Enclosed Ambient temp.: -25°C to 65°C  <br>CPU max die: 105°C<br><br>Humidity (non-condensing): 10% – 90% |
| Dimensions | Board: 102mm x 69mm  <br>Enclosed: 141.5 x 78 x 30mm |
| Power | 7V – 28V wide range  <br>PoE sink support |
| Enclosure | Optional extruded aluminum (IP32) enclosure |
|     | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355) |

> [!INFO]
> Supported with i.MX8M-PLUS SOM. For more detailed information about our SOM-i.MX8M series please visit this user manual : [i.MX8M Plus SOM Hardware User Manual](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493766) .

> [!NOTE]
> **Please note**
> (\*) Only USB 2.0 supported with the i.MX8M Mini SoC.  
> (\*\*) Only supported with the i.MX8M SoC.  
> (\*\*\*) Only 1 x MIPI-CSI supported with the i.MX8M Mini SoC.

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the i.MX8M Plus Block Diagram.

![](./attachments/image-20211107-104502.png)

<a id="visual-features-overview"></a>

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Pulse.

![](./attachments/HummingBoard%20Pulse%20layout%20(2)-20221207-195839.png)

Print side connector overview of the HummingBoard Pulse.

![](./attachments/HummingBoard%20Pulse%20layout%20(1)-20221207-195811.png)

<a id="software-setup"></a>

## Software Setup

<a id="cable-setup-and-prerequisites"></a>

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

- Linux or Windows PC
- HummingBoard Pulse with SOM
- 12V Power adapter (HummingBoard Pulse has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
- Micro USB to USB for console, the HummingBoard Pulse has an onboard FTDI chip.
- IP router or IP switch

<a id="boot-select"></a>

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. On first use microSD is recommended source, configure dip switch S3 as follows:

| **Function/Switch** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| microSD | ON  | ON  | X   | X   | X   | X   |

“X” means don’t care, leave as is.

For additional options, please refer to [i.MX8M Series HummingBoard Boot Select](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287343073) page.

<a id="booting-from-sd-card"></a>

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![](./attachments/image-20240107-134703.png)

> [!INFO]
> Please Note:
> The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from an SD card.

**1\. Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/build_date_20240617-rev_87b97f9/imx8mp-sdhc-debian-87b97f9.img.xz
```

- For more Debian releases, please visit [Debian Release for i.MX8](https://images.solid-run.com/IMX8/imx8mp_build).

**2\. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc imx8mp-sdhc-debian-87b97f9.img.xz | sudo dd of=/dev/sdX bs=4k conv=fdatasync status=progress
```

- For more information, please visit [Flashing an SD Card](https://solidrun.atlassian.net/wiki/spaces/developer/pages/288129025) .

> [!NOTE]
> Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

**3\. SD card insertion**

Please Insert the SD card into your device.

**4\. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5\. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](./attachments/image-20210926-110202.png)

- In order to be able to log in , please insert “root” as a username and password as follows:

![](./attachments/image-20210926-110919.png)

<a id="programming-emmc"></a>

## Programming eMMC

Boot Linux from uSD and follow the Instructions bellow to Program the eMMC

1. **Programming the Bootloader on eMMC Boot Partition:**
```
# Download the bootloader binary (u-boot-mmc:2:1.bin) from https://images.solid-run.com/IMX8/imx8mp_build:
wget http://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/build_date_20241210-rev_ddc90d8/u-boot-mmc:2:1-ddc90d8.bin
# Disable write protection:
echo 0 > /sys/class/block/mmcblk2boot0/force_ro
# Write the bootloader to the boot partition:
dd if=u-boot-mmc:2:1-ddc90d8.bin of=/dev/mmcblk2boot0 conv=sync
# Re-enable write protection:
echo 1 > /sys/class/block/mmcblk2boot0/force_ro
# Enable the eMMC boot partition:
mmc bootpart enable 1 1 /dev/mmcblk2
```
2. **Programming the Debian Image on the eMMC Main Partition:**  
```
# Download the Debian Image from https://images.solid-run.com/IMX8/imx8mp_build:
wget http://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/build_date_20241210-rev_ddc90d8/imx8mp-sdhc-debian-ddc90d8.img.xz
# Write the Yocto image to the eMMC main partition:
xz -dc imx8mp-sdhc-debian-ddc90d8.img.xz | dd of=/dev/mmcblk2 bs=4k conv=fdatasync
```
3. Set the boot select to boot from eMMC as documented [here](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287343073) and do reset to boot from eMMC.

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

1\. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

> [!NOTE]
> To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

2\. Install the wpa\_supplicant package:

```
apt-get install wpasupplicant 
```

3\. Edit network interfaces file :

At the bottom of the file, add the following lines to allow wlan as a network connection:

```
cat <<EOF > /etc/network/interfaces.d/wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

EOF
```

4\. Create a configuration file with the relevant ssid:

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

5\. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

- For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

<a id="bluetooth"></a>

#### Bluetooth

1\. For showing all Bluetooth devices, run the following:

```
apt-get install bluez
hciconfig -a
```

2\. Choose a device, and turn it on:

```
 hciconfig hci0 up
```

3\. Set up the Bluetooth name:

```
hciconfig hci0 name 'SolidRun_Ble'
```

4\. Make your Bluetooth detectable by other devices:

```
hciconfig hci0 piscan
```

5\. If you want to connect to other devices:

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

<a id="gpio-pins-control"></a>

#### GPIO Pins Control

In order to be able to control the GPIO pins, please refer to [GPIO Pins Control - HummingBoard Pulse/Mate & i.MX8M Plus SOM](https://solidrun.atlassian.net/wiki/spaces/developer/pages/396197889)

<a id="enable-the-mini-pcie-slot-j20"></a>

#### Enable the MINI-PCIe slot ‘J20’

![](./attachments/image-20211227-160646.png)

To activate the mini-pcie connector you should run the commands bellow (Enable the modem Power & do Rest):

```
# enable power supply for M.2 and PCIe: "M2_3V3"
echo 10 > /sys/class/gpio/export 
echo out > /sys/class/gpio/gpio10/direction
echo 1 > /sys/class/gpio/gpio10/value

# pcie reset: "Mini-PCIe_PREST"
echo 1 > /sys/class/gpio/export 
echo out > /sys/class/gpio/gpio1/direction
echo 1 > /sys/class/gpio/gpio1/value
```

> [!NOTE]
> **Please Note**
> mPCIe interface doesn't support PCIe interface - it supports USB 3.0 only.

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

<a id="enable-the-m2-slot-m1"></a>

#### Enable the M.2 slot ‘M1’

![](./attachments/image-20211229-214652.png)

To activate the M.2 connector you should run the commands bellow (Enable the modem Power & do Rest):

```
# enable power supply for M.2 and PCIe: "M2_3V3"
echo 10 > /sys/class/gpio/export 
echo out > /sys/class/gpio/gpio10/direction
echo 1 > /sys/class/gpio/gpio10/value

# M.2 reset: "M.2_PREST"
echo 6 > /sys/class/gpio/export 
echo out > /sys/class/gpio/gpio6/direction
echo 1 > /sys/class/gpio/gpio6/value

# M.2 GPS Enable: "M.2_GPS_EN"
echo 7 > /sys/class/gpio/export 
echo out > /sys/class/gpio/gpio7/direction
echo 1 > /sys/class/gpio/gpio7/value
```

<a id="spi"></a>

#### SPI

For testing you serial peripheral interface - SPI, please see this documentation [SPI from Linux with spidev](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/321880065?draftShareId=ac699b08-ef2b-4682-9832-b012e01aeef0).

<a id="audio"></a>

#### Audio

First, you need to check that the required device is the default one by run:

```
$ aplay -L
```

If the sysdefault:CARD doesn’t set to wm8904 like this example

![](./attachments/image-20231126-094246.png)

Then you can play sound with choosing the device who set to wm8904 and generate audio, in the above situation the device is hw:CARD=wm8904audio so the test will work as this:

```
$ speaker-test -D hw:CARD=wm8904audio -t sine -c 2 -f 1000 -l 5
```

- NOTE: the “ -c “ flag used to set the number of the channels that you have in your audio output device, in my example I have 2 channels.

If the sysdefault:CARD=wm8904 you can test with this command:

```
$ speaker-test -t sine -f 1000 -l 5  
```

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

For getting started with the Camera Module on your board, please see this documentation [Basler Camera Quick Start Guide](https://solidrun.atlassian.net/wiki/spaces/developer/pages/315588609).

<a id="tlv-eeprom-support"></a>

## TLV EEPROM Support

Starting from April 01. 2022, the EEPROMs on Carriers, i.MX8M Plus SoMs are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. Check our [iMXMP EEPROM documentation](https://solidrun.atlassian.net/wiki/spaces/developer/pages/344883516) for additional information.

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

- [i.MX8M Software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493777)

<a id="documentation"></a>

## Documentation

      

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-7d65026d-7eac-46f9-82b3-30da646c3efe)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard-Pulse-Part-Assembly.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard-Pulse-Part-Assembly.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard-Pulse-Part-Assembly.zip) | ZIP Archive [HummingBoard-Pulse-Part-Assembly.zip](/wiki/download/attachments/262144001/HummingBoard-Pulse-Part-Assembly.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-0ae43a4a-05cc-4237-8292-74eb184c2be7)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard+iMX8+Schematics.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard+iMX8+Schematics.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard+iMX8+Schematics.zip) | ZIP Archive [HummingBoard iMX8 Schematics.zip](/wiki/download/attachments/262144001/HummingBoard%20iMX8%20Schematics.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-550ae301-1732-4520-bb32-892f1e14cc97)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard+iMX8+Mechanical+Drawings.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip) | ZIP Archive [HummingBoard iMX8 Mechanical Drawings.zip](/wiki/download/attachments/262144001/HummingBoard%20iMX8%20Mechanical%20Drawings.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-35851a60-0e75-4f54-98a0-85fb436c8eb3)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard+Puls-REV.2.5-pcb.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard+Puls-REV.2.5-pcb.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard+Puls-REV.2.5-pcb.zip) | ZIP Archive [HummingBoard Puls-REV.2.5-pcb.zip](/wiki/download/attachments/262144001/HummingBoard%20Puls-REV.2.5-pcb.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-7afebff7-2b6c-4f04-9d53-c3e28492618e)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard+iMX8+PCB.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard+iMX8+PCB.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard+iMX8+PCB.zip) | ZIP Archive [HummingBoard iMX8 PCB.zip](/wiki/download/attachments/262144001/HummingBoard%20iMX8%20PCB.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-aa9593bf-1e3c-4cd2-856a-4f8e53d89c29)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard+iMX8+Gerbers.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard+iMX8+Gerbers.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard+iMX8+Gerbers.zip) | ZIP Archive [HummingBoard iMX8 Gerbers.zip](/wiki/download/attachments/262144001/HummingBoard%20iMX8%20Gerbers.zip?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-0c2242aa-8be3-431e-9273-168282639208)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HummingBoard+Pulse+Pin+MUX.xlsx?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HummingBoard+Pulse+Pin+MUX.xlsx&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HummingBoard+Pulse+Pin+MUX.xlsx) | Microsoft Excel Spreadsheet [HummingBoard Pulse Pin MUX.xlsx](/wiki/download/attachments/262144001/HummingBoard%20Pulse%20Pin%20MUX.xlsx?api=v2) | Dec 26, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-7e9733e2-59ca-47d3-b149-39c542b0e841)<br><br>[Preview] [View](/wiki/download/attachments/262144001/HS00016-Heatsink.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=262144001&fileName=HS00016-Heatsink.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=262144001&fileName=HS00016-Heatsink.zip) | ZIP Archive [HS00016-Heatsink.zip](/wiki/download/attachments/262144001/HS00016-Heatsink.zip?api=v2) | Jul 15, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |

[Download All](/wiki/download/all_attachments?pageId=262144001)

[ Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden