# RZ/G2L and RZ/V2L SOM Hardware User Manual

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 11 Oct 2023 | Mikhail Anikin | 1.0 |     |
| 16 Oct 2023 | Sasha Strizhiver | 1.1 | general comments |
| Nov 2, 2023 | Shahar Fridman | 1.2 | Add Power Consumption Measurement |
| 31 Dec 2024 | Yazan Shhady | 1.3 | **Add SOM Rev 1.2 changes:**<br><br>**1.** Connect the WIFI clock (PMIC\_32KHz\_CLK) to Pull Up  <br>**2**. Move RZ\_P5\_1 from J7-33 to J7-13 to support M.2 Reset on the HBP  <br>**3.** Move RZ\_P5\_0 from J7-39 to J7-15  <br>**4\.** Move RZ\_P5\_2 from J7-37 to J7-8  <br>**5\.** Enable power control from BtB. Adding U14 (PU/PD select)  <br>**6.** Move RZ\_P16\_0 from J7-59 to J7-79  <br>**7.** Add AUDIO\_CLK to J7-59  <br>**8.** Add R116 to support RTC clock from MPIO2.  <br>**9.** Swapping I2C1 pins on J9: **SOM V1.2**\=> J9-51-SDA, J9-53-SCL (**SOM V1.1** => J9-51-SCL, J9-53-SDA). |
| Table of Contents | - [Revisions and Notes](#revisions-and-notes)<br>- [Introduction](#introduction)<br>- [Overview](#overview)<br>  - [Highlighted Features](#highlighted-features)<br>  - [Supporting Products](#supporting-products)<br>- [Description](#description)<br>  - [Block Diagram](#block-diagram)<br>  - [Features Summary](#features-summary)<br>- [Core System Components](#core-system-components)<br>  - [RZ/G2L SoC Family](#rz-g2l-soc-family)<br>  - [MEMORIES](#memories)<br>  - [DDR4](#ddr4)<br>  - [eMMC and SD NAND Memory](#emmc-and-sd-nand-memory)<br>  - [Micro-SD (Carrier)](#micro-sd-carrier)<br>  - [Quad Serial NOR Flash (SOM)](#quad-serial-nor-flash-som)<br>  - [EEPROM (SOM)](#eeprom-som)<br>  - [Serial NOR Flash (Carrier)](#serial-nor-flash-carrier)<br>  - [10/100/1000 Mbps Ethernet PHY](#10-100-1000-mbps-ethernet-phy)<br>  - [WI-FI (802.11AC/A/B/G/N) AND BT 5.3 (MURATA'S CERTIFIED MODULE)](#wi-fi-80211ac-a-b-g-n-and-bt-53-muratas-certified-module)<br>  - [WI-FI & BT](#wi-fi-bt)<br>- [External Interfaces](#external-interfaces)<br>  - [General](#general)<br>  - [USB 2.0](#usb-20)<br>  - [MIPI CSI](#mipi-csi)<br>  - [MIPI DSI](#mipi-dsi)<br>  - [Parallel Interface](#parallel-interface)<br>  - [UART](#uart)<br>  - [SPI](#spi)<br>  - [I2C](#i2c)<br>  - [uSD](#usd)<br>  - [CAN-FD](#can-fd)<br>- [CONNECTOR’S SIGNAL DESCRIPTION](#connectors-signal-description)<br>  - [J5001](#j5001)<br>  - [J7](#j7)<br>  - [J9](#j9)<br>  - [mikroBUS](#mikrobus)<br>  - [LCD (Parallel Video Output) Signals allocation](#lcd-parallel-video-output-signals-allocation)<br>- [Power & Reset](#power-reset)<br>  - [POWER CONSUMPTION](#power-consumption)<br>    - [RZ/G2L Power Table](#rz-g2l-power-table)<br>    - [RZ/V2L Power Table](#rz-v2l-power-table)<br>  - [RESET](#reset)<br>- [RZG2L/V2L INTEGRATION MANUAL](#rzg2l-v2l-integration-manual)<br>  - [POWER UP SEQUENCE](#power-up-sequence)<br>  - [BOOTING OPTIONS](#booting-options)<br>    - [Strap pins Booting](#strap-pins-booting)<br>  - [I2C INTERFACES](#i2c-interfaces)<br>  - [GPIO INTERFACES](#gpio-interfaces)<br>- [Mechanical Description](#mechanical-description)<br>- [SOM Version Changes:](#som-version-changes)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

<a id="introduction"></a>

## Introduction

This User Manual relates to the SolidRun’s RZG2 series, which includes

- RZG2L Dual-core ARM A55 (1.2GHz) w Cortex-M33 (200MHz)
- RZV2L Dual-core ARM A55 (1.2GHz) w Cortex-M33 (200MHz) and Renesas Original AI Accelerator "DRP-AI" 

<a id="overview"></a>

## Overview

The SolidRun’s RZG2L/V2L family is a high-performance 64-Bit Renesas. RZ/G2 Based SOMs with Integrated GPU for Next-Gen Human-Machine Interfaces. RZV2L is adding an AI accelerator to the G2L. 

Ideal for automation, smart buildings, network cameras, and IoT devices, SolidRun RZ/G2 SOMs combine a powerful MPU, GPU, extended ECC, Ethernet, and offer long-term Linux software support. 

<a id="highlighted-features"></a>

#### Highlighted Features

- Ultra-small footprint SOM (47x30mm) including three board-to-board connectors (250 total pins number). 
- Renesas’s SoC supports the DUAL version. 
  - Dual Cortex A55 and up to 1.2GHz 
  - Cortex-M33 subsystem processor supports real-time tasks. 
  - Video codec (H.264). 
  - AI accelerator; DRP-AI (**V2L only**) 
  - High-security engines. 
  - Dual Ethernet interfaces. 
  - Up to two CAN interfaces. 
  - High industrial reliability with in-line ECC on DDR4 and on on-chip RAM. 
  - Single MIPI-CSI and single MIPI-DSI (H.264) 
  - Optional RGB interface. 
  - Two USB 2.0. 
- DDR4 memory in x16 configurations supports up to 2GB and up to 1.6GT/s. 
- Up to 128GB eMMC. 
- 1Mb QSPI NOR Flash 
- Wi-Fi 11b/g/n/ac + Bluetooth 5.0 certified module 
- 1Mb QSPI NOR Flash 
- 1Kb I2C EEPROM 
- Power management devices 
- Commercial and industrial temperature grade support. 

<a id="supporting-products"></a>

#### Supporting Products

The following products are provided by SolidRun both as production-level platforms and as reference examples on how to incorporate the SOM in different levels of integration:

- [HummingBoard Pro](../renesas-rz-based-products/hummingboard-pro-rz-g2l-som-quick-start-guide.md) – An extended board computer incorporating the SOM with different Linux distributions while adding extra hardware functionalities and access to the hardware.

<a id="description"></a>

## Description

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the RZ/G2L Blocks Diagram.

![](./attachments/MicrosoftTeams-image(1)-20231015-144520.png)

<a id="features-summary"></a>

#### Features Summary

Following are the features summary of the SOM. Notice that some of the features are pinout multiplexed (please refer to the pin mux table below and the Renesas datasheets): 

- Renesas’s RZG2 series SoC (Dual ARM® Cortex™ A55 Processor, up to 1.2 GHz) 
- Cortex-M33 (200MHz) subsystem processor. 
- AI accelerator; DRP-AI (**V2L only**) 
- Up to 2GByte DDR4 memory and up to 1.6GT/s 
- Eight bits eMMC 5.1 memory or a four bits SD interface 
- 1Kb I2C EEPROM. 
- 8Mb QSPI NOR Flash. 
- 4-lanes MIPI-DSI interface 
- Optional RGB (8,8,8) interface. 
- 3D graphics engine (Arm Mali-G31). 
- Video codec (H.264). 
- 4-lanes MIPI CSI-2  
- Dual 10/100/1000 Mbps Ethernet PHY 
- Wi-Fi (802.11a/b/g/n/ac) + BT (5.0) Murata's certified module  
- Two USB 2.0 Host and Device 
- Single eSPI interface. 
- Up to four Serial interfaces. 
- Up to 2 CAN-FD. 
- Power: 
  - A single 5.0V input using B-to-B connector. 
  - 3.3V/1A output to support carrier's digital interfaces. 
  - RAA215300 PMIC 

<a id="core-system-components"></a>

## Core System Components

<a id="rz-g2l-soc-family"></a>

#### RZ/G2L SoC Family

Ideal for automation, smart buildings, network cameras, and IoT devices, SolidRun RZ/G2 SOMs combine a powerful MPU, GPU, extended ECC, Ethernet, and offer long-term Linux software support 

![](./attachments/image-20221215-075410.png)

A verified Linux Package (VLP) reduces cost and simplifies design.

![](./attachments/image-20221215-075435.png)

<a id="memories"></a>

#### MEMORIES

The RZG2L SOM supports a variety of memory interfaces for booting and data storage. The following figure describes the RZG2L memory interfaces.

![](./attachments/image-20231015-093712.png)

<a id="ddr4"></a>

#### DDR4

- Up to 2GB memory space.
- 16 Bits data bus.
- Up to 1600 MT/s.
- ECC function for single-bit and double-bit error reporting, single-bit error correction, and programmable removal of ECC storage
- Support various low-power modes, clocks, and power-gated operations.
- Support Self-Refresh mode.

<a id="emmc-and-sd-nand-memory"></a>

#### **eMMC and SD NAND Memory**

SD0 of the RZG2L/V2L can be configured as an 8-bit eMMC interface or a 4-bit SDIO. Configuration can be done during the boot process (Boot strap pins, SD0\_DEV\_SEL) or by SW (SD0\_DEV\_SEL\_SW, GPIO\_P22\_1). 

Selecting SD0’s physical connection (eMMC or uSD card) is done by an analog switch.

> [!INFO]
> The state of the analog switch can be set by a DIP-Switch, SW or PU/PD resistors.

 **eMMC**

- Up to 128GB memory space.
- 8 Bits data bus.
- Support MMC standard, up to version 4.5.1.
- Supports High-speed, HS200 transfer modes
- uSDHC-0.
- Can be used as BOOT NVM \*\*

<a id="micro-sd-carrier"></a>

#### **Micro-SD (Carrier)**

- Optional on the carrier board
- uSDHC-0.
- Implements 4 data bits.
- Support SD/SDIO standard up to version 3.0.
- SD, SDHC, and SDXC SD memory card access supported.
- Default, high-speed, UHS-I/SDR50, and SDR104 transfer modes supported
- Can be used as BOOT NVM \*\*

<a id="quad-serial-nor-flash-som"></a>

#### **Quad Serial NOR Flash (SOM)**

- Each channel can be configured as a 1/2/4-bit operation.
- Support both SDR (66MHz) mode and DDR (50MHz) mode
- No reset
- QSPIA/nSS0.
- Can be used as BOOT NVM \*\*

<a id="eeprom-som"></a>

#### **EEPROM (SOM)**

- 1Kb EEPROM
- ON-Semi’s CAT24AA01TDI or compatible
- I2C0
- Address 0X50 (7 bits format)
- Stores SOM’s configurations.

<a id="serial-nor-flash-carrier"></a>

#### **Serial NOR Flash (Carrier)**

- Optional on carrier board
- 1-bit data bus.
- eSPI1/nSS0
- Can be used as BOOT NVM \*

> [!CAUTION]
> **\* Note – eMMC and uSD share the same signals.**
> **\*\* Note – Boot configuration is set by the Boot-strap pins**

<a id="10-100-1000-mbps-ethernet-phy"></a>

#### **10/100/1000 Mbps Ethernet PHY**

 The SOM supports two fast Ethernet interfaces.

![](./attachments/RZ_G2L_V2L%20Eth%202023(1)-20231015-094209.png)

- RGMII interface.
- 802.3 Ethernet interface for 1000BASE-T, 100BASE-TX, and 10BASE-T.
- MaxLinear's MxL86110I PHY.
- Auto-MDIX and polarity correction.
- Energy-Efficient Ethernet (EEE) and power down mode.
- 10k byte jumbo frame support.

<a id="wi-fi-80211ac-a-b-g-n-and-bt-53-muratas-certified-module"></a>

#### WI-FI (802.11AC/A/B/G/N) AND BT 5.3 (MURATA'S CERTIFIED MODULE)

![](./attachments/RZ_G2L_V2L%20WiFi%20Bt%202023-20231010-142958.png)

<a id="wi-fi-bt"></a>

#### **WI-FI & BT**

 The WI-FI & BT module is Murata’s 1MW module Based on Cypress CYW43455 chip. The WI-FI main features are:

- Operate at ISM frequency Band (2.4/5 GHz)
- IEEE Standards Support 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac
- WI-FI over SDIO-1 interface
- BT 5.3 BR/EDR/LE
- BT over UART-2 Interface
- Global certification.

<a id="external-interfaces"></a>

## External Interfaces

<a id="general"></a>

#### General

The SOM incorporates three Hirose DF40 board-to-board headers.

The selection of the Hirose DF40 is due to the following criteria:

- Miniature (0.4m pitch)
- Highly reliable manufacturer
- Availability (worldwide distribution channels)
- Excellent signal integrity (supports 6Gbps)
  - Please contact Hirose or SolidRun for reliability and test result data.
- Mating height of between 1.5mm to 4.0mm (1.5mm to 3.0mm if using 70-pin Board-to-Board header). RZG2L/V2L SOM’s headers are fixed, the final mating height is determined by carrier implementation

<a id="usb-20"></a>

#### USB 2.0

The RZG2L/V2L supports two USB 2.0 interfaces. The following figure describes the USB interfaces.

![](./attachments/RZ_G2L_V2L%20USB%202023-20231011-074314.png)

The USB’s main features are:

- Single USB 2.0 OTG/DRD(Host/Function) interface (USB0)
- Single USB 2.0 Host interface (USB1).
- Support mode: High-Speed(480Mbps)/Full-Speed(12Mbps)/Low-Speed(1.5Mbps).
- OTG function (Rev2.0).
- B2B Connector’s Signal Description
- DRD (Dual-Role-Device) function (Static switch between Host and Function).
- Power control signals are not part of the USB module, any available GPIO can be used.

> [!WARNING]
> **Note – The voltage on VBUS is 5V.**

<a id="mipi-csi"></a>

#### MIPI CSI

The following figure describes the CSI interface.

![](./attachments/RZ_G2L_V2L%20CSI%202023-20231011-075431.png)

- Supports MIPI CSI-2 V2.1 and MIPI D-PHY V2.1 (80 Mbps ~ 1500 Mbps).
- Maximum image size: 5 M pixels.
- Minimum image size: QVGA (320 × 240) ＝ 76.8 K pixels.
- Maximum number of valid pixels in the horizontal direction: 2800 pixels.
- Maximum number of valid pixels in the vertical direction: 4095 lines
- Support 1/2/4 lanes.
- Support 4 Virtual Channel.

<a id="mipi-dsi"></a>

#### MIPI DSI

The following figure describes the DSI interface.

![](./attachments/RZ_G2L_V2L%20DSI%202023-20231011-075552.png)

The DSI main features are:

- Display Serial Interface Version 1.3.1.
- Support up to Full HD (1920 × 1080), 60 fps (RGB888).
- Maximum Bandwidth: 1.5 Gbps per lane, 4 data lanes.
- Support Output Data Format: RGB666 / RGB888.
- Supports 1, 2, 3 and 4 lane configurations.
- Support for Virtual Channel

<a id="parallel-interface"></a>

#### Parallel Interface

- Support WXGA (1280x800), 60 fps.
- Support Output Data Format: RGB666 / RGB888. 
- CLK / HD / VD timing signal supported. 

<a id="uart"></a>

#### UART

Up to 4 UART interfaces. The following figure describes the UART interfaces.

![](./attachments/RZ_G2L_V2L%20UART%202023(2)-20231015-095457.png)

The UART interface's main features are:

- UART 2 is connected directly to the WI-FI/BT Modem to support the BT. It is NOT available on the SOM B-t-B connector.
- UART 0 supports TX, RX and is used as terminal interface
- UART 1 supports TX, RX, CTS and RTS.
- UART 3 supports TX and RX.
- UART 3 supports TX and RX.
- Selectable bit rate with an on-chip baud rate generator.

> [!WARNING]
> **Note – UART interfaces are available as ALT functional signals of other signals.**

<a id="spi"></a>

#### SPI

Up to 3 SPI interfaces. The following figure describes the eSPI interface.

![](./attachments/RZ_G2L_V2L%20SPI%202023-20231011-081313.png)

- Single chip select nSS0.
- Master/Slave configurable.
- Switching of the polarity of the serial transfer clock.
- Switching of the clock phase of serial transfer.
- Transfer bit-length is selectable as 8, 16, or 32 bits.

> [!WARNING]
> **Note SPI interfaces are available as ALT functional signals of other signals.**

<a id="i2c"></a>

#### I2C

Up to 4 I2C Interfaces. The following figure describes the I2C interfaces.

![](./attachments/RZ_G2L_V2L%20I2C%202023(1)-20231015-100122.png)

The I2C main features are:

- I2C-3 is used only on the SOM. It is connected to the PMIC.
- I2C-0 is available on the connector and connected to the SOM’s EEPROM.
- I2C-1 and I2C2 are available on the BtB connectors.
- I2C bus format or SMBus format.
- Master mode or slave mode selectable
- Up to 1 Mbps.
- Up to three slave-address settings can be made.
- Internal time-out function is capable of detecting long-interval stop of the SCL (clock signal).

> [!WARNING]
> **Note – I2C interfaces are available as ALT functional signals of other signals.**

<a id="usd"></a>

#### uSD

The uSD interface is multiplexed with the eMMC interface. Only one of them is available.

<a id="can-fd"></a>

#### CAN-FD

Up to 2 CANFD interfaces are available. The following figure describes the CAN interfaces.

![](./attachments/RZ_G2L_V2L%20CAN-FD%202023-20231011-083300.png)

The CAN main features are:

- Supports two interface modes, classical CAN mode and CANFD mode.
- ISO11898-1 compliant.
- Maximum 1 Mbps in classical CAN mode.
- Nominal bit rate: max.1 Mbps, data bit rate: max. 4 Mbps in CANFD mode.

<a id="connectors-signal-description"></a>

## CONNECTOR’S SIGNAL DESCRIPTION

<a id="j5001"></a>

#### J5001

| **PIN** | **HBP 2.5** |     | **RZG2L 1.2** |     |     | **PIN** | **HBP 2.5** |     | **RZG2L 1.2** |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | TP4 |     | NC  |     |     | 2   | NC  |     | NC  |     |
| 3   | DIP-SWITCH | 1V8 | MD0 | 1V8 |     | 4   | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA3\_N |     |
| 5   | DIP-SWITCH | 1V  | MD1 | 1V8 |     | 6   | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA3\_P |     |
| 7   | GND |     | GND |     |     | 8   | GND |     | GND |     |
| 9   | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_CLK\_P |     |     | 10  | GND |     | GND |     |
| 11  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_CLK\_N |     |     | 12  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA0\_N |     |
| 13  | GND |     | GND |     |     | 14  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA0\_P |     |
| 15  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA2\_N |     |     | 16  | GND |     | GND |     |
| 17  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA2\_P |     |     | 18  | Mini-PCIe (J20, optional) |     | NC  |     |
| 19  | GND |     | GND |     |     | 20  | Mini-PCIe (J20, optional) |     | NC  |     |
| 21  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA1\_N |     |     | 22  | GND |     | GND |     |
| 23  | DSI-CON (J19) or DSI-HDMI |     | RZ\_DSI\_DATA1\_P |     |     | 24  | M.2\_W\_DIS# | 1V8 | DISP\_DATA15/GPIO\_P14\_0 | 3V3 |
| 25  | GND |     | GND |     |     | 26  | Mini-PCIe\_W\_DIS# | 3V3 | DISP\_DATA16/GPIO\_P14\_1 | 3V3 |
| 27  | M.2\_WAKW\_ON\_LAN (PCIe) | NA  | GPIO\_P19\_1 | 3V3 |     | 28  | USB1\_PWR\_EN | 3V3 | RZ\_USB0\_VBUSEN | 3V3 |
| 29  | MIKROBUS (J10-4) | NA  | RZ\_SCIF1\_TXD | 3V3 |     | 30  | GND |     | GND |     |
| 31  | MIKROBUS (J10-3) | NA  | RZ\_SCIF1\_RXD | 3V3 |     | 32  | Mini-PCIe (J20, optional) |     | NC  |     |
| 33  | GND |     | GND |     |     | 34  | Mini-PCIe (J20, optional) |     | NC  |     |
| 35  | NC  |     | GPIO\_P19\_0 | 3V3 |     | 36  | GND |     | GND |     |
| 37  | MIKROBUS (J10-1) | NA  | RZ\_SCIF1\_CTS | 3V3 |     | 38  | Mini-PCIe (J20, optional) |     | NC  |     |
| 39  | MIKROBUS (J10-2) | NA  | RZ\_SCIF1\_RTS | 3V3 |     | 40  | Mini-PCIe (J20, optional) |     | NC  |     |
| 41  | HEADER, DIP-SW | 3V3 | MD2 | 1V8 |     | 42  | GND |     | GND |     |
| 43  | DSI\_TS\_nINT (DSI-HDMI) | 3V3 | DISP\_DATA5/GPIO\_P9\_1 | 3V3 |     | 44  | LED (D34) | 3V3 | DISP\_DATA0/GPIO\_P7\_2 | 3V3 |
| 45  | NC  |     | DISP\_DATA6/GPIO\_P10\_0 | 3V3 |     | 46  | LED (D33) | 3V3 | GPIO\_P48\_2 | 3V3 |
| 47  | GND |     | GND |     |     | 48  | LED (D32) | 3V3 | GPIO\_P47\_1 | 3V3 |
| 49  | NC  |     | GPIO\_P40\_2 | 3V3 |     | 50  | LED (D31) | 3V3 | GPIO\_P47\_2 | 3V3 |
| 51  | HEADER, DIP-SW | 3V3 | GPIO\_P47\_3 | 3V3 |     | 52  | GND |     | GND |     |
| 53  | WIFI\_DP (HUB to IMX8M) | NA  | ADC\_CH0 |     |     | 54  | CSI-CON(CON7) |     | RZ\_CSI\_DATA0\_N |     |
| 55  | WIFI\_DN (HUB to IMX8M) | NA  | ADC\_CH3 |     |     | 56  | CSI-CON(CON7) |     | RZ\_CSI\_DATA0\_P |     |
| 57  | GND |     | GND |     |     | 58  | GND |     | GND |     |
| 59  | CSI-CON(CON7) |     | RZ\_CSI\_CLK\_P |     |     | 60  | CSI-CON(CON7) |     | RZ\_CSI\_DATA2\_P |     |
| 61  | CSI-CON(CON7) |     | RZ\_CSI\_CLK\_N |     |     | 62  | CSI-CON(CON7) |     | RZ\_CSI\_DATA2\_N |     |
| 63  | GND |     | GND |     |     | 64  | GND |     | GND |     |
| 65  | CSI-CON(CON7) |     | RZ\_CSI\_DATA3\_P |     |     | 66  | CSI-CON(CON7) |     | RZ\_CSI\_DATA1\_P |     |
| 67  | CSI-CON(CON7) |     | RZ\_CSI\_DATA3\_N |     |     | 68  | CSI-CON(CON7) |     | RZ\_CSI\_DATA1\_N |     |
| 69  | GND |     | GND |     |     | 70  | GND |     | GND |     |

<a id="j7"></a>

#### J7

| **PIN** | **HBP 2.5** |     | **RZG2L 1.2** |     |     | **PIN** | **HBP 2.5** |     | **RZG2L 1.2** |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | ETH\_NIC (Intel, U6) |     | NC  |     |     | 2   | ETH\_NIC (Intel, U6) |     | NC  |     |
| 3   | ETH\_NIC (Intel, U6) |     | NC  |     |     | 4   | ETH\_NIC (Intel, U6) |     | NC  |     |
| 5   | GND |     | GND |     |     | 6   | GND |     | GND |     |
| 7   | ETH\_NIC (Intel, U6) |     | NC  |     |     | 8   | HEADER (CON4) | NA  | GPIO\_P5\_2 (was ~NC~ in SOM Rev 1.1) |     |
| 9   | ETH\_NIC (Intel, U6) |     | NC  |     |     | 10  | mPCIe (J20) | 3V3 | GPIO\_P42\_2 | 3V3 |
| 11  | GND |     | GND |     |     | 12  | HEADER (CON4) | NA  | GPIO\_P42\_3 | 3V3 |
| 13  | M.2\_RESET# | 1V8 | GPIO\_P5\_1 (was ~NC~ in SOM Rev 1.1) |     |     | 14  | POE\_AT\_DET | 3V3 | DISP\_DATA17/GPIO\_P15\_0 | 3V3 |
| 15  | RTC\_CLKO (RTC Int.) | 3V3 | GPIO\_P5\_0 (was ~NC~ in SOM Rev 1.1) |     |     | 16  | DSI-CON (J19) or DSI-HDMI | NA  | DISP\_DATA18/GPIO\_P15\_1 | 3V3 |
| 17  | GND |     | GND |     |     | 18  | M.2\_PCIe\_3V3\_EN | 3V3 | DISP\_DATA21/GPIO\_P17\_0 | 3V3 |
| 19  | HDMI CON (J1) |     | NC  |     |     | 20  | HEADER (CON4) | NA  | DISP\_DATA22/GPIO\_P17\_1 | 3V3 |
| 21  | HDMI CON (J1) |     | NC  |     |     | 22  | HEADER (CON4) | NA  | DISP\_DATA23/GPIO\_P17\_2 | 3V3 |
| 23  | GND |     | GND |     |     | 24  | HEADER (CON4) | NA  | DISP\_CLK/GPIO\_P6\_0 | 3V3 |
| 25  | HDMI CON (J1) |     | NC  |     |     | 26  | USB-HUB\_RST# | 3V3 | GPIO\_P39\_1 | 3V3 |
| 27  | HDMI CON (J1) |     | NC  |     |     | 28  | HEADER (CON4) | NA  | GPIO\_P39\_2 | 3V3 |
| 29  | GND |     | GND |     |     | 30  | HEADER (CON4) | NA  | DISP\_HSYNC/GPIO\_P6\_1 | 3V3 |
| 31  | HDMI CON (J1) |     | NC  |     |     | 32  | TP6 |     | DISP\_VSYNC/GPIO\_P7\_0 | 3V3 |
| 33  | HDMI CON (J1) |     | NC (was ~GPIO\_P5\_1~ in SOM Rev 1.1) | 3V3 |     | 34  | NC  |     | DISP\_DE/GPIO\_P7\_1 | 3V3 |
| 35  | GND |     | GND |     |     | 36  | HEADER (CON4) | NA  | GPIO\_P36\_1 | 3V3 |
| 37  | HDMI CON (J1) |     | NC (was ~GPIO\_P5\_2~ in SOM Rev 1.1) | 3V3 |     | 38  | CSI-CON(CON7) | NA  | RZ\_SCIF3\_TXD | 3V3 |
| 39  | HDMI CON (J1) |     | NC (was ~GPIO\_P5\_0~ in SOM Rev 1.1) | 3V3 |     | 40  | NC  |     | GPIO\_P32\_1 | 3V3 |
| 41  | GND |     | GND |     |     | 42  | GND |     | GND |     |
| 43  | HDMI CON (J1) | 3V3 | DISP\_DATA9/GPIO\_P11\_1 | 3V3 |     | 44  | LED (D30) | 3V3 | RZ\_SCIF3\_RXD | 3V3 |
| 45  | HDMI CON (J1) | 5V  | DISP\_DATA10/GPIO\_P12\_0 | 3V3 |     | 46  | HEADER (CON4) | NA  | GPIO\_P33\_0 | 3V3 |
| 47  | HDMI CON (J1) | 5V  | DISP\_DATA13/GPIO\_P13\_1 | 3V3 |     | 48  | GND |     | GND |     |
| 49  | HDMI CON (J1) | 5V  | DISP\_DATA14/GPIO\_P13\_2 | 3V3 |     | 50  | HEADER (CON4) | NA  | GPIO\_P32\_0 | 3V3 |
| 51  | AUDIO CODEC | 3V3 | RZ\_SSI0\_BCK | 3V3 |     | 52  | TERMINAL\_TX | 3V3 | RZ\_SCIF0\_TXD | 3V3 |
| 53  | AUDIO CODEC | 3V3 | RZ\_SSI0\_TXD | 3V3 |     | 54  | TERMINAL\_RX | 3V3 | RZ\_SCIF0\_RXD | 3V3 |
| 55  | AUDIO CODEC | 3V3 | RZ\_SSI0\_RCK | 3V3 |     | 56  | NC  |     | DISP\_DATA20/GPIO\_P16\_1 | 3V3 |
| 57  | AUDIO CODEC | 3V3 | RZ\_SSI0\_RXD | 3V3 |     | 58  | GND |     | GND |     |
| 59  | AUDIO CODEC | 3V3 | AUDIO\_CLK (was ~GPIO\_P16\_0/DISP\_DATA19~ in SOM Rev 1.1) | 3V3 |     | 60  | USB-HUB |     | NC  |     |
| 61  | GND |     | GND |     |     | 62  | USB-HUB |     | NC  |     |
| 63  | HEADER (CON4) | NA  | VDD\_RTC | 3V3 |     | 64  | GND |     | GND |     |
| 65  | RESET-B | 1V8 | SYS\_nRST | 1V8 |     | 66  | USB-HUB |     | NC  |     |
| 67  | HEADER (CON4) | NA  | ETH1\_TRX3\_P |     |     | 68  | USB-HUB |     | NC  |     |
| 69  | HEADER (CON4) | NA  | ETH1\_TRX3\_N |     |     | 70  | GND |     | GND |     |
| 71  | HEADER (CON4) | NA  | ETH1\_TRX2\_P |     |     | 72  | HEADER (CON4) | NA  | ETH1\_TRX1\_P |     |
| 73  | MICRO-SD | NA  | ETH1\_TRX2\_N |     |     | 74  | HEADER (CON4) | NA  | ETH1\_TRX1\_N |     |
| 75  | GND |     | GND |     |     | 76  | GND |     | GND |     |
| 77  | HDMI CON (J1) |     | NC  |     |     | 78  | HEADER (CON4) | NA  | ETH1\_TRX0\_P |     |
| 79  | HDMI CON (J1) |     | GPIO\_P16\_0/DISP\_DATA19 (was ~NC~ in SOM Rev 1.1) |     |     | 80  | HEADER (CON4) | NA  | ETH1\_TRX0\_N |     |

<a id="j9"></a>

#### J9

| **PIN** | **HBP 2.5** |     | **RZG2L 1.2** |     |     | **PIN** | **HBP 2.5** |     | **RZG2L 1.2** |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | ETH-POE |     | ETH\_TRX3\_N |     |     | 2   | GND |     | GND |     |
| 3   | ETH-POE |     | ETH\_TRX3\_P |     |     | 4   | USB-TYPE-A |     | GPIO\_P1\_0 | 3V3 |
| 5   | GND |     | GND |     |     | 6   | USB-TYPE-A |     | GPIO\_P43\_0 | 3V3 |
| 7   | ETH-POE |     | ETH\_TRX2\_N |     |     | 8   | GND |     | GND |     |
| 9   | ETH-POE |     | ETH\_TRX2\_P |     |     | 10  | USB-TYPE-A |     | NC  |     |
| 11  | GND |     | GND |     |     | 12  | USB-TYPE-A |     | RZ\_USB1\_OVERCUR | 3V3 |
| 13  | ETH-POE |     | ETH\_TRX1\_N |     |     | 14  | GND |     | GND |     |
| 15  | ETH-POE |     | ETH\_TRX1\_P |     |     | 16  | USB-TYPE-A |     | RZ\_USB0\_DP |     |
| 17  | GND |     | GND |     |     | 18  | USB-TYPE-A |     | RZ\_USB0\_DM |     |
| 19  | ETH-POE |     | ETH\_TRX0\_N |     |     | 20  | GND |     | GND |     |
| 21  | ETH-POE |     | ETH\_TRX0\_P |     |     | 22  | USB-HUB |     | RZ\_USB1\_DP |     |
| 23  | GND |     | GND |     |     | 24  | USB-HUB |     | RZ\_USB1\_DM |     |
| 25  | ETH-LED |     | LED\_0/PHY\_CFG0 | 3V3 |     | 26  | GND |     | GND |     |
| 27  | ETH-LED |     | LED1\_0/PHY\_CFG1 | 3V3 |     | 28  | M.2\_GPS\_EN# | NA  | RZ\_SCIF4\_RX | 3V3 |
| 29  | HEADER (CON4) |     | GPIO\_P43\_1 | 3V3 |     | 30  | J9-59 (BT\_FW\_FLASH, J9-59) | NA  | RZ\_SCIF4\_TX | 3V3 |
| 31  | MIPI-DSI, ETH-NIC, DSI-CON, CSI-CON, RTC, MIKROBUS | 3V3 | RZ\_RIIC0\_SCL | 3V3 |     | 32  | MIKROBUS (J8-3) | NA  | RZ\_RSPI1\_SSL | 3V3 |
| 33  | MIPI-DSI, ETH-NIC, DSI-CON, CSI-CON, RTC, MIKROBUS | 3V3 | RZ\_RIIC0\_SDA | 3V3 |     | 34  | CSI-CON  (J19) or DSI-HDMI | 3V3 | RZ\_SCIF4\_CLK | 3V3 |
| 35  | GND |     | GND |     |     | 36  | GND |     | GND |     |
| 37  | USB\_HUB\_CH1\_PWR\_EN | 3V3 | RZ\_USB1\_VBUSEN | 3V3 |     | 38  | MICRO-SD | SD2 | SD\_SD0\_CLK | SD2 |
| 39  | J9-55 (BT\_FW\_FLASH, J9-55) | NA  | GPIO\_P43\_2 | 3V3 |     | 40  | MICRO-SD | SD2 | SD\_SD0\_CMD | SD2 |
| 41  | ETH-NIC RST# (Intel, U6) | 3V3 | GPIO\_P43\_3 | 3V3 |     | 42  | MICRO-SD | SD2 | SD\_SD0\_DATA0 | SD2 |
| 43  | USB1\_VBUS | 5V  | RZ\_USB0\_VBUSIN | 5V  |     | 44  | MICRO-SD | SD2 | SD\_SD0\_DATA1 | SD2 |
| 45  | MIKROBUS (J8-5) | NA  | RZ\_RSPI1\_MISO | 3V3 |     | 46  | MICRO-SD | SD2 | SD\_SD0\_DATA2 | SD2 |
| 47  | MIKROBUS (J8-6) | NA  | RZ\_RSPI1\_MOSI | 3V3 |     | 48  | MICRO-SD | SD2 | SD\_SD0\_DATA3 | SD2 |
| 49  | MIKROBUS (J8-4) | NA  | RZ\_RSPI1\_CK | 3V3 |     | 50  | MICRO-SD | SD2 | RZ\_SD0\_CD | SD2 |
| 51  | AUD\_CODEC, USB-TYPEC, USB-HUB | 3V3 | **RZ\_RIIC1\_SDA** (Was ~RZ\_RIIC1\_SCL~ in SOM Rev 1.1) | 3V3 |     | 52  | USB-HUB | 3V3 | RZ\_RSPI2\_CK | 3V3 |
| 53  | AUD\_CODEC, USB-TYPEC, USB-HUB | 3V3 | **RZ\_RIIC1\_SCL** (Was ~RZ\_RIIC1\_SDA~ in SOM Rev 1.1) | 3V3 |     | 54  | HEADER, DIP-SW | 3V3 | RZ\_RSPI2\_MOSI | 3V3 |
| 55  | BT-FW\_FLASH (J9-39) | NA  | DISP\_DATA8/RZ\_CAN0\_RX |     |     | 56  | NC  |     | RZ\_RSPI2\_MISO | 3V3 |
| 57  | HEADER (CON4) | NA  | DISP\_DATA7/RZ\_CAN0\_TX |     |     | 58  | NC  |     | RZ\_RSPI2\_SSL | 3V3 |
| 59  | BT-FW\_FLASH (J9-30) | NA  | DISP\_DATA12/RZ\_CAN1\_RX |     |     | 60  | NC  |     | RZ\_WDTOVF\_PERROUT | 3V3 |
| 61  | MICRO-SD |     | DISP\_DATA11/RZ\_CAN1\_TX |     |     | 62  | PUSH-B |     | PMIC\_PWRON | 3V3 |
| 63  | 3V3\_IN |     | 3V3\_OUT |     |     | 64  | HEADER, DIP-SW | 3V3 | SD0\_DEV\_SEL | 3V3 |
| 65  | 3V3\_IN |     | 3V3\_OUT |     |     | 66  | NC  |     | PMIC\_EN | 3V3 |
| 67  | 3V3\_IN |     | 3V3\_OUT |     |     | 68  | MICRO-SD | NA  | GPIO\_SD0\_PWR\_EN | 3V3 |
| 69  | 3V3\_IN |     | 3V3\_OUT |     |     | 70  | GND |     | GND |     |
| 71  | VIN\_5V0 |     | VIN\_5V0 |     |     | 72  | GND |     | GND |     |
| 73  | VIN\_5V0 |     | VIN\_5V0 |     |     | 74  | GND |     | GND |     |
| 75  | VIN\_5V0 |     | VIN\_5V0 |     |     | 76  | GND |     | GND |     |
| 77  | VIN\_5V0 |     | VIN\_5V0 |     |     | 78  | GND |     | GND |     |
| 79  | VIN\_5V0 |     | VIN\_5V0 |     |     | 80  | GND |     | GND |     |

<a id="mikrobus"></a>

#### mikroBUS

| **HBP 2.4** | **RZG2L 1.1** |
| --- | --- |
| MIKROBUS (J8-2) | RZ\_SSI0\_RXD |
| MIKROBUS (J8-3) | RZ\_RSPI1\_SSL |
| MIKROBUS (J8-4) | RZ\_RSPI1\_CK |
| MIKROBUS (J8-5) | RZ\_RSPI1\_MISO |
| MIKROBUS (J8-6) | RZ\_RSPI1\_MOSI |
| MIKROBUS (J10-1) | RZ\_SCIF1\_CTS |
| MIKROBUS (J10-2) | RZ\_SCIF1\_RTS |
| MIKROBUS (J10-3) | RZ\_SCIF1\_RXD |
| MIKROBUS (J10-4) | RZ\_SCIF1\_TXD |
| MIKROBUS (J10-5) | RZ\_RIIC0\_SCL |
| MIKROBUS (J10-6) | RZ\_RIIC0\_SDA |

<a id="lcd-parallel-video-output-signals-allocation"></a>

#### LCD (Parallel Video Output) Signals allocation

| **LCD** | **B-to-B connector** |
| --- | --- |
| DISP\_DATA0 | J5001-44 |
| DISP\_DATA1 | J9-52 |
| DISP\_DATA2 | J9-54 |
| DISP\_DATA3 | J9-56 |
| DISP\_DATA4 | J9-58 |
| DISP\_DATA5 | J5001-43 |
| DISP\_DATA6 | J5001-45 |
| DISP\_DATA7 | J9-57 |
| DISP\_DATA8 | J9-55 |
| DISP\_DATA9 | J7-43 |
| DISP\_DATA10 | J7-45 |
| DISP\_DATA11 | J9-61 |
| DISP\_DATA12 | J9-59 |
| DISP\_DATA13 | J7-47 |
| DISP\_DATA14 | J7-49 |
| DISP\_DATA15 | J5001-24 |
| DISP\_DATA16 | J5001-26 |
| DISP\_DATA17 | J7-14 |
| DISP\_DATA18 | J7-16 |
| DISP\_DATA19 | J7-79 (Was J7-59 in SOM Rev 1.1) |
| DISP\_DATA20 | J7-56 |
| DISP\_DATA21 | J7-18 |
| DISP\_DATA22 | J7-20 |
| DISP\_DATA23 | J7-22 |
| DISP\_HSYNC | J7-30 |
| DISP\_VSYNC | J7-32 |
| DISP\_DE | J7-34 |
| DISP\_CLK | J7-24 |

<a id="power-reset"></a>

## Power & Reset

The RZG2L/V2L SOM power source is a single 5V source. It uses Renesas’s PMIC to source all the SOM's power rails. The following figure describes the power architecture.

![](./attachments/image-20221215-091341.png)

The power architecture's main features are:

- Single 5V power source.
- Renesas’s RAA215300 sources the RZG2L/V2L power rails.
- 3.3V output up to 0.6A (Need to calculate system and SOM power).
- Power up sequence is supported by the PMIC configuration.

<a id="power-consumption"></a>

#### POWER CONSUMPTION

<a id="rz-g2l-power-table"></a>

##### RZ/G2L Power Table

| **Mode** | **Voltage** | **Current** | **Power** |
| --- | --- | --- | --- |
| Idle, Linux up | 5V  | 240mA | 1.2W |
| Linux up, wifi connected to 2.4GHz<br><br>and sending packet by iperf3 | 5V  | 400mA | 2W  |
| Linux up, wifi connected to 5GHz and sending packet by iperf3 | 5V  | 430mA | 2.15W |
| Linux up, scanning for bluetooth device | 5V  | 250mA | 1.25W |
| Linux up, GPU stress by glmark2 | 5V  | 460mA | 2.3W |
| Linux up, CPU stress to maximum | 5V  | 400mA | 2W  |
| All utilities are active in the same time (Wifi, GPU stress, CPU stress, Bluetooth) | 5V  | 670mA | 3.35W |

<a id="rz-v2l-power-table"></a>

##### RZ/V2L Power Table

| **Mode** | **Voltage** | **Current** | **Power** |
| --- | --- | --- | --- |
| Idle, Linux up | 5V  | 240mA | 1.2W |
| Linux up, wifi connected to 2.4GHz<br><br>and sending packet by iperf3 | 5V  | 384mA | 1.94W |
| Linux up, wifi connected to 5GHz and sending packet by iperf3 | 5V  | 427mA | 2.135W |
| Linux up, scanning for bluetooth device | 5V  | 255mA | 1.275W |
| Linux up, GPU stress by glmark2 | 5V  | 480mA | 2.4W |
| Linux up, CPU stress to maximum | 5V  | 384mA | 1.92W |
| Linux up, AI tested with web camera | 5V  | 864mA | 4.32W |
| All utilities are active in the same time (Wifi, GPU stress, CPU stress, Bluetooth) | 5V  | 528mA | 2.64W |

<a id="reset"></a>

#### RESET

The PMIC generates the POR. A reset signal (PMIC\_CRST\_IN#) from the carrier board can generate a POR.

The PMIC supports a Power ON/OFF\* signal to disable/enable all power signals besides RTC.

The PMIC supports an RTC that can be powered by a battery (J7-63).

> [!INFO]
> **(\*) Note – The PMIC enables the power at Power-Up (No need to push the ON/OFF).**

<a id="rzg2l-v2l-integration-manual"></a>

## RZG2L/V2L INTEGRATION MANUAL

<a id="power-up-sequence"></a>

#### POWER UP SEQUENCE

A single 5V input sources the RZG2L/V2L. The PMIC supports all power sequences.

When using the SOM 3.3V output there is no need to consider its power sequence. If an external power source is used for the 3.3V, it must be powered according to the power sequence rules. (See RZG2L/V2L datasheet for details)

<a id="booting-options"></a>

#### BOOTING OPTIONS

<a id="strap-pins-booting"></a>

##### Strap pins Booting

The RZG2L/V2L boost from different NVM or serial interfaces according to external resistors setting. The boot configuration is set by the three configuration signals (MD0, MD1, and MD2) and a selection signal (SD0\_DEV\_SEL) that select between eMMC and uSD (Mux on SOM). Below is a table describing the configuration modes. 

| **MD2**<br><br>J5001-41 | **MD1**<br><br>J5001-5 | **MD0**<br><br>J5001-3 | **SD0\_DEV\_SEL**<br><br>J9-64 | **MODE** |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | uSD (Start up 3.3V) |
| 0   | 0   | 1   | 1   | eMMC (1.8V) |
| 0   | 1   | 1   | N/A | SPI Single/Quad/Octal (1.8V) |
| 1   | 0   | 1   | N/A | SCIF Download |

> [!INFO]
> Note – There are setting resistors on the SOM, but they are not assembled in the default configuration. Setting is done on the carrier board.

<a id="i2c-interfaces"></a>

#### I2C INTERFACES

The RZG2L/V2L uses I2C2 (PMIC) interfaces for its internal configurations.

<a id="gpio-interfaces"></a>

#### GPIO INTERFACES

The RZG2L/V2L SOM uses some GPIO signals for its internal controls. The following table describes the GPIO allocation.

| **Signal** | **I/O** | **Description** | **Remarks** |
| --- | --- | --- | --- |
| ENET\_nINT | P27\_0 | Ethernet interrupt | Active Low |
| ENET1\_nINT | P42\_4 | Ethernet 1 interrupt | Active Low |
| WL\_REG\_ON | P23\_1 | Enable the WLAN | Active High |
| BT\_REG\_ON | P23\_0 | Enable the BT | Active High |

<a id="mechanical-description"></a>

## Mechanical Description

Following is a diagram of the TOP VIEW of the RZG2L/V2L.

![](./attachments/image-20231011-083955.png)

<a id="som-version-changes"></a>

## **SOM Version Changes:**

| **SOM Version** | **SOM Version Changes** |
| --- | --- |
| 1.0 | Prototype Version |
| 1.1 | 1. Swapping between **TX\_CLK** and **TX\_CTL** in the Ethernet PHYs<br>2. Connecting **ETH0** power to **3V3** |
| 1.2 | 1. Connect the **WIFI** clock (**PMIC\_32KHz\_CLK**) to Pull Up<br>2. Move **RZ\_P5\_1** from J7-33 to J7-13 to support M.2 Reset on the HBP<br>3. Move **RZ\_P5\_0** from J7-39 to J7-15<br>4. Move **RZ\_P5\_2** from J7-37 to J7-8<br>5. Enable power control from BtB. Adding U14 (PU/PD select)<br>6. Move **RZ\_P16\_0** from J7-59 to J7-79<br>7. Add **AUDIO\_CLK** to J7-59<br>8. Add **R116** to support **RTC** clock from **MPIO2**.<br>9. Swapping I2C1 pins on J9: J9-51-SDA, J9-53-SCL. |

<a id="documentation"></a>

## Documentation

      

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-6cea4cd3-6f09-4a2c-9ea5-b32cd59736b8)<br><br>[Preview] [View](/wiki/download/attachments/511148033/rzg2l-and-rzv2l-som-rev1.2-simplified-schematics.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=511148033&fileName=rzg2l-and-rzv2l-som-rev1.2-simplified-schematics.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=511148033&fileName=rzg2l-and-rzv2l-som-rev1.2-simplified-schematics.pdf) | PDF File [rzg2l-and-rzv2l-som-rev1.2-simplified-schematics.pdf](/wiki/download/attachments/511148033/rzg2l-and-rzv2l-som-rev1.2-simplified-schematics.pdf?api=v2) | Dec 31, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |

[RZG2L_pinfunction_List_r1.1.xlsx](./attachments/RZG2L_pinfunction_List_r1.1.xlsx)

[Buy a Sample Now](https://www.solid-run.com/embedded-industrial-iot/renesas-rz-family/rz-g2l-som/)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden