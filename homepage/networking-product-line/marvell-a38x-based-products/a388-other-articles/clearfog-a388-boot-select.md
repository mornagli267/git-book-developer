# ClearFog A388 Boot Select

#### SD Card

You will need to download an operating system for the ClearFog and flash in to a blank SD card in order to use the system. You can download official release distributions and find flashing instructions at [SolidRun Images (solid-run.com)](https://images.solid-run.com/). In addition there are also several community released distributions available. Once downloaded and flashed, the SD card with the flashed OS  image must be inserted into the MicroSD slot on the ClearFog .

#### A388 SoM Boot Select

Before powering up the board  for the first time it is recommended to select the boot media. In order to configure the boot media to MicroSD, please set the S1 switch to match the second option from the following table (SD/eMMC):

|         | **Switch 1** | **Switch 2** | **Switch 3** | **Switch 4** | **Switch 5** |
| ------- | ------------ | ------------ | ------------ | ------------ | ------------ |
| SPI     | OFF          | OFF          | OFF          | ON           | OFF          |
| SD/eMMC | OFF          | OFF          | ON           | ON           | ON           |
| M.2 SSD | ON           | ON           | ON           | OFF          | OFF          |
| UART    | OFF          | ON           | OFF          | OFF          | ON           |
