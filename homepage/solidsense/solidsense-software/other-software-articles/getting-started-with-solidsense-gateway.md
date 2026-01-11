# Getting started with SolidSense gateway

> [!WARNING]
> The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.  
> [Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.

<a id="introduction"></a>

## Introduction

Thanks for purchasing the SolidSense IoT gateway. The system can be used in 3 ways:

1. Ready to go **SolidSense IoT platform** (SolidSense Out-Of-the-Box) with Eclipse Kura Framework and Wirepas/Bluetooth Low Energy MQTT gateways built-in applications. Configure the gateway via Kura and that’s it you can directly have your data forwarded to your cloud application.
2. Developing your own application or add-on on top of the platform. Simple additions can be developed via Python 3.7 using the pre-installed packages. For more sophisticated development, a Docker infrastructure is ready to host your containers.
3. Create your own SolidSense image derived from SolidSense OOB.
4. From bare metal. You can create your own Linux image starting from SolidRun BSP. The support for these developments are not covered in the SolidSense section. [](https://developer.solid-run.com/article-categories/nxp-i-mx6-based-products/)As an helper we have created the [SolidSense OEM software image](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264404993)  based on a standard Debian Buster version.

All the online documentation is focusing on the case 1 to help to quickly setup your gateway. The case 2-3 are still to be developed and the case 4 is not part of the SolidSense online documentation and developer wanting to build their own image shall start from here. Do not hesitate to query us about support services to help you start efficiently.

The gateways are delivered with or without the firmware image flashed, but Uboot is always installed on the eMMC. In case your gateway does not have a firmware included and you need it see: [Upgrading or installing a SolidSense gateway with version 1.0 and higher](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264208388) .

<a id="hardware-and-software-first-steps"></a>

## Hardware and software first steps

If you have chosen to run your gateway on the SolidSense IoT platform, then the following steps are for you.

Very few things to perform indeed, attach the minimum antennas and plug in.We recommend to attach the WiFi antenna at minimum to check that the system is starting correctly. If after 2-3 mn you see an SSID equal to the unit serial number, the firmware is up and running. Then you can start to [Configuring SolidSense networking with Kura](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179294)  and [Configuring and testing the Wirepas gateway software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/263946241)  if you are using that technology.

For ssh access, please reach out Solid Run SolidSense support service.

If you use SolidSense as a Wirepas gateway you can directly to [Configuring and testing the Wirepas gateway software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/263946241) .

To use the Bluetooth Low Energy features go to configure the [Bluetooth Low Energy – Installation and operation](../../solidsense-software/ble/bluetooth-low-energy-installation-and-operation.md) .

To setup the gateway supervision (service contract may apply) [Using Eclipse Kapua to supervise and configure SolidSense gateways](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264142858)

<a id="support"></a>

## Support

Please consult our [SolidSense Support Overview](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264437768) .

<a id="developing-your-own-applications"></a>

## Developing your own applications

The SolidSense gateway is based on an open software platform and open source components to allow any specific development to be realized on top of it. The **SolidSense IoT platform** is not a development platform by itself as it is focusing on production features like read-only file system and remote software upgrade, so we recommend to perform the development cycle on a flexible Debian Buster image, then to port the result on top of the production platform.

The simplest and most robust solution is to use Docker containers to deploy your applications. This will avoid hard dependencies on the system and will allow upgrade cycles that are linked with the platform. By selecting a baseline close from the SolidSense IoT platform the size of the container can be kept minimal.