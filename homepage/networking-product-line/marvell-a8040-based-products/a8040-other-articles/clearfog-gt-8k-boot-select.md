# ClearFog GT-8K Boot Select

## SD Card

You will need to download an operating system for the ClearFog GT-8K and flash in to a blank SD card in order to use the system.

* You can download official release distributions and find flashing instructions at our [ClearFog GT 8K Quick Start Guide](/homepage/networking-product-line/marvell-a8040-based-products/clearfog-gt-8k-quick-start-guide.md)  page.
* For more information about how to flash the SD card, please refer to [Flashing an SD Card](/homepage/other-articles/flashing-an-sd-card.md) .

## Boot Select

Before powering up the board for the first time, it is recommended to select the boot media. The boot source is selected by setting SW6 (on the print side) to the right mode.

Here are the available modes:

![](../../../../.gitbook/assets/image-20211228-082700.png)

The switches on the boot source selector must be set as follows:

|                 |              |              |              |              |              |
| --------------- | ------------ | ------------ | ------------ | ------------ | ------------ |
| **Boot Source** | **Position** | **Position** | **Position** | **Position** | **Position** |
| **SPI ROM**     | OFF          | OFF          | ON           | OFF          | OFF          |
| **SD Card**     | ON           | ON           | OFF          | ON           | OFF          |
| **eMMC**        | ON           | ON           | ON           | OFF          | OFF          |
