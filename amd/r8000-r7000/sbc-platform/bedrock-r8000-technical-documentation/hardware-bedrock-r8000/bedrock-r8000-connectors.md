# Bedrock R8000 connectors

## Bedrock R8000 connectors

* [DC IN connector](bedrock-r8000-connectors.md#dc-in-connector)
  * [Mating connector](bedrock-r8000-connectors.md#mating-connector)
* [Remote power button connector](bedrock-r8000-connectors.md#remote-power-button-connector)
  * [Remote power button pinout](bedrock-r8000-connectors.md#remote-power-button-pinout)
  * [Remote power LED parameters](bedrock-r8000-connectors.md#remote-power-led-parameters)
  * [More info](bedrock-r8000-connectors.md#more-info)
* [WiFi antenna connector](bedrock-r8000-connectors.md#wifi-antenna-connector)
* [LTE/5G antenna connector](bedrock-r8000-connectors.md#lte-5g-antenna-connector)

## DC IN connector

Manufacturer: Phoenix Contact\
Manufacturer PN: 1827868

[https://www.phoenixcontact.com/en-pc/products/printed-circuit-board-connector-mc-15-2-gf-381-1827868](https://www.phoenixcontact.com/en-pc/products/printed-circuit-board-connector-mc-15-2-gf-381-1827868)

#### Mating connector

Manufacturer: Phoenix Contact\
Manufacturer PN: 1827703

[https://www.phoenixcontact.com/en-us/products/pcb-plug-mc-15-2-stf-381-1827703](https://www.phoenixcontact.com/en-us/products/pcb-plug-mc-15-2-stf-381-1827703)

{% hint style="info" %}
SolidRun offers [SRBD-CABDC](/amd/r8000-r7000/sbc-platform/bedrock-r8000-technical-documentation/bedrock-r8000-r7000-accessories.md#dc-cable-phoenix-connector) Pigtail DC cable for Bedrock with the mating connector
{% endhint %}


## Remote power button connector

Manufacturer: [Molex](https://www.molex.com/en-us/home)\
Manufacturer PN: 353630460

#### Remote power button pinout

![](<../../../../.gitbook/assets/power button.jpg>)

#### Remote power LED parameters

|                              |       |
| ---------------------------- | ----- |
| Voltage - Forward (Vf) (Typ) | 3.2 V |
| Current (Typ)                | 20 mA |

#### More info

* [Datasheet](https://www.molex.com/en-us/products/part-detail/353630460)
* SolidRun remote power button cable:
  * SolidRun PN: SRBD-CABBTN
  * Description: 1m cable with panel mount power button (black) with integrated blue LED (IP67 rating)
  * Panel mount power button: [https://www.e-switch.com/product-catalog/rp8100-series-round-illuminated-pushbutton-switch](https://www.e-switch.com/product-catalog/rp8100-series-round-illuminated-pushbutton-switch)
* [Remote power button schematics](https://drive.google.com/file/d/1yIGvfnjJ2ggpG37PPsWe57a5aQo70dfN/view?usp=sharing)

## WiFi antenna connector

WiFi connector type in Bedrock: **Female RP-SMA** (center pin)

![](../../../../.gitbook/assets/image-20230512-092939.png)

Use a **Male RP-SMA** WiFi antenna (center hole)

![](../../../../.gitbook/assets/image-20230512-093038.png)

## LTE/5G antenna connector

LTE/5G connector type in Bedrock: **Female SMA** (center hole)

![](../../../../.gitbook/assets/image-20230512-093331.png)

Use a **Male SMA** LTE/5G antenna (center pin)

![](../../../../.gitbook/assets/image-20230512-093408.png)
