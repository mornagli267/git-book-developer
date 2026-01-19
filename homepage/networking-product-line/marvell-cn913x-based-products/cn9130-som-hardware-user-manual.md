# CN9130 SOM Hardware User Manual

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Revision** | **Notes**                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------------- |
| 26 Sep 2021       | Alon Rotman                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.0          | <p>Initial release<br><br>information 2. Relevant for PCB revision 1.0</p>               |
| 24 Nov 2021       | Alon Rotman                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.1          |                                                                                          |
| Oct 29,2023       | Rabeeh Khoury                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1.2          | Added PCB rev 1.3 3D Model in Documentation section                                      |
| Sep 02, 2024      | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.3          | Updated AP/CP Signal usage and B2B connectors tables according to production version SoM |
| Sep 10, 2024      | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.3.1        | Updated J3 SPI/USB signals                                                               |
| Sep 12, 2024      | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.3.2        | removed invalid mating connector part number for J3                                      |
| Sep 16, 2024      | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.3.3        | added ptp signal descriptions                                                            |
| Dec 01, 2024      | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.4          | updated core clock signal descriptions to match pinout tables                            |
| Table of Contents | <p>- <a href="cn9130-som-hardware-user-manual.md#revision-and-notes">Revision and Notes</a><br>- <a href="cn9130-som-hardware-user-manual.md#introduction">Introduction</a><br>- <a href="cn9130-som-hardware-user-manual.md#overview">Overview</a><br>- <a href="cn9130-som-hardware-user-manual.md#block-diagram">Block Diagram</a><br>- <a href="cn9130-som-hardware-user-manual.md#specifications">Specifications</a><br>- <a href="cn9130-som-hardware-user-manual.md#compatibility-between-soms-a388-and-cn9130">Compatibility between SOMs A388 and CN9130</a><br>- <a href="cn9130-som-hardware-user-manual.md#power-consumption">Power Consumption</a><br>- <a href="cn9130-som-hardware-user-manual.md#frequency-scaling">Frequency Scaling</a><br>- <a href="cn9130-som-hardware-user-manual.md#power-measurments">Power Measurments</a><br>- <a href="cn9130-som-hardware-user-manual.md#cn9130-som-extensions">CN9130 SOM extensions</a><br>- <a href="cn9130-som-hardware-user-manual.md#serdes-muxing-cn9130-cp0">SERDES Muxing CN9130 – CP0:</a><br>- <a href="cn9130-som-hardware-user-manual.md#core-clock-boot-straps">CORE Clock BOOT Straps</a><br>- <a href="cn9130-som-hardware-user-manual.md#boot-mode-boot-straps">BOOT MODE BOOT Straps</a><br>- <a href="cn9130-som-hardware-user-manual.md#cp0-mpp620">CP0 MPP[62:0]</a><br>- <a href="cn9130-som-hardware-user-manual.md#som-header-details">SOM Header Details</a><br>- <a href="cn9130-som-hardware-user-manual.md#connector-j1">Connector J1</a><br>- <a href="cn9130-som-hardware-user-manual.md#connector-j2">Connector J2</a><br>- <a href="cn9130-som-hardware-user-manual.md#connector-j3">Connector J3</a><br>- <a href="cn9130-som-hardware-user-manual.md#heatsink">Heatsink</a><br>- <a href="cn9130-som-hardware-user-manual.md#precision-time-protocol-ptp">Precision Time Protocol (PTP)</a><br>- <a href="cn9130-som-hardware-user-manual.md#enable-ptp-on-clearfog-base-pro">Enable PTP on Clearfog Base / Pro</a><br>- <a href="cn9130-som-hardware-user-manual.md#documentation">Documentation</a></p> |              |                                                                                          |

{% hint style="info" %}
No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.
{% endhint %}


## Introduction

This document is intended for hardware engineers that are willing to integrate the [CN9130 SOM](https://www.solid-run.com/embedded-networking/marvell-octeon-tx2-family/cn9130-som/) from SolidRun ltd, into their own design.

The document provides details with regards CN9130 SOM rev 1.1.

The CN9130 SOM is pin and size compatible to the A388 SOM by SolidRun and can be used as an upgrade for the existing ClearFog Base and ClearFog Pro.&#x20;

{% hint style="warning" %}
**Note:** the pinout of the CN9130 and A388 are slightly different due to the MPP muxing of each SoC. please review carefully the tables below
{% endhint %}


#### Overview

CN9130 System On Module is a highly integrated SOM module based on Marvell’s CN9130 SoC.

The SoC highlights are up to 2.2GHz with 4 Cortex A72 Arm cores, DDR4 controller and 6 high speed SERDESs.

The module integrates the following features –

1. CN9130 SoC (up to 2.2GHz).
2. &#x20;On board 64bit DDR4 bus supporting up to 16GB at 2400MT/s without ECC
3. Single 12V or 5V DC-input is required.

#### Block Diagram

![](<../../../.gitbook/assets/CN9130 SOM block diagram.png>)

#### Specifications

|                        |                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Features**           | **CN9130 SOM Specifications**                                                                                                                       |
| Processor Core         | 4 cores Arm Cortex A72                                                                                                                              |
| Processor speed        | <p>2.2GHz (Commercial)<br>2GHz (Industrial)</p>                                                                                                     |
| DDR                    | <p>On board DDR4:<br>Up to 16GB @ 2400MT/s<br>64bit (+ optional 8bit of ECC)</p>                                                                    |
| eMMC                   | Up to 64GB (assembled 8GB)                                                                                                                          |
| Flash                  | 64Mbit SPI NOR flash                                                                                                                                |
| SATA 3.0               | up to 2 Ports                                                                                                                                       |
| Ethernet               | <p>1x MDI using 88E1512 PHY<br><br>1x 10/5 GbE port + 2x 1/2.5 GbE Ports<br>or<br>2x 5 GbE Port +1x 1/2.5 GbE Port</p>                              |
| PCIe gen 3.0           | <p>1 Port x4 + 2 Ports x 1<br>Total of 3 controllers and up to 6 lanes</p>                                                                          |
| USB 3.0                | Up to 2 x USB 3.0 (Host/Device)                                                                                                                     |
| I2C                    | 2                                                                                                                                                   |
| SMI & XSMI             | 2                                                                                                                                                   |
| UART                   | 2                                                                                                                                                   |
| PPS/PTP/Sync-E support | Untested, for authoritative information, consult Marvell documentation and Errata (available under NDA).                                            |
| SPI bus                | ✓                                                                                                                                                   |
| RTC support            | ✓                                                                                                                                                   |
| Power                  | <p>5V to 12V DC-input<br>11.3W full system</p>                                                                                                      |
| Supported OS           | Linux kernel 5.8x Yocto DPDK UEFI KVM/QEMU/Containers NFV Openstack compute node                                                                    |
| Environment            | <p>Commercial: 0°C to 70°C<br>Industrial: -40°C to 85°C<br>Humidity (non-condensing): 10% – 90%</p>                                                 |
| Dimensions             | 49mm X 35mm                                                                                                                                         |
|                        | [Buy Now](https://shop.solid-run.com/product-category/networking-soms-coms/cn9130-som/?_ga=2.268861170.2016484779.1641802897-2012112798.1622706355) |

#### Compatibility between SOMs A388 and CN9130

Both SOMs have exactly the same form factor and footprint

The CN9130 SOM was designed to support SolidRun’s ClearFog Base/Pro. In case of any custom design based on A388 that wants to upgrade to CN9130, any case needs to be examined individually and  review carefully the borad-to-board pinout&#x20;

In the documentation section there is an excel table with exact pinout difference&#x20;

Main differences due to SoC pinout:

|                  |                             |                               |
| ---------------- | --------------------------- | ----------------------------- |
| **Feature**      | **A388**                    | **CN9130**                    |
| USB2.0           | 3 Ports                     | 2 Ports                       |
| SATA 3.0         | 3 Ports                     | 2 Ports                       |
| 125MHz clock out | ✓                           | X                             |
| SD/EMMC Boot     | boot from either SD or eMMC | Can boot from both SD or eMMC |
| MCi interface    | X                           | ✓ – Connector J3              |
| input voltage    | 5V and 3.3V                 | 5V                            |

#### Power Consumption

The following power consumption measurements were conducted on the following setup:

1. Clearfog Pro carrier board
2. Voltage / current measurement on v\_5v0 voltage rail
3. No mPCIe / USB / SATA / ETH cable were connected to the carrier board
4. Temperature measurement was taken from linux using the following command\
   ‘cat /sys/class/thermal/thermal\_zone?/temp’
5. Current and Voltage measured using an oscilloscope&#x20;
6. Linux command ‘memtester 100M > /dev/null &’ ran 4 times according to core count
7. Linux command ‘cpuburn-krait’ is ran 4 times in background. The reason cpuburn-krait was chosen is since it can generate most heat out of the cores (the core pipeline are most utilized)\
   &#x20;

#### Frequency Scaling

In order to improve power efficiency and increase temperature limits, SolidRun had enabled cpu frequency scaling.

Please refer to the patch below for more information.

[https://github.com/SolidRun/cn913x\_build/commit/5fe77346371a230fd2468bfb11cbcc2c1ea10345](https://github.com/SolidRun/cn913x_build/commit/5fe77346371a230fd2468bfb11cbcc2c1ea10345)

SolidRun, recommends to not disable the frequency scaling feature.

#### Power Measurments

The measurements below were conducted without frequency scaling, to reflect the maximum power consumption:

|                                 |                                |                              |
| ------------------------------- | ------------------------------ | ---------------------------- |
| **Test**                        | **Power \[W]**                 | **Tj \[degC]**               |
| Idle u-boot                     | 4.6                            | 50                           |
| idle Linux                      | <p>4.08<br>4.2<br>4.7<br>5</p> | <p>53<br>65<br>90<br>105</p> |
| memtester 64bit 2400MT/s        | <p>9.25<br>10.1<br>11.3</p>    | <p>70<br>85<br>105</p>       |
| cpuburn-karit 4 cores at 2.2GHz | <p>9.3<br>9.86<br>10.8</p>     | <p>70<br>90<br>105</p>       |

## CN9130 SOM extensions

The CN9130 has two extension busses of  high performance, low latency and low power Marvell® MoChi interfaces (MCi). Each bus is comprised of 4x high speed differential pairs and a dedicated LVDS clock. Both busses are exposed through the SOM connector,  enabling to connect 1 or 2 additional 88F8215 comprising the kits of CN9131 and CN9132 on the carrier board and extending the SERDES count from 6 to 12 or 18.&#x20;

#### SERDES Muxing CN9130 – CP0:

|                                            |                    |                      |                    |                    |                          |                   |
| ------------------------------------------ | ------------------ | -------------------- | ------------------ | ------------------ | ------------------------ | ----------------- |
| **Interface**                              | **SERDES Lane0**   | **SERDES Lane1**     | **SERDES Lane2**   | **SERDES Lane3**   | **SERDES Lane4**         | **SERDES Lane5**  |
| 10GBASE-R/XFI                              |                    |                      | ETH\_Port0         |                    | ETH\_Port0               |                   |
| 5GBASE-R                                   |                    |                      | ETH\_Port0         |                    | ETH\_Port0 or ETH\_Port1 |                   |
| 10GBASE-X2 (RXAUI)                         |                    |                      | ETH\_Port0 Lane 0  | ETH\_Port0 Lane 1  | ETH\_Port0 Lane0         | ETH\_Port0 Lane 1 |
| 1000BASE-X (SGMII) / 2.5GBASE-X (HS-SGMII) | ETH\_Port1         | ETH\_Port2           | ETH\_Port0         | ETH\_Port1         | ETH\_Port0 or ETH\_Port1 | ETH\_Port2        |
| SATA 3.0                                   | SATA1              | SATA0                | SATA0              | SATA1              |                          | SATA1             |
| USB 3.0 HOST                               |                    | USB 3.0 Port0 Host   | USB 3.0 Port0 Host | USB 3.0 Port1 Host | USB 3.0 Port1 Host       |                   |
| USB 3.0 Device                             |                    | USB 3.0 Port0 Decive |                    |                    | USB 3.0 Port0 Decive     |                   |
| PCIe RC/EP                                 | PCIex4 Port0 LANE0 | PCIex4 Port0 LANE1   | PCIex4 Port0 LANE2 | PCIex4 Port0 LANE3 | PCIex1 Port1             | PCIex1 Port2      |
| **Assignment on Clearfog Base**            | SATA0 Port 1       | USB-3.0 Host Port0   | XFI ETH Port0      | SGMII ETH Port1    | USB-3.0 Host Port 1      | PCIe Gen3 Port 2  |
| **Assignment on Clearfog Pro**             | SATA0 Port 1       | USB-3.0 Host Port0   | XFI ETH Port0      | SGMII ETH Port1    | PCIe Gen3 Port 1         | PCIe Gen3 Port 2  |

The following port configuration can’t be used simultaneously:

* SGMII port 0 / HS SGMII port0, RXAUI and XFI/10GBASE
* SGMII port 1 and HS SGMII port 1
* SGMII port 2 and HS SGMII port 2

#### CORE Clock BOOT Straps

* PLL\_SEL\[0] – MPP\[15] – CP\_SPI1\_MOSI
* PLL\_SEL\[1] – MPP\[16] – CP\_SPI1\_SCK
* PLL\_SEL\[2] – MPP\[17] – CP0\_SYS\_PLL\_SEL2
* PLL\_SEL\[3] – MPP\[46] (not exposed on B2B connector, 10K pull-down on SoM)

|                       |                                   |
| --------------------- | --------------------------------- |
| **Core Clock \[MHz]** | **Configuration PLL\_SEL \[3:0]** |
| 1600                  | 0x0000 (0h0)                      |
| 2000                  | 0x0010 (0h2)                      |
| 2200                  | 0x0100 (0h4)                      |

#### BOOT MODE BOOT Straps

* BOOT\_MODE\[0] – MPP18, 10K PU
* BOOT\_MODE\[1] – MPP19, 10K PU
* BOOT\_MODE\[2] – MPP20, 10K PD (not exposed on B2B connector)
* BOOT\_MODE\[3] – MPP21, 10K PU
* BOOT\_MODE\[4] – MPP22, 10K PU (not exposed on B2B connector)
* BOOT\_MODE\[5] – MPP23, 10K PU (not exposed on B2B connector)

|                                         |                                     |
| --------------------------------------- | ----------------------------------- |
| **BOOT MODE**                           | **Configuration BOOT\_MODE \[5:0]** |
| SD Card (CP\_SD)                        | 0b101001 (0x29)                     |
| eMMC (AP\_SD)                           | 0b101010 (0x2A)                     |
| NOR Flash SPI 24 address bit (CP\_SPI1) | 0b110010 (0x32)                     |
| SD Card (CP\_SD, undocumented)          | 0b111001 (0x39)                     |
| eMMC (AP\_SD, undocumented)             | 0b111010 (0x3A)                     |

#### CP0 MPP\[62:0]

| MPP #        | Pin # | Pin Description      | Notes                                                                |
| ------------ | ----- | -------------------- | -------------------------------------------------------------------- |
| AP\_MPP\[0]  | AP10  | AP\_SD\_CLK          | 1.8V, serial 22ohm resistor                                          |
| AP\_MPP\[1]  | AT10  | AP\_SD\_CMD          | 1.8V, 10K PU                                                         |
| AP\_MPP\[2]  | AP16  | AP\_SD\_D\[0]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[3]  | AP18  | AP\_SD\_D\[1]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[4]  | AT16  | AP\_SD\_D\[2]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[5]  | AP14  | AP\_SD\_D\[3]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[6]  | AP12  | AP\_SD\_DS           | RCLK, 10K PD                                                         |
| AP\_MPP\[7]  | AT14  | AP\_SD\_D\[4]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[8]  | AT12  | AP\_SD\_D\[5]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[9]  | AT18  | AP\_SD\_D\[6]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[10] | AV18  | AP\_SD\_D\[7]        | 1.8V, 10K PU                                                         |
| AP\_MPP\[11] | AY18  | AP\_UA0\_TXD         | <p>PD - Reset strap<br>3.3V thorough FXL2TD245L10X level shifter</p> |
| AP\_MPP\[12] | BA17  | AP\_SD\_HW\_RST      | 1.8V, 10K PD                                                         |
| AP\_MPP\[19] | AW17  | AP\_UA0\_RXD         | 3.3V thorough FXL2TD245L10X level shifter                            |
| MPP\[0]      | AY38  | CP\_SMI\_MDIO        | 1.8V                                                                 |
| MPP\[1]      | AV38  | CP\_SMI\_MDC         | 1.8V                                                                 |
| MPP\[2]      | AW39  | CP\_UA1\_RXD         | 3.3V thorough FXL2TD245L10X level shifter                            |
| MPP\[3]      | AY40  | CP\_UA1\_TXD         | 3.3V through FXL2TD245L10X level shifter                             |
| MPP\[4]      | AW41  | CP\_GPIO\[4]         | 1.8V                                                                 |
| MPP\[5]      | BA39  | CP\_GPIO\[5]         | 1.8V                                                                 |
| MPP\[6]      | AW35  | CP\_PTP\_PULSE       | 1.8V                                                                 |
| MPP\[7]      | AY36  | CP\_PTP\_CLK         | 1.8V                                                                 |
| MPP\[8]      | BA37  | CP\_PTP\_PCLK\_OUT   | 1.8V                                                                 |
| MPP\[9]      | AW37  | NC                   |                                                                      |
| MPP\[10]     | BA35  | DDR\_SPD\_STRAP0     | 1.8V, PU ECC / PD No ECC                                             |
| MPP\[11]     | AV36  | DDR\_SPD\_STRAP1     | 1.8V, PU 8GB, PD 4GB                                                 |
| MPP\[12]     | AV32  | CP\_SPI1\_CSn\[1]    | 3.3V                                                                 |
| MPP\[13]     | AY34  | CP\_SPI1\_MISO       | 3.3V                                                                 |
| MPP\[14]     | AT36  | CP\_SPI1\_CSn\[0]    | 3.3V                                                                 |
| MPP\[15]     | AT32  | CP\_SPI1\_MOSI       | <p>3.3V, CPU Subsystem Clock<br>CP0_SYS_PLL_SEL0</p>                 |
| MPP\[16]     | AV34  | CP\_SPI1\_SCK        | <p>3.3V, CPU Subsystem Clock<br>CP0_SYS_PLL_SEL1</p>                 |
| MPP\[17]     | BA29  | CP\_GPIO\[17]        | <p>3.3V, PD 50k, CPU Subsystem Clock<br>CP0_SYS_PLL_SEL2</p>         |
| MPP\[18]     | AW29  | CP\_BOOT\_MODE\_SEL0 | 3.3V, Boot Mode\[0]                                                  |
| MPP\[19]     | AV30  | CP\_BOOT\_MODE\_SEL1 | 3.3V, Boot Mode\[1]                                                  |
| MPP\[20]     | BA31  | CP\_BOOT\_MODE\_SEL2 | 3.3V, Boot Mode\[2]                                                  |
| MPP\[21]     | AT30  | CP\_BOOT\_MODE\_SEL3 | 3.3V, Boot Mode\[3]                                                  |
| MPP\[22]     | AY30  | CP\_BOOT\_MODE\_SEL4 | 3.3V, Boot Mode\[4]                                                  |
| MPP\[23]     | AP32  | CP\_BOOT\_MODE\_SEL5 | 3.3V, Boot Mode\[5]                                                  |
| MPP\[24]     | AP34  | NC                   |                                                                      |
| MPP\[25]     | AT34  | CP\_GPIO\[25]        | <p>3.3V, Reset strap<br>2.2K PD</p>                                  |
| MPP\[26]     | AT38  | CP\_GPIO\[26]        | <p>3.3V, Reset strap<br>10K PU</p>                                   |
| MPP\[27]     | AW31  | CP\_GPIO\[27]        | 3.3V                                                                 |
| MPP\[28]     | AY32  | CP\_GPIO\[28]        | 3.3V                                                                 |
| MPP\[29]     | BA33  | CP\_GPIO\[29]        | 3.3V                                                                 |
| MPP\[30]     | AW33  | CP\_GPIO\[30]        | 3.3V                                                                 |
| MPP\[31]     | AP36  | CP\_GPIO\[31]        | 3.3V                                                                 |
| MPP\[32]     | H30   | CP\_GPIO\[32]        | 3.3V                                                                 |
| MPP\[33]     | C39   | CP\_GPIO\[33]        | 3.3V                                                                 |
| MPP\[34]     | C41   | CP\_GPIO\[34]        | 3.3V                                                                 |
| MPP\[35]     | F32   | CP\_I2C1\_SDA        | 3.3V, 2.2K PU                                                        |
| MPP\[36]     | H32   | CP\_I2C1\_SCK        | 3.3V, 2.2K PU                                                        |
| MPP\[37]     | F34   | CP\_I2C0\_SCK        | <p>3.3V, 2.2K PU<br>EEPROM 0x53</p>                                  |
| MPP\[38]     | H34   | CP\_I2C0\_SDA        | <p>3.3V, 2.2K PU<br>EEPROM 0x53</p>                                  |
| MPP\[39]     | F30   | CP\_GPIO\[39]        | 3.3V                                                                 |
| MPP\[40]     | F36   | CP\_RCVR1\_CLK       | 3.3V, 25MHz for SYNC-E connected to J1                               |
| MPP\[41]     | H36   | VHV\_EN              | 3.3V, 1K PD, can enable 1.8V supply for CP\_VHV                      |
| MPP\[42]     | E39   | NC                   |                                                                      |
| MPP\[43]     | D30   | CP\_SD\_CRD\_DT      | 3.3V                                                                 |
| MPP\[44]     | D38   | CP\_GE2\_TXD\[2]     | 1.8V, Reset Strap                                                    |
| MPP\[45]     | A39   | CP\_GE2\_TXD\[3]     | 1.8V, Reset strap                                                    |
| MPP\[46]     | C37   | CP\_GE2\_TXD\[1]     | <p>1.8V, CPU Subsystem Clock<br>CP0_SYS_PLL_SEL3, 10K PD</p>         |
| MPP\[47]     | A37   | CP\_GE2\_TXD\[0]     | 1.8V, Reset strap, 2.2K PD                                           |
| MPP\[48]     | B40   | CP\_GE2\_TXCTL       | 1.8V, Reset strap                                                    |
| MPP\[49]     | B38   | CP\_GE2\_TXCLKOUT    | 1.8V, serial 22ohm resistor                                          |
| MPP\[50]     | C35   | CP\_GE2\_RXCLK       | 1.8V, serial 22ohm resistor                                          |
| MPP\[51]     | D34   | CP\_GE2\_RXD\[0]     | 1.8V                                                                 |
| MPP\[52]     | A35   | CP\_GE2\_RXD\[1]     | 1.8V                                                                 |
| MPP\[53]     | B36   | CP\_GE2\_RXD\[2]     | 1.8V                                                                 |
| MPP\[54]     | D36   | CP\_GE2\_RXD\[3]     | 1.8V                                                                 |
| MPP\[55]     | B34   | CP\_GE2\_RXCTL       | 1.8V                                                                 |
| MPP\[56]     | D32   | CP\_SD\_CLK          | 3.3V                                                                 |
| MPP\[57]     | B32   | CP\_SD\_CMD          | 3.3V                                                                 |
| MPP\[58]     | A33   | CP\_SD\_D\[0]        | 3.3V                                                                 |
| MPP\[59]     | C33   | CP\_SD\_D\[1]        | 3.3V                                                                 |
| MPP\[60]     | A31   | CP\_SD\_D\[2]        | 3.3V                                                                 |
| MPP\[61]     | C31   | CP\_SD\_D\[3]        | 3.3V                                                                 |
| MPP\[62]     | B30   | NC                   |                                                                      |

## SOM Header Details

Following are the SOM Connectors J1, J2, J3 pin mapping –

GND pins are marked with Red&#x20;

The SOM has 3 connectors:

1. J1, J2 – DF40C-80DP-0.4V(51), 80\
   Mating connectors:

* DF40C-80DS-0.4V(51) – 1.5mm mating height
* DF40C(2.0)-80DS-0.4V(51) – 2mm mating height
* DF40C(4.0)-80DS-0.4V(51) – 4mm mating height

2. J3 – DF40C-70DP-0.4V(51), 70\
   Mating connectors:

* DF40C-70DS-0.4V(51) – 1.5mm mating height
* DF40C(2.0)-70DS-0.4V(51) – 2mm mating height

3. Spacers

* Manufacture PN: N0143416A (for 1.5mm stacking height)
* Screw M1.6&#x20;

#### Connector J1

| Notes                                          | Driving IC   | Schematics Pin Name       | Pin Number | Pin Number | Schematics Pin Name      | Driving IC                    | Notes                                                                   |
| ---------------------------------------------- | ------------ | ------------------------- | ---------- | ---------- | ------------------------ | ----------------------------- | ----------------------------------------------------------------------- |
|                                                |              |                           | 2          | 1          | GND (FIXED)              |                               |                                                                         |
|                                                |              |                           | 4          | 3          | MDI\_P0                  | CP0 RGMII through 88E1512 PHY |                                                                         |
| 3.3V                                           | CP\_MPP\[40] | RCVR1\_CLK\_CP0           | 6          | 5          | MDI\_N0                  | CP0 RGMII through 88E1512 PHY |                                                                         |
|                                                |              |                           | 8          | 7          | GND (FIXED)              |                               |                                                                         |
|                                                |              |                           | 10         | 9          | MDI\_P1                  | CP0 RGMII through 88E1512 PHY |                                                                         |
|                                                |              |                           | 12         | 11         | MDI\_N1                  | CP0 RGMII through 88E1512 PHY |                                                                         |
| 3.3V, 2.2K PU                                  | CP\_MPP\[36] | I2C1\_CP0\_SCL            | 14         | 13         | GND (FIXED)              |                               |                                                                         |
| 3.3V                                           | CP\_MPP\[12] | SPI1\_CP0\_CS1\_N         | 16         | 15         | MDI\_P2                  | CP0 RGMII through 88E1512 PHY |                                                                         |
| 3.3V                                           | CP\_MPP\[29] | CP0\_GPIO2                | 18         | 17         | MDI\_N2                  | CP0 RGMII through 88E1512 PHY |                                                                         |
| 3.3V thorough NTB0102GD level shifter, 2.2K PU | CP\_MPP\[2]  | UART1\_CP0\_RX            | 20         | 19         | GND (FIXED)              |                               |                                                                         |
| 3.3V                                           | CP\_MPP\[30] | CP0\_GPIO3                | 22         | 21         | MDI\_P3                  | CP0 RGMII through 88E1512 PHY |                                                                         |
| 3.3V thorough NTB0102GD level shifter, 2.2K PU | CP\_MPP\[3]  | UART1\_CP0\_TX            | 24         | 23         | MDI\_N3                  | CP0 RGMII through 88E1512 PHY |                                                                         |
|                                                |              | GND (FIXED)               | 26         | 25         | GND (FIXED)              |                               |                                                                         |
| 1.8V                                           | CP\_MPP\[5]  | CP0\_GPIO9\_1.8V          | 28         | 27         | PHY0\_RST\_N\_1.8V       |                               | 1.8V, input reset to PHY                                                |
| 3.3V, Reset Strap                              | CP\_MPP\[18] | CP0\_BOOT\_MODE\_SEL0     | 30         | 29         | GBE0\_LED2\_INT\_N\_1.8V | 88E1512                       | 1.8V, serial 510ohm resistor                                            |
| 3.3V, Reset Strap                              | CP\_MPP\[19] | CP0\_BOOT\_MODE\_SEL1     | 32         | 31         | GBE0\_LED1\_1.8V         | 88E1512                       | 1.8V, serial 510ohm resistor                                            |
| 3.3V, Reset Strap                              | CP\_MPP\[21] | CP0\_BOOT\_MODE\_SEL3     | 34         | 33         | GBE0\_LED0\_1.8V         | 88E1512                       | 1.8V, serial 510ohm resistor                                            |
| SD CARD, 3.3V, 2.2K PU                         | CP\_MPP\[43] | SD\_CP0\_CD\_N            | 36         | 35         | SMI\_CP0\_MDIO           | CP\_MPP\[0]                   | <p>1.8V, 2.2K PU,<br>connected to PHY 88E1512 ADD 0x0</p>               |
| 3.3V thorough NTB0102GD level shifter, 2.2K PU | AP\_MPP\[19] | UART\_AP\_RX0             | 38         | 37         | SMI\_CP0\_MDC            | CP\_MPP\[1]                   | <p>1.8V, 2.2K PD (Reset Strap),<br>connected to PHY 88E1512 ADD 0x0</p> |
| 3.3V thorough NTB0102GD level shifter, 2.2K PU | AP\_MPP\[11] | UART\_AP\_TX0             | 40         | 39         | POWER\_OFF\_N            |                               | 1.8V                                                                    |
| <p>Reset IN<br>3.3V, 2.2K PU</p>               |              | SYS\_RESET\_N             | 42         | 41         | GND (FIXED)              |                               |                                                                         |
|                                                |              |                           | 44         | 43         | JTAG\_CP0\_TCK           |                               | JTAG, 3.3V, 10K PD                                                      |
| <p>Reset OUT<br>3.3V, 2.2K PU</p>              |              | CP0\_SYSRST\_OUT\_N       | 46         | 45         | JTAG\_CP0\_TRST\_N       |                               | JTAG, 3.3V, 10K PD                                                      |
|                                                |              |                           | 48         | 47         | JTAG\_CP0\_TDI           |                               | JTAG, 3.3V, 10K PU                                                      |
| JTAG, 3.3V, 10K PU                             |              | JTAG\_CP0\_TMS            | 50         | 49         | JTAG\_CP0\_TDO           |                               | JTAG, 3.3V, 10K PU                                                      |
|                                                |              |                           | 52         | 51         | CP0\_GPIO0               | CP\_MPP\[27]                  | 3.3V                                                                    |
| SD CARD, 3.3V                                  | CP\_MPP\[58] | SD\_CP0\_SDIO\_D0         | 54         | 53         | SD\_CP0\_SDIO\_CMD       | CP\_MPP\[57]                  | SD CARD, 3.3V                                                           |
| SD CARD, 3.3V                                  | CP\_MPP\[61] | SD\_CP0\_SDIO\_D3         | 56         | 55         | SD\_CP0\_SDIO\_CLK       | CP\_MPP\[56]                  | SD CARD, 3.3V                                                           |
|                                                |              | GND (FIXED)               | 58         | 57         | CP0\_\_GPIO1             | CP\_MPP\[28]                  | 3.3V                                                                    |
| SD CARD, 3.3V                                  | CP\_MPP\[59] | SD\_CP0\_SDIO\_D1         | 60         | 59         | GND (FIXED)              |                               |                                                                         |
| SD CARD, 3.3V                                  | CP\_MPP\[60] | SD\_CP0\_SDIO\_D2         | 62         | 61         | I2C1\_CP0\_SDA           | CP\_MPP\[35]                  | 3.3V, 2.2K PU                                                           |
|                                                |              |                           | 64         | 63         |                          |                               |                                                                         |
| <p>3.3V, 2.2K PU,<br>EEPROM 0x53</p>           | CP\_MPP\[38] | I2C0\_CP0\_SDA            | 66         | 65         |                          |                               |                                                                         |
| <p>3.3V, 2.2K PU,<br>EEPROM 0x53</p>           | CP\_MPP\[37] | I2C0\_CP0\_SCL            | 68         | 67         |                          |                               |                                                                         |
| 1.8V                                           | CP\_MPP\[6]  | PTP\_CP0\_PULSE\_1.8V     | 70         | 69         | VIN                      |                               | 12V or 5V                                                               |
| 1.8V                                           | CP\_MPP\[7]  | PTP\_CP0\_CLK\_IN\_1.8V   | 72         | 71         | VIN                      |                               | 12V or 5V                                                               |
| 1.8V                                           | CP\_MPP\[8]  | PTP\_CP0\_PCLK\_OUT\_1.8V | 74         | 73         | VIN                      |                               | 12V or 5V                                                               |
| 1.8V                                           | CP\_MPP\[4]  | CP0\_GPIO8\_1.8V          | 76         | 75         | VIN                      |                               | 12V or 5V                                                               |
|                                                |              | GND (FIXED)               | 78         | 77         | VIN                      |                               | 12V or 5V                                                               |
|                                                |              |                           | 80         | 79         | VIN                      |                               | 12V or 5V                                                               |

#### Connector J2

| Notes                        | Driving IC   | Schematics Pin Name | Pin Number | Pin Number | Schematics Pin Name | Driving IC   | Notes                                               |
| ---------------------------- | ------------ | ------------------- | ---------- | ---------- | ------------------- | ------------ | --------------------------------------------------- |
| No on-board serial capacitor |              | B2B\_SRD2\_TX\_P    | 2          | 1          | GND (FIXED)         |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD2\_TX\_N    | 4          | 3          | USB2\_CP0\_DP1      |              |                                                     |
|                              |              | GND (FIXED)         | 6          | 5          | USB2\_CP0\_DM1      |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD2\_RX\_P    | 8          | 7          | GND (FIXED)         |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD2\_RX\_N    | 10         | 9          |                     |              |                                                     |
|                              |              | GND (FIXED)         | 12         | 11         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD4\_RX\_P    | 14         | 13         | GND (FIXED)         |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD4\_RX\_N    | 16         | 15         | USB2\_CP0\_DP0      |              |                                                     |
|                              |              | GND (FIXED)         | 18         | 17         | USB2\_CP0\_DM0      |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD4\_TX\_P    | 20         | 19         | CP0\_GPIO4          | CP\_MPP\[31] | 3.3V                                                |
| No on-board serial capacitor |              | B2B\_SRD4\_TX\_N    | 22         | 21         |                     |              |                                                     |
|                              |              | GND (FIXED)         | 24         | 23         | 3.3V\_RTC\_B2B      |              | 3.3V battery voltage                                |
| No on-board serial capacitor |              | B2B\_SRD1\_TX\_P    | 26         | 25         | PCIE\_REFCLK\_N1    |              | 100MHz HCSL clock out, no serial capacitors         |
| No on-board serial capacitor |              | B2B\_SRD1\_TX\_N    | 28         | 27         | PCIE\_REFCLK\_P1    |              | 100MHz HCSL clock out, no serial capacitors         |
|                              |              | GND (FIXED)         | 30         | 29         | GND (FIXED)         |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD1\_RX\_P    | 32         | 31         | PCIE\_REFCLK\_P0    |              | 100MHz HCSL clock out, no serial capacitors         |
| No on-board serial capacitor |              | B2B\_SRD1\_RX\_N    | 34         | 33         | PCIE\_REFCLK\_N0    |              | 100MHz HCSL clock out, no serial capacitors         |
|                              |              | GND (FIXED)         | 36         | 35         | GND (FIXED)         |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD5\_RX\_P    | 38         | 37         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD5\_RX\_N    | 40         | 39         |                     |              |                                                     |
|                              |              | GND (FIXED)         | 42         | 41         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD5\_TX\_P    | 44         | 43         | CP0\_SYS\_PLL\_SEL2 | CP\_MPP\[17] | 3.3V, PD 50k, Boot strap                            |
| No on-board serial capacitor |              | B2B\_SRD5\_TX\_N    | 46         | 45         | CP0\_GPIO5          | CP\_MPP\[32] | 3.3V                                                |
|                              |              | GND (FIXED)         | 48         | 47         | CP0\_GPIO7          | CP\_MPP\[34] | 3.3V                                                |
| No on-board serial capacitor |              | B2B\_SRD3\_TX\_P    | 50         | 49         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD3\_TX\_N    | 52         | 51         |                     |              |                                                     |
|                              |              | GND (FIXED)         | 54         | 53         | GND (FIXED)         |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD3\_RX\_P    | 56         | 55         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD3\_RX\_N    | 58         | 57         | CP0\_GPIO6          | CP\_MPP\[33] | 3.3V                                                |
|                              |              | GND (FIXED)         | 60         | 59         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD0\_RX\_P    | 62         | 61         |                     |              |                                                     |
| No on-board serial capacitor |              | B2B\_SRD0\_RX\_N    | 64         | 63         | 1.8V\_VHV           |              | NC                                                  |
|                              |              | GND (FIXED)         | 66         | 65         | 1.8V\_OUT           |              | Option to provide 1.8V out for low power misc logic |
| No on-board serial capacitor |              | B2B\_SRD0\_TX\_P    | 68         | 67         | 1.8V\_OUT           |              | Option to provide 1.8V out for low power misc logic |
| No on-board serial capacitor |              | B2B\_SRD0\_TX\_N    | 70         | 69         |                     |              |                                                     |
|                              |              | GND (FIXED)         | 72         | 71         | PHY\_CLK125\_OUT    |              |                                                     |
|                              |              |                     | 74         | 73         | CP0\_MPP39          | CP\_MPP\[39] | 3.3V                                                |
|                              |              |                     | 76         | 75         |                     |              |                                                     |
| 3.3V                         | CP\_MPP\[13] | SPI1\_CP0\_MISO\_M  | 78         | 77         | SPI1\_CP0\_MOSI\_M  | CP\_MPP\[15] | 3.3V, Boot Strap                                    |
| 3.3V                         | CP\_MPP\[14] | SPI1\_CP0\_CS0\_N   | 80         | 79         | SPI1\_CP0\_CLK\_M   | CP\_MPP\[16] | 3.3V, Boot Strap                                    |

#### Connector J3

| Notes                                                  | Driving IC    | Schematics Pin Name   | Pin Number | Pin Number | Schematics Pin Name   | Driving IC | Notes                                      |
| ------------------------------------------------------ | ------------- | --------------------- | ---------- | ---------- | --------------------- | ---------- | ------------------------------------------ |
|                                                        |               | GND (FIXED)           | 2          | 1          | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_N2 | 4          | 3          | AP\_MCI0\_TX\_CP1\_P0 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_P2 | 6          | 5          | AP\_MCI0\_TX\_CP1\_N0 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 8          | 7          | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_N1 | 10         | 9          | REFCLK\_MCI0\_CP1\_N  |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_P1 | 12         | 11         | REFCLK\_MCI0\_CP1\_P  |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 14         | 13         | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_N0 | 16         | 15         | AP\_MCI0\_TX\_CP1\_P1 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_P0 | 18         | 17         | AP\_MCI0\_TX\_CP1\_N1 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 20         | 19         | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_P3 | 22         | 21         | AP\_MCI0\_TX\_CP1\_P2 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI0\_RX\_CP1\_N3 | 24         | 23         | AP\_MCI0\_TX\_CP1\_N2 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 26         | 25         | GND (FIXED)           |            |                                            |
| Drive high for muxing SoM SPI FLash to J3-SPI\_B2B\_\* | SPI Mux       | SEL\_SPI\_MUX         | 28         | 27         | AP\_MCI0\_TX\_CP1\_P3 |            | No on-board serial capacitor               |
| controlled by SEL\_SPI\_MUX                            | SoM SPI Flash | SPI\_B2B\_CS0\_N      | 30         | 29         | AP\_MCI0\_TX\_CP1\_N3 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | GND (FIXED)           | 32         | 31         | GND (FIXED)           |            |                                            |
| controlled by SEL\_SPI\_MUX                            | SoM SPI Flash | SPI\_B2B\_CLK         | 34         | 33         |                       |            |                                            |
| controlled by SEL\_SPI\_MUX                            | SoM SPI Flash | SPI\_B2B\_MOSI        | 36         | 35         |                       |            | Connected to on board STM32 for management |
| controlled by SEL\_SPI\_MUX                            | SoM SPI Flash | SPI\_B2B\_MISO        | 38         | 37         |                       |            | 3.3V, connected to EFUSE                   |
|                                                        |               | GND (FIXED)           | 40         | 39         | GND (FIXED)           |            |                                            |
| Not connected since v1.1                               |               | USB\_MCU\_DP          | 42         | 41         | AP\_MCI1\_TX\_CP2\_P3 |            | No on-board serial capacitor               |
| Not connected since v1.1                               |               | USB\_MCU\_DM          | 44         | 43         | AP\_MCI1\_TX\_CP2\_N3 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 46         | 45         | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_P0 | 48         | 47         | AP\_MCI1\_TX\_CP2\_N0 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_N0 | 50         | 49         | AP\_MCI1\_TX\_CP2\_P0 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 52         | 51         | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_P1 | 54         | 53         | REFCLK\_MCI1\_CP2\_N  |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_N1 | 56         | 55         | REFCLK\_MCI1\_CP2\_P  |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 58         | 57         | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_P3 | 60         | 59         | AP\_MCI1\_TX\_CP2\_P1 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_N3 | 62         | 61         | AP\_MCI1\_TX\_CP2\_N1 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 64         | 63         | GND (FIXED)           |            |                                            |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_N2 | 66         | 65         | AP\_MCI1\_TX\_CP2\_N2 |            | No on-board serial capacitor               |
| No on-board serial capacitor                           |               | AP\_MCI1\_RX\_CP2\_P2 | 68         | 67         | AP\_MCI1\_TX\_CP2\_P2 |            | No on-board serial capacitor               |
|                                                        |               | GND (FIXED)           | 70         | 69         | GND (FIXED)           |            |                                            |

## Heatsink

SolidRun provides few types of heatsinks:

1. Cool-plate: flattens the surface of the SOM, making it easier for integration  in any enclosure design
2. Evaluation heatsink: add-on for the cool-plate, with short ribs, enabling to mount a 40mmX40mm fan. This heatsink is to be used in open frame systems, to enable developers to work with the CN9130 SOM during bring-up and software development

## Precision Time Protocol (PTP)

**Note: Information on PTP is based on SoM schematics and SoC datasheet analysis, but actual functionality has not been tested. For authoritative information, consultation of Marvell documentation and Errata (available under NDA) is strongly recommended.**

CN9130 SoC has hardware support for PTP\* and Synchronous Ethernet\*.

There are three related electrical signals:

1. PTP\_PULSE (IN/OUT): Pulse per second.\
   Muxable to J1-57 (MPP\[28])
2. PTP\_CLK (IN/OUT) @ J1-18 (MPP\[29]), J2-73 (MPP): Discrete trigger using Generate function.\
   Muxable to J1-18 (MPP\[29]), J2-73 (MPP\[39])
3. PTP\_PCLK\_OUT (OUT): Recovered clock output.\
   Muxable to J1-22 (MPP\[30])

PTP\_PULSE and PTP\_CLK can each synchronise between master and slave, the former generating periodic pulses while the latter depends on external events such as Update and Generate.

The PTP reference clock is generated internally.

PCLK\_OUT provides the recovered clock, generated from a serdes lane according to its configuration registers.

### Enable PTP on Clearfog Base / Pro

**Note: Information on PTP is based on SoM schematics and SoC datasheet analysis, but actual functionality has not been tested. For authoritative information, consult Marvell documentation and Errata (available under NDA).**

Clearfog Base / Pro support the mentioned PTP signals on the mikroBus connector:

* PTP\_PULSE: U14-2 / U3-2 “RST”
* PTP\_CLK: U14-9 / U3-9 “PWM”
* PTP\_PCLK\_OUT: U14-10 / U3-10 “INT”

By default these are acting as GPIOs, apply the device-tree changes below to select PTP:

```
diff --git a/arch/arm64/boot/dts/marvell/cn9130-cf-base.dts b/arch/arm64/boot/dts/marvell/cn9130-cf-base.dts
index 788a5c302b17..d93ad507ac24 100644
--- a/arch/arm64/boot/dts/marvell/cn9130-cf-base.dts
+++ b/arch/arm64/boot/dts/marvell/cn9130-cf-base.dts
@@ -136,7 +136,7 @@ led@1 {
 };
 
 &cp0_pinctrl {
-	pinctrl-0 = <&sim_select_pins>;
+	pinctrl-0 = <&ptp_pins>, <&sim_select_pins>;
 	pintrl-names = "default";
 
 	rear_button_pins: cp0-rear-button-pins {
diff --git a/arch/arm64/boot/dts/marvell/cn9130-cf.dtsi b/arch/arm64/boot/dts/marvell/cn9130-cf.dtsi
index ad0ab34b6602..240e298e897a 100644
--- a/arch/arm64/boot/dts/marvell/cn9130-cf.dtsi
+++ b/arch/arm64/boot/dts/marvell/cn9130-cf.dtsi
@@ -123,6 +123,8 @@ &cp0_pcie2 {
 };
 
 &cp0_pinctrl {
+	pinctrl-0 = <&ptp_pins>;
+
 	cp0_i2c1_pins: cp0-i2c1-pins {
 		marvell,pins = "mpp35", "mpp36";
 		marvell,function = "i2c1";
@@ -134,6 +136,11 @@ cp0_mmc0_pins: cp0-mmc0-pins {
 		marvell,function = "sdio";
 	};
 
+	ptp_pins: cp0-ptp-pins {
+		marvell,pins = "mpp28", "mpp30", "mpp39";
+		marvell,function = "ptp";
+	};
+
 	mikro_spi_pins: cp0-spi1-cs1-pins {
 		marvell,pins = "mpp12";
 		marvell,function = "spi1";

```

PTP is supported by the CN9130 Linux Etherent Controller Driver “MVPP2”, ensure to enable it’s kernel config option `CONFIG_MVPP2_PTP`: [https://github.com/torvalds/linux/blob/master/drivers/net/ethernet/marvell/Kconfig#L97](https://github.com/torvalds/linux/blob/master/drivers/net/ethernet/marvell/Kconfig#l97)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                                           | File                                                                                                                                                           | Modified                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-12a73a8b-9f03-4869-aff2-4abaa6bd5374">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/cn9130_som_rev1.1-simplified+schematics.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>  | PDF File [cn9130\_som\_rev1.1-simplified schematics.pdf](../../../wiki/download/attachments/197493875/cn9130_som_rev1.1-simplified%20schematics.pdf)           | Nov 07, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/)      |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-103595da-c1a5-4726-9a78-a4b51aa012e0">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/CN9130-som-heatsink-files.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                | ZIP Archive [CN9130-som-heatsink-files.zip](../../../wiki/download/attachments/197493875/CN9130-som-heatsink-files.zip)                                        | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/)      |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-5ffa3854-8d74-4418-b7e1-2cdc454645c3">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/B2B+pinout+A388+and+CN9130.xlsx">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>              | Microsoft Excel Spreadsheet [B2B pinout A388 and CN9130.xlsx](../../../wiki/download/attachments/197493875/B2B%20pinout%20A388%20and%20CN9130.xlsx)            | Dec 26, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/)      |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-3010ed0e-86d6-4838-86eb-3092bfa7688d">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/CN9130-SOM-Mechanical-Files.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>              | ZIP Archive [CN9130-SOM-Mechanical-Files.zip](../../../wiki/download/attachments/197493875/CN9130-SOM-Mechanical-Files.zip) Change: CPU height 2.2mm --> 1.8mm | Dec 29, 2021 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/)      |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-632e333d-e54c-4737-8548-4a585f879021">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/CN9130_SOM_REV1.1_STEP.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                   | ZIP Archive [CN9130\_SOM\_REV1.1\_STEP.zip](../../../wiki/download/attachments/197493875/CN9130_SOM_REV1.1_STEP.zip)                                           | Mar 15, 2022 by [alon rotman](../../../wiki/people/5f67bce7460930007791b95f/)                      |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-ccb6686b-4616-421e-9456-68b321398f9d">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/Reliability+prediction+for+CN9130+SOM+V1.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | PDF File [Reliability prediction for CN9130 SOM V1.pdf](../../../wiki/download/attachments/197493875/Reliability%20prediction%20for%20CN9130%20SOM%20V1.pdf)   | Apr 14, 2022 by [SolidRun](../../../wiki/people/557058:12be2ae4-3a6e-40cc-a677-bdfc4c987d1f/)      |
| <p>Labels<br><br>- No labels<br>- <a href="cn9130-som-hardware-user-manual.md#section-c63f7da5-25cc-4e4a-b1f3-67024fd5a9b1">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/197493875/CN9130_SOM_REV1.3_3D.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>                     | ZIP Archive [CN9130\_SOM\_REV1.3\_3D.zip](../../../wiki/download/attachments/197493875/CN9130_SOM_REV1.3_3D.zip)                                               | Oct 29, 2023 by [Rabeeh Khoury](../../../wiki/people/557058:99a92153-3f5e-430e-b8cf-907fde28b14e/) |

[Download All](../../../wiki/download/all_attachments)

[Buy a Sample Now](https://shop.solid-run.com/product-category/networking-soms-coms/cn9130-som/?_ga=2.268861170.2016484779.1641802897-2012112798.1622706355)
