# i.MX6 SOM Hardware User Manual

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Revision** | **Notes**                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| 18 Jun 2014       | Rabeeh Khoury                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1.0          | Initial release                                                                                       |
| 24 Jul 2017       | Rabeeh Khoury                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1.1          | Covers SOM rev 1.5 Documentation of booting from GPIOs                                                |
| Nov 8, 2023       | Shahar Fridman                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1.2          | Add power consumption table                                                                           |
| 12 Nov 2024       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1.3          | Updated pin descriptions to include notes indicating where pins are unavailable on SOM version V1.9+. |
| Table of Contents | <p>- <a href="imx6-som-hardware-user-manual.md#revision-and-notes">Revision and Notes</a><br>- <a href="imx6-som-hardware-user-manual.md#introduction">Introduction</a><br>- <a href="imx6-som-hardware-user-manual.md#overview">Overview</a><br>- <a href="imx6-som-hardware-user-manual.md#highlighted-features">Highlighted Features</a><br>- <a href="imx6-som-hardware-user-manual.md#supporting-products">Supporting Products</a><br>- <a href="imx6-som-hardware-user-manual.md#summary-of-features">Summary of Features</a><br>- <a href="imx6-som-hardware-user-manual.md#block-diagram">Block Diagram</a><br>- <a href="imx6-som-hardware-user-manual.md#core-system-components">Core System Components</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-soc-family">i.MX6 SOC Family</a><br>- <a href="imx6-som-hardware-user-manual.md#10-100-1000-mbps-ethernet-phy">10/100/1000 MBPS Ethernet PHY</a><br>- <a href="imx6-som-hardware-user-manual.md#bcm-4330-based-som-rev-13-wireless-lan-80211-b-g-n-bluetooth-40-sip">BCM 4330 Based (SOM Rev 1.3) – Wireless LAN 802.11 B/G/N &#x26; Bluetooth 4.0 SiP</a><br>- <a href="imx6-som-hardware-user-manual.md#ti-wilink8-basedsom-rev-15-wireless-lan-80211-b-g-n-bluetooth-41-sip">TI WiLink8 Based(SOM Rev 1.5) – Wireless LAN 802.11 B/G/N &#x26; Bluetooth 4.1 SiP</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-som-interfaces">i.MX6 SOM Interfaces</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-som-external-interfaces-brief">i.MX6 SOM- External Interfaces Brief</a><br>- <a href="imx6-som-hardware-user-manual.md#sr-som-mx6-on-board-functions">SR-SOM-MX6 ON Board Functions</a><br>- <a href="imx6-som-hardware-user-manual.md#10-100-1000-mbps-phy">10/100/1000 Mbps PHY</a><br>- <a href="imx6-som-hardware-user-manual.md#80211-b-g-n-and-bluetooth-sip">802.11 b/g/n and Bluetooth SiP</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-som-external-interfaces-detailed-description">i.MX6 SOM External Interfaces Detailed Description</a><br>- <a href="imx6-som-hardware-user-manual.md#j5002-board-to-board-header-pin-description">J5002 Board to Board Header Pin Description</a><br>- <a href="imx6-som-hardware-user-manual.md#j8004-board-to-board-header-pin-description">J8004 Board to Board Header Pin Description</a><br>- <a href="imx6-som-hardware-user-manual.md#j5001-board-to-board-header-pin-description">J5001 Board to Board Header Pin Description</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-som-power-up-sequence">i.MX6 SOM Power Up Sequence</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-som-gpio-internal-boot-source-configuration">i.MX6 SOM GPIO (Internal) Boot Source Configuration</a><br>- <a href="imx6-som-hardware-user-manual.md#boot-from-sdhc2-external-sd-card">Boot from SDHC2 External SD Card</a><br>- <a href="imx6-som-hardware-user-manual.md#boot-from-sdhc3-emmc">Boot from SDHC3 eMMC</a><br>- <a href="imx6-som-hardware-user-manual.md#boot-from-sata">Boot from SATA</a><br>- <a href="imx6-som-hardware-user-manual.md#rev-13-debugging-capability">Rev 1.3 Debugging Capability</a><br>- <a href="imx6-som-hardware-user-manual.md#rev-15-debugging-capability">Rev 1.5 Debugging Capability</a><br>- <a href="imx6-som-hardware-user-manual.md#differences-between-som-versions">Differences Between SOM Versions</a><br>- <a href="imx6-som-hardware-user-manual.md#changes-between-som-rev-10-to-rev-12">Changes Between SOM Rev 1.0 to Rev 1.2</a><br>- <a href="imx6-som-hardware-user-manual.md#changes-between-som-rev-12-to-rev-13">Changes Between SOM Rev 1.2 to Rev 1.3</a><br>- <a href="imx6-som-hardware-user-manual.md#changes-between-som-rev-13-to-rev-15">Changes Between SOM Rev 1.3 to Rev 1.5</a><br>- <a href="imx6-som-hardware-user-manual.md#typical-power-consumption">Typical Power Consumption</a><br>- <a href="imx6-som-hardware-user-manual.md#imx6-som-power-consumption">imx6 SOM Power Consumption</a><br>- <a href="imx6-som-hardware-user-manual.md#maximum-rating">Maximum Rating</a><br>- <a href="imx6-som-hardware-user-manual.md#mechanical-description">Mechanical Description</a><br>- <a href="imx6-som-hardware-user-manual.md#documentation">Documentation</a><br>- <a href="imx6-som-hardware-user-manual.md#related-articles">Related Articles</a></p> |              |                                                                                                       |

{% hint style="info" %}
**Disclaimer** No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.
{% endhint %}


## Introduction

This User Manual relates to the SolidRun [SOM-i.MX6 series](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx6-family/imx6-som/#overview), which includes –

Single core ARM A9 (1 GHz) of the i.MX6 SoC: SOM-i1 (C1000S-D512-FE)

Dual lite core ARM A9 (1GHz) of the i.MX6 SoC: SOM-i2 (C1000DL-D1024-FE)

Dual core ARM A9 (1GHz) of the i.MX6 SoC: SOM-i2eX (C1000DM-D1024-GE-W)

Quad core ARM A9 (1GHz) of the i.MX6 SoC: SOM-i4 (C1000QM-D2048-GE-W)

#### Overview

The SolidRun SR-SOM-MX6 is a high performance micro system on module (SOM) based on the highly integrated NXP/Freescale i.MX6 family of products.

#### Highlighted Features

* Ultra small footprint SOM (47x30mm) including three board-to-board connectors. Mating height is carrier board dependent.
* Freescale i.MX6 SoC (supports solo, dual lite, dual and quad versions)
  * Up to quad Cortex A9 and up to 1.2GHz
  * Integrated multi format decoders and encoders, de-interlacing and color conversion functions
  * Integrated OpenVG, OpenGL ES 2.0 and OpenCL 1.1 EP GPU
  * DDR3 memories in x32 or x64 configurations (either 2 x16 or 4 x16 on a single chip select)
* Power management devices
* Gigabit Ethernet phy based on Qualcomm Atheros 8035 (footprint compatible with 8030 fast Ethernet phy)
* Rev 1.3 – Broadcom BCM4330 based WiFi 11n and Bluetooth 4.0 (2.4GHz)
* Rev 1.5 – TI Wilink8 based WiFi 11n (up to dual MIMO 2.4GHz/5GHz) and Bluetooth 4.1 / BLE

#### Supporting Products

The following products are provided from SolidRun both as production level platforms and as reference examples on how to incorporate the SOM in different levels of integration:

* HummingBoard (Base/Pro/Gate/Edge) – A board computer that incorporates the SOM retains the same Linux distributions while adding extra hardware functionalities and access to the hardware.
* CuBox-i – A minicomputer that is only 2″x2″x2″ in size that runs Linux with different distribution variants, use cases.

#### Summary of Features

Following is the features summary of the SOM. Notice that some of the features are pinout multiplexed (please refer to the pin muxing below and the Freescale i.MX6 data sheets):

* Freescale i.MX6 series SoC (Solo/Dual Lite/Dual/Quad ARM® Cortex™ A9 Processor, up to 1.2 GHz)
* Up to 2GByte
* HDMI 1.4 interface
* LVDS display interface
* MIPI DSI
* MIPI CSI-2
* Parallel camera interface
* Parallel display interface
* 10/100/1000 Mbps Ethernet PHY
* SOM rev 1.3 – Wireless LAN 802.11 b/g/n and Bluetooth 4.0
* SOM rev 1.5 – SISO or dual MIMO 2.4 or 5GHz (depends on part) 802.11 b/g/n with Bluetooth 4.1
* 1 x USB 2.0 host and 1 x USB 2.0 OTG
* 3 x SD / MMC interfaces
* Serial interfaces
* CAN Bus
* Required power supplies –
  * One 3.3V to 5.0V interface (called in the doc VIN\_5V0)
  * One 3.3V (called in the doc NVCC\_EIM0)
  * One SNVS and VDDHIGH\_IN power supply (called in the doc VSNVS\_3V0) Notice how NVCC\_EIM0 and VSNVS\_3V0 can be combined into one in the HummingBoard design.
  * Optionally two SD interface power supplies (NVCC\_SD2, NVCC\_SD3) can be externally set to either 3.3v or 1.8v for UHS-1 support.

## Block Diagram

![](<../../../.gitbook/assets/i.MX6 SOM rev 1.5 block diagram 2021.jpg>)

## Core System Components

#### i.MX6 SOC Family

The Freescale i.MX6 SoC is an implementation of the ARM CortexTM-A9 core, which operates at frequencies up to 1.2 GHz. The i.MX6 provides a variety of interfaces and supports the following main features:

* Single, dual and quad processor ARM Cortex™-A9 SMP configuration. Each processor includes:
  * 32 Kbyte L1 Instruction Cache
  * 32 Kbyte L1 Data Cache
  * Private Timer and Watchdog
  * Cortex-A9 NEON MPE (Media Processing Engine) Co-processor:
  * SIMD Media Processing Architecture
    * NEON register file with 32×64-bit general-purpose registers
    * NEON Integer execute pipeline (ALU, Shift, MAC)
    * NEON dual, single-precision floating point execute pipeline (FADD, FMUL)
    * NEON load/store and permute pipeline
  * Unified L2 cache
  * General Interrupt Controller (GIC) with 128 interrupt support
  * Global Timer
  * Snoop Control Unit (SCU)
  * Integrated Power Management unit:
    * Die temperature sensor with alarms
    * Dynamic voltage and frequency scaling for low power modes
    * Flexible clock gating control scheme
  * Graphics, Multimedia & hardware acceleration engines:
    * Video Processing Unit (VPU) – A DSP with hardware acceleration engines for video decoding and encoding
    * Image Processing Unit (IPUv3) – A hardware engine for processing images, frames, de-interlacing and various other tasks
    * 3D Graphics Processing Engine (3D GPU) – OpenGL ES 2.0 and OpenCL 1.1 EP GPU engine scalable from one shader up to 4
    * 2D Graphics Processing Engine (2D GPU) – For BitBlt function etc…
    * 2D Graphics Processing Engine (OpenVG) – OpenVG compliant GPU
    * Asynchronous sample rate converters (ASRC)
  * Security:
    * ARM TrustZone including the TZ architecture (interrupt and memory separation)
    * CAAM module – cipher acceleration and assurance module including a true pseudo random number generator (NIST certified)
    * Secure boot (HAB) and central security unit controlled via OTP fuses
  * I/O:
    * High Speed USB 2.0 OTG (Up to 480 Mbps) with integrated HS USB Phy
    * High Speed USB 2.0 HOST (Up to 480Mbps) with integrated USB phy
    * Single lane PCI-Express 2.0 (includes clock generation)
    * Misc. SD and MMC interface with 3.3v / 1.8v voltage level support (for UHS-1 speeds)
  * Misc. serial interfaces (SPI, NOR, I2S, I2C, CAN etc…)

{% hint style="info" %}
Please refer to Freescale i.MX6 datasheets with regards to differences between the various devices, number of processors, L2 cache size, GPU supported (i.e. gc880 vs gc2000), etc…
{% endhint %}


#### 10/100/1000 MBPS Ethernet PHY

The Ethernet PHY is based on the Qualcomm / Atheros AR8035 PHY and incorporates the following features:

* 10BASE-Te/100BASE-TX/1000BASE-T IEEE 802.3 compliant
* 1000BASE-T PCS and auto-negotiation with next page support
* IEEE 802.3az EEE
* Green ETHOS power saving modes with internal automatic DSP power-saving scheme
* SmartEEE
* Wake on LAN
* Automatic MDI/MDIX crossover and polarity correction
* IEEE 802.3u compliant auto negotiation
* Cable Diagnostic Test (CDT)

The PHY is connected via the i.MX6 RGMII interface.

#### BCM 4330 Based (SOM Rev 1.3) – Wireless LAN 802.11 B/G/N & Bluetooth 4.0 SiP

The system in package (SiP) is based on the AzureWave AW-NH660 module and incorporates the following features:

* BCM4330 WiFi / BT based
* WiFi / BT co-existence support
* WiFi :
  * Integrated CPU with on-chip memory for complete WLAN subsystem minimizing the need to wake up the application processor
  * SDIO based interface (connected via the i.MX6 SD1 interface)
  * Single band 2.4 GHz 802.11 b/g/n
  * Supports IEEE 802.11d, e, j, I, j, r, k, w
  * WEP, WPA/WPA2, AES, TKIP, CKIP (SW) based security
  * WMM/WMM-PS/WMM-SA
  * Proprietary protocols – CCXv2/CCXv3/CCXv4/CCXv5, WFAEC
* Bluetooth:
  * Fully supports Bluetooth 4.0 + EDR (AFH, QoS, eSCO, fast connect, SSP, SSR, EPR, EIR, LST)
  * High speed UART (max 4Mbps) and PCM for Bluetooth support (connected via\
    i.MX6 UART4 interface and i.MX6 AUD3 audio PCM interface)
  * HS packet types, class 1 or class 2 transmitter type operation

#### TI WiLink8 Based(SOM Rev 1.5) – Wireless LAN 802.11 B/G/N & Bluetooth 4.1 SiP

The SiP (System in package) incorporates the following features –

* TI Wilink 8 WiFi / BT based
* WiFi / BT co-existence support
* WiFi :
  * Integrated RF front end, power amplified, DC-DC, crystal, switches, filters and\
    power management
  * SDIO based interface (connected via the i.MX6 SD1 interface)
  * 2.4 GHz or 5 GHz (depending on model) 802.11 a/b/g/n
  * SISO or MIMO (two antennas)
  * 20 and 40 MHz channels on 2.4/5 GHz bands
  * Wi-Fi direct multi-role multi-channel
  * Up to 10 clients supported in AP role
* Bluetooth:
  * Fully supports Bluetooth 4.1 + EDR including Bluetooth low energy
  * High speed UART (max 4Mbps) and PCM for Bluetooth support (connected via\
    i.MX6 UART4 interface

## i.MX6 SOM Interfaces

#### i.MX6 SOM- External Interfaces Brief

The SOM incorporates three Hirose DF40 board-to-board headers. The selection of the Hirose DF40 is due to the following criteria:

* Miniature (0.4m pitch)
* Highly reliable manufacturer
* Availability (worldwide distribution channels)
* Excellent signal integrity (supports 6Gbps)
  * Please contact Hirose or SolidRun for reliability and test result data.
* Mating height of between 1.5mm to 4.0mm (1.5mm to 3.0mm if using 70-pin Board-to-Board header). SR-SOM-MX6 headers are fixed, the final mating height is determined by carrier implementation

The different board-to-board functionality is defined as follows:

* Main 80 pin B2B. Includes the following functionality:
  * Main supply +3.3v to +5.0v in (5 pins)
  * I/O supply +3.3V and SD2, SD3 supplies (can be fixed +3.3V or externally switched +3.3V / 1.8V to support UHS-1)
  * Ethernet MDI (4 differential pairs), LED activity or link (10/100/1000) and Ethernet TCT
  * SATA TX/RX (2 differential pairs) – Functional on i.MX6 dual and quad (not supported on solo / dual lite)
  * USB OTG and HOST (2 differential pairs)
  * Various GPIOs and pins that can be muxed. By default, it is configured to be 2xI2C, PWMs (1 through 4), SPI 2, SD2 interface and USB enable.
* Second 80 pin B2B. The board-to-board exposes the following functionality:
  * System power on reset
  * HDMI 1.4 (4 differential pairs), CEC, +5V boosted I2C and HDMI HPD
  * PCI express 2.0 (3 differential pairs include TX/RX and clock)
  * USB OTG charge detect and USB OTG ID
  * MIPI CSI 2 (3 differential pairs for solo / dual lite and 5 differential pairs for dual / quad versions)
  * MIPI DSI (3 differential pairs)
  * LVDS 0 (5 differential pairs)
  * UART1 (typically used for main system debug port)
  * Various GPIOs and pins that can be muxed. By default, it is configured to be AUD5 I2S interface, CCM CLKO1/CLKO2, SD2 voltage select, SPDIF out, USB HOST / OTG over current indication.
* Third 70 pin B2B. This board-to-board exposes the following functionality:
  * Power management (EIM\_WAIT, TAMPER, PMIC standby, MX6\_ONOFF, PMIC\_ON\_REQ)
  * Boot mode override
  * MLB interface (marked as reserved on rev 1.3 and not available on rev 1.5. Contact SolidRun about availability of i.MX6 SOM with MLB interface)
  * Various GPIOs and pins that can be muxed. By default it is configured to be UART3, SPDIF in, Display and camera parallel interface, UART2, Watchdog timer, SD3 and SD4 interfaces)

## SR-SOM-MX6 ON Board Functions

#### 10/100/1000 Mbps PHY

The SOM incorporates a Qualcomm / Atheros AR8035 PHY. The PHY connectivity is as follows:

* Uses 2.5V interface voltage level
* RGMII (optional AR8030 with RMII)
* Phy reset function via i.MX6 pad V5 (KEY\_ROW4). Active low
* Default phy address either 0x0 or 0x4 (depends on LED activity reset strap, either pulled down or pulled up)

{% hint style="warning" %}
**Please note** Note that due to internal i.MX6 buses the 1000Mbps interface speed is limited to 470Mbps.
{% endhint %}


#### 802.11 b/g/n and Bluetooth SiP

The SOM incorporates AzureWave AW-660 SiP or TI Wilink8 SiP. The SiP interfaces are:

* WiFi connectivity via i.MX6 SDIO1
* Bluetooth connectivity via i.MX6 UART4
* Audio PCM connectivity via i.MX6 AUD3
* Antenna via onboard UFL connector

## i.MX6 SOM External Interfaces Detailed Description

As previously described, the SOM incorporates three Hirose DF40 based board-to-board headers.

The SOM uses the header of these board-to-board connectors which is fixed in height, while the mating height is determined by the carrier, by using different Hirose DF40 receptacle mating heights (1.5 to 4.0mm) (1.5mm to 3.0mm if using 70-pin Board-to-Board header).

#### J5002 Board to Board Header Pin Description

This board-to-board header uses Hirose DF40 DH40C-80DP-0.4V(51) header. The pin description may be found in the following tables:

| **Notes**      | **IC ball number** | **IC pad name** | **Driving IC** | **Schematics pad** | **Pin number** | **Pin number** | **Schematics pad**       | **Driving IC** | **IC pad name**    | **IC ball number** | **Notes**                                                                                                                                                      |
| -------------- | ------------------ | --------------- | -------------- | ------------------ | -------------- | -------------- | ------------------------ | -------------- | ------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                |                    |                 |                | GND                | 2              | 1              | MDI\_TRXN3               | Ethernet PHY   | MDI\_TRXN3         | 19                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 100 Ohm   | B14                | SATA\_RXP       | i.MX6          | SATA\_RXP          | 4              | 3              | MDI\_TRXP3               | Ethernet PHY   | MDI\_TRXP3         | 18                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 100 Ohm   | A14                | SATA\_RXM       | i.MX6          | SATA\_RXN          | 6              | 5              | GND                      |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 8              | 7              | MDI\_TRXN2               | Ethernet PHY   | MDI\_TRXN2         | 16                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 100 Ohm   | B12                | SATA\_TXM       | i.MX6          | SATA\_TXN          | 10             | 9              | MDI\_TRXP2               | Ethernet PHY   | MDI\_TRXP2         | 15                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 100 Ohm   | A12                | SATA\_TXP       | i.MX6          | SATA\_TXP          | 12             | 11             | GND                      |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 14             | 13             | MDI\_TRXN1               | Ethernet PHY   | MDI\_TRXN1         | 13                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 90 Ohm    | A6                 | USB\_OTG\_DP    | i.MX6          | USB\_OTG\_DP       | 16             | 15             | MDI\_TRXP1               | Ethernet PHY   | MDI\_TRXP1         | 12                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 90 Ohm    | B6                 | USB\_OTG\_DN    | i.MX6          | USB\_OTG\_DN       | 18             | 17             | GND                      |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 20             | 19             | MDI\_TRXN0               | Ethernet PHY   | MDI\_TRXN0         | 10                 | Diff 100 Ohm                                                                                                                                                   |
| Diff 90 Ohm    | E10                | USB\_H1\_DP     | i.MX6          | USB\_HOST\_DP      | 22             | 21             | MDI\_TRXP0               | Ethernet PHY   | MDI\_TRXP0         | 9                  | Diff 100 Ohm                                                                                                                                                   |
| Diff 90 Ohm    | F10                | USB\_H1\_DN     | i.MX6          | USB\_HOST\_DN      | 24             | 23             | GND                      |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 26             | 25             | LED\_10\_100\_1000       | Ethernet PHY   | LED\_10\_100\_1000 | 22                 |                                                                                                                                                                |
|                | T5                 | GPIO\_0         | i.MX6          | USB\_H1\_PWR\_EN   | 28             | 27             | LED\_ACT                 | Ethernet PHY   | LED\_ACT           | 21                 |                                                                                                                                                                |
|                | E23                | EIM\_D22        | i.MX6          | USB\_OTG\_PWR\_EN  | 30             | 29             | ETH\_TCT                 | Ethernet PHY   | ETH\_TCT           | N/A                |                                                                                                                                                                |
| BOOT\_CFG4\[5] | K20                | EIM\_RW         | i.MX6          | ECSPI2\_SS0        | 32             | 31             | I2C3\_SCL                | i.MX6          | EIM\_D17           | F21                | 4.7kohm NVCC\_EIM0 pulled up                                                                                                                                   |
| BOOT\_CFG4\[2] | K22                | EIM\_LBA        | i.MX6          | ECSPI2\_SS1        | 34             | 33             | I2C3\_SDA                | i.MX6          | EIM\_D18           | D24                | 4.7kohm NVCC\_EIM0 pulled up                                                                                                                                   |
|                |                    |                 |                | GND                | 36             | 35             | GND                      |                |                    |                    |                                                                                                                                                                |
|                | C21                | SD2\_CLK        | i.MX6          | SD2\_CLK           | 38             | 37             | SD3\_CLK                 | i.MX6          | SD3\_CLK           | D14                | This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC.                                                                      |
|                | F19                | SD2\_CMD        | i.MX6          | SD2\_CMD           | 40             | 39             | SD3\_CMD                 | i.MX6          | SD3\_CMD           | B13                | This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC.                                                                      |
|                | A22                | SD2\_DATA0      | i.MX6          | SD2\_DATA0         | 42             | 41             | PWM2\_OUT                | i.MX6          | DISP0\_DAT9        | T25                |                                                                                                                                                                |
|                | E20                | SD2\_DATA1      | i.MX6          | SD2\_DATA1         | 44             | 43             | USB\_OTG\_VBUS           | i.MX6          | USB\_OTG\_VBUS     | E9                 |                                                                                                                                                                |
|                | A23                | SD2\_DATA2      | i.MX6          | SD2\_DATA2         | 46             | 45             | ECSPI2\_MISO             | i.MX6          | EIM\_OE            | J24                |                                                                                                                                                                |
|                | B22                | SD2\_DATA3      | i.MX6          | SD2\_DATA3         | 48             | 47             | ECSPI2\_MOSI             | i.MX6          | EIM\_CS1           | J23                |                                                                                                                                                                |
|                | R6                 | GPIO\_4         | i.MX6          | SD2\_CD\_B         | 50             | 49             | ECSPI2\_SCLK             | i.MX6          | EIM\_CS0           | H24                |                                                                                                                                                                |
|                | D10                | USB\_H1\_VBUS   | i.MX6          | USB\_H1\_VBUS      | 52             | 51             | I2C1\_SDA                | i.MX6          | EIM\_D28           | G23                | 4.7kohm NVCC\_EIM0 pulled up                                                                                                                                   |
| BOOT\_CFG1\[6] | K25                | EIM\_DA6        | i.MX6          | DISP1\_DATA03      | 54             | 53             | I2C1\_SCL                | i.MX6          | EIM\_D21           | H20                | 4.7kohm NVCC\_EIM0 pulled up                                                                                                                                   |
| BOOT\_CFG1\[7] | L25                | EIM\_DA7        | i.MX6          | DISP1\_DATA02      | 56             | 55             | PWM3\_OUT                | i.MX6          | SD4\_DAT1          | B19                |                                                                                                                                                                |
| BOOT\_CFG1\[3] | K24                | EIM\_DA3        | i.MX6          | DISP1\_DATA06      | 58             | 57             | PWM4\_OUT                | i.MX6          | SD4\_DAT2          | F17                |                                                                                                                                                                |
| BOOT\_CFG2\[0] | L24                | EIM\_DA8        | i.MX6          | DISP1\_DATA01      | 60             | 59             | \_\_NC\_\_SPDIF\_CLK\_IN | NC             |                    |                    |                                                                                                                                                                |
| BOOT\_CFG1\[4] | L22                | EIM\_DA4        | i.MX6          | DISP1\_DATA05      | 62             | 61             | NVCC\_SD2                | i.MX6          | NVCC\_SD2          | G17                |                                                                                                                                                                |
| BOOT\_CFG1\[5] | L23                | EIM\_DA5        | i.MX6          | DISP1\_DATA04      | 64             | 63             | NVCC\_SD3                | i.MX6          | NVCC\_SD3          | G14                |                                                                                                                                                                |
| BOOT\_CFG2\[1] | M21                | EIM\_DA9        | i.MX6          | DISP1\_DATA00      | 66             | 65             | NVCC\_EIM0               | Many           |                    |                    | <p>Although called NVCC_EIM0, this power rail supplies the i.MX6, Ethernet phy, WiFi / BT and others.<br> Refer to the public schematics for more details.</p> |
|                | R22                | DISP0\_DAT8     | i.MX6          | PWM1\_OUT          | 68             | 67             | NVCC\_EIM0               |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 70             | 69             | VSNVS\_3V0               | i.MX6          |                    |                    | In rev 1.2 and beyond this is VDD\_SNVS\_IN and VDDHIGH\_IN power domains                                                                                      |
|                |                    |                 |                | GND                | 72             | 71             | VIN\_5V0                 |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 74             | 73             | VIN\_5V0                 |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 76             | 75             | VIN\_5V0                 |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 78             | 77             | VIN\_5V0                 |                |                    |                    |                                                                                                                                                                |
|                |                    |                 |                | GND                | 80             | 79             | VIN\_5V0                 |                |                    |                    |                                                                                                                                                                |

#### J8004 Board to Board Header Pin Description

| **Notes**    | **IC ball number** | **IC pad name** | **Driving IC** | **Schematics pad** | **Pin number** | **Pin number** | **Schematics pad**  | **Driving IC** | **IC pad name**  | **IC ball number** | **Notes**                                     |
| ------------ | ------------------ | --------------- | -------------- | ------------------ | -------------- | -------------- | ------------------- | -------------- | ---------------- | ------------------ | --------------------------------------------- |
| Diff 85 Ohm  | B1                 | PCIE\_RXM       | i.MX6          | PCIE\_RXM          | 2              | 1              | CLK1\_P             | i.MX6          | CLK1\_P          | D7                 | Diff 85 Ohm                                   |
| Diff 85 Ohm  | B2                 | PCIE\_RXP       | i.MX6          | PCIE\_RXP          | 4              | 3              | CLK1\_N             | i.MX6          | CLK1\_N          | C7                 | Diff 85 Ohm                                   |
|              |                    |                 |                | GND                | 6              | 5              | GND                 |                |                  |                    |                                               |
| Diff 100 Ohm | E4                 | CSI\_D0M        | i.MX6          | CSI\_D0M           | 8              | 7              | PCIE\_TXM           | i.MX6          | PCIE\_TXM        | A3                 | Diff 85 Ohm                                   |
| Diff 100 Ohm | E3                 | CSI\_D0P        | i.MX6          | CSI\_D0P           | 10             | 9              | PCIE\_TXP           | i.MX6          | PCIE\_TXP        | B3                 | Diff 85 Ohm                                   |
|              |                    |                 |                | GND                | 12             | 11             | GND                 |                |                  |                    |                                               |
| Diff 100 Ohm | D1                 | CSI\_D1M        | i.MX6          | CSI\_D1M           | 14             | 13             | CSI\_CLK0P          | i.MX6          | CSI\_CLK0M       | F3                 | Diff 100 Ohm                                  |
| Diff 100 Ohm | D2                 | CSI\_D1P        | i.MX6          | CSI\_D1P           | 16             | 15             | CSI\_CLK0M          | i.MX6          | CSI\_CLK0P       | F4                 | Diff 100 Ohm                                  |
|              |                    |                 |                | GND                | 18             | 17             | GND                 |                |                  |                    |                                               |
| Diff 100 Ohm | E1                 | CSI\_D2M        | i.MX6          | CSI\_D2M           | 20             | 19             | HDMI\_D2P           | i.MX6          | HDMI\_D2P        | K4                 | Diff 100 Ohm                                  |
| Diff 100 Ohm | E2                 | CSI\_D2P        | i.MX6          | CSI\_D2P           | 22             | 21             | HDMI\_D2M           | i.MX6          | HDMI\_D2M        | K3                 | Diff 100 Ohm                                  |
|              |                    |                 |                | GND                | 24             | 23             | GND                 |                | GND              |                    |                                               |
| Diff 100 Ohm | F2                 | CSI\_D3M        | i.MX6          | CSI\_D3M           | 26             | 25             | HDMI\_D1P           | i.MX6          | HDMI\_D1P        | J4                 | Diff 100 Ohm                                  |
| Diff 100 Ohm | F1                 | CSI\_D3P        | i.MX6          | CSI\_D3P           | 28             | 27             | HDMI\_D1M           | i.MX6          | HDMI\_D1M        | J3                 | Diff 100 Ohm                                  |
|              |                    |                 |                | GND                | 30             | 29             | GND                 |                | GND              |                    |                                               |
| Diff 100 Ohm | H2                 | DSI\_D1M        | i.MX6          | DSI\_D1M           | 32             | 31             | HDMI\_D0P           | i.MX6          | HDMI\_D0P        | K6                 | Diff 100 Ohm                                  |
| Diff 100 Ohm | H1                 | DSI\_D1P        | i.MX6          | DSI\_D1P           | 34             | 33             | HDMI\_D0M           | i.MX6          | HDMI\_D0M        | K5                 | Diff 100 Ohm                                  |
|              |                    |                 |                | GND                | 36             | 35             | GND                 |                | GND              |                    |                                               |
| Diff 100 Ohm | G2                 | DSI\_D0M        | i.MX6          | DSI\_D0M           | 38             | 37             | HDMI\_CLKP          | i.MX6          | HDMI\_CLKP       | J6                 | Diff 100 Ohm                                  |
| Diff 100 Ohm | G1                 | DSI\_D0P        | i.MX6          | DSI\_D0P           | 40             | 39             | HDMI\_CLKM          | i.MX6          | HDMI\_CLKM       | J5                 | Diff 100 Ohm                                  |
|              |                    |                 |                | GND                | 42             | 41             | GND                 |                |                  |                    |                                               |
| Diff 100 Ohm | H3                 | DSI\_CLK0M      | i.MX6          | DSI\_CLK0M         | 44             | 43             | HDMI\_TX\_CEC\_LINE | i.MX6          | KEY\_ROW2        | W4                 |                                               |
| Diff 100 Ohm | H4                 | DSI\_CLK0P      | i.MX6          | DSI\_CLK0P         | 46             | 45             | HDMI\_TX\_DDC\_SCL  | i.MX6          | KEY\_COL3        | U5                 | Boosted to 5V and 4.7kohm pulled up           |
|              |                    |                 |                | GND                | 48             | 47             | HDMI\_TX\_DDC\_SDA  | i.MX6          | KEY\_ROW3        | T7                 |                                               |
|              | R1                 | GPIO\_17        | i.MX6          | SPDIF\_OUT         | 50             | 49             | HDMI\_HPD           | i.MX6          | HDMI\_HPD        | K1                 | Level shifted to 3.3v                         |
|              | M1                 | CSI0\_DAT10     | i.MX6          | UART1\_TX\_DATA    | 52             | 51             | AUD5\_TXC           | i.MX6          | KEY\_COL0        | W5                 |                                               |
|              | M3                 | CSI0\_DAT11     | i.MX6          | UART1\_RX\_DATA    | 54             | 53             | AUD5\_TXD           | i.MX6          | KEY\_ROW0        | V6                 |                                               |
|              | T4                 | GPIO\_1         | i.MX6          | USB\_OTG\_ID       | 56             | 55             | AUD5\_TXFS          | i.MX6          | KEY\_COL1        | U7                 |                                               |
|              |                    |                 |                | GND                | 58             | 57             | AUD5\_RXD           | i.MX6          | DISP0\_DAT19     | U23                |                                               |
| Diff 100 Ohm | U2                 | LVDS0\_TX0\_N   | i.MX6          | LVDS0\_TX0\_N      | 60             | 59             | CCM\_CLKO1          | i.MX6          | GPIO\_5          | R4                 |                                               |
| Diff 100 Ohm | U1                 | LVDS0\_TX0\_P   | i.MX6          | LVDS0\_TX0\_P      | 62             | 61             | GND                 |                |                  |                    |                                               |
|              |                    |                 |                | GND                | 64             | 63             | CCM\_CLKO2          | i.MX6          | NANDF\_CS2       | A17                |                                               |
| Diff 100 Ohm | U4                 | LVDS0\_TX1\_N   | i.MX6          | LVDS0\_TX1\_N      | 66             | 65             | POR\_B              | i.MX6          | POR\_B           | C11                | Rev 1.5 adds 100nF capacitance on this signal |
| Diff 100 Ohm | U3                 | LVDS0\_TX1\_P   | i.MX6          | LVDS0\_TX1\_P      | 68             | 67             | USB\_OTG\_OC        | i.MX6          | KEY\_COL4        | T6                 |                                               |
|              |                    |                 |                | GND                | 70             | 69             | USB\_H!\_OC         | i.MX6          | GPIO\_3          | R7                 |                                               |
| Diff 100 Ohm | V2                 | LVDS0\_TX2\_N   | i.MX6          | LVDS0\_TX2\_N      | 72             | 71             | USB\_OTG\_CHD\_B    | i.MX6          | USB\_OTG\_CHD\_B | B8                 |                                               |
| Diff 100 Ohm | V1                 | LVDS0\_TX2\_P   | i.MX6          | LVDS0\_TX2\_P      | 74             | 73             | SD2\_VSELECT        | i.MX6          | KEY\_ROW1        | U6                 |                                               |
|              |                    |                 |                | GND                | 76             | 75             | GND                 |                |                  |                    |                                               |
| Diff 100 Ohm | V4                 | LVDS0\_CLK\_N   | i.MX6          | LVDS0\_CLK\_N      | 78             | 77             | LVDS0\_TX3\_P       | i.MX6          | LVDS0\_TX3\_P    | W1                 | Diff 100 Ohm                                  |
| Diff 100 Ohm | V3                 | LVDS0\_CLK\_P   | i.MX6          | LVDS0\_CLK\_P      | 80             | 79             | LVDS0\_TX3\_N       | i.MX6          | LVDS0\_TX3\_N    | W2                 | Diff 100 Ohm                                  |

#### J5001 Board to Board Header Pin Description

| **Notes**                                                                                 | **IC ball** | **IC pad name** | **Driving IC** | **Schematics pad** | **Pin number** | **Pin number** | **Schematics pad** | **Driving IC** | **IC pad name** | **IC ball** | **Notes**              |
| ----------------------------------------------------------------------------------------- | ----------- | --------------- | -------------- | ------------------ | -------------- | -------------- | ------------------ | -------------- | --------------- | ----------- | ---------------------- |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | F13         | SD3\_DAT7       | i.MX6          | SD3\_DATA7         | 2              | 1              | EIM\_WAIT          | i.MX6          | EIM\_WAIT       | M25         | BOOT\_CFG4\[1]         |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | E13         | SD3\_DAT6       | i.MX6          | SD3\_DATA6         | 4              | 3              | BOOT\_MODE0        | i.MX6          | BOOT\_MODE0     | C12         |                        |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | C13         | SD3\_DAT5       | i.MX6          | SD3\_DATA5         | 6              | 5              | BOOT\_MODE1        | i.MX6          | BOOT\_MODE1     | F12         |                        |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | D13         | SD3\_DAT4       | i.MX6          | SD3\_DATA4         | 8              | 7              | TAMPER             | i.MX6          | TAMPER          | E11         |                        |
|                                                                                           |             |                 |                | GND                | 10             | 9              | PMIC\_STBY\_REQ    | i.MX6          | PMIC\_STBY\_REQ | F11         |                        |
| Rev 1.5                                                                                   | W6          | KEY\_COL2       | i.MX6          | FLEXCAN1\_TX (1.5) | 12             | 11             | GPIO3\_IO19        | i.MX6          | EIM\_D19        | G21         | Rev 1.5                |
| Rev 1.5                                                                                   | R3          | GPIO\_7         | i.MX6          | GPIO7 (1.5)        | 14             | 13             | MX6\_ONOFF         | i.MX6          | ONOFF           | D12         |                        |
|                                                                                           |             |                 |                | GND                | 16             | 15             | PMIC\_ON\_REQ      | i.MX6          | PMIC\_ON\_REQ   | D11         |                        |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | B15         | SD3\_DAT3       | i.MX6          | SD3\_DATA3         | 18             | 17             | EIM\_A25           | i.MX6          | EIM\_A25        | H19         | Rev 1.5                |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | A15         | SD3\_DAT2       | i.MX6          | SD3\_DATA2         | 20             | 19             | EIM\_D16           | i.MX6          | EIM\_D16        | C25         | Rev 1.5                |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | F14         | SD3\_DAT1       | i.MX6          | SD3\_DATA1         | 22             | 21             | EIM\_BCLK          | i.MX6          | EIM\_BCLK       | N22         | Rev 1.5                |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | E14         | SD3\_DAT0       | i.MX6          | SD3\_DATA0         | 24             | 23             | EIM\_D20           | i.MX6          | EIM\_D20        | G20         | Rev 1.5                |
| This signal is not available on SOM V1.9+ with or without eMMC, or on SOM V1.5 with eMMC. | D15         | SD3\_RST        | i.MX6          | SD3\_RST           | 26             | 25             | EIM\_D23           | i.MX6          | EIM\_D23        | D25         | Rev 1.5                |
|                                                                                           | P6          | GPIO\_18        | i.MX6          | SD3\_VSELECT       | 28             | 27             | EIM\_D29           | i.MX6          | EIM\_D29        | J19         | Rev 1.5                |
|                                                                                           |             |                 |                | GND                | 30             | 29             | UART3\_TX\_DATA    | i.MX6          | EIM\_D24        | F22         |                        |
|                                                                                           | E16         | SD4\_CLK        | i.MX6          | SD4\_CLK           | 32             | 31             | UART3\_RX\_DATA    | i.MX6          | EIM\_D25        | G22         |                        |
|                                                                                           | B17         | SD4\_CMD        | i.MX6          | SD4\_CMD           | 34             | 33             | GND                |                |                 |             |                        |
|                                                                                           | D18         | SD4\_DAT0       | i.MX6          | SD4\_DATA0         | 36             | 35             | SPDIF\_IN          | i.MX6          | ENET\_RX\_ER    | W23         |                        |
|                                                                                           | A20         | SD4\_DAT3       | i.MX6          | SD4\_DATA3         | 38             | 37             | EIM\_EB2           | i.MX6          | EIM\_EB2        | E22         | Rev 1.5 BOOT\_CFG4\[6] |
|                                                                                           | J20         | EIM\_D30        | i.MX6          | DISP1\_DATA21      | 40             | 39             | EIM\_EB3           | i.MX6          | EIM\_EB3        | F23         | Rev 1.5 BOOT\_CFG4\[7] |
|                                                                                           | H21         | EIM\_D31        | i.MX6          | WDOG1\_B           | 42             | 41             | DI1\_PIN02         | i.MX6          | EIM\_DA11       | M20         | BOOT\_CFG2\[3]         |
|                                                                                           | E18         | SD4\_DAT4       | i.MX6          | UART2\_RX\_DATA    | 44             | 43             | DI1\_PIN15         | i.MX6          | EIM\_DA10       | M22         | BOOT\_CFG2\[2]         |
|                                                                                           | D19         | SD4\_DAT7       | i.MX6          | UART2\_TX\_DATA    | 46             | 45             | DI1\_D0\_CS        | i.MX6          | EIM\_DA13       | M23         | BOOT\_CFG2\[5]         |
|                                                                                           | B20         | SD4\_DAT6       | i.MX6          | UART2\_CTS\_B      | 48             | 47             | GND                |                |                 |             |                        |
|                                                                                           | C19         | SD4\_DAT5       | i.MX6          | UART2\_RTS\_B      | 50             | 49             | DI1\_D1\_CS        | i.MX6          | EIM\_DA14       | N23         | BOOT\_CFG2\[6]         |
|                                                                                           |             |                 |                | GND                | 52             | 51             | DI1\_PIN03         | i.MX6          | EIM\_DA12       | M24         | BOOT\_CFG2\[4]         |
| BOOT\_CFG3\[0]                                                                            | H25         | EIM\_A16        | i.MX6          | DI1\_DISP\_CLK     | 54             | 53             | DI1\_PIN01         | i.MX6          | EIM\_DA15       | N24         | BOOT\_CFG2\[7]         |
| BOOT\_CFG3\[7]                                                                            | J21         | EIM\_A23        | i.MX6          | DISP1\_DATA18      | 56             | 55             | DISP1\_DATA08      | i.MX6          | EIM\_DA1        | J25         | BOOT\_CFG1\[1]         |
|                                                                                           | H21         | EIM\_D31        | i.MX6          | DISP1\_DATA20      | 58             | 57             | DISP1\_DATA10      | i.MX6          | EIM\_EB1        | K23         | BOOT\_CFG4\[4]         |
| BOOT\_CFG1\[0]                                                                            | L20         | EIM\_DA0        | i.MX6          | DISP1\_DATA09      | 60             | 59             | DISP1\_DATA12      | i.MX6          | EIM\_A17        | G24         | BOOT\_CFG3\[1]         |
| BOOT\_CFG3\[4]                                                                            | H22         | EIM\_A20        | i.MX6          | DISP1\_DATA15      | 62             | 61             | DISP1\_DATA22      | i.MX6          | EIM\_D26        | E24         |                        |
| BOOT\_CFG3\[2]                                                                            | J22         | EIM\_A18        | i.MX6          | DISP1\_DATA13      | 64             | 63             | DISP1\_DATA14      | i.MX6          | EIM\_A19        | G25         | BOOT\_CFG3\[3]         |
| BOOT\_CFG3\[5]                                                                            | H23         | EIM\_A21        | i.MX6          | DISP1\_DATA16      | 66             | 65             | DISP1\_DATA23      | i.MX6          | EIM\_D27        | E25         |                        |
| BOOT\_CFG4\[3]                                                                            | K21         | EIM\_EB0        | i.MX6          | DISP1\_DATA11      | 68             | 67             | DISP1\_DATA19      | i.MX6          | EIM\_A24        | F25         | BOOT\_CFG4\[0]         |
| BOOT\_CFG1\[2]                                                                            | L21         | EIM\_DA2        | i.MX6          | DISP1\_DATA07      | 70             | 69             | DISP1\_DATA17      | i.MX6          | EIM\_A22        | F24         | BOOT\_CFG3\[6]         |

#### i.MX6 SOM Power Up Sequence

Integration with the SR-SOM-MX6 is easy, power sequencing wise. Note the following requirements:

* The SOM internal power management contains a soft-start clamp that gradually raises its internally generated power supplies once VIN\_5V0 is applied. The soft-start timing is set to be 800us (typ.). SNVS\_3V0 must be applied well ahead of the internal power rails. We recommend that SNVS\_3V0 be applied no later than 200uS after
* SNVS\_3V0 must be applied before NVCC\_EIM0, NVCC\_SD2 and NVCC\_SD3. Alternatively, SNVS\_3V0 can be shorted with those power supplies as long as they do not exceed 3.3v (absolute maximum including overvoltage ripples).

{% hint style="warning" %}
**Please note** Notice the HummingBoard design, where there is a single 3.2V power rail generated from the 5V DC IN (either via LDO or external DC-DC), and that rail is directly applied to VSNVS\_3V0, NVCC\_EIM0 together with the VIN\_5V0.
{% endhint %}


* Notice that a cost saving practice when integrating SR-SOM-MX6 is to have a single DC-DC of output voltage 3.2v, and -+100mV ripple that supplies all the SR-SOM-MX6 supplies, except the USB\_OTG\_VBUS and USB\_HOST\_VBUS which are 5V when

## **i.MX6 SOM GPIO (Internal) Boot Source Configuration**

1. MX6 is very flexible when it comes to selecting the boot source. This section describes how to set pull up /down on the carrier board in order to perform boot indicated by GPIOs

Blowing the device’s eFuses is alternative to using GPIOs in order to set boot source. This topic is widely covered on the SolidRun [eFuses for i.MX6 SOM (Developers page)](imx6-other-articles/efuses-for-imx6-som-developers-page.md) .

{% hint style="warning" %}
If the boot method is set, via eFuses (irreversible operation) then boot select via GPIO pull up/down will be void and ONLY the eFusing configuration regulates the boot device.
{% endhint %}


{% hint style="warning" %}
The section below assumes that the SOM’s boot eFuses are not set, it also assumes that the boot mode is set to BOOT\_MODE\[1:0] = 0b10, indicating boot from GPIOs.
{% endhint %}


The following are the general instructions on how to perform boot from different common sources, the guideline in general is the following –

1. BOOT\_CFGx\[7:0] is pulled down in reset and then reverts to pull up.
2. The user should pull up the required pins, but making sure that all pins in the bus are either floating, tri-stated in reset (POR\_B) or pulled down.

Since the above forces the user to pull up/down the entire bus, below are more pervasive examples of 3 different boot sources used as in [HummingBoard Edge Quick Start Guide](hummingboard-imx6-sbc-quick-start-guide/hummingboard-edge-quick-start-guide.md) :

* SDHC2 SD
* SDHC3 eMMC
* SATA

#### **Boot from SDHC2 External SD Card**

The following is an example of booting from SD card through schematics signals SD2\_\*:

The following must be pulled up (10 kohm or lower):

|                   |                    |                         |
| ----------------- | ------------------ | ----------------------- |
| **BOOT CFG name** | **i.MX6 pad name** | **Schematics pad name** |
| BOOT\_CFG1\[6]    | EIM\_DA6           | DISP1\_DATA03           |
| BOOT\_CFG2\[3]    | EIM\_DA11          | DI1\_PIN02              |

{% hint style="warning" %}
**Please note** SolidRun tested pulling down the signals as described below, but the user can experiment with the signals that are not marked with ‘Must be 0’; but SolidRun does not test those signals behavior.
{% endhint %}


|                   |                    |                         |                                       |
| ----------------- | ------------------ | ----------------------- | ------------------------------------- |
| **BOOT CFG name** | **i.MX6 pad name** | **Schematics pad name** | **Notes**                             |
| BOOT\_CFG1\[0]    | EIM\_DA0           | DISP1\_DATA09           | Can be either 0 or 1                  |
| BOOT\_CFG1\[1]    | EIM\_DA1           | DISP1\_DATA08           | If 1 power cycles the external device |
| BOOT\_CFG1\[2]    | EIM\_DA2           | DISP1\_DATA07           | Can be either 0 or 1                  |
| BOOT\_CFG1\[3]    | EIM\_DA3           | DISP1\_DATA06           | Must be 0                             |
| BOOT\_CFG1\[4]    | EIM\_DA4           | DISP1\_DATA05           | Must be 0                             |
| BOOT\_CFG1\[5]    | EIM\_DA5           | DISP1\_DATA04           | Must be 0                             |
| BOOT\_CFG1\[7]    | EIM\_DA7           | DISP1\_DATA02           | Must be 0                             |
| BOOT\_CFG2\[0]    | EIM\_DA8           | DISP1\_DATA01           | Must be 0                             |
| BOOT\_CFG2\[1]    | EIM\_DA9           | DISP1\_DATA00           | Must be 0                             |
| BOOT\_CFG2\[2]    | EIM\_DA10          | DI1\_PIN15              | Must be 0                             |
| BOOT\_CFG2\[4]    | EIM\_DA12          | DI1\_PIN03              | Must be 0                             |
| BOOT\_CFG2\[5]    | EIM\_DA13          | DI1\_D0\_CS             | Can be 1 in case of 4 bit SD          |
| BOOT\_CFG2\[6]    | EIM\_DA14          | DI1\_D1\_CS             | Must be 0                             |
| BOOT\_CFG2\[7]    | EIM\_DA15          | DI1\_PIN01              | Must be 0                             |
| BOOT\_CFG3\[6]    | EIM\_A22           | DISP1\_DATA17           | Must be 0                             |
| BOOT\_CFG3\[7]    | EIM\_A23           | DISP1\_DATA18           | Must be 0                             |
| BOOT\_CFG3\[2]    | EIM\_A18           | DISP1\_DATA13           | Boot freq – preferred 0               |
| BOOT\_CFG4\[7]    | EIM\_EB3           | EIM\_EB3                | Must be 0                             |

The other signals in BOOT\_CFG3 and BOOT\_CFG4 that are not defined in the above two tables do not affect this boot method.

#### **Boot from SDHC3 eMMC**

The following is an example of booting SD card through schematics signals SD3\_\*:

The following must be pulled up (10 kohm or lower):

|                   |                    |                         |
| ----------------- | ------------------ | ----------------------- |
| **BOOT CFG name** | **i.MX6 pad name** | **Schematics pad name** |
| BOOT\_CFG1\[5]    | EIM\_DA5           | DISP1\_DATA04           |
| BOOT\_CFG1\[6]    | EIM\_DA6           | DISP1\_DATA03           |
| BOOT\_CFG2\[4]    | EIM\_DA12          | DI1\_PIN03              |

{% hint style="warning" %}
SolidRun tested pulling down the signals as described below, but the user can experiment with the signals that are not marked with ‘Must be 0’; but SolidRun does not test those signals behavior.
{% endhint %}


|                   |                    |                         |                         |
| ----------------- | ------------------ | ----------------------- | ----------------------- |
| **BOOT CFG name** | **i.MX6 pad name** | **Schematics pad name** | **Notes**               |
| BOOT\_CFG1\[0]    | EIM\_DA0           | DISP1\_DATA09           | Can be either 0 or 1    |
| BOOT\_CFG1\[1]    | EIM\_DA1           | DISP1\_DATA08           | Must be 0               |
| BOOT\_CFG1\[2]    | EIM\_DA2           | DISP1\_DATA07           | Must be 0               |
| BOOT\_CFG1\[3]    | EIM\_DA3           | DISP1\_DATA06           | Must be 0               |
| BOOT\_CFG1\[4]    | EIM\_DA4           | DISP1\_DATA05           | Must be 0               |
| BOOT\_CFG1\[7]    | EIM\_DA7           | DISP1\_DATA02           | Must be 0               |
| BOOT\_CFG2\[0]    | EIM\_DA8           | DISP1\_DATA01           | Must be 0               |
| BOOT\_CFG2\[1]    | EIM\_DA9           | DISP1\_DATA00           | Must be 0               |
| BOOT\_CFG2\[2]    | EIM\_DA10          | DI1\_PIN15              | Must be 0               |
| BOOT\_CFG2\[3]    | EIM\_DA11          | DI1\_PIN02              | Must be 0               |
| BOOT\_CFG2\[5]    | EIM\_DA13          | DI1\_D0\_CS             | Can be 1 or 0           |
| BOOT\_CFG2\[6]    | EIM\_DA14          | DI1\_D1\_CS             | Must be 0               |
| BOOT\_CFG2\[7]    | EIM\_DA15          | DI1\_PIN01              | Must be 0               |
| BOOT\_CFG3\[6]    | EIM\_A22           | DISP1\_DATA17           | Must be 0               |
| BOOT\_CFG3\[7]    | EIM\_A23           | DISP1\_DATA18           | Must be 0               |
| BOOT\_CFG3\[2]    | EIM\_A18           | DISP1\_DATA13           | Boot freq – preferred 0 |
| BOOT\_CFG4\[7]    | EIM\_EB3           | EIM\_EB3                | Must be 0               |

The other signals in BOOT\_CFG3 and BOOT\_CFG4 that are not defined in the above two tables do not affect this boot method.

#### Boot from SATA

The following must be pulled up (10 kohm or lower):

|                   |                    |                         |
| ----------------- | ------------------ | ----------------------- |
| **BOOT CFG name** | **i.MX6 pad name** | **Schematics pad name** |
| BOOT\_CFG1\[5]    | EIM\_DA5           | DISP1\_DATA04           |
| BOOT\_CFG2\[4]    | EIM\_DA11          | DI1\_PIN03              |

{% hint style="warning" %}
**Please Note** SolidRun tested pulling down the signals as described below, but the user can experiment with the signals that are not marked with ‘Must be 0’; but SolidRun does not test those signals behavior.
{% endhint %}


|                   |                    |                         |                                                         |
| ----------------- | ------------------ | ----------------------- | ------------------------------------------------------- |
| **BOOT CFG name** | **i.MX6 pad name** | **Schematics pad name** | **Notes**                                               |
| BOOT\_CFG1\[4]    | EIM\_DA4           | DISP1\_DATA05           | Must be 0                                               |
| BOOT\_CFG1\[6]    | EIM\_DA6           | DISP1\_DATA03           | Must be 0                                               |
| BOOT\_CFG1\[7]    | EIM\_DA7           | DISP1\_DATA02           | Must be 0                                               |
| BOOT\_CFG2\[0]    | EIM\_DA8           | DISP1\_DATA01           | Refer to spec about BOOT\_CFG2\[1:0]                    |
| BOOT\_CFG2\[1]    | EIM\_DA9           | DISP1\_DATA00           | As above; defines cable length                          |
| BOOT\_CFG2\[2]    | EIM\_DA10          | DI1\_PIN15              | Can be either 0 or 1                                    |
| BOOT\_CFG2\[3]    | EIM\_DA11          | DI1\_PIN02              | Can be either 0 or 1 (RX spread spectrum)               |
| BOOT\_CFG2\[4]    | EIM\_DA11          | DI1\_PIN03              | <p>Can be either 0 or 1 (TX<br><br>spread spectrum)</p> |
| BOOT\_CFG3\[6]    | EIM\_A22           | DISP1\_DATA17           | Must be 0                                               |
| BOOT\_CFG3\[7]    | EIM\_A23           | DISP1\_DATA18           | Must be 0                                               |
| BOOT\_CFG3\[2]    | EIM\_A18           | DISP1\_DATA13           | Boot freq – preferred 0                                 |
| BOOT\_CFG4\[7]    | EIM\_EB3           | EIM\_EB3                | Must be 0                                               |

The other signals in BOOT\_CFG1, BOOT\_CFG2, BOOT\_CFG3 and BOOT\_CFG4 that are not defined in the above two tables do not affect this boot method.

#### **Rev 1.3 Debugging Capability**

&#x20;Rev 1.3 of SR-SOM-MX6 exposes two main debugging interfaces:

1. UART interface
2. JTAG interface

The UART interface is a null modem interface that is internally pulled up to two different voltage levels:

1. NVCC\_EIM0 voltage in case AzureWave SiP is not used (typically 3V)
2. 8v when the AzureWave SiP is used (signals are shared with SDIO interface that is limited to 2.8V)

The UART interface is optional to use and mentioned here since most of the software infrastructure used in CuBox-i and HummingBoard uses those two signals for debugging.

JTAG interface is on the SR-SOM-mx6 and is exposed as test pins. Following is a snapshot of the test points and its connectivity traces:

![](../../../.gitbook/assets/image-20211226-093141.png)

#### **Rev 1.5 Debugging Capability**

Rev 1.5 of SR-SOM-MX6 exposes the UART interface which is the main debugging interface. The UART interface is a null modem interface.

#### **Differences Between SOM Versions**

**Changes Between SOM Rev 1.0 to Rev 1.2**

Moved VDD\_HIGH\_IN power rail from NVCC\_EIM0 power pin to SNVS\_3V0 power pin.

**Changes Between SOM Rev 1.2 to Rev 1.3**

Added three mechanical holes for RF cage to cover BRCM4330 based WiFi/BT SiP.

**Changes Between SOM Rev 1.3 to Rev 1.5**

Refer to PCN #20160901000 on SolidRun’s wiki pages for more details, the highlights are –

1. Replaced BCM4330 based SiP with TI Wilink8
2. Added optional eMMC. Note that if the SOM has eMMC assembled then the SD3\_\* signals are not routed to the board-to-board headers but are used locally for the eMMC on the SOM.

#### **Typical Power Consumption**

The following power measurements were performed on a CuBox-i4pro based system, where the main supply is 5V and internally a 5V to 3.3V LDO is being used on the carrier board (refer to CuBox-i rev-1.1 schematics).

The CuBox-i4pro incorporates the quad processor at 1GHz, 2GByte of DDR3 memory, gigabit Ethernet PHY and the WiFi and Bluetooth chipset.

|                                                                                                   |                                   |                                                                                                        |
| ------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Setup**                                                                                         | **5V DC input power consumption** | **Notes**                                                                                              |
| Android idle                                                                                      | 240mA                             | <p>Performance governor, HDMI is on,<br><br>USB, eSata, WiFi and Ethernet are off</p>                  |
| Android idle with Ethernet                                                                        | 340mA                             | <p>Performance governor, HDMI is on, USB, eSata, WiFi and Ethernet is<br><br>1Gbps (note #1)</p>       |
| Android Nenamark2 benchmark                                                                       | 750mA                             | Performance governor, HDMI is on, usb, sata, wifi and Ethernet are off                                 |
| Full load – Android Nenamark2 benchmark + 4 processors running 100% (dd command memory to memory) | 1190mA                            | Performance governor, HDMI is on, USB, eSata, WiFi and Ethernet is 1Gbps (note #1). Tj is 55c          |
| Full load – Android Nenamark2 benchmark + 4 processors running 100% (dd command memory to memory) | 1300mA                            | Performance governor, HDMI is on, usb, sata, wifi and Ethernet is 1Gbps (note #1). Tj is 87c (note #2) |
| Video 1080p Big Buck Bunny with AC3 audio codec (gstreamer from local SD)                         | Varies between 340mA to 410mA     | Performance governor, HDMI is on, USB, eSata, WiFi and Ethernet are off                                |
| Linux idle                                                                                        | 170mA                             | <p>Performance governor, HDMI, USB,<br><br>eSata, WiFi and Ethernet are all off.</p>                   |
| Linux suspend to memory                                                                           | 30mA                              | Note #3                                                                                                |

_Figure 6 Typical Power Consumption: CuBox-i4pro_

Notes:

1. CuBox-i uses an LDO that provides 5V to 3.3V conversion that feeds the Ethernet PHY on the SOM. Due to that, the addition of 100mA on the 3.3V rail when PHY is set to 1Gbps, adds 100mA consumption on the 5.0V power rails.
2. Notice the power difference between the same workload while Tjunction of the die is 55c and 87c (\~110mA difference from the 5V power rail).

{% hint style="info" %}
It takes about 60 minutes to reach that stable 87c Tjunction.
{% endhint %}


1. This is using Linux suspend to memory when the front LED is off. This consumption is mainly due to DDR entering self-refresh (2GByte) and some consumption on the 3.3V LDO and leakage on the processor and SoC digital part rails.

#### imx6 SOM Power Consumption

| **Mode**                                                                            | **Voltage** | **Current** | **Power** |
| ----------------------------------------------------------------------------------- | ----------- | ----------- | --------- |
| Idle, Linux up                                                                      | 5V          | 220mA       | 1.1W      |
| Linux up, wifi connected to 2.4GHz and sending packet by iperf3                     | 5V          | 400mA       | 2W        |
| Linux up, scanning for bluetooth device                                             | 5V          | 230mA       | 1.15W     |
| Linux up, GPU stress by glmark2                                                     | 5V          | 650mA       | 3.25W     |
| Linux up, CPU stress to maximum                                                     | 5V          | 550mA       | 2.75W     |
| All utilities are active in the same time (Wifi, GPU stress, CPU stress, Bluetooth) | 5V          | 770mA       | 3.85W     |

#### **Maximum Rating**

Following are the maximum ratings on different power signals and power rails.

|                                                                                                               |                              |         |                            |          |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------- | -------------------------- | -------- |
| **Parameter Description**                                                                                     | **Symbol**                   | **Min** | **Max**                    | **Unit** |
| Supplies VDD\_SNVS\_IN and VDD\_HIGH\_IN on i.MX6 starting rev 1.2                                            | VSNVS\_3V0                   | 2.8     | 3.3                        | V        |
| eMMC/SD supply voltage                                                                                        | NVCC\_SD2 NVCC\_SD3          | 1.65    | 3.6                        | V        |
| Main 3.3v supply voltage for i.MX6, Ethernet phy and other                                                    | NVCC\_EIM0                   | 3.2     | 3.6                        | V        |
| USB OTG and H1 supply voltage                                                                                 | USB\_OTG\_VBUS USB\_H1\_VBUS | 4.4     | 5.25                       | V        |
| DC-DC supplies, HDMI I2C boost and WiFi/BT main supply (1)                                                    | VIN\_5V0                     | 3.2     | 6                          | V        |
| Supplies VDD\_SNVS\_IN and VDD\_HIGH\_IN on i.MX6                                                             | VSNVS\_3V0                   | –       | 250                        | mA       |
| Supplies i.MX6 (GPIO, Parallel display interface etc…), AR8030/AR8035 Ethernet phy, part of the AzureWave SiP | NVCC\_EIM0                   | –       | <p>300 (2)<br><br>(5)</p>  | mA       |
| SD2 I/O                                                                                                       | NVCC\_SD2                    | –       | 22 (3)                     | mA       |
| SD3 I/O                                                                                                       | NVCC\_SD3                    | –       | 40 (3)                     | mA       |
| Supplies all SR-SOM-MX6 power management devices.                                                             | VIN\_5V0                     | –       | <p>1500 (4)<br><br>(5)</p> | mA       |

{% hint style="warning" %}
HDMI I2C is voltage boosted using VIN\_5V0 power rail. Due to that VIN\_5V0 = 5V is recommended since HDMI EDID requires 5V voltage.
{% endhint %}


1. AR8035 Gigabit Ethernet PHY consumes 150mA out of those in a 100-meter cable configuration.
2. This is reduced to 150mA when the AR8035 is not active.
3. Assumes ultra-high speed: 1.8v, 100MHz clock rate and double data rate on data; 4-bit data on SD2 and 8-bit data on SD3.
4. Assumes VIN\_5V0 = 5v. When supplying less than 5V, the maximum current increases accordingly; it is recommended to add additional margins on current limit.

{% hint style="warning" %}
Notice that a common practice when integrating SR-SOM-MX6 is to have a single DC-DC, of 3.2v that supplies all the SR-SOM-MX6 supplies, except the USB\_OTG\_VBUS and USB\_HOST\_VBUS.
{% endhint %}


5\. SR-SOM-MX6 rev 1.5 incorporates TI WiLink8 based device vs. BCM4330. This adds 285mA on the NVCC\_EIM0 but remove 200mA requirement from VIN\_5V0.

## **Mechanical Description**

Following is a diagram of the TOP VIEW of the i.MX6 SOM:

![](../../../.gitbook/assets/image-20211226-093334.png)

Note the following details:

* The carrier board must use the same footprint as in the above mechanical

{% hint style="info" %}
Since this is a TOP VIEW of the print side of the SR-SOM-MX6, the diagram above describes the dimensions and placement of the board-to-board headers, mechanical holes and boundaries of the SR-SOM-MX6, as-is.
{% endhint %}


* J5002 is the main board-to-board header (bottom side in the diagram).
* J8004 is the second board-to-board header (upper side in the diagram).
* J5001 is the third board-to-board header (right side in the diagram).
* CuBox-i design does not use the mechanical holes, since the mating strength of two Hirose DF40 pairs and the internal heat spreader is satisfactory for the design requirements.
* In case 1.5mm mating height was chosen, then the SR-SOM-MX6 requirement would be that all area beneath it on the carrier will be all dedicated ONLY for the board-to-board connectivity; no other components are allowed. In case higher mating is chosen, then 1.5mm should be reserved for the SR-SOM-MX6. For instance, if 3.5mm mating height is chosen, then 1.5mm is dedicated to the SR-SOM-MX6 print side components and the remaining 2mm for the carrier components underneath the SR-SOM-MX6.

Refer to SolidRun HummingBoard and CuBox-i design and layout, where there are examples of the main and second 80 pin header board-to-board usage.

## Documentation

* [iMX6 SOM Heatsink.zip](../sbc-platform/attachments/iMX6%20SOM%20Heatsink.zip)
* [Diff between Rev 1.3 and Rev 1.5.pdf](../sbc-platform/attachments/Diff%20between%20Rev%201.3%20and%20Rev%201.5.pdf)
* [imx6-rev-1_5-simplified-schematics.pdf](../sbc-platform/attachments/imx6-rev-1_5-simplified-schematics.pdf)
* [sr-usom-mx6-3_b2b_connectors_locations.zip](../sbc-platform/attachments/sr-usom-mx6-3_b2b_connectors_locations.zip)
* [iMX6 SOM Mechanical files.zip](../sbc-platform/attachments/iMX6%20SOM%20Mechanical%20files.zip)
* [imx6 som MTBF.pdf](../sbc-platform/attachments/imx6%20som%20MTBF.pdf)
* [sr-usom-mx6-fusing.zip](../sbc-platform/attachments/sr-usom-mx6-fusing.zip)
* [i,MX6 SOM Heatsink 3D.STEP](../sbc-platform/attachments/i,MX6%20SOM%20Heatsink%203D.STEP)
* [imx6-som-rev-2.0-schematics.pdf](../sbc-platform/attachments/imx6-som-rev-2.0-schematics.pdf)



[Buy a Sample Now](https://shop.solid-run.com/?orderby=price\&filter_som-com-family=nxp-i-mx6&_ga=2.61323183.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
