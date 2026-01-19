# HummingBoard Pulse & i.MX8M Plus SOM Quick Start Guide

![](<../../../../.gitbook/assets/HummingBoard Pulse with i.MX8 plus sideways (small).png>)

## Introduction

The following quick start guide provides background information about the [HummingBoard Pulse](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/hummingboard-m/#pulse).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Revision** | **Notes**                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------- |
| 28 Oct 2021       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1.0          | Initial release                                                   |
| 04 Dec 2023       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1.1          | Add More Features                                                 |
| 29 Dec 2024       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1.2          | Provide more detailed instructions for programming MAC addresses. |
| 31 Dec 2024       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1.3          | Add instructions for programming the eMMC.                        |
| Table of Contents | <p>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#product-specifications">Product specifications</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#hummingboard-pulse">HummingBoard Pulse</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#booting-from-sd-card">Booting from SD card</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#programming-emmc">Programming eMMC</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#final-stages">Final stages</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#wifi">WiFi</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#gpio-pins-control">GPIO Pins Control</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#enable-the-mini-pcie-slot-j20">Enable the MINI-PCIe slot ‘J20’</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#cellular-modem">Cellular Modem</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#enable-the-m2-slot-m1">Enable the M.2 slot ‘M1’</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#spi">SPI</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#audio">Audio</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#basler-camera">Basler Camera</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#tlv-eeprom-support">TLV EEPROM Support</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#mac-address">MAC Address</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                                                                   |

## Hardware Setup

#### Product specifications

| **Model**        | <p><br><br>#### HummingBoard Pulse</p>                                                                                                                                                                                                                                      |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SOM Model        | <p>NXP i.MX8M Dual / Quad core Arm Cortex A53 up to 1.5GHz (with Arm M4 GPP)<br><br>NXP i.MX8M Mini Single to Quad core Arm Cortex A53 up to 1.8GHz (with Arm M4 GPP)</p>                                                                                                   |
| Memory & Storage | <p>Up to 4GB LPDDR4<br>eMMC<br>MicroSD</p>                                                                                                                                                                                                                                  |
| Network          | 2 x RJ45                                                                                                                                                                                                                                                                    |
| Connectivity     | <p>2 x USB 3.0 *<br>Mini PCIe<br>M.2<br>SIM card slot</p>                                                                                                                                                                                                                   |
| Media            | <p>HDMI 2.0 out **<br>MIPI-DSI<br>2 x MIPI-CSI ***<br>Digital audio (Riser interface FPC connector)<br><br>Onboard audio codec</p>                                                                                                                                          |
| I/O              | <p>1 x Reset button<br>1 x Configurable push button<br>MikroBus click interface<br>3 x LED indicators<br>RTC</p>                                                                                                                                                            |
| OS Support       | Linux                                                                                                                                                                                                                                                                       |
| Environment      | <p>Commercial:<br>Ambient temp.: 0°C to 70°C<br>Enclosed ambient temp.: 0°C to 40°C<br>CPU max die: 105°C<br><br>Industrial:<br>Ambient temp.: -40°C to 85°C<br>Enclosed Ambient temp.: -25°C to 65°C<br>CPU max die: 105°C<br><br>Humidity (non-condensing): 10% – 90%</p> |
| Dimensions       | <p>Board: 102mm x 69mm<br>Enclosed: 141.5 x 78 x 30mm</p>                                                                                                                                                                                                                   |
| Power            | <p>7V – 28V wide range<br>PoE sink support</p>                                                                                                                                                                                                                              |
| Enclosure        | Optional extruded aluminum (IP32) enclosure                                                                                                                                                                                                                                 |
|                  | [Buy Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22\&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)                                                                                                                            |

{% hint style="info" %}
Supported with i.MX8M-PLUS SOM. For more detailed information about our SOM-i.MX8M series please visit this user manual : [i.MX8M Plus SOM Hardware User Manual](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493766) .
{% endhint %}


{% hint style="info" %}
**Please note** (\*) Only USB 2.0 supported with the i.MX8M Mini SoC.\
(\*\*) Only supported with the i.MX8M SoC.\
(\*\*\*) Only 1 x MIPI-CSI supported with the i.MX8M Mini SoC.
{% endhint %}


#### Block Diagram

The following figure describes the i.MX8M Plus Block Diagram.

![](../../../../.gitbook/assets/image-20211107-104502.png)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Pulse.

![](<../../../../.gitbook/assets/HummingBoard Pulse layout (2)-20221207-195839.png>)

Print side connector overview of the HummingBoard Pulse.

![](<../../../../.gitbook/assets/HummingBoard Pulse layout (1)-20221207-195811.png>)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard Pulse with SOM
* 12V Power adapter (HummingBoard Pulse has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
* Micro USB to USB for console, the HummingBoard Pulse has an onboard FTDI chip.
* IP router or IP switch

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. On first use microSD is recommended source, configure dip switch S3 as follows:

| **Function/Switch** | **1** | **2** | **3** | **4** | **5** | **6** |
| ------------------- | ----- | ----- | ----- | ----- | ----- | ----- |
| microSD             | ON    | ON    | X     | X     | X     | X     |

“X” means don’t care, leave as is.

For additional options, please refer to [i.MX8M Series HummingBoard Boot Select](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287343073) page.

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![](../../../../.gitbook/assets/image-20240107-134703.png)

{% hint style="info" %}
Please Note: The black rectangle represents the switch position.
{% endhint %}


Once you set the switches, you can apply the following for booting from an SD card.

**1. Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX8/imx8mp_build/build_date_20240617-rev_87b97f9/imx8mp-sdhc-debian-87b97f9.img.xz
```

* For more Debian releases, please visit [Debian Release for i.MX8](https://images.solid-run.com/IMX8/imx8mp_build).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc imx8mp-sdhc-debian-87b97f9.img.xz | sudo dd of=/dev/sdX bs=4k conv=fdatasync status=progress
```

* For more information, please visit [Flashing an SD Card](https://solidrun.atlassian.net/wiki/spaces/developer/pages/288129025) .

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![](<../../../../.gitbook/assets/image-20210926-110202 (3).png>)

* In order to be able to log in , please insert “root” as a username and password as follows:

![](<../../../../.gitbook/assets/image-20210926-110919 (3).png>)

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

![image-20241203-154508.png](../../../../.gitbook/assets/image-20241203-154508.png)

![image-20241203-154758.png](../../../../.gitbook/assets/image-20241203-154758.png)

![image-20241203-154958.png](../../../../.gitbook/assets/image-20241203-154958.png)

In the end you should see with “lsblk” that the partition size is in the required size.

## More Features

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).\
Models HummingBoard with WiFi, can be connected via [WiFi](../cubox-m-quick-start-guide.md#wifi) or wired Ethernet.

* Please check you Ethernet connection.
* Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

* For more detailed information, please refer to [i.MX8M Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) .

**WiFi**

* You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1\. To bring a WiFi interface up, run the following :

```
ifconfig wlan0 up 
```

{% hint style="info" %}
To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).
{% endhint %}


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

{% hint style="info" %}
Check your personal ssids by running : ‘iw dev wlan0 scan’
{% endhint %}


5\. Make sure it works:

Restart your device and it should connect to the wireless network. If it doesn't, repeat above steps or get help from an adult.

* For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

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

* Start by scanning for other Bluetooth devices:

```
hcitool scan
```

* Choose a MAC address and connect :

```
rfcomm connect 0  $MAC 10 & 
```

* You can check the communication between the devices by writing :

```
l2ping -c 4  $MAC
```

#### GPIO Pins Control

In order to be able to control the GPIO pins, please refer to [GPIO Pins Control - HummingBoard Pulse/Mate & i.MX8M Plus SOM](https://solidrun.atlassian.net/wiki/spaces/developer/pages/396197889)

#### Enable the MINI-PCIe slot ‘J20’

![](../../../../.gitbook/assets/image-20211227-160646.png)

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

{% hint style="info" %}
**Please Note** mPCIe interface doesn't support PCIe interface - it supports USB 3.0 only.
{% endhint %}


#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

* For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

#### Enable the M.2 slot ‘M1’

![](../../../../.gitbook/assets/image-20211229-214652.png)

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

#### SPI

For testing you serial peripheral interface - SPI, please see this documentation [SPI from Linux with spidev](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/321880065?draftShareId=ac699b08-ef2b-4682-9832-b012e01aeef0).

#### Audio

First, you need to check that the required device is the default one by run:

```
$ aplay -L
```

If the sysdefault:CARD doesn’t set to wm8904 like this example

![](../../../../.gitbook/assets/image-20231126-094246.png)

Then you can play sound with choosing the device who set to wm8904 and generate audio, in the above situation the device is hw:CARD=wm8904audio so the test will work as this:

```
$ speaker-test -D hw:CARD=wm8904audio -t sine -c 2 -f 1000 -l 5
```

* NOTE: the “ -c “ flag used to set the number of the channels that you have in your audio output device, in my example I have 2 channels.

If the sysdefault:CARD=wm8904 you can test with this command:

```
$ speaker-test -t sine -f 1000 -l 5  
```

**GUI On Debian**

There is an option with the **Debian** image, up to the user, to work with a GUI like Weston, GNOME and etc.\
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

NOTE: ‘gnome-session’ is an example of gnome that we can work with, you can replace the ‘session' with another GNOME extention. 3. Start your GNOME GUI.

```
$ sudo systemctl start gdm
```

* For logging in you need a user on your device to log into it. You can create one before step 3 by this command (replace the ‘username’ with name that you want) :

```
$ sudo adduser username
```

* You can jump between GUIs that you install (like gnome-session) by the setting button that locates in the down right corner of the home screen.

#### Basler Camera

For getting started with the Camera Module on your board, please see this documentation [Basler Camera Quick Start Guide](https://solidrun.atlassian.net/wiki/spaces/developer/pages/315588609).

## TLV EEPROM Support

Starting from April 01. 2022, the EEPROMs on Carriers, i.MX8M Plus SoMs are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. Check our [iMXMP EEPROM documentation](https://solidrun.atlassian.net/wiki/spaces/developer/pages/344883516) for additional information.

## MAC Address

There are two options for storing MAC addresses on the i.MX8MP platform:

1. **Store the MAC address in OTP eFuses**

* This is a **non-reversible action**, as the eFuse is permanently programmed.

2. **Store the MAC address in EEPROM using TLV format** (Recommended)

* This method allows flexibility and is the preferred approach.
* [Guidelines](../imx8m-other-articles/imx8mp-eeprom-programming-tlv.md#progammring-mac-address) for Programming a MAC Address in TLV Format

**Default Configuration**

* By default, the MAC address is stored in the SOM's TLV EEPROM.
* All SOMs are pre-flashed with SolidRun's default MAC address range in the TLV EEPROM.

**Custom MAC Address Option**

* There is an option to provide a custom MAC address range.
* SolidRun can program the custom MAC addresses into the TLV EEPROM upon request.

## List Of Supported OS

| **OS**                                                           |                                                                                    |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| ![](<../../../../.gitbook/assets/image-20211024-150854 (1).png>) | [Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) |
| ![](<../../../../.gitbook/assets/image-20211024-151110 (2).png>) | [Yocto](https://github.com/SolidRun/meta-solidrun-arm-imx8/tree/zeus-imx8mp)       |
| ![](<../../../../.gitbook/assets/image-20211024-150920 (1).png>) | [Buildroot](https://github.com/SolidRun/imx8mp_build)                              |

## Build from source

* [i.MX8M Software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197493777)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                                                                     | File                                                                                                                                                     | Modified                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-7d65026d-7eac-46f9-82b3-30da646c3efe">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard-Pulse-Part-Assembly.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>      | ZIP Archive [HummingBoard-Pulse-Part-Assembly.zip](../../../../wiki/download/attachments/262144001/HummingBoard-Pulse-Part-Assembly.zip)                 | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-0ae43a4a-05cc-4237-8292-74eb184c2be7">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard+iMX8+Schematics.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>          | ZIP Archive [HummingBoard iMX8 Schematics.zip](../../../../wiki/download/attachments/262144001/HummingBoard%20iMX8%20Schematics.zip)                     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-550ae301-1732-4520-bb32-892f1e14cc97">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard+iMX8+Mechanical+Drawings.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | ZIP Archive [HummingBoard iMX8 Mechanical Drawings.zip](../../../../wiki/download/attachments/262144001/HummingBoard%20iMX8%20Mechanical%20Drawings.zip) | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-35851a60-0e75-4f54-98a0-85fb436c8eb3">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard+Puls-REV.2.5-pcb.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>         | ZIP Archive [HummingBoard Puls-REV.2.5-pcb.zip](../../../../wiki/download/attachments/262144001/HummingBoard%20Puls-REV.2.5-pcb.zip)                     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-7afebff7-2b6c-4f04-9d53-c3e28492618e">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard+iMX8+PCB.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                 | ZIP Archive [HummingBoard iMX8 PCB.zip](../../../../wiki/download/attachments/262144001/HummingBoard%20iMX8%20PCB.zip)                                   | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-aa9593bf-1e3c-4cd2-856a-4f8e53d89c29">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard+iMX8+Gerbers.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>             | ZIP Archive [HummingBoard iMX8 Gerbers.zip](../../../../wiki/download/attachments/262144001/HummingBoard%20iMX8%20Gerbers.zip)                           | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-0c2242aa-8be3-431e-9273-168282639208">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HummingBoard+Pulse+Pin+MUX.xlsx">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>           | Microsoft Excel Spreadsheet [HummingBoard Pulse Pin MUX.xlsx](../../../../wiki/download/attachments/262144001/HummingBoard%20Pulse%20Pin%20MUX.xlsx)     | Dec 26, 2021 by [SolidRun](../../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-pulse-imx8m-plus-som-quick-start-guide.md#section-7e9733e2-59ca-47d3-b149-39c542b0e841">Edit Labels</a><br><br>[Preview] <a href="../../../../wiki/download/attachments/262144001/HS00016-Heatsink.zip">View</a> <a href="../../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                      | ZIP Archive [HS00016-Heatsink.zip](../../../../wiki/download/attachments/262144001/HS00016-Heatsink.zip)                                                 | Jul 15, 2024 by [Yazan Shhady](../../../../wiki/people/5f67bce9ed55c7006abc6319/)                |

[Download All](../../../../wiki/download/all_attachments)

[Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22\&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
