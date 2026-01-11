# Switching PCIe to MSATA

The mini-pcie slots on the top of the board can be configured to be either SATA or PCIe. This configuration does not auto-detect yet and needs to be hard coded in u-boot. I can add a u-boot env variable to switch between them. You need to modify the #if 1 to #if 0 in the following two places –\
[https://github.com/SolidRun/u-boot-armada38x/blob/u-boot-2013.01-15t1-clearfog/tools/marvell/bin\_hdr/src\_phy/a38x/mvHighSpeedTopologySpec-38x.c#L92](https://github.com/SolidRun/u-boot-armada38x/blob/u-boot-2013.01-15t1-clearfog/tools/marvell/bin_hdr/src_phy/a38x/mvHighSpeedTopologySpec-38x.c#l92)

and

[https://github.com/SolidRun/u-boot-armada38x/blob/u-boot-2013.01-15t1-clearfog/tools/marvell/bin\_hdr/src\_phy/a38x/mvHighSpeedTopologySpec-38x.c#L98](https://github.com/SolidRun/u-boot-armada38x/blob/u-boot-2013.01-15t1-clearfog/tools/marvell/bin_hdr/src_phy/a38x/mvHighSpeedTopologySpec-38x.c#l98)

This will modify the SERDES of the PEX (pcie) to become a SATA port

### Bootdevice (Dipswitch)

On both carrier boards – the boot device can be chosen by using the SW1 Dipswitch.

![](../../../../.gitbook/assets/image-20211228-082458.png)

> \[!INFO] White is the dip position. Black is the background.

> \[!WARNING] UART Booting does **not** work with above configuration! Instead, use **01001** where 1 means on, and 0 means off.

> \[!WARNING] Additional Information: If the SOM has eMMC onboard – SD interface will not work.
