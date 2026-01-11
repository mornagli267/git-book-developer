# Upgrading Clearfog Pro to support CN9130 SOM

This guide is meant to explain how to upgrade the the ClearFog Pro to support both CN9130 SOM and A388 SOM.

<a id="25mhz-reference-clocks-for-ethernet-switch-and-phy"></a>

## 25MHz reference clocks for Ethernet Switch and PHY

**Note: Clearfog Pro revision 2.2.9 and later already include these changes.**

Dis-/Assemble the components from table below:

|     |     |     |     |
| --- | --- | --- | --- |
| #   | RefDes | Action | Comments |
| 1   | R140 | Remove | resistor 220Ω |
| 2   | R141 | Remove | resistor 499Ω |
| 3   | C52, C55 | Add | capacitor 22pF |
| 4   | Y1  | Add | crystal 25MHz 3.2mm x 2.5mm SMT |
| 5   | R138 | Remove | resistor 220Ω |
| 6   | R139 | Remove | resistor 499Ω |
| 7   | C154, C158 | Add | capacitor 22pF |
| 8   | Y2  | Add | crystal 25MHz 3.2mm x 2.5mm SMT |

The components locations are marked green / red in the pictures below:

<a id="components-side"></a>

### Components side

![cfpro_a38x_cn9130_phy_clock.png](./attachments/cfpro_a38x_cn9130_phy_clock.png)

<a id="print-side"></a>

### Print Side

![cfpro_a38x_cn9130_dsaswitch_clock.png](./attachments/cfpro_a38x_cn9130_dsaswitch_clock.png)

<a id="impact"></a>

### Impact

CN9130 SoM does not provide a 25MHz reference clock output, The changes outlined disconnect the SoM reference clock signal and replace it with crystals for both ethernet switch and port 6 phy.

<a id="sfp-rate-select-rs0-rs1"></a>

## SFP Rate-Select (RS0/RS1)

**Note: Clearfog Pro revision 2.2.12 and later already include these changes.**

Dis-/Assemble the components from table below:

|     |     |     |     |
| --- | --- | --- | --- |
| #   | RefDes | Action | Comments |
| 1   | R102, R103 | Remove | resistor 0Ω |
| 2   | R95, R96 | Add | resistor 1kΩ |

The components locations are marked red in the picture below:

![cfpro_a38x_cn9130_sfp.png](./attachments/cfpro_a38x_cn9130_sfp.png)

<a id="impact"></a>

### Impact

R95/R96 enable high-speed mode (10Gbps) for TX and RX on SFP modules.  
Without this change CN9130 SoM SFP port will be limited to sgmii (2.5Gbps and lower) speeds even though the cpu side supports up to 10Gbps.