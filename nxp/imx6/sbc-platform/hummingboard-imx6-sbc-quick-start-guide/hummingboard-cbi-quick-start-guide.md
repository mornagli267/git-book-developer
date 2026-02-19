# HummingBoard CBi Quick Start Guide

![](<../../../../.gitbook/assets/HummingBoard CBi sideways (small).png>)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Revision** | **Notes**       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 14 Nov 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1.0          | Initial release |
| Table of Contents | <p>- <a href="hummingboard-cbi-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#booting-form-an-sd-card">Booting form an SD card</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#canbus-and-rs485-support">CanBUS and RS485 Support</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#initial-setup">Initial Setup</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#canbus-enable">CanBUS Enable</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#rs485-enable">RS485 Enable</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#install-to-emmc">Install to eMMC</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#wi-fi">Wi-fi</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#cellular-modem">Cellular Modem</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#gpio-pins-control">GPIO pins Control</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#canbus-and-rs485-test">CanBUS and RS485 Test</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#build-u-boot-kernel-from-sources">Build U-Boot &#x26; Kernel from sources</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-cbi-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Introduction

The following quick start guide provides background information about the [HummingBoard CBi](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx6-family/hummingboard/#cbi) product which use the i.MX6 System on module.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Hardware Setup

#### Product Specifications

|                      |                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SOM Model**        | NXP i.MX6 based Solo to Quad Core SOM                                                                                                                             |
| **Processor**        | i.MX6 Solo – Quad core ARM Cortex A9 up to 800Mhz                                                                                                                 |
| **Memory & Storage** | Up to 2GB DDR3                                                                                                                                                    |
|                      | uSD, eMMC (8GB), M.2 (2242)                                                                                                                                       |
| **Network**          | 1 x RJ45                                                                                                                                                          |
| **Connectivity**     | 1 x CAN bus                                                                                                                                                       |
|                      | 1 x RS485                                                                                                                                                         |
|                      | 4 x USB 2.0                                                                                                                                                       |
|                      | Mini PCIe                                                                                                                                                         |
|                      | M.2                                                                                                                                                               |
|                      | SIM card slot                                                                                                                                                     |
| **Media**            | LVDS                                                                                                                                                              |
|                      | MIPI-DSI                                                                                                                                                          |
|                      | MIPI-CSI-2                                                                                                                                                        |
| **I/O**              | 1 x Reset button                                                                                                                                                  |
|                      | 1 x Configurable push button                                                                                                                                      |
|                      | 3 x LED indicators                                                                                                                                                |
|                      | RTC                                                                                                                                                               |
|                      | IR reciver                                                                                                                                                        |
| **OS Support**       | Linux                                                                                                                                                             |
| **Dimensions**       | 102mm x 69mm                                                                                                                                                      |
| **Power**            | 7V – 36V wide range                                                                                                                                               |
| **Environment**      | Metal Enclosure                                                                                                                                                   |
|                      | [Buy Now](https://shop.solid-run.com/product-category/embedded-computers/nxp-family/hummingboard-cbi/?_ga=2.88522648.2016484779.1641802897-2012112798.1622706355) |

{% hint style="info" %}
Supported with i.MX6 SOM. For more detailed information about our SOM-i.MX6 series please visit this user manual : [i.MX6 SOM Hardware User Manual](/nxp/imx6/com-som/imx6-som-hardware-user-manual.md) .
{% endhint %}


#### **Block Diagram**

The following figure describes the Hummingboard CBi Block Diagram.

![](<../../../../.gitbook/assets/HummingBoard CBi block diagram (1)-20211114-110600.png>)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard CBi.

![](../../../../.gitbook/assets/image-20211114-110715.png)

Print side connector overview of the HummingBoard CBi.

![](../../../../.gitbook/assets/image-20211114-110741.png)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up the board:

* Linux or Windows PC
* HummingBoard CBi with SOM
* 12V Power adapter (HummingBoard CBi has wide range input of 9V-36V, it is recommended to use 12V power adapter)
* USB to UART cable
* IP router or IP switch

## Booting form an SD card

On the HummingBoard CBi it is possible to boot from different media.

For Booting from an SD card, jumpers need to be setup at J5005 as follows:

![](../../../../.gitbook/assets/image-20211114-094820.png)

{% hint style="info" %}
Before you set the boot jumpers, please refer to [HummingBoard Edge/Gate Boot Jumpers](../imx6-other-articles/hummingboard-edge-gate-boot-jumpers.md) for more information about J5005.
{% endhint %}


Once you setup the jumpers, you can apply the following for booting from an SD card.

**1. Downloading the Debian image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/IMX6/Debian/sr-imx6-debian-bullseye-20220712-cli-sdhc.img.xz
```

* For more Debian releases, please visit [Debian Release](https://images.solid-run.com/IMX6/Debian).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
xz -dc sr-imx6-debian-bullseye-20220712-cli-sdhc.img.xz | dd of=/dev/sdX bs=4M conv=fsync
```

* For more information, please visit [Flashing an SD Card](/other-articles/flashing-an-sd-card.md) .

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5. Serial connection**

Please connect the UART cable to the pins on connector J25 as shown in the below picture, then you can refer to [Serial Connection](/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

![](../../../../.gitbook/assets/image-20211114-100743.png)

{% hint style="info" %}
For more information about J25 connector, please refer to [HummingBoard Gate/Edge UART console](../imx6-other-articles/hummingboard-gate-edge-uart-console.md) .
{% endhint %}


Once you installed the necessary serial connection software, please run the following:

```
setenv som_rev 'V15'; saveenv; boot 
```

And you should be able to see the following:

![](../../../../.gitbook/assets/image-20210926-110202.png)

* In order to be able to log in , please insert “debian” as a username and password as follows:

![](../../../../.gitbook/assets/image-20210926-110919.png)

## CanBUS and RS485 Support

#### **Initial Setup**

HummingBoard CBi can use the CAN-Bus and RS485 only if booted with the appropriate device-tree. From U-Boot console, interrupt boot by pressing any key during the Hit any key to stop autoboot prompt. Then permanently choose the cbi device-tree variant:

```
Hit any key to stop autoboot:  0
=> setenv is_cbi 1
=> saveenv
=> reset
```

**Use the following commands in order to keep your system up-to-date:**

```
apt-get update 
apt-get upgrade 
reboot
```

#### CanBUS Enable

1\. Download the compressed zip file:

```
sudo wget https://developer.solid-run.com/wp-content/uploads/2021/12/hb-cbi-dtbs-k5.10.zip -O /tmp/hb-cbi-dtbs-k5.10.zip
```

2\. Unzip the file:

```
unzip -o /tmp/hb-cbi-dtbs-k5.10.zip -d /boot/dtbs/5.10.0-8-armmp/
```

3\. Restart your device:

```
reboot
```

#### RS485 Enable

1\. Add a support for rs485conf and compile an exec file by runnig the following:

```
git clone https://github.com/mniestroj/rs485conf.git
cd rs485conf
make
```

{% hint style="info" %}
Before you run the above, please install some helping commands by running: `apt-get install make gcc git`
{% endhint %}


2\. Copy the output of the exec file bu running:

```
cp rs485conf /usr/bin/
```

3\. Add an execute permission to the file:

```
 chmod +x /usr/bin/rs485conf
```

## Install to eMMC

* You can follow this document [Install to eMMC](https://github.com/SolidRun/documentation/blob/bsp/imx6/debian-11_sr1.md#install-to-emmc) to install debian to an eMMC device.

## More Features

#### Internet

* Please check you Ethernet connection.
* Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

* For more detailed information, please refer to [i.MX6 Debian](/nxp/imx6/sbc-platform/imx6-software/imx6-debian.md) .

**Wi-fi**

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

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

* For some cellular modules to be connected, please refer to [Cellular Modules](/nxp/imx6/sbc-platform/imx6-other-articles/cellular-modules.md).

#### GPIO pins Control

In order to be able to control the GPIO pins, please refer to [HummingBoard Edge/Gate/CBi GPIO Pins Control](../imx6-other-articles/hummingboard-edge-gate-cbi-gpio-pins-control.md) .

## CanBUS and RS485 Test

For testing your CANBus and RS-485 interfaces, please refer to [HummingBoard CBi RS485 and CAN bus](/nxp/imx6/sbc-platform/imx6-other-articles/hummingboard-cbi-rs485-and-can-bus.md) .

## List Of Supported OS

| **OS**                                                     |                                                                                         |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| ![](../../../../.gitbook/assets/image-20211223-104106.png) | [i.MX6 Debian](/nxp/imx6/sbc-platform/imx6-software/imx6-debian.md)    |
| ![](../../../../.gitbook/assets/image-20211223-104124.png) | [Yocto for i.MX6](/nxp/imx6/sbc-platform/imx6-software/yocto-for-imx6.md) |
| ![](../../../../.gitbook/assets/image-20211223-104144.png) | [i.MX6 Archlinux](/nxp/imx6/sbc-platform/imx6-software/imx6-archlinux.md) |
| ![](../../../../.gitbook/assets/image-20211223-104259.png) | [XBian for i.MX6](/nxp/imx6/sbc-platform/imx6-software/xbian-for-imx6.md) |

## Build U-Boot & Kernel from sources

* Build a Linux kernel -  [i.MX6 Kernel](/nxp/imx6/sbc-platform/imx6-software/imx6-kernel.md)
* Build a U-Boot - [i.MX6 U-Boot](/nxp/imx6/sbc-platform/imx6-software/imx6-u-boot.md)

## Documentation

{% file src="attachments/HummingBoard2%20Assembly-Files.zip" %}
{% file src="attachments/HummingBoard2%20Enclosure-Files.zip" %}
{% file src="attachments/HummingBoard2-v1.4-layout_pcb.zip" %}
{% file src="attachments/HummingBoard2-gerber-rev1.2.zip" %}
{% file src="attachments/HummingBoard2%20PCB%20parts%20assembly%20Rev%201.4.zip" %}
{% file src="attachments/HummingBoard2%20Schematics.pdf" %}



[Buy a Sample Now](https://shop.solid-run.com/product-category/embedded-computers/nxp-family/hummingboard-cbi/?_ga=2.88522648.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
