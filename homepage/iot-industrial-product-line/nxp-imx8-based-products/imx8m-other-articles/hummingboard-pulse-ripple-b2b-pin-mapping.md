# HummingBoard Pulse/Ripple B2B Pin Mapping

<a id="background"></a>

## Background

Below tables reference the HummingBoard Pulse rev 2.4 pin mapping description for all the i.MX8M SOM variants (i.MX8M,i.MX8M Mini,i.MX8M Plus). All the SOMs share a similar pinout, thus allowing them to be used on the same development platform.

<a id="j5001-connector"></a>

## J5001 connector

| **PIN** | **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |     | **PIN** | **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | TP4 | PMIC\_ON | NC  | NC  |     | 2   | NC  | NC  | DSI\_EN, [GPIO1.IO](http://GPIO1.IO)\[08\] | DSI\_EN, [GPIO1.IO](http://GPIO1.IO)\[08\] |
| 3   | DIP-SWITCH | BOOT\_MODE0 | BOOT\_MODE0 | BOOT\_MODE0 |     | 4   | DSI-CON (J19) or DSI-HDMI | DSI\_DN3 | DSI\_DN3 | DSI\_DN3 |
| 5   | DIP-SWITCH | BOOT\_MODE1 | BOOT\_MODE1 | BOOT\_MODE1 |     | 6   | DSI-CON (J19) or DSI-HDMI | DSI\_DP3 | DSI\_DP3 | DSI\_DP3 |
| 7   | GND | GND | GND | GND |     | 8   | GND | GND | DSI\_TS\_Nint, [GPIO1.IO](http://GPIO1.IO)\[09\] | GND |
| 9   | DSI-CON (J19) or DSI-HDMI | DSI\_CKP | DSI\_CKP | DSI\_CKP |     | 10  | GND | GND | GND | GND |
| 11  | DSI-CON (J19) or DSI-HDMI | DSI\_CKN | DSI\_CKN | DSI\_CKN |     | 12  | DSI-CON (J19) or DSI-HDMI | DSI\_DN0 | DSI\_DN0 | DSI\_DN0 |
| 13  | GND | GND | GND | GND |     | 14  | DSI-CON (J19) or DSI-HDMI | DSI\_DP0 | DSI\_DP0 | DSI\_DP0 |
| 15  | DSI-CON (J19) or DSI-HDMI | DSI\_DN2 | DSI\_DN2 | DSI\_DN2 |     | 16  | GND | GND | GND | GND |
| 17  | DSI-CON (J19) or DSI-HDMI | DSI\_DP2 | DSI\_DP2 | DSI\_DP2 |     | 18  | Mini-PCIe (J20, optional) | PCIE1\_REF\_CLKP\_CN | NC  | LVDS0\_CLK\_P |
| 19  | GND | GND | GND | GND |     | 20  | Mini-PCIe (J20, optional) | PCIE1\_REF\_CLKN\_CN | NC  | LVDS0\_CLK\_N |
| 21  | DSI-CON (J19) or DSI-HDMI | DSI\_DN1 | DSI\_DN1 | DSI\_DN1 |     | 22  | GND | GND | GND | GND |
| 23  | DSI-CON (J19) or DSI-HDMI | DSI\_DP1 | DSI\_DP1 | DSI\_DP1 |     | 24  | M.2\_W\_DIS# | PCIE\_nPME, [GPIO3.IO](http://GPIO3.IO)\[5 | PCIE\_CLKREQ, [GPIO1.IO](http://GPIO1.IO)\[12\] | M.2\_W\_DIS#, [GPIO1.IO](http://GPIO1.IO)\[13\] |
| 25  | GND | GND | GND | GND |     | 26  | Mini-PCIe\_W\_DIS# | PCIe\_nWAKE, [GPIO3.IO](http://GPIO3.IO)\[12\] | PCIe\_Nwake, [GPIO2.IO](http://GPIO2.IO)\[20\] | Mini-PCIe\_W\_DIS#, [GPIO1.IO](http://GPIO1.IO)\[05\] |
| 27  | M.2\_WAKW\_ON\_LAN (PCIe) | PWM1\_OUT, [GPIO1.IO](http://GPIO1.IO)\[1\] | DSI\_BL\_PWM,[GPIO1.IO](http://GPIO1.IO)\[01\] | M.2\_WAKW\_ON\_LAN,[GPIO1.IO](http://GPIO1.IO)\[12\] |     | 28  | USB1\_PWR\_EN | USB1\_SS\_SEL, [GPIO3.IO](http://GPIO3.IO)\[15\] | PCIe\_nRST, [GPIO4.IO](http://GPIO4.IO)\[21\] | USB1\_PWR\_EN, [GPIO1.IO](http://GPIO1.IO)\[15\] |
| 29  | MIKROBUS (J10-4) | UART3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[27\] | UART1\_TXD, [GPIO5.IO](http://GPIO5.IO)\[23\] | UART3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[7\] |     | 30  | GND | GND | GND | GND |
| 31  | MIKROBUS (J10-3) | UART3\_RXD, [GPIO5.IO](http://GPIO5.IO)\[26\] | UART1\_RXD, [GPIO5.IO](http://GPIO5.IO)\[22\] | UART3\_RXD, [GPIO5.IO](http://GPIO5.IO)\[6\] |     | 32  | Mini-PCIe (J20, optional) | PCIE1\_TXP\_C | NC  | LVDS0\_TX2\_N |
| 33  | GND | GND | GND | GND |     | 34  | Mini-PCIe (J20, optional) | PCIE1\_TXN\_C | NC  | LVDS0\_TX2\_P |
| 35  | NC  | NC  | PCIe\_nDIS, [GPIO1.IO](http://GPIO1.IO)\[05\] | NC  |     | 36  | GND | GND | GND | GND |
| 37  | MIKROBUS (J10-1) | UART3\_CTS, [GPIO5.IO](http://GPIO5.IO)\[8\] | UART1\_CTS, [GPIO5.IO](http://GPIO5.IO)\[26\] | UART3\_CTS, [GPIO5.IO](http://GPIO5.IO)\[8\] |     | 38  | Mini-PCIe (J20, optional) | PCIE1\_RXP\_C | NC  | LVDS0\_TX3\_N |
| 39  | MIKROBUS (J10-2) | UART3\_RTS, [GPIO5.IO](http://GPIO5.IO)\[9\] | UART1\_RTS, [GPIO5.IO](http://GPIO5.IO)\[27\] | UART3\_RTS, [GPIO5.IO](http://GPIO5.IO)\[9\] |     | 40  | Mini-PCIe (J20, optional) | PCIE1\_RXN\_C | NC  | LVDS0\_TX3\_P |
| 41  | HEADER, DIP-SW | SAI1\_TXD2, [GPIO4.IO](http://GPIO4.IO)\[14\] (BT\_CFG10) | SAI1\_TXD2, [GPIO4.IO](http://GPIO4.IO)\[14\] (BT\_CFG10) | SAI2\_TXC, [GPIO4.IO](http://GPIO4.IO)\[25\] |     | 42  | GND | GND | GND | GND |
| 43  | DSI\_TS\_nINT (DSI-HDMI) | DSI\_TS\_nINT, [GPIO5.IO](http://GPIO5.IO)\[7\] | CSI\_PWDN, [GPIO1.IO](http://GPIO1.IO)\[07\] | SAI2\_MCLK, [GPIO4.IO](http://GPIO4.IO)\[27\] |     | 44  | LED (D34) | UART2\_RXD, [GPIO5.IO](http://GPIO5.IO)\[24\] | UART3\_RXD, [GPIO5.IO](http://GPIO5.IO)\[6\] | SAI2\_RXC, [GPIO4.IO](http://GPIO4.IO)\[22\] (UART1\_RX) |
| 45  | NC  | NC  | MIPI\_CSI0\_MCLK\_OUT, [GPIO1.IO](http://GPIO1.IO)\[14\] | SAI2\_TXD, [GPIO4.IO](http://GPIO4.IO)\[26\] |     | 46  | LED (D33) | UART2\_TXD, [GPIO5.IO](http://GPIO5.IO)\[25\] | UART3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[7\] | SAI2\_RXFS, [GPIO4.IO](http://GPIO4.IO)\[21\] (UART1\_TX) |
| 47  | GND | GND | GND | GND |     | 48  | LED (D32) | UART2\_CTS, [GPIO5.IO](http://GPIO5.IO)\[28\] | UART3\_CTS, [GPIO5.IO](http://GPIO5.IO)\[8\] | SAI2\_RXD, [GPIO4.IO](http://GPIO4.IO)\[23\] (UART1\_CTS) |
| 49  | NC  | NC  | MIPI\_CSI0\_RST#, [GPIO1.IO](http://GPIO1.IO)\[06\] | LVDS0\_TX1\_N |     | 50  | LED (D31) | UART2\_RTS, [GPIO5.IO](http://GPIO5.IO)\[29\] | UART3\_RTS, [GPIO5.IO](http://GPIO5.IO)\[9\] | SAI2\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[24\] (UART1\_RTS) |
| 51  | HEADER, DIP-SW | SAI1\_TXD4, [GPIO4.IO](http://GPIO4.IO)\[16\] (BT\_CFG12) | SAI1\_TXD4, [GPIO4.IO](http://GPIO4.IO)\[16\] (BT\_CFG12) | LVDS0\_TX1\_P |     | 52  | GND | GND | GND | GND |
| 53  | WIFI\_DP (HUB to IMX8M) | WIFI\_USB\_DP | I2C4\_SCL | LVDS0\_TX0\_N |     | 54  | CSI-CON(CON7) | CSI\_P1\_DN0 | CSI\_DN0 | CSI\_DN0 |
| 55  | WIFI\_DN (HUB to IMX8M) | WIFI\_USB\_DN | I2C4\_SDA | LVDS0\_TX0\_P |     | 56  | CSI-CON(CON7) | CSI\_P1\_DP0 | CSI\_DP0 | CSI\_DP0 |
| 57  | GND | GND | GND | GND |     | 58  | GND | GND | GND | GND |
| 59  | CSI-CON(CON7) | CSI\_P1\_CKP | CSI\_CKP | CSI\_CKP |     | 60  | CSI-CON(CON7) | CSI\_P1\_DP2 | CSI\_DP2 | CSI\_DP2 |
| 61  | CSI-CON(CON7) | CSI\_P1\_CKN | CSI\_CKN | CSI\_CKN |     | 62  | CSI-CON(CON7) | CSI\_P1\_DN2 | CSI\_DN2 | CSI\_DN2 |
| 63  | GND | GND | GND | GND |     | 64  | GND | GND | GND | GND |
| 65  | CSI-CON(CON7) | CSI\_P1\_DP3 | CSI\_DP3 | CSI\_DP3 |     | 66  | CSI-CON(CON7) | CSI\_P1\_DP1 | CSI\_DP1 | CSI\_DP1 |
| 67  | CSI-CON(CON7) | CSI\_P1\_DN3 | CSI\_DP3 | CSI\_DP3 |     | 68  | CSI-CON(CON7) | CSI\_P1\_DN1 | CSI\_DN1 | CSI\_DN1 |
| 69  | GND | GND | GND | GND |     | 70  | GND | GND | GND | GND |

<a id="j7-connector"></a>

## J7 connector

| **PIN** | **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |     | **PIN** | **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | ETH\_NIC (Intel, U6) | PCIE2\_REF\_CLKP\_CN | PCIEC\_CLKN (Optional) | PCIEC\_CLKN |     | 2   | ETH\_NIC (Intel, U6) | PCIE2\_RXN | PCIEC\_RXN (Optional) | PCIE\_RXN |
| 3   | ETH\_NIC (Intel, U6) | PCIE2\_REF\_CLKN\_CN | PCIEC\_CLKP (Optional) | PCIEC\_CLKP |     | 4   | ETH\_NIC (Intel, U6) | PCIE2\_RXP | PCIEC\_RXP (Optional) | PCIE\_RXP |
| 5   | GND | GND | GND | GND |     | 6   | GND | GND | GND | GND |
| 7   | ETH\_NIC (Intel, U6) | PCIE2\_TXN | PCIEC\_TXN (Optional) | PCIEC\_TXN |     | 8   | HEADER (CON4) | SAI3\_MCLK, [GPIO5.IO](http://GPIO5.IO)\[2\] | SAI3\_MCLK, [GPIO5.IO](http://GPIO5.IO)\[2\] | NC  |
| 9   | ETH\_NIC (Intel, U6) | PCIE2\_TXP | PCIEC\_TXP (Optional) | PCIEC\_TXP |     | 10  | HEADER (CON4) | SAI3\_RXC, [GPIO4.IO](http://GPIO4.IO)\[29\] | SAI3\_RXC, [GPIO4.IO](http://GPIO4.IO)\[29\] | Mini-PCIe\_PREST#, [GPIO1.IO](http://GPIO1.IO)\[01\] |
| 11  | GND | GND | GND | GND |     | 12  | HEADER (CON4) | SAI1\_TXC, [GPIO4.IO](http://GPIO4.IO)\[11\] | SAI1\_TXC, [GPIO4.IO](http://GPIO4.IO)\[11\] | SPDIF\_RX, [GPIO5.IO](http://GPIO5.IO)\[4\] |
| 13  | M.2\_RESET# | SAI3\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[31\] | SAI3\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[31\] | M.2\_RESET#, [GPIO1.IO](http://GPIO1.IO)\[06\] |     | 14  | POE\_AT\_DET | SAI3\_TXC [GPIO5.IO](http://GPIO5.IO)\[0\] | SAI3\_TXC, [GPIO5.IO](http://GPIO5.IO)\[0\] | POE\_AT\_DET, [GPIO1.IO](http://GPIO1.IO)\[09\] |
| 15  | RTC\_CLKO (RTC Int.) | SAI3\_RXFS, [GPIO4.IO](http://GPIO4.IO)\[28\] | SAI3\_RXFS, [GPIO4.IO](http://GPIO4.IO)\[28\] | NC  |     | 16  | DSI-CON (J19) or DSI-HDMI | SPDIF\_TX, [GPIO5.IO](http://GPIO5.IO)\[3\] | SPDIF\_TX, [GPIO5.IO](http://GPIO5.IO)\[3\] | SPDIF\_TX, [GPIO5.IO](http://GPIO5.IO)\[3\] |
| 17  | GND | GND | GND | GND |     | 18  | M.2\_PCIe\_3V3\_EN | IR\_CAP, [GPIO1.IO](http://GPIO1.IO)\[12\] | IR\_CAP, [GPIO1.IO](http://GPIO1.IO)\[13\] | M.2\_PCIe\_3V3\_EN, [GPIO1.IO](http://GPIO1.IO)\[10\] |
| 19  | HDMI CON (J1) | HDMI\_TXP2 | NC  | HDMI\_TXP2 |     | 20  | HEADER (CON4) | SAI1\_TXD7, [GPIO4.IO](http://GPIO4.IO)\[19\] (BT\_CFG15) | SAI1\_TXD7, [GPIO4.IO](http://GPIO4.IO)\[19\] (BT\_CFG15) | SPDIF\_EXT\_CLK, [GPIO5.IO](http://GPIO5.IO)\[5\] |
| 21  | HDMI CON (J1) | HDMI\_TXN2 | CLKOUT1 | HDMI\_TXN2 |     | 22  | HEADER (CON4) | SAI1\_TXD0, [GPIO4.IO](http://GPIO4.IO)\[12\] (BT\_CFG8) | SAI1\_TXD0, [GPIO4.IO](http://GPIO4.IO)\[12\] (BT\_CFG8) | NC  |
| 23  | GND | GND | CLKOUT2 | GND |     | 24  | HEADER (CON4) | SAI1\_TXD1, [GPIO4.IO](http://GPIO4.IO)\[13\] (BT\_CFG9) | SAI1\_TXD1, [GPIO4.IO](http://GPIO4.IO)\[13\] (BT\_CFG9) | DSI\_EN, [GPIO1.IO](http://GPIO1.IO)\[08\] |
| 25  | HDMI CON (J1) | HDMI\_TXP1 | NC  | HDMI\_TXP1 |     | 26  | USB-HUB\_RST# | SAI3\_RXD, [GPIO4.IO](http://GPIO4.IO)\[30\] | SAI3\_RXD, [GPIO4.IO](http://GPIO4.IO)\[30\] | USB-HUB\_RST#, [GPIO1.IO](http://GPIO1.IO)\[15\] |
| 27  | HDMI CON (J1) | HDMI\_TXN1 | NC  | HDMI\_TXN1 |     | 28  | HEADER (CON4) | SAI1\_TXD3, [GPIO4.IO](http://GPIO4.IO)\[15\] (BT\_CFG11) | SAI1\_TXD6, [GPIO4.IO](http://GPIO4.IO)\[18\] (BT\_CFG14) | QSPIA\_DATA0, [GPIO3.IO](http://GPIO3.IO)\[6\] |
| 29  | GND | GND | NC  | GND |     | 30  | HEADER (CON4) | SAI1\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[10\] | SAI1\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[10\] | QSPIA\_DATA1, [GPIO3.IO](http://GPIO3.IO)\[7\] |
| 31  | HDMI CON (J1) | HDMI\_TXP0 | NC  | HDMI\_TXP0 |     | 32  | TP6 | nWDOG, [GPIO1.IO](http://GPIO1.IO)\[2\] | SAI3\_RXC, [GPIO4.IO](http://GPIO4.IO)\[29\] | QSPIA\_DATA2, [GPIO3.IO](http://GPIO3.IO)\[8\] |
| 33  | HDMI CON (J1) | HDMI\_TXN0 | NC  | HDMI\_TXN0 |     | 34  | NC  | NC  | SYS\_STATUS, [GPIO3.IO](http://GPIO3.IO)\[16\] | QSPIA\_DATA3, [GPIO3.IO](http://GPIO3.IO)\[9\] |
| 35  | GND | GND | NC  | GND |     | 36  | HEADER (CON4) | SAI1\_MCLK, [GPIO4.IO](http://GPIO4.IO)\[20\] | SAI1\_MCLK, [GPIO4.IO](http://GPIO4.IO)\[20\] | QSPIA\_Nss0, [GPIO3.IO](http://GPIO3.IO)\[1\] |
| 37  | HDMI CON (J1) | HDMI\_CLKP | NC  | HDMI\_CLKP |     | 38  | CSI-CON(CON7) | CLKO2, [GPIO1.IO](http://GPIO1.IO)\[15\] | UART2\_CTS, [GPIO5.IO](http://GPIO5.IO)\[28\] | UART4\_TXD, [GPIO5.IO](http://GPIO5.IO)\[29\] |
| 39  | HDMI CON (J1) | HDMI\_CLKN | CLKIN1 | HDMI\_CLKN |     | 40  | NC  | NC  | NC  | QSPIA\_SCLK, [GPIO3.IO](http://GPIO3.IO)\[0\] |
| 41  | GND | GND | GND | GND |     | 42  | GND | GND | GND | GND |
| 43  | HDMI CON (J1) | HDMI\_CEC | CLKIN2 | HDMI\_CEC |     | 44  | LED (D30) | [GPIO5.IO](http://GPIO5.IO)\[21\] | UART2\_RTS, [GPIO5.IO](http://GPIO5.IO)\[29\] | UART4\_RXD, [GPIO5.IO](http://GPIO5.IO)\[28\] |
| 45  | HDMI CON (J1) | HDMI\_DDC\_SCL | NC  | HDMI\_DDC\_SCL |     | 46  | HEADER (CON4) | SAI1\_RXD7, [GPIO4.IO](http://GPIO4.IO)\[9\] (BT\_CFG7) | SAI1\_RXD7, [GPIO4.IO](http://GPIO4.IO)\[9\] (BT\_CFG7) | MB-RST, [GPIO1.IO](http://GPIO1.IO)\[0\] |
| 47  | HDMI CON (J1) | HDMI\_DDC\_SDA | NC  | HDMI\_DDC\_SDA |     | 48  | GND | GND | GND | GND |
| 49  | HDMI CON (J1) | HDMI\_HPD | TEST\_MODE | HDMI\_HPD |     | 50  | HEADER (CON4) | SAI1\_RXD5, [GPIO4.IO](http://GPIO4.IO)\[7\] (BT\_CFG5) | SAI1\_RXD5, [GPIO4.IO](http://GPIO4.IO)\[7\] (BT\_CFG5) | USB2\_ID |
| 51  | AUDIO CODEC | SAI2\_TXC, [GPIO4.IO](http://GPIO4.IO)\[25\] | SAI2\_TXC, [GPIO4.IO](http://GPIO4.IO)\[25\] | SAI3\_TXC,[GPIO5.IO](http://GPIO5.IO)\[0\] |     | 52  | TERMINAL\_TX | UART1\_TXD (Terminal), [GPIO5.IO](http://GPIO5.IO)\[23\] | UART2\_TXD (Terminal), [GPIO5.IO](http://GPIO5.IO)\[25\] | UART2\_TXD (Terminal), [GPIO5.IO](http://GPIO5.IO)\[25\] |
| 53  | AUDIO CODEC | SAI2\_TXD, [GPIO4.IO](http://GPIO4.IO)\[26\] | SAI2\_TXD, [GPIO4.IO](http://GPIO4.IO)\[26\] | SAI3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[1\] |     | 54  | TERMINAL\_RX | UART1\_RXD (Terminal), [GPIO5.IO](http://GPIO5.IO)\[22\] | UART2\_RXD (Terminal), [GPIO5.IO](http://GPIO5.IO)\[24\] | UART2\_RXD (Terminal), [GPIO5.IO](http://GPIO5.IO)\[24\] |
| 55  | AUDIO CODEC | SAI2\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[24\] | SAI2\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[24\] | SAI3\_TXFS, [GPIO4.IO](http://GPIO4.IO)\[31\] |     | 56  | NC  | USB1\_ID | USB1\_ID | USB1\_ID |
| 57  | AUDIO CODEC | SAI2\_RXD, [GPIO4.IO](http://GPIO4.IO)\[23\] | SAI2\_RXD, [GPIO4.IO](http://GPIO4.IO)\[23\] | SAI3\_RXD, [GPIO4.IO](http://GPIO4.IO)\[30\] |     | 58  | GND | GND | GND | GND |
| 59  | AUDIO CODEC | SAI2\_MCLK, [GPIO4.IO](http://GPIO4.IO)\[27\] | SAI2\_MCLK, [GPIO4.IO](http://GPIO4.IO)\[27\] | SAI3\_MCLK, [GPIO5.IO](http://GPIO5.IO)\[2\] |     | 60  | USB-HUB | USB2\_RXP | NC  | USB2\_RXP |
| 61  | GND | GND | GND | GND |     | 62  | USB-HUB | USB2\_RXN | NC  | USB2\_RXN |
| 63  | HEADER (CON4) | SAI1\_RXD6, [GPIO4.IO](http://GPIO4.IO)\[8\] (BT\_CFG6) | SAI1\_RXD6, [GPIO4.IO](http://GPIO4.IO)\[8\] (BT\_CFG6) | SAI3\_RXC, [GPIO4.IO](http://GPIO4.IO)\[29\] |     | 64  | GND | GND | GND | GND |
| 65  | RESET-B | SYS\_nRST | SYS\_nRST | SYS\_nRST |     | 66  | USB-HUB | USB2\_TXN | NC  | USB2\_TXN |
| 67  | HEADER (CON4) | SAI1\_RXD4, [GPIO4.IO](http://GPIO4.IO)\[6\] (BT\_CFG4) | SAI1\_RXD4, [GPIO4.IO](http://GPIO4.IO)\[6\] (BT\_CFG4) | ETH1\_TRX3\_P (Second ETH) |     | 68  | USB-HUB | USB2\_TXP | NC  | USB2\_TXP |
| 69  | HEADER (CON4) | SAI1\_RXC, [GPIO4.IO](http://GPIO4.IO)\[1\] | SAI1\_RXC, [GPIO4.IO](http://GPIO4.IO)\[1\] | ETH1\_TRX3\_N (Second ETH) |     | 70  | GND | GND | GND | GND |
| 71  | HEADER (CON4) | SAI1\_RXFS, | SAI1\_RXFS, [GPIO4.IO](http://GPIO4.IO)\[0\] | ETH1\_TRX2\_P (Second ETH) |     | 72  | HEADER (CON4) | SAI1\_RXD2, [GPIO4.IO](http://GPIO4.IO)\[4\] (BT\_CFG2) | SAI1\_RXD2, [GPIO4.IO](http://GPIO4.IO)\[4\] (BT\_CFG2) | ETH1\_TRX1\_P (Second ETH) |
| 73  | MICRO-SD | SD2\_VSELECT, [GPIO1.IO](http://GPIO1.IO)\[4\] | USB2\_ID (Pull-Up, 3V3) | ETH1\_TRX2\_N (Second ETH) |     | 74  | HEADER (CON4) | SAI1\_RXD3, [GPIO4.IO](http://GPIO4.IO)\[5\] (BT\_CFG3) | SAI1\_RXD3, [GPIO4.IO](http://GPIO4.IO)\[5\] (BT\_CFG3) | ETH1\_TRX1\_N (Second ETH) |
| 75  | GND | GND | GND | GND |     | 76  | GND | GND | GND | GND |
| 77  | HDMI CON (J1) | HDMI\_AUXP | NC  | EARC\_N\_HPD |     | 78  | HEADER (CON4) | SAI1\_RXD0, [GPIO4.IO](http://GPIO4.IO)\[2\] (BT\_CFG0) | SAI1\_RXD0, [GPIO4.IO](http://GPIO4.IO)\[2\] (BT\_CFG0) | ETH1\_TRX0\_P (Second ETH) |
| 79  | HDMI CON (J1) | HDMI\_AUXN | NC  | EARC\_P\_UTIL |     | 80  | HEADER (CON4) | SAI1\_RXD1, [GPIO4.IO](http://GPIO4.IO)\[3\] (BT\_CFG1) | SAI1\_RXD1, [GPIO4.IO](http://GPIO4.IO)\[3\] (BT\_CFG1) | ETH1\_TRX0\_N (Second ETH) |

<a id="j9-connector"></a>

## J9 connector

| **PIN** | **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |     | **PIN** | **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | ETH-POE | MDI\_TRXN3 | MDI\_TRXN3 | MDI\_TRXN3 |     | 2   | GND | GND | GND | GND |
| 3   | ETH-POE | MDI\_TRXP3 | MDI\_TRXP3 | MDI\_TRXP3 |     | 4   | USB-TYPE-A | USB1\_TXP | NC  | USB1\_TXP |
| 5   | GND | GND | GND | GND |     | 6   | USB-TYPE-A | USB1\_TXN | NC  | USB1\_TXN |
| 7   | ETH-POE | MDI\_TRXN2 | MDI\_TRXN2 | MDI\_TRXN2 |     | 8   | GND | GND | GND | GND |
| 9   | ETH-POE | MDI\_TRXP2 | MDI\_TRXP2 | MDI\_TRXP2 |     | 10  | USB-TYPE-A | USB1\_RXP | NC  | USB1\_RXP |
| 11  | GND | GND | GND | GND |     | 12  | USB-TYPE-A | USB1\_RXN | NC  | USB1\_RXN |
| 13  | ETH-POE | MDI\_TRXN1 | MDI\_TRXN1 | MDI\_TRXN1 |     | 14  | GND | GND | GND |     |
| 15  | ETH-POE | MDI\_TRXP1 | MDI\_TRXP1 | MDI\_TRXP1 |     | 16  | USB-TYPE-A | USB1\_DP | USB1\_DP | USB1\_DP |
| 17  | GND | GND | GND | GND |     | 18  | USB-TYPE-A | USB1\_DN | USB1\_DN | USB1\_DN |
| 19  | ETH-POE | MDI\_TRXN0 | MDI\_TRXN0 | MDI\_TRXN0 |     | 20  | GND | GND | GND | GND |
| 21  | ETH-POE | MDI\_TRXP0 | MDI\_TRXP0 | MDI\_TRXP0 |     | 22  | USB-HUB | USB2\_DP | USB2\_DP | USB2\_DP |
| 23  | GND | GND | GND | GND |     | 24  | USB-HUB | USB2\_DN | USB2\_DN | USB2\_DN |
| 25  | ETH-LED | LED\_10\_100\_LED\_1000 | LED\_10\_100\_LED\_1000 | LED\_0/PHY\_CFG0 |     | 26  | GND | GND | GND | GND |
| 27  | ETH-LED | LED\_ACT | LED\_ACT | LED1\_0/PHY\_CFG0 |     | 28  | M.2\_GPS\_EN# | USB\_H1\_PWR\_EN, [GPIO3.IO](http://GPIO3.IO)\[4\] | SAI5\_RXFS,[GPIO3.IO](http://GPIO3.IO)\[19\] | M.2\_GPS\_EN#, [GPIO1.IO](http://GPIO1.IO)\[07\] |
| 29  | HEADER (CON4) | PPS (Eth PHY) | PPS (Eth PHY) | NC  |     | 30  | J9-59 (BT\_FW\_FLASH, J9-59) | USB\_OTG\_PWR\_EN, [GPIO3.IO](http://GPIO3.IO)\[2\] | SPDIF\_EXT\_CLK, [GPIO5.IO](http://GPIO5.IO)\[05\] | NC  |
| 31  | MIPI-DSI, ETH-NIC, DSI-CON, CSI-CON, RTC, MIKROBUS | I2C3\_SCL | I2C3\_SCL | I2C3\_SCL |     | 32  | MIKROBUS (J8-3) | ECSPI2\_SS0, [GPIO5.IO](http://GPIO5.IO)\[13\] | ECSPI2\_SS0, [GPIO5.IO](http://GPIO5.IO)\[13\] (UART4\_RTS) | ECSPI2\_SS0, [GPIO5.IO](http://GPIO5.IO)\[13\] |
| 33  | MIPI-DSI, ETH-NIC, DSI-CON, CSI-CON, RTC, MIKROBUS | I2C3\_SDA | I2C3\_SDA | I2C3\_SDA |     | 34  | CSI-CON (J19) or DSI-HDMI | [GPIO5.IO](http://GPIO5.IO)\[6\] | PDM\_DATA1, [GPIO3.IO](http://GPIO3.IO)\[22\] | NC  |
| 35  | GND | GND | GND | GND |     | 36  | GND | GND | GND | GND |
| 37  | USB\_HUB\_CH1\_PWR\_EN | CSI\_nRST, [GPIO1.IO](http://GPIO1.IO)\[6\] | TCPC\_Nint1, [GPIO2.IO](http://GPIO2.IO)\[11\] | USB\_HUB\_CH1\_PWR\_EN, [GPIO1.IO](http://GPIO1.IO)\[14\] |     | 38  | MICRO-SD | SD2\_CLK, [GPIO2.IO](http://GPIO2.IO)\[13\] | SD2\_CLK, [GPIO2.IO](http://GPIO2.IO)\[13\] | SD2\_CLK, [GPIO2.IO](http://GPIO2.IO)\[13\] |
| 39  | J9-55 (BT\_FW\_FLASH, J9-55) | AUD\_nMUTE, [GPIO1.IO](http://GPIO1.IO)\[8\] | PDM\_DATA0, [GPIO3.IO](http://GPIO3.IO)\[21\] | NC  |     | 40  | MICRO-SD | SD2\_CMD, [GPIO2.IO](http://GPIO2.IO)\[14\] | SD2\_CMD, [GPIO2.IO](http://GPIO2.IO)\[14\] | SD2\_CMD, [GPIO2.IO](http://GPIO2.IO)\[14\] |
| 41  | ETH-NIC RST# (Intel, U6) | CLKO\_25MHz, [GPIO3.IO](http://GPIO3.IO)\[11\] | PDM\_CLK, [GPIO3.IO](http://GPIO3.IO)\[20\] | NC  |     | 42  | MICRO-SD | SD2\_DATA0, [GPIO2.IO](http://GPIO2.IO)\[15\] | SD2\_DATA0, [GPIO2.IO](http://GPIO2.IO)\[15\] | SD2\_DATA0, [GPIO2.IO](http://GPIO2.IO)\[15\] |
| 43  | USB1\_VBUS | USB1\_VBUS | USB1\_VBUS | USB1\_VBUS\_5V |     | 44  | MICRO-SD | SD2\_DATA1, [GPIO2.IO](http://GPIO2.IO)\[16\] | SD2\_DATA1, [GPIO2.IO](http://GPIO2.IO)\[16\] | SD2\_DATA1, [GPIO2.IO](http://GPIO2.IO)\[16\] |
| 45  | MIKROBUS (J8-5) | ECSPI2\_MISO, [GPIO5.IO](http://GPIO5.IO)\[12\] | ECSPI2\_MISO, [GPIO5.IO](http://GPIO5.IO)\[12\] (UART4\_CTS) | ECSPI2\_MISO, [GPIO5.IO](http://GPIO5.IO)\[12\] |     | 46  | MICRO-SD | SD2\_DATA2, [GPIO2.IO](http://GPIO2.IO)\[17\] | SD2\_DATA2, [GPIO2.IO](http://GPIO2.IO)\[17\] | SD2\_DATA2, [GPIO2.IO](http://GPIO2.IO)\[17\] |
| 47  | MIKROBUS (J8-6) | ECSPI2\_MOSI, [GPIO5.IO](http://GPIO5.IO)\[11\] | ECSPI2\_MOSI, [GPIO5.IO](http://GPIO5.IO)\[11\] (UART4\_TXD) | ECSPI2\_MOSI,[GPIO5.IO](http://GPIO5.IO)\[11\] |     | 48  | MICRO-SD | SD2\_DATA3, [GPIO2.IO](http://GPIO2.IO)\[18\] | SD2\_DATA3, [GPIO2.IO](http://GPIO2.IO)\[18\] | SD2\_DATA3, [GPIO2.IO](http://GPIO2.IO)\[18\] |
| 49  | MIKROBUS (J8-4) | ECSPI2\_SCLK, [GPIO5.IO](http://GPIO5.IO)\[10\] | ECSPI2\_SCLK, [GPIO5.IO](http://GPIO5.IO)\[10\] (UART4\_RXD) | ECSPI2\_SCLK, [GPIO5.IO](http://GPIO5.IO)\[10\] |     | 50  | MICRO-SD | SD2\_NCD, [GPIO2.IO](http://GPIO2.IO)\[12\] | SD2\_NCD, [GPIO2.IO](http://GPIO2.IO)\[12\] | SD2\_NCD, [GPIO2.IO](http://GPIO2.IO)\[12\] |
| 51  | AUD\_CODEC, USB-TYPEC, USB-HUB | I2C2\_SDA | I2C2\_SDA | I2C2\_SDA |     | 52  | USB-HUB | USB2\_VBUS | USB2\_VBUS | USB2\_VBUS\_3V3 |
| 53  | AUD\_CODEC, USB-TYPEC, USB-HUB | I2C2\_SCL | I2C2\_SCL | I2C2\_SCL |     | 54  | HEADER, DIP-SW | SAI1\_TXD5,[GPIO4.IO](http://GPIO4.IO)\[17\] (BT\_CFG13) | SAI1\_TXD5, [GPIO4.IO](http://GPIO4.IO)\[17\] (BT\_CFG13) | SAI5\_MCLK, [GPIO3.IO](http://GPIO3.IO)\[25\] |
| 55  | BT-FW\_FLASH (J9-39) | SWDCLK1 (BT Flash) | NC  | SAI5\_RXC, [GPIO3.IO](http://GPIO3.IO)\[20\] |     | 56  | NC  | NC  | SAI5\_MCLK, [GPIO3.IO](http://GPIO3.IO)\[25\] | SAI5\_RXD3, [GPIO3.IO](http://GPIO3.IO)\[24\] |
| 57  | HEADER (CON4) | CLK\_25M (Eth PHY) | CLK\_25M (Eth PHY) | SAI5\_RXD2, [GPIO3.IO](http://GPIO3.IO)\[23\] |     | 58  | NC  | NC  | PDM\_DATA2, [GPIO3.IO](http://GPIO3.IO)\[23\] | NC  |
| 59  | BT-FW\_FLASH (J9-30) | SWDIO1 (BT Flash) | NC  | NC  |     | 60  | NC  | NC  | PDM\_DATA3, [GPIO3.IO](http://GPIO3.IO)\[24\] | WDOG\_B, [GPIO1.IO](http://GPIO1.IO)\[02\] |
| 61  | MICRO-SD | NVCC\_SD2 | SPDIF\_RX, [GPIO5.IO](http://GPIO5.IO)\[4\] | NC  |     | 62  | PUSH-B | ONOFF | ONOFF | ONOFF |
| 63  | 3V3\_IN | 3V3\_OUT | 3V3\_OUT | 3V3\_OUT |     | 64  | HEADER, DIP-SW | SAI1\_TXD6, [GPIO4.IO](http://GPIO4.IO)\[18\] (BT\_CFG14) | SAI1\_TXD3, [GPIO4.IO](http://GPIO4.IO)\[15\] (BT\_CFG11) | NC  |
| 65  | 3V3\_IN | 3V3\_OUT | 3V3\_OUT | 3V3\_OUT |     | 66  | NC  | NC  | SAI3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[1\] | VSD\_3V3 (uSD power for next HBP) |
| 67  | 3V3\_IN | 3V3\_OUT | 3V3\_OUT | 3V3\_OUT |     | 68  | MICRO-SD | PWM2\_OUT, [GPIO1.IO](http://GPIO1.IO)\[13\] | SD2\_nRST, [GPIO2.IO](http://GPIO2.IO)\[19\] | SD2\_RESET\_B, [GPIO2.IO](http://GPIO2.IO)\[19\] |
| 69  | 3V3\_IN | 3V3\_OUT | NC  | 3V3\_OUT |     | 70  | GND | GND | GND | GND |
| 71  | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 |     | 72  | GND | GND | GND | GND |
| 73  | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 |     | 74  | GND | GND | GND | GND |
| 75  | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 |     | 76  | GND | GND | GND | GND |
| 77  | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 |     | 78  | GND | GND | GND | GND |
| 79  | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 | VIN\_5V0 |     | 80  | GND | GND | GND | GND |

<a id="mikrobus-connector"></a>

## mikroBUS connector

| **HummingBoard Pulse 2.4** | **IMX8M rev 2.0** | **IMX8M Mini rev 1.2** | **IMX8M Plus rev 1.0** |
| --- | --- | --- | --- |
| MIKROBUS (J8-2) | SAI2\_RXD, [GPIO4.IO](http://GPIO4.IO)\[23\] | SAI2\_RXD, [GPIO4.IO](http://GPIO4.IO)\[23\] | SAI3\_RXD, [GPIO4.IO](http://GPIO4.IO)\[30\] |
| MIKROBUS (J8-3) | ECSPI2\_SS0, [GPIO5.IO](http://GPIO5.IO)\[13\] | ECSPI2\_SS0, [GPIO5.IO](http://GPIO5.IO)\[13\] (UART4\_RTS) | ECSPI2\_SS0, [GPIO5.IO](http://GPIO5.IO)\[13\] |
| MIKROBUS (J8-4) | ECSPI2\_SCLK, [GPIO5.IO](http://GPIO5.IO)\[10\] | ECSPI2\_SCLK, [GPIO5.IO](http://GPIO5.IO)\[10\] (UART4\_RXD) | ECSPI2\_SCLK, [GPIO5.IO](http://GPIO5.IO)\[10\] |
| MIKROBUS (J8-5) | ECSPI2\_MISO, [GPIO5.IO](http://GPIO5.IO)\[12\] | ECSPI2\_MISO, [GPIO5.IO](http://GPIO5.IO)\[12\] (UART4\_CTS) | ECSPI2\_MISO, [GPIO5.IO](http://GPIO5.IO)\[12\] |
| MIKROBUS (J8-6) | ECSPI2\_MOSI, [GPIO5.IO](http://GPIO5.IO)\[11\] | ECSPI2\_MOSI, [GPIO5.IO](http://GPIO5.IO)\[11\] (UART4\_TXD) | ECSPI2\_MOSI,[GPIO5.IO](http://GPIO5.IO)\[11\] |
|     |     |     |     |
| MIKROBUS (J10-1) | UART3\_CTS, [GPIO5.IO](http://GPIO5.IO)\[8\] | UART1\_CTS, [GPIO5.IO](http://GPIO5.IO)\[26\] | UART3\_CTS, [GPIO5.IO](http://GPIO5.IO)\[8\] |
| MIKROBUS (J10-2) | UART3\_RTS, [GPIO5.IO](http://GPIO5.IO)\[9\] | UART1\_RTS, [GPIO5.IO](http://GPIO5.IO)\[27\] | UART3\_RTS, [GPIO5.IO](http://GPIO5.IO)\[9\] |
| MIKROBUS (J10-3) | UART3\_RXD, [GPIO5.IO](http://GPIO5.IO)\[26\] | UART1\_RXD, [GPIO5.IO](http://GPIO5.IO)\[22\] | UART3\_RXD, [GPIO5.IO](http://GPIO5.IO)\[6\] |
| MIKROBUS (J10-4) | UART3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[27\] | UART1\_TXD, [GPIO5.IO](http://GPIO5.IO)\[23\] | UART3\_TXD, [GPIO5.IO](http://GPIO5.IO)\[7\] |
| MIKROBUS (J10-5) | I2C3\_SCL | I2C3\_SCL | I2C3\_SCL |
| MIKROBUS (J10-6) | I2C3\_SDA | I2C3\_SDA | I2C3\_SDA |