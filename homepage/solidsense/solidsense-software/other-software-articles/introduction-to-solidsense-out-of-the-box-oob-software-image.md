# Introduction to SolidSense Out-of-the-Box (OOB) software image

> [!WARNING]
> The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.  
> [Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.

<a id="solidsense-oob-purpose-and-overview"></a>

## SolidSense OOB purpose and overview

The SolidSense Out of the Box image allows to start very quickly an IoT system without having the hurdle to develop a full software stack on the gateway.

The SolidSense OOB gateway software is  including the fundamental features:

- Civil Infrastructure Program (Yocto) Kernel, bringing an increasing robustness and long term stability over the Debian based systems
- “Over the Air” further upgrades with the integration [Mender.io](http://Mender.io) client in the rootfs.
- Eclipse Kura framework
- Direct integration of Wirepas gateway application and modem-GPS management server
- Read-only root file system and docker infrastructure pre-installed.

With just some configurations using Kura the gateway can:

1. Interface a Wirepas network with a cloud interface via MQTT
2. Perform BLE operation either via a default BLE client or via Kura
3. Manage the gateway configuration via Kura web interface
4. Manage the cellular interface
5. Develop visually application with Kura
6. Connect to Kapua for supervision and data collection
7. Manage software via Mender
8. Develop additional Python 3 applications
9. Run you Docker application containers

So that is a lot that you can already do on the basis of our standard image. However, to be in full control this image can be customized using our Yocto recipes that are available in our [List of SolidSense software repository](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264568840)

<a id="solidsense-oob-software-roadmap"></a>

## SolidSense OOB Software roadmap

Currently units are delivered with SolidSense V1.1a.

Coming soon and already available as beta version, the SolidSense V2.0 is coming. And here are the main new features included in it:

- New Linux kernel version 5.4 for additional robustness in particular on the management of the overlay file system.
- Kura V5.0 This is major release for Kura as SolidSense 1.1 is based on Kura 4 that is 3 years old.
  - That brings several security related features for access to the Web interface.
  - New Wifi control interface taking into account the actual transceiver and country characteristics as well as the management of the 5GHz band
  - For all details see the Kura site
- New Wirepas configuration interface allowing the visibility of the actual configuration and more parameters (keys)
- Wirepas data monitoring web interface
- Wirepas JSON payload
- Wirepas backend WebSocket transport
- Wirepas OTAP for version 5.1
- LED indication on Wirepas data transport
- Many small improvements and bug corrections that are not listed here
- Pre-installed [Remote.it](http://Remote.it) client for remote access of the gateway

The new SolidSense gateways N6 Industrial and N8 Compact are delivered directly with SolidSense V2.0 Beta (SolidSense V1.2ed8)

**General availability for SolidSense V2.0 is planned for September 2021**

<a id="download-links-for-upgrades"></a>

## Download links for upgrades

<a id="solidsense-version-11a"></a>

### SolidSense version 1.1a

[Full eMMC flashing image](https://images.solidsense.io/SolidSense/bootable_sdcard/Solidsense-1.1a-2020120300.img.xz)

[Mender upgrade artifact (Dual Core)](https://images.solidsense.io/SolidSense/mender/SolidRun-signed/1.1a/n6gsdl-core-image-minimal-Solidsense-1.1a-2020120300.mender)

<a id="solidsense-version-20-beta"></a>

#### SolidSense version 2.0 Beta

[Full eMMC flashing image](https://images.solidsense.io/SolidSense/bootable_sdcard/Solidsense-1.1a-2020120300.img.xz)

[Mender upgrade artifact (Dual Core)](https://images.solidsense.io/SolidSense/mender/SolidRun-signed/1.1a/n6gsdl-core-image-minimal-Solidsense-1.1a-2020120300.mender)

<a id="upgrade-constraints-and-recommendation"></a>

## Upgrade constraints and recommendation

Upgrade to 2.0 is only possible from version 1.1 or 1.1a, so if you have a very old version (like 0.9xx) please upgrade first to 1.1a

Upgrade from 1.1 to 2.0 needs a new Kura database, so by default all your settings will be lost and the new configuration will be the default one. To avoid that issue please create a provisioning file with your own default configuration. [Configuration provisioning of the SolidSense gateways](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264765441) . The provisioning file is reapplied upon upgrade.

<a id="troubleshooting-upgrade"></a>

#### Troubleshooting upgrade

The upgrade process only changes to rofs (Read-Only file system) while the ovfs (Overlay file system) is left unchanged.That gives the advantage that all modification made on the rofs are kept unchanged after the upgrade as the ovfs is still here. However, some ovfs files may not be compatible with the new rofs preventing the system to work properly. If this is happening then removing the rofs to have a fresh start is recommended. This is triggered by

```
sudo su
/opt/scripts/restart --wipe
```

The unit is rebooting with an empty ovfs, meaning that all user configuration is to be re-created. This can be done with a good provisioning file (SolidSense-conf-custom.yml) that will re-create the specific configuration upon boot.

<a id="disk-partitioning-and-file-systems"></a>

## Disk partitioning and file systems

SolidSense gateways are delivered with 8Gb eMMC as hard disk with a specific partitioning to support all features. Here is the disk map implemented by the SolidSense image

| Device | Purpose | Size | Mounted as |
| --- | --- | --- | --- |
| /dev/mmcblk2boot0 | Boot |     | N/A |
| /dev/mmcblk2rpmb | RPMB |     | N/A |
| /dev/mmcblk2p1 | ROFS Part a | 1.5GB | /media/rfs/ro\* |
| /dev/mmcblk2p2 | ROFS Part b | 1.5GB | /media/rfs/ro\* |
| /dev/mmcblk2p3 | Overlay FS | 64MB | /media/rfs/rw |
| /dev/mmcblk2p4 | Data | 4.2GB | /data |

Only one of the ROFS partitions is mounted as a given time. This the active partition containing the running read-only root file system. The partition not mounted is the backup one that can be used by Mender either to:

1. Rollback to previous system in case of problems
2. Download the new version in the background

The overlay file system is recording all changes made on the system and in particular all configuration changes. The interesting point is that the changes made in the configuration are surviving a root fs change required for an upgrade. On the other hand the overlay file system can be wiped out and the gateway restart like fresh from factory but with the latest installed release.

The Data partition is never directly impacted by upgrades and shall contain the stable part of the application. It can also be used to add additional features to the system. The following directories are created (and used by the system)

|     |     |
| --- | --- |
| /data/solidsense | SolidSense configuration files. Can be extended by user |
| /data/docker | Docker sub-system files |
| /data/mender | Mender files (but not static configuration) |
| /data/u-boot | U boot environment |
| /data/.var/log | System log files (/var/log) |

Application developers can add any additional directory in /data.