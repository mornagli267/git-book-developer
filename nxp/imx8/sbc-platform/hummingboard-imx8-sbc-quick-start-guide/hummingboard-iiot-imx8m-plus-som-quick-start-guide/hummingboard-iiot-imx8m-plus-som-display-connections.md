# HummingBoard IIoT & i.MX8M Plus SoM Display Connections

## HummingBoard IIoT & i.MX8M Plus SoM Display Connections

## Introduction

The HummingBoard IIoT supports both MIPI-DSI and LVDS displays.\
Instructions are provided below for particular supported panels.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Revision** | **Notes**       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | --------------- |
| 31 Jul 2025       | Josua Mayer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1            | Initial release |
| Table of Contents | <p>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#introduction">Introduction</a><br>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#supported-panels">Supported Panels</a><br>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#enable-panel-in-software">Enable Panel in Software</a><br>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#electrical-connection">Electrical Connection</a><br>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#winstar-wj70n3tyjhmng0-dsi">Winstar WJ70N3TYJHMNG0 (DSI)</a><br>- <a href="hummingboard-iiot-imx8m-plus-som-display-connections.md#winstar-wf70a8syjhlnga-lvds">Winstar WF70A8SYJHLNGA (LVDS)</a></p> |              |                 |

## Supported Panels

* Winstar WJ70N3TYJHMNG0 (DSI):\
  `imx8mp-hummingboard-iiot-panel-dsi-WJ70N3TYJHMNG0.dtbo`
* Winstar WF70A8SYJHLNGA (LVDS):\
  `imx8mp-hummingboard-iiot-panel-lvds-WF70A8SYJHLNGA.dtso`

{% hint style="info" %}
**Note:** The DSI panel is sold part of “HummingBoard i.MX8M IIOT” Evaluation Kits, for separate availability contact [sales@solid-run.com](mailto:sales@solid-run.com).
{% endhint %}


{% hint style="info" %}
**Note:** Using both DSI and LVDS panels at the same time leads to various software issues and is not recommended.
{% endhint %}


## Enable Panel in Software

On HummingBoard-IIoT supported panels are enabled by DeviceTree Overlays.

Edit file `extlinux.conf` on the first partition of the board adding the line starting with “FDTOVERLAYS” - either from a PC, or from the device serial console, **then reboot**. The resulting file should look similar to the example below (line 5 is the important addition, substitute the filename based on actual panel from the list above):

```
default Yocto
label Yocto
   kernel /Image
   fdtdir /
   FDTOVERLAYS ../freescale/imx8mp-hummingboard-iiot-panel-dsi-WJ70N3TYJHMNG0.dtbo
append root=PARTUUID=076c4a2a-02 rootwait
```

{% hint style="info" %}
**Note:** Note the FDTOVERLAYS line can be extended with additional overlays e.g. for adding cameras.
{% endhint %}


{% hint style="info" %}
**Note:** Enabling both DSI and LVDS panel overlays at the same time leads to various software issues and is not recommended.
{% endhint %}


For editing on device can use `nano` text editor:

```
mount /dev/mmcblk1p1 /boot
nano /boot/extlinux/extlinux.conf
# save with ctrl+o, exit with ctrl+x
sync
reboot
```

## Electrical Connection

Carefully review the connections shown below, wrong orientation of cable may damage the panel.

### Winstar WJ70N3TYJHMNG0 (DSI)

LVDS panel is connected to J25 on the HB-IIoT (same side of PCB as SoM and M.2 connectors). The cable used should expose contacts at the upper side of the panel, facing away from the PCB. The connector on HB-IIoT supports contacts on either side.

![imx8mp-hb-iiot-dsi-panel.jpg](../../../../../.gitbook/assets/imx8mp-hb-iiot-dsi-panel.jpg)

{% hint style="info" %}
**Note:** Ensure cable is connected exactly as shown in the picture, wrong orientation may damage the panel.
{% endhint %}


### Winstar WF70A8SYJHLNGA (LVDS)

LVDS panel is connected to J24 on the HB-IIoT (same side of PCB as USB and Ethernet connectors). The cable used should expose contacts at the upper side of the panel, facing away from the PCB. The connector on HB-IIoT supports contacts on either side.

![HummingBoard IIoT connected LVDS.png](<../../../../../.gitbook/assets/HummingBoard IIoT connected LVDS.png>)

{% hint style="info" %}
**Note:** Ensure cable is connected exactly as shown in the picture, wrong orientation may damage the panel.
{% endhint %}

