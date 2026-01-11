# CN9132 COM on HoneyComb LX2

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 04 Nov 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Introduction](#introduction)<br>  - [Feature/pinout Difference:](#feature-pinout-difference)<br>- [CEx7 CN9132 on HoneyComb HW Interfaces](#cex7-cn9132-on-honeycomb-hw-interfaces)<br>- [Pinout Comparison](#pinout-comparison)<br>- [List Of Supported OS](#list-of-supported-os) |     |     |

<a id="introduction"></a>

## Introduction

Both CEx7 LX2160 and CEx7 CN9132 are designed as COM Expresses Type 7 standard, therefore their carriers such as HoneyComb and CN9132 EVAL, can support either of the COMs. The COM Express type 7 standard is not strict and allows a certain amount of flexibility, therefore, even though both CEx7 LX2160 and CEx7 CN9132 are COM Expresses Type 7, the features and pinout are slightly different. Below, is a detailed explanation on the difference and the usage of CEx7 CN9132 on the HoneyComb CEx7 LX2160 carrier

<a id="feature-pinout-difference"></a>

#### Feature/pinout Difference:

| **Interface** | **Interface** | **COM Express Min/Max Standard** | **LX2160** | **CN9132** |
| --- | --- | --- | --- | --- |
| ETH | 1GbE | 1/1 | GE0\_MDI\[0:3\] | GE0\_MDI\[0:3\] |
|     | 10G\_KR\[3:0\] | 0/4 | 10G\_KR\[3:0\] – 10/25GbE per lane  <br>or  <br>40/100GbE per port | 10G\_KR\[2:0\] – 10GbE  <br>10G\_KR\[3\] – NC |
| PCIe | PCIe\[3:0\] | 4/4 | PCIe Gen3 X4 | PCIe Gen3 X4 |
|     | PCIe\[5:4\] | 2/2 | PCIe Gen3 X2 | PCIe Gen3 X2 |
|     | PCIe\[7:6\] | 0/2 | NC  | NC  |
|     | PCIe\[15:8\] | 0/8 | PCIE\[11:8\] – PCIE X4  <br>PCIE\[15:12\] – PCIE X4  <br>or  <br>PCIE\[15:8\] – PCIE X8 | PCIE\[8\] – PCIE X1  <br>PCIE\[12\] – PCIE X1 |
|     | PCIe\[31:16\] | 0/16 | PCIE\[17:16\] – PCIE X2  <br>or  <br>PCIE\[19:16\] – PCIE X4 | PCIE\[16\] – PCIE X1  <br>PCIE\[20\] – PCIE X1  <br>PCIE\[24\] – PCIE X1  <br>PCIE\[28\] – PCIE X1 |
| SATA | SATA\[1:0\] | 0/2 | SATA\[1:0\] | SATA\[1:0\] |
| USB | USB 2.0 \[3:0\] | 4/4 | USB 2.0 \[3:0\] | USB 2.0 \[3:0\] |
|     | USB 3.0\[3:0\] | 0/4 | USB 3.0 \[3:0\] | USB 3.0 \[3\] |
| Peripherals | SMB CLK/DAT | 1/1 | V   | V   |
|     | I2C CLK/DAT | 1/1 | V   | V   |
|     | SPI | 1/1 | Secondary SPI on Carrier | Secondary SPI on Carrier |
|     | NCSI | 0/1 | NC  | NC  |
|     | SER\[1:0\] TX/RX | 0/2 | V   | V   |
|     | GPI\[3:0\] / GPO\[3:0\] | 8/8 | SDIO\[3:0\] | SDIO\[3:0\] |
|     | RST/PWR\_OK |     | V   | V   |
|     | MDC/MDIO\[1:0\] | 0/2 | V   | V   |
|     | Fan Control | 0/1 | PWM/TACHO | PWM/TACHO |
|     | RTC | 0/1 | V   | V   |
| Power | VCC\_5V\_SBY | 4/4 | NC  | NC  |
|     | 12V | 24/24 | V   | V   |
| PTP/SYNC-E | Pin C40 / SDP0 | 0/1 | PULSE\_OUT1 | CP0\_PULSE |
|     | Pin A49 / RSVD | 0/1 | TRIG\_IN1 | RSVD |
|     | Pin D83 / RSVD | 0/1 | ALARM\_OUT1 | CP2\_PULSE |
|     | Pin D40/ SDP1 | 0/1 | PULSE\_OUT2 | CP1\_PULSE |
|     | Pin C17/ SDP3 | 0/1 | TRIG\_IN2 | CP1\_CLK\_IN |
|     | Pin D64 / RSVD | 0/1 | ALARM\_OUT2 | CP1\_CLK\_OUT |
|     | Pin C17/ SDP2 | 0/1 | CLK\_IN | CP0\_CLK\_IN |
|     | Pin D77 / RSVD | 0/1 | CLK\_OUT | CP0\_CLK\_OUT |
|     | Pin D97 / RSVD | 0/1 | RCLK0 | CP2\_CLK\_IN |
|     | Pin D63 / RSVD | 0/1 | RCLK1 | CP2\_CLK\_OUT |

<a id="cex7-cn9132-on-honeycomb-hw-interfaces"></a>

## CEx7 CN9132 on HoneyComb HW Interfaces

Please see below the features overview of the connector side of the HoneyComb LX2.

![](./attachments/image-20211226-125453.png)

<a id="pinout-comparison"></a>

## Pinout Comparison

For Pinout comparison, please refer to the [Pinout Planner Tool Guide](https://solidrun.atlassian.net/wiki/spaces/developer/pages/201392150) .  

<a id="list-of-supported-os"></a>

## List Of Supported OS

| **OS** |     |
| --- | --- |
| ![](./attachments/image-20211024-150854.png) | [https://github.com/SolidRun/Documentation/tree/bsp/cn913x](https://github.com/SolidRun/Documentation/tree/bsp/cn913x) |
| Debian Image  <br>Builder | [https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79](https://github.com/SolidRun/debian-builder/tree/7f1357cc6e262f19f1031e76b5c98870faeb7b79) |
| ![](./attachments/image-20220403-092027.png) | [https://github.com/SolidRun/cn913x\_build](https://github.com/SolidRun/cn913x_build) |