# LX2162A SOM Hardware User Manual

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 27 Mar 2022 | Rabeeh Khoury | 1.0 |     |
| May 15, 2023 | Rabeeh Khoury | 1.1 | - Limited DDR4 configuration to 8 and 16GByte only (removed 32GByte support).<br>- Added notes withregards max power consumption |
| Table of Contents | - [Revisions and Notes](#revisions-and-notes)<br>- [Introduction](#introduction)<br>- [Specifications](#specifications)<br>- [Overview](#overview)<br>- [Description](#description)<br>  - [Block Diagram](#block-diagram)<br>- [Simplified Schematics](#simplified-schematics)<br>- [Module dimensions and board to board header orientation](#module-dimensions-and-board-to-board-header-orientation)<br>- [Module Max Power Consumption Measurements](#module-max-power-consumption-measurements)<br>- [SERDES configuration](#serdes-configuration)<br>  - [SERDES block #1 (SD1)](#serdes-block-1-sd1)<br>  - [SERDES block #2 (SD2)](#serdes-block-2-sd2)<br>- [Pinout](#pinout)<br>  - [J3 Header](#j3-header)<br>  - [J2 Header](#j2-header)<br>  - [J1 Header\*](#j1-header)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

> [!INFO]
> No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.

<a id="introduction"></a>

## Introduction

This document is intended for hardware engineers that are willing to integrate

[LX2162A SOM](https://www.solid-run.com/embedded-networking/nxp-lx2160a-family/lx2162a-som/) module from SolidRun ltd.

The document provides details with regards LX2162A module rev 1.0.

Below are two pictures of the SOM; the first is the top side where most of the heat is generated; and the second is from the bottom side where it connects to a carrier board -

![LX2162A SOM Top](./attachments/LX2162%20som%20top.png)

![LX2162A SOM Bottom](./attachments/LX2162%20som%20bottom.png)

<a id="specifications"></a>

## Specifications

|     |     |     |     |
| --- | --- | --- | --- |
|     | **LX2082A** | **LX2122A** | **LX2162A** |
| **CPU Details** | NXP Layerscape LX2082A  <br>8 x Cortex A72 | NXP Layerscape LX2122A  <br>12 x Cortex A72 | NXP Layerscape LX2162A  <br>16 x Cortex A72 |
| **CPU Speed** | 2.0GHz Commercial | 2.0GHz Commercial | 2.0GHz Commercial |
| **RAM** | Single channel  <br>with 8GB or 16GB DDR4 | Single channel  <br>with 8GB or 16GB DDR4 | Single channel  <br>with 8GB or 16GB DDR4 |
| **Internal Storage** | 8GB eMMC  <br>64MB SPI<br><br>(other ordering options available) | 8GB eMMC  <br>64MB SPI<br><br>(other ordering options available) | 8GB eMMC  <br>64MB SPI<br><br>(other ordering options available) |
| **External Storage Support** | SD  <br>PCIe-SSD | SD  <br>PCIe-SSD | SD  <br>PCIe-SSD |
| **Ethernet** | Serdes block 1 (4x25 GbE / 1x100 GbE / 4x10GbE)  <br>Serdes block 2 (8x1GbE)(\*)  <br>Sync-E, 1588-V2<br><br>1GbE with PHY | Serdes block 1 (4x25 GbE / 1x100 GbE / 4x10GbE)  <br>Serdes block 2 (8x1GbE)(\*)  <br>Sync-E, 1588-V2<br><br>1GbE with PHY | Serdes block 1 (4x25 GbE / 1x100 GbE / 4x10GbE)  <br>Serdes block 2 (8x1GbE)(\*)  <br>Sync-E, 1588-V2<br><br>1GbE with PHY |
| **USB 3.0** | 1   | 1   | 1   |
| **PCIe** | 8 (Gen 3 – 2 controllers)\* | 8 (Gen 3 – 2 controllers)\* | 8 (Gen 3 – 2 controllers)\* |
| **I2C** | 4   | 4   | 4   |
| **UART** | 2   | 2   | 2   |
| **GPIO** | ✔   | ✔   | ✔   |
| **SATA** | 4xGen 3(\*) | 4xGen 3(\*) | 4xGen 3(\*) |
| **Security** | NXP Layerscape Secure Boot | NXP Layerscape Secure Boot | NXP Layerscape Secure Boot |
| **SD** | 1   | 1   | 1   |
| **JTAG** | ✔   | ✔   | ✔   |
| **OS Support** | Linux  <br>DPDK  <br>UEFI | Linux  <br>DPDK  <br>UEFI | Linux  <br>DPDK  <br>UEFI |
| **Size** | 55 x 48 mm | 55 x 48 mm | 55 x 48 mm |
| **Interface** | 3 x Hirose DF40 connectors | 3 x Hirose DF40 connectors | 3 x Hirose DF40 connectors |
| **Main Voltage** | 12V | 12V | 12V |
| **I/O Voltage** | 3.3V/1.8V | 3.3V/1.8V | 3.3V/1.8V |
| **Temperature** | Commercial: 0°C to 70°C | Commercial: 0°C to 70°C | Commercial: 0°C to 70°C |
| **Humidity** | Humidity (non-condensing): 10% – 90% | Humidity (non-condensing): 10% – 90% | Humidity (non-condensing): 10% – 90% |
|     | [Contact Us](https://www.solid-run.com/contact-us/) | [Contact Us](https://www.solid-run.com/contact-us/) | [Contact Us](https://www.solid-run.com/contact-us/) |

(\*) Configurable SD2 SERDESs based on NXP LX2162A processor specifications.

<a id="overview"></a>

## Overview

LX2162A SOM is a highly integrated SOM module based on NXP’s [LX2162A](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/layerscape-processors/layerscape-lx2162a-lx2122a-lx2082a-processors:LX2162A) SoC.

The SoC highlights are up to 2.0GHz 16 x Cortex A72 Arm cores, DDR4 2900 MT/s up to 16 GB capacity with ECC and 12 high speed SERDESes.

The module integrates the following features –

1. LX2162A SoC (up to 2.0GHz).
2. On-board single controller supports up to 16GByte DDR4 2900Mtps memory with and without ECC.
3. Single 12V DC-input is required.

<a id="description"></a>

## Description

<a id="block-diagram"></a>

#### Block Diagram

The following figure describes the LX2162A SOM Blocks Diagram.

![](./attachments/LX2162A%20SOM%20block%20diagram.jpg)

<a id="simplified-schematics"></a>

## Simplified Schematics

Following is a link to that simplified schematics of the board : [LX2162A COM Simplified Schematics](https://solidrun.atlassian.net/wiki/download/attachments/197494140/LX2162A%20SOM%20Simplified%20Schematics%20Rev1.0.pdf?api=v2)

LX2162A SOM simplified schematics is intended for the following audience –

1. Software and firmware engineers that enables them to understand the IO and signal connectivity of the SOM design.
2. Hardware engineers that are willing to use the SOM and build their own development board.

<a id="module-dimensions-and-board-to-board-header-orientation"></a>

## Module dimensions and board to board header orientation

[SOM bottom side DXF file](https://solidrun.atlassian.net/wiki/download/attachments/197494140/LX2162A-SOM-bottom-dxf.dxf?api=v2) - use attached dxf file for board dimensions, mounting holes and board to board connectors location

\*note the board to board pin numbers and keep in mind this is bottom view

![](./attachments/LX2162A-SOM-bottom-dxf.jpg)

<a id="module-max-power-consumption-measurements"></a>

## Module Max Power Consumption Measurements

Worst case scenario measured, power consumption wise was ~35W on the following scenario -

1. SOM attached to a simple carrier baseboard
2. Measured the 12v power rail coming to the whole system
3. Running 16 threads cpuburn application or memtester application on all cores
4. CPU junction temperature set to max at 105c
5. Test excludes SERDES connection, so additional 2-3W for SERDES connections must be taken into account.

<a id="serdes-configuration"></a>

## SERDES configuration

LX2162A has 2 configurable SERDES blocks named SD1, and SD2.

SERDES 1 block has 4 SERDESes, and SERDES 2 block has 8 SERDESes that can be configured by protocol number. The protocol numbers are limited and can be selected from the following configurations –

<a id="serdes-block-1-sd1"></a>

#### SERDES block #1 (SD1)

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Protocol** | **Lane 0 10G-KR0** | **Lane 1 10G- KR1** | **Lane 2 10G-KR2** | **Lane 3 10G-KR3** |
| 0   | off | off | off | off |
| 1 (\*) | PCIe.1 x4 |     |     |     |
| 2 (\*) | SGMII.3 | SGMII.4 | SGMII.5 | SGMII.6 |
| 3   | USXGMII / XFI.3 | USXGMII / XFI.4 | USXGMII / XFI.5 | USXGMII / XFI.6 |
| 9 (\*) | PCIe.1 x1 | SGMII.4 | SGMII.5 | SGMII.6 |
| 11 (\*) | PCIe.1 x2 |     | SGMII.5 | SGMII.6 |
| 15  | 50GE.1 |     | 50GE.2 |     |
| 16  | 50GE.1 |     | 25GE.5 | 25GE.6 |
| 17  | 25GE.3 | 25GE.4 | 25GE.5 | 25GE.6 |
| 18  | USXGMII / XFI.3 | USXGMII / XFI.4 | 25GE.5 | 25GE.6 |
| 20  | 40GE.1 |     |     |     |

(\*) Contact SolidRun for this option - requires assembling 100MHz reference clock for SD1 PLLF instead of default 161.13285MHz reference clock

(\*) As a self-service the customer can modify the default REFDES U10 that is 161.13285MHz differential clock which is Epson PN X1G004251012100 to Epson PN SG3225EAN 100.000000M-KEGA3. The placement of U10 is as below - (pin 1 marked in red dot) -

![image-20241212-144549.png](./attachments/image-20241212-144549.png)

<a id="serdes-block-2-sd2"></a>

#### SERDES block #2 (SD2)

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Protocol** | **Lane 0 10G-KR0** | **Lane 1 10G- KR1** | **Lane 2 10G-KR2** | **Lane 3 10G-KR3** | **Lane 4 PCIe16** | **Lane 5 PCIe17** | **Lane 6 PCIe18** | **Lane 7 PCIe19** |
| 0   | off | off | off | off | off | off | off | off |
| 1   | PCIe.3 x 2 (gen 1,2) |     | SATA.1 | SATA.2 | PCIe.4 x4 (gen 1,2) |     |     |     |
| 2   | PCIe.3 x8 |     |     |     |     |     |     |     |
| 3   | PCIe.3 x4 |     |     |     | PCIe.4 x4 |     |     |     |
| 4   | PCIe.3 x4 (gen 1,2) |     |     |     | PCIe.4 x2 (gen 1,2) |     | SATA.1 | SATA.2 |
| 5   | PCIe.3 x4 |     |     |     | SATA.3 | SATA.4 | SATA.1 | SATA.2 |
| 6   | PCIe.3 x4 (gen 1,2) |     |     |     | SGMII.15 | SGMII.16 | USXGMII / XFI.13 | USXGMII / XFI.14 |
| 7   | PCIe.3 x1 (gen 1,2) | SGMII.12 | SGMII.17 | SGMII.18 | PCIe.4 x1 (gen 1,2) | SGMII.16 | USXGMII / XFI.13 | USXGMII / XFI.14 |
| 8   | X   | X   | SATA.1 | SATA.2 | SATA.3 | SATA.4 | USXGMII / XFI.13 | USXGMII / XFI.14 |
| 9   | SGMII.11 | SGMII.12 | SGMII.17 | SGMII.18 | SGMII.15 | SGMII.16 | SGMII.13 | SGMII.14 |
| 10  | SGMII.11 | SGMII.12 | SGMII.17 | SGMII.18 | PCIe.4 x4 |     |     |     |
| 11  | PCIe.3 x1 | SGMII.12 | SGMII.17 | SGMII.18 | PCIe.4 x1 | SGMII.16 | SGMII.13 | SGMII.14 |
| 12  | SGMII.11 | SGMII.12 | SGMII.17 | SGMII.18 | PCIe.4 x2 (gen 1,2) |     | SATA.1 | SATA.2 |
| 13  | PCIe.3 x4 |     |     |     | PCIe.2 x2 |     | SGMII.13 | SGMII.14 |
| 14  | PCIe.3 x2 |     | SGMII.17 | SGMII.18 | PCIe.2 x2 |     | SGMII.13 | SGMII.14 |

**Notice:** By default SD2 PLLS is assembled as onboard 156.25MHz and an external 100MHz reference clock (HCSL) is required to be supplied by the carrier board. There is an option to order with an integrated 100MHz reference clock but will require special order from SolidRun.

<a id="pinout"></a>

## Pinout

<a id="j3-header"></a>

#### J3 Header

| **Notes** | **Driving IC** | **IC ball number** | **Schematics Pin Name** | **Pin Number** | **Pin Number** | **Schematics Pin Name** | **IC ball number** | **Driving IC** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Can be floated, or pulled to GND until carrier board powers are valid |     |     | PWR\_OK | 2   | 1   | EVT0\_B | T4  | 1.8V, GPIO\_3\[12\], 4.7K Pull-up | SMB\_ALERT# |
| Connect to RTC battery source |     |     | VBAT | 4   | 3   | EVT1\_B | T6  | 1.8V, GPIO\_3\[13\], 4.7K Pull-up | THRM# |
| Output from SOM. Can be used by carrier board up to 600mA |     |     | 5V  | 6   | 5   | EVT2\_B | U5  | 1.8V, GPIO\_3\[14\], 4.7K Pull-up |     |
| Output from SOM. Can be used by carrier board up to 600mA |     |     | 5V  | 8   | 7   | EVT4\_B | AA3 | 1.8V, GPIO\_3\[16\], 4.7K Pull-up |     |
| PROC\_TMS | LX2162A | E21 | DUT\_TMS | 10  | 9   | EVT3\_B | Y4  | 1.8V, GPIO\_3\[15\], 4.7K Pull-up |     |
| PROC\_TCK | LX2162A | E23 | DUT\_TCK | 12  | 11  | TA\_BB\_VDD |     |     |     |
| Output from SOM. Can be used by carrier board up to 300mA |     |     | 3.3V | 14  | 13  | TMP\_DETECT\_B | Y6  | 1.8V, 4.7K Pull-up |     |
| PROC\_TDI | LX2162A | F20 | DUT\_TDI | 16  | 15  | OVDD |     |     | 1.8v Output from SOM. Can be used by carrier board up to 300mA |
| Control the main DC-DC controller |     |     | I2C\_MASTER\_SCL | 18  | 17  | V\_2.5 |     |     | Output from SOM. Can be used by carrier board up to 600mA |
| Control the main DC-DC controller |     |     | I2C\_MASTER\_SDA | 20  | 19  | V\_2.5 |     |
| PROC\_TDO | LX2162A | E19 | DUT\_TDO | 22  | 21  | I2C1\_SCL\_3p3 |     | NTSX2102GD, 2.2K Pull-up |     |
| Can be used to program the internal efuses |     |     | TA\_PROG\_SFP | 24  | 23  | I2C1\_SDA\_3p3 |     | NTSX2102GD, 2.2K Pull-up |     |
| FTM1\_CH4 / GPIO\_3\[0\] | 1.8V,  4.7K Pull-up | R5  | PROC\_IRQ0 | 26  | 25  | SPI\_D0\_1v8 |     |     |     |
|     |     |     | SPI\_MUX\_1v8\_3v3 | 28  | 27  | SPI\_D1\_1v8 |     |     |     |
|     |     |     | SPI\_CS\_B\_1v8 | 30  | 29  | SPI\_SCK\_1v8 |     |     |     |

<a id="j2-header"></a>

#### J2 Header

| **Notes** | **Driving IC** | **IC ball number** | **Schematics Pin Name** | **Pin Number** | **Pin Number** | **Schematics Pin Name** | **IC ball number** | **Driving IC** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Diff 100 Ohm | AR8035 |     | MDI\_P0 | 2   | 1   | 12V |     |     | Single 12v input to SOM . Can be up to 15V |
| Diff 100 Ohm | AR8035 |     | MDI\_N0 | 4   | 3   | 12V |     |     |
|     |     |     | GND | 6   | 5   | 12V |     |     |
| Diff 100 Ohm | AR8035 |     | MDI\_P1 | 8   | 7   | 12V |     |     |
| Diff 100 Ohm | AR8035 |     | MDI\_N1 | 10  | 9   | 12V |     |     |
|     |     |     | GND | 12  | 11  | 12V |     |     |
| Diff 100 Ohm | AR8035 |     | MDI\_P2 | 14  | 13  | 12V |     |     |
| Diff 100 Ohm | AR8035 |     | MDI\_N2 | 16  | 15  | 12V |     |     |
|     |     |     | GND | 18  | 17  | GND |     |     |     |
| Diff 100 Ohm | AR8035 |     | MDI\_P3 | 20  | 19  | SYS\_RESET\_IN\_1v8# |     | PT7M3808G01 | 1.8v system reset input |
| Diff 100 Ohm | AR8035 |     | MDI\_N3 | 22  | 21  | SYSRST\_OUT\_3v3# |     | MC74VHC1GT08 | 3.3v system reset out |
|     |     |     | GND | 24  | 23  | PROC\_EC2\_RXD0 | AW3 | LX2162A | TSEC\_1588\_TRIG\_IN2 / GPIO\_4\[21\] |
|     | AR8035 |     | GBE0\_LINK1000# | 26  | 25  | PROC\_EC2\_RXD1 | AV2 | LX2162A | TSEC\_1588\_PULSE\_OUT1 / GPIO\_4\[20\] |
|     | AR8035 |     | GBE0\_ACT# | 28  | 27  | PROC\_EC2\_RXD2 | AU1 | LX2162A | GPIO\_4\[19\] |
|     | AR8035 |     | GBE0\_LINK# | 30  | 29  | PROC\_EC2\_RXD3 | AR1 | LX2162A | GPIO\_4\[18\] |
| **Used for boot select** | 1.8V, CFG\_RCW\_SRC3, 10K Pull-up | AH6 | CFG\_RCW\_SRC3 | 32  | 31  | PROC\_EC2\_RX\_CLK | AR3 | LX2162A | TSEC\_1588\_CLK\_IN / GPIO\_4\[22\] |
| CFG\_RCW\_SRC0<br><br>**Used for boot select** | LX2162A | AH4 | UART2\_TXD\_1v8 | 34  | 33  | GND |     |     |     |
|     | LX2162A | AE3 | UART2\_RXD\_1v8 | 36  | 35  | I1588\_TRIG\_IN1 | AW1 | LX2162A | TSEC\_1588\_TRIG\_IN1 / GPIO\_4\[23\] |
| PWRBTN# | 1.8V, GPIO3\[6\],  <br>4.7K Pull-up |     | PROC\_IRQ6 | 38  | 37  | I1588\_ALARM\_OUT2 | AR5 | LX2162A | TSEC\_1588\_ALARM\_OUT2 / GPIO\_4\[12\] |
| ASLEEP / EVT9\_B / GPIO\_2\[6\]<br><br>**Used for boot select** | 1.8V,  10K Pull-up | AC1 | CFG\_RCW\_SRC2 | 40  | 39  | I1588\_CLK\_OUT | AU3 | LX2162A | TSEC\_1588\_CLK\_OUT / GPIO\_4\[14\] / EC2\_TXD1\_S |
| LX2162A\_RCLK0 |     | AV6 | IEEE\_RCLK0 | 42  | 41  | I1588\_PULSE\_OUT2 | AU5 | LX2162A | TSEC\_1588\_PULSE\_OUT2 / GPIO\_4\[15\] / EC2\_TXD0\_S |
| LX2162A\_RCLK1 |     | AT6 | IEEE\_RCLK1 | 44  | 43  | I1588\_ALARM\_OUT1 | AT4 | LX2162A | TSEC\_1588\_ALARM\_OUT1 / GPIO\_4\[13\] / EC2\_TXD2\_S |
| GPIO\_3\[10\] | 1.8V,  4.7K Pull-up | U3  | PROC\_IRQ10 | 46  | 45  | UART1\_TXD\_1v8 | AD4 | LX2162A | CFG\_RCW\_SRC1<br><br>**Used for boot select** |
| SUS\_S5# | 1.8V,  4.7K Pull-up | R1  | PROC\_IRQ7 | 48  | 47  | UART1\_RXD\_1v8 | AC3 | LX2162A |     |
|     | 1.8V,  2.2K Pull-up | AG1 | EMI2\_MDC | 50  | 49  | PROC\_IRQ11 | U1  | LX2162A |     |
|     | 1.8V,  2.2K Pull-up | AG3 | EMI2\_MDIO | 52  | 51  | EMI1\_3V3\_MDC |     | NTSX2102GD |     |
|     | LX2162A | W5  | TA\_BB\_TMP\_DETECT\_B | 54  | 53  | EMI1\_3V3\_MDIO |     | NTSX2102GD |     |
| GPIO\_4\[17\] / EC2\_GTX\_CLK\_S | LX2162A | AP6 | PROC\_EC2\_GTX\_CLK | 56  | 55  | FAN\_TACHIN |     |     |     |
|     |     |     | GND | 58  | 57  | PROC\_EC2\_TX\_EN | AV4 | LX2162A | GPIO\_4\[16\] / EC2\_TX\_CTL\_S |
|     | NVT4857UK |     | SD\_CMD | 60  | 59  | PROC\_IRQ9 | AA1 | 1.8V,  4.7K Pull-up |     |
|     | NVT4857UK |     | SD\_D0 | 62  | 61  | PROC\_IRQ5 | W1  | 1.8V,  4.7K Pull-up |     |
|     | NVT4857UK |     | SD\_D1 | 64  | 63  | PROC\_IRQ1 | P2  | 1.8V,  4.7K Pull-up |     |
|     | NVT4857UK |     | SD\_D2 | 66  | 65  | I2C3\_SCL | P6  | LX2162A |     |
|     | NVT4857UK |     | SD\_D3 | 68  | 67  | I2C3\_SDA | N6  | LX2162A |     |
|     | NVT4857UK |     | SD\_CD | 70  | 69  | I2C5\_SDA | K2  | LX2162A |     |
|     | NVT4857UK |     | SD\_CLK | 72  | 71  | I2C5\_SCL | J1  | LX2162A |     |
| Diff 90 Ohm | LX2162A | A5  | USB\_SSRX0+ | 74  | 73  | USB0+ | A9  | LX2162A | Diff 90 Ohm |
| Diff 90 Ohm | LX2162A | B6  | USB\_SSRX0- | 76  | 75  | USB0- | B10 | LX2162A | Diff 90 Ohm |
| Diff 90 Ohm | LX2162A | A7  | USB\_SSTX0+ | 78  | 77  | GND |     |     |     |
| Diff 90 Ohm | LX2162A | B8  | USB\_SSTX0- | 80  | 79  | FAN\_PWM |     |     |     |

<a id="j1-header"></a>

#### J1 Header\*

| **Notes** | **Driving IC** | **IC ball number** | **Schematics Pin Name** | **Pin Number** | **Pin Number** | **Schematics Pin Name** | **IC ball number** | **Driving IC** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | GND | 2   | 1   | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG7 | SD1\_RX3\_P | 4   | 3   | SD1\_TX3\_P | BE9 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH8 | SD1\_RX3\_N | 6   | 5   | SD1\_TX3\_N | BD10 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 8   | 7   | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG5 | SD1\_RX2\_P | 10  | 9   | SD1\_TX2\_P | BE7 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH6 | SD1\_RX2\_N | 12  | 11  | SD1\_TX2\_N | BD8 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 14  | 13  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BC1 | SD1\_RX1\_P | 16  | 15  | SD1\_TX1\_P | BC5 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BD2 | SD1\_RX1\_N | 18  | 17  | SD1\_TX1\_N | BD4 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 20  | 19  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BA1 | SD1\_RX0\_P | 22  | 21  | SD1\_TX0\_P | BA5 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BB2 | SD1\_RX0\_N | 24  | 23  | SD1\_TX0\_N | BB4 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 26  | 25  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG9 | SD2\_RX0\_P | 28  | 27  | SD2\_TX0\_P | BE11 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH10 | SD2\_RX0\_N | 30  | 29  | SD2\_TX0\_N | BD12 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 32  | 31  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG11 | SD2\_RX1\_P | 34  | 33  | SD2\_TX1\_P | BE13 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH12 | SD2\_RX1\_N | 36  | 35  | SD2\_TX1\_N | BD14 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 38  | 37  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG13 | SD2\_RX2\_P | 40  | 39  | SD2\_TX2\_P | BE15 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH14 | SD2\_RX2\_N | 42  | 41  | SD2\_TX2\_N | BD16 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 44  | 43  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG15 | SD2\_RX3\_P | 46  | 45  | SD2\_TX3\_P | BE17 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH16 | SD2\_RX3\_N | 48  | 47  | SD2\_TX3\_N | BD18 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 50  | 49  | GND |     |     |     |
| Diff 100 Ohm / SD2\_PLLF\_REF\_CLK\_P | \*100M HCSL required | BG19 | CLK\_SLOT1\_P | 52  | 51  | CLK\_161\_BYP\_P |     |     | Not Connected |
| Diff 100 Ohm/ SD2\_PLLF\_REF\_CLK\_N | \*100M HCSL required | BH20 | CLK\_SLOT1\_N | 54  | 53  | CLK\_161\_BYP\_N |     |     | Not Connected |
|     |     |     | GND | 56  | 55  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG23 | SD2\_RX4\_P | 58  | 57  | SD2\_TX4\_P | BE23 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH24 | SD2\_RX4\_N | 60  | 59  | SD2\_TX4\_N | BD24 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 62  | 61  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG25 | SD2\_RX5\_P | 64  | 63  | SD2\_TX5\_P | BE25 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH26 | SD2\_RX5\_N | 66  | 65  | SD2\_TX5\_N | BD26 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 68  | 67  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG27 | SD2\_RX6\_P | 70  | 69  | SD2\_TX6\_P | BE27 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH28 | SD2\_RX6\_N | 72  | 71  | SD2\_TX6\_N | BD28 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 74  | 73  | GND |     |     |     |
| Diff 100 Ohm | LX2162A | BG29 | SD2\_RX7\_P | 76  | 75  | SD2\_TX7\_P | BE29 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
| Diff 100 Ohm | LX2162A | BH30 | SD2\_RX7\_N | 78  | 77  | SD2\_TX7\_N | BD30 | LX2162A | Diff 100 Ohm (\*)DC block capacitor required |
|     |     |     | GND | 80  | 79  | GND |     |     |     |

> [!INFO]
> \*No DC blocking capacitor on any of the SerDes lanes on the SOM.

<a id="documentation"></a>

## Documentation

       

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-d944186c-4d80-49a2-b83e-9c61aedd6bae)<br><br>[Preview] [View](/wiki/download/attachments/197494140/LX2162A+SOM+pinout.xlsx?version=1) | Microsoft Excel Spreadsheet [LX2162A SOM pinout.xlsx](/wiki/download/attachments/197494140/LX2162A%20SOM%20pinout.xlsx?api=v2) | Mar 27, 2022 by [Ilan Braun](/wiki/people/6231e3991f014e0069cd4610) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-3204dd6f-09e0-4ef6-9a40-d9f83807792f)<br><br>[Preview] [View](/wiki/download/attachments/197494140/LX2162A+SOM+Simplified+Schematics+Rev1.0.pdf?version=1) | PDF File [LX2162A SOM Simplified Schematics Rev1.0.pdf](/wiki/download/attachments/197494140/LX2162A%20SOM%20Simplified%20Schematics%20Rev1.0.pdf?api=v2) | Apr 03, 2022 by [Ilan Braun](/wiki/people/6231e3991f014e0069cd4610) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-8e99736e-ef89-4872-b6ef-537e3b587f0b)<br><br>[Preview] [View](/wiki/download/attachments/197494140/LX2162A-SOM-bottom-dxf.dxf?version=1) | File [LX2162A-SOM-bottom-dxf.dxf](/wiki/download/attachments/197494140/LX2162A-SOM-bottom-dxf.dxf?api=v2) | Apr 13, 2022 by [Ilan Braun](/wiki/people/6231e3991f014e0069cd4610) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-6b87a1d0-1399-4aa2-ae37-8489b9dd86b3)<br><br>[Preview] [View](/wiki/download/attachments/197494140/LX2162-SOM-v+1_0--3D.zip?version=5) | ZIP Archive [LX2162-SOM-v 1\_0--3D.zip](/wiki/download/attachments/197494140/LX2162-SOM-v%201_0--3D.zip?api=v2) | Oct 18, 2023 by [Rabeeh Khoury](/wiki/people/557058:99a92153-3f5e-430e-b8cf-907fde28b14e) |

[Download All](/wiki/download/all_attachments?pageId=197494140)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden