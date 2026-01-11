# i.MX6 SOM boot configuration pins

<a id="boot-configuration-pins"></a>

## Boot configuration pins

Below table described the available booting options :

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **IMX-6 Boot** | BT\_CFG1\_7 | BT\_CFG1\_6 | BT\_CFG1\_5 | BT\_CFG1\_4 | BT\_CFG2\_6 | BT\_CFG2\_5 | BT\_CFG2\_4 | BT\_CFG2\_3 | BT\_CFG4\_5 | BT\_CFG4\_4 | BT\_CFG4\_2 | BT\_CFG4\_1 | BT\_CFG4\_0 |
|     | 011X = eMMC Boot |     |     |     | 00 = 1-bit  <br>00 = 1 – bit |     | 10 = SD3 Boot |     | XX  |     | XX  |     |     |
|     | 010X = SD Boot |     |     |     | 00 = 1-bit |     | 01 = SD2 Boot |     | XX  |     | XX  |     |     |
|     | 0011 = Serial ROM Boot |     |     |     | XX  |     | XX  |     | 00 – SPIx\_SS0  <br>01 – SPIx\_SS1 |     | 000 – SPI-1 |     |     |
|     | 0010 = SATA |     |     |     | XX  |     | X0  |     | XX  |     | XX  |     |     |

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Boot Mode** | BT\_CFG1\_7 | BT\_CFG1\_6 | BT\_CFG1\_5 | BT\_CFG1\_4 | BT\_CFG1\_3 | BT\_CFG1\_2 | BT\_CFG1\_1 | BT\_CFG1\_0 | BT\_CFG2\_7 | BT\_CFG2\_6 | BT\_CFG2\_5 | BT\_CFG2\_4 | BT\_CFG2\_3 | BT\_CFG2\_2 | BT\_CFG2\_1 | BT\_CFG2\_0 |
| **Schematics signals** | DISP1\_DATA02 | DISP1\_DATA03 | DISP1\_DATA04 | DISP1\_DATA05 | DISP1\_DATA06 | DISP1\_DATA07 | DISP1\_DATA08 | DISP1\_DATA09 | DI1\_PIN01 | DI1\_D1\_CS | DI1\_D0\_CS | DI1\_PIN03 | DI1\_PIN02 | DI1\_PIN15 | DISP1\_DATA00 | DISP1\_DATA01 |
| **i.MX6 Datasheet** | EIM\_DA7 | EIM\_DA7 | EIM\_DA5 | EIM\_DA4 | EIM\_DA3 | EIM\_DA2 | EIM\_DA1 | EIM\_DA0 | EIM\_DA15 | EIM\_DA14 | EIM\_DA13 | EIM\_DA12 | EIM\_DA11 | EIM\_DA10 | EIM\_DA9 | EIM\_DA8 |
| **HummingBoard2 Connector** | J9/56 | J9/54 | J9/64 | J9/62 | J9/58 | J5001/70 | J5001/55 | J5001/60 | J5001/52 | J5001/49 | J5001/45 | J5001/51 | J5001/41 | J5001/43 | J9/66 | J9/60 |

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Boot Mode** | BT\_CFG3\_7 | BT\_CFG3\_6 | BT\_CFG3\_5 | BT\_CFG3\_4 | BT\_CFG3\_3 | BT\_CFG3\_2 | BT\_CFG3\_1 | BT\_CFG3\_0 | BT\_CFG4\_7 | BT\_CFG4\_6 | BT\_CFG4\_5 | BT\_CFG4\_4 | BT\_CFG4\_3 | BT\_CFG4\_2 | BT\_CFG4\_1 | BT\_CFG4\_0 |
| **Schematics signals** | DISP1\_DATA18 | DISP1\_DATA17 | DISP1\_DATA16 | DISP1\_DATA15 | DISP1\_DATA14 | DISP1\_DATA13 | DISP1\_DATA12 | DI1\_DISP\_CLK | EIM\_EB3 | EIM\_EB2 | ECSPI2\_SS0 | DISP1\_DATA10 | DISP1\_DATA11 | ECSPI2\_SS1 | EIM\_WAIT | DISP1\_DATA19 |
| **i.MX6 Datasheet** | EIM\_A23 | EIM\_A22 | EIM\_A21 | EIM\_A20 | EIM\_A19 | EIM\_A18 | EIM\_A17 | EIM\_A16 | EIM\_EB3 | EIM\_EB2 | EIM\_RW | EIM\_EB1 | EIM\_EB0 | EIM\_LBA | EIM\_WAIT | EIM\_A24 |
| **HummingBoard2 Connector** | J5001/56 | J5001/69 | J5001/66 | J5001/62 | J5001/63 | J5001/64 | J5001/59 | J5001/54 | J5001/39 | J5001/37 | J9/32 | J5001/57 | J5001/68 | J9/34 | J5001/1 | J5001/67 |

Below is an example for a start up sequence :

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|     | BT\_CFG1\_6 | BT\_CFG1\_5 | BT\_CFG2\_4 | BT\_CFG2\_3 |
|     | DISP1\_DATA03 | DISP1\_DATA04 | DI1\_PIN03 | DI1\_PIN02 |
| eMMC | 1   | 1   | 1   | 0   |
| uSD | 1   | 0   | 0   | 1   |