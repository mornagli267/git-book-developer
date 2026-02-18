# ClearFog GTR Boot Select

You will need to download an operating system for the ClearFog GTR and flash in to a USB Disk or M.2 SSD in order to use the system. You can download official release distributions and find flashing instructions at [SolidRun Images](https://images.solid-run.com/A38X). In addition, there are also several community released distributions available. Once downloaded and flashed, the USB Disk/M.2 with the flashed OS image must be inserted into the ClearFog.

#### ClearFog GTR Family Boot Select

Before powering up the board  for the first time it is recommended to select the boot media. In order to configure the boot media to eMMC, please set the **SW4** switch to match the second option from the following table (SD/eMMC):

|         | **Switch 1** | **Switch 2** | **Switch 3** | **Switch 4** | **Switch 5** |
| ------- | ------------ | ------------ | ------------ | ------------ | ------------ |
| SPI     | OFF          | OFF          | OFF          | ON           | OFF          |
| SD/eMMC | OFF          | OFF          | ON           | ON           | ON           |
| M.2 SSD | ON           | ON           | ON           | OFF          | OFF          |
| UART    | OFF          | ON           | OFF          | OFF          | ON           |

{% hint style="info" %}
* The ClearFog GTR including U-Boot into eMMC by default.
* The ClearFog GTR does not have an SD card slot.
{% endhint %}

