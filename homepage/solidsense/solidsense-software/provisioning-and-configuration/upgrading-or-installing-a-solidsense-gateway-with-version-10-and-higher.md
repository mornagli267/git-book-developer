# Upgrading or installing a SolidSense gateway with version 1.0 and higher

> \[!WARNING] The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.\
> [Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.

## Installing SolidSense gateways

**SolidSense gateways are shipped with SolidSense OOB 1.0 (or up) pre-flashed unless otherwise specified for specific orders.**

For details on[Introduction to SolidSense Out-of-the-Box (OOB) software image](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264667139)

Any upgrades from a release higher then 0.91 is done via over the network process (OTA) and will not require any physical intervention on the gateway. See the planned roadmap below for the new features.This can also be done via [Using Mender software management | Upgrading-your-image-using-Mender](https://solidrun.atlassian.net/wiki/spaces/developer/pages/263585806/Using+Mender+software+management#upgrading-your-image-using-mender) .

**The upgrade is available for all SolidSense versions N6 Indoor, N6 Outdoor, N6 Industrial and the upcoming N8 Compact including Quad core.**

#### Restrictions and upgrade caution

The new upgrade mechanism requires a new hard disk (eMMC) layout and therefore all pre-existing data will be lost upon upgrade. Please back-up any sensible data. All pre-existing configuration will also be lost and in particular Wirepas sink and transport configurations will have to be re-applied.

> \[!WARNING] **Please Note** Re-flashing the full eMMC shall be used if no SolidSense is already installed. For any software upgrade prefer using Mender via OTA or via local upgrade.

#### Procedure for full re-flashing of the eMMC

1. Download the image from the SolidSense server:&#x20;

[V1.1a image (\~650MB)](https://images.solidsense.io/SolidSense/Solidsense-1.1a-2020120300.img.xz) You can check [Introduction to SolidSense Out-of-the-Box (OOB) software image](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264667139)  for the latest roadmap images.

2\. Flash the image an a USB stick (good quality) using a tool like Etcher

3\. Plug a HDMI screen and a (QWERTY) keyboard. This can be tricky on N6-Outdoor units and do not hesitate to ask SolidRun run support for help. Plug the USB stick (preferably on the lower USB slot near the power supply connector) and then trigger a power supply and **gain access to the Uboot prompt by typing any key** on the keyboard.

4\. On the Uboot command line type the 2 following commands.

```
env run findfdt
env run usb_boot
```

The gateway starts the upgrade that takes around 5mn, when the process is finished a login prompts is displayed on the screen

5\. Power off the gateway, screen and keyboard can be disconnected as well as they are no longer needed.&#x20;

**USB stick must also be removed**.

6\. Power on the gateway and it shall boot on the version 0.9 and be ready for configuration

## Default configuration

The default network configuration is the same as in previous version:

* Ethernet as WAN with IP address acquired via DHCP
* WiFi access point active with SSID == gateway Serial Number and IP address 172.16.1.1
* WiFi default Passphrase: testKEYS

There is no installation required and no need to gain access via ssh on the gateway for additional manual intervention, all configuration can be done via Kura.

see [Configuring SolidSense networking with Kura](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179294)

see  [Configuring and testing the Wirepas gateway software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/263946241) . Note that no installation is required.

From the version 0.95 on, the default configuration is controlled by the [Configuration provisioning of the SolidSense gateways](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264765441) . Please look to the corresponding documentation.
