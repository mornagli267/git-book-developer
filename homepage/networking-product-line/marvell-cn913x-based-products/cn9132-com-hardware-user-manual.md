# CN9132 COM Hardware User Manual

<a id="dual-revision-and-notes"></a>

## Dual Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 26 Apr 2020 | Alon Rotman | 1.0 | 1. Initial release information<br>2. Relevant for PCB revision 1.0 |
| 10 Oct 2020 | Alon Rotman | 1.1 | 1. Update CN913x configurations<br>2. Update Connector A/B C/D pinout<br>3. Relevant for PCB rev1.1 |
| 29 Oct 2020 | Alon Rotman | 1.2 | Updated CP\[2:0\] MPPs tables according to PCB rev1.1 |
| Dec 01, 2024 | Josua Mayer | 1.3 | Cosmetic updates and minor corrections to MPP and connector tables according to PCB rev1.3 |
| Dec 30, 2024 | Josua Mayer | 1.3.1 | Marked PTP feature as Untested. |
| Table of Contents | - [Dual Revision and Notes](#dual-revision-and-notes)<br>- [Introduction](#introduction)<br>  - [Overview](#overview)<br>  - [Specifications](#specifications)<br>- [Simplified Schematics](#simplified-schematics)<br>- [Power Consumption](#power-consumption)<br>- [High Speed port configuration](#high-speed-port-configuration)<br>  - [Maximum Port combination:](#maximum-port-combination)<br>- [SERDES MUXing](#serdes-muxing)<br>  - [Each CP (CP0, CP1 and CP2) support the same mux options individually:](#each-cp-cp0-cp1-and-cp2-support-the-same-mux-options-individually)<br>- [AP/CP\[0:2\] Multi Purpose Pins](#ap-cp02-multi-purpose-pins)<br>  - [AP MPP\[0:19\]](#ap-mpp019)<br>  - [CP0 MPP\[0:62\]](#cp0-mpp062)<br>  - [CP1 MPP\[0:62\]](#cp1-mpp062)<br>  - [CP2 MPP\[0:62\]](#cp2-mpp062)<br>- [Assembly Options](#assembly-options)<br>  - [CP0 SDIO Interface Voltage Domain](#cp0-sdio-interface-voltage-domain)<br>  - [CP2 GE1 (RGMII) Interface Voltage Domain](#cp2-ge1-rgmii-interface-voltage-domain)<br>  - [Trusted Platform Module](#trusted-platform-module)<br>  - [SMB\_ALERT\_N](#smb_alert_n)<br>  - [BIOS\_DIS0# / BIOS\_DIS1#](#bios_dis0-bios_dis1)<br>- [COM Express Header Details](#com-express-header-details)<br>  - [AB Header](#ab-header)<br>  - [CD Header](#cd-header)<br>- [Common Questions and Answers](#common-questions-and-answers)<br>- [Documentation](#documentation)<br>- [Related Articles](#related-articles) |     |     |

> [!INFO]
> **Disclaimer**
> No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.

<a id="introduction"></a>

## Introduction

This document is intended for hardware engineers that are willing to integrate [CN913x COM express type 7](https://www.solid-run.com/embedded-networking/marvell-octeon-tx2-family/cex7-cn913x-com/) module from SolidRun ltd.

The document provides details with regards CN913x module rev 1.3.

<a id="overview"></a>

#### Overview

- CN9132 COM Express type 7 is a highly integrated COM modules based on Marvell’s CN913x SoC.
- The SoC highlights are up to 2.2GHz with 4 Cortex A72 Arm cores, DDR4 controller and 18 high speed SERDESs.

The module integrates the following features –

1. CN9130 SoC (up to 2.2GHz).
2. SO-DIMM DDR4 connected to the DDR controller. The SO-DIMM supports up to 16GByte SO-DIMM DDR4 2400Mtps memory with and without ECC, registered or non-registered.
3. Single 12V DC-input is required.

<a id="specifications"></a>

#### Specifications

| Features | CN9132 | CN9131 | CN9130 |
| --- | --- | --- | --- |
| Form Factor | COM Express type 7 | COM Express type 7 | COM Express type 7 |
| Processor Core | 4 cores Arm Cortex A72 | 4 cores Arm Cortex A72 | 4 cores Arm Cortex A72 |
| Processor speed | Up to 2.2GHz | Up to 2.2GHz | Up to 2.2GHz |
| Memory | Dual Channel SO-DIMM DDR4;<br><br>up to 32GB at 2400MT/s<br><br>(16GB for each channel) | Dual Channel SO-DIMM DDR4;<br><br>up to 32GB at 2400MT/s<br><br>(16GB for each channel) | Dual Channel SO-DIMM DDR4;<br><br>up to 32GB at 2400MT/s<br><br>(16GB for each channel) |
| ECC | Optional | Optional | Optional |
| eMMC | Up to 64GB (assembled 8GB) | Up to 64GB (assembled 8GB) | Up to 64GB (assembled 8GB) |
| Flash | 64Mbit SPI NOR flash | 64Mbit SPI NOR flash | 64Mbit SPI NOR flash |
| SATA 3.0 | 2   | 1   | 0   |
| Supported OS | Linux kernel 5.8x  <br>Yocto  <br>DPDK  <br>UEFI  <br>KVM/QEMU/Containers  <br>NFV  <br>Openstack compute node | Linux kernel 5.8x  <br>Yocto  <br>DPDK  <br>UEFI  <br>KVM/QEMU/Containers  <br>NFV  <br>Openstack compute node | Linux kernel 5.8x  <br>Yocto  <br>DPDK  <br>UEFI  <br>KVM/QEMU/Containers  <br>NFV  <br>Openstack compute node |
| XFI/RXAUI/SGMII | 3   | 2   | 1   |
| PCIe gen 3.0 | 1 x PCIe Gen 3.0 x4  <br>1 x PCIe Gen 3.0 x2  <br>6 x PCIe Gen 3.0 x1 | 1 x PCIe Gen 3.0 x4  <br>1 x PCIe Gen 3.0 x2  <br>3 x PCIe Gen 3.0 x1 | 1 x PCIe Gen 3.0 x4  <br>1 x PCIe Gen 3.0 x1 |
| USB 3.0 | 1   | 0   | 0   |
| I2C | 6   | 5   | 4   |
| SMI & XSMI | 3   | 2   | 1   |
| UART | 2   | 2   | 2   |
| PPS/PTP/Sync-E support | Untested, for authoritative information, consult Marvell documentation and Errata (available under NDA). | Untested, for authoritative information, consult Marvell documentation and Errata (available under NDA). | Untested, for authoritative information, consult Marvell documentation and Errata (available under NDA). |
| SPI bus | ✓   | ✓   | ✓   |
| RTC support | ✓   | ✓   | ✓   |
| Power | 12V (9V-15V)  <br>up to 15W full system | 12V (9V-15V)  <br>up to 13W full system | 12V (9V-15V)  <br>up to 11W full system |
| Environment | Commercial: 0°C to 70°C  <br>Industrial: -40°C to 85°C  <br>Humidity (non-condensing): 10% – 90% | Commercial: 0°C to 70°C  <br>Industrial: -40°C to 85°C  <br>Humidity (non-condensing): 10% – 90% | Commercial: 0°C to 70°C  <br>Industrial: -40°C to 85°C  <br>Humidity (non-condensing): 10% – 90% |
| Dimensions | 125mm X 95mm | 125mm X 95mm | 125mm X 95mm |

[Buy a Sample Now](https://shop.solid-run.com/?s=CEx7+CN9132&post_type=product)

<a id="simplified-schematics"></a>

## Simplified Schematics

CN9130 COM express type 7 simplified schematics is intended for the following audience –

1. Software and firmware engineers that enables them to understand the IO and signal connectivity of the COM express design.
2. Hardware engineers that are willing to use the COM express and build their own development board. This document completes the CEx7 CN9130 reference manual from description of signal and implementation wise.

<a id="power-consumption"></a>

## Power Consumption

TBD

<a id="high-speed-port-configuration"></a>

## High Speed port configuration

The CN9130 Com Express Type 7 family includes 3 variations:

1. CN9130 is comprised from a single CN9130.
2. CN9131 is comprised from a single CN9130 with **one** additional 88F8215. This includes a CP with 6 shared high speed SERDES interfaces, for a total of 12 lanes.
3. CN9132 is comprised from a single CN9130 with **two** additional 88F8215. Each one of them has a CP with 6 shared high speed SERDES interfaces, for a total of 18 lanes.

<a id="maximum-port-combination"></a>

#### Maximum Port combination:

| Feature | CN9132 | CN9131 | CN9130 |
| --- | --- | --- | --- |
| PCIe 3.0 | 1x Port X4 lanes  <br>+  <br>2x Ports X1  <br>Total of 3 controllers and up to 6 lanes | 1x Port X4 lanes  <br>+  <br>2x Ports X1  <br>Total of 3 controllers and up to 6 lanes | 1x Port X4 lanes  <br>+  <br>2x Ports X1  <br>Total of 3 controllers and up to 6 lanes |
| Ethernet | 3x 10/5 GbE port +  <br>6x 1/2.5 GbE Ports  <br>or  <br>6x 5 GbE Port +  <br>3x 1/2.5 GbE Port | 2x 10/5 GbE port +  <br>4x 1/2.5 GbE Ports  <br>or  <br>4x 5 GbE Port +  <br>2x 1/2.5 GbE Port | 1x 10/5 GbE port +  <br>2x 1/2.5 GbE Ports  <br>or  <br>2x 5 GbE Port +  <br>1x 1/2.5 GbE Port |
| USB 3.0 | 6 x USB 3.0  <br>(Host/Device) | 4 x USB 3.0  <br>(Host/Device) | 2 x USB 3.0  <br>(Host/Device) |
| SATA 3.0 | 6 x SATA 3.0 | 4 x SATA 3.0 | 2 x SATA 3.0 |
| SERDES LANES | 18 Lanes | 12 Lanes | 6 Lanes |
| 88F8215 | 2   | 1   | 0   |

<a id="serdes-muxing"></a>

## SERDES MUXing

<a id="each-cp-cp0-cp1-and-cp2-support-the-same-mux-options-individually"></a>

#### Each CP (CP0, CP1 and CP2) support the same mux options individually:

| **Interface** | **SERDES Lane0** | **SERDES Lane1** | **SERDES Lane**2 | **SERDES Lane**3 | **SERDES Lane**4 | **SERDES Lane**5 |
| --- | --- | --- | --- | --- | --- | --- |
| 10GBASE-R/XFI |     |     | Port 0 |     | Port 0 |     |
| 5GBASE-R |     |     | Port 0 |     | Port 0 or 1 |     |
| 10GBASE-X2 (RXAUI) |     |     | Port 0 Lane 0 | Port 0 Lane 1 | Port 0 Lane0 | Port 0 Lane 1 |
| 1000BASE-X (SGMII) / 2.5GBASE-X (HS-SGMII) | Port 1 | Port 2 | Port 0 | Port 1 | Port 0 or 1 | Port 2 |
| SATA 3.0 | Port 1 | Port 0 | Port 0 | Port 1 |     | Port 1 |
| USB 3.0 HOST |     | Port 0 | Port 0 | Port 1 | Port 1 |     |
| USB 3.0 Device |     | Port 0 |     |     | Port0 |     |
| PCIe  <br>RC/EP | PCIex4 Port0 LANE0 | PCIex4 Port0 LANE1 | PCIex4 Port0 LANE2 | PCIex4 Port0 LANE3 | PCIex1 Port1 | PCIex1 Port2 |
| **Evaluation Board Default Configuration of CP0** | **PCIex4 Port 0 Lane 0** | **PCIex4 Port 0 Lane 1** | **PCIex4 Port 0 Lane 2** | **PCIex4 Port 0 Lane 3** | **10GBASE-R/XFI Port 0** | **2.5GBASE-X/HS-SGMII Port 2** |
| **Evaluation Board Default Configuration of CP1** | **PCIex2 Port0 LANE0** | **PCIex2 Port0 LANE1** | **10GBASE-R/XFI Port 0** | **SATA 3.0 Port 1** | **PCIex1 Port 1** | **PCIex1 Port 2** |
| **Evaluation Board Default Configuration of CP2** | **PCIex1 Port 0** | **USB-3.0 Host Port 0** | **5GBASE-R/XFI Port 0** | **SATA 3.0 Port 1** | **PCIex1 Port 1** | **PCIex1 Port 2** |

The following port configurations can’t be used simultaneously:

- SGMII port 0 / HS SGMII port0, RXAUI and XFI/10GBASE
- SGMII port 1 and HS SGMII port 1
- SGMII port 2 and HS SGMII port 2

Note that all PCIe lanes specified in the CN9132 default configuration are connected to PCIe pins in the COM Express connector and are routed as 90 ohm differential pairs

<a id="ap-cp02-multi-purpose-pins"></a>

## AP/CP\[0:2\] Multi Purpose Pins

<a id="ap-mpp019"></a>

#### AP MPP\[0:19\]

| MPP # | Pin # | Pin Description | Notes |
| --- | --- | --- | --- |
| AP\_MPP\[0\] | AP10 | AP\_SD\_CLK | 1.8V, serial 22ohm resistor |
| AP\_MPP\[1\] | AT10 | AP\_SD\_CMD | 1.8V, 10K PU |
| AP\_MPP\[2\] | AP16 | AP\_SD\_D\[0\] | 1.8V, 10K PU |
| AP\_MPP\[3\] | AP18 | AP\_SD\_D\[1\] | 1.8V, 10K PU |
| AP\_MPP\[4\] | AT16 | AP\_SD\_D\[2\] | 1.8V, 10K PU |
| AP\_MPP\[5\] | AP14 | AP\_SD\_D\[3\] | 1.8V, 10K PU |
| AP\_MPP\[6\] | AP12 | AP\_SD\_DS | RCLK, 10K PD |
| AP\_MPP\[7\] | AT14 | AP\_SD\_D\[4\] | 1.8V, 10K PU |
| AP\_MPP\[8\] | AT12 | AP\_SD\_D\[5\] | 1.8V, 10K PU |
| AP\_MPP\[9\] | AT18 | AP\_SD\_D\[6\] | 1.8V, 10K PU |
| AP\_MPP\[10\] | AV18 | AP\_SD\_D\[7\] | 1.8V, 10K PU |
| AP\_MPP\[11\] | AY18 | AP\_UA0\_TXD | PD - Reset strap  <br>3.3V through FXL2TD245L10X level shifter |
| AP\_MPP\[12\] | BA17 | AP\_SD\_HW\_RST | 1.8V, 10K PD |
| AP\_MPP\[19\] | AW17 | AP\_UA0\_RXD | 3.3V through FXL2TD245L10X level shifter |

<a id="cp0-mpp062"></a>

#### CP0 MPP\[0:62\]

| MPP # | Pin # | Pin Description | Notes |
| --- | --- | --- | --- |
| MPP\[0\] | AY38 | CP\_GE1\_RXD\[3\] |     |
| MPP\[1\] | AV38 | CP\_GE1\_RXD\[2\] |     |
| MPP\[2\] | AW39 | CP\_GE1\_RXD\[1\] |     |
| MPP\[3\] | AY40 | CP\_GE1\_RXD\[0\] |     |
| MPP\[4\] | AW41 | CP\_GE1\_RXCTL |     |
| MPP\[5\] | BA39 | CP\_GE1\_RXCLK |     |
| MPP\[6\] | AW35 | CP\_GE1\_TXD\[3\] |     |
| MPP\[7\] | AY36 | CP\_GE1\_TXD\[2\] |     |
| MPP\[8\] | BA37 | CP\_GE1\_TXD\[1\] |     |
| MPP\[9\] | AW37 | CP\_GE1\_TXD\[0\] |     |
| MPP\[10\] | BA35 | CP\_GE1\_TXCTL |     |
| MPP\[11\] | AV36 | CP\_GE1\_TXCLKOUT |     |
| MPP\[12\] | AV32 | CP\_SPI1\_CSn\[1\] | 3.3V |
| MPP\[13\] | AY34 | CP\_SPI1\_MISO | 3.3V |
| MPP\[14\] | AT36 | CP\_SPI1\_CSn\[0\] | 3.3V, for on-SoM SPI Flash |
| MPP\[15\] | AT32 | CP\_SPI1\_MOSI | 3.3V, 10k PD, CPU Subsystem Clock  <br>CP0\_SYS\_PLL\_SEL0 |
| MPP\[16\] | AV34 | CP\_SPI1\_SCK | 3.3V, 10k PU, 1k PD via SW2-1, CPU Subsystem Clock  <br>CP0\_SYS\_PLL\_SEL1 |
| MPP\[17\] | BA29 | CP\_GPIO\[17\] | 3.3V, 10k PU, 1k PD via SW2-2, CPU Subsystem Clock  <br>CP0\_SYS\_PLL\_SEL2 |
| MPP\[18\] | AW29 | CP\_BOOT\_MODE\_SEL0 | 3.3V, 10k PU, 4.7k PD via SW1-5, Boot Mode\[0\] |
| MPP\[19\] | AV30 | CP\_BOOT\_MODE\_SEL1 | 3.3V, 10k PU, 4.7k PD via SW1-4, Boot Mode\[1\] |
| MPP\[20\] | BA31 | CP\_BOOT\_MODE\_SEL2 | 3.3V, 10k PU, 4.7k PD via SW1-3, Boot Mode\[2\] |
| MPP\[21\] | AT30 | CP\_BOOT\_MODE\_SEL3 | 3.3V, 10k PU, 1k PD via SW1-2, Boot Mode\[3\] |
| MPP\[22\] | AY30 | CP\_BOOT\_MODE\_SEL4 | 3.3V, 10k PU, 4.7k PD via SW1-1, Boot Mode\[4\] |
| MPP\[23\] | AP32 | CP\_BOOT\_MODE\_SEL5 | 3.3V, 10k PU, Boot Mode\[5\] |
| MPP\[24\] | AP34 | CP\_MPP\[24\] | 3.3V, 2.2K PU |
| MPP\[25\] | AT34 | CP\_MPP\[25\] | 3.3V, 2.2k PD, Reset strap |
| MPP\[26\] | AT38 | CP\_MPP\[26\] | 3.3V, 10k PU, Reset strap |
| MPP\[27\] | AW31 | CP\_MPP\[27\] | 3.3V, 10K PU, SODIMM EVENT\_N |
| MPP\[28\] | AY32 | CP\_PTP\_PULSE |     |
| MPP\[29\] | BA33 | CP\_PTP\_CLK |     |
| MPP\[30\] | AW33 | CP\_PTP\_PCLK\_OUT |     |
| MPP\[31\] | AP36 | CP\_MPP\[31\] | 3.3V, 2.2K PU, PWRBTN\_N |
| MPP\[32\] | H30 | CP\_MPP\[32\] | BIOS\_DIS status |
| MPP\[33\] | C39 | CP\_MPP\[33\] | BIOS\_DIS override BIOS\_DIS |
| MPP\[34\] | C41 | CP\_MPP\[34\] | 3.3V, 2.2K PU, SUS\_5\_N |
| MPP\[35\] | F32 | CP\_I2C1\_SDA | 3.3V, 2.2K PU, i2c mux,  <br>used addresses: 0x53, 0x2F, 0x6A, 0x51 |
| MPP\[36\] | H32 | CP\_I2C1\_SCK | 3.3V, 2.2K PU |
| MPP\[37\] | F34 | CP\_I2C0\_SCK | 3.3V, 2.2K PU  <br>EEPROM 0x50,  <br>SPD 0x53 |
| MPP\[38\] | H34 | CP\_I2C0\_SDA | 3.3V, 2.2K PU  <br>EEPROM 0x50,  <br>SPD 0x53 |
| MPP\[39\] | F30 | CP\_MPP\[39\] | FAN\_PWM\_R |
| MPP\[40\] | F36 | CP\_SMI\_MDIO | 3.3V, 2.2K PU |
| MPP\[41\] | H36 | CP\_SMI\_MDC | 3.3V, 2.2K PU |
| MPP\[42\] | E39 | CP\_XSMI\_MDC | 3.3V, 2.2K PU, can replace CP\_SMI\_MDC by assembly option |
| MPP\[43\] | D30 | CP\_XSMI\_MDIO | 3.3V, 2.2K PU, can replace CP\_SMI\_MDIO by assembly option |
| MPP\[44\] | D38 | CP\_MPP\[44\] | 3.3V, 10k PD, PCIe0 clock config |
| MPP\[45\] | A39 | CP\_MPP\[45\] | 3.3V, 10k PD, Reset strap |
| MPP\[46\] | C37 | CP\_MPP\[46\] | 3.3V, 10k PD, CPU Subsystem Clock  <br>CP0\_SYS\_PLL\_SEL3 |
| MPP\[47\] | A37 | CP\_MPP\[47\] | 3.3V, 2.2k PD, Reset strap |
| MPP\[48\] | B40 | CP\_MPP\[48\] | 3.3V, 10k PD, PCIe1 clock config |
| MPP\[49\] | B38 | CP\_MPP\[49\] | 3.3V, 1k PD, can enable 1.8V supply for CP0:CP\_VHV |
| MPP\[50\] | C35 | CP\_UA2\_TXD | 3.3V |
| MPP\[51\] | D34 | CP\_UA2\_RXD | 3.3V |
| MPP\[52\] | A35 | CP\_RCVR1\_CLK/CP\_RCVR2\_CLK | 3.3V, Recovered clock for SyncE |
| MPP\[53\] | B36 | AP\_VHV\_EN | 3.3V, 1k PD, can enable 1.8V supply for AP\_VHV |
| MPP\[54\] | D36 | CP\_MPP\[54\] | 3.3V, connected with ethernet phy clock output |
| MPP\[55\] | B34 | CP\_SD\_CRD\_DT | 3.3V, 2.2k PU |
| MPP\[56\] | D32 | CP\_SD\_CLK | 3.3V (1.8V assembly option) |
| MPP\[57\] | B32 | CP\_SD\_CMD | 3.3V (1.8V assembly option) |
| MPP\[58\] | A33 | CP\_SD\_D\[0\] | 3.3V (1.8V assembly option) |
| MPP\[59\] | C33 | CP\_SD\_D\[1\] | 3.3V (1.8V assembly option) |
| MPP\[60\] | A31 | CP\_SD\_D\[2\] | 3.3V (1.8V assembly option) |
| MPP\[61\] | C31 | CP\_SD\_D\[3\] | 3.3V (1.8V assembly option) |
| MPP\[62\] | B30 | NC  | 3.3V (1.8V assembly option) |

<a id="cp1-mpp062"></a>

#### CP1 MPP\[0:62\]

| MPP # | Pin # | Pin Description | Notes |
| --- | --- | --- | --- |
| MPP\[0\] | AB21 | NC  | 3.3V |
| MPP\[1\] | AC21 | NC  | 3.3V |
| MPP\[2\] | AA22 | NC  | 3.3V |
| MPP\[3\] | AA23 | NC  | 3.3V |
| MPP\[4\] | AA21 | NC  | 3.3V |
| MPP\[5\] | AB22 | NC  | 3.3V |
| MPP\[6\] | AC18 | NC  | 3.3V |
| MPP\[7\] | AB18 | NC  | 3.3V |
| MPP\[8\] | AA19 | NC  | 3.3V |
| MPP\[9\] | AA20 | NC  | 3.3V |
| MPP\[10\] | AA18 | NC  | 3.3V |
| MPP\[11\] | AB19 | CP\_MPP\[11\] | 3.3V, BATLOW\_N |
| MPP\[12\] | AA12 | CP\_MPP\[12\] | 3.3V, SPKR |
| MPP\[13\] | AB13 | CP\_SPI1\_MISO | 3.3V, 2.2k PU |
| MPP\[14\] | AA17 | CP\_SPI1\_CSn\[0\] | 3.3V, 2.2k PU, for on-SoM TPM (assembly option) |
| MPP\[15\] | AA14 | CP\_SPI1\_MOSI | 3.3V, 10k PD |
| MPP\[16\] | AA13 | CP\_SPI1\_SCK | 3.3V, 10k PU |
| MPP\[17\] | AA8 | CP\_MPP\[17\] | 3.3V, 2.2k PU, TPM PIRQ\_N |
| MPP\[18\] | AA9 | CP\_MPP\[18\] | 3.3V, Boot Mode\[0\] |
| MPP\[19\] | AB9 | CP\_MPP\[19\] | 3.3V, Boot Mode\[1\] |
| MPP\[20\] | AB10 | CP\_MPP\[20\] | 3.3V, Boot Mode\[2\] |
| MPP\[21\] | AA7 | CP\_MPP\[21\] | 3.3V, Boot Mode\[3\] |
| MPP\[22\] | AC9 | CP\_MPP\[22\] | 3.3V, Boot Mode\[4\] |
| MPP\[23\] | AB16 | CP\_MPP\[23\] | 3.3V, Boot Mode\[5\] |
| MPP\[24\] | AA16 | NC  | 3.3V |
| MPP\[25\] | AB15 | CP\_MPP\[25\] | 3.3V, 2.2k PD, Reset strap |
| MPP\[26\] | AC15 | CP\_MPP\[26\] | 3.3V, 2.2k PD, Reset strap |
| MPP\[27\] | AA10 | NC  | 3.3V |
| MPP\[28\] | AA11 | CP\_PTP\_PULSE | 3.3V |
| MPP\[29\] | AC12 | CP\_PTP\_CLK | 3.3V |
| MPP\[30\] | AB12 | CP\_PTP\_PCLK\_OUT | 3.3V |
| MPP\[31\] | AA15 | NC  | 3.3V |
| MPP\[32\] | A9  | NC  | 3.3V |
| MPP\[33\] | B5  | CP\_MPP\[33\] | 3.3V, THERMTRIP\_N |
| MPP\[34\] | B6  | CP\_MPP\[34\] | 3.3V, THRM\_N |
| MPP\[35\] | C11 | CP\_I2C1\_SDA | 3.3V, 2.2k PU |
| MPP\[36\] | C10 | CP\_I2C1\_SCK | 3.3V, 2.2k PU |
| MPP\[37\] | C9  | CP\_XSMI\_MDC | 3.3V, 2.2k PU |
| MPP\[38\] | B9  | CP\_XSMI\_MDIO | 3.3V, 2.2k PU |
| MPP\[39\] | C8  | CP\_SATA1\_PRESENT\_ACTIVEn | 3.3V |
| MPP\[40\] | C7  | CP\_MPP\[4\] | 3.3V, WAKE0 |
| MPP\[41\] | C8  | NC  | 3.3V |
| MPP\[42\] | A6  | CP\_MPP\[42\] | 3.3V, 2.2k PU, 10G\_PHY\_RST\_23 |
| MPP\[43\] | C6  | CP\_MPP\[43\] | 3.3V, 2.2k PU, 10G\_PHY\_RST\_01 |
| MPP\[44\] | B3  | CP\_MPP\[44\] | 3.3V, 10k PD, PCIe0 clock config |
| MPP\[45\] | C4  | NC  | 3.3V, 10k PD, Reset strap |
| MPP\[46\] | B2  | NC  | 3.3V |
| MPP\[47\] | C2  | NC  | 3.3V, 2.2k PD, Reset strap |
| MPP\[48\] | C5  | NC  | 3.3V, PCIe1 clock config |
| MPP\[49\] | A3  | NC  | 3.3V |
| MPP\[50\] | D3  | CP\_MPP\[50\] | 3.3V, 2.2K PU, CP1\_SFP\_INT1 |
| MPP\[51\] | E2  | CP\_MPP\[51\] | 3.3V, 2.2K PU, WAKE1 |
| MPP\[52\] | E3  | CP\_RCVR1\_CLK/CP\_RCVR2\_CLK | 3.3V, Recovered clock for SyncE |
| MPP\[53\] | C3  | NC  | 3.3V |
| MPP\[54\] | C1  | NC  | 3.3V |
| MPP\[55\] | F2  | NC  | 3.3V |
| MPP\[56\] | H3  | NC  | 3.3V |
| MPP\[57\] | H2  | NC  | 3.3V |
| MPP\[58\] | G3  | NC  | 3.3V |
| MPP\[59\] | F3  | NC  | 3.3V |
| MPP\[60\] | J1  | NC  | 3.3V |
| MPP\[61\] | J2  | NC  | 3.3V |
| MPP\[62\] | F1  | NC  | 3.3V |

<a id="cp2-mpp062"></a>

#### CP2 MPP\[0:62\]

| MPP # | Pin # | Pin Description | Notes |
| --- | --- | --- | --- |
| MPP\[0\] | AB21 | CP\_UA0\_RXD | 3.3V (1.8V assembly option), RSVD0 |
| MPP\[1\] | AC21 | CP\_UA0\_TXD | 3.3V (1.8V assembly option), RSVD1 |
| MPP\[2\] | AA22 | CP\_UA1\_RXD | 3.3V (1.8V assembly option), RSVD2 |
| MPP\[3\] | AA23 | CP\_UA1\_TXD | 3.3V (1.8V assembly option), RSVD3 |
| MPP\[4\] | AA21 | CP\_UA1\_CTS | 3.3V (1.8V assembly option), RSVD4 |
| MPP\[5\] | AB22 | CP\_UA1\_RTS | 3.3V (1.8V assembly option), RSVD5 |
| MPP\[6\] | AC18 | CP\_SATA1\_PRESENTn | 3.3V (1.8V assembly option), RSVD6 |
| MPP\[7\] | AB18 | CP\_SPI0\_CSn\[1\] | 3.3V (1.8V assembly option), RSVD7 |
| MPP\[8\] | AA19 | CP\_SPI0\_CSn\[0\] | 3.3V (1.8V assembly option), RSVD8 |
| MPP\[9\] | AA20 | CP\_SPI0\_MOSI | 3.3V (1.8V assembly option), RSVD9 |
| MPP\[10\] | AA18 | CP\_SPI0\_MISO | 3.3V (1.8V assembly option), RSVD10 |
| MPP\[11\] | AB19 | CP\_SPI0\_SCK | 3.3V (1.8V assembly option), RSVD11 |
| MPP\[12\] | AA12 | NC  | 3.3V |
| MPP\[13\] | AB13 | NC  | 3.3V |
| MPP\[14\] | AA17 | NC  | 3.3V |
| MPP\[15\] | AA14 | NC  | 3.3V |
| MPP\[16\] | AA13 | NC  | 3.3V |
| MPP\[17\] | AA8 | NC  | 3.3V |
| MPP\[18\] | AA9 | CP0\_BOOT\_MODE\_SEL0 | 3.3V |
| MPP\[19\] | AB9 | CP0\_BOOT\_MODE\_SEL1 | 3.3V |
| MPP\[20\] | AB10 | CP0\_BOOT\_MODE\_SEL2 | 3.3V |
| MPP\[21\] | AA7 | CP0\_BOOT\_MODE\_SEL3 | 3.3V |
| MPP\[22\] | AC9 | CP0\_BOOT\_MODE\_SEL4 | 3.3V |
| MPP\[23\] | AB16 | CP0\_BOOT\_MODE\_SEL5 | 3.3V |
| MPP\[24\] | AA16 | NC  | 3.3V |
| MPP\[25\] | AB15 | CP\_MPP\[25\] | 3.3V, 2.2k PD, Reset strap |
| MPP\[26\] | AC15 | CP\_MPP\[26\] | 3.3V, 2.2k PD, Reset strap |
| MPP\[27\] | AA10 | CP\_MPP\[27\] | 3.3V, RSVD27 |
| MPP\[28\] | AA11 | CP2\_PTP\_PULSE | 3.3V |
| MPP\[29\] | AC12 | CP2\_PTP\_CLK\_IN | 3.3V |
| MPP\[30\] | AB12 | CP2\_PTP\_PCLK\_OUT | 3.3V |
| MPP\[31\] | AA15 | CP\_MPP\[31\] | 3.3V, RSVD31 |
| MPP\[32\] | A9  | CP\_MPP\[32\] | 3.3V, RSVD32 |
| MPP\[33\] | B5  | NC  | 3.3V |
| MPP\[34\] | B6  | NC  | 3.3V |
| MPP\[35\] | C11 | CP\_I2C1\_SDA | 3.3V, 2.2k PU |
| MPP\[36\] | C10 | CP\_I2C1\_SCK | 3.3V, 2.2k PU |
| MPP\[37\] | C9  | CP\_SMI\_MDC/CP\_XSMI\_MDC | 3.3V, 2.2K PU |
| MPP\[38\] | B9  | CP\_SMI\_MDIO/CP\_XSMI\_MDIO | 3.3V, 2.2K PU |
| MPP\[39\] | C8  | NC  | 3.3V |
| MPP\[40\] | C7  | CP\_MPP\[40\] | 3.3V, GPO2 |
| MPP\[41\] | C8  | NC  | 3.3V |
| MPP\[42\] | A6  | CP\_MPP\[42\] | 3.3V, 2.2k PU, RSVD37 |
| MPP\[43\] | C6  | CP\_MPP\[43\] | 3.3V, 2.2k PU, RSVD38 |
| MPP\[44\] | B3  | CP\_MPP\[44\] | 3.3V, 10k PD, PCIe0 clock config |
| MPP\[45\] | C4  | NC  | 3.3V, 10k PD, Reset strap |
| MPP\[46\] | B2  | NC  | 3.3V |
| MPP\[47\] | C2  | NC  | 3.3V, 2.2k PD, Reset strap |
| MPP\[48\] | C5  | NC  | 3.3V, PCIe1 clock config |
| MPP\[49\] | A3  | NC  | 3.3V |
| MPP\[50\] | D3  | CP\_MPP\[50\] | 3.3V, 2.2k PU, CP2\_SFP\_INT2 |
| MPP\[51\] | E2  | NC  | 3.3V |
| MPP\[52\] | E3  | NC  | 3.3V |
| MPP\[53\] | C3  | NC  | 3.3V |
| MPP\[54\] | C1  | NC  | 3.3V |
| MPP\[55\] | F2  | CP\_MPP\[55\] | 3.3V, RSVD55 |
| MPP\[56\] | H3  | CP\_MPP\[56\] | 3.3V, RSVD56 |
| MPP\[57\] | H2  | NC  | 3.3V |
| MPP\[58\] | G3  | NC  | 3.3V |
| MPP\[59\] | F3  | NC  | 3.3V |
| MPP\[60\] | J1  | NC  | 3.3V |
| MPP\[61\] | J2  | NC  | 3.3V |
| MPP\[62\] | F1  | NC  | 3.3V |

<a id="assembly-options"></a>

## Assembly Options

Under MOQ certain customizations are possible by special assembly. This is an incomplete list of such options:

<a id="cp0-sdio-interface-voltage-domain"></a>

#### CP0 SDIO Interface Voltage Domain

CP0 Signals MPP\[56:62\] are by default configured for 3.3V signalling. They can be switched to 1.8V by removing R349 and adding R348.

<a id="cp2-ge1-rgmii-interface-voltage-domain"></a>

#### CP2 GE1 (RGMII) Interface Voltage Domain

CP2 Signals MPP\[0:11\] are by default configured for 3.3V signalling. They can be switched to 1.8V by removing R543 and adding R544.

<a id="trusted-platform-module"></a>

#### Trusted Platform Module

The module can accomodate a TPM (SLB9670 at U15). By default modules ship without.

<a id="smb_alert_n"></a>

#### SMB\_ALERT\_N

This signal can optionally be driven by CP0 MPP\[23\] (CP0\_BOOT\_MODE\_SEL5) when assembling R536. By default it is not connected.

<a id="bios_dis0-bios_dis1"></a>

#### BIOS\_DIS0# / BIOS\_DIS1#

By default BIOS\_DIS0# controls a mux that can swap SPI CS0 (for SPI Flash on COM) and CS1 (routed to carrier) used during boot. BIOS\_DIS1# is floating by default.

Optionally BIOS\_DIS1# may control the mux if R264 is assembled, BIOS\_DIS0# may be disconnected by removing R263.

<a id="com-express-header-details"></a>

## COM Express Header Details

Following are the COM express type 7 AB and CD pin mapping –

- Pins marked with ~strikethrough~ are unused / unconnected pins
- Pins marked with Red are GND or power

<a id="ab-header"></a>

#### AB Header

| Notes | Driving IC | Pin Name | Pin Number | Pin Number | Schematics Pin Name | Driving IC | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | GND (FIXED) | A1  | B1  | GND (FIXED) |     |     |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI3- | A2  | B2  | GBE0\_ACT# | 88E1512 PHY LED\[1\] |     |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI3+ | A3  | B3  | ~LPC\_FRAME#~ |     | Not used |
| Not used |     | ~GBE0\_LINK100#~ | A4  | B4  | ~LPC\_AD0~ |     | Not used |
|     | 88E1512 PHY LED\[2\] | GBE0\_LINK1000# | A5  | B5  | ~LPC\_AD1~ |     | Not used |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI2- | A6  | B6  | ~LPC\_AD2~ |     | Not used |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI2+ | A7  | B7  | ~LPC\_AD3~ |     | Not used |
|     | 88E1512 PHY LED\[0\] | GBE0\_LINK# | A8  | B8  | ~LPC\_DRQ0#~ |     | Not used |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI1- | A9  | B9  | ~LPC\_DRQ1#~ |     | Not used |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI1+ | A10 | B10 | ~LPC\_CLK~ |     | Not used |
|     |     | GND (FIXED) | A11 | B11 | GND (FIXED) |     |     |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI0- | A12 | B12 | PWRBTN# | CP0 MPP\[31\] | 3.3V, 2.2k PU |
|     | CP0 Port 0 (RGMII) via 88E1512 PHY | GBE0\_MDI0+ | A13 | B13 | SMB\_CK | CP0 I2C1 via PCA9547AP I2C Mux @ 77 Channel 3 | 3.3V, 2.2k pull-up |
| Not used |     | ~GBE0\_CTREF~ | A14 | B14 | SMB\_DAT | CP0 I2C1 via PCA9547AP I2C Mux @ 77 Channel 3 | 3.3V, 2.2k pull-up |
| Not used |     | ~SUS\_S3#~ | A15 | B15 | SMB\_ALERT# | CP0 MPP\[23\] | 3.3V, 10k PU, assembly option |
| Serial 10nF | CP1 SD\[3\] | SATA0\_TX+ | A16 | B16 | SATA1\_TX+ | CP2 SD\[3\] | Serial 10nF |
| Serial 10nF | CP1 SD\[3\] | SATA0\_TX- | A17 | B17 | SATA1\_TX- | CP2 SD\[3\] | Serial 10nF |
| Not used |     | ~SUS\_S4#~ | A18 | B18 | ~SUS\_STAT#~ |     |     |
| Serial 10nF | CP1 SD\[3\] | SATA0\_RX+ | A19 | B19 | SATA1\_RX+ | CP2 SD\[3\] | Serial 10nF |
| Serial 10nF | CP1 SD\[3\] | SATA0\_RX- | A20 | B20 | SATA1\_RX- | CP2 SD\[3\] | Serial 10nF |
|     |     | GND (FIXED) | A21 | B21 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_TX15+~ | A22 | B22 | ~PCIE\_RX15+~ |     | Not used |
| Not used |     | ~PCIE\_TX15-~ | A23 | B23 | ~PCIE\_RX15-~ |     | Not used |
| 3.3v, 2.2k pull-up | CP0 MPP\[34\] | SUS\_S5# | A24 | B24 | PWR\_OK | Power enable | 3.3V, 4.7k PU,  <br>Refer to power-up sequence |
| Not used |     | ~PCIE\_TX14+~ | A25 | B25 | ~PCIE\_RX14+~ |     | Not used |
| Not used |     | ~PCIE\_TX14-~ | A26 | B26 | ~PCIE\_RX14+~ |     | Not used |
| 3.3V | CP1 MPP\[11\] | BATLOW# | A27 | B27 | ~WDT~ |     | Not used |
| 3.3V | CP1 MPP\[39\] | SATA\_ACT# | A28 | B28 | RSVD | CP2 MPP\[8\] | RSVD8  <br>1.8V / 3.3V |
| RSVD0  <br>1.8V / 3.3V | CP2 MPP\[0\] | RSVD | A29 | B29 | RSVD | CP2 MPP\[9\] | RSVD9  <br>1.8V / 3.3V |
| RSVD1  <br>1.8V / 3.3V | CP2 MPP\[1\] | RSVD | A30 | B30 | RSVD | CP2 MPP\[10\] | RSVD10  <br>1.8V / 3.3V |
|     |     | GND (FIXED) | A31 | B31 | GND (FIXED) |     |     |
| RSVD2  <br>1.8V / 3.3V | CP2 MPP\[2\] | RSVD | A32 | B32 | SPKR | CP1 MPP\[12\] | 3.3V |
| RSVD3  <br>1.8V / 3.3V | CP2:CP\_MPP\[3\] | RSVD | A33 | B33 | I2C\_CK | CP0 MPP\[36\] | CP0 I2C1, shared with I2C Mux @ 0x77 |
| 3.3v, 2.2k pull-up | SPI CS0/1 switch | BIOS\_DIS0# | A34 | B34 | I2C\_DAT | CP0 MPP\[35\] | CP0 I2C1, shared with I2C Mux @ 0x77 |
| 3.3V | CP1 MPP\[33\] | THRMTRIP# | A35 | B35 | THRM# | CP1 MPP\[34\] |     |
| Not used |     | ~PCIE\_TX13+~ | A36 | B36 | ~PCIE\_RX13+~ |     | Not used |
| Not used |     | ~PCIE\_TX13-~ | A37 | B37 | ~PCIE\_RX13-~ |     | Not used |
|     |     | GND | A38 | B38 | GND |     |     |
| Serial 220nF | CP1 SD\[4\] | PCIE\_TX12+ | A39 | B39 | PCIE\_RX12+ | CP1 SD\[4\] |     |
| Serial 220nF | CP1 SD\[4\] | PCIE\_TX12- | A40 | B40 | PCIE\_RX12+ | CP1 SD\[4\] |     |
|     |     | GND (FIXED) | A41 | B41 | GND (FIXED) |     |     |
|     | CP1 USB-2.0 PHY 0 | USB2- | A42 | B42 | USB3- | CP0 USB-2.0 PHY 1 |     |
|     | CP1 USB-2.0 PHY 0 | USB2+ | A43 | B43 | USB3+ | CP0 USB-2.0 PHY 1 |     |
| Not used |     | ~USB\_2\_3\_OC#~ | A44 | B44 | ~USB\_0\_1\_OC#~ |     |     |
|     | CP0 USB-2.0 PHY 0 | USB0- | A45 | B45 | USB1- | CP2 USB-2.0 PHY 0 |     |
|     | CP0 USB-2.0 PHY 0 | USB0+ | A46 | B46 | USB1+ | CP2 USB-2.0 PHY 0 |     |
| 3.3V, 100nF, assembly option for diode sharing 3.3V supply | CP0 RTC | VCC\_RTC | A47 | B47 | ~ESPI\_EN~ |     | Not used |
| RSVD4  <br>1.8V / 3.3V | CP2 MPP\[4\] | RSVD | A48 | B48 | RSVD | CP2 MPP\[11\] | RSVD11  <br>1.8V / 3.3V |
| PTP\_CP1\_CLK\_IN | CP1 MPP\[29\] | RSVD | A49 | B49 | SYS\_RESET# | System Reset input | 3.3V, 10k PU |
| Not used |     | ~LPC\_SERIRQ~ | A50 | B50 | CB\_RESET# | Carrier board reset output, can be used as PERST | 3.3V, full drive |
|     |     | GND (FIXED) | A51 | B51 | GND (FIXED) |     |     |
| Serial 220nF | CP1 SD\[1\] | PCIE\_TX5+ | A52 | B52 | PCIE\_RX5+ | CP1 SD\[1\] |     |
| Serial 220nF | CP1 SD\[1\] | PCIE\_TX5- | A53 | B53 | PCIE\_RX5- | CP1 SD\[1\] |     |
| microSD D\[0\] | CP0 MPP\[58\] | GPI0 | A54 | B54 | GPO1 | CP0 MPP\[57\] | microSD CMD |
| Serial 220nF | CP1 SD\[0\] | PCIE\_TX4+ | A55 | B55 | PCIE\_RX4+ | CP1 SD\[0\] |     |
| Serial 220nF | CP1 SD\[0\] | PCIE\_TX4- | A56 | B56 | PCIE\_RX4- | CP1 SD\[0\] |     |
|     |     | GND | A57 | B57 | GPO2 | CP2 MPP\[40\] | 3.3V |
| Serial 220nF | CP0 SD\[3\] | PCIE\_TX3+ | A58 | B58 | PCIE\_RX3+ | CP0 SD\[3\] |     |
| Serial 220nF | CP0 SD\[3\] | PCIE\_TX3- | A59 | B59 | PCIE\_RX3- | CP0 SD\[3\] |     |
|     |     | GND (FIXED) | A60 | B60 | GND (FIXED) |     |     |
| Serial 220nF | CP0 SD\[2\] | PCIE\_TX2+ | A61 | B61 | PCIE\_RX2+ | CP0 SD\[2\] |     |
| Serial 220nF | CP0 SD\[2\] | PCIE\_TX2- | A62 | B62 | PCIE\_RX2- | CP0 SD\[2\] |     |
| microSD D\[1\] | CP0 MPP\[59\] | GPI1 | A63 | B63 | GPO3/SD\_CD | CP0 MPP\[55\] | micro SD CD |
| Serial 220nF | CP0 SD\[1\] | PCIE\_TX1+ | A64 | B64 | PCIE\_RX1+ | CP0 SD\[1\] |     |
| Serial 220nF | CP0 SD\[1\] | PCIE\_TX1- | A65 | B65 | PCIE\_RX1- | CP0 SD\[1\] |     |
|     |     | GND | A66 | B66 | WAKE0# | CP1 MPP\[40\] | 3.3V, 2.2k PU |
| microSD D\[2\] | CP0 MPP\[60\] | GPI2 | A67 | B67 | WAKE1# | CP1 MPP\[51\] | 3.3V, 2.2k PU |
| Serial 220nF | CP0 SD\[0\] | PCIE\_TX0+ | A68 | B68 | PCIE\_RX0+ | CP0 SD\[0\] |     |
| Serial 220nF | CP0 SD\[0\] | PCIE\_TX0- | A69 | B69 | PCIE\_RX0- | CP0 SD\[0\] |     |
|     |     | GND (FIXED) | A70 | B70 | GND (FIXED) |     |     |
| Serial 220nF | CP0 SD\[5\] | PCIE\_TX8+ | A71 | B71 | PCIE\_RX8+ | CP0 SD\[5\] |     |
| Serial 220nF | CP0 SD\[5\] | PCIE\_TX8- | A72 | B72 | PCIE\_RX8- | CP0 SD\[5\] |     |
|     |     | GND | A73 | B73 | GND |     |     |
| Not used |     | ~PCIE\_TX9+~ | A74 | B74 | ~PCIE\_RX9+~ |     | Not used |
| Not used |     | ~PCIE\_TX9-~ | A75 | B75 | ~PCIE\_RX9-~ |     | Not used |
|     |     | GND | A76 | B76 | GND |     |     |
| Not used |     | ~PCIE\_TX10+~ | A77 | B77 | ~PCIE\_RX10+~ |     | Not used |
| Not used |     | ~PCIE\_TX10-~ | A78 | B78 | ~PCIE\_RX10-~ |     | Not used |
|     |     | GND | A79 | B79 | GND |     |     |
|     |     | GND (FIXED) | A80 | B80 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_TX11+~ | A81 | B81 | ~PCIE\_RX11+~ |     | Not used |
| Not used |     | ~PCIE\_TX11-~ | A82 | B82 | ~PCIE\_RX11-~ |     | Not used |
|     |     | GND | A83 | B83 | GND |     |     |
| Not used |     | ~NCSI\_TX\_EN~ | A84 | B84 | ~VCC\_5V\_SBY~ |     | Not used |
| microSD D\[3\] | CP0 MPP\[61\] | GPI3 | A85 | B85 | ~VCC\_5V\_SBY~ |     | Not used |
| RSVD5  <br>1.8V / 3.3V | CP2 MPP\[5\] | RSVD | A86 | B86 | ~VCC\_5V\_SBY~ |     | Not used |
| RSVD7  <br>1.8V / 3.3V | CP2 MPP\[7\] | RSVD | A87 | B87 | ~VCC\_5V\_SBY~ |     | Not used |
| HCSL PCIe Gen3 compliant | 100MHz clock generator | PCIE\_CK\_REF+ | A88 | B88 | BIOS\_DIS1# |     | SPI CS0/1 switch, asembly option |
| HCSL PCIe Gen3 compliant | 100MHz clock generator | PCIE\_CK\_REF- | A89 | B89 | ~NCSI\_RX\_ER~ |     | Not used |
|     |     | GND (FIXED) | A90 | B90 | GND (FIXED) |     |     |
|     | 3.3v power. Gated by 12v input | SPI\_POWER | A91 | B91 | ~NCSI\_CLK\_IN~ |     | Not used |
| 3.3V | CP0 MPP\[13\] | SPI\_MISO | A92 | B92 | ~NCSI\_RXD1~ |     | Not used |
| microSD CLK | CP0 MPP\[56\] | GPO0 | A93 | B93 | ~NCSI\_RXD0~ |     | Not used |
| 3.3V | CP0 MPP\[16\] | SPI\_CLK | A94 | B94 | ~NCSI\_CRS\_DV~ |     | Not used |
| 3.3V | CP0 MPP\[15\] | SPI\_MOSI | A95 | B95 | ~NCSI\_TXD1~ |     | Not used |
| 3.3V, assembly option | SLB9670 | TPM\_PP | A96 | B96 | ~NCSI\_TXD0~ |     | Not used |
| Not used |     | ~TYPE10#~ | A97 | B97 | SPI\_CS# | CP0 MPP\[14\] / CP0 MPP\[12\] selected by BIOS\_DIS0# | 3.3V |
| 3.3V | AP MPP\[11\] | SER0\_TX | A98 | B98 | ~NCSI\_ARB\_IN~ |     | Not used |
| 3.3V | AP MPP\[19\] | SER0\_RX | A99 | B99 | ~NCSI\_ARB\_OUT~ |     | Not used |
|     |     | GND (FIXED) | A100 | B100 | GND (FIXED) |     |     |
| 3.3V | CP0 MPP\[50\] | CAN0/SER1\_TX | A101 | B101 | FAN\_PWMOUT | CP0 MPP\[39\] & EMC2301 | EMC2301 is assembly option |
| 3.3V | CP0 MPP\[51\] | CAN0/SER1\_RX | A102 | B102 | FAN\_TACHIN | CP0 MPP\[26\] & EMC2301 | EMC2301 is assembly option |
| Not used |     | ~LID#~ | A103 | B103 | ~SLEEP#~ |     | Not used |
|     | 12v input (9v-15v) | VCC\_12V | A104 | B104 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12v input (9v-15v) | VCC\_12V | A105 | B105 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12v input (9v-15v) | VCC\_12V | A106 | B106 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12v input (9v-15v) | VCC\_12V | A107 | B107 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12v input (9v-15v) | VCC\_12V | A108 | B108 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12v input (9v-15v) | VCC\_12V | A109 | B109 | VCC\_12V | 12V input (9v-15v) |     |
|     |     | GND (FIXED) | A110 | B110 | GND (FIXED) |     |     |

<a id="cd-header"></a>

#### CD Header

| Notes | Driving IC | Schematics Pin Name | Pin Number | Pin Number | Schematics Pin Name | Driving IC | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | GND (FIXED) | C1  | D1  | GND (FIXED) |     |     |
|     |     | GND | C2  | D2  | GND |     |     |
| Not used |     | ~USB\_SSRX0-~ | C3  | D3  | ~USB\_SSTX0-~ |     | Not used |
| Not used |     | ~USB\_SSRX0+~ | C4  | D4  | ~USB\_SSTX0+~ |     | Not used |
|     |     | GND | C5  | D5  | GND |     |     |
|     | CP2 SD\[1\] | USB\_SSRX1- | C6  | D6  | USB\_SSTX1- | CP2 SD\[1\] | Serial 100nF |
|     | CP2 SD\[1\] | USB\_SSRX1+ | C7  | D7  | USB\_SSTX1+ | CP2 SD\[1\] | Serial 100nF |
|     |     | GND | C8  | D8  | GND |     |     |
| Not used |     | ~USB\_SSRX2-~ | C9  | D9  | ~USB\_SSTX2-~ |     | Not used |
| Not used |     | ~USB\_SSRX2+~ | C10 | D10 | ~USB\_SSTX2+~ |     | Not used |
|     |     | GND (FIXED) | C11 | D11 | GND (FIXED) |     |     |
| Not used |     | ~USB\_SSRX3-~ | C12 | D12 | ~USB\_SSTX3-~ |     | Not used |
| Not used |     | ~USB\_SSRX3+~ | C13 | D13 | ~USB\_SSTX3+~ |     | Not used |
|     |     | GND | C14 | D14 | GND |     |     |
| Not used |     | ~10G\_PHY\_MDC\_SCL3~ | C15 | D15 | ~10G\_PHY\_MDIO\_SDA3~ |     | Not used |
| 3.3V, 2.2k pull-up  <br>Can be configured as I2C | CP2 MPP\[37\] | 10G\_PHY\_MDC\_SCL2 | C16 | D16 | 10G\_PHY\_MDIO\_SDA2 | CP2 MPP\[38\] | 3.3V, 2.2k pull-up  <br>Can be configured as I2C |
| 3.3V, PTP\_CP0\_CLK\_IN | CP0 MPP\[29\] | 10G\_SDP2 | C17 | D17 | 10G\_SDP3 | CP2 MPP\[29\] | 3.3V, PTP\_CP2\_CLK\_IN |
|     |     | GND | C18 | D18 | GND |     |     |
| Not used |     | ~PCIE\_RX6+~ | C19 | D19 | ~PCIE\_TX6+~ |     | Not used |
| Not used |     | ~PCIE\_RX6-~ | C20 | D20 | ~PCIE\_TX6-~ |     | Not used |
|     |     | GND (FIXED) | C21 | D21 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_RX7+~ | C22 | D22 | ~PCIE\_TX7+~ |     | Not used |
| Not used |     | ~PCIE\_RX7-~ | C23 | D23 | ~PCIE\_TX7-~ |     | Not used |
| 3.3V, 2.2k PU | CP2 MPP\[50\] | 10G\_INT2 | C24 | D24 | ~10G\_INT3~ |     | Not used |
|     |     | GND | C25 | D25 | GND |     |     |
| Not used |     | ~10G\_KR\_RX3+~ | C26 | D26 | ~10G\_KR\_TX3+~ |     | Not used |
| Not used |     | ~10G\_KR\_RX3-~ | C27 | D27 | ~10G\_KR\_TX3-~ |     | Not used |
|     |     | GND | C28 | D28 | GND |     |     |
|     | CP2 SD\[2\] | 10G\_KR\_RX2+ | C29 | D29 | 10G\_KR\_TX2+ | CP2 SD\[2\] |     |
|     | CP2 SD\[2\] | 10G\_KR\_RX2- | C30 | D30 | 10G\_KR\_TX2- | CP2 SD\[2\] |     |
|     |     | GND (FIXED) | C31 | D31 | GND (FIXED) |     |     |
| Not used |     | ~10G\_SFP\_SDA3~ | C32 | D32 | ~10G\_SFP\_SCL3~ |     | Not used |
| 3.3V, 2.2k PU | CP2 MPP\[35\] | 10G\_SFP\_SDA2 | C33 | D33 | 10G\_SFP\_SCL2 | CP2 MPP\[36\] | 3.3V, 2.2k PU |
| 3.3V, 2.2k PU | CP1 MPP\[42\] | 10G\_PHY\_RST\_23 | C34 | D34 | 10G\_PHY\_CAP\_23 | CP2 MPP\[31\] | 3.3V, RSVD31 |
| 3.3V, 2.2k PU | CP1 MPP\[43\] | 10G\_PHY\_RST\_01 | C35 | D35 | 10G\_PHY\_CAP\_01 | CP2 MPP\[32\] | 3.3V, RSVD32 |
| 3.3V, 2.2k PU | CP0 I2C1 via PCA9547AP I2C Mux @ 77 Channel 1 | 10G\_LED\_SDA | C36 | D36 | RSVD | CP1 MPP\[28\] | 3.3V, PTP\_CP1\_PULSE |
| 3.3V, 2.2k PU | CP0 I2C1 via PCA9547AP I2C Mux @ 77 Channel 1 | 10G\_LED\_SCL | C37 | D37 | RSVD |     | Not used |
| 3.3V, 2.2k PU | CP1 MPP\[35\] | 10G\_SFP\_SDA1 | C38 | D38 | 10G\_SFP\_SCL1 | CP1 MPP\[36\] | 3.3V, 2.2k PU |
| 3.3V, 2.2k PU | CP0 I2C1 via PCA9547AP I2C Mux @ 77 Channel 2 | 10G\_SFP\_SDA0 | C39 | D39 | 10G\_SFP\_SCL0 | CP0 I2C1 via PCA9547AP I2C Mux @ 77 Channel 2 | 3.3V, 2.2k PU |
| 3.3V, PTP\_CP0\_PULSE | CP0 MPP\[28\] | 10G\_SDP0 | C40 | D40 | 10G\_SDP1 | CP2 MPP\[28\] | 3.3V, PTP\_CP2\_PULSE |
|     |     | GND (FIXED) | C41 | D41 | GND (FIXED) |     |     |
|     | CP1 SD\[2\] | 10G\_KR\_RX1+ | C42 | D42 | 10G\_KR\_TX1+ | CP1 SD\[2\] |     |
|     | CP1 SD\[2\] | 10G\_KR\_RX1- | C43 | D43 | 10G\_KR\_TX1- | CP1 SD\[2\] |     |
|     |     | GND | C44 | D44 | GND |     |     |
| 3.3V, 2.2k PU,  <br>Can be configured as I2C | CP1 MPP\[37\] | 10G\_PHY\_MDC\_SCL1 | C45 | D45 | 10G\_PHY\_MDIO\_SDA1 | CP1 MPP\[38\] | 3.3V, 2.2k PU,  <br>Can be configured as I2C |
| 3.3V, 2.2k PU, shared with PHY on COM | CP0 MPP\[41\] (/ CP0 MPP\[42\]) | 10G\_PHY\_MDC\_SCL0 | C46 | D46 | 10G\_PHY\_MDIO\_SDA0 | CP0 MPP\[40\] (/ CP0 MPP\[43\]) | 3.3V, 2.2k PU, shared with PHY on COM |
| 3.3V, 2.2k PU | CP0 MPP\[24\] | 10G\_INT0 | C47 | D47 | 10G\_INT1 | CP1 MPP\[50\] | 3.3V, 2.2k PU |
|     |     | GND | C48 | D48 | GND |     |     |
|     | CP0 SD\[4\] | 10G\_KR\_RX0+ | C49 | D49 | 10G\_KR\_TX0+ | CP0 SD\[4\] |     |
|     | CP0 SD\[4\] | 10G\_KR\_RX0- | C50 | D50 | 10G\_KR\_TX0- | CP0 SD\[4\] |     |
|     |     | GND (FIXED) | C51 | D51 | GND (FIXED) |     |     |
|     | CP1 SD\[5\] | PCIE\_RX16+ | C52 | D52 | PCIE\_TX16+ | CP1 SD\[5\] | Serial 220nF |
|     | CP1 SD\[5\] | PCIE\_RX16- | C53 | D53 | PCIE\_TX16- | CP1 SD\[5\] | Serial 220nF |
| Indicate TYPE 7# | GND | TYPE0# | C54 | D54 | RSVD | CP2 MPP\[6\] | 1.8V / 3.3V, RSVD6 |
| Not used |     | ~PCIE\_RX17+~ | C55 | D55 | ~PCIE\_TX17+~ |     | Not used |
| Not used |     | ~PCIE\_RX17-~ | C56 | D56 | ~PCIE\_TX17-~ |     | Not used |
| Not used |     | TYPE1# | C57 | D57 | TYPE2# | GND | Indicate TYPE 7# |
| Not used |     | ~PCIE\_RX18+~ | C58 | D58 | ~PCIE\_TX18+~ |     | Not used |
| Not used |     | ~PCIE\_RX18-~ | C59 | D59 | ~PCIE\_TX18-~ |     | Not used |
|     |     | GND (FIXED) | C60 | D60 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_RX19+~ | C61 | D61 | ~PCIE\_TX19+~ |     | Not used |
| Not used |     | ~PCIE\_RX19-~ | C62 | D62 | ~PCIE\_TX19-~ |     | Not used |
| 3.3V, RSVD56 | CP2 MPP\[56\] | RSVD | C63 | D63 | RSVD | CP1 MPP\[52\] | 3.3V, RCVR0\_CLK\_CP1 |
| 3.3V, RSVD27 | CP2 MPP\[27\] | RSVD | C64 | D64 | RSVD | CP2 MPP\[30\] | 3.3V, PTP\_CP2\_PCLK\_OUT |
|     | CP2 SD\[0\] | PCIE\_RX20+ | C65 | D65 | PCIE\_TX20+ | CP2 SD\[0\] | Serial 220nF |
|     | CP2 SD\[0\] | PCIE\_RX20- | C66 | D66 | PCIE\_TX20- | CP2 SD\[0\] | Serial 220nF |
|     |     | ~RAPID\_SHUTDOWN~ | C67 | D67 | GND |     |     |
| Not used |     | ~PCIE\_RX21+~ | C68 | D68 | ~PCIE\_TX21+~ |     | Not used |
| Not used |     | ~PCIE\_RX21-~ | C69 | D69 | ~PCIE\_TX21-~ |     | Not used |
|     |     | GND (FIXED) | C70 | D70 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_RX22+~ | C71 | D71 | ~PCIE\_TX22+~ |     | Not used |
| Not used |     | ~PCIE\_RX22-~ | C72 | D72 | ~PCIE\_TX22-~ |     | Not used |
|     |     | GND | C73 | D73 | GND |     |     |
| Not used |     | ~PCIE\_RX23+~ | C74 | D74 | ~PCIE\_TX23+~ |     | Not used |
| Not used |     | ~PCIE\_RX23-~ | C75 | D75 | ~PCIE\_TX23-~ |     | Not used |
|     |     | GND | C76 | D76 | GND |     |     |
| 3.3V, RSVD37 | CP2 MPP\[42\] | RSVD | C77 | D77 | RSVD | CP0 MPP\[30\] | 3.3V, PTP\_CP0\_PCLK\_OUT |
|     | CP2 SD\[4\] | PCIE\_RX24+ | C78 | D78 | PCIE\_TX24+ | CP2 SD\[4\] | Serial 220nF |
|     | CP2 SD\[4\] | PCIE\_RX24- | C79 | D79 | PCIE\_TX24- | CP2 SD\[4\] | Serial 220nF |
|     |     | GND (FIXED) | C80 | D80 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_RX25+~ | C81 | D81 | ~PCIE\_TX25+~ |     | Not used |
| Not used |     | ~PCIE\_RX25-~ | C82 | D82 | ~PCIE\_TX25-~ |     | Not used |
| 3.3V, RSVD38 | CP2 MPP\[43\] | RSVD | C83 | D83 | RSVD | CP1 MPP\[30\] | 3.3V, PTP\_CP1\_PCLK\_OUT |
|     |     | GND | C84 | D84 | GND |     |     |
| Not used |     | ~PCIE\_RX26+~ | C85 | D85 | ~PCIE\_TX26+~ |     | Not used |
| Not used |     | ~PCIE\_RX26-~ | C86 | D86 | ~PCIE\_TX26-~ |     | Not used |
|     |     | GND | C87 | D87 | GND |     |     |
| Not used |     | ~PCIE\_RX27+~ | C88 | D88 | ~PCIE\_TX27+~ |     | Not used |
| Not used |     | ~PCIE\_RX27-~ | C89 | D89 | ~PCIE\_TX27-~ |     | Not used |
|     |     | GND (FIXED) | C90 | D90 | GND (FIXED) |     |     |
|     | CP2 SD\[5\] | PCIE\_RX28+ | C91 | D91 | PCIE\_TX28+ | CP2 SD\[5\] | Serial 220nF |
|     | CP2 SD\[5\] | PCIE\_RX28- | C92 | D92 | PCIE\_TX28- | CP2 SD\[5\] | Serial 220nF |
|     |     | GND | C93 | D93 | GND |     |     |
| Not used |     | ~PCIE\_RX29+~ | C94 | D94 | ~PCIE\_TX29+~ |     | Not used |
| Not used |     | ~PCIE\_RX29-~ | C95 | D95 | ~PCIE\_TX29-~ |     | Not used |
|     |     | GND | C96 | D96 | GND |     |     |
| 3.3V, RSVD55 | CP2 MPP\[55\] | RSVD | C97 | D97 | RSVD | CP0 MPP\[52\] | 3.3V, RCVR1\_CLK\_CP0 |
| Not used |     | ~PCIE\_RX30+~ | C98 | D98 | ~PCIE\_TX30+~ |     | Not used |
| Not used |     | ~PCIE\_RX30-~ | C99 | D99 | ~PCIE\_TX30-~ |     | Not used |
|     |     | GND (FIXED) | C100 | D100 | GND (FIXED) |     |     |
| Not used |     | ~PCIE\_RX31+~ | C101 | D101 | ~PCIE\_TX31+~ |     | Not used |
| Not used |     | ~PCIE\_RX31-~ | C102 | D102 | ~PCIE\_TX31-~ |     | Not used |
|     |     | GND | C103 | D103 | GND |     |     |
|     | 12V input (9v-15v) | VCC\_12V | C104 | D104 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12V input (9v-15v) | VCC\_12V | C105 | D105 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12V input (9v-15v) | VCC\_12V | C106 | D106 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12V input (9v-15v) | VCC\_12V | C107 | D107 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12V input (9v-15v) | VCC\_12V | C108 | D108 | VCC\_12V | 12V input (9v-15v) |     |
|     | 12V input (9v-15v) | VCC\_12V | C109 | D109 | VCC\_12V | 12V input (9v-15v) |     |
|     |     | GND (FIXED) | C110 | D110 | GND (FIXED) |     |     |

<a id="common-questions-and-answers"></a>

## Common Questions and Answers

**Q:** Are the I2C signals 3.3v?

**A:** Per the COM express specifications, all GPIO and control signals are in the 3.3v domain. Please refer to the AB and CD header description on the pull-up values of those signals.  

**Q:** Can the SERDES lanes be configured differently than the COM express standard?

**A:** Yes.  

<a id="documentation"></a>

## Documentation

      

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-2ca05027-d13f-444d-8286-66d9e11a01fd)<br><br>[Preview] [View](/wiki/download/attachments/197493937/CN9132+COM+3D-files.zip?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493937&fileName=CN9132+COM+3D-files.zip&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493937&fileName=CN9132+COM+3D-files.zip) | ZIP Archive [CN9132 COM 3D-files.zip](/wiki/download/attachments/197493937/CN9132%20COM%203D-files.zip?api=v2) | Nov 08, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-e3293594-24b1-4571-a1a5-e1832398654d)<br><br>[Preview] [View](/wiki/download/attachments/197493937/CN9132+COM_1.1-simplified-schematics.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=197493937&fileName=CN9132+COM_1.1-simplified-schematics.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=197493937&fileName=CN9132+COM_1.1-simplified-schematics.pdf) | PDF File [CN9132 COM\_1.1-simplified-schematics.pdf](/wiki/download/attachments/197493937/CN9132%20COM_1.1-simplified-schematics.pdf?api=v2) | Nov 08, 2021 by [SolidRun](/wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f) |

[Download All](/wiki/download/all_attachments?pageId=197493937)

[ Buy a Sample Now](https://shop.solid-run.com/?s=CEx7+CN9132&post_type=product)

<a id="related-articles"></a>

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden