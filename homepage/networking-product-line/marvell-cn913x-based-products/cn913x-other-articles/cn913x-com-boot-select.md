# CN913x COM Boot Select

<a id="cn9132-com-express-type-7-boot-select"></a>

#### CN9132 COM Express Type 7 Boot Select

Before powering up the board  for the first time it is recommended to select the boot media. In order to configure the boot media to MicroSD, please set the S1 switch to match the second option from the following table (SD/eMMC):  

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| BOOT MODE | SW1 #1 | SW1 #2 | SW1 #3 | SW1 #4 | SW1 #5 | SW1 #6 |
| SPI | OFF | ON  | ON  | OFF | ON  | X   |
| SD  | ON  | OFF | ON  | ON  | OFF | X   |
| eMMC | ON  | OFF | ON  | OFF | ON  | X   |

|     |     |     |
| --- | --- | --- |
| Frequency | SW2 #1 | SW2 #1 |
| 2.2GHz | ON  | OFF |
| 2GHz | OFF | OFF |
| 1.6GHz | OFF | ON  |

  

![](./attachments/image-20220112-142628.png)