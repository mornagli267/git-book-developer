# HummingBoard IIoT & i.MX8M Plus SoM Display Connections

<a id="introduction"></a>

# Introduction

The HummingBoard IIoT supports both MIPI-DSI and LVDS displays.  
Instructions are provided below for particular supported panels.

<a id="revision-and-notes"></a>

# Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 31 Jul 2025 | Josua Mayer | 1   | Initial release |
| Table of Contents | - [Introduction](#introduction)<br>- [Revision and Notes](#revision-and-notes)<br>- [Supported Panels](#supported-panels)<br>- [Enable Panel in Software](#enable-panel-in-software)<br>- [Electrical Connection](#electrical-connection)<br>  - [Winstar WJ70N3TYJHMNG0 (DSI)](#winstar-wj70n3tyjhmng0-dsi)<br>  - [Winstar WF70A8SYJHLNGA (LVDS)](#winstar-wf70a8syjhlnga-lvds) |     |     |

<a id="supported-panels"></a>

# Supported Panels

- Winstar WJ70N3TYJHMNG0 (DSI):  
`imx8mp-hummingboard-iiot-panel-dsi-WJ70N3TYJHMNG0.dtbo`
- Winstar WF70A8SYJHLNGA (LVDS):  
`imx8mp-hummingboard-iiot-panel-lvds-WF70A8SYJHLNGA.dtso`

> [!NOTE]
> **Note:** The DSI panel is sold part of “HummingBoard i.MX8M IIOT” Evaluation Kits, for separate availability contact [sales@solid-run.com](mailto:sales@solid-run.com).

> [!NOTE]
> **Note:** Using both DSI and LVDS panels at the same time leads to various software issues and is not recommended.

<a id="enable-panel-in-software"></a>

# Enable Panel in Software

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

> [!NOTE]
> **Note:** Note the FDTOVERLAYS line can be extended with additional overlays e.g. for adding cameras.

> [!NOTE]
> **Note:** Enabling both DSI and LVDS panel overlays at the same time leads to various software issues and is not recommended.

For editing on device can use `nano` text editor:

```
mount /dev/mmcblk1p1 /boot
nano /boot/extlinux/extlinux.conf
# save with ctrl+o, exit with ctrl+x
sync
reboot
```

<a id="electrical-connection"></a>

# Electrical Connection

Carefully review the connections shown below, wrong orientation of cable may damage the panel.

<a id="winstar-wj70n3tyjhmng0-dsi"></a>

## Winstar WJ70N3TYJHMNG0 (DSI)

LVDS panel is connected to J25 on the HB-IIoT (same side of PCB as SoM and M.2 connectors). The cable used should expose contacts at the upper side of the panel, facing away from the PCB. The connector on HB-IIoT supports contacts on either side.

![imx8mp-hb-iiot-dsi-panel.jpg](./attachments/imx8mp-hb-iiot-dsi-panel.jpg)

> [!NOTE]
> **Note:** Ensure cable is connected exactly as shown in the picture, wrong orientation may damage the panel.

<a id="winstar-wf70a8syjhlnga-lvds"></a>

## Winstar WF70A8SYJHLNGA (LVDS)

LVDS panel is connected to J24 on the HB-IIoT (same side of PCB as USB and Ethernet connectors). The cable used should expose contacts at the upper side of the panel, facing away from the PCB. The connector on HB-IIoT supports contacts on either side.

![HummingBoard IIoT connected LVDS.png](./attachments/HummingBoard%20IIoT%20connected%20LVDS.png)

> [!NOTE]
> **Note:** Ensure cable is connected exactly as shown in the picture, wrong orientation may damage the panel.