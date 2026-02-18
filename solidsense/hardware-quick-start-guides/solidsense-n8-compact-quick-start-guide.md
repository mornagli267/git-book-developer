# SolidSense N8 Compact Quick Start Guide

## SolidSense N8 Compact Quick Start Guide

![](../../../.gitbook/assets/image-20211219-084743.png)

### Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Revision** | **Notes**                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------- |
| 19 Dec 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1.0          | Initial release                                                                         |
| 02 Oct 2024       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1.1          | Adding documentation of additional details on SKU descriptions and sink specifications. |
| Table of Contents | <p>- <a href="solidsense-n8-compact-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="solidsense-n8-compact-quick-start-guide.md#introduction">Introduction</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#solidsensen8compactquickstartguide-mainfeatures">Main features</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#hardware-setup">Hardware Setup</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#product-specifications">Product Specifications</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#visual-features-overview">Visual features overview</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#power-connection">Power Connection</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#network-configuration">Network Configuration</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#sink-nina-b1-or-fwm7blz22">Sink Nina-B1 or FWM7BLZ22</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#sink-pinout">Sink Pinout</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#pin-module">Pin / Module</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#nina-b1">Nina-B1</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#fwm7blz22">FWM7BLZ22</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#nina-b1-circuit">Nina-B1 Circuit</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#fwm7blz22-circuit">FWM7BLZ22 Circuit</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#wirepas-firmware">Wirepas Firmware</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#ble-firmware">BLE Firmware</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#sink-device-uart4">Sink Device - UART4</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#canbus-and-rs485">CanBus and RS485</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#graceful-boot-application">Graceful Boot Application</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#hardware-used-by-application">Hardware used by application</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#how-the-application-works">How the application works</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#modifying-the-application">Modifying the application</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#kernel-part">Kernel part</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#u-boot-part">U-boot part</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#cover-removal">Cover Removal</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#hardware-interfaces">Hardware interfaces</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#boot-select">Boot Select</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#serial-connection">Serial connection</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#booting-debian-from-sd-card">Booting Debian from SD card</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#build-from-sources">Build from sources</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#support">Support</a><br><br>- <a href="solidsense-n8-compact-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                                                                                         |

### Introduction

The following quick start guide provides background information about the [SolidSense N8 Compact.](https://www.solid-run.com/edge-gateway-solidsense/#iot-compacthttps-wwwsolid-runcom-edge-gateway-solidsense-iot-compact)

SolidSense N8 IoT Compact Edge Gateway is an enterprise Internet of Things gateway designed for servicing a local network of IoT devices with a range of solutions and business applications. SolidSense is the ultimate IoT M2M solution, with high-end connectivity options.

Based on NXP i.MX8M Nano processors, , SolidSense is a feature-rich edge platform designed to provide flexibility for developers and OEMs in implementing an almost endless range of IoT solutions.

## Main features

SoC: NXP i.MX 8M Nano Arm Cortex A53 Single core @1500MHz + Cortex M7@650MHz\
Memory: 1GB DDR4\
Storage: 8GB eMMC\
Temperature: Commercial (0C to 50C)\
OS: Linux

### Hardware Setup

**Product Specifications**

|                                  | <p><strong>SolidSense N8 IoT Compact BLE</strong><br>SRG0401.0<strong>X</strong>SY {x=1,2; Y=D,W}</p> | <p><strong>SolidSense N8 IoT Compact LTE BLE</strong><br>SRG0402.0<strong>X</strong>SY {x=1,2; Y=D,W}</p>                                      | <p><strong>SolidSense N8 IoT Compact Extended</strong><br>SRG0403.0<strong>X</strong>SY {x=1,2; Y=D,W}</p> | <p><strong>SolidSense N8 IoT Compact Extended LTE</strong><br>SRG0404.0<strong>X</strong>SY {x=1,2; Y=D,W}</p>                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| I/Os                             | <p>1 x USB 2.0<br>1 x BLE 5.0 (SDR based on nRF52832 – Wirepas Compatible)</p>                        | <p>1 x USB 2.0<br>1 x BLE 5.0 (SDR based on nRF52832 – Wirepas Compatible)</p>                                                                 | <p>1 x RS485<br>1 x CAN<br>1 x USB 2.0</p>                                                                 | <p>1 x RS485<br>1 x CAN<br>1 x USB 2.0</p>                                                                                                     |
| Networking                       | <p>1 x Ethernet RJ45 10/100/1000<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth 5.0</p>                  | <p>1 x Ethernet RJ45 10/100/1000<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth 5.0<br>1 x LTE Cat 4 Worldwide + GPS (with fallback on 3G/2G)</p> | <p>1 x Ethernet RJ45 10/100/1000<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth 5.0</p>                       | <p>1 x Ethernet RJ45 10/100/1000<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth 5.0<br>1 x LTE Cat 4 Worldwide + GPS (with fallback on 3G/2G)</p> |
| Processor                        | NXP i.MX 8M Nano Arm Cortex A53 Single core @1500MHz + Cortex M7@650MHz                               | NXP i.MX 8M Nano Arm Cortex A53 Single core @1500MHz + Cortex M7@650MHz                                                                        | NXP i.MX 8M Nano Arm Cortex A53 Single core @1500MHz + Cortex M7@650MHz                                    | NXP i.MX 8M Nano Arm Cortex A53 Single core @1500MHz + Cortex M7@650MHz                                                                        |
| Memory & Storage                 | <p>1GB DDR4<br>8GB eMMC<br>MicroSD</p>                                                                | <p>1GB DDR4<br>8GB eMMC<br>MicroSD</p>                                                                                                         | <p>1GB DDR4<br>8GB eMMC<br>MicroSD</p>                                                                     | <p>1GB DDR4<br>8GB eMMC<br>MicroSD</p>                                                                                                         |
| Misc.                            | <p>Programmable LEDs<br>Supercap protection<br>RTC w/ battery</p>                                     | <p>Programmable LEDs<br>Supercap protection<br>RTC w/ battery</p>                                                                              | <p>Programmable LEDs<br>Supercap protection<br>RTC w/ battery</p>                                          | <p>Programmable LEDs<br>Supercap protection<br>RTC w/ battery</p>                                                                              |
| Development and Debug interfaces | Console port (internal)                                                                               | Console port (internal)                                                                                                                        | Console port (internal)                                                                                    | Console port (internal)                                                                                                                        |
| Power                            | <p>9V-36V<br>PoE sink</p>                                                                             | 9V-36V                                                                                                                                         | <p>9V-36V<br>PoE sink</p>                                                                                  | 9V-36V                                                                                                                                         |
| Expansion card I/Os ( \* )       | 1 x internal expansion header                                                                         | 1 x internal expansion header                                                                                                                  | 1 x internal expansion header                                                                              | 1 x internal expansion header                                                                                                                  |
| Temperature                      | 0°C to 50°C                                                                                           | 0°C to 50°C                                                                                                                                    | 0°C to 50°C                                                                                                | 0°C to 50°C                                                                                                                                    |
| Dimensions                       | 150 x 85 x 40mm                                                                                       | 150 x 85 x 40mm                                                                                                                                | 150 x 85 x 40mm                                                                                            | 150 x 85 x 40mm                                                                                                                                |
| Enclosure                        | Plastic casing with internal antennas for WiFi-Bluetooth/BLE                                          | Plastic casing with internal antenna for WiFi-Bluetooth. One SMA port for LTE.                                                                 | Plastic casing with internal antenna for WiFi-Bluetooth                                                    | Plastic casing with internal antenna for WiFi-Bluetooth. One SMA port for LTE.                                                                 |

{% hint style="info" %}
**Please Note** (\*) Only accessible with case open.
* All **SRG40X.01SD** {X: 1, 2, 5} SKUs comes with U-Blox Nina-B1 (U-Blox comes with BLE FW by default except if you order the version with SW except SD like SRG40x.01SW **will come with Wirepass FW** )
* All **SRG40X.02SD** {X: 1, 2, 5} SKUs comes with fwm7blz22 (FWM7BLZ22 comes with BLE FW by default except if you order the version with SW except SD like SRG40x.02SW will come with Wirepass FW )
* **SRG405.02SD** = full assembled (including all options in the list...)\
-> SolidSense N8 Compact - WiFi BLE-FWM LTE POE RS485 CAN ETH-ADIN
{% endhint %}


![](<../../../.gitbook/assets/masterLayer.0003 (3).png>)

**Block Diagram**

The following figure describes the SolidSense N8 Compact Edge Block Diagram.

![](../../../.gitbook/assets/image-20211219-084606.png)

**Visual features overview**

Please see below the features overview of the front side of the product.

![](../../../.gitbook/assets/image-20211219-111337.png)

{% hint style="info" %}
**Note**\
The unit has two Dual-Band Antennas (for WIFI Module and U-Blox): RF ANT 2.4GHZ/5.4GHZ FLAT PATCH .
{% endhint %}


The system can be used in 4 ways:

1. Ready to go **SolidSense IoT platform** (SolidSense Out-Of-the-Box) with Eclipse Kura Framework and Wirepas/Bluetooth Low Energy MQTT gateways built-in applications. Configure the gateway via Kura and that’s it you can directly have your data forwarded to your cloud application.
2. Developing your own application or add-on on top of the platform. Simple additions can be developed via Python 3.7 using the pre-installed packages. For more sophisticated development, a Docker infrastructure is ready to host your containers.
3. Create your own SolidSense image derived from SolidSense OOB.
4. From bare metal. You can create your own Linux image starting from SolidRun BSP. The support for these developments are not covered in the SolidSense section.

{% hint style="success" %}
The product comes with a SolidSense built in software and ready to go.
{% endhint %}


### Power Connection

Connect your power adaptor to the DC jack (12-36 V), and then connect the adaptor to mains supply.

{% hint style="success" %}
A green LED will light up at the front panel. This is an indication of your device working.\
If it didn’t seem to be lit, then you have to press the on/off button.
{% endhint %}


### Network Configuration

For managing your IoT gateway, monitor the gateway status, and manage the network configuration, you can refer to [Configuring SolidSense networking with Kura](../solidsense-software/kura/configuring-solidsense-networking-with-kura.md) .

Please see below picture to get the serial number for SSID of the network.

![](../../../.gitbook/assets/image-20211219-160537.png)

### Sink **Nina-B1** or **FWM7BLZ22**

This module can be programmed with either Wirepas or BLE firmware.

For all SRG40X.01SD SKUs (`X`: 1, 2, 5), the device comes with a U-Blox Nina-B1 module, which includes BLE firmware by default. If ordered with the "SW" suffix instead of "SD" (e.g., SRG40X.01SW), it will come with Wirepas firmware instead.

Similarly, all SRG40X.02SD SKUs (`X`: 1, 2, 5) are equipped with an FWM7BLZ22 module, which also includes BLE firmware by default. Ordering with the "SW" suffix (e.g., SRG40X.02SW) provides the module with Wirepas firmware instead.

#### **Sink Pinout**

| <p><br><br>### <strong>Pin / Module</strong></p> | <p><br><br>### <strong>Nina-B1</strong><br><br>SKUs SRG40X.0<strong>1</strong> {X: 1, 2, 5}</p> | <p><br><br>### <strong>FWM7BLZ22</strong><br><br>SKUs SRG40X.0<strong>2</strong> {X: 1, 2, 5}</p> |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| UART\_0\_PIN\_TX                                 | 6                                                                                               | 6                                                                                                 |
| UART\_0\_PIN\_RX                                 | 5                                                                                               | 8                                                                                                 |
| UART\_0\_PIN\_RTS                                | N.C                                                                                             | N.C                                                                                               |
| UART\_0\_PIN\_CTS                                | PD                                                                                              | PD                                                                                                |

**Nina-B1 Circuit**

**FWM7BLZ22 Circuit**

#### Wirepas Firmware

If you are using SolidSense as a Wirepas gateway you can directly configure your Wirepas gateway by referring to [Configuring and testing the Wirepas gateway software](../solidsense-software/wirepas/configuring-and-testing-the-wirepas-gateway-software.md) .

For flashing or re-flashing wirepas sinks, please refer to [Flashing or Re-flashing Wirepas sinks on SolidSense gateway (V0.9 and up)](../solidsense-software/wirepas/flashing-or-re-flashing-wirepas-sinks-on-solidsense-gateway-v09-and-up.md) .

{% hint style="info" %}
When using the Solidsense software, UART4 (displayed as `/dev/ttymxc3` in Linux) should be linked to `wirepasSink1.service` for proper sink configuration on the N8 Compact.
{% endhint %}


{% hint style="info" %}
Wirepas is exclusively supported by our distribution partner [CTHINGS.CO | Edge IoT Solutions](https://cthings.co/)
{% endhint %}


#### BLE Firmware

This module supports BLE and can be programmed with BLE firmware on N8 products.\
To build and program the BLE firmware, please follow the instructions in the repository: [SolidRun BLE Firmware Guide](https://github.com/SolidRun/mynewt-sr-blehci/tree/master).\
The firmware is built on the Apache Mynewt OS, using the Apache NimBLE application to provide BLE functionality and HCI protocol support.

{% hint style="info" %}
The SRG40X.0**Y**SD SKUs (`X`: 1, 2, 5; `Y`: 1, 2) come with BLE firmware pre-programmed by default.
{% endhint %}


#### Sink Device - UART4

UART4 appears as `/dev/ttymxc3` in Linux.

### CanBus and RS485

![](../../../.gitbook/assets/image-20211219-165900.png)

**Connector Description**

![](../../../.gitbook/assets/image-20211219-164638.png)

6 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm) - 180° Free Hanging (In-Line) like this [connector](https://www.digikey.com/en/products/detail/phoenix-contact/1790111/2743737).

**CanBUS and RS485 Test**

For testing your CANBus and RS-485 interfaces, please refer to [SolidSense N8 Compact RS485 and CAN bus](../solidsense-other-articles/solidsense-n8-compact-rs485-and-can-bus.md) .

**Bluetooth**

1\. For showing all Bluetooth devices, run the following:

```
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

### Graceful Boot Application

Our source code [https://github.com/SolidRun/imx8mp\_build/tree/imx8mn](https://github.com/SolidRun/imx8mp_build/tree/imx8mn)  includes a graceful boot/reboot application which prevents corruptions of the filesystem due to power loss.

**Hardware used by application**

* 5\[F] Supercapacitor which can supply power to the board for \~10-15 seconds.
* Supercapacitor backup power manager IC.
* I/O expander, connected to the backup power manager IC.

**All these components are part of the board (if assembled).**

**How the application works**

The kernel polls the I/O expander, once the kernel detects that the external power is off (signal from the supercapacitor backup power manager IC), it throws "RESTART" keys.\
The keys are catched by input-event-daemon, then the daemon reboots the system.\
On boot, U-boot polls the I/O expander and won't boot until:

* An external power source is connected to the board.
* The capacitor charge is >90% (so it will last for the boot process, until the daemon will be started).

Once these requirement meet, U-boot will boot the system.

**If you are using our Kernel and U-boot, but you are not using our Buildroot, make sure you have a daemon to catch the thrown keys.**

**Modifying the application**

**Kernel part**

In order to remove the kernel part, remove "gpio\_keys\_polled" node from devicetree.\
The devicetree path is: `build/linux-imx/arch/arm64/boot/dts/freescale/imx8mn-compact.dts`

**U-boot part**

The default configuration for the U-boot part is checking that an external power source is connected and the capacitor charge is >90%.\
This is configured in the bootcmd environment parameter: `check_power_connection 2;`.\
The argument "2" indicates that the extenral power connection and capacitor charge should be checked.\
If you just want to check the power connection, change the argument to "1" `check_power_connection 1;`.\
If you want to cancel the power check, you can delete the check\_power\_connection part from the bootcmd environment parameter.

### Cover Removal

For removing the enclosure , please follow the below instructions:

![](../../../.gitbook/assets/image-20211219-122540.png)

1. Remove 4 rubber feet (F) from screw holes in base.
2. Remove 4 Enclosure self-tapping screw (D) tightened to Top cover bosses (E).
3. Remove Top cover (C).
4. Remove Front cover (A) and Rear cover (B).

### Hardware interfaces

Please see below the features overview of the connector side of the Compact.

![](../../../.gitbook/assets/image-20211219-085810.png)

Print side connector overview of the Compact.

![](../../../.gitbook/assets/image-20211219-085828.png)

### Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media to MicroSD, please set the S1 switch to match the first option from the following table:

|          |              |              |
| -------- | ------------ | ------------ |
|          | **Switch 1** | **Switch 2** |
| **SD**   | ON           | ON           |
| **eMMC** | OFF          | ON           |

### Serial connection

Please connect the UART cable to the pins on connector J13 as shown in the above connector side picture under HW interfaces, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

![](../../../.gitbook/assets/image-20211219-165131.png)

Once you have installed the necessary serial connection software, reset your device and you should be able to see the following:

![](../../../.gitbook/assets/image-20211223-082956.png)

* In order to be able to log in, please insert ‘**solidsense**’ as username and ‘**aiPh2eim**’ as password.

### Booting Debian from SD card

The following shows how to set the switches on the boot source selector:

|        |              |              |
| ------ | ------------ | ------------ |
|        | **Switch 1** | **Switch 2** |
| **SD** | ON           | ON           |

### List Of Supported OS

| **OS**                                                  |                                                                                                                                                      |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../../.gitbook/assets/image-20211219-112058.png) | [IMX8M Nano Compact - Yocto](../../iot-industrial-product-line/nxp-imx8-based-products/imx8m-plus-mini-nano-software/solidsense-n8-compact-yocto.md) |
| ![](../../../.gitbook/assets/image-20211219-085009.png) | [Buildroot](https://github.com/SolidRun/imx8mp_build/tree/imx8mn)                                                                                    |

### Build from sources

* [i.MX8M Nano Compact ATF, U-Boot and Linux kernel](../../iot-industrial-product-line/nxp-imx8-based-products/imx8m-plus-mini-nano-software/solidsense-n8-compact-atf-u-boot-and-linux-kernel.md)
* [IMX8M Nano Compact - Yocto](../../iot-industrial-product-line/nxp-imx8-based-products/imx8m-plus-mini-nano-software/solidsense-n8-compact-yocto.md)
* [https://github.com/SolidRun/imx8mp\_build/tree/develop-lf-6.6.52-2.2.0-imx8mn](https://github.com/SolidRun/imx8mp_build/tree/develop-lf-6.6.52-2.2.0-imx8mn)

### Support

Please follow our [SolidSense Support Overview](../solidsense-software/other-software-articles/solidsense-support-overview.md) page.

### Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
