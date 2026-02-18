# i.MX6 SOM available I/Os

<a id="available-i-os"></a>

#### Available I/Os

The below table describes the available input/output of the i.MX6 SOM. Specific functions are detailed on the 1st column.

{% hint style="warning" %}
**Please note**
GPIOs marked in green take part in the booting process, please take special care on their state during reset.
{% endhint %}


|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Interface** | **Signals** | **GPIO** | **Connector Pin**  <br>**HB2/SOM** | **HB2** | **COMMENTS** |
|     |     |     |     |     |     |
| UART1 | TX  | (GPIO5\_IO28) | J7-52 (J8004) | Terminal (Buffered) | J-25 |
|     | RX  | (GPIO5\_IO29) | J7-54 (J8004) | Terminal (Buffered) | J-25 |
|     | CTS | (GPIO3\_IO20) | J5001-23 | NC  |     |
|     | RTS | (GPIO3\_IO19) | J5001-11 | NC  |     |
|     |     |     |     |     |     |
| UART2 | TX  | (GPIO2\_IO15) | J5001-46 | RS485-TX | J-35 |
|     | RX  | (GPIO2\_IO12) | J5001-44 | RS485-RX | J-35 |
|     | CTS | (GPIO2\_IO14) | J5001-48 | RS485-DE |     |
|     | RTS | (GPIO2\_IO13) | J5001-50 | V\_USB3 PWR\_EN |     |
|     |     |     |     |     |     |
| UART3 | TX  | (GPIO3\_IO24) | J5001-29 | MIKROBUS | U10002 |
|     | RX  | (GPIO3\_IO25) | J5001-31 | MIKROBUS | U10002 |
|     | CTS | (GPIO3\_IO24) | J5001-40 | NU  | J-23 (DISP1\_DATA21) |
|     | RTS | (GPIO3\_IO31) | J5001-58 | NU  | J-23 (DISP1\_DATA20) |
|     |     |     |     |     |     |
| UART4 | TX  | (GPIO4\_IO06) | J7-51 (J8004) | AUDIO CODEC | UART4 is used on the SOM on different pins |
|     | RX  | (GPIO4\_IO07) | J7-53 (J8004) | AUDIO CODEC | UART4 is used on the SOM on different pins |
|     |     |     |     |     |     |
| UART5 | TX  | (GPIO4\_IO08) | J7-73 (J8004) | AUDIO CODEC |     |
|     | RX  | (GPIO4\_IO09) | J7-55 (J8004) | SD2\_VSELECT | Select betweent 3.3V and 1.8V |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
| CAN | TX  | GPIO4\_IO10 | J5001-12 | CAN | J-28. Whne the HDMI is assembled there is no CAN interface |
|     | RX  | GPIO4\_IO11 | J7-23 (J8004) | HDMI/CAN | J-28. Whne the HDMI is assembled there is no CAN interface |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
| SPI | ECSPI2\_MISO | GPIO2\_IO25 | J9-45 (J5002) | MIKROBUS | U10002 |
|     | ECSPI2\_MOSI | GPIO2\_IO24 | J9-47 (J5002) | MIKROBUS | U10002 |
|     | ECSPI2\_SCLK | GPIO2\_IO23 | J9-49 (J5002) | MIKROBUS | U10002 |
|     | ECSPI2\_SS0 | GPIO2\_IO26 | J9-32 (J5002) | MIKROBUS | U10002 |
|     | ECSPI2\_SS1 | GPIO2\_IO27 | J9-34 (J5002) | MIKROBUS | U10002 |
|     |     |     |     |     |     |
| I2C1 | SCL | GPIO3\_IO21 | J9-51 (J5002) | MPCIe/AUDIO |     |
|     | SDA | GPIO3\_IO28 | J9-53 (J5002) | MPCIe/AUDIO |     |
|     |     |     |     |     |     |
| I2C3 | SCL | GPIO3\_IO17 | J9-33 (J5002) | MIKROBUS | U10002 |
|     | SDA | GPIO3\_IO18 | J9-31 (J5002) | MIKROBUS | U10002 |
|     |     |     |     |     |     |
| SPDIF | IN  | GPIO1\_IO24 | J5001-35 | NU  | J-24 |
|     | OUT | GPIO7\_IO17 | J7-50 (J8004) | NU  | J-24 |
|     |     |     |     |     |     |
| HDMI | HDMI\_CEC | GPIO5\_IO02 | J5001-17 | NC  |     |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
| IO  |     | GPIO1\_IO00 | J9-24 (J5002) | USB\_H1\_PWR\_EN |     |
|     |     | GPIO1\_IO01 | J7-56 (J8004) | USB\_OTG\_ID |     |
|     |     | GPIO1\_IO03 | J7-69 (J8004) | CAP\_TOUCH\_INT | J-6 |
|     |     | GPIO1\_IO07 | J5001-14 | NC  |     |
|     |     | GPIO1\_IO09 | J5001-42 | MIKROBUS | U10002 |
|     |     | GPIO1\_IO15 | J7-59 (J8004) | AUDIO CLK |     |
|     |     | GPIO1\_IO25 | J9-59 (J5002) | NC  |     |
|     |     |     |     |     |     |
|     |     | GPIO2\_IO08 | J5001-36 | msata\_DISABLE | U2027 |
|     |     | GPIO2\_IO09 | J9-55 (J5002) | DISP0\_CONTRAST | J-6 |
|     |     | GPIO2\_IO10 | J9-57 (J5002) | DSI Connectors | J-8 |
|     |     | GPIO2\_IO11 | J5001-38 | MPCIe RST# | J-5 |
|     |     | GPIO2\_IO16 | J5001-69 | NU  | J-23 (DISP1\_DATA17) |
|     |     | GPIO2\_IO17 | J5001-66 | NU  | J-23 (DISP1\_DATA16) |
|     |     | GPIO2\_IO18 | J5001-62 | NU  | J-24 (DISP1\_DATA15) |
|     |     | GPIO2\_IO19 | J5001-63 | NU  | J-24 (DISP1\_DATA14) |
|     |     | GPIO2\_IO20 | J5001-64 | NU  | J-23 (DISP1\_DATA13) |
|     |     | GPIO2\_IO21 | J5001-59 | NU  | J-23 (DISP1\_DATA12) |
|     |     | GPIO2\_IO22 | J5001-54 | NU  | J-23 (DI1\_DISP\_CLK) |
|     |     | GPIO2\_IO28 | J5001-68 | NU  | J-24 (DISP1\_DATA11) |
|     |     | GPIO2\_IO29 | J5001-57 | NU  |     |
|     |     | GPIO2\_IO30 | J5001-37 | NC  | (EIM\_EB2) |
|     |     | GPIO2\_IO31 | J5001-39 | NC  | (EIM\_EB3) |
|     |     |     |     |     |     |
|     |     | GPIO3\_IO00 | J5001-60 | NU  | J-23 (DISP1\_DATA09) |
|     |     | GPIO3\_IO01 | J5001-55 | NU  | J-23 (DISP1\_DATA08) |
|     |     | GPIO3\_IO02 | J5001-70 | NU  | J-22 (DISP1\_DATA07) |
|     |     | GPIO3\_IO03 | J9-58 (J5002) | NU  | J-22 (DISP1\_DATA06) |
|     |     | GPIO3\_IO04 | J9-62 (J5002) | NU  | J-21 (DISP1\_DATA05) |
|     |     | GPIO3\_IO05 | J9-64 (J5002) | BOOT | J-5005 (DISP1\_DATA04) |
|     |     | GPIO3\_IO06 | J9-54 (J5002) | BOOT | J-5005 (DISP1\_DATA03) |
|     |     | GPIO3\_IO07 | J9-56 (J5002) | NU  | J-22 (DISP1\_DATA02) |
|     |     | GPIO3\_IO08 | J9-60 (J5002) | NU  | J-21 (DISP1\_DATA01) |
|     |     | GPIO3\_IO09 | J9-66 (J5002) | NU  | J-21 (DISP1\_DATA00) |
|     |     | GPIO3\_IO10 | J5001-43 | NU  | J-22 (DI1\_PIN15) |
|     |     | GPIO3\_IO11 | J5001-41 | BOOT | J-5005 (DI1\_PIN02) |
|     |     | GPIO3\_IO12 | J5001-51 | BOOT | J-5005 (DI1\_PIN03) |
|     |     | GPIO3\_IO13 | J5001-45 | NU  | J-23 (DI1\_D0\_CS) |
|     |     | GPIO3\_IO14 | J5001-49 | NU  | J-23 (DI1\_D1\_CS) |
|     |     | GPIO3\_IO15 | J5001-53 | NU  | J-24 (DI1\_PIN01) |
|     |     | GPIO3\_IO16 | J5001-19 | NC  |     |
|     |     | GPIO3\_IO23 | J5001-25 | NC  |     |
|     |     | GPIO3\_IO26 | J5001-61 | NU  | J-24 (DISP1\_DATA22) |
|     |     | GPIO3\_IO27 | J5001-65 | NU  | J-24 (DISP1\_DATA23) |
|     |     | GPIO3\_IO29 | J5001-27 | NC  |     |
|     |     |     |     |     |     |
|     |     | GPIO4\_IO14 | J7-67 (J8004) | DSI Connector | J-6 |
|     |     | GPIO4\_IO29 | J9-68 (J5002) | MIKROBUS | U10002 |
|     |     | GPIO4\_IO30 | J9-41 (J5002) | uSD Power Cycle |     |
|     |     |     |     |     |     |
|     |     | GPIO5\_IO00 | J5001-1 | NC  | (EIM\_WAIT) |
|     |     | GPIO5\_IO04 | J5001-67 | NU  | J-24 (DISP1\_DATA19) |
|     |     | GPIO5\_IO13 | J7-57 (J8004) | AUD5\_RXD |     |
|     |     |     |     |     |     |
|     |     | GPIO6\_IO06 | J5001-56 | NU  | J-24 (DISP1\_DATA18) |
|     |     | GPIO6\_IO15 | J7-63 (J8004) | DSI Connector | J-8 |
|     |     |     |     |     |     |
|     |     | GPIO7\_IO09 | J5001-34 | IR\_RECEIVE |     |
|     |     | GPIO7\_IO10 | J5001-32 | USB4\_PWR\_EN |     |
|     |     | GPIO7\_IO13 | J5001-28 | A/D INT |     |