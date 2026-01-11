# ClearFog CN9130 Boot Select

<a id="sd-card"></a>

#### SD Card

You will need to download an operating system for the ClearFog and flash in to a blank SD card in order to use the system. You can download official release distributions and find flashing instructions at [SolidRun Images (solid-run.com)](https://images.solid-run.com/). In addition there are also several community released distributions available. Once downloaded and flashed, the SD card with the flashed OS  image must be inserted into the MicroSD slot on the ClearFog .

<a id="cn9130-som-boot-select"></a>

#### CN9130 SOM Boot Select

Before powering up the board  for the first time it is recommended to select the boot media. In order to configure the boot media to MicroSD, please set the S1 switch to match the second option from the following table (SD/eMMC):

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|     | Switch 1 | Switch 2 | Switch 3 | Switch 4 | Switch 5 |
| SPI | ON  | X   | OFF | ON  | X   |
| SD  | OFF | X   | ON  | OFF | X   |
| eMMC | OFF | X   | OFF | ON  | X   |
| 2.2GHz Core Freq | X   | ON  | X   | X   | X   |
| 2GHz Core Freq | X   | OFF | X   | X   | X   |