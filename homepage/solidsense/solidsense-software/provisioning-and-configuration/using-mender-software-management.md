# Using Mender software management

> [!WARNING]
> The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.

<a id="introduction-to-mender"></a>

## Introduction to Mender

Mender is developed by Northern Tech of Norway and commercialized by the [Mender.io Web site](https://mender.io/).

It offers safe Over the Air Software upgrade but also many more features that I will not develop here. Mender works with 2 software components:

- Mender client running on the gateway and that is installed part of the SolidSense OOB image
- Mender server running on a cloud server. Several flavor are available: Community edition for test and limited features, hosted Mender, Mender Enterprise

SolidRun is not proposing any Mender services for commercial and operational use. All commercial discussions shall be held directly with Mender and we will be very happy to provide the introduction.

For test and PoC purposes, SolidRun is hosting a Mender community edition that can be used for a limited number of systems and that is operated solely by SolidRun personnel. To go commercial in large scale and be in control of your software upgrades each customer must have its own Mender instance or subscription.

For full Mender documentation refer to Mender website

<a id="the-solidsense-mender-client"></a>

## The SolidSense Mender client

Mender and SolidSense rely on the principle of a read-only root file system. On the eMMC there are 2 rofs partitions for active and standby root fs. A new version of the rofs can be downloaded in the background without perturbing the operations and a system swap is triggered by rebooting the system. Rollback is automatically performed if the boot on the version is not successful.

The Mender client is installed part of the SolidSense OOB image. That includes some changes in Uboot to manage the active boot partition.

<a id="useful-mender-commands"></a>

## Useful Mender commands

A few Mender commands are useful to understand the status of the software on the gateway. They are accessible via shell commands after having gain su level by ‘sudo su’

```
# display the current active image versionmender -show-artifact## force the query of the server for new softwaremender -check-update## send the gateway inventory to the servermender -send-inventory
```

The mender commands can be sent from Kura or Kapua command service. In that case, the commend shall be prefixed by ‘krc’ as some mender commands do not have return value and confuse the Command service. Ex: ‘krc mender -show-artifact’

<a id="upgrading-your-image-using-mender"></a>

## Upgrading your image using Mender

Rather than re-flashing completely the gateway storage via full image flash, it could be simpler to perform a local upgrade of the image using Mender.

**Step 1:** Download the signed Mender artifact (if you don’t have your own Mender server) from [here](https://images.solidsense.io/SolidSense/mender/SolidRun-signed/index.html)

You have to select the SolidSense software release and the hardware architecture as there is 2 artifacts for each release: 1 for Dual Lite CPU and one for Quad Core ones. The Mender artifact shall be accessible on the gateway and we propose two solutions: Download from an external computer on an USB drive that will be mounted on the gateway for installation or download directly on the gateway via the ‘curl’ command.

```
##  Download the release 1.1a on the gateway (assuming solidsense home dir)#curl -o Solidsense-1.1a-2020120300.mender https://images.solidsense.io/SolidSense/mender/SolidRun-signed/1.1a/n6gsdl-core-image-minimal-Solidsense-1.1a-2020120300.mender
```

Step 2: Install the new release

```
## install the previously downloaded image# assuming that current directory is solidsense home dir# The file name is to be adjusted versus the downloaded file namesudo sumender install Solidsense-1.1a-2020120300.menderreboot...# after restart and loginmender commit
```

<a id="troubleshooting-upgrades"></a>

## Troubleshooting upgrades

During the upgrade phase, only the read-only root file system (rofs) is upgraded while all the modifications and configuration that resides in the overlay file system are left unchanged. However, in some cases some changes between rofs and ovfs are not fully compatible leading to dysfunctional systems.

To recover the best is to rebuild the ovfs from scratch using: /opt/scripts/restart –wipe

This will erase also all configurations and changes that were applied in the ovfs. However, if the configuration is built from the provisioning system it will automatically be rebuilt. It is safe to have a way to rebuild gateway configuration is case of major upgrade.

<a id="attaching-the-gateway-for-your-own-mender"></a>

## Attaching the gateway for your own Mender

All the Mender configuration is located in /etc/mender and is by default configured to be attached to the SolidSense Mender instance. To attach your gateways to your own Mender, you need to create your own artifact and this can done in 2 ways

Solution 1: Starting from the SolidSense image downloaded from the [SolidSense image server](https://images.solidsense.io/SolidSense/)

Solution 2: Building your own Yocto image from the recipe (see article)

In both cases you will have to update the /etc/mender directory with your own parameters and generate a Mender “Artifact”.

> [!WARNING]
> **Please Note**
> The current article gives an overview on the process to create or modify Mender artifacts to have the full control of the software. It requires Linux expertise and a detailed reading of the Mender documentation. SolidRun can propose support packages to help though the process.

In any case the first point is to understand how to manage and generate Mender artifact. [Here is the corresponding documentation](https://docs.mender.io/artifact-creation).

SolidSense device types to be set in Mender artifacts

| Type | SolidSense models |
| --- | --- |
| n6gsdl | N6 Indoor, N6 Outdoor dual core |
| n6gq | N6 Indoor, N6 Outdoor quad core |
| in6gsdl | N6 Industrial dual core |
| in6gq | N6 Industrial quad core |

<a id="starting-from-a-solidsense-artifact"></a>

### Starting from a SolidSense artifact

That is the simplest solution if the modifications to image are limited. You need to download the unsigned artifact from the [SolidSense file server](https://images.solidsense.io/SolidSense/mender/SolidRun-unsigned/index.html).

If the modifications are very limited you can use the tools from to modify the artifacts (see Mender documentation). The minimum to be done is to replace the default SolidSense mender.conf (in /etc/mender) by the one needed for your cloud configuration ([see documentation](https://docs.mender.io/client-installation/configuration-file))

After the update, the critical process is to sign the artifact following the Mender documentation

If modifications are more important, it could be easier to extract the rootfs.ext4 full file system for the Mender artifact on a dedicated disk (like an SD card)

```
tar xf <mender artifact>
```

Then you can directly make all needed modifications (without exceeding the partition size [Introduction to SolidSense Out-of-the-Box (OOB) software image | Disk-partitioning-and-file-systems](https://solidrun.atlassian.net/wiki/spaces/developer/pages/264667139/Introduction+to+SolidSense+Out-of-the-Box+OOB+software+image#disk-partitioning-and-file-systems) ) and then re-create the artifact and sign it.