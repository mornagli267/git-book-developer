# List of SolidSense software repository

> \[!WARNING] The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.\
> [Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.

## Foreword

All SolidSense software is open source  as per the company charter. You will find here the link to all Git repositories that are used to build the SolidSense system.

The exact branch can vary but you can backtrack the build using the manifest file

For those who wants to build their own Yocto image the SolidSense recipe are also available.

## Repository links

SolidSense utilities: [SolidSense-V1](https://github.com/SolidRun/SolidSense-V1)

Modem management: [SolidSense-Modem\_GPS\_Service](https://github.com/SolidRun/SolidSense-Modem_GPS_Service)

MQTT Client:[SolidSense-MQTT](https://github.com/SolidRun/SolidSense-MQTT)

Bluetooth:[SolidSense-BLE](https://github.com/SolidRun/SolidSense-BLE)

Wirepas: [Wirepas gateway](https://github.com/SolidRun/gateway) and [Wirepas backend-api](https://github.com/SolidRun/gateway)

Kura: [Kura 5.0 SolidSense configured branch](https://github.com/SolidRun/kura/tree/solidsense-develop)

## Yocto recipe

The Yocto recipe can be cloned to build your own Yocto version

1. Clone [reference implementation of the CIP Core project](https://github.com/SolidRun/cip-project-deby)
2. Then clone [SolidRun specific files](https://github.com/SolidRun/meta-cip-sr-common) in the ‘poky’ directory of the first repositoty

We understand that creating your own Yocto image is not trivial and we support services can be available to help.
