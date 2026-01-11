# Bluetooth Low Energy – Installation and operation

> \[!WARNING] The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.

## Introduction

From version 1.1 on, the BLE gateway is integrated in the SolidSense MQTT gateway. Please refer to the [SolidSense MQTT gateway](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264142849) . Alternatively the Kura framework can be used as well to develop BLE applications connected to the cloud. Please refer to Kura documentation and to the corresponding section in the SolidSense documentation.

This software package allows to easily develop Bluetooth Low Energy (BLE 4.2) applications on top of the SolidSense gateway. It can be used either on the TI WL1831 chip (hci0) or one of the Nordic chip (nRF52832 on indoor or nRF52840 on outdoor) if they are not used by Wirepas. The Nordic are on the interfaces hc1 and hci2. Gateways delivered before February 2020 do not have a BLE stack flashed on the Nordic chip, in that case the Bluetooth stack can be flashed from the shell. See the corresponding paragraph below.

The detailed MQTT interface definition can be found in the [MQTT Interface definition document](https://images.solidsense.io/SolidSense/doc/SolidSense%20MQTT%20Gateway%20-%20Specifications%20-%20V2.0.0-Draft-200616.pdf).

The key features are the following:

1. Scan for surrounding BLE devices and publish advertisement packets. Several options are existing for publishing and decoding the content of there advertisements. In particular, specific beacons format like Eddystone and iBeacon are recognized and can be published with specific topics as well as Services like Temperature or battery level.
2. Configurable filters to eliminate unwanted devices
3. Full GATT client allowing detailed transactions with devices implementing GATT server capabilities.
4. Local configuration via Kura or remote via Kapua
5. Secured TLS communication with the MQTT broker

## Configuration

The hci0 interface supported by the TI WL1831 is always available and does not need any specific configuration.

One or both Nordic chips can be configured to support Bluetooth Low Energy and become the Bluetooth device hc1 (via ttymxc1) or Bluetooth device hci2 (via ttxymxc2).

In order to be effective, there are several steps that needs to be performed:

1. The Nordic chip needs to be flashed with the Bluetooth stack. This is explained here: [Bluetooth Low Energy – Installation and operation | Flashing-the-Nordic-chip-with-BLE-stack-–-N6-Indoor](https://solidrun.atlassian.net/wiki/spaces/developer/pages/267026433#flashing-the-nordic-chip-with-ble-stack-n6-indoor)
2. The supporting systemd services ble1 and ble2 respectively needs to be enabled and started. Alternatively, the custom configuration file can be edited to configure automatically the BLE services during provisioning.

### Automatic provisioning of Bluetooth hc1 and/or hci2

The custom provisioning file resides in /data/solidsense/config

To use hc1 or hci2, creating a custom provisioning configuration is necessary and the configuration file /data/solidsense/ble\_gateway/parameters.json is to be edited to change the default value that is hci0

To have the bluetooth services being configured using gateway provisioning, the following lines need to be added to the SolidSense-custom-conf.yml

```
#   hci0 on TI WL1831 on internal interface
#  Configured by default
#      
- service:
    type: BluetoothService
    name: hci1
    state: active
    parameters:
        port: ttymxc1
 
- service:
    type: BluetoothService
    name: hci2
    state: active
    parameters:
        port: ttymxc2
```

## Troubleshooting

For pure Bluetooth level troubleshooting and basic testing, you can use the following tools

```
bluetoothctl
```

That tool allows to perform all Bluetooth operations (see documentation on the Web). This can be useful to discriminate a problem in the gateway or to check basic operational state of the interface. In particular checking if the interface is well powered and perform a basic scan.

```
hciconfig
```

List existing hci interfaces and their status.

## Errors reported in MQTT

In the current version there is a limited number of errors that are reported in MQTT messages (gatt\_result topic only)

Error 3: Connection failed or the device was not detected in the previous scan\
Error 4: Communication error during GATT transaction\
Error 6: GATT read error. Likely to be a wrong Characteristic UUID\
Error 9: GATT Write error\
Error 11: Notification setup error

Error reporting is planned to be improved in later release.

## Flashing the Nordic chip with BLE stack – N6 Indoor

This operation is needed only for gateways shipped from factory before Jan 20, 2020.

If the Nordic chip has been previously flashed with Wirepas the flashing will proceed but the chip will not work properly. Flash only chip fresh from factory. It is not required to flash both chips.

In the picture below

* Chip#1 corresponding to hci1 is the lower 2.4Ghz antenna
* Chip#2 corresponding to hc2 is the upper 2.4 Ghz antenna

![](../../../../.gitbook/assets/image-20211104-092447.png)

If any service was previously using the chip it shall be stopped. The gateway must have been previously upgrade to V0.95 or higher

The procedure is to be performed with shell commands as root (sudo).

```
# getting the binaries form the file server
curl -o blehci-boot-1.2.0.bin https://images.solidsense.io/SolidSense/nina-b1/blehci-boot-1.2.0.bin
curl -o blehci-1.2.0.img https://images.solidsense.io/SolidSense/nina-b1/blehci-1.2.0.img
#
# Flashing the chip #1
# 
/opt/scripts/flash_ublox --sink 1 --type boot blehci-boot-1.2.0.bin 
/opt/scripts/flash_ublox --sink 1 --type program blehci-1.2.0.img 
# 
# Flashing the chip #2 
# 
/opt/scripts/flash_ublox --sink 2 --type boot blehci-boot-1.2.0.bin 
/opt/scripts/flash_ublox --sink 2 --type program blehci-1.2.0.img
```

Perform a power cycle after re-flashing

N6 Indoor and N6 Industrial

These units are using nRF52840 and therefore needs different binaries

For boot use: [https://images.solidsense.io/SolidSense/bluetooth/nina-b3/nina-b3\_boot-1.8.1.bin](https://images.solidsense.io/SolidSense/bluetooth/nina-b3/nina-b3_boot-1.8.1.bin)

For program use: [https://images.solidsense.io/SolidSense/bluetooth/nina-b3/nina-b3\_blehci-1.8.1.bin](https://images.solidsense.io/SolidSense/bluetooth/nina-b3/nina-b3_blehci-1.8.1.bin)
