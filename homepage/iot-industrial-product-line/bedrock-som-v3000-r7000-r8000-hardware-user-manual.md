# Bedrock SOM V3000 / R7000 / R8000 - Hardware User Manual

![](./attachments/e2I938HxMdmXcRQAR4ucFky9uCd0oRptWQZF0YSB2MlnNW-mYT01w0psTVjI5NzVNUx9fstX6Y1kLKyofj1Bs54UQf9IGHH2iuAyK9BihurDYtUzACJrPIX5aiB7mkex7cRojTIdiYwyyZEXGvhAB7E)

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 01 May 2024 | Firas Abd El Gani | 1.0 |     |
| Table of Contents | - [Introduction](#introduction)<br>  - [Bedrock SOM](#bedrock-som)<br>  - [NIO - Networking & I/O Extension Board](#nio-networking-i-o-extension-board)<br>  - [About this User Manual](#about-this-user-manual)<br>- [Bedrock SOM Block Diagram](#bedrock-som-block-diagram)<br>- [Mechanical Files](#mechanical-files)<br>- [Typical Block Diagram of a complete system](#typical-block-diagram-of-a-complete-system)<br>- [Bedrock Cartridge](#bedrock-cartridge)<br>- [SOM Board-to-Board Connectors - MFG P/N](#som-board-to-board-connectors-mfg-p-n)<br>- [Board-to-board Connectors Pin-out](#board-to-board-connectors-pin-out)<br>- [OrCad Symbols](#orcad-symbols)<br>- [Differential Signals Impedance](#differential-signals-impedance)<br>- [Thermal coupling](#thermal-coupling)<br>  - [First stage thermal coupling in cartridge](#first-stage-thermal-coupling-in-cartridge)<br>  - [2nd stage thermal coupling (heatplate, NVME, RAM, cartridge)](#2nd-stage-thermal-coupling-heatplate-nvme-ram-cartridge)<br>- [Power Consumption](#power-consumption)<br>- [Power Input](#power-input)<br>- [Flashing BIOS and MPS Power Controller (Soon)](#flashing-bios-and-mps-power-controller-soon) |     |     |

<a id="introduction"></a>

# **Introduction**

This user manual is intended to assist board-designers who consider developing a custom NIO for SolidRun Bedrock SOM.

<a id="bedrock-som"></a>

## Bedrock SOM

Bedrock SOM is a system-on-module based on AMD Ryzen Embedded / Mobile processors with FP7R2 footprint. It is a compact self-contained computer system with processing, RAM, storage, power regulation and cooling. It brings out only the native I/O of the processor through high density board-to-board connectors to allow highly-modular system design with a high-degree of system customization by extension boards.

Currently Bedrock SOM is offered with several Ryzen variants including

- [Ryzen Embedded V3000 series](https://www.amd.com/en/products/embedded/ryzen/ryzen-v3000-series.html)
- [Ryzen Embedded 8000 series (“Hawk Point”)](https://www.amd.com/en/products/embedded/ryzen/ryzen-8000-series.html)
- [Ryzen 7000 series (“Phoenix”)](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7840u.html)

To learn about the unique properties of each processor please review the corresponding [Bedrock PC documentation](https://www.solid-run.com/industrial-computers/).

<a id="nio-networking-i-o-extension-board"></a>

## NIO - Networking & I/O Extension Board

NIO stands for Networking & I/O. NIO extension board is connected directly to Bedrock SOM.

SolidRun offers several types of NIO boards. NIO design files are offered as reference for board-designers who considering developing custom NIO boards.

<a id="about-this-user-manual"></a>

## About this User Manual

This manual will guide you through the key aspects of integrating Bedrock SOM into your custom NIO design. It covers essential design considerations, including power requirements, signal integrity, thermal management, and connectivity options, ensuring you can fully harness the power of the AMD Ryzen™ processor in your specific application.

Each section of this manual provides detailed information and technical specifications to help you understand the interfaces, pinouts, and schematic design principles necessary for successful integration. Additionally, we provide best practices and expert tips to mitigate common design challenges and optimize your development process.

<a id="bedrock-som-block-diagram"></a>

# **Bedrock SOM Block Diagram**

![image-20240523-104242.png](./attachments/image-20240523-104242.png)

> [!NOTE]
> Please note that Port 9 (Lanes: 17-20) are used for the SoM’s Internal NVME.

Feature Summary:

- Memory: DDR5 Dual 64BG Channels, Support Up to DDR5-5600.
- USB:  
2x USB4 (40 Gbps) - Supports USB-C Alt-Mode.  
2x USB 3.2 Gen2 (10 Gbps).  
4x USB2.0
- Display:  
• DisplayPort 0 (DP0) : eDP/DP/HDMI  
• DisplayPort 1 (DP1) : eDP/DP/HDMI  
• DisplayPort 2 (DP2, USBC0) : DP/HDMI; or USB-C with DP alt mode; or USB4  
• DisplayPort 3 (DP3, USBC1) : DP/HDMI; or USB-C with DP alt mode; or USB4  
• DisplayPort 4 (DP4, USBC4) : DP/HDMI; or USB-C with DP alt mode  
Note: Maximum 4 displays can be outputted simultaneously.
- PCIe: 9 ports, 16 Lanes PCIe Gen 4.
- Power: DC 12V-24V.
- Dimentions (83 mm x 91 mm x 12.7 mm) - Including SODIMM Modules.
- UART: 4 Ports.
- SPI: Yes.
- eSPI: Yes.
- I2C: 2 Ports.
- BIOS: AMI Aptio V

<a id="mechanical-files"></a>

# **Mechanical Files**

SoM Board Dimensions: 83 x 75.76 mm (Top View):

![](./attachments/lFOnTdbvfWJrIdtKj-x6Tnb2h5uEIZjNXp9GZl1vh3IYMB-iOnVP511JVqqF8KrDLX4jI3gmeC9nm_ze7sTFhuXLeTpH7iS4KzQtWHWcwjq3AzqflhAjqAwMc2CKF8acYKCU7Km6H0PrzwmPleDNyOU)

Mechanical Files Download Link:  
[Bedrock SOM - Mechanical Files.zip](https://drive.google.com/file/d/1x6WCio1rlT2fanu_FUwZUYKD36Y2fDIM/view?usp=sharing)

<a id="typical-block-diagram-of-a-complete-system"></a>

# **Typical Block Diagram of a complete system**

![](./attachments/9-3scmofEZyiAROu_OZ3UtOJZACxxmRJewHw9TG03bXGIsoT46i476oNv6HrBYG2z8XWufvWf8NPOJHW4tWtVhnzHNYm1MIHZpXxuRvSYnJ1DmzT1k1naINzyvVGE7ytSapV90TZCgcMQDE3Y3RCO3o)

<a id="bedrock-cartridge"></a>

# **Bedrock Cartridge**

As part of developing a custom extension board for the Bedrock SOM, it’s recommended to use [Bedrock Cartridge](https://solidrun.atlassian.net/wiki/spaces/developer/pages/634454119/Bedrock+Cartridge+SoM+3D+model).

Bedrock Cartridge provides the following:

- Highly effective 1st stage thermal coupling (TIM0) to the Ryzen die to a copper heatplate.  
Coupling the heatplate to a heatsink/cold-plate is easy. Coupling the die is challenging.
- Provision for mounting NIO securely with accurate spacing.
- Easy mounting of SOM to enclosure / heatsink / cold-plate.
- Thermal coupling for SOM’s DC-to-DC converters
- Mounting of NVME SSD  
Not present on SOM itself
- Securing and thermal coupling for SODIMMs
- RTC battery compartment
- Physical protection and rigidity to the SOM
- Rigid chassis for the Bedrock Deck with multiple threaded mounting holes

![](./attachments/ChlqefgmxN68Xjj7MEKfkkDTsjjKOm--f20j0t1gI2JXvz7ONQnyR6kzotxZmqpPPrLI7nYoHt1iVVTulAbYS2A1Gf9gjzFvMXGjlGMUT3AfdZzdZmRh-bax_bnGJ0Sn7ksgRIDfnpnZD6ubdVXKT_w)

<a id="som-board-to-board-connectors-mfg-p-n"></a>

# **SOM Board-to-Board Connectors - MFG P/N**

| Connector RefDes on<br><br>Bedrock SoM | MFG P/N | Connector RefDes on<br><br>NIO | MFG P/N |
| --- | --- | --- | --- |
| J1  | DF40C-100D**P**\-0.4V(51) | J5  | DF40C-100D**S**\-0.4V(51) |
| J2  | DF40C-100D**P**\-0.4V(51) | J6  | DF40C-100D**S**\-0.4V(51) |
| J3  | DF40C-100D**P**\-0.4V(51) | J4  | DF40C-100D**S**\-0.4V(51) |
| J4  | DF40C-80D**P**\-0.4V(51) | J7  | DF40C-80D**S**\-0.4V(51) |

Bedrock SoM Connectors (Males):

![](./attachments/ZgncuI2R5bTgyxBKRCtxSAJrlJXRnC86-UWlh456bAGt_IutGNx_JuQYLmTR_PbG2aAeiFvupY9aD-ZweaYdMpQ9trlWf2VRENU2N7y8X1e8Dhct9QgtAYkQuCA_2HU0KoOuWoI7MchG74qAv5Vv4zw)

NIO Connectors (Females):

![](./attachments/JXWIxruhWqtKhLeylcTp7jPHNE0l9X23_e4eQbm3niMbykBhnb0UFO37XfIt54higRVDx2qXSkAhU0PuPu7DBVlf6qr2azXCGwrke52ufPdNYIOE12sysoiQ3bjL5CmQlzYsjYh_ekvWm8Qd_CFZutM)

Note: Top Side of SoM is placed on Top Side of NIO, where the two boards are flipped one towards the other.

<a id="board-to-board-connectors-pin-out"></a>

# **Board-to-board Connectors Pin-out**

The following is an example of the B2B pinout in NIO.  
Please note that the pinout relates to the *female* connectors on a carrier, **to which the Bedrock SoM male Connectors are inserted**, and here we gave an example for SolidRun NIO Connectors (J4, J5, J6, J7). It’s important to be careful which pin is number #1.

![](./attachments/mJ_FRFaGzvYwRC37nPP_-etZhV9YeV4FA1I-9DfzPd9MaLI1psMy26Dwo2dTPyfoo18CNFEWcteBwYHP7xtFx5PyIiNTi9fpst9sAovKsMp-E7-KrzsI0nrc0W4Isdd5k5xrpf-x9OTg0jwSdKy_jws)

<a id="nio-r7000-basic-pinout"></a>

### NIO R7000 Basic pinout

| <a id="j5"></a><br><br>##### J5 | <a id="pin"></a><br><br>##### Pin# | <a id="j6"></a><br><br>##### J6 | <a id="pin"></a><br><br>##### Pin# | <a id="j4"></a><br><br>##### J4 | <a id="pin"></a><br><br>##### Pin# | <a id="j7"></a><br><br>##### J7 | <a id="pin"></a><br><br>##### Pin# |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <a id="vddbt_rtc"></a><br><br>##### VDDBT\_RTC | <a id="j5-93"></a><br><br>##### J5-93 | <a id="dp3_auxn-usbc1_sbtx"></a><br><br>##### DP3\_AUXN/USBC1\_SBTX | <a id="j6-62"></a><br><br>##### J6-62 | <a id="dp2_hpd"></a><br><br>##### DP2\_HPD | <a id="j4-79"></a><br><br>##### J4-79 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-64"></a><br><br>##### J7-64 |
| <a id="48m_osc"></a><br><br>##### 48M\_OSC | <a id="j5-77"></a><br><br>##### J5-77 | <a id="dp3_auxp-usbc1_sbrx"></a><br><br>##### DP3\_AUXP/USBC1\_SBRX | <a id="j6-60"></a><br><br>##### J6-60 | <a id="dp3_hpd"></a><br><br>##### DP3\_HPD | <a id="j4-85"></a><br><br>##### J4-85 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-72"></a><br><br>##### J7-72 |
| <a id="acp_wov_dmic_clk"></a><br><br>##### ACP\_WOV\_DMIC\_CLK | <a id="j5-91"></a><br><br>##### J5-91 | <a id="gfx_clkn_r"></a><br><br>##### GFX\_CLKN\_R | <a id="j6-23"></a><br><br>##### J6-23 | <a id="dp4_auxn"></a><br><br>##### DP4\_AUXN | <a id="j4-81"></a><br><br>##### J4-81 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-80"></a><br><br>##### J7-80 |
| <a id="acp_wov_dmic_dat0"></a><br><br>##### ACP\_WOV\_DMIC\_DAT0 | <a id="j5-95"></a><br><br>##### J5-95 | <a id="gfx_clkp_r"></a><br><br>##### GFX\_CLKP\_R | <a id="j6-25"></a><br><br>##### J6-25 | <a id="dp4_auxp"></a><br><br>##### DP4\_AUXP | <a id="j4-83"></a><br><br>##### J4-83 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-69"></a><br><br>##### J7-69 |
| <a id="ac_pres"></a><br><br>##### AC\_PRES | <a id="j5-26"></a><br><br>##### J5-26 | <a id="gfx_slot_rx0n"></a><br><br>##### GFX\_SLOT\_RX0N | <a id="j6-53"></a><br><br>##### J6-53 | <a id="dp4_hpd"></a><br><br>##### DP4\_HPD | <a id="j4-87"></a><br><br>##### J4-87 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-77"></a><br><br>##### J7-77 |
| <a id="agpio11_mdio3_sda"></a><br><br>##### AGPIO11\_MDIO3\_SDA | <a id="j5-55"></a><br><br>##### J5-55 | <a id="gfx_slot_rx0p"></a><br><br>##### GFX\_SLOT\_RX0P | <a id="j6-55"></a><br><br>##### J6-55 | <a id="usbc0_dn"></a><br><br>##### USBC0\_DN | <a id="j4-48"></a><br><br>##### J4-48 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-66"></a><br><br>##### J7-66 |
| <a id="agpio17"></a><br><br>##### AGPIO17 | <a id="j5-86"></a><br><br>##### J5-86 | <a id="gfx_slot_rx1n"></a><br><br>##### GFX\_SLOT\_RX1N | <a id="j6-59"></a><br><br>##### J6-59 | <a id="usbc0_dp"></a><br><br>##### USBC0\_DP | <a id="j4-46"></a><br><br>##### J4-46 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-74"></a><br><br>##### J7-74 |
| <a id="agpio18"></a><br><br>##### AGPIO18 | <a id="j5-78"></a><br><br>##### J5-78 | <a id="gfx_slot_rx1p"></a><br><br>##### GFX\_SLOT\_RX1P | <a id="j6-61"></a><br><br>##### J6-61 | <a id="usbc0_nova_rxan"></a><br><br>##### USBC0\_NOVA\_RXAN | <a id="j4-40"></a><br><br>##### J4-40 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-63"></a><br><br>##### J7-63 |
| <a id="agpio21"></a><br><br>##### AGPIO21 | <a id="j5-1"></a><br><br>##### J5-1 | <a id="gfx_slot_rx2n"></a><br><br>##### GFX\_SLOT\_RX2N | <a id="j6-65"></a><br><br>##### J6-65 | <a id="usbc0_nova_rxap"></a><br><br>##### USBC0\_NOVA\_RXAP | <a id="j4-42"></a><br><br>##### J4-42 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-71"></a><br><br>##### J7-71 |
| <a id="agpio22"></a><br><br>##### AGPIO22 | <a id="j5-34"></a><br><br>##### J5-34 | <a id="gfx_slot_rx2p"></a><br><br>##### GFX\_SLOT\_RX2P | <a id="j6-67"></a><br><br>##### J6-67 | <a id="usbc0_nova_rxbn"></a><br><br>##### USBC0\_NOVA\_RXBN | <a id="j4-52"></a><br><br>##### J4-52 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-79"></a><br><br>##### J7-79 |
| <a id="agpio24"></a><br><br>##### AGPIO24 | <a id="j5-58"></a><br><br>##### J5-58 | <a id="gfx_slot_rx3n"></a><br><br>##### GFX\_SLOT\_RX3N | <a id="j6-71"></a><br><br>##### J6-71 | <a id="usbc0_nova_rxbp"></a><br><br>##### USBC0\_NOVA\_RXBP | <a id="j4-54"></a><br><br>##### J4-54 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-68"></a><br><br>##### J7-68 |
| <a id="agpio3"></a><br><br>##### AGPIO3 | <a id="j5-53"></a><br><br>##### J5-53 | <a id="gfx_slot_rx3p"></a><br><br>##### GFX\_SLOT\_RX3P | <a id="j6-73"></a><br><br>##### J6-73 | <a id="usbc0_nova_txan"></a><br><br>##### USBC0\_NOVA\_TXAN | <a id="j4-47"></a><br><br>##### J4-47 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-76"></a><br><br>##### J7-76 |
| <a id="agpio32"></a><br><br>##### AGPIO32 | <a id="j5-83"></a><br><br>##### J5-83 | <a id="gfx_slot_rx4n"></a><br><br>##### GFX\_SLOT\_RX4N | <a id="j6-77"></a><br><br>##### J6-77 | <a id="usbc0_nova_txap"></a><br><br>##### USBC0\_NOVA\_TXAP | <a id="j4-45"></a><br><br>##### J4-45 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-65"></a><br><br>##### J7-65 |
| <a id="agpio4"></a><br><br>##### AGPIO4 | <a id="j5-28"></a><br><br>##### J5-28 | <a id="gfx_slot_rx4p"></a><br><br>##### GFX\_SLOT\_RX4P | <a id="j6-79"></a><br><br>##### J6-79 | <a id="usbc0_nova_txbn"></a><br><br>##### USBC0\_NOVA\_TXBN | <a id="j4-51"></a><br><br>##### J4-51 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-73"></a><br><br>##### J7-73 |
| <a id="agpio89"></a><br><br>##### AGPIO89 | <a id="j5-43"></a><br><br>##### J5-43 | <a id="gfx_slot_rx5n"></a><br><br>##### GFX\_SLOT\_RX5N | <a id="j6-83"></a><br><br>##### J6-83 | <a id="usbc0_nova_txbp"></a><br><br>##### USBC0\_NOVA\_TXBP | <a id="j4-53"></a><br><br>##### J4-53 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-70"></a><br><br>##### J7-70 |
| <a id="agpio90"></a><br><br>##### AGPIO90 | <a id="j5-21"></a><br><br>##### J5-21 | <a id="gfx_slot_rx5p"></a><br><br>##### GFX\_SLOT\_RX5P | <a id="j6-85"></a><br><br>##### J6-85 | <a id="usbc1_dn"></a><br><br>##### USBC1\_DN | <a id="j4-66"></a><br><br>##### J4-66 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-78"></a><br><br>##### J7-78 |
| <a id="apu_alert"></a><br><br>##### APU\_ALERT# | <a id="j5-72"></a><br><br>##### J5-72 | <a id="gfx_slot_rx6n"></a><br><br>##### GFX\_SLOT\_RX6N | <a id="j6-89"></a><br><br>##### J6-89 | <a id="usbc1_dp"></a><br><br>##### USBC1\_DP | <a id="j4-64"></a><br><br>##### J4-64 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-67"></a><br><br>##### J7-67 |
| <a id="apu_i2c0_scl_1v8"></a><br><br>##### APU\_I2C0\_SCL\_1V8 | <a id="j5-11"></a><br><br>##### J5-11 | <a id="gfx_slot_rx6p"></a><br><br>##### GFX\_SLOT\_RX6P | <a id="j6-91"></a><br><br>##### J6-91 | <a id="usbc1_rxan"></a><br><br>##### USBC1\_RXAN | <a id="j4-60"></a><br><br>##### J4-60 | <a id="vin_alw"></a><br><br>##### VIN\_ALW | <a id="j7-75"></a><br><br>##### J7-75 |
| <a id="apu_i2c0_sda_1v8"></a><br><br>##### APU\_I2C0\_SDA\_1V8 | <a id="j5-9"></a><br><br>##### J5-9 | <a id="gfx_slot_rx7n"></a><br><br>##### GFX\_SLOT\_RX7N | <a id="j6-95"></a><br><br>##### J6-95 | <a id="usbc1_rxap"></a><br><br>##### USBC1\_RXAP | <a id="j4-58"></a><br><br>##### J4-58 | <a id="acp_wov_dmic_dat1"></a><br><br>##### ACP\_WOV\_DMIC\_DAT1 | <a id="j7-48"></a><br><br>##### J7-48 |
| <a id="apu_i2c1_scl_1v8"></a><br><br>##### APU\_I2C1\_SCL\_1V8 | <a id="j5-13"></a><br><br>##### J5-13 | <a id="gfx_slot_rx7p"></a><br><br>##### GFX\_SLOT\_RX7P | <a id="j6-97"></a><br><br>##### J6-97 | <a id="usbc1_rxbn"></a><br><br>##### USBC1\_RXBN | <a id="j4-72"></a><br><br>##### J4-72 | <a id="acp_wov_dmic_dat2"></a><br><br>##### ACP\_WOV\_DMIC\_DAT2 | <a id="j7-42"></a><br><br>##### J7-42 |
| <a id="apu_i2c1_sda_1v8"></a><br><br>##### APU\_I2C1\_SDA\_1V8 | <a id="j5-27"></a><br><br>##### J5-27 | <a id="gfx_slot_tx0n_c"></a><br><br>##### GFX\_SLOT\_TX0N\_C | <a id="j6-6"></a><br><br>##### J6-6 | <a id="usbc1_rxbp"></a><br><br>##### USBC1\_RXBP | <a id="j4-70"></a><br><br>##### J4-70 | <a id="acp_wov_dmic_dat3"></a><br><br>##### ACP\_WOV\_DMIC\_DAT3 | <a id="j7-56"></a><br><br>##### J7-56 |
| <a id="apu_prochot"></a><br><br>##### APU\_PROCHOT# | <a id="j5-81"></a><br><br>##### J5-81 | <a id="gfx_slot_tx0p_c"></a><br><br>##### GFX\_SLOT\_TX0P\_C | <a id="j6-8"></a><br><br>##### J6-8 | <a id="usbc1_txan"></a><br><br>##### USBC1\_TXAN | <a id="j4-57"></a><br><br>##### J4-57 | <a id="az_bitlk-sw1_mclk-tdm0_bclk_hdr"></a><br><br>##### AZ\_BITLK/SW1\_MCLK/TDM0\_BCLK\_HDR | <a id="j7-44"></a><br><br>##### J7-44 |
| <a id="apu_rst"></a><br><br>##### APU\_RST# | <a id="j5-74"></a><br><br>##### J5-74 | <a id="gfx_slot_tx1n_c"></a><br><br>##### GFX\_SLOT\_TX1N\_C | <a id="j6-18"></a><br><br>##### J6-18 | <a id="usbc1_txap"></a><br><br>##### USBC1\_TXAP | <a id="j4-59"></a><br><br>##### J4-59 | <a id="conf_4"></a><br><br>##### CONF\_4 | <a id="j7-36"></a><br><br>##### J7-36 |
| <a id="apu_sclk0_1v8"></a><br><br>##### APU\_SCLK0\_1V8 | <a id="j5-19"></a><br><br>##### J5-19 | <a id="gfx_slot_tx1p_c"></a><br><br>##### GFX\_SLOT\_TX1P\_C | <a id="j6-20"></a><br><br>##### J6-20 | <a id="usbc1_txbn"></a><br><br>##### USBC1\_TXBN | <a id="j4-63"></a><br><br>##### J4-63 | <a id="conf_5"></a><br><br>##### CONF\_5 | <a id="j7-6"></a><br><br>##### J7-6 |
| <a id="apu_sclk1_1v8"></a><br><br>##### APU\_SCLK1\_1V8 | <a id="j5-37"></a><br><br>##### J5-37 | <a id="gfx_slot_tx2n_c"></a><br><br>##### GFX\_SLOT\_TX2N\_C | <a id="j6-30"></a><br><br>##### J6-30 | <a id="usbc1_txbp"></a><br><br>##### USBC1\_TXBP | <a id="j4-65"></a><br><br>##### J4-65 | <a id="dout_bt_hdr"></a><br><br>##### DOUT\_BT\_HDR | <a id="j7-52"></a><br><br>##### J7-52 |
| <a id="apu_sdata0_1v8"></a><br><br>##### APU\_SDATA0\_1V8 | <a id="j5-17"></a><br><br>##### J5-17 | <a id="gfx_slot_tx2p_c"></a><br><br>##### GFX\_SLOT\_TX2P\_C | <a id="j6-32"></a><br><br>##### J6-32 | <a id="usbc4_dn"></a><br><br>##### USBC4\_DN | <a id="j4-92"></a><br><br>##### J4-92 | <a id="gpp_clk5n_r"></a><br><br>##### GPP\_CLK5N\_R | <a id="j7-41"></a><br><br>##### J7-41 |
| <a id="apu_sdata1_1v8"></a><br><br>##### APU\_SDATA1\_1V8 | <a id="j5-39"></a><br><br>##### J5-39 | <a id="gfx_slot_tx3n_c"></a><br><br>##### GFX\_SLOT\_TX3N\_C | <a id="j6-42"></a><br><br>##### J6-42 | <a id="usbc4_dp"></a><br><br>##### USBC4\_DP | <a id="j4-90"></a><br><br>##### J4-90 | <a id="gpp_clk5p_r"></a><br><br>##### GPP\_CLK5P\_R | <a id="j7-39"></a><br><br>##### J7-39 |
| <a id="apu_sfh_scl"></a><br><br>##### APU\_SFH\_SCL | <a id="j5-67"></a><br><br>##### J5-67 | <a id="gfx_slot_tx3p_c"></a><br><br>##### GFX\_SLOT\_TX3P\_C | <a id="j6-44"></a><br><br>##### J6-44 | <a id="usbc4_ss_rxan"></a><br><br>##### USBC4\_SS+\_RXAN | <a id="j4-86"></a><br><br>##### J4-86 | <a id="gpp_clk6n_r"></a><br><br>##### GPP\_CLK6N\_R | <a id="j7-45"></a><br><br>##### J7-45 |
| <a id="apu_sfh_sda"></a><br><br>##### APU\_SFH\_SDA | <a id="j5-38"></a><br><br>##### J5-38 | <a id="gfx_slot_tx4n"></a><br><br>##### GFX\_SLOT\_TX4N | <a id="j6-54"></a><br><br>##### J6-54 | <a id="usbc4_ss_rxap"></a><br><br>##### USBC4\_SS+\_RXAP | <a id="j4-84"></a><br><br>##### J4-84 | <a id="gpp_clk6p_r"></a><br><br>##### GPP\_CLK6P\_R | <a id="j7-47"></a><br><br>##### J7-47 |
| <a id="apu_sic"></a><br><br>##### APU\_SIC | <a id="j5-82"></a><br><br>##### J5-82 | <a id="gfx_slot_tx4p"></a><br><br>##### GFX\_SLOT\_TX4P | <a id="j6-56"></a><br><br>##### J6-56 | <a id="usbc4_ss_rxbn"></a><br><br>##### USBC4\_SS+\_RXBN | <a id="j4-96"></a><br><br>##### J4-96 | <a id="gpp_rx10n"></a><br><br>##### GPP\_RX10N | <a id="j7-10"></a><br><br>##### J7-10 |
| <a id="apu_sid"></a><br><br>##### APU\_SID | <a id="j5-90"></a><br><br>##### J5-90 | <a id="gfx_slot_tx5n"></a><br><br>##### GFX\_SLOT\_TX5N | <a id="j6-66"></a><br><br>##### J6-66 | <a id="usbc4_ss_rxbp"></a><br><br>##### USBC4\_SS+\_RXBP | <a id="j4-98"></a><br><br>##### J4-98 | <a id="gpp_rx10p"></a><br><br>##### GPP\_RX10P | <a id="j7-12"></a><br><br>##### J7-12 |
| <a id="apu_thermtrip"></a><br><br>##### APU\_THERMTRIP# | <a id="j5-15"></a><br><br>##### J5-15 | <a id="gfx_slot_tx5p"></a><br><br>##### GFX\_SLOT\_TX5P | <a id="j6-68"></a><br><br>##### J6-68 | <a id="usbc4_ss_txan"></a><br><br>##### USBC4\_SS+\_TXAN | <a id="j4-69"></a><br><br>##### J4-69 | <a id="gpp_rx11n"></a><br><br>##### GPP\_RX11N | <a id="j7-33"></a><br><br>##### J7-33 |
| <a id="az_rst-sw0_mdata1-tdm0_din_hdr"></a><br><br>##### AZ\_RST#/SW0\_MDATA1/TDM0\_DIN\_HDR | <a id="j5-84"></a><br><br>##### J5-84 | <a id="gfx_slot_tx6n"></a><br><br>##### GFX\_SLOT\_TX6N | <a id="j6-78"></a><br><br>##### J6-78 | <a id="usbc4_ss_txap"></a><br><br>##### USBC4\_SS+\_TXAP | <a id="j4-71"></a><br><br>##### J4-71 | <a id="gpp_rx11p"></a><br><br>##### GPP\_RX11P | <a id="j7-35"></a><br><br>##### J7-35 |
| <a id="az_sdin0-sw0_mdata3_hdr"></a><br><br>##### AZ\_SDIN0/SW0\_MDATA3\_HDR | <a id="j5-64"></a><br><br>##### J5-64 | <a id="gfx_slot_tx6p"></a><br><br>##### GFX\_SLOT\_TX6P | <a id="j6-80"></a><br><br>##### J6-80 | <a id="usbc4_ss_txbn"></a><br><br>##### USBC4\_SS+\_TXBN | <a id="j4-75"></a><br><br>##### J4-75 | <a id="gpp_rx12n"></a><br><br>##### GPP\_RX12N | <a id="j7-5"></a><br><br>##### J7-5 |
| <a id="az_sdin1-sw0_mclk_tdm1_bclk_hdr"></a><br><br>##### AZ\_SDIN1/SW0\_MCLK\_TDM1\_BCLK\_HDR | <a id="j5-89"></a><br><br>##### J5-89 | <a id="gfx_slot_tx7n"></a><br><br>##### GFX\_SLOT\_TX7N | <a id="j6-90"></a><br><br>##### J6-90 | <a id="usbc4_ss_txbp"></a><br><br>##### USBC4\_SS+\_TXBP | <a id="j4-77"></a><br><br>##### J4-77 | <a id="gpp_rx12p"></a><br><br>##### GPP\_RX12P | <a id="j7-3"></a><br><br>##### J7-3 |
| <a id="az_sdin2-sw0_mdata0-tdm1_out_hdr"></a><br><br>##### AZ\_SDIN2/SW0\_MDATA0/TDM1\_OUT\_HDR | <a id="j5-66"></a><br><br>##### J5-66 | <a id="gfx_slot_tx7p"></a><br><br>##### GFX\_SLOT\_TX7P | <a id="j6-92"></a><br><br>##### J6-92 | <a id="usbn3"></a><br><br>##### USBN3 | <a id="j4-89"></a><br><br>##### J4-89 | <a id="gpp_tx10n"></a><br><br>##### GPP\_TX10N | <a id="j7-11"></a><br><br>##### J7-11 |
| <a id="az_sdout-sw0_mdata2-tdm0_dout_hdr"></a><br><br>##### AZ\_SDOUT/SW0\_MDATA2/TDM0\_DOUT\_HDR | <a id="j5-98"></a><br><br>##### J5-98 | <a id="gpp_clk1n_r"></a><br><br>##### GPP\_CLK1N\_R | <a id="j6-29"></a><br><br>##### J6-29 | <a id="usbn6"></a><br><br>##### USBN6 | <a id="j4-95"></a><br><br>##### J4-95 | <a id="gpp_tx10p"></a><br><br>##### GPP\_TX10P | <a id="j7-9"></a><br><br>##### J7-9 |
| <a id="az_sync-sw1_mdata0-tdm0_frm_hdr"></a><br><br>##### AZ\_SYNC/SW1\_MDATA0/TDM0\_FRM\_HDR | <a id="j5-100"></a><br><br>##### J5-100 | <a id="gpp_clk1p_r"></a><br><br>##### GPP\_CLK1P\_R | <a id="j6-31"></a><br><br>##### J6-31 | <a id="usbn7"></a><br><br>##### USBN7 | <a id="j4-99"></a><br><br>##### J4-99 | <a id="gpp_tx11n"></a><br><br>##### GPP\_TX11N | <a id="j7-17"></a><br><br>##### J7-17 |
| <a id="conf_1"></a><br><br>##### CONF\_1 | <a id="j5-92"></a><br><br>##### J5-92 | <a id="gpp_clk2n_r"></a><br><br>##### GPP\_CLK2N\_R | <a id="j6-35"></a><br><br>##### J6-35 | <a id="usbp3"></a><br><br>##### USBP3 | <a id="j4-91"></a><br><br>##### J4-91 | <a id="gpp_tx11p"></a><br><br>##### GPP\_TX11P | <a id="j7-15"></a><br><br>##### J7-15 |
| <a id="conf_2"></a><br><br>##### CONF\_2 | <a id="j5-61"></a><br><br>##### J5-61 | <a id="gpp_clk2p_r"></a><br><br>##### GPP\_CLK2P\_R | <a id="j6-37"></a><br><br>##### J6-37 | <a id="usbp6"></a><br><br>##### USBP6 | <a id="j4-93"></a><br><br>##### J4-93 | <a id="gpp_tx12n_c"></a><br><br>##### GPP\_TX12N\_C | <a id="j7-21"></a><br><br>##### J7-21 |
| <a id="conf_3"></a><br><br>##### CONF\_3 | <a id="j5-97"></a><br><br>##### J5-97 | <a id="gpp_clk3n_r"></a><br><br>##### GPP\_CLK3N\_R | <a id="j6-48"></a><br><br>##### J6-48 | <a id="usbp7"></a><br><br>##### USBP7 | <a id="j4-97"></a><br><br>##### J4-97 | <a id="gpp_tx12p_c"></a><br><br>##### GPP\_TX12P\_C | <a id="j7-23"></a><br><br>##### J7-23 |
| <a id="conf_6"></a><br><br>##### CONF\_6 | <a id="j5-85"></a><br><br>##### J5-85 | <a id="gpp_clk3p_r"></a><br><br>##### GPP\_CLK3P\_R | <a id="j6-50"></a><br><br>##### J6-50 | <a id="dp0_auxn"></a><br><br>##### DP0\_AUXN | <a id="j4-4"></a><br><br>##### J4-4 | <a id="int_clk_req3"></a><br><br>##### INT\_CLK\_REQ3# | <a id="j7-38"></a><br><br>##### J7-38 |
| <a id="dp_steresosync"></a><br><br>##### DP\_STERESOSYNC | <a id="j5-80"></a><br><br>##### J5-80 | <a id="gpp_rx13n"></a><br><br>##### GPP\_RX13N | <a id="j6-17"></a><br><br>##### J6-17 | <a id="dp0_auxp"></a><br><br>##### DP0\_AUXP | <a id="j4-6"></a><br><br>##### J4-6 | <a id="lrclk_bt_hdr"></a><br><br>##### LRCLK\_BT\_HDR | <a id="j7-54"></a><br><br>##### J7-54 |
| <a id="egpio67"></a><br><br>##### EGPIO67 | <a id="j5-3"></a><br><br>##### J5-3 | <a id="gpp_rx13p"></a><br><br>##### GPP\_RX13P | <a id="j6-19"></a><br><br>##### J6-19 | <a id="dp0_blon"></a><br><br>##### DP0\_BLON | <a id="j4-35"></a><br><br>##### J4-35 | <a id="rtc_clk2_r"></a><br><br>##### RTC\_CLK2\_R | <a id="j7-40"></a><br><br>##### J7-40 |
| <a id="egpio74"></a><br><br>##### EGPIO74 | <a id="j5-7"></a><br><br>##### J5-7 | <a id="gpp_rx14n"></a><br><br>##### GPP\_RX14N | <a id="j6-11"></a><br><br>##### J6-11 | <a id="dp0_blpwm"></a><br><br>##### DP0\_BLPWM | <a id="j4-39"></a><br><br>##### J4-39 | <a id="sdin_bt_hdr"></a><br><br>##### SDIN\_BT\_HDR | <a id="j7-50"></a><br><br>##### J7-50 |
| <a id="egpio76"></a><br><br>##### EGPIO76 | <a id="j5-5"></a><br><br>##### J5-5 | <a id="gpp_rx14p"></a><br><br>##### GPP\_RX14P | <a id="j6-13"></a><br><br>##### J6-13 | <a id="dp0_digon"></a><br><br>##### DP0\_DIGON | <a id="j4-37"></a><br><br>##### J4-37 | <a id="uart4_cts"></a><br><br>##### UART4\_CTS# | <a id="j7-4"></a><br><br>##### J7-4 |
| <a id="egpio78"></a><br><br>##### EGPIO78 | <a id="j5-35"></a><br><br>##### J5-35 | <a id="gpp_rx15n"></a><br><br>##### GPP\_RX15N | <a id="j6-5"></a><br><br>##### J6-5 | <a id="dp0_hpd"></a><br><br>##### DP0\_HPD | <a id="j4-33"></a><br><br>##### J4-33 | <a id="uart4_intr"></a><br><br>##### UART4\_INTR | <a id="j7-2"></a><br><br>##### J7-2 |
| <a id="egpio79"></a><br><br>##### EGPIO79 | <a id="j5-8"></a><br><br>##### J5-8 | <a id="gpp_rx15p"></a><br><br>##### GPP\_RX15P | <a id="j6-7"></a><br><br>##### J6-7 | <a id="dp0_tx0n"></a><br><br>##### DP0\_TX0N | <a id="j4-10"></a><br><br>##### J4-10 | <a id="uart4_txd"></a><br><br>##### UART4\_TXD | <a id="j7-34"></a><br><br>##### J7-34 |
| <a id="espi_clk_ec"></a><br><br>##### ESPI\_CLK\_EC | <a id="j5-6"></a><br><br>##### J5-6 | <a id="gpp_rx8n"></a><br><br>##### GPP\_RX8N | <a id="j6-47"></a><br><br>##### J6-47 | <a id="dp0_tx0p"></a><br><br>##### DP0\_TX0P | <a id="j4-12"></a><br><br>##### J4-12 | <a id="usb5_ss_rxn"></a><br><br>##### USB5\_SS+\_RXN | <a id="j7-24"></a><br><br>##### J7-24 |
| <a id="espi_dat0_ec"></a><br><br>##### ESPI\_DAT0\_EC | <a id="j5-22"></a><br><br>##### J5-22 | <a id="gpp_rx8p"></a><br><br>##### GPP\_RX8P | <a id="j6-49"></a><br><br>##### J6-49 | <a id="dp0_tx1n"></a><br><br>##### DP0\_TX1N | <a id="j4-18"></a><br><br>##### J4-18 | <a id="usb5_ss_rxp"></a><br><br>##### USB5\_SS+\_RXP | <a id="j7-22"></a><br><br>##### J7-22 |
| <a id="espi_dat1_ec"></a><br><br>##### ESPI\_DAT1\_EC | <a id="j5-14"></a><br><br>##### J5-14 | <a id="gpp_rx9n"></a><br><br>##### GPP\_RX9N | <a id="j6-41"></a><br><br>##### J6-41 | <a id="dp0_tx1p"></a><br><br>##### DP0\_TX1P | <a id="j4-16"></a><br><br>##### J4-16 | <a id="usb5_ss_txn"></a><br><br>##### USB5\_SS+\_TXN | <a id="j7-16"></a><br><br>##### J7-16 |
| <a id="espi_dat2_ec"></a><br><br>##### ESPI\_DAT2\_EC | <a id="j5-18"></a><br><br>##### J5-18 | <a id="gpp_rx9p"></a><br><br>##### GPP\_RX9P | <a id="j6-43"></a><br><br>##### J6-43 | <a id="dp0_tx2n"></a><br><br>##### DP0\_TX2N | <a id="j4-24"></a><br><br>##### J4-24 | <a id="usb5_ss_txp"></a><br><br>##### USB5\_SS+\_TXP | <a id="j7-18"></a><br><br>##### J7-18 |
| <a id="espi_dat3_ec"></a><br><br>##### ESPI\_DAT3\_EC | <a id="j5-20"></a><br><br>##### J5-20 | <a id="gpp_tx13n_c"></a><br><br>##### GPP\_TX13N\_C | <a id="j6-36"></a><br><br>##### J6-36 | <a id="dp0_tx2p"></a><br><br>##### DP0\_TX2P | <a id="j4-22"></a><br><br>##### J4-22 | <a id="usbc5_rx2n"></a><br><br>##### USBC5\_RX2N | <a id="j7-57"></a><br><br>##### J7-57 |
| <a id="fanout0_1v8"></a><br><br>##### FANOUT0\_1V8 | <a id="j5-47"></a><br><br>##### J5-47 | <a id="gpp_tx13p_c"></a><br><br>##### GPP\_TX13P\_C | <a id="j6-38"></a><br><br>##### J6-38 | <a id="dp0_tx3n"></a><br><br>##### DP0\_TX3N | <a id="j4-28"></a><br><br>##### J4-28 | <a id="usbc5_rx2p"></a><br><br>##### USBC5\_RX2P | <a id="j7-59"></a><br><br>##### J7-59 |
| <a id="fantach0_1v8"></a><br><br>##### FANTACH0\_1V8 | <a id="j5-45"></a><br><br>##### J5-45 | <a id="gpp_tx14n"></a><br><br>##### GPP\_TX14N | <a id="j6-24"></a><br><br>##### J6-24 | <a id="dp0_tx3p"></a><br><br>##### DP0\_TX3P | <a id="j4-30"></a><br><br>##### J4-30 | <a id="usbc5_tx2n"></a><br><br>##### USBC5\_TX2N | <a id="j7-29"></a><br><br>##### J7-29 |
| <a id="intruder_alert"></a><br><br>##### INTRUDER\_ALERT | <a id="j5-50"></a><br><br>##### J5-50 | <a id="gpp_tx14p"></a><br><br>##### GPP\_TX14P | <a id="j6-26"></a><br><br>##### J6-26 | <a id="dp1_auxn"></a><br><br>##### DP1\_AUXN | <a id="j4-9"></a><br><br>##### J4-9 | <a id="usbc5_tx2p"></a><br><br>##### USBC5\_TX2P | <a id="j7-27"></a><br><br>##### J7-27 |
| <a id="int_clk_req0"></a><br><br>##### INT\_CLK\_REQ0# | <a id="j5-46"></a><br><br>##### J5-46 | <a id="gpp_tx15n"></a><br><br>##### GPP\_TX15N | <a id="j6-12"></a><br><br>##### J6-12 | <a id="dp1_auxp"></a><br><br>##### DP1\_AUXP | <a id="j4-11"></a><br><br>##### J4-11 | <a id="usbn2"></a><br><br>##### USBN2 | <a id="j7-30"></a><br><br>##### J7-30 |
| <a id="int_clk_req1"></a><br><br>##### INT\_CLK\_REQ1# | <a id="j5-44"></a><br><br>##### J5-44 | <a id="gpp_tx15p"></a><br><br>##### GPP\_TX15P | <a id="j6-14"></a><br><br>##### J6-14 | <a id="dp1_blon"></a><br><br>##### DP1\_BLON | <a id="j4-76"></a><br><br>##### J4-76 | <a id="usbn5"></a><br><br>##### USBN5 | <a id="j7-53"></a><br><br>##### J7-53 |
| <a id="int_clk_req2"></a><br><br>##### INT\_CLK\_REQ2# | <a id="j5-42"></a><br><br>##### J5-42 | <a id="gpp_tx8n"></a><br><br>##### GPP\_TX8N | <a id="j6-96"></a><br><br>##### J6-96 | <a id="dp1_blpwm"></a><br><br>##### DP1\_BLPWM | <a id="j4-80"></a><br><br>##### J4-80 | <a id="usbn6"></a><br><br>##### USBN6 | <a id="j4-95"></a><br><br>##### J4-95 |
| <a id="int_sensor_0"></a><br><br>##### INT\_SENSOR\_0 | <a id="j5-36"></a><br><br>##### J5-36 | <a id="gpp_tx8p"></a><br><br>##### GPP\_TX8P | <a id="j6-98"></a><br><br>##### J6-98 | <a id="dp1_digon"></a><br><br>##### DP1\_DIGON | <a id="j4-78"></a><br><br>##### J4-78 | <a id="usbp2"></a><br><br>##### USBP2 | <a id="j7-28"></a><br><br>##### J7-28 |
| <a id="int_sensor_1"></a><br><br>##### INT\_SENSOR\_1 | <a id="j5-65"></a><br><br>##### J5-65 | <a id="gpp_tx9n"></a><br><br>##### GPP\_TX9N | <a id="j6-84"></a><br><br>##### J6-84 | <a id="dp1_hpd"></a><br><br>##### DP1\_HPD | <a id="j4-41"></a><br><br>##### J4-41 | <a id="usbp5"></a><br><br>##### USBP5 | <a id="j7-51"></a><br><br>##### J7-51 |
| <a id="kr10g_phy1_intr_1v8"></a><br><br>##### KR10G\_PHY1\_INTR#\_1V8 | <a id="j5-32"></a><br><br>##### J5-32 | <a id="gpp_tx9p"></a><br><br>##### GPP\_TX9P | <a id="j6-86"></a><br><br>##### J6-86 | <a id="dp1_tx0n"></a><br><br>##### DP1\_TX0N | <a id="j4-5"></a><br><br>##### J4-5 | <a id="33v_alw_som"></a><br><br>##### 3.3V\_ALW\_SOM | <a id="j7-58"></a><br><br>##### J7-58 |
| <a id="m2_ssd0_led"></a><br><br>##### M2\_SSD0\_LED# | <a id="j5-2"></a><br><br>##### J5-2 | <a id="som_enable"></a><br><br>##### SOM\_ENABLE | <a id="j6-74"></a><br><br>##### J6-74 | <a id="dp1_tx0p"></a><br><br>##### DP1\_TX0P | <a id="j4-3"></a><br><br>##### J4-3 | <a id="33v_alw_som"></a><br><br>##### 3.3V\_ALW\_SOM | <a id="j7-60"></a><br><br>##### J7-60 |
| <a id="mdio0_scl"></a><br><br>##### MDIO0\_SCL | <a id="j5-24"></a><br><br>##### J5-24 |     |     | <a id="dp1_tx1n"></a><br><br>##### DP1\_TX1N | <a id="j4-17"></a><br><br>##### J4-17 | <a id="33v_alw_som"></a><br><br>##### 3.3V\_ALW\_SOM | <a id="j7-62"></a><br><br>##### J7-62 |
| <a id="mdio0_sda"></a><br><br>##### MDIO0\_SDA | <a id="j5-10"></a><br><br>##### J5-10 |     |     | <a id="dp1_tx1p"></a><br><br>##### DP1\_TX1P | <a id="j4-15"></a><br><br>##### J4-15 |     |     |
| <a id="mdio1_scl"></a><br><br>##### MDIO1\_SCL | <a id="j5-40"></a><br><br>##### J5-40 |     |     | <a id="dp1_tx2n"></a><br><br>##### DP1\_TX2N | <a id="j4-23"></a><br><br>##### J4-23 |     |     |
| <a id="mdio1_sda"></a><br><br>##### MDIO1\_SDA | <a id="j5-59"></a><br><br>##### J5-59 |     |     | <a id="dp1_tx2p"></a><br><br>##### DP1\_TX2P | <a id="j4-21"></a><br><br>##### J4-21 |     |     |
| <a id="mdio2_scl"></a><br><br>##### MDIO2\_SCL | <a id="j5-68"></a><br><br>##### J5-68 |     |     | <a id="dp1_tx3n"></a><br><br>##### DP1\_TX3N | <a id="j4-29"></a><br><br>##### J4-29 |     |     |
| <a id="mpm_event"></a><br><br>##### MPM\_EVENT# | <a id="j5-33"></a><br><br>##### J5-33 |     |     | <a id="dp1_tx3p"></a><br><br>##### DP1\_TX3P | <a id="j4-27"></a><br><br>##### J4-27 |     |     |
| <a id="pcie_rst"></a><br><br>##### PCIE\_RST# | <a id="j5-79"></a><br><br>##### J5-79 |     |     | <a id="dp2_auxn-usbc0_sbtx"></a><br><br>##### DP2\_AUXN/USBC0\_SBTX | <a id="j4-36"></a><br><br>##### J4-36 |     |     |
| <a id="pcie_rst1"></a><br><br>##### PCIE\_RST1# | <a id="j5-31"></a><br><br>##### J5-31 |     |     | <a id="dp2_auxp-usbc0_sbrx"></a><br><br>##### DP2\_AUXP/USBC0\_SBRX | <a id="j4-34"></a><br><br>##### J4-34 |     |     |
| <a id="pcie_wake"></a><br><br>##### PCIE\_WAKE# | <a id="j5-49"></a><br><br>##### J5-49 |     |     | <a id="dp2_hpd"></a><br><br>##### DP2\_HPD | <a id="j4-79"></a><br><br>##### J4-79 |     |     |
| <a id="pwr_btn"></a><br><br>##### PWR\_BTN# | <a id="j5-51"></a><br><br>##### J5-51 |     |     | <a id="dp3_hpd"></a><br><br>##### DP3\_HPD | <a id="j4-85"></a><br><br>##### J4-85 |     |     |
| <a id="sata_act_18v"></a><br><br>##### SATA\_ACT\_1.8V# | <a id="j5-25"></a><br><br>##### J5-25 |     |     | <a id="dp4_auxn"></a><br><br>##### DP4\_AUXN | <a id="j4-81"></a><br><br>##### J4-81 |     |     |
| <a id="sensor_misc1"></a><br><br>##### SENSOR\_MISC1 | <a id="j5-57"></a><br><br>##### J5-57 |     |     | <a id="dp4_auxp"></a><br><br>##### DP4\_AUXP | <a id="j4-83"></a><br><br>##### J4-83 |     |     |
| <a id="sensor_misc2"></a><br><br>##### SENSOR\_MISC2 | <a id="j5-71"></a><br><br>##### J5-71 |     |     | <a id="dp4_hpd"></a><br><br>##### DP4\_HPD | <a id="j4-87"></a><br><br>##### J4-87 |     |     |
| <a id="sensor_misc3"></a><br><br>##### SENSOR\_MISC3 | <a id="j5-63"></a><br><br>##### J5-63 |     |     |     |     |     |     |
| <a id="sensor_misc4"></a><br><br>##### SENSOR\_MISC4 | <a id="j5-69"></a><br><br>##### J5-69 |     |     |     |     |     |     |
| <a id="sys_rst"></a><br><br>##### SYS\_RST# | <a id="j5-48"></a><br><br>##### J5-48 |     |     |     |     |     |     |
| <a id="sys_s0_pwr_en"></a><br><br>##### SYS\_S0\_PWR\_EN | <a id="j5-12"></a><br><br>##### J5-12 |     |     |     |     |     |     |
| <a id="sys_s3_pwr_en"></a><br><br>##### SYS\_S3\_PWR\_EN | <a id="j5-41"></a><br><br>##### J5-41 |     |     |     |     |     |     |
| <a id="tmon_i2c_scl"></a><br><br>##### TMON\_I2C\_SCL | <a id="j5-54"></a><br><br>##### J5-54 |     |     |     |     |     |     |
| <a id="tmon_i2c_sda"></a><br><br>##### TMON\_I2C\_SDA | <a id="j5-56"></a><br><br>##### J5-56 |     |     |     |     |     |     |
| <a id="tpad_int"></a><br><br>##### TPAD\_INT# | <a id="j5-23"></a><br><br>##### J5-23 |     |     |     |     |     |     |
| <a id="uart0_cts"></a><br><br>##### UART0\_CTS# | <a id="j5-99"></a><br><br>##### J5-99 |     |     |     |     |     |     |
| <a id="uart0_intr"></a><br><br>##### UART0\_INTR | <a id="j5-94"></a><br><br>##### J5-94 |     |     |     |     |     |     |
| <a id="uart0_rts"></a><br><br>##### UART0\_RTS# | <a id="j5-96"></a><br><br>##### J5-96 |     |     |     |     |     |     |
| <a id="uart0_rxd"></a><br><br>##### UART0\_RXD | <a id="j5-75"></a><br><br>##### J5-75 |     |     |     |     |     |     |
| <a id="uart0_txd"></a><br><br>##### UART0\_TXD | <a id="j5-73"></a><br><br>##### J5-73 |     |     |     |     |     |     |
| <a id="uart2_txd"></a><br><br>##### UART2\_TXD | <a id="j5-88"></a><br><br>##### J5-88 |     |     |     |     |     |     |
| <a id="usbc_i2c_scl"></a><br><br>##### USBC\_I2C\_SCL | <a id="j5-62"></a><br><br>##### J5-62 |     |     |     |     |     |     |
| <a id="usbc_i2c_sda"></a><br><br>##### USBC\_I2C\_SDA | <a id="j5-87"></a><br><br>##### J5-87 |     |     |     |     |     |     |
| <a id="usbc_pd_int"></a><br><br>##### USBC\_PD\_INT | <a id="j5-52"></a><br><br>##### J5-52 |     |     |     |     |     |     |
| <a id="usb_ocp"></a><br><br>##### USB\_OCP# | <a id="j5-60"></a><br><br>##### J5-60 |     |     |     |     |     |     |

<a id="orcad-symbols"></a>

# **OrCad Symbols**

In the following link you will find a PDF and OrCad Symbols for the NIO board-to-board connectors, to which the SoM (Male) Connectors are inserted: 

1. [**NIO BtB Connectors - PDF**](https://drive.google.com/file/d/1xB46dORFV3Gp8puEIqd73Do4I4A2uQde/view?usp=sharing)
2. [**NIO BtB Connectors - OrCad Symbols**](https://drive.google.com/file/d/1xFvehTro61wH1tTmV1JiQuoHRzARKDgt/view?usp=sharing)

<a id="differential-signals-impedance"></a>

# **Differential Signals Impedance**

[In this Excel](https://docs.google.com/spreadsheets/d/1FFL56p2GHO3JOiYYOMDi9Uce2WsCgf6ddNtgSrbaBDc/edit?usp=sharing), you will find a list for the impedance for each differential signal. 

Note: All differential pairs are 90-Ohm, the rest are GPIOs/Single-Ended signals which are 50-Ohm by default.

<a id="thermal-coupling"></a>

# **Thermal coupling**

<a id="first-stage-thermal-coupling-in-cartridge"></a>

## **First stage thermal coupling in cartridge**

The cartridge is assembled in the factory and should not be disassembled. It provides 1st stage cooling for the processor and power FETs.

<a id="2nd-stage-thermal-coupling-heatplate-nvme-ram-cartridge"></a>

## **2nd stage thermal coupling (heatplate, NVME, RAM, cartridge)**

- Thermal grease should be applied on heatplate. Heatplate should be attached to a cold plate.
- Thermal pad should be applied on NVME
- If device is intended to work at high ambient temperature it is advised to apply thermal gel between SODIMMs and RAM cover and thermal grease on top side of RAM cover
- The frame of the skirt is thermally coupled to the cold plate. Consider applying thermal paste on the frame of the skirt.

![Thermal_Grease2.png](./attachments/Thermal_Grease2.png)

<a id="power-consumption"></a>

# **Power Consumption**

<a id="smartshift-technology-for-optimized-power-management"></a>

### SmartShift Technology for Optimized Power Management

One of the key features of our System on Module, integrated with AMD Ryzen™ processors, is the SmartShift technology. This innovative feature allows for dynamic adjustment of power allocation between the CPU and other system components. By intelligently shifting power where it's needed most, SmartShift enhances overall performance and efficiency, making it an ideal solution for power-sensitive applications.

<a id="controlling-cpu-power-consumption"></a>

### Controlling CPU Power Consumption

With SmartShift, you can precisely control the power consumption of the CPU, tailoring it to fit the specific needs of your application. This capability is especially beneficial in scenarios where power efficiency is crucial, such as in portable or battery-operated devices. You can set a limit to the CPU power consumption, for example, capping it at a specific wattage to balance performance with power usage.

<a id="configuring-cpu-power-limits-in-bios"></a>

### Configuring CPU Power Limits in BIOS

To configure the CPU power limits, you can access the BIOS settings of our System on Module. We provide a detailed guide on how to navigate these settings and effectively set the desired power caps for your application.

For step-by-step instructions on accessing and modifying these settings, please visit our detailed BIOS configuration page here: [Bedrock V3000 BIOS Settings - Power Screen](https://solidrun.atlassian.net/wiki/spaces/developer/pages/464027649/Bedrock+V3000+BIOS+Settings#power-screen).

By leveraging the SmartShift technology and configuring your CPU power settings via BIOS, you can optimize your system’s performance and power consumption, leading to a more efficient and tailored usage according to your specific requirements. This section of the manual ensures that you have all the necessary tools and knowledge to take full advantage of the innovative features provided by our System on Module.

To demonstrate the efficacy and benefits of the SmartShift technology in our System on Module (SoM), extensive measurements have been conducted using a SoM based on the AMD Ryzen™ 7 7840HS processor paired with the Networking & I/O extension board (NIO). These tests were aimed at validating how effectively SmartShift manages power distribution under various operational conditions.

<a id="smartshift-configuration-parameters"></a>

### SmartShift Configuration Parameters:

The SmartShift feature is controlled through four key parameters in the BIOS Power tab, which allow for precise management of power distribution and consumption:

- **APU Only sPPT Limit**: Sets the peak power limit that the Accelerated Processing Unit (APU) can consume.
- **Sustained Power Limit**: Defines the sustained power threshold for long-term performance stability.
- **Fast PPT Limit**: Regulates the rapid power allowance for short bursts of intensive processing.
- **Slow PPT Limit**: Controls the lower power threshold, suitable for maintaining efficiency during less demanding tasks.

<a id="measurement-results"></a>

### Measurement Results

The following table illustrates the power consumption results (in Watts) observed under various settings of these parameters. These measurements provide clear insights into how SmartShift adjusts power usage dynamically, ensuring optimal performance and efficiency across different workloads and operational states.

The tests outlined in the table above were conducted while the system was running CineBench R23, specifically utilizing the Multi-Core test mode. This benchmarking tool is widely recognized for its ability to stress multiple CPU cores simultaneously, making it an ideal platform for evaluating the performance of the SmartShift technology under high computational loads. By conducting the tests in this environment, we ensure that the measurements accurately reflect the capabilities of SmartShift to dynamically manage and optimize power consumption during intensive processing tasks.

| **Setting Description** | **APU only sPPT Limit (mW)** | **Sustained PowerLimit (SPL) (mW)** | **Fast PPT limit**  <br>**(mW)** | **Slow PPT Limit**  <br>**(mW)** | **Scope Measurment \[Cinebench Multi\]: Total Power \[W\]** |
| --- | --- | --- | --- | --- | --- |
| **Energy Saving** | 5000 | 5000 | 5000 | 5000 | [14.7](https://drive.google.com/file/d/1g8dZm3DITwetPaUz2h37IoKcPkeZdlt7/view?usp=sharing) |
| 8000 | 8000 | 8000 | 8000 | [14.9](https://drive.google.com/file/d/1g8HxmO7Jc9lY5nxcKPzDloRKCjMnHGYj/view?usp=sharing) |
| 10000 | 10000 | 10000 | 10000 | [16.5](https://drive.google.com/file/d/1g7CzrXT89efIK49PYBxK29MfULcTM9Py/view?usp=sharing) |
| 20000 | 20000 | 20000 | 20000 | [25.1](https://drive.google.com/file/d/1g6HEnN4Z4QcZ3GFOz2mek2aZT8-6V9Ds/view?usp=sharing) |
| **Balanced Performance** | 30000 | 30000 | 30000 | 30000 | [37.5](https://drive.google.com/file/d/1g5gtqXmj1jZqR6BMNM-RMDGfanoHeekq/view?usp=sharing) |
| 40000 | 40000 | 40000 | 40000 | [45.5](https://drive.google.com/file/d/1g5d1SqSAC5UzPbpAMv2HcBZ5Ur9wZxru/view?usp=sharing) |
| 54000 | 54000 | 54000 | 54000 | [58.3](https://drive.google.com/file/d/1gAnDFr-SQLjGLXevaeYLy_iS1OBw-QZR/view?usp=sharing) |
| **High Performance** | 60000 | 60000 | 60000 | 60000 | [63](https://drive.google.com/file/d/1g0-IIqxHfi5ZDVda6_opOZwHtUV1KCen/view?usp=sharing) |
| 65000 | 65000 | 65000 | 65000 | [68](https://drive.google.com/file/d/1g1UNk8gteEK6AX1bFgnJsydKkl5JwnBR/view?usp=sharing) |
| 70000 | 70000 | 70000 | 70000 | [74](https://drive.google.com/file/d/1g1hnGeCrrd8OrOQ3yFBgIxRjYaG7PS_H/view?usp=sharing) |
| 75000 | 75000 | 75000 | 75000 | [77](https://drive.google.com/file/d/1g1inOfJBKXlpAW1AKlq3RDSZqk9yHGBP/view?usp=sharing) |
| 80000 | 80000 | 80000 | 80000 | [78.3](https://drive.google.com/file/d/1g3dyy5c2ZNryTH-cI2v58KTu9AbWRPEt/view?usp=sharing) |
| 90000 | 90000 | 90000 | 90000 | [78.6](https://drive.google.com/file/d/1g4Ml3iRr8IPlix3-W7jV-sMqgiIoeCX8/view?usp=sharing) |

> [!NOTE]
> Note: the measurements were performed with 19V input voltage.

<a id="power-input"></a>

# **Power Input**

The recommended input range for the SoM is 12V-24V.

> [!WARNING]
> Note: there is no reverse polarity protection on the SoM, please be careful not to confuse between the “+” and “-” signs. (**Red is Positive “+”**, **Black is Negative “-”**)

![](./attachments/0RMlhOtSRfdf6sYgznDfNW8KbIKu-vGoG9YKoVizeQ7d1LjR4kq3HED-OB8BCpMVnxkVBfZJGZPmCBWpiGi_qQC4qE8NLQc81Ku5AqJLHfH_eFjUgjF3tqsrxv1LTWdJb_K0AuLgAIDiO2ifUYE0V6I)

SolidRun uses Molex [1053071202](https://www.molex.com/en-us/products/part-detail/1053071202) Connector to interface between the SoM power input and the Phoenix Connecter.

![](./attachments/2t1J54AFT1l6woDGp2Nl5nb_Yww_9_yub0HC8DIlSz-4vmRn0wLfFlNrT2tlyICiyBYsTGv4gIcz88UqH6r5OPbstloUeetUmbu-fHCnOQec4ly0y2XWC9gqqsDyCtvIhKlIJA4u5BR9BwHMtN1XZCQ)

<a id="flashing-bios-and-mps-power-controller-soon"></a>

# **Flashing BIOS and MPS Power Controller**  
(Soon)