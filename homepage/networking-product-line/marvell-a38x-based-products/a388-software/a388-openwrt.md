# A388 OpenWrt

{% hint style="info" %}
**The information below is outdated and ClearFog A388 Base/Pro support is already mainlined to OpenWrt repositories.**
{% endhint %}


<a id="description"></a>

### Description

```
   _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
```

OpenWrt is described as a Linux distribution for embedded devices.

Instead of trying to create a single, static firmware, OpenWrt provides a fully writable filesystem with package management. This frees you from the application selection and configuration provided by the vendor and allows you to customize the device through the use of packages to suit any application. For developer, OpenWrt is the framework to build an application without having to build a complete firmware around it; for users this means the ability for full customization, to use the device in ways never envisioned.

<a id="installation"></a>

### Installation

For Installation please have a look here:

[https://github.com/MarvellEmbeddedProcessors/openwrt-bb/wiki](https://github.com/MarvellEmbeddedProcessors/openwrt-bb/wiki)

Debugging:

Please use the MicroUSB Port:

```
sudo minicom -D /dev/ttyUSB0 -b 115200n8
```

<a id="external-links"></a>

### External Links

- [https://www.openwrt.org/](https://www.openwrt.org/)
- [https://forum.openwrt.org/](https://forum.openwrt.org/)
- [https://github.com/MarvellEmbeddedProcessors/openwrt-bb/wiki](https://github.com/MarvellEmbeddedProcessors/openwrt-bb/wiki)
- [https://wiki.openwrt.org/toh/solidrun/clearfog](https://wiki.openwrt.org/toh/solidrun/clearfog)