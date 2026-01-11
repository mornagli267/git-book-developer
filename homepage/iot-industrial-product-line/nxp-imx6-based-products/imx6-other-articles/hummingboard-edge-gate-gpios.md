# HummingBoard Edge/Gate GPIOs

<a id="description"></a>

### Description

GPIO, or General-Purpose Input/Output is a mechanism that allows a computing board to provide electrical contacts for signalling to a wide range of external devices. These pins allow commercial and hobbyist projects to do things like communicate with a “breakout board”, or individual physical modules – like a motor. Below is the layout of the GPIOs on the HummingBoard Gate/Edge:

![](./attachments/image-20211226-133042.png)

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GPIO Number** | **GPIO Row** | **GPIO Column** |     |     |     |     | **GPIO Number** | **GPIO Row** | **GPIO Column** |
|     |     |     |     | **J21** |     |     |     |     |     |
|     |     |     | 3.2V | 1   | 2   | 5V  |     |     |     |
| 73  | 3   | 9   | DISP1\_DAT00 | 3   | 4   | DISP1\_DAT01 | 72  | 3   | 8   |
| 69  | 3   | 5   | DISP1\_DAT04 | 5   | 6   | DISP1\_DAT05 | 68  | 3   | 4   |
|     |     |     |     | **J23** |     |     |     |     |     |
| 77  | 3   | 13  | DI1\_D0\_CS | 1   | 2   | DI1\_D1\_CS | 78  | 3   | 14  |
| 65  | 3   | 1   | DISP1\_DAT08 | 3   | 4   | DISP1\_DAT09 | 64  | 3   | 0   |
| 53  | 2   | 21  | DISP1\_DAT12 | 5   | 6   | DISP1\_DAT13 | 52  | 2   | 20  |
| 49  | 2   | 17  | DISP1\_DAT16 | 7   | 8   | DISP1\_DAT17 | 48  | 2   | 16  |
| 95  | 3   | 31  | DISP1\_DAT20 | 9   | 10  | DISP1\_DAT21 | 94  | 3   | 30  |
|     |     |     | GND | 11  | 12  | DI1\_DISP\_CLK | 54  | 2   | 22  |
|     |     |     |     | **J22** |     |     |     |     |     |
| 74  | 3   | 10  | DI1\_PIN15 | 1   | 2   | DI1\_PIN02 | 75  | 3   | 11  |
| 71  | 3   | 7   | DISP1\_DATA02 | 3   | 4   | DISP1\_DATA03 | 70  | 3   | 6   |
| 67  | 3   | 3   | DISP1\_DATA06 | 5   | 6   | DISP1\_DATA07 | 66  | 3   | 2   |
|     |     |     |     | **J24** |     |     |     |     |     |
| 79  | 3   | 15  | DI1\_PIN01 | 1   | 2   | DI1\_PIN03 | 76  | 3   | 12  |
| 61  | 2   | 29  | DISP1\_DATA10 | 3   | 4   | DISP1\_DATA11 | 60  | 2   | 28  |
| 51  | 2   | 19  | DISP1\_DATA14 | 5   | 6   | DISP1\_DATA15 | 50  | 2   | 18  |
| 166 | 6   | 6   | DISP1\_DATA18 | 7   | 8   | DISP1\_DATA19 | 132 | 5   | 4   |
| 90  | 3   | 26  | DISP1\_DATA22 | 9   | 10  | DISP1\_DATA23 | 91  | 3   | 27  |
| 24  | 1   | 24  | SPDIF\_IN | 11  | 12  | SPDIF\_OUT | 204 | 7   | 12  |

<a id="pinout-names"></a>

### Pinout Names

These are all documented in the device-tree files. By default all are GPIO pins.

[https://github.com/SolidRun/linux-fslc/blob/3.14-1.0.x-mx6-sr/arch/arm/boot/dts/imx6qdl-hummingboard2.dtsi#L328](https://github.com/SolidRun/linux-fslc/blob/3.14-1.0.x-mx6-sr/arch/arm/boot/dts/imx6qdl-hummingboard2.dtsi#l328)