# CuBox-i Quick Start Guide

![](../../../.gitbook/assets/new-cubox-md-768x740-20211021-095706.png)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Revision** | **Notes**       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 26 Sep 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1.0          | Initial release |
| Table of Contents | <p>- <a href="cubox-i-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="cubox-i-quick-start-guide.md#introduction">Introduction</a><br>- <a href="cubox-i-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="cubox-i-quick-start-guide.md#product-specifications">Product Specifications</a><br>- <a href="cubox-i-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="cubox-i-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="cubox-i-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="cubox-i-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="cubox-i-quick-start-guide.md#booting-form-an-sd-card">Booting form an SD card</a><br>- <a href="cubox-i-quick-start-guide.md#more-features">More Features</a><br>- <a href="cubox-i-quick-start-guide.md#internet">Internet</a><br>- <a href="cubox-i-quick-start-guide.md#wi-fi">Wi-fi</a><br>- <a href="cubox-i-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="cubox-i-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="cubox-i-quick-start-guide.md#build-u-boot-kernel-from-sources">Build U-Boot &#x26; Kernel from sources</a><br>- <a href="cubox-i-quick-start-guide.md#documentation">Documentation</a><br>- <a href="cubox-i-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Introduction

The following quick start guide provides background information about the [CuBox-i](https://www.solid-run.com/fanless-computers/cubox/#cubox-i).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Hardware Setup

#### Product Specifications

|                                      |                                                                                                        |                                                                                                        |                                                                                                        |                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Model**                            | CuBox i1                                                                                               | CuBox i2                                                                                               | CuBox i2eX                                                                                             | CuBox i4P                                                                                              |
| **I/Os**                             | <p>2 x USB 2.0<br>1 x eSATA</p>                                                                        | <p>2 x USB 2.0<br>1 x eSATA</p>                                                                        | <p>2 x USB 2.0<br>1 x eSATA</p>                                                                        | <p>2 x USB 2.0<br>1 x eSATA</p>                                                                        |
| **Networking**                       | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)</p> | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)</p> | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)</p> | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)</p> |
| **Processor**                        | NXP i.MX 6 Single core Arm Cortex A9 up to 1GHz                                                        | NXP i.MX 6 Dual Lite core Arm Cortex A9 up to 1GHz                                                     | NXP i.MX 6 Dual core Arm Cortex A9 up to 1GHz                                                          | NXP i.MX 6 Quad core Arm Cortex A9 up to 1GHz                                                          |
| **Memory & Storage**                 | <p>512MB DDR3<br>8GB eMMC<br>MicroSD</p>                                                               | <p>1GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                 | <p>1GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                 | <p>2GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                 |
| **Display**                          | HDMI                                                                                                   | HDMI                                                                                                   | HDMI                                                                                                   | HDMI                                                                                                   |
| **Misc.**                            | <p>Reset button<br>RTC<br>IR reciver</p>                                                               | <p>Reset button<br>RTC<br>IR reciver</p>                                                               | <p>Reset button<br>RTC<br>IR reciver</p>                                                               | <p>Reset button<br>RTC<br>IR reciver</p>                                                               |
| **Development and Debug interfaces** | Micro USB                                                                                              | Micro USB                                                                                              | Micro USB                                                                                              | Micro USB                                                                                              |
| **Power**                            | 5V                                                                                                     | 5V                                                                                                     | 5V                                                                                                     | 5V                                                                                                     |
| **Expansion card I/Os**              | None                                                                                                   | None                                                                                                   | None                                                                                                   | None                                                                                                   |
| **Temperature**                      | Commercial: 0°C to 40°C                                                                                | Commercial: 0°C to 40°C                                                                                | Commercial: 0°C to 40°C                                                                                | Commercial: 0°C to 40°C                                                                                |
| **Dimensions**                       | 50 x 50 x 50mm                                                                                         | 50 x 50 x 50mm                                                                                         | 50 x 50 x 50mm                                                                                         | 50 x 50 x 50mm                                                                                         |
| **Enclosure**                        | ABS Plastic                                                                                            | ABS Plastic                                                                                            | ABS Plastic                                                                                            | ABS Plastic                                                                                            |

[Buy a Sample Now](https://shop.solid-run.com/product-category/embedded-computers/nxp-family/cubox-i/?_ga=2.159864382.2016484779.1641802897-2012112798.1622706355https://shop.solid-run.com/product-category/embedded-computers/nxp-family/cubox-i/?_ga=2.159864382.2016484779.1641802897-2012112798.1622706355)

{% hint style="info" %}
Supported with i.MX6 SOM. For more detailed information about our SOM-i.MX6 series please visit this user manual : [i.MX6 SOM Hardware User Manual](/nxp/imx6/com-som/imx6-som-hardware-user-manual.md).
{% endhint %}


#### Block Diagram

The following figure describes the i.MX6 Block Diagram.

![](../../../.gitbook/assets/image-20210926-130003.png)

#### Visual features overview

![](../../../.gitbook/assets/image-20211024-141057.png)

![](../../../.gitbook/assets/14497284277_d1eb13c8d7_o.png)

* A demonstration of how to connect your cables and other peripherals to your CuBox-i can be found here : [How to connect cables and peripherals to your CuBox-i](https://youtu.be/o7M4BL6nLTY)

## Software Setup

#### Cable setup and prerequisites

* Micro USB cable
* Power supplier : regulated 5V supply with 2A source capacity (3A for CuBox-i4pro)
* Micro SD card
* Linux or Windows PC
* Router or switch with Ethernet cable

{% hint style="warning" %}
Note that using an adaptor with an output voltage which is higher than 5V will damage your device and possibly other connected USB devices.
{% endhint %}


## Booting form an SD card

**1. Downloading the Yocto image**

Download the Yocto image by running the following command on your Linux/Windows PC:

```
wget https://images.solid-run.com/IMX6/meta-solidrun-arm-imx6/2024-07-05_ab67695/core-image-weston-sdk-imx6qdlcubox.wic.gz
```

* For other software releases, please visit [images.solid-run.com/IMX6](https://images.solid-run.com/IMX6).

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
gzip -dc core-image-weston-sdk-imx6qdlcubox.wic.gz | dd of=/dev/sdX bs=4M conv=fsync
```

* For more information, please visit [Flashing an SD Card](/other-articles/flashing-an-sd-card.md) .

{% hint style="info" %}
Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

{% hint style="success" %}
A red LED will light up at the front panel. This is an indication of boot loader firmware is running.If you find you need additional help, please contact us and we’ll do our best to get back to you with more personal support.
{% endhint %}


**5. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see a log-in prompt similar to the following:

![](<../../../.gitbook/assets/image-20210926-110202 (1).png>)

* In order to be able to log in , please insert “root” as a username, password is empty:

![](<../../../.gitbook/assets/image-20210926-110919 (1).png>)

## More Features

#### Internet

If you have purchased CuBox-i1 or CuBox-i2 first connect an Ethernet cable to your CuBox-i (for internet access during boot-up). Models CuBox-i2ex and CuBox-i4Pro (Or CuBox i1 / i2 with WiFi function), can be connected via Wi-Fi or wired Ethernet.

* Please check you Ethernet connection.

**Wi-fi**

* You can connect to WiFi using any application, such as : [connmanctl](https://wiki.archlinux.org/title/ConnMan#wi-fi) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant)
* TLDR Connecting to WiFi network using connman:

```
root@imx6qdlcubox:~# connmanctl 
connmanctl> enable wifi
Enabled wifi
connmanctl> scan wifi
Scan completed for wifi
connmanctl> services
    Vodafone Hotspot     wifi_10cea9c83c04_566f6461666f6e6520486f7473706f74_managed_none
    Vodafone-guest       wifi_10cea9c83c04_566f6461666f6e652d6775657374_managed_psk
    ...
connmanctl> agent on
Agent registered
connmanctl> connect wifi_10cea9c83c04_566f6461666f6e652d6775657374_managed_psk
Agent RequestInput wifi_10cea9c83c04_566f6461666f6e652d6775657374_managed_psk
  Passphrase = [ Type=psk, Requirement=mandatory ]
Passphrase? super-secret-pw
Connected wifi_10cea9c83c04_566f6461666f6e652d6775657374_managed_psk
connmanctl> quit
root@imx6qdlcubox:~# ping google.com
PING google.com (216.58.206.46): 56 data bytes
64 bytes from 216.58.206.46: seq=0 ttl=118 time=13.097 ms
...
```

#### Bluetooth

1. For showing all Bluetooth devices, run the following:

```
hciconfig -a
```

2\. Choose a device, and turn it on:

```
rfkill unblock bluetooth
hciconfig hci0 up
```

3.Set up the Bluetooth name:

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

## List Of Supported OS

| **OS**                                                        |                                                                                         |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| ![](<../../../.gitbook/assets/image-20211223-104106 (1).png>) | [i.MX6 Debian](/nxp/imx6/sbc-platform/imx6-software/imx6-debian.md)    |
| ![](<../../../.gitbook/assets/image-20211223-104124 (1).png>) | [Yocto for i.MX6](/nxp/imx6/sbc-platform/imx6-software/yocto-for-imx6.md) |
| ![](<../../../.gitbook/assets/image-20211223-104144 (1).png>) | [i.MX6 Archlinux](/nxp/imx6/sbc-platform/imx6-software/imx6-archlinux.md) |
| ![](<../../../.gitbook/assets/image-20211223-104259 (1).png>) | [XBian for i.MX6](/nxp/imx6/sbc-platform/imx6-software/xbian-for-imx6.md) |

## Build U-Boot & Kernel from sources

* Build a Linux kernel -  [i.MX6 Kernel](/nxp/imx6/sbc-platform/imx6-software/imx6-kernel.md)
* Build a U-Boot - [i.MX6 U-Boot](/nxp/imx6/sbc-platform/imx6-software/imx6-u-boot.md)

## Documentation

* [cubox-i-plastic-model.zip](attachments/cubox-i-plastic-model.zip)
* [CuBox-I schematics.pdf](attachments/CuBox-I%20schematics.pdf)



[Buy a Sample Now](https://shop.solid-run.com/product-category/embedded-computers/nxp-family/cubox-i/?_ga=2.159864382.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
