# Bedrock SOM V3000 / R7000 / R8000 - Hardware User Manual

## Bedrock SOM V3000 / R7000 / R8000 - Hardware User Manual

![](../../.gitbook/assets/e2I938HxMdmXcRQAR4ucFky9uCd0oRptWQZF0YSB2MlnNW-mYT01w0psTVjI5NzVNUx9fstX6Y1kLKyofj1Bs54UQf9IGHH2iuAyK9BihurDYtUzACJrPIX5aiB7mkex7cRojTIdiYwyyZEXGvhAB7E)

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |              |           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- |
| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Revision** | **Notes** |
| 01 May 2024       | Firas Abd El Gani                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1.0          |           |
| Table of Contents | <p>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#introduction">Introduction</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#bedrock-som">Bedrock SOM</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#nio-networking-i-o-extension-board">NIO - Networking &#x26; I/O Extension Board</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#about-this-user-manual">About this User Manual</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#bedrock-som-block-diagram">Bedrock SOM Block Diagram</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#mechanical-files">Mechanical Files</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#typical-block-diagram-of-a-complete-system">Typical Block Diagram of a complete system</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#bedrock-cartridge">Bedrock Cartridge</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#som-board-to-board-connectors-mfg-p-n">SOM Board-to-Board Connectors - MFG P/N</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#board-to-board-connectors-pin-out">Board-to-board Connectors Pin-out</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#orcad-symbols">OrCad Symbols</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#differential-signals-impedance">Differential Signals Impedance</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#thermal-coupling">Thermal coupling</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#first-stage-thermal-coupling-in-cartridge">First stage thermal coupling in cartridge</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#2nd-stage-thermal-coupling-heatplate-nvme-ram-cartridge">2nd stage thermal coupling (heatplate, NVME, RAM, cartridge)</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#power-consumption">Power Consumption</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#power-input">Power Input</a><br>- <a href="bedrock-som-v3000-r7000-r8000-hardware-user-manual.md#flashing-bios-and-mps-power-controller-soon">Flashing BIOS and MPS Power Controller (Soon)</a></p> |              |           |

## **Introduction**

This user manual is intended to assist board-designers who consider developing a custom NIO for SolidRun Bedrock SOM.

### Bedrock SOM

Bedrock SOM is a system-on-module based on AMD Ryzen Embedded / Mobile processors with FP7R2 footprint. It is a compact self-contained computer system with processing, RAM, storage, power regulation and cooling. It brings out only the native I/O of the processor through high density board-to-board connectors to allow highly-modular system design with a high-degree of system customization by extension boards.

Currently Bedrock SOM is offered with several Ryzen variants including

* [Ryzen Embedded V3000 series](https://www.amd.com/en/products/embedded/ryzen/ryzen-v3000-series.html)
* [Ryzen Embedded 8000 series (“Hawk Point”)](https://www.amd.com/en/products/embedded/ryzen/ryzen-8000-series.html)
* [Ryzen 7000 series (“Phoenix”)](https://www.amd.com/en/products/processors/laptop/ryzen/7000-series/amd-ryzen-7-7840u.html)

To learn about the unique properties of each processor please review the corresponding [Bedrock PC documentation](https://www.solid-run.com/industrial-computers/).

### NIO - Networking & I/O Extension Board

NIO stands for Networking & I/O. NIO extension board is connected directly to Bedrock SOM.

SolidRun offers several types of NIO boards. NIO design files are offered as reference for board-designers who considering developing custom NIO boards.

### About this User Manual

This manual will guide you through the key aspects of integrating Bedrock SOM into your custom NIO design. It covers essential design considerations, including power requirements, signal integrity, thermal management, and connectivity options, ensuring you can fully harness the power of the AMD Ryzen™ processor in your specific application.

Each section of this manual provides detailed information and technical specifications to help you understand the interfaces, pinouts, and schematic design principles necessary for successful integration. Additionally, we provide best practices and expert tips to mitigate common design challenges and optimize your development process.

## **Bedrock SOM Block Diagram**

![image-20240523-104242.png](../../.gitbook/assets/image-20240523-104242.png)

{% hint style="info" %}
Please note that Port 9 (Lanes: 17-20) are used for the SoM’s Internal NVME.
{% endhint %}


Feature Summary:

* Memory: DDR5 Dual 64BG Channels, Support Up to DDR5-5600.
* USB:\
  2x USB4 (40 Gbps) - Supports USB-C Alt-Mode.\
  2x USB 3.2 Gen2 (10 Gbps).\
  4x USB2.0
* Display:\
  • DisplayPort 0 (DP0) : eDP/DP/HDMI\
  • DisplayPort 1 (DP1) : eDP/DP/HDMI\
  • DisplayPort 2 (DP2, USBC0) : DP/HDMI; or USB-C with DP alt mode; or USB4\
  • DisplayPort 3 (DP3, USBC1) : DP/HDMI; or USB-C with DP alt mode; or USB4\
  • DisplayPort 4 (DP4, USBC4) : DP/HDMI; or USB-C with DP alt mode\
  Note: Maximum 4 displays can be outputted simultaneously.
* PCIe: 9 ports, 16 Lanes PCIe Gen 4.
* Power: DC 12V-24V.
* Dimentions (83 mm x 91 mm x 12.7 mm) - Including SODIMM Modules.
* UART: 4 Ports.
* SPI: Yes.
* eSPI: Yes.
* I2C: 2 Ports.
* BIOS: AMI Aptio V

## **Mechanical Files**

SoM Board Dimensions: 83 x 75.76 mm (Top View):

![](../../.gitbook/assets/lFOnTdbvfWJrIdtKj-x6Tnb2h5uEIZjNXp9GZl1vh3IYMB-iOnVP511JVqqF8KrDLX4jI3gmeC9nm_ze7sTFhuXLeTpH7iS4KzQtWHWcwjq3AzqflhAjqAwMc2CKF8acYKCU7Km6H0PrzwmPleDNyOU)

Mechanical Files Download Link:\
[Bedrock SOM - Mechanical Files.zip](https://drive.google.com/file/d/1x6WCio1rlT2fanu_FUwZUYKD36Y2fDIM/view?usp=sharing)

## **Typical Block Diagram of a complete system**

![](../../.gitbook/assets/9-3scmofEZyiAROu_OZ3UtOJZACxxmRJewHw9TG03bXGIsoT46i476oNv6HrBYG2z8XWufvWf8NPOJHW4tWtVhnzHNYm1MIHZpXxuRvSYnJ1DmzT1k1naINzyvVGE7ytSapV90TZCgcMQDE3Y3RCO3o)

## **Bedrock Cartridge**

As part of developing a custom extension board for the Bedrock SOM, it’s recommended to use [Bedrock Cartridge](https://solidrun.atlassian.net/wiki/spaces/developer/pages/634454119/Bedrock+Cartridge+SoM+3D+model).

Bedrock Cartridge provides the following:

* Highly effective 1st stage thermal coupling (TIM0) to the Ryzen die to a copper heatplate.\
  Coupling the heatplate to a heatsink/cold-plate is easy. Coupling the die is challenging.
* Provision for mounting NIO securely with accurate spacing.
* Easy mounting of SOM to enclosure / heatsink / cold-plate.
* Thermal coupling for SOM’s DC-to-DC converters
* Mounting of NVME SSD\
  Not present on SOM itself
* Securing and thermal coupling for SODIMMs
* RTC battery compartment
* Physical protection and rigidity to the SOM
* Rigid chassis for the Bedrock Deck with multiple threaded mounting holes

![](../../.gitbook/assets/ChlqefgmxN68Xjj7MEKfkkDTsjjKOm--f20j0t1gI2JXvz7ONQnyR6kzotxZmqpPPrLI7nYoHt1iVVTulAbYS2A1Gf9gjzFvMXGjlGMUT3AfdZzdZmRh-bax_bnGJ0Sn7ksgRIDfnpnZD6ubdVXKT_w)

## **SOM Board-to-Board Connectors - MFG P/N**

| <p>Connector RefDes on<br><br>Bedrock SoM</p> | MFG P/N                  | <p>Connector RefDes on<br><br>NIO</p> | MFG P/N                  |
| --------------------------------------------- | ------------------------ | ------------------------------------- | ------------------------ |
| J1                                            | DF40C-100D**P**-0.4V(51) | J5                                    | DF40C-100D**S**-0.4V(51) |
| J2                                            | DF40C-100D**P**-0.4V(51) | J6                                    | DF40C-100D**S**-0.4V(51) |
| J3                                            | DF40C-100D**P**-0.4V(51) | J4                                    | DF40C-100D**S**-0.4V(51) |
| J4                                            | DF40C-80D**P**-0.4V(51)  | J7                                    | DF40C-80D**S**-0.4V(51)  |

Bedrock SoM Connectors (Males):

![](../../.gitbook/assets/ZgncuI2R5bTgyxBKRCtxSAJrlJXRnC86-UWlh456bAGt_IutGNx_JuQYLmTR_PbG2aAeiFvupY9aD-ZweaYdMpQ9trlWf2VRENU2N7y8X1e8Dhct9QgtAYkQuCA_2HU0KoOuWoI7MchG74qAv5Vv4zw)

NIO Connectors (Females):

![](../../.gitbook/assets/JXWIxruhWqtKhLeylcTp7jPHNE0l9X23_e4eQbm3niMbykBhnb0UFO37XfIt54higRVDx2qXSkAhU0PuPu7DBVlf6qr2azXCGwrke52ufPdNYIOE12sysoiQ3bjL5CmQlzYsjYh_ekvWm8Qd_CFZutM)

Note: Top Side of SoM is placed on Top Side of NIO, where the two boards are flipped one towards the other.

## **Board-to-board Connectors Pin-out**

The following is an example of the B2B pinout in NIO.\
Please note that the pinout relates to the _female_ connectors on a carrier, **to which the Bedrock SoM male Connectors are inserted**, and here we gave an example for SolidRun NIO Connectors (J4, J5, J6, J7). It’s important to be careful which pin is number #1.

![](../../.gitbook/assets/mJ_FRFaGzvYwRC37nPP_-etZhV9YeV4FA1I-9DfzPd9MaLI1psMy26Dwo2dTPyfoo18CNFEWcteBwYHP7xtFx5PyIiNTi9fpst9sAovKsMp-E7-KrzsI0nrc0W4Isdd5k5xrpf-x9OTg0jwSdKy_jws)

#### NIO R7000 Basic pinout

| <p><br><br>##### J5</p>                                | <p><br><br>##### Pin#</p>   | <p><br><br>##### J6</p>                  | <p><br><br>##### Pin#</p>  | <p><br><br>##### J4</p>                  | <p><br><br>##### Pin#</p>  | <p><br><br>##### J7</p>                              | <p><br><br>##### Pin#</p>  |
| ------------------------------------------------------ | --------------------------- | ---------------------------------------- | -------------------------- | ---------------------------------------- | -------------------------- | ---------------------------------------------------- | -------------------------- |
| <p><br><br>##### VDDBT_RTC</p>                         | <p><br><br>##### J5-93</p>  | <p><br><br>##### DP3_AUXN/USBC1_SBTX</p> | <p><br><br>##### J6-62</p> | <p><br><br>##### DP2_HPD</p>             | <p><br><br>##### J4-79</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-64</p> |
| <p><br><br>##### 48M_OSC</p>                           | <p><br><br>##### J5-77</p>  | <p><br><br>##### DP3_AUXP/USBC1_SBRX</p> | <p><br><br>##### J6-60</p> | <p><br><br>##### DP3_HPD</p>             | <p><br><br>##### J4-85</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-72</p> |
| <p><br><br>##### ACP_WOV_DMIC_CLK</p>                  | <p><br><br>##### J5-91</p>  | <p><br><br>##### GFX_CLKN_R</p>          | <p><br><br>##### J6-23</p> | <p><br><br>##### DP4_AUXN</p>            | <p><br><br>##### J4-81</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-80</p> |
| <p><br><br>##### ACP_WOV_DMIC_DAT0</p>                 | <p><br><br>##### J5-95</p>  | <p><br><br>##### GFX_CLKP_R</p>          | <p><br><br>##### J6-25</p> | <p><br><br>##### DP4_AUXP</p>            | <p><br><br>##### J4-83</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-69</p> |
| <p><br><br>##### AC_PRES</p>                           | <p><br><br>##### J5-26</p>  | <p><br><br>##### GFX_SLOT_RX0N</p>       | <p><br><br>##### J6-53</p> | <p><br><br>##### DP4_HPD</p>             | <p><br><br>##### J4-87</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-77</p> |
| <p><br><br>##### AGPIO11_MDIO3_SDA</p>                 | <p><br><br>##### J5-55</p>  | <p><br><br>##### GFX_SLOT_RX0P</p>       | <p><br><br>##### J6-55</p> | <p><br><br>##### USBC0_DN</p>            | <p><br><br>##### J4-48</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-66</p> |
| <p><br><br>##### AGPIO17</p>                           | <p><br><br>##### J5-86</p>  | <p><br><br>##### GFX_SLOT_RX1N</p>       | <p><br><br>##### J6-59</p> | <p><br><br>##### USBC0_DP</p>            | <p><br><br>##### J4-46</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-74</p> |
| <p><br><br>##### AGPIO18</p>                           | <p><br><br>##### J5-78</p>  | <p><br><br>##### GFX_SLOT_RX1P</p>       | <p><br><br>##### J6-61</p> | <p><br><br>##### USBC0_NOVA_RXAN</p>     | <p><br><br>##### J4-40</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-63</p> |
| <p><br><br>##### AGPIO21</p>                           | <p><br><br>##### J5-1</p>   | <p><br><br>##### GFX_SLOT_RX2N</p>       | <p><br><br>##### J6-65</p> | <p><br><br>##### USBC0_NOVA_RXAP</p>     | <p><br><br>##### J4-42</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-71</p> |
| <p><br><br>##### AGPIO22</p>                           | <p><br><br>##### J5-34</p>  | <p><br><br>##### GFX_SLOT_RX2P</p>       | <p><br><br>##### J6-67</p> | <p><br><br>##### USBC0_NOVA_RXBN</p>     | <p><br><br>##### J4-52</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-79</p> |
| <p><br><br>##### AGPIO24</p>                           | <p><br><br>##### J5-58</p>  | <p><br><br>##### GFX_SLOT_RX3N</p>       | <p><br><br>##### J6-71</p> | <p><br><br>##### USBC0_NOVA_RXBP</p>     | <p><br><br>##### J4-54</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-68</p> |
| <p><br><br>##### AGPIO3</p>                            | <p><br><br>##### J5-53</p>  | <p><br><br>##### GFX_SLOT_RX3P</p>       | <p><br><br>##### J6-73</p> | <p><br><br>##### USBC0_NOVA_TXAN</p>     | <p><br><br>##### J4-47</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-76</p> |
| <p><br><br>##### AGPIO32</p>                           | <p><br><br>##### J5-83</p>  | <p><br><br>##### GFX_SLOT_RX4N</p>       | <p><br><br>##### J6-77</p> | <p><br><br>##### USBC0_NOVA_TXAP</p>     | <p><br><br>##### J4-45</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-65</p> |
| <p><br><br>##### AGPIO4</p>                            | <p><br><br>##### J5-28</p>  | <p><br><br>##### GFX_SLOT_RX4P</p>       | <p><br><br>##### J6-79</p> | <p><br><br>##### USBC0_NOVA_TXBN</p>     | <p><br><br>##### J4-51</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-73</p> |
| <p><br><br>##### AGPIO89</p>                           | <p><br><br>##### J5-43</p>  | <p><br><br>##### GFX_SLOT_RX5N</p>       | <p><br><br>##### J6-83</p> | <p><br><br>##### USBC0_NOVA_TXBP</p>     | <p><br><br>##### J4-53</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-70</p> |
| <p><br><br>##### AGPIO90</p>                           | <p><br><br>##### J5-21</p>  | <p><br><br>##### GFX_SLOT_RX5P</p>       | <p><br><br>##### J6-85</p> | <p><br><br>##### USBC1_DN</p>            | <p><br><br>##### J4-66</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-78</p> |
| <p><br><br>##### APU_ALERT#</p>                        | <p><br><br>##### J5-72</p>  | <p><br><br>##### GFX_SLOT_RX6N</p>       | <p><br><br>##### J6-89</p> | <p><br><br>##### USBC1_DP</p>            | <p><br><br>##### J4-64</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-67</p> |
| <p><br><br>##### APU_I2C0_SCL_1V8</p>                  | <p><br><br>##### J5-11</p>  | <p><br><br>##### GFX_SLOT_RX6P</p>       | <p><br><br>##### J6-91</p> | <p><br><br>##### USBC1_RXAN</p>          | <p><br><br>##### J4-60</p> | <p><br><br>##### VIN_ALW</p>                         | <p><br><br>##### J7-75</p> |
| <p><br><br>##### APU_I2C0_SDA_1V8</p>                  | <p><br><br>##### J5-9</p>   | <p><br><br>##### GFX_SLOT_RX7N</p>       | <p><br><br>##### J6-95</p> | <p><br><br>##### USBC1_RXAP</p>          | <p><br><br>##### J4-58</p> | <p><br><br>##### ACP_WOV_DMIC_DAT1</p>               | <p><br><br>##### J7-48</p> |
| <p><br><br>##### APU_I2C1_SCL_1V8</p>                  | <p><br><br>##### J5-13</p>  | <p><br><br>##### GFX_SLOT_RX7P</p>       | <p><br><br>##### J6-97</p> | <p><br><br>##### USBC1_RXBN</p>          | <p><br><br>##### J4-72</p> | <p><br><br>##### ACP_WOV_DMIC_DAT2</p>               | <p><br><br>##### J7-42</p> |
| <p><br><br>##### APU_I2C1_SDA_1V8</p>                  | <p><br><br>##### J5-27</p>  | <p><br><br>##### GFX_SLOT_TX0N_C</p>     | <p><br><br>##### J6-6</p>  | <p><br><br>##### USBC1_RXBP</p>          | <p><br><br>##### J4-70</p> | <p><br><br>##### ACP_WOV_DMIC_DAT3</p>               | <p><br><br>##### J7-56</p> |
| <p><br><br>##### APU_PROCHOT#</p>                      | <p><br><br>##### J5-81</p>  | <p><br><br>##### GFX_SLOT_TX0P_C</p>     | <p><br><br>##### J6-8</p>  | <p><br><br>##### USBC1_TXAN</p>          | <p><br><br>##### J4-57</p> | <p><br><br>##### AZ_BITLK/SW1_MCLK/TDM0_BCLK_HDR</p> | <p><br><br>##### J7-44</p> |
| <p><br><br>##### APU_RST#</p>                          | <p><br><br>##### J5-74</p>  | <p><br><br>##### GFX_SLOT_TX1N_C</p>     | <p><br><br>##### J6-18</p> | <p><br><br>##### USBC1_TXAP</p>          | <p><br><br>##### J4-59</p> | <p><br><br>##### CONF_4</p>                          | <p><br><br>##### J7-36</p> |
| <p><br><br>##### APU_SCLK0_1V8</p>                     | <p><br><br>##### J5-19</p>  | <p><br><br>##### GFX_SLOT_TX1P_C</p>     | <p><br><br>##### J6-20</p> | <p><br><br>##### USBC1_TXBN</p>          | <p><br><br>##### J4-63</p> | <p><br><br>##### CONF_5</p>                          | <p><br><br>##### J7-6</p>  |
| <p><br><br>##### APU_SCLK1_1V8</p>                     | <p><br><br>##### J5-37</p>  | <p><br><br>##### GFX_SLOT_TX2N_C</p>     | <p><br><br>##### J6-30</p> | <p><br><br>##### USBC1_TXBP</p>          | <p><br><br>##### J4-65</p> | <p><br><br>##### DOUT_BT_HDR</p>                     | <p><br><br>##### J7-52</p> |
| <p><br><br>##### APU_SDATA0_1V8</p>                    | <p><br><br>##### J5-17</p>  | <p><br><br>##### GFX_SLOT_TX2P_C</p>     | <p><br><br>##### J6-32</p> | <p><br><br>##### USBC4_DN</p>            | <p><br><br>##### J4-92</p> | <p><br><br>##### GPP_CLK5N_R</p>                     | <p><br><br>##### J7-41</p> |
| <p><br><br>##### APU_SDATA1_1V8</p>                    | <p><br><br>##### J5-39</p>  | <p><br><br>##### GFX_SLOT_TX3N_C</p>     | <p><br><br>##### J6-42</p> | <p><br><br>##### USBC4_DP</p>            | <p><br><br>##### J4-90</p> | <p><br><br>##### GPP_CLK5P_R</p>                     | <p><br><br>##### J7-39</p> |
| <p><br><br>##### APU_SFH_SCL</p>                       | <p><br><br>##### J5-67</p>  | <p><br><br>##### GFX_SLOT_TX3P_C</p>     | <p><br><br>##### J6-44</p> | <p><br><br>##### USBC4_SS+_RXAN</p>      | <p><br><br>##### J4-86</p> | <p><br><br>##### GPP_CLK6N_R</p>                     | <p><br><br>##### J7-45</p> |
| <p><br><br>##### APU_SFH_SDA</p>                       | <p><br><br>##### J5-38</p>  | <p><br><br>##### GFX_SLOT_TX4N</p>       | <p><br><br>##### J6-54</p> | <p><br><br>##### USBC4_SS+_RXAP</p>      | <p><br><br>##### J4-84</p> | <p><br><br>##### GPP_CLK6P_R</p>                     | <p><br><br>##### J7-47</p> |
| <p><br><br>##### APU_SIC</p>                           | <p><br><br>##### J5-82</p>  | <p><br><br>##### GFX_SLOT_TX4P</p>       | <p><br><br>##### J6-56</p> | <p><br><br>##### USBC4_SS+_RXBN</p>      | <p><br><br>##### J4-96</p> | <p><br><br>##### GPP_RX10N</p>                       | <p><br><br>##### J7-10</p> |
| <p><br><br>##### APU_SID</p>                           | <p><br><br>##### J5-90</p>  | <p><br><br>##### GFX_SLOT_TX5N</p>       | <p><br><br>##### J6-66</p> | <p><br><br>##### USBC4_SS+_RXBP</p>      | <p><br><br>##### J4-98</p> | <p><br><br>##### GPP_RX10P</p>                       | <p><br><br>##### J7-12</p> |
| <p><br><br>##### APU_THERMTRIP#</p>                    | <p><br><br>##### J5-15</p>  | <p><br><br>##### GFX_SLOT_TX5P</p>       | <p><br><br>##### J6-68</p> | <p><br><br>##### USBC4_SS+_TXAN</p>      | <p><br><br>##### J4-69</p> | <p><br><br>##### GPP_RX11N</p>                       | <p><br><br>##### J7-33</p> |
| <p><br><br>##### AZ_RST#/SW0_MDATA1/TDM0_DIN_HDR</p>   | <p><br><br>##### J5-84</p>  | <p><br><br>##### GFX_SLOT_TX6N</p>       | <p><br><br>##### J6-78</p> | <p><br><br>##### USBC4_SS+_TXAP</p>      | <p><br><br>##### J4-71</p> | <p><br><br>##### GPP_RX11P</p>                       | <p><br><br>##### J7-35</p> |
| <p><br><br>##### AZ_SDIN0/SW0_MDATA3_HDR</p>           | <p><br><br>##### J5-64</p>  | <p><br><br>##### GFX_SLOT_TX6P</p>       | <p><br><br>##### J6-80</p> | <p><br><br>##### USBC4_SS+_TXBN</p>      | <p><br><br>##### J4-75</p> | <p><br><br>##### GPP_RX12N</p>                       | <p><br><br>##### J7-5</p>  |
| <p><br><br>##### AZ_SDIN1/SW0_MCLK_TDM1_BCLK_HDR</p>   | <p><br><br>##### J5-89</p>  | <p><br><br>##### GFX_SLOT_TX7N</p>       | <p><br><br>##### J6-90</p> | <p><br><br>##### USBC4_SS+_TXBP</p>      | <p><br><br>##### J4-77</p> | <p><br><br>##### GPP_RX12P</p>                       | <p><br><br>##### J7-3</p>  |
| <p><br><br>##### AZ_SDIN2/SW0_MDATA0/TDM1_OUT_HDR</p>  | <p><br><br>##### J5-66</p>  | <p><br><br>##### GFX_SLOT_TX7P</p>       | <p><br><br>##### J6-92</p> | <p><br><br>##### USBN3</p>               | <p><br><br>##### J4-89</p> | <p><br><br>##### GPP_TX10N</p>                       | <p><br><br>##### J7-11</p> |
| <p><br><br>##### AZ_SDOUT/SW0_MDATA2/TDM0_DOUT_HDR</p> | <p><br><br>##### J5-98</p>  | <p><br><br>##### GPP_CLK1N_R</p>         | <p><br><br>##### J6-29</p> | <p><br><br>##### USBN6</p>               | <p><br><br>##### J4-95</p> | <p><br><br>##### GPP_TX10P</p>                       | <p><br><br>##### J7-9</p>  |
| <p><br><br>##### AZ_SYNC/SW1_MDATA0/TDM0_FRM_HDR</p>   | <p><br><br>##### J5-100</p> | <p><br><br>##### GPP_CLK1P_R</p>         | <p><br><br>##### J6-31</p> | <p><br><br>##### USBN7</p>               | <p><br><br>##### J4-99</p> | <p><br><br>##### GPP_TX11N</p>                       | <p><br><br>##### J7-17</p> |
| <p><br><br>##### CONF_1</p>                            | <p><br><br>##### J5-92</p>  | <p><br><br>##### GPP_CLK2N_R</p>         | <p><br><br>##### J6-35</p> | <p><br><br>##### USBP3</p>               | <p><br><br>##### J4-91</p> | <p><br><br>##### GPP_TX11P</p>                       | <p><br><br>##### J7-15</p> |
| <p><br><br>##### CONF_2</p>                            | <p><br><br>##### J5-61</p>  | <p><br><br>##### GPP_CLK2P_R</p>         | <p><br><br>##### J6-37</p> | <p><br><br>##### USBP6</p>               | <p><br><br>##### J4-93</p> | <p><br><br>##### GPP_TX12N_C</p>                     | <p><br><br>##### J7-21</p> |
| <p><br><br>##### CONF_3</p>                            | <p><br><br>##### J5-97</p>  | <p><br><br>##### GPP_CLK3N_R</p>         | <p><br><br>##### J6-48</p> | <p><br><br>##### USBP7</p>               | <p><br><br>##### J4-97</p> | <p><br><br>##### GPP_TX12P_C</p>                     | <p><br><br>##### J7-23</p> |
| <p><br><br>##### CONF_6</p>                            | <p><br><br>##### J5-85</p>  | <p><br><br>##### GPP_CLK3P_R</p>         | <p><br><br>##### J6-50</p> | <p><br><br>##### DP0_AUXN</p>            | <p><br><br>##### J4-4</p>  | <p><br><br>##### INT_CLK_REQ3#</p>                   | <p><br><br>##### J7-38</p> |
| <p><br><br>##### DP_STERESOSYNC</p>                    | <p><br><br>##### J5-80</p>  | <p><br><br>##### GPP_RX13N</p>           | <p><br><br>##### J6-17</p> | <p><br><br>##### DP0_AUXP</p>            | <p><br><br>##### J4-6</p>  | <p><br><br>##### LRCLK_BT_HDR</p>                    | <p><br><br>##### J7-54</p> |
| <p><br><br>##### EGPIO67</p>                           | <p><br><br>##### J5-3</p>   | <p><br><br>##### GPP_RX13P</p>           | <p><br><br>##### J6-19</p> | <p><br><br>##### DP0_BLON</p>            | <p><br><br>##### J4-35</p> | <p><br><br>##### RTC_CLK2_R</p>                      | <p><br><br>##### J7-40</p> |
| <p><br><br>##### EGPIO74</p>                           | <p><br><br>##### J5-7</p>   | <p><br><br>##### GPP_RX14N</p>           | <p><br><br>##### J6-11</p> | <p><br><br>##### DP0_BLPWM</p>           | <p><br><br>##### J4-39</p> | <p><br><br>##### SDIN_BT_HDR</p>                     | <p><br><br>##### J7-50</p> |
| <p><br><br>##### EGPIO76</p>                           | <p><br><br>##### J5-5</p>   | <p><br><br>##### GPP_RX14P</p>           | <p><br><br>##### J6-13</p> | <p><br><br>##### DP0_DIGON</p>           | <p><br><br>##### J4-37</p> | <p><br><br>##### UART4_CTS#</p>                      | <p><br><br>##### J7-4</p>  |
| <p><br><br>##### EGPIO78</p>                           | <p><br><br>##### J5-35</p>  | <p><br><br>##### GPP_RX15N</p>           | <p><br><br>##### J6-5</p>  | <p><br><br>##### DP0_HPD</p>             | <p><br><br>##### J4-33</p> | <p><br><br>##### UART4_INTR</p>                      | <p><br><br>##### J7-2</p>  |
| <p><br><br>##### EGPIO79</p>                           | <p><br><br>##### J5-8</p>   | <p><br><br>##### GPP_RX15P</p>           | <p><br><br>##### J6-7</p>  | <p><br><br>##### DP0_TX0N</p>            | <p><br><br>##### J4-10</p> | <p><br><br>##### UART4_TXD</p>                       | <p><br><br>##### J7-34</p> |
| <p><br><br>##### ESPI_CLK_EC</p>                       | <p><br><br>##### J5-6</p>   | <p><br><br>##### GPP_RX8N</p>            | <p><br><br>##### J6-47</p> | <p><br><br>##### DP0_TX0P</p>            | <p><br><br>##### J4-12</p> | <p><br><br>##### USB5_SS+_RXN</p>                    | <p><br><br>##### J7-24</p> |
| <p><br><br>##### ESPI_DAT0_EC</p>                      | <p><br><br>##### J5-22</p>  | <p><br><br>##### GPP_RX8P</p>            | <p><br><br>##### J6-49</p> | <p><br><br>##### DP0_TX1N</p>            | <p><br><br>##### J4-18</p> | <p><br><br>##### USB5_SS+_RXP</p>                    | <p><br><br>##### J7-22</p> |
| <p><br><br>##### ESPI_DAT1_EC</p>                      | <p><br><br>##### J5-14</p>  | <p><br><br>##### GPP_RX9N</p>            | <p><br><br>##### J6-41</p> | <p><br><br>##### DP0_TX1P</p>            | <p><br><br>##### J4-16</p> | <p><br><br>##### USB5_SS+_TXN</p>                    | <p><br><br>##### J7-16</p> |
| <p><br><br>##### ESPI_DAT2_EC</p>                      | <p><br><br>##### J5-18</p>  | <p><br><br>##### GPP_RX9P</p>            | <p><br><br>##### J6-43</p> | <p><br><br>##### DP0_TX2N</p>            | <p><br><br>##### J4-24</p> | <p><br><br>##### USB5_SS+_TXP</p>                    | <p><br><br>##### J7-18</p> |
| <p><br><br>##### ESPI_DAT3_EC</p>                      | <p><br><br>##### J5-20</p>  | <p><br><br>##### GPP_TX13N_C</p>         | <p><br><br>##### J6-36</p> | <p><br><br>##### DP0_TX2P</p>            | <p><br><br>##### J4-22</p> | <p><br><br>##### USBC5_RX2N</p>                      | <p><br><br>##### J7-57</p> |
| <p><br><br>##### FANOUT0_1V8</p>                       | <p><br><br>##### J5-47</p>  | <p><br><br>##### GPP_TX13P_C</p>         | <p><br><br>##### J6-38</p> | <p><br><br>##### DP0_TX3N</p>            | <p><br><br>##### J4-28</p> | <p><br><br>##### USBC5_RX2P</p>                      | <p><br><br>##### J7-59</p> |
| <p><br><br>##### FANTACH0_1V8</p>                      | <p><br><br>##### J5-45</p>  | <p><br><br>##### GPP_TX14N</p>           | <p><br><br>##### J6-24</p> | <p><br><br>##### DP0_TX3P</p>            | <p><br><br>##### J4-30</p> | <p><br><br>##### USBC5_TX2N</p>                      | <p><br><br>##### J7-29</p> |
| <p><br><br>##### INTRUDER_ALERT</p>                    | <p><br><br>##### J5-50</p>  | <p><br><br>##### GPP_TX14P</p>           | <p><br><br>##### J6-26</p> | <p><br><br>##### DP1_AUXN</p>            | <p><br><br>##### J4-9</p>  | <p><br><br>##### USBC5_TX2P</p>                      | <p><br><br>##### J7-27</p> |
| <p><br><br>##### INT_CLK_REQ0#</p>                     | <p><br><br>##### J5-46</p>  | <p><br><br>##### GPP_TX15N</p>           | <p><br><br>##### J6-12</p> | <p><br><br>##### DP1_AUXP</p>            | <p><br><br>##### J4-11</p> | <p><br><br>##### USBN2</p>                           | <p><br><br>##### J7-30</p> |
| <p><br><br>##### INT_CLK_REQ1#</p>                     | <p><br><br>##### J5-44</p>  | <p><br><br>##### GPP_TX15P</p>           | <p><br><br>##### J6-14</p> | <p><br><br>##### DP1_BLON</p>            | <p><br><br>##### J4-76</p> | <p><br><br>##### USBN5</p>                           | <p><br><br>##### J7-53</p> |
| <p><br><br>##### INT_CLK_REQ2#</p>                     | <p><br><br>##### J5-42</p>  | <p><br><br>##### GPP_TX8N</p>            | <p><br><br>##### J6-96</p> | <p><br><br>##### DP1_BLPWM</p>           | <p><br><br>##### J4-80</p> | <p><br><br>##### USBN6</p>                           | <p><br><br>##### J4-95</p> |
| <p><br><br>##### INT_SENSOR_0</p>                      | <p><br><br>##### J5-36</p>  | <p><br><br>##### GPP_TX8P</p>            | <p><br><br>##### J6-98</p> | <p><br><br>##### DP1_DIGON</p>           | <p><br><br>##### J4-78</p> | <p><br><br>##### USBP2</p>                           | <p><br><br>##### J7-28</p> |
| <p><br><br>##### INT_SENSOR_1</p>                      | <p><br><br>##### J5-65</p>  | <p><br><br>##### GPP_TX9N</p>            | <p><br><br>##### J6-84</p> | <p><br><br>##### DP1_HPD</p>             | <p><br><br>##### J4-41</p> | <p><br><br>##### USBP5</p>                           | <p><br><br>##### J7-51</p> |
| <p><br><br>##### KR10G_PHY1_INTR#_1V8</p>              | <p><br><br>##### J5-32</p>  | <p><br><br>##### GPP_TX9P</p>            | <p><br><br>##### J6-86</p> | <p><br><br>##### DP1_TX0N</p>            | <p><br><br>##### J4-5</p>  | <p><br><br>##### 3.3V_ALW_SOM</p>                    | <p><br><br>##### J7-58</p> |
| <p><br><br>##### M2_SSD0_LED#</p>                      | <p><br><br>##### J5-2</p>   | <p><br><br>##### SOM_ENABLE</p>          | <p><br><br>##### J6-74</p> | <p><br><br>##### DP1_TX0P</p>            | <p><br><br>##### J4-3</p>  | <p><br><br>##### 3.3V_ALW_SOM</p>                    | <p><br><br>##### J7-60</p> |
| <p><br><br>##### MDIO0_SCL</p>                         | <p><br><br>##### J5-24</p>  |                                          |                            | <p><br><br>##### DP1_TX1N</p>            | <p><br><br>##### J4-17</p> | <p><br><br>##### 3.3V_ALW_SOM</p>                    | <p><br><br>##### J7-62</p> |
| <p><br><br>##### MDIO0_SDA</p>                         | <p><br><br>##### J5-10</p>  |                                          |                            | <p><br><br>##### DP1_TX1P</p>            | <p><br><br>##### J4-15</p> |                                                      |                            |
| <p><br><br>##### MDIO1_SCL</p>                         | <p><br><br>##### J5-40</p>  |                                          |                            | <p><br><br>##### DP1_TX2N</p>            | <p><br><br>##### J4-23</p> |                                                      |                            |
| <p><br><br>##### MDIO1_SDA</p>                         | <p><br><br>##### J5-59</p>  |                                          |                            | <p><br><br>##### DP1_TX2P</p>            | <p><br><br>##### J4-21</p> |                                                      |                            |
| <p><br><br>##### MDIO2_SCL</p>                         | <p><br><br>##### J5-68</p>  |                                          |                            | <p><br><br>##### DP1_TX3N</p>            | <p><br><br>##### J4-29</p> |                                                      |                            |
| <p><br><br>##### MPM_EVENT#</p>                        | <p><br><br>##### J5-33</p>  |                                          |                            | <p><br><br>##### DP1_TX3P</p>            | <p><br><br>##### J4-27</p> |                                                      |                            |
| <p><br><br>##### PCIE_RST#</p>                         | <p><br><br>##### J5-79</p>  |                                          |                            | <p><br><br>##### DP2_AUXN/USBC0_SBTX</p> | <p><br><br>##### J4-36</p> |                                                      |                            |
| <p><br><br>##### PCIE_RST1#</p>                        | <p><br><br>##### J5-31</p>  |                                          |                            | <p><br><br>##### DP2_AUXP/USBC0_SBRX</p> | <p><br><br>##### J4-34</p> |                                                      |                            |
| <p><br><br>##### PCIE_WAKE#</p>                        | <p><br><br>##### J5-49</p>  |                                          |                            | <p><br><br>##### DP2_HPD</p>             | <p><br><br>##### J4-79</p> |                                                      |                            |
| <p><br><br>##### PWR_BTN#</p>                          | <p><br><br>##### J5-51</p>  |                                          |                            | <p><br><br>##### DP3_HPD</p>             | <p><br><br>##### J4-85</p> |                                                      |                            |
| <p><br><br>##### SATA_ACT_1.8V#</p>                    | <p><br><br>##### J5-25</p>  |                                          |                            | <p><br><br>##### DP4_AUXN</p>            | <p><br><br>##### J4-81</p> |                                                      |                            |
| <p><br><br>##### SENSOR_MISC1</p>                      | <p><br><br>##### J5-57</p>  |                                          |                            | <p><br><br>##### DP4_AUXP</p>            | <p><br><br>##### J4-83</p> |                                                      |                            |
| <p><br><br>##### SENSOR_MISC2</p>                      | <p><br><br>##### J5-71</p>  |                                          |                            | <p><br><br>##### DP4_HPD</p>             | <p><br><br>##### J4-87</p> |                                                      |                            |
| <p><br><br>##### SENSOR_MISC3</p>                      | <p><br><br>##### J5-63</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### SENSOR_MISC4</p>                      | <p><br><br>##### J5-69</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### SYS_RST#</p>                          | <p><br><br>##### J5-48</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### SYS_S0_PWR_EN</p>                     | <p><br><br>##### J5-12</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### SYS_S3_PWR_EN</p>                     | <p><br><br>##### J5-41</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### TMON_I2C_SCL</p>                      | <p><br><br>##### J5-54</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### TMON_I2C_SDA</p>                      | <p><br><br>##### J5-56</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### TPAD_INT#</p>                         | <p><br><br>##### J5-23</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### UART0_CTS#</p>                        | <p><br><br>##### J5-99</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### UART0_INTR</p>                        | <p><br><br>##### J5-94</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### UART0_RTS#</p>                        | <p><br><br>##### J5-96</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### UART0_RXD</p>                         | <p><br><br>##### J5-75</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### UART0_TXD</p>                         | <p><br><br>##### J5-73</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### UART2_TXD</p>                         | <p><br><br>##### J5-88</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### USBC_I2C_SCL</p>                      | <p><br><br>##### J5-62</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### USBC_I2C_SDA</p>                      | <p><br><br>##### J5-87</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### USBC_PD_INT</p>                       | <p><br><br>##### J5-52</p>  |                                          |                            |                                          |                            |                                                      |                            |
| <p><br><br>##### USB_OCP#</p>                          | <p><br><br>##### J5-60</p>  |                                          |                            |                                          |                            |                                                      |                            |

## **OrCad Symbols**

In the following link you will find a PDF and OrCad Symbols for the NIO board-to-board connectors, to which the SoM (Male) Connectors are inserted:&#x20;

1. [**NIO BtB Connectors - PDF**](https://drive.google.com/file/d/1xB46dORFV3Gp8puEIqd73Do4I4A2uQde/view?usp=sharing)
2. [**NIO BtB Connectors - OrCad Symbols**](https://drive.google.com/file/d/1xFvehTro61wH1tTmV1JiQuoHRzARKDgt/view?usp=sharing)

## **Differential Signals Impedance**

[In this Excel](https://docs.google.com/spreadsheets/d/1FFL56p2GHO3JOiYYOMDi9Uce2WsCgf6ddNtgSrbaBDc/edit?usp=sharing), you will find a list for the impedance for each differential signal.&#x20;

Note: All differential pairs are 90-Ohm, the rest are GPIOs/Single-Ended signals which are 50-Ohm by default.

## **Thermal coupling**

### **First stage thermal coupling in cartridge**

The cartridge is assembled in the factory and should not be disassembled. It provides 1st stage cooling for the processor and power FETs.

### **2nd stage thermal coupling (heatplate, NVME, RAM, cartridge)**

* Thermal grease should be applied on heatplate. Heatplate should be attached to a cold plate.
* Thermal pad should be applied on NVME
* If device is intended to work at high ambient temperature it is advised to apply thermal gel between SODIMMs and RAM cover and thermal grease on top side of RAM cover
* The frame of the skirt is thermally coupled to the cold plate. Consider applying thermal paste on the frame of the skirt.

![Thermal\_Grease2.png](../../.gitbook/assets/Thermal_Grease2.png)

## **Power Consumption**

#### SmartShift Technology for Optimized Power Management

One of the key features of our System on Module, integrated with AMD Ryzen™ processors, is the SmartShift technology. This innovative feature allows for dynamic adjustment of power allocation between the CPU and other system components. By intelligently shifting power where it's needed most, SmartShift enhances overall performance and efficiency, making it an ideal solution for power-sensitive applications.

#### Controlling CPU Power Consumption

With SmartShift, you can precisely control the power consumption of the CPU, tailoring it to fit the specific needs of your application. This capability is especially beneficial in scenarios where power efficiency is crucial, such as in portable or battery-operated devices. You can set a limit to the CPU power consumption, for example, capping it at a specific wattage to balance performance with power usage.

#### Configuring CPU Power Limits in BIOS

To configure the CPU power limits, you can access the BIOS settings of our System on Module. We provide a detailed guide on how to navigate these settings and effectively set the desired power caps for your application.

For step-by-step instructions on accessing and modifying these settings, please visit our detailed BIOS configuration page here: [Bedrock V3000 BIOS Settings - Power Screen](../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/bios-bedrock-v3000/bedrock-v3000-bios-settings.md#power-screen).

By leveraging the SmartShift technology and configuring your CPU power settings via BIOS, you can optimize your system’s performance and power consumption, leading to a more efficient and tailored usage according to your specific requirements. This section of the manual ensures that you have all the necessary tools and knowledge to take full advantage of the innovative features provided by our System on Module.

To demonstrate the efficacy and benefits of the SmartShift technology in our System on Module (SoM), extensive measurements have been conducted using a SoM based on the AMD Ryzen™ 7 7840HS processor paired with the Networking & I/O extension board (NIO). These tests were aimed at validating how effectively SmartShift manages power distribution under various operational conditions.

#### SmartShift Configuration Parameters:

The SmartShift feature is controlled through four key parameters in the BIOS Power tab, which allow for precise management of power distribution and consumption:

* **APU Only sPPT Limit**: Sets the peak power limit that the Accelerated Processing Unit (APU) can consume.
* **Sustained Power Limit**: Defines the sustained power threshold for long-term performance stability.
* **Fast PPT Limit**: Regulates the rapid power allowance for short bursts of intensive processing.
* **Slow PPT Limit**: Controls the lower power threshold, suitable for maintaining efficiency during less demanding tasks.

#### Measurement Results

The following table illustrates the power consumption results (in Watts) observed under various settings of these parameters. These measurements provide clear insights into how SmartShift adjusts power usage dynamically, ensuring optimal performance and efficiency across different workloads and operational states.

The tests outlined in the table above were conducted while the system was running CineBench R23, specifically utilizing the Multi-Core test mode. This benchmarking tool is widely recognized for its ability to stress multiple CPU cores simultaneously, making it an ideal platform for evaluating the performance of the SmartShift technology under high computational loads. By conducting the tests in this environment, we ensure that the measurements accurately reflect the capabilities of SmartShift to dynamically manage and optimize power consumption during intensive processing tasks.

| **Setting Description**  | **APU only sPPT Limit (mW)** | **Sustained PowerLimit (SPL) (mW)** | <p><strong>Fast PPT limit</strong><br><strong>(mW)</strong></p> | <p><strong>Slow PPT Limit</strong><br><strong>(mW)</strong></p>                            | **Scope Measurment \[Cinebench Multi]: Total Power \[W]**                                  |
| ------------------------ | ---------------------------- | ----------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Energy Saving**        | 5000                         | 5000                                | 5000                                                            | 5000                                                                                       | [14.7](https://drive.google.com/file/d/1g8dZm3DITwetPaUz2h37IoKcPkeZdlt7/view?usp=sharing) |
| 8000                     | 8000                         | 8000                                | 8000                                                            | [14.9](https://drive.google.com/file/d/1g8HxmO7Jc9lY5nxcKPzDloRKCjMnHGYj/view?usp=sharing) |                                                                                            |
| 10000                    | 10000                        | 10000                               | 10000                                                           | [16.5](https://drive.google.com/file/d/1g7CzrXT89efIK49PYBxK29MfULcTM9Py/view?usp=sharing) |                                                                                            |
| 20000                    | 20000                        | 20000                               | 20000                                                           | [25.1](https://drive.google.com/file/d/1g6HEnN4Z4QcZ3GFOz2mek2aZT8-6V9Ds/view?usp=sharing) |                                                                                            |
| **Balanced Performance** | 30000                        | 30000                               | 30000                                                           | 30000                                                                                      | [37.5](https://drive.google.com/file/d/1g5gtqXmj1jZqR6BMNM-RMDGfanoHeekq/view?usp=sharing) |
| 40000                    | 40000                        | 40000                               | 40000                                                           | [45.5](https://drive.google.com/file/d/1g5d1SqSAC5UzPbpAMv2HcBZ5Ur9wZxru/view?usp=sharing) |                                                                                            |
| 54000                    | 54000                        | 54000                               | 54000                                                           | [58.3](https://drive.google.com/file/d/1gAnDFr-SQLjGLXevaeYLy_iS1OBw-QZR/view?usp=sharing) |                                                                                            |
| **High Performance**     | 60000                        | 60000                               | 60000                                                           | 60000                                                                                      | [63](https://drive.google.com/file/d/1g0-IIqxHfi5ZDVda6_opOZwHtUV1KCen/view?usp=sharing)   |
| 65000                    | 65000                        | 65000                               | 65000                                                           | [68](https://drive.google.com/file/d/1g1UNk8gteEK6AX1bFgnJsydKkl5JwnBR/view?usp=sharing)   |                                                                                            |
| 70000                    | 70000                        | 70000                               | 70000                                                           | [74](https://drive.google.com/file/d/1g1hnGeCrrd8OrOQ3yFBgIxRjYaG7PS_H/view?usp=sharing)   |                                                                                            |
| 75000                    | 75000                        | 75000                               | 75000                                                           | [77](https://drive.google.com/file/d/1g1inOfJBKXlpAW1AKlq3RDSZqk9yHGBP/view?usp=sharing)   |                                                                                            |
| 80000                    | 80000                        | 80000                               | 80000                                                           | [78.3](https://drive.google.com/file/d/1g3dyy5c2ZNryTH-cI2v58KTu9AbWRPEt/view?usp=sharing) |                                                                                            |
| 90000                    | 90000                        | 90000                               | 90000                                                           | [78.6](https://drive.google.com/file/d/1g4Ml3iRr8IPlix3-W7jV-sMqgiIoeCX8/view?usp=sharing) |                                                                                            |

{% hint style="info" %}
Note: the measurements were performed with 19V input voltage.
{% endhint %}


## **Power Input**

The recommended input range for the SoM is 12V-24V.

{% hint style="warning" %}
Note: there is no reverse polarity protection on the SoM, please be careful not to confuse between the “+” and “-” signs. (**Red is Positive “+”**, **Black is Negative “-”**)
{% endhint %}


![](../../.gitbook/assets/0RMlhOtSRfdf6sYgznDfNW8KbIKu-vGoG9YKoVizeQ7d1LjR4kq3HED-OB8BCpMVnxkVBfZJGZPmCBWpiGi_qQC4qE8NLQc81Ku5AqJLHfH_eFjUgjF3tqsrxv1LTWdJb_K0AuLgAIDiO2ifUYE0V6I)

SolidRun uses Molex [1053071202](https://www.molex.com/en-us/products/part-detail/1053071202) Connector to interface between the SoM power input and the Phoenix Connecter.

![](../../.gitbook/assets/2t1J54AFT1l6woDGp2Nl5nb_Yww_9_yub0HC8DIlSz-4vmRn0wLfFlNrT2tlyICiyBYsTGv4gIcz88UqH6r5OPbstloUeetUmbu-fHCnOQec4ly0y2XWC9gqqsDyCtvIhKlIJA4u5BR9BwHMtN1XZCQ)

## **Flashing BIOS and MPS Power Controller**

(Soon)
