# HummingBoard Pro & i.MX8M Plus SOM Quick Start Guide

![i.MX8M Plus - HummingBoard Pro Sideways.png](./attachments/i.MX8M%20Plus%20-%20HummingBoard%20Pro%20Sideways.png)

<a id="introduction"></a>

## Introduction

The following quick start guide provides background information about the [HummingBoard Pro](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/hummingboard-m/#pulse).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 21 Jan 2024 | Yazan Shhady | 1.0 | Initial release |
| 22 Dec 2024 | Yazan Shhady | 1.1 | Add instructions for programming the eMMC. |
| 31 Dec 2024 | Yazan Shhady | 1.2 | Provide more detailed instructions for programming MAC addresses. |
| 27 Jul 2025 | Josua Mayer | 1.3 | Fix microsd boot-select setting |
| 11 Dec 2025 | Yazan Shhady | 1.4 | Correct DC input voltage range to 7V–18V |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Hardware Setup](#hardware-setup)<br>  - [Product specifications](#product-specifications)<br>  - [HummingBoard Pro](#hummingboard-pro)<br>  - [Block Diagram](#block-diagram)<br>  - [Visual features overview](#visual-features-overview)<br>- [Software Setup](#software-setup)<br>  - [Cable setup and prerequisites](#cable-setup-and-prerequisites)<br>- [Boot Select](#boot-select)<br>- [Booting from SD card](#booting-from-sd-card)<br>- [Programming eMMC](#programming-emmc)<br>  - [Final stages](#final-stages)<br>- [More Features](#more-features)<br>  - [Internet](#internet)<br>    - [WiFi](#wifi)<br>  - [Bluetooth](#bluetooth)<br>  - [GPIO Pins Control](#gpio-pins-control)<br>  - [Cellular Modem](#cellular-modem)<br>  - [SPI](#spi)<br>  - [Audio](#audio)<br>  - [Basler Camera](#basler-camera)<br>- [TLV EEPROM Support](#tlv-eeprom-support)<br>- [MAC Address](#mac-address)<br>- [List Of Supported OS](#list-of-supported-os)<br>- [Build from source](#build-from-source)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="hardware-setup"></a>

## Hardware Setup

<a id="product-specifications"></a>

#### Product specifications

| **Model** | <a id="hummingboard-pro"></a><br><br>#### HummingBoard Pro |
| --- | --- |
| SOM Model | NXP i.MX8M Plus Dual / Quad core Arm Cortex A53 up to 1.8GHz (with Arm M7 GPP) |
| Memory & Storage | Up to 4GB LPDDR4  <br>eMMC  <br>MicroSD |
| Network | 2 x Ethernet RJ45 10/100/1000  <br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4/5 GHz) |
| Connectivity | 2 x USB 3.0  <br>Mini PCIe  <br>M.2  <br>SIM card slot |
| Media | HDMI 2.0 out  <br>MIPI-DSI  <br>2 x MIPI-CSI  <br>Digital audio (Riser interface FPC connector)<br><br>Onboard audio codec |
| I/O | 1 x Reset button  <br>1 x Configurable push button  <br>MikroBus click interface  <br>3 x LED indicators  <br>RTC |
| OS Support | Linux |
| Environment | Commercial: 0°C to 70°C  <br>Industrial: -40°C to 85°C |
| Dimensions | PCBA: 100 x 70mm  <br>Enclosure : 120 x 80 x 30mm |
| Power | 7V – 18V wide range  <br>PoE sink support 802.3af Class 0 |
| Enclosure | Optional extruded aluminum (IP32) enclosure |
|     | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355) |

> [!INFO]
> Supported with i.MX8M-PLUS SOM. For more detailed information about our SOM-i.MX8M series please visit this user manual : [i.MX8M Plus SOM Hardware User Manual](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493766) .

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the i.MX8M Pro Block Diagram.

![HummingBoard Pro - i.MX8M Plus Block Diagram (1).png](./attachments/HummingBoard%20Pro%20-%20i.MX8M%20Plus%20Block%20Diagram%20(1).png)

<a id="visual-features-overview"></a>

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Pro.

![HummingBoard Pro - i.MX8M Plus layout.png](./attachments/HummingBoard%20Pro%20-%20i.MX8M%20Plus%20layout.png)

Print side connector overview of the HummingBoard Pro.

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

![Unbenannt.png](./attachments/Unbenannt.png)

> [!INFO]
> Note: The black rectangle represents the switch position.

Once you set the switches, you can apply the following for booting from an SD card.

**1\. Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/lf-6.6.52-2.2.0/2025-07-02_cffbac8/debian-bootimg-cffbac8.img.xz
```

- For more Debian releases, please visit [Debian Release for i.MX8](https://images.solid-run.com/IMX8/imx8mp_build).

**2\. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc debian-bootimg-cffbac8.img.xz | sudo dd of=/dev/sdX bs=4k conv=fdatasync status=progress
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
- Update Debian Repository Sources:
  - Open the sources.list file to edit your system's repository configuration:
```
sudo nano /etc/apt/sources.list
```
  - Update the repository lines in the file with the following entries:
```
deb https://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
deb-src https://deb.debian.org/debian bookworm main contrib non-free non-free-firmware 
```
- Use the following commands in order to keep your system up-to-date:
```
sudo apt-get update 
sudo apt-get upgrade -y
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

**Please Note**

> [!NOTE]
> - mPCIe interface **doesn't** support **PCIe** interface - it supports USB 3.0 only.
> - M.2 interface supports PCIe and USB 3.0 interfaces

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

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
5. Run Weston.
  -  Connect your HDMI cable and you should be able to see the following :![](./attachments/IMG-6928-20211014-134838.jpg)

> [!NOTE]
> By default one application is available, the terminal emulator, at the upper left corner.

- Start weston FROM A PHYSICAL TERMINAL (from the above terminal, not remote or serial session):

```
  weston
```

This will bring up the following:

![](./attachments/IMG-6920-20211014-132727.jpg)

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

> [!NOTE]
> For more applications, you can refer to [GUI Support](https://github.com/SolidRun/documentation/blob/bsp/imx6/debian-11_sr1.md#wayland) to install X11, OpenGL-ES, GStreamer, or you can follow this page [Gnome](https://linuxhint.com/install_gnome_debian_10_minimal_server/) for installing Gnome desktop

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
| Labels<br><br>- No labels<br>- [Edit Labels](#section-6668bb0e-e4ae-4e9c-ac35-987c537b4f5f)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard+Pulse+Pin+MUX.xlsx?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard+Pulse+Pin+MUX.xlsx&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard+Pulse+Pin+MUX.xlsx) | Microsoft Excel Spreadsheet [HummingBoard Pulse Pin MUX.xlsx](/wiki/download/attachments/582057985/HummingBoard%20Pulse%20Pin%20MUX.xlsx?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-06f976bb-f6cd-4c96-9fdc-9e72340db974)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard+iMX8+Gerbers.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard+iMX8+Gerbers.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard+iMX8+Gerbers.zip) | ZIP Archive [HummingBoard iMX8 Gerbers.zip](/wiki/download/attachments/582057985/HummingBoard%20iMX8%20Gerbers.zip?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-64f7b83e-1ef5-4bcc-9468-fea65b7070db)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard+iMX8+PCB.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard+iMX8+PCB.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard+iMX8+PCB.zip) | ZIP Archive [HummingBoard iMX8 PCB.zip](/wiki/download/attachments/582057985/HummingBoard%20iMX8%20PCB.zip?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-1ff6c6f6-3253-4504-8fb0-09535f03d477)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard+Puls-REV.2.5-pcb.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard+Puls-REV.2.5-pcb.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard+Puls-REV.2.5-pcb.zip) | ZIP Archive [HummingBoard Puls-REV.2.5-pcb.zip](/wiki/download/attachments/582057985/HummingBoard%20Puls-REV.2.5-pcb.zip?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-5eeef2e3-bd7c-4757-a0e9-71c576a688cf)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard+iMX8+Mechanical+Drawings.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard+iMX8+Mechanical+Drawings.zip) | ZIP Archive [HummingBoard iMX8 Mechanical Drawings.zip](/wiki/download/attachments/582057985/HummingBoard%20iMX8%20Mechanical%20Drawings.zip?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-7595c71b-8ab3-43ad-a3d6-f04300652c1c)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard+iMX8+Schematics.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard+iMX8+Schematics.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard+iMX8+Schematics.zip) | ZIP Archive [HummingBoard iMX8 Schematics.zip](/wiki/download/attachments/582057985/HummingBoard%20iMX8%20Schematics.zip?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-28326f6c-82d5-49cc-8151-bd920292093d)<br><br>[Preview] [View](/wiki/download/attachments/582057985/HummingBoard-Pulse-Part-Assembly.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=HummingBoard-Pulse-Part-Assembly.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=HummingBoard-Pulse-Part-Assembly.zip) | ZIP Archive [HummingBoard-Pulse-Part-Assembly.zip](/wiki/download/attachments/582057985/HummingBoard-Pulse-Part-Assembly.zip?api=v2) | Jan 21, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-0b18cffd-8613-4798-a138-c8aadbbfb86e)<br><br>[Preview] [View](/wiki/download/attachments/582057985/hummingboard-pro-extended-v1.0-simplified-schematics.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=hummingboard-pro-extended-v1.0-simplified-schematics.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=hummingboard-pro-extended-v1.0-simplified-schematics.pdf) | PDF File [hummingboard-pro-extended-v1.0-simplified-schematics.pdf](/wiki/download/attachments/582057985/hummingboard-pro-extended-v1.0-simplified-schematics.pdf?api=v2) | Jan 22, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-24aef688-3b70-45ad-bd1c-5fa660e700d9)<br><br>[Preview] [View](/wiki/download/attachments/582057985/hummingboard-pro_extended_v1.0_full_schematics.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=582057985&fileName=hummingboard-pro_extended_v1.0_full_schematics.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=582057985&fileName=hummingboard-pro_extended_v1.0_full_schematics.pdf) | PDF File [hummingboard-pro\_extended\_v1.0\_full\_schematics.pdf](/wiki/download/attachments/582057985/hummingboard-pro_extended_v1.0_full_schematics.pdf?api=v2) | May 11, 2025 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |

- Drag and drop to upload or [browse for files] ![](/wiki/images/icons/wait.gif)

Upload file 

File description  

[Download All](/wiki/download/all_attachments?pageId=582057985)

[ Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden