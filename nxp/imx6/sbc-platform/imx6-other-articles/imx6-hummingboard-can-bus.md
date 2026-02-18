# i.MX6 HummingBoard – CAN bus

{% hint style="warning" %}
**CAN Bus is only supported on Hummingboard Edge/Gate/CBi and i.MX6 SOM Rev. v1.5 and higher.**
{% endhint %}


### Overview

A Controller Area Network (CAN bus) is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other in applications without a host computer. It is a message-based protocol, designed originally for multiplex electrical wiring within automobiles to save on copper, but is also used in many other contexts. (source [http://wikipedia.com](http://wikipedia.com) ).

### Hardware Modification

**Notes**

1. Requires SOM rev 1.4 and newer
2. Requires HummingBoard Edge/Gate/CBi
3. Overlaps with HDMI connector CEC function. So only this or the HDMI connector can be assembled

![](../../../../.gitbook/assets/image-20211226-132717.png)

In order to get the CAN bus up and running, following hardware modifications need to be done:

* Disassemble D5 and the HDMI connector
* Assemble:
* R54
* R53
* C100
* U10003 (CAN transceiver , for example TJA1050)
* R55
* L12
* L13
* C101
* C102
* L13
* J28

Per the HummingBoard CBi schematics:[HummingBoard CBi Quick Start Guide](/nxp/imx6/sbc-platform/hummingboard-imx6-sbc-quick-start-guide/hummingboard-cbi-quick-start-guide.md)

## Software Modification

**Device Tree Changes**

**Edit following lines in the Device tree**

* Disable HDMI-CEC by setting status = “disabled” – in [Github DeviceTree](https://github.com/SolidRun/linux-fslc/blob/3.14-1.0.x-mx6-sr-next/arch/arm/boot/dts/imx6qdl-hummingboard2.dtsi#l259)
* Enable Flexcan1 in [Github DeviceTree](https://github.com/SolidRun/linux-fslc/blob/3.14-1.0.x-mx6-sr-next/arch/arm/boot/dts/imx6qdl-hummingboard2.dtsi#l237)

#### (Re-)Compile DeviceTree

Generically speaking, the raw .dts files can be compiled into .dtb using the device-tree-compiler dtc. The most straightforward way to invoke it is by configuring the linux kernel tree, and then running

```
make dtbs
```

The kernel-tree needs to be configured first. Please refer to [i.MX6 Kernel](/nxp/imx6/sbc-platform/imx6-software/imx6-kernel.md)  for generic instructions, or consult the distro documentation

{% hint style="success" %}
**DTB files can also be de- and recompiled. Consult the manpage of** _**dtc**_ **for additional information.**
{% endhint %}


#### (Re-)Compile Linux Kernel

**Either recompile linux kernel with config :**

```
CONFIG_CAN=y
CONFIG_CAN_RAW=y
CONFIG_CAN_DEV=y
CONFIG_CAN_FLEXCAN=y
```

**or activate modules:**

```
modprobe can
modprobe flexcan
modprobe can-dev
modprobe can-rawTest CanBUS
```

**Enable device can0:**

```
ip link set can0 up type can bitrate xxxxxx
```

(ex:125000)

**Checking:**

```
ip -details link show can0
```

The easiest way to test the CanBUS is to use the [CAN-Utils](https://github.com/linux-can/can-utils), which are available for Debain/Ubuntu etc.

Example commands:

**Sending:**

```
cansend can0
```

**receiving:**

```
candump can0
```
