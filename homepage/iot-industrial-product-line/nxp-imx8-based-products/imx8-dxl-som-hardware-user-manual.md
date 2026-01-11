# i.MX8 DXL SOM Hardware User Manual

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 14 Feb 2024 | Noam Weidenfeld | 1.0 |     |
| Oct 9, 2024 | Josua Mayer | 1.1 | Added missing Tables for odd numbered pins of b2b connectors |
| Nov 10, 2024 | Josua Mayer | 1.2 | Added u.FL connector labels |
| Table of Contents | - [Revisions and Notes](#revisions-and-notes)<br>- [Introduction](#introduction)<br>- [Overview](#overview)<br>  - [Highlighted Features](#highlighted-features)<br>  - [Supporting Products](#supporting-products)<br>- [Description](#description)<br>  - [Block Diagram](#block-diagram)<br>  - [Features Summary](#features-summary)<br>- [Core System Components](#core-system-components)<br>  - [i.MX8-XLite SoC Family](#imx8-xlite-soc-family)<br>  - [Memories](#memories)<br>    - [LPDDR4](#lpddr4)<br>    - [eMMC NAND Flash](#emmc-nand-flash)<br>    - [Quad Serial NOR Flash (Carrier)](#quad-serial-nor-flash-carrier)<br>    - [EEPROM (SOM)](#eeprom-som)<br>    - [Micro-SD (Not Supported)](#micro-sd-not-supported)<br>  - [V2X Modem (SDR)](#v2x-modem-sdr)<br>  - [Sensors](#sensors)<br>- [IMX8-XLite External Interfaces](#imx8-xlite-external-interfaces)<br>  - [General](#general)<br>  - [Supported Interfaces](#supported-interfaces)<br>    - [PCIe](#pcie)<br>    - [USB-2](#usb-2)<br>    - [RGMI](#rgmi)<br>    - [FlexCAN](#flexcan)<br>    - [FlexSPI](#flexspi)<br>    - [LPSPI](#lpspi)<br>    - [Ultra Secured Digital Host Controller (uSDHC)](#ultra-secured-digital-host-controller-usdhc)<br>  - [B2B Connector’s Signal Description](#b2b-connectors-signal-description)<br>    - [J13 (odd)](#j13-odd)<br>    - [J13 (even)](#j13-even)<br>    - [J14 (odd)](#j14-odd)<br>    - [J14 (even)](#j14-even)<br>- [Power and Reset](#power-and-reset)<br>  - [Power Architecture](#power-architecture)<br>  - [Reset](#reset)<br>- [IMX8-XLite Integration Manual](#imx8-xlite-integration-manual)<br>  - [Booting Options](#booting-options)<br>  - [I2C Interfaces](#i2c-interfaces)<br>  - [GPIO Interfaces](#gpio-interfaces)<br>  - [IMX8-XLite SOM Debugging Capability](#imx8-xlite-som-debugging-capability)<br>- [Mechanical Description](#mechanical-description)<br>- [Ordering Information](#ordering-information)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

> [!INFO]
> No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.

<a id="introduction"></a>

## Introduction

This User Manual relates to the SolidRun IMX8 DXL series, which includes.

- Dual core ARM A35 (1.2GHz) w Cortex-M4 (266 MHz).
- Single core ARM A35 (1.2GHz) w Cortex-M4 (266 MHz).

<a id="overview"></a>

## Overview

The SolidRun’s SR-SOM-MX8 family is a high-performance micro system on module (S.O.M.) based on the highly integrated Freescale i.MX8M family of products including the IMX8M, IMX8M-Mini, IMX8M-Plus and IMX8 DXL.

The IMX8 DXL is targeting the Automotive After-Market.

<a id="highlighted-features"></a>

#### Highlighted Features

- Ultra-small footprint SOM (50x35mm) including two board-to-board connectors (160 total pins number).
- Freescale i.MX8 DXL SoC supports Solo and DUAL Lite versions.
  - Up to Dual Cortex A35 and up to 1.2GHz
  - Cortex-M4 subsystem processor supports real time tasks.
  - High security engines and Tamper detection.
  - A single Ethernet interface (RGMII).
  - Two USB 2.0 (OTG) interfaces.
  - Up to three CAN interfaces.
  - A single PCIe 3.0 interface.
  - High industrial reliability with in-line ECC on LPDDR and on on-chip RAM.
- LPDDR4 memory in x16 configurations supports up to 4GB and up to 2.4GT/s.
- Up to 64GB eMMC.
- SAF5400 DSRC modem/dual antenna (u.FL) and AFE supporting the V2X application.
- SFX1800 security element for the V2X applications.
- MIA-M10Q GPS (u.FL) module supporting all protocols.
- 3D accelerometer and 3D gyroscope, Barometer and Magnetometer sensors support.
- Power management devices
- Automotive temperature grade support.

<a id="supporting-products"></a>

#### Supporting Products

The following products are provided from SolidRun both as production level platforms and as reference examples on how to incorporate the SOM in different levels of integration:

- HummingBoard V2X– A board computer that incorporates the SOM retains the same Android and different Linux distributions while adding extra hardware functionalities and access to the hardware.

<a id="description"></a>

## Description

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the IMX8 DXL Blocks Diagram.

![image-20240214-105413.png](./attachments/image-20240214-105413.png)

<a id="features-summary"></a>

#### Features Summary

Following is the features summary of the SOM. Notice that some of the features are pinout multiplexed (please refer to the pin mux table below and the Freescale i.MX8-XLite data sheets):

- Ultra-small footprint SOM (50x35mm) including two board-to-board connectors (160 total pins number).
- Freescale i.MX8 DXL SoC supports Solo and DUAL Lite versions.
  - Up to Dual Cortex A35 and up to 1.2GHz
  - Cortex-M4 subsystem processor supports real time tasks.
  - High security engines and Tamper detection.
  - A single Ethernet interface (RGMII).
  - Two USB 2.0 (OTG) interfaces.
  - Up to three CAN interfaces.
  - A single PCIe 3.0 interface.
  - High industrial reliability with in-line ECC on LPDDR and on on-chip RAM.
- LPDDR4 memory in x16 configurations supports up to 4GB and up to 2.4GT/s.
- Up to 64GB eMMC.
- SAF5400 DSRC modem/dual antenna (u.FL) and AFE supporting the V2X application.
- SFX1800 security element for the V2X applications.
- MIA-M10Q GPS (u.FL) module supporting all protocols.
- 3D accelerometer and 3D gyroscope, Barometer and Magnetometer sensors support.
- Power management devices
- Automotive temperature grade support.

<a id="core-system-components"></a>

## Core System Components

<a id="imx8-xlite-soc-family"></a>

### i.MX8-XLite SoC Family

The IMX8 XLite family of processors includes the i.MX 8DualXLite and i.MX 8SoloXLite. These devices target the automotive and industrial market segments.

These devices are designed to achieve both high performance and low power consumption.

The following figure describes the CPU block diagram.

![image-20240214-105520.png](./attachments/image-20240214-105520.png)

<a id="memories"></a>

### Memories

The IMX8-XLite SOM supports varieties of memory interfaces for booting and data storage. The following figure describes the IMX-8 SOM memory interfaces.

![image-20240214-105653.png](./attachments/image-20240214-105653.png)

<a id="lpddr4"></a>

#### **LPDDR4**

- Up to 4GB memory space.
- 16 Bits data bus.
- Up to 2400 MT/s.
- Inline ECC.

<a id="emmc-nand-flash"></a>

#### **eMMC NAND Flash**

- Up to 64GB memory space.
- 8 Bits data bus.
- Support MMC standard, up to version 5.1.
- uSDHC-0.
- Can be used as BOOT NVM

<a id="quad-serial-nor-flash-carrier"></a>

#### **Quad Serial NOR Flash (Carrier)**

- Can be configured as 1/2/4-bit operation.
- Support both SDR mode and DDR mode
- No reset
- QSPIA/nSS0.
- Can be used as BOOT NVM.

<a id="eeprom-som"></a>

#### **EEPROM (SOM)**

- 1Kb EEPROM
- ON-Semi’s CAT24AA01TDI or compatible
- I2C2
- Address 0X50 (7 bits format)
- Stores SOM’s configurations.

<a id="micro-sd-not-supported"></a>

#### **Micro-SD (Not Supported)**

<a id="v2x-modem-sdr"></a>

### V2X Modem (SDR)

The SOM support One-chip V2X transceiver and baseband, with dual antenna

and ECDSA support. The SDR architecture enables support for V2X applications all over the world (for example, North America, Japan, and Europe).

SAF5400 is a transceiver with integrated SDR processor, providing a system solution for Vehicle-to-Vehicle and Vehicle-to-Infrastructure applications.

The following figure describes the V2X modem architecture.

![image-20240214-105844.png](./attachments/image-20240214-105844.png)

The V2X modem integrates the following elements:

- SAF5400 V2X transceiver and baseband, with dual antenna and ECDSA support.
- Two Analog Front End parts controlled by the SAF5400.
- Passive elements for RF line calibration\*.
- U.FL connectors (labeled J15 / J16).

- The modem was calibrated to support the V2X (SDR) standards using the u.FL connectors

The SOM integrates a security chip (SXF1800) and a GPS module (MIA-M10Q) to support the V2X Modem.

**SXF1800:**

SXF1800 is based on highly secure microcontroller used also to protect mobile payments, providing highest proven assets protection.

For more information check the SXF1800 link:

[SXF1800 | V2X Secure Element | NXP Semiconductors](https://www.nxp.com/products/wireless-connectivity/dsrc-safety-modem/secure-element-ic-for-v2x-communication:SXF1800)

**MIA-M10Q:**

The M10 platform supports concurrent reception of four GNSS (GPS, GLONASS, Galileo, and BeiDou).

Antenna connector is u.FL (labeled J17).

For more details check the MIA-M10Q datasheet:

[MIA-M10 series | u-blox](https://www.u-blox.com/en/product/mia-m10-series)

<a id="sensors"></a>

### Sensors

The IMX8-XLite SOM integrates three MEM sensors. The figure below describes the sensors integration.

![image-20240214-105955.png](./attachments/image-20240214-105955.png)

**ISM330 - 3D accelerometer and 3D gyroscope**

- 3D accelerometer with selectable full scale: ±2/±4/±8/±16 g.
- 3D gyroscope with extended selectable full scale: ±125/±250/±500/±1000/±2000/±4000 dps.

For more details see: [ISM330DHCX - iNEMO inertial module with Machine Learning Core, Finite State Machine with digital output for industrial applications. - STMicroelectronics](https://www.st.com/en/mems-and-sensors/ism330dhcx.html)

**ILPS22QS – Barometer**

- Selectable dual full-scale absolute pressure range
- Mode 1: 260 ~ 1260 hPa

– Mode 2: 260 ~ 4060 hPa

For more information see: [Datasheet - ILPS22QS - Dual full-scale, 1260 hPa and 4060 hPa, absolute digital output barometer with embedded Qvar electrostatic sensor](https://www.st.com/resource/en/datasheet/ilps22qs.pdf)

**IIS2MDCTR – Magnetometer**

- High-accuracy, ultra-low-power 3-axis digital magnetic sensor.
- Magnetic field dynamic range up to ±50 gauss.

For more information see: [IIS2MDC - High accuracy, ultra-low-power ,3-axis digital output magnetometer - STMicroelectronics](https://www.st.com/en/mems-and-sensors/iis2mdc.html)

<a id="imx8-xlite-external-interfaces"></a>

## IMX8-XLite External Interfaces

<a id="general"></a>

### General

The SOM integrates three Hirose DF40 board-to-board headers.

The selection of the Hirose DF40 is due to the following criteria:

- Miniature (0.4m pitch)
- Highly reliable manufacturer
- Availability (worldwide distribution channels)
- Excellent signal integrity (supports 6Gbps)
  - Please contact Hirose or SolidRun for reliability and test result data.

<a id="supported-interfaces"></a>

### Supported Interfaces

<a id="pcie"></a>

#### PCIe

The IMX8-XLite SOM supports a single PCIe interfaces. The following figure describes the PCIe interfaces.

![image-20240214-111049.png](./attachments/image-20240214-111049.png)

The PCIe main features are:

- On board coupling capacitors for TX and CLK.
- Generates the PCIe clock.
- 1× PCIe 3.0 (1-lane) with L1 substate support.
- PCIe 1.0 and 2.0 compliant.
- Maximum link speed up to Gen3 (8 GT/s).
- Support PCIe control signals: CLKREQ, WAKE and PERST.

For more details se the CPU datasheet. [i.MX 8XLite Applications Processors for Telematics, V2X and Industrial Control | NXP Semiconductors](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8xlite-applications-processors-for-telematics-v2x-and-industrial-control:iMX8XLite)

<a id="usb-2"></a>

#### USB-2

The IMX8-XLite supports two USB interfaces. The following figure describes the USB interfaces.

![image-20240214-111130.png](./attachments/image-20240214-111130.png)

The USB main features are:

- USB1 and USB2 are directly connected to the CPU (No HUB).
- Two USB2.0 OTG controller.
- High Speed (480 Mbps), full speed (12 Mbps) and low speed (1.5Mbps).
- Fully compatible with the USB On-The-Go supplement to the USB 2.0 specification.
- Fully compatible with the USB 2.0 specification.
- Power control signal is not part of the USB module, any available GPIO can be used.

For more details see the CPU datasheet. [i.MX 8XLite Applications Processors for Telematics, V2X and Industrial Control | NXP Semiconductors](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8xlite-applications-processors-for-telematics-v2x-and-industrial-control:iMX8XLite)

> [!NOTE]
> **Note – The voltage on VBUS can support 5V.**

<a id="rgmi"></a>

#### RGMI

The IMX8-XLite supports an RGMII interface connected to the BtB connectors. The following figure describes the RGMII interface.

![image-20240214-111224.png](./attachments/image-20240214-111224.png)

- Gigabit Ethernet Media Access Controller (MAC) designed to support both10/100 /1000 Mbps Ethernet/IEEE 802.3 networks with Audio Video Bridging (AVB) capabilities.
- hardware support for IEEE1588 Precision Time Protocol (PTP) v2.0.
- MDC/MDIO management link.

For more details see the CPU datasheet. [i.MX 8XLite Applications Processors for Telematics, V2X and Industrial Control | NXP Semiconductors](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8xlite-applications-processors-for-telematics-v2x-and-industrial-control:iMX8XLite)

<a id="flexcan"></a>

#### FlexCAN

The IMX8-XLite supports up to three FlexCAN interfaces. Main features are:

- CAN with Flexible Data rate (CAN FD) protocol and the CAN protocol according to the CAN 2.0B protocol specification.
- Compliant with the ISO 11898-1:2015 standard.

[i.MX 8XLite Applications Processors for Telematics, V2X and Industrial Control | NXP Semiconductors](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8xlite-applications-processors-for-telematics-v2x-and-industrial-control:iMX8XLite)

<a id="flexspi"></a>

#### FlexSPI

- Single Quad SPI/Octal SPI.
- Single, dual, quad, and octal mode of operation.
- Support for flash data strobe signal for data sampling in DDR and SDR mode.

[i.MX 8XLite Applications Processors for Telematics, V2X and Industrial Control | NXP Semiconductors](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8xlite-applications-processors-for-telematics-v2x-and-industrial-control:iMX8XLite)

<a id="lpspi"></a>

#### LPSPI

- Two SPI interfaces.
- Can be configured either as a master or slave.
- Supports DMA accesses and generates DMA requests.

<a id="ultra-secured-digital-host-controller-usdhc"></a>

#### Ultra Secured Digital Host Controller (uSDHC)

- Single 4-bits interface.
- Provides the interface between the host system and the eMMC, SD card, and SDIO.
- Compatible with the eMMC System Specification version 4.2/4.3/4.4/4.41/5.0/5.1.
- Compatible with the SD Memory Card Specification version 3.0 and supports the Extended Capacity SD Memory Card.
- Compatible with the SDIO Specification version 2.0/3.0.
- Card bus clock frequency up to 104 MHz.

For more details see the CPU datasheet. [i.MX 8XLite Applications Processors for Telematics, V2X and Industrial Control | NXP Semiconductors](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8xlite-applications-processors-for-telematics-v2x-and-industrial-control:iMX8XLite)

<a id="b2b-connectors-signal-description"></a>

### B2B Connector’s Signal Description

<a id="j13-odd"></a>

#### **J13 (odd)**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **PIN** | **SOM (J13)** |     | **Reference Carrier (J9)** |     |
| 1   | **PCIE0\_RX\_P** |     | PCIE0\_RX\_P |     |
| 3   | **PCIE0\_RX\_N** |     | PCIE0\_RX\_N |     |
| 5   | **GND** |     | GND |     |
| 7   | **PCIE0\_TX\_P** |     | PCIE0\_TX\_P |     |
| 9   | **PCIE0\_TX\_N** |     | PCIE0\_TX\_N |     |
| 11  | **GND** |     | GND |     |
| 13  | **PCIE\_REF\_CLK\_P** |     | PCIE\_REF\_CLK\_P |     |
| 15  | **PCIE\_REF\_CLK\_N** |     | PCIE\_REF\_CLK\_N |     |
| 17  | **GND** |     | GND |     |
| 19  | **NC** |     | NC  |     |
| 21  | **NC** |     | NC  |     |
| 23  | **GND** |     | GND |     |
| 25  | **NC** |     | NC  |     |
| 27  | **NC** |     | NC  |     |
| 29  | **GND** |     | GND |     |
| 31  | **NC** |     | NC  |     |
| 33  | **NC** |     | NC  |     |
| 35  | **GND** |     | GND |     |
| 37  | **NC** |     | NC  |     |
| 39  | **NC** |     | NC  |     |
| 41  | **GND** |     | GND |     |
| 43  | **NC** |     | NC  |     |
| 45  | **NC** |     | NC  |     |
| 47  | QSPI0\_DATA0 (GPIO3\_IO09) | 1V8 | QSPI0\_DATA0 (QSPI Flash) | 1V8 |
| 49  | QSPI0\_DATA1 (GPIO3\_IO10) | 1V8 | QSPI0\_DATA1 (QSPI Flash) | 1V8 |
| 51  | QSPI0\_DATA2 (GPIO3\_IO11) | 1V8 | QSPI0\_DATA2 (QSPI Flash) | 1V8 |
| 53  | QSPI0\_DATA3 (GPIO3\_IO12) | 1V8 | QSPI0\_DATA3 (QSPI Flash) | 1V8 |
| 55  | QSPI0\_DQS (GPIO3\_IO13) | 1V8 | QSPI0\_DQS (QSPI Flash) | 1V8 |
| 57  | QSPI0A\_SS0\_B (GPIO3\_IO14) | 1V8 | QSPI0A\_SS0\_B (QSPI Flash) | 1V8 |
| 59  | QSPI0A\_SCLK (GPIO3\_IO16) | 1V8 | QSPI0A\_SCLK (QSPI Flash) | 1V8 |
| 61  | **GND** |     | GND |     |
| 63  | **SYS\_RST\_1V8\_B** | 1V8 | SYS\_RST\_1V8\_B (QSPI Flash) | 1V8 |
| 65  | **MANUAL\_RST\_B** | 1V8 | SYS\_nRST | 1V8 |
| 67  | **ON\_OFF\_BUTTON** | 1V8 | NC  |     |
| 69  | MCLK\_OUT0 (GPIO0\_IO20) | 1V8 | IO\_INT# (I2C IO Exp.) | 1V8 |
| 71  | SPI3\_CS0 (GPIO0\_IO16) | 1V8 | USB\_HUB\_CH1\_PWR\_EN | 1V8 |
| 73  | **SCU\_BOOT\_MODE0** | 1V8 | BOOT (S1-1) | 1V8 |
| 75  | **GND** |     | GND |     |
| 77  | **SCU\_BOOT\_MODE1** | 1V8 | BOOT (S1-2) | 1V8 |
| 79  | **SCU\_BOOT\_MODE2** | 1V8 | BOOT (PD) |     |

<a id="j13-even"></a>

#### **J13 (even)**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **PIN** | **SOM (J13)** |     | **Reference Carrier (J9)** |     |
| 2   | PCIE\_CTRL\_CLKREQ\_B (GPIO4\_IO01, GPIO07\_IO01) | 3V3 | EXT. (J21-48) |     |
| 4   | PCIE\_CTRL\_WAKE\_B (GPIO4\_IO02, GPIO07\_IO02) | 3V3 | EXT. (J21-50) |     |
| 6   | GND |     | GND |     |
| 8   | PCIE\_CTRL\_PERST\_B (GPIO4\_IO00, GPIO07\_IO00) | 3V3 | EXT. (J21-52) |     |
| 10  | SPI3\_CS1 | 1V8 | NC  |     |
| 12  | SPI3\_SCK (GPIO0\_IO13) | 1V8 | BT\_REG\_ON (WI-FI Module) | 1V8 |
| 14  | SPI3\_SDO (GPIO0\_IO14) | 1V8 | RF\_PWR (Cellular Power) | 1V8 |
| 16  | SPI3\_SDI (GPIO0\_IO15) | 1V8 | WL\_REG\_ON (WI-FI Module) |     |
| 18  | NC  |     | NC  |     |
| 20  | (GPIO2\_IO08\_IN, GPIO6\_IO022\_IN) | 3V3 | DEV\_CFG\_N (SJA1110AEL) | 3V3 |
| 22  | NC  | 1V8 | NC  |     |
| 24  | M40\_UART0\_TX (GPIO1\_IO11, M40\_GPIO0\_IO03) | 1V8 | RESET\_N (LTE-EG25) | 1V8 |
| 26  | M40\_UART0\_RX (GPIO1\_IO12, M40\_GPIO0\_IO02) | 1V8 | PWRKEY (LTE-EG25) | 1V8 |
| 28  | BB\_USDHC2\_CLK (GPIO4\_IO29) | 1V8 | BB\_USDHC2\_CLK (WI-FI Module) | 1V8 |
| 30  | BB\_USDHC2\_DAT3 (GPIO5\_IO02) | 1V8 | BB\_USDHC2\_DAT3 (WI-FI Module) | 1V8 |
| 32  | BB\_USDHC2\_DAT2 (GPIO5\_IO01) | 1V8 | BB\_USDHC2\_DAT2 (WI-FI Module) | 1V8 |
| 34  | BB\_USDHC2\_DAT1 (GPIO5\_IO00) | 1V8 | BB\_USDHC2\_DAT1 (WI-FI Module) | 1V8 |
| 36  | BB\_USDHC2\_DAT0 (GPIO4\_IO31) | 1V8 | BB\_USDHC2\_DAT0 (WI-FI Module) | 1V8 |
| 38  | BB\_USDHC2\_CMD (GPIO4\_IO30) | 1V8 | BB\_USDHC2\_CMD (WI-FI Module) | 1V8 |
| 40  | NC  |     | NC  |     |
| 42  | GND | 3V3(PU) |     |     |
| 44  | ENET\_PHY\_MDIO (GPIO5\_IO10, GPIO07\_IO16) | 3V3(PU) | ENET\_PHY\_MDIO (SJA1110AEL) | 3V3 |
| 46  | ENET\_PHY\_MDC (GPIO5\_IO11, GPIO07\_IO17) | 3V3 | ENET\_PHY\_MDC (SJA1110AEL) | 3V3 |
| 48  | GND |     | GND |     |
| 50  | NC  |     | NC  |     |
| 52  | TERMINAL\_UART0\_TX | 3V3 | TERMINAL\_UART0\_TX | 3V3 |
| 54  | TERMINAL\_UART0\_RX | 3V3 | TERMINAL\_UART0\_RX | 3V3 |
| 56  | NC  |     | NC  |     |
| 58  | GND |     | GND |     |
| 60  | SCU\_UART0\_TX (SCU\_GPIO0\_IO01) | 1V8 | NC  |     |
| 62  | SCU\_UART0\_RX (SCU\_GPIO0\_IO00, GPIO2\_IO03) | 1V8 | NC  |     |
| 64  | GND |     | GND |     |
| 66  | MCLK\_IN0 (GPIO0\_IO19) | 1V8 | PTP\_CLK (SJA1110AEL) |     |
| 68  | MCLK\_IN1 | 1V8 | NC  |     |
| 70  | GND |     | GND |     |
| 72  | UART1\_RX (GPIO0\_IO22) | 1V8 | UART1\_RX (WI-FI Module) (J21-40) | 1V8 |
| 74  | UART1\_TX (GPIO0\_IO21) | 1V8 | UART1\_TX (WI-FI Module) (J21-42) | 1V8 |
| 76  | GND |     | GND |     |
| 78  | UART1\_CTS\_B (GPIO0\_IO24) | 1V8 | UART1\_CTS\_B (WI-FI Module) (J21-46) | 1V8 |
| 80  | UART1\_RTS\_B | 1V8 | UART1\_RTS\_B (WI-FI Module) (J21-44) | 1V8 |

<a id="j14-odd"></a>

#### **J14 (odd)**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **PIN** | **SOM (J14)** |     | **Reference Carrier (J16)** |     |
| 1   | **NC** |     | NC  |     |
| 3   | **NC** |     | NC  |     |
| 5   | **GND** | 3V3 | GND |     |
| 7   | FLEXCAN0\_RX (GPIO1\_IO15, GPIO06\_IO08) | 3V3 | FLEXCAN0\_RX (CAN Transceiver) | 3V3 |
| 9   | FLEXCAN0\_TX (GPIO1\_IO16, GPIO06\_IO09) |     | FLEXCAN0\_TX (CAN Transceiver) | 3V3 |
| 11  | **GND** | 3V3 | GND |     |
| 13  | FLEXCAN1\_RX (GPIO1\_IO17, GPIO06\_IO10) | 3V3 | FLEXCAN1\_RX (CAN Transceiver) | 3V3 |
| 15  | FLEXCAN1\_TX (GPIO1\_IO18, GPIO06\_IO11) |     | FLEXCAN1\_TX (CAN Transceiver) | 3V3 |
| 17  | **GND** |     | GND |     |
| 19  | **NC** |     | NC  |     |
| 21  | **NC** |     | NC  |     |
| 23  | **GND** | 3V3 | GND |     |
| 25  | FLEXCAN2\_RX (GPIO1\_IO19, GPIO06\_IO12) | 3V3 | FLEXCAN2\_RX (J21-36) | 3V3 |
| 27  | FLEXCAN2\_TX (GPIO1\_IO20, GPIO06\_IO13) |     | FLEXCAN2\_TX (J21-34) | 3V3 |
| 29  | **NC** | 3V3 (PU) | NC  |     |
| 31  | I2C3\_SCL (GPIO3\_IO02) | 3V3 (PU) | I2C3\_SCL | 3V3 |
| 33  | I2C3\_SDA (GPIO3\_IO03) |     | I2C3\_SDA | 3V3 |
| 35  | **GND** | 3V3 | GND |     |
| 37  | ENET1\_PHY\_INT\_B (GPIO2\_IO05\_IN, GPIO06\_IO19\_IN) | 3V3 | ENET1\_PHY\_INT\_B (J21-30) | 3V3 |
| 39  | **USB\_OTG2\_ID** | 3V3 | NC  | 3V3 |
| 41  | **USB\_OTG1\_ID** | 5V  | NC  | 3V3 |
| 43  | **OTG1\_VBUS** | 3V3 | USB\_5V | 5V  |
| 45  | SPI0\_SDI (GPIO1\_IO05,M40\_GPIO00\_IO02) | 3V3 | SPI0\_SDI (SJA1110AEL) (J21-31) | 3V3 |
| 47  | SPI0\_SDO (GPIO1\_IO06,M40\_GPIO00\_IO01) | 3V3 | SPI0\_SDO (SJA1110AEL) (J21-33) | 3V3 |
| 49  | SPI0\_SCK (GPIO1\_IO04,M40\_GPIO00\_IO00) | 3V3 (PU) | SPI0\_SCK (SJA1110AEL) (J21-35) | 3V3 |
| 51  | I2C2\_SDA (GPIO3\_IO00) | 3V3 (PU) | I2C2\_SDA | 3V3 |
| 53  | I2C2\_SCL (GPIO3\_IO01) | 1V8 | I2C2\_SCL | 3V3 |
| 55  | **VDD\_1V8 (OUT)** | 1V8 | SOM's PMIC | 1V8 |
| 57  | **VDD\_1V8 (OUT)** | 1V8 | SOM's PMIC | 1V8 |
| 59  | **VDD\_1V8 (OUT)** | 1V8 | SOM's PMIC | 1V8 |
| 61  | **VDD\_1V8 (OUT)** | 3V3 | SOM's PMIC | 1V8 |
| 63  | **VDD\_3V3 (OUT)** | 3V3 | SOM's PMIC | 3V3 |
| 65  | **VDD\_3V3 (OUT)** | 3V3 | SOM's PMIC | 3V3 |
| 67  | **VDD\_3V3 (OUT)** | 3V3 | SOM's PMIC | 3V3 |
| 69  | **VDD\_3V3 (OUT)** | 5V  | SOM's PMIC | 3V3 |
| 71  | **VIN** | 5V  | VIN | 5V  |
| 73  | **VIN** | 5V  | VIN | 5V  |
| 75  | **VIN** | 5V  | VIN | 5V  |
| 77  | **VIN** | 5V  | VIN | 5V  |
| 79  | **VIN** |     | VIN | 5V  |

<a id="j14-even"></a>

#### **J14 (even)**

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **PIN** | **SOM (J14)** |     | **Reference Carrier (J16)** |     |
| 2   | GND |     | GND |     |
| 4   | NC  |     | NC  |     |
| 6   | NC  |     | NC  |     |
| 8   | GND |     | GND |     |
| 10  | USB\_OTG1\_PWR (GPIO4\_IO03, GPIO07\_IO03) | 3V3 | SW\_RSTn (SJA1110AEL) | 3V3 |
| 12  | USB\_OTG2\_PWR (GPIO4\_IO04, GPIO07\_IO04) | 3V3 | SW\_CORE\_RSTn (SJA1110AEL) | 3V3 |
| 14  | GND |     | GND |     |
| 16  | USB\_OTG1\_DP |     | USB\_OTG1\_DP (J26-6) |     |
| 18  | USB\_OTG1\_DN |     | USB\_OTG1\_DN (J26-5) |     |
| 20  | GND |     | GND |     |
| 22  | USB\_OTG2\_DP |     | USB\_OTG2\_DP (LTE-EG25) |     |
| 24  | USB\_OTG2\_DN |     | USB\_OTG2\_DN (LTE-EG25) |     |
| 26  | GND |     | GND |     |
| 28  | USB\_OTG2\_OC (GPIO4\_IO06, GPIO07\_IO06) | 3V3 | INT\_N (SJA1110AEL) | 3V3 |
| 30  | USB\_OTG1\_OC (GPIO4\_IO05, GPIO07\_IO05) | 3V3 | SW\_PE (SJA1110AEL's Power Enable) | 3V3 |
| 32  | SPI0\_CS0 (GPIO1\_IO08,M40\_GPIO00\_IO03) | 3V3 | SPI0\_CS0 (SJA1110AEL) | 3V3 |
| 34  | SPI0\_CS1 (GPIO1\_IO07) | 3V3 | SPI0\_CS1 (SJA1110AEL) | 3V3 |
| 36  | GND |     | GND |     |
| 38  | ENET1\_RGMII\_TXC (GPIO0\_IO00) | 3V3 | ENET1\_RGMII\_TXC (SJA1110AEL) | 3V3 |
| 40  | ENET1\_RGMII\_TX\_CTL (GPIO0\_IO02) | 3V3 | ENET1\_RGMII\_TX\_CTL (SJA1110AEL) | 3V3 |
| 42  | ENET1\_RGMII\_TXD0 (GPIO0\_IO08, GPIO06\_IO02) | 3V3 | ENET1\_RGMII\_TXD0 (SJA1110AEL) | 3V3 |
| 44  | ENET1\_RGMII\_TXD1 (GPIO0\_IO09, GPIO06\_IO03) | 3V3 | ENET1\_RGMII\_TXD1 (SJA1110AEL) | 3V3 |
| 46  | ENET1\_RGMII\_TXD2 (GPIO0\_IO01) | 3V3 | ENET1\_RGMII\_TXD2 (SJA1110AEL) | 3V3 |
| 48  | ENET1\_RGMII\_TXD3 (GPIO0\_IO03) | 3V3 | ENET1\_RGMII\_TXD3 (SJA1110AEL) | 3V3 |
| 50  | NC  |     | NC  |     |
| 52  | OTG2\_VBUS | 5V  | USB\_5V | 5V  |
| 54  | NC  |     | NC  |     |
| 56  | V\_BCKP | 3V3 | NC  | 3V3 |
| 58  | ENET1\_RGMII\_RXC (GPIO0\_IO04) | 3V3 | ENET1\_RGMII\_RXC (SJA1110AEL) | 3V3 |
| 60  | ENET1\_RGMII\_RX\_CTL (GPIO0\_IO11, GPIO06\_IO05) | 3V3 | ENET1\_RGMII\_RX\_CTL (SJA1110AEL) | 3V3 |
| 62  | ENET1\_RGMII\_RXD0 (GPIO0\_IO10, GPIO06\_IO04) | 3V3 | ENET1\_RGMII\_RXD0 (SJA1110AEL) | 3V3 |
| 64  | ENET1\_RGMII\_RXD1 (GPIO0\_IO07, GPIO06\_IO01) | 3V3 | ENET1\_RGMII\_RXD1 (SJA1110AEL) | 3V3 |
| 66  | ENET1\_RGMII\_RXD2 (GPIO0\_IO06, GPIO06\_IO00) | 3V3 | ENET1\_RGMII\_RXD2 (SJA1110AEL) | 3V3 |
| 68  | ENET1\_RGMII\_RXD3 (GPIO0\_IO05) | 3V3 | ENET1\_RGMII\_RXD3 (SJA1110AEL) | 3V3 |
| 70  | GND |     | GND |     |
| 72  | GND |     | GND |     |
| 74  | GND |     | GND |     |
| 76  | GND |     | GND |     |
| 78  | GND |     | GND |     |
| 80  | GND |     | GND |     |

<a id="power-and-reset"></a>

## Power and Reset

<a id="power-architecture"></a>

### Power Architecture

The IMX8-XLite power is a single 5V source. It uses NXP’s PMIC to source all the SOM's power rails and a 3.3V Buck to generate the 3.3V. The following figure describes the power architecture.

![image-20240214-111628.png](./attachments/image-20240214-111628.png)

The power architecture main features are:

- Single 5V power source.
- NXP’s PF7100.
- TI’s TPSM82822 generates the 3.3V/2A.
- 3.3V output up to 0.5A (Need to calculate system and SOM power).
- 1.8V output (Buck3) up to 1A (Need to calculate system and SOM power).
- Power up sequence is supported by the PMIC configuration.

<a id="reset"></a>

### Reset

The reset signal is generated by the PMIC after all power are “ON” and a manual reset button.

![image-20240214-111659.png](./attachments/image-20240214-111659.png)

<a id="imx8-xlite-integration-manual"></a>

## IMX8-XLite Integration Manual

<a id="booting-options"></a>

### Booting Options

The following table describes the booting options:

![image-20240214-111730.png](./attachments/image-20240214-111730.png)

The supported booting options are:

- Boot from eFuse “000”
- Boot from USB serial downloader “001”
- Boot from eMMC0 “010”

All boot signals are available on the Board-to-Board connectors.

<a id="i2c-interfaces"></a>

### I2C Interfaces

The IMX8-XLite SOM uses I2C2 and I2C3 interfaces for its internal configurations.

**I2C2**

- GPS Module (M1). Address 0x42 (7 bits).
- Board-to-Board connectors.

**I2C3**

- 3D accelerometer and 3D gyroscope. Address 0xD6.
- Barometer. Address 0xB8.
- Magnetometer. Address 0x3C.
- Board-to-Board connectors.

**PIMIC I2C**

The PMIC has a dedicated I2C interface

<a id="gpio-interfaces"></a>

### GPIO Interfaces

The IMX8-XLite uses some GPIO signals for its internal controls. The following table describes the GPIO allocation.

|     |     |     |     |
| --- | --- | --- | --- |
| **Signal** | **I/O** | **Description** | **Remarks** |
| SAF5400\_RST | [GPIO1.IO](http://GPIO1.IO)\[10\] | Reset the V2X modem | Active Low |
| SAF\_BOOT0 | [GPIO1.IO](http://GPIO1.IO)\[09\] | Set the V2X modem boot option | “0” QSPI<br><br>“1” SDIO |
| GPS\_RSTN | [GPIO2.IO](http://GPIO2.IO)\[08\] | Reset the GPS | Input |
| GPS\_INT | [GPIO2.IO](http://GPIO2.IO)\[09\] | GPS Interrupt | Active Low |
| 6AX\_INT | [GPIO2.IO](http://GPIO2.IO)\[11\] | 3D accelerometer and 3D gyroscope Interrupt | Active Low |
| MAG\_INT | [GPIO2.IO](http://GPIO2.IO)\[10\] | Enable the WLAN | Active High |

<a id="imx8-xlite-som-debugging-capability"></a>

### IMX8-XLite SOM Debugging Capability

The IMX8-XLite SOM supports two main debugging interfaces:

- UART interface
- JTAG interface

The UART interface is a null modem interface that is internally pulled up and supports using UART0 TX/RX signals.

UART2 signals are available:

- B-t-B connector for carrier support

The UART interface is optional to use and mentioned here since most of the software infrastructure used in HummingBoard uses those two signals for debugging.

JTAG interface is on the IMX8-XLite SOM and is exposed as test pins on print side. Following is a snapshot of the test points and its connectivity traces:

![image-20240214-111854.png](./attachments/image-20240214-111854.png)

<a id="mechanical-description"></a>

## Mechanical Description

Following is a diagram of the TOP VIEW of the IMX8-XLite SOM.

![image-20240214-111907.png](./attachments/image-20240214-111907.png)

For more information and carrier design instruction contact SolidRun Support.

<a id="ordering-information"></a>

## Ordering Information

Please refer to the SolidRun website for more information regarding part numbers and the procedure for placing an order. [www.solid-run.com](http://www.solid-run.com/)

<a id="documentation"></a>

## Documentation

     

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-80757c79-ef08-48ee-a14a-70b5b671663a)<br><br>[Preview] [View](/wiki/download/attachments/613416973/IMX8XL+SOM-v2_BoardAndModels.step?version=1) [Properties](/wiki/pages/editattachment.action?pageId=613416973&fileName=IMX8XL+SOM-v2_BoardAndModels.step&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=613416973&fileName=IMX8XL+SOM-v2_BoardAndModels.step) | File [IMX8XL SOM-v2\_BoardAndModels.step](/wiki/download/attachments/613416973/IMX8XL%20SOM-v2_BoardAndModels.step?api=v2) | Mar 11, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-1b945e56-c8cf-413b-81a2-b474d05a49de)<br><br>[Preview] [View](/wiki/download/attachments/613416973/IMX8DXL_SOM_V2X_3D_model.rar?version=3) [Properties](/wiki/pages/editattachment.action?pageId=613416973&fileName=IMX8DXL_SOM_V2X_3D_model.rar&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=613416973&fileName=IMX8DXL_SOM_V2X_3D_model.rar) | File [IMX8DXL\_SOM\_V2X\_3D\_model.rar](/wiki/download/attachments/613416973/IMX8DXL_SOM_V2X_3D_model.rar?api=v2) | Mar 11, 2024 by [Yazan Shhady](/wiki/people/5f67bce9ed55c7006abc6319) |

- Drag and drop to upload or [browse for files] ![](/wiki/images/icons/wait.gif)

Upload file 

File description  

</form> </div> </div> <div> <a class="download-all-link" href="/wiki/download/all\_attachments?pageId=613416973" title="Download all the latest versions of attachments on this content as single zip file.">Download All</a> </div> </div> <h2 id="i.MX8DXLSOMHardwareUserManual-RelatedArticles">Related Articles</h2><div class="error">Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden</div></x-turndown>