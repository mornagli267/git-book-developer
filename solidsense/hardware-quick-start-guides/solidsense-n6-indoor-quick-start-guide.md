# SolidSense N6 Indoor Quick Start Guide

![](../../../.gitbook/assets/image-20220117-152021.png)

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Revision** | **Notes** |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- |
| 19 Dec 2021       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1.0          |           |

## Introduction

The following quick start guide provides background information about the [SolidSense N6 Indoor Edge Gateway.](https://www.solid-run.com/edge-gateway-solidsense/#indoor)

SolidSense N6 Edge Gateway is an enterprise Internet of Things gateway designed for servicing a local network of IoT devices with a range of solutions and business applications. SolidSense is the ultimate IoT M2M solution, with high-end connectivity options, on an industrial grade fanless platform in both an indoor and outdoor configuration.

Based on the robust and modular NXP i.MX6 Arm Cortex A9 Single/Dual/Quad-core processor, SolidSense is a feature-rich edge platform designed to provide flexibility for developers and OEMs in implementing an almost endless range of IoT solutions.

## Specifications

|                                  | LTE Europe (EU)                                                                                                                                                                                                                                  | LTE USA (US)                                                                                                                                                                                                                                     | LTE Australia (AU)                                                                                                                                                                                                                               | Ethernet                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| I/Os                             | 4 x USB 2.0                                                                                                                                                                                                                                      | 4 x USB 2.0                                                                                                                                                                                                                                      | 4 x USB 2.0                                                                                                                                                                                                                                      | 4 x USB 2.0                                                                                                                                        |
| Networking                       | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)<br>1 x Dual BLE 5.0 (SDR based on nRF52832)<br>1 x LTE Cat 4 EU + GPS (with fallback on 3G/2G)<br>Optional LTE Cat M1 (Worldwide) + EGPRS</p> | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)<br>1 x Dual BLE 5.0 (SDR based on nRF52832)<br>1 x LTE Cat 4 US + GPS (with fallback on 3G/2G)<br>Optional LTE Cat M1 (Worldwide) + EGPRS</p> | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)<br>1 x Dual BLE 5.0 (SDR based on nRF52832)<br>1 x LTE Cat 4 AU + GPS (with fallback on 3G/2G)<br>Optional LTE Cat M1 (Worldwide) + EGPRS</p> | <p>1 x Ethernet RJ45 10/100/1000 (max 470 MB/s)<br>1 x 802.11 a/b/g/n WiFi and Bluetooth (2.4 GHz)<br>1 x Dual BLE 5.0 (SDR based on nRF52832)</p> |
| Processor                        | NXP i.MX6 Arm Cortex A9 Dual core 800MHz                                                                                                                                                                                                         | NXP i.MX6 Arm Cortex A9 Dual core 800MHz                                                                                                                                                                                                         | NXP i.MX6 Arm Cortex A9 Dual core 800MHz                                                                                                                                                                                                         | NXP i.MX6 Arm Cortex A9 Dual core 800MHz                                                                                                           |
| Memory & Storage                 | <p>1GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                                                                                                                                                           | <p>1GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                                                                                                                                                           | <p>1GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                                                                                                                                                           | <p>1GB DDR3<br>8GB eMMC<br>MicroSD</p>                                                                                                             |
| Display                          | HDMI                                                                                                                                                                                                                                             | HDMI                                                                                                                                                                                                                                             | HDMI                                                                                                                                                                                                                                             | HDMI                                                                                                                                               |
| Misc.                            | Programmable LEDs                                                                                                                                                                                                                                | Programmable LEDs                                                                                                                                                                                                                                | Programmable LEDs                                                                                                                                                                                                                                | Programmable LEDs                                                                                                                                  |
| Development and Debug interfaces | Console port (internal)                                                                                                                                                                                                                          | Console port (internal)                                                                                                                                                                                                                          | Console port (internal)                                                                                                                                                                                                                          | Console port (internal)                                                                                                                            |
| Power                            | 9V to 36V via twist and lock jack                                                                                                                                                                                                                | 9V to 36V via twist and lock jack                                                                                                                                                                                                                | 9V to 36V via twist and lock jack                                                                                                                                                                                                                | CE, FCC/CSA                                                                                                                                        |
| Temperature                      | -25°C to 65°C                                                                                                                                                                                                                                    | -25°C to 65°C                                                                                                                                                                                                                                    | -25°C to 65°C                                                                                                                                                                                                                                    | -25°C to 65°C                                                                                                                                      |
| Dimensions                       | 120 x 80 x 30mm                                                                                                                                                                                                                                  | 120 x 80 x 30mm                                                                                                                                                                                                                                  | 120 x 80 x 30mm                                                                                                                                                                                                                                  | 120 x 80 x 30mm                                                                                                                                    |
| Enclosure                        | Extruded aluminum, 5 x SMA (3 x 2.4GHz, LTE, GPS)                                                                                                                                                                                                | Extruded aluminum, 5 x SMA (3 x 2.4GHz, LTE, GPS)                                                                                                                                                                                                | Extruded aluminum, 5 x SMA (3 x 2.4GHz, LTE, GPS)                                                                                                                                                                                                | Extruded aluminum, 3 x SMA (3 x 2.4GHz)                                                                                                            |

![](../../../.gitbook/assets/image-20220117-153041.png)

### Environmental Ratings

|                           |                             |
| ------------------------- | --------------------------- |
| Operating Temperature     | -25C to 65C                 |
| Storage Temperature       | -20C to 80C                 |
| Ambient Relative Humidity | 5% to 95% (non condesnsing) |

## Block Diagram

The following figure describes the **SolidSense N6 Indoor Edge Gateway** Block Diagram.

![](../../../.gitbook/assets/image-20220118-080456.png)

## Visual features overview

Please see below the features overview of the top side of the product.

![](../../../.gitbook/assets/image-20220117-152508.png)

## Feature Specifications

### SMA Connectors

The SolidSense N6 indoor features **5 SMA** connectors as described below:

**From left to right:**

* 2.4G – u-blox Nina B1 ([J2 on u-blox addon card Schematics](https://solidrun.atlassian.net/wiki/pages/viewpageattachments.action?pageId=263684108\&preview=%2F263684108%2F288194765%2Fublox-pinout-solidsense-v20.pdf) ) | SMA-RP
* WiFi – TI1831MOD (On SOM) | SMA-RP
* GPS – Quectel EC25 (GPS) | SMA
* 2.4G – u-blox Nina B1 ([J6 on u-blox addon card Schematics](https://solidrun.atlassian.net/wiki/pages/viewpageattachments.action?pageId=263684108\&preview=%2F263684108%2F288194765%2Fublox-pinout-solidsense-v20.pdf)) | SMA-RP

![](../../../.gitbook/assets/image-20220117-162936.png)

LTE – Quectel EC25 (Main) | SMA

![](../../../.gitbook/assets/image-20220117-162928.png)

{% hint style="success" %}
**Please Note** For more information about the antennas used (optional) with the SolidSense N6 indoor please see this article : [SolidSense N6 Indoor Kits](/solidsense/solidsense-other-articles/solidsense-n6-indoor-kits.md)
{% endhint %}


The assembly of the u.FL to SMA cables can be seen in the picture below;

![](../../../.gitbook/assets/image-20220117-162956.png)

### LED

Bi-color (Red,Green) LEDs, Datasheet can be found [here](solidsense-n6-indoor-quick-start-guide.md#section-237d5123-0656-4645-be84-4a1d46e832ca),\
For user programming / indication / status.

### HDMI

SolidSense uses PN ABA-HDM-051-P01 by LOTES

### USB

SolidSense uses PN USB-A2D16F-2B8N by CZT

Each USB port is able to provide up to 0.5A

### MicroSD

SolidSense uses PN ZM90-15000-0BR1 by CEN LINK, Datasheet can be seen here: [http://www.cenlink.com.tw/upload/20120718204404.pdf](http://www.cenlink.com.tw/upload/20120718204404.pdf)&#x20;

### Ethernet

SolidSense uses PN B50(15-02)G8-09-A023-B52 by BTOP : [http://www.magnetic-rj45jack.com/sale-10691195-bicolor-led-rj45-connector-port-high-performance-for-maximum-emi-suppression.html](http://www.magnetic-rj45jack.com/sale-10691195-bicolor-led-rj45-connector-port-high-performance-for-maximum-emi-suppression.html)

{% hint style="info" %}
**Please Note** Due to internal i.MX6 buses the 1000Mbps interface speed is limited to 470Mbps.
{% endhint %}


### DC jack

* Input voltage range: 9-36V
* Power consumption idle:  0.4W
* Power consumption maximum: 8W
* Diameter : Outer 5.5mm , Inner 2.1mm with twist & lock feature

Please refer to this article for more information :  [i.MX6 Application Note – Suspend to Memory Power Measurements](../../iot-industrial-product-line/nxp-imx6-based-products/imx6-other-articles/imx6-application-note-suspend-to-memory-power-measurements.md)

## The system can be used in 4 ways

1. Ready to go **SolidSense IoT platform** (SolidSense Out-Of-the-Box) with Eclipse Kura Framework and Wirepas/Bluetooth Low Energy MQTT gateways built-in applications. Configure the gateway via Kura and that’s it you can directly have your data forwarded to your cloud application.
2. Developing your own application or add-on on top of the platform. Simple additions can be developed via Python 3.7 using the pre-installed packages. For more sophisticated development, a Docker infrastructure is ready to host your containers.
3. Create your own SolidSense image derived from SolidSense OOB.
4. From bare metal. You can create your own Linux image starting from SolidRun BSP. The support for these developments are not covered in the SolidSense section.

{% hint style="success" %}
The product comes with a SolidSense built in software and ready to go.
{% endhint %}


## Network Configuration

For managing your IoT gateway, monitor the gateway status, and manage the network configuration, you can refer to [Configuring SolidSense networking with Kura](/solidsense/solidsense-software/kura/configuring-solidsense-networking-with-kura.md) .

Please see below picture to get the serial number for SSID of the network.

## Mesh Network - Wirepas

![](../../../.gitbook/assets/image-20220117-152655.png)

If you are using SolidSense as a Wirepas gateway you can directly configure your Wirepas gateway by referring to [Configuring and testing the Wirepas gateway software](/solidsense/solidsense-software/wirepas/configuring-and-testing-the-wirepas-gateway-software.md) .

For flashing or re-flashing Wirepas sinks, please refer to [Flashing or Re-flashing Wirepas sinks on SolidSense gateway (V0.9 and up)](../solidsense-software/wirepas/flashing-or-re-flashing-wirepas-sinks-on-solidsense-gateway-v09-and-up.md) .

## RF Performance

### TI1831MOD

|                                 |                                  |      |         |      |       |
| ------------------------------- | -------------------------------- | ---- | ------- | ---- | ----- |
| **WiFi Receive Specifications** |                                  |      |         |      |       |
| Parameter                       | Test condition                   | Min  | Typical | Max  | Units |
| Frequency                       | 2.4-GHz Receiver Characteristics | 2412 |         | 2484 | MHz   |
| Sensitivity                     | 802.11b at 11Mbps                |      | -87.9   |      | dBm   |
|                                 | 802.11g at 54Mbps                |      | -74.9   |      | dBm   |
|                                 | 802.11n at MCS7 HT20             |      | -72.4   |      | dBm   |
|                                 | 802.11n at MCS7 HT40             |      | -67     |      | dBm   |

|                                  |   |   |      |   |     |
| -------------------------------- | - | - | ---- | - | --- |
| **WiFi Transmit Specifications** |   |   |      |   |     |
| Output Power                     |   |   | 17.4 |   | dBm |

Approvals

* FCC (USA)
* ISED (Canada)
* ETSI/CE (Europe)
* MIC (Japan)

### U-Blox Nina B1

|                                |                |     |         |     |       |
| ------------------------------ | -------------- | --- | ------- | --- | ----- |
| **BLE Receive Specifications** | Test condition | Min | Typical | Max | Units |
| Frequency Range                |                |     | 2440    |     | MHz   |
| Sensitivity                    |                |     | -95     |     | dBm   |

|                                 |                |     |         |     |       |
| ------------------------------- | -------------- | --- | ------- | --- | ----- |
| **BLE Transmit Specifications** | Test condition | Min | Typical | Max | Units |
| Output Power                    |                |     | 7       |     | dBm   |

Approvals

* Europe
* USA
* Japan
* Taiwan
* South Korea
* Brazil
* Australia and New Zealand
* South Africa

### Quectel EC25

|                                 |                |     |                   |     |       |
| ------------------------------- | -------------- | --- | ----------------- | --- | ----- |
| **LTE Transmit Specifications** | Test condition | Min | Typical           | Max | Units |
| LTE FDD                         |                |     | 150(DL)/50(UL)    |     | Mbps  |
| LTE TDD                         |                |     | 130(DL)/30(UL)    |     | Mbps  |
| DC-HSDPA                        |                |     | 42(DL)            |     | Mbps  |
| HSUPA                           |                |     | 5.76(UL)          |     | Mbps  |
| WCDMA                           |                |     | 384(DL)/384(UL)   |     | Kbps  |
| GSM EDGE                        |                |     | 296(DL)/236.8(UL) |     | Kbps  |
| GSM GPRS                        |                |     | 107(DL)/85.6(UL)  |     | Kbps  |

{% hint style="info" %}
**Please Note** DL = Download UL = Upload
{% endhint %}


|                            |         |               |                          |
| -------------------------- | ------- | ------------- | ------------------------ |
| **Cellular bands (CAT 4)** |         |               |                          |
| **EU Bands**               | LTE FDD |               | B1/ B3/ B5/ B7/ B8/ B20  |
| LTE TDD                    |         | B38/ B40 /B41 |                          |
| 3G                         |         | B1/ B5/ B8    |                          |
| **US bands**               | LTE FDD |               | B2/ B4/ B12              |
| 3G                         |         | B2/ B4/ B5    |                          |
| **AU/LAT bands**           | LTE FDD |               | B1/B2/B3/B4/B5/B7/B8/B28 |
| LTE TDD                    |         | B40           |                          |
| 3G                         |         | B1/B2/B5/B8   |                          |

Electrical Specifications

|                                        |                          |                    |
| -------------------------------------- | ------------------------ | ------------------ |
| **Electrical Characteristics**         |                          |                    |
| **Output Power**                       | **Sensitivity**          | **Consumption**    |
| Class 4 (33dBm±2dB) for GSM850         | LTE B1: -101.5dBm (10M)  | 3.6mA @Sleep, Typ. |
| Class 4 (33dBm±2dB) for EGSM900        | LTE B2: -101dBm (10M)    | 35mA @Idle         |
| Class 1 (30dBm±2dB) for DCS1800        | LTE B3: -101.5dBm (10M)  |                    |
| Class 1 (30dBm±2dB) for PCS1900        | LTE B4: -101dBm (10M)    |                    |
| Class E2 (27dBm±3dB) for GSM850 8-PSK  | LTE B5: -101dBm (10M)    |                    |
| Class E2 (27dBm±3dB) for EGSM900 8-PSK | LTE B7: -99.5dBm (10M)   |                    |
| Class E2 (26dBm±3dB) for DCS1800 8-PSK | LTE B8: -101dBm (10M)    |                    |
| Class E2 (26dBm±3dB) for PCS1900 8-PSK | LTE B12: -101dBm (10M)   |                    |
| Class 3 (24dBm+1/-3dB) for WCDMA bands | LTE B13: -100dBm (10M)   |                    |
| Class 3 (23dBm±2dB) for LTE-FDD bands  | LTE B14: -99dBm (10M)    |                    |
| Class 3 (23dBm±2dB) for LTE-TDD bands  | LTE B18: -101.7dBm (10M) |                    |
|                                        | LTE B19: -101.4dBm (10M) |                    |
|                                        | LTE B20: -102.5dB (10M)  |                    |
|                                        | LTE B26: -101.5dBm (10M) |                    |
|                                        | LTE B28: -102dBm (10M)   |                    |
|                                        | LTE B38: -100dBm (10M)   |                    |
|                                        | LTE B40: -100dBm (10M)   |                    |
|                                        | LTE B41: -99dBm (10M)    |                    |
|                                        | LTE B66: -99dBm (10M)    |                    |
|                                        | LTE B71: -100dBm (10M)   |                    |
|                                        | WCDMA B1: -110dBm        |                    |
|                                        | WCDMA B2: -110dBm        |                    |
|                                        | WCDMA B4: -110dBm        |                    |
|                                        | WCDMA B5: -110.5dBm      |                    |
|                                        | WCDMA B6: -110.5dBm      |                    |
|                                        | WCDMA B8: -110.5dBm      |                    |
|                                        | WCDMA B19: -110.5dBm     |                    |
|                                        | GSM850: -109dBm          |                    |
|                                        | EGSM900: -109dBm         |                    |
|                                        | DCS1800: -109dBm         |                    |
|                                        | PCS1900: -109dBm         |                    |

Approvals

* RoHS Compliant
* CE/GCF/Vodafone (Europe)
* FCC/PTCRB/AT\&T/Verizon\* (North America)
* RCM/Telstra (Australia)
* JATE/TELEC/DOCOMO\*/Softbank\* (Japan)
* NCC (Taiwan)
* KC/SKT/KT\*/LGU+\* (Korea)
* IC/Rogers (Canada)
* NBTC (Thailand)
* Anatel (Brazil)

{% hint style="info" %}
**Please note** (\*) Under development
{% endhint %}


## Labels

### Product Label

Each SolidSense unit has a unique MAC address and Serial Number as detailed below;

* (1P) – Product SKU
* (S) – Serial Number
* (23S) – MAC Address

The 2D barcode matrix contains this information as well as country of origin.

![](../../../.gitbook/assets/image-20220117-162637.png)

### Package Label

Each SolidSense unit has the below label on the product package; the 2D barcode matrix has this information encoded.

* (1P) – Product SKU
* (S) – Serial Number
* (Q) – Quantity

![](../../../.gitbook/assets/image-20220117-162621.png)

### Package Description

Length : 172mm | Width : 150mm | Height : 55mm | Weight : 415gr (Inc. packaging box)

Each product is packed into a single package with anti-static foam as shown in the picture below.

![](https://developer.solid-run.com/wp-content/uploads/2019/07/IMG_20190724_142614-1010x1024.jpg)

![](https://developer.solid-run.com/wp-content/uploads/2019/07/IMG_20190724_142624-1024x922.jpg)

## Bluetooth

1. For showing all Bluetooth devices, run the following:

```
hciconfig -a
```

1. Choose a device, and turn it on:

```
 hciconfig hci0 up
```

1. Set up the Bluetooth name:

```
hciconfig hci0 name 'SolidRun_Ble'
```

1. Make your Bluetooth detectable by other devices:

```
hciconfig hci0 piscan
```

1. If you want to connect to other devices:

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

## Support

Please follow our [SolidSense Support Overview](/solidsense/solidsense-software/other-software-articles/solidsense-support-overview.md) page.

## Documentation

|   | File | Modified |
| - | ---- | -------- |

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
