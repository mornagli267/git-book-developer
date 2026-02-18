# HummingBoard Ripple & RZ/G2LC SOM Quick Start Guide

![](../../../.gitbook/assets/hb-ripple-rzg2lc.png)

## Introduction

The following quick start guide provides background information about the [HummingBoard RZ/G2LC](https://www.solid-run.com/embedded-industrial-iot/renesas-rz-family/rz-g2lc-som#carrier-boards).

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Revision** | **Notes**                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------- |
| 23 Nov 2022       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.0          | Initial release                                                           |
| 28 Feb 2023       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.1          | Updated SW Versions                                                       |
| May 15, 2023      | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.2          | Updated SD SW Versions                                                    |
| 18 Nov 2024       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.3          | Updated the documentation to reflect the eMMC speed mode as **HighSpeed** |
| Table of Contents | <p>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#product-specifications">Product specifications</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#generating-yocto-buildroot-and-debian-image">Generating Yocto, Buildroot and Debian image</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#booting-from-sd-card">Booting from SD card</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#more-features">More Features</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#internet">Internet</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#wifi">WiFi</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#bluetooth">Bluetooth</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#cellular-modem">Cellular Modem</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                                                                           |

## Hardware Setup

#### Product specifications

|                                  | HUMMINGBOARD RZ/G2LC                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| I/Os                             | <p>2 x USB 3.0<br><br>1 x MIPI-CSI</p>                                                |
| Networking                       | <p>1 x Ethernet RJ45 10/100<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4 GHz)</p> |
| Processor                        | Renesas RZ/G2LC Dual core Arm Cortex A55 up to 1.2GHz + Cortex M33                    |
| Memory & Storage                 | <p>Up to 2GB DDR4<br>8GB eMMC (<strong>Mode:</strong> HighSpeed) [*]<br>MicroSD</p>   |
| Display                          | micro HDMI                                                                            |
| Misc.                            | <p>1 x Reset button<br>1 x Configurable push button<br>3 x LED indicators<br>RTC</p>  |
| Development and Debug interfaces | Micro USB                                                                             |
| Power                            | 7V – 36V                                                                              |
| Expansion card I/Os              | <p>mikroBUS header<br>Mini Pcie with SIM holder</p>                                   |
| Temperature                      | <p>Commercial: 0°C to 70°C<br>Industrial: -40°C to 85°C</p>                           |
| Dimensions                       | <p>PCBA: 100 x 70mm<br>Enclosure: 120 x 80 x 30mm</p>                                 |
| Enclosure                        | Extruded aluminium                                                                    |
|                                  | [Buy Now](https://shop.solid-run.com/product/SRG2L-EVKHR-R00/)                        |

{% hint style="info" %}
\[\*] **eMMC Speed Mode:** HighSpeed (up to 52MHz) Supported with RZ/G2LC SOM. For more detailed information about our SOM-RZ/G2LC series please visit this user manual : [RZ/G2LC SOM Hardware User Manual](rz-g2lc-som-hardware-user-manual.md) .
{% endhint %}


#### Block Diagram

The following figure describes the RZ/G2LC Block Diagram.

![](../../../.gitbook/assets/image-20230228-164654.png)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard RZ/G2LC

![](../../../.gitbook/assets/image-20221123-212506.png)

Print side connector overview of the HummingBoard RZ/G2LC.

![](<../../../.gitbook/assets/image-20211104-110340 (1).png>)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard Ripple with RZ/G2LC SOM (HummingBoard RZ/G2LC)
* 12V Power adapter (HummingBoard Ripple has wide range input of 7V-36V, it is recommended to use 12V power adapter).
* Micro USB to USB for console, the HummingBoard Ripple has an onboard FTDI chip.
* IP router or IP switch
* USB Disk and SD Card

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [HummingBoard RZ/G2LC Boot Select](rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md) .

{% hint style="info" %}
eMMC and SD connect to the same SDIO signals via MUX so we can’t have access to the SD & eMMC at the same time, select eMMC/SD by setting switch **S3**{6} → off : eMMC , on : SD
{% endhint %}


## Generating Yocto, Buildroot and Debian image

**Yocto**

1. Clone the repository from the “List of supported OS” link and move your terminal to this directory.
2. Download the layers by this command

```
$ repo init -u https://github.com/SolidRun/meta-solidrun-arm-rzg2lc.git -b dunfell -m meta-solidrun-arm-rzg2lc.xml
$ repo sync  
```

3. In this stage you can modify your image configs as you want, you can find more info about it the the repository.
4. For graphics support you need to explore in the readme file in the github and follow the instructions of this utility.
5. Set the environment of the image that going to be build by this command

```
$ TEMPLATECONF=$PWD/meta-solidrun-arm-rzg2lc/docs/template/conf/rzg2lc-solidrun source poky/oe-init-build-env build
```

6. Build your own Yocto image by this command

```
$ MACHINE=rzg2lc-hummingboard bitbake <target>
```

* NOTE: Choose your relevant target, for example:\
  -core-image-bsp: cli image.\
  -core-image-weston: graphical image.\
  -core-image-qt: graphical image including qt.

**Buildroot/Debian**

1. Clone the repository from the “List of supported OS” link and move your terminal to this directory.
2. In this stage you can modify your image configs as you want, you can find more info about it the the repository.
3. Build your own image by this command

```
$ MACHINE=rzg2lc-hummingboard Distro=<Buildroot/Debian> ./runme.sh
```

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![](../../../.gitbook/assets/image-20221123-220813.png)

{% hint style="info" %}
Please Note: The black rectangle represents the switch position.
{% endhint %}


Once you set the switches, you can apply the following for booting from SD card:

1. **Downloading the image**\
   Download the image (for example Debian) by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/RZ/Debian/build_date_20240529-git_rev_f22483f/rzg2lc-solidrun-sd-emmc-debian-f22483f.img.xz
```

* For more Debian releases, please visit [Debian Releases for RZ/G2LC](https://images.solid-run.com/RZ/rzg2lc_build).

2. **Writing the image to the SD card**\
   Use the following commands for writing the image to an SD card:

```
xz -dc rzg2lc-solidrun-sd-emmc-debian-f22483f.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync 
```

* For more information, please visit [Flashing an SD Card](../../other-articles/flashing-an-sd-card.md) .
* **Note:** Plug a micro SD into your Linux PC, the following assumes that the USB-Disk / Micro-SD is added as /dev/sdX and all it’s partitions are unmounted.
* **Note:** You can use the following command for writing to the SD in case you generated your own image:

```
$ sudo dd if=/your/image/path of=/dev/sdX bs=4k conv=fdatasync
```

3. **SD card insertion**\
   Please Insert the SD card into your device.
4. Power connection\
   Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.
5. **Power On**\
   Hold on the **On/Off** Power button - **SW1** (as shown in the figure below)![](../../../.gitbook/assets/image-20230228-151346.png)

* **Note:** The system should turn on by default when the power is connected (without pressing the button).

6. **Serial Connection**\
   Please insert the micro USB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.\
   Once you installed the necessary serial connection software, you should be able to see the following:

![](../../../.gitbook/assets/image-20231127-133436.png)

* Enter “root” in the login like the above example and then you can move on to use the device.

**Final stages**

The following stages need to be done in order to finalise the imaging:

1. Run `fdisk /dev/mmcblk0` if using SD or eMMC.
2. Recreate the rootfs partition (mostly the second partition) by deleting it and then creating a new partition that starts at the next sector after the first one and extends to the end of the drive (or less depending on your needs).
3. Write the new partition, when prompt about ‘Do you want to remove the signature?’ then answer with Yes.
4. Run `resize2fs /dev/mmcblk0p2` if using SD Card or eMMC.
5. In this stage the root partition should be big enough to start populating it; but first update the RTC clock.
6. Connect the RJ45 to your network with internet access (and DHCP server); and then run `dhclient`.
7. Update the RTC clock by running `ntpdate pool.ntp.org` and then `hwclock -w`.
8. Run apt-update commands below and then populate the root filesystem as you wish.

```
$ apt-get update && apt-get upgrade -y
```

Here is an example of the process until the 3rd step (include):

![](../../../.gitbook/assets/image-20231206-093535.png)

After those steps you should end the process in this way (step 4 to the end):

![](../../../.gitbook/assets/image-20231206-094407.png)

In the end you should see with “lsblk” that the partition size is in the required size.

### **More Features**

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).\
Models HummingBoard with WiFi, can be connected via [WiFi](../nxp-imx8-based-products/cubox-m-quick-start-guide.md#wifi) or wired Ethernet.

* Please check you Ethernet connection.
* Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

* For more detailed information, please refer to [RZ/G2LC Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) .

**WiFi**

* You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1. To bring a WiFi interface up, run the following :

```
$ ifconfig wlan0 up 
```

{% hint style="info" %}
To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).
{% endhint %}


2. Install the wpa\_supplicant package:

```
$ apt-get install wpasupplicant 
```

3. Edit network interfaces file :

At the bottom of the file, add the following lines to allow wlan as a network connection:

```
cat <<EOF > /etc/network/interfaces.d/wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
EOF

```

4. Create a configuration file with the relevant ssid:

```
cat <<EOF > /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=/run/wpa_supplicant
update_config=1
network={
    ssid="MYSSID"
    psk="passphrase" 
}
EOF

```

{% hint style="info" %}
Check your personal ssids by running : ‘iw dev wlan0 scan’
{% endhint %}


5. Make sure it works:

Restart your device and it should connect to the wireless network. You can check it by running the command `$ iwconfig` . If it doesn't, repeat above steps or get help from an adult.

* For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

#### Bluetooth

1. For showing all Bluetooth devices, run the following:

```
$ apt-get install bluez
$ bluetoothctl
```

2. Turn the device on:

```
[bluetooth]# power on
```

3. Make your Bluetooth detectable by other devices:

```
[bluetooth]# discoverable on
```

4. If you want to connect to other devices:

* Start by scanning for other Bluetooth devices:

```
[bluetooth]# scan on
```

* Choose a MAC address and connect :

```
[bluetooth]# pair $MAC 
```

* You can check the pairing list between the devices by writing :

```
[bluetooth]# paired-devices
```

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

* How to connect to the network:\
  1\. Install “modemmanager” package on your debian.

```
 $ sudo apt install modemmanager
```

2\. Search for your modem location:

```
$ mmcli -L
```

3\. Connect to your modem:

```
$ mmcli --modem=/your/modem/location
```

4\. Enable the modem:

```
$ mmcli --modem=/your/modem/location -e
```

5\. Scan for networks:

```
$ mmcli --modem=/your/modem/location --3gpp-scan
```

6\. connect to 3gpp network:

```
$ mmcli --modem=/your/modem/location --3gpp-register-in-operator=<network ID>
```

7\. Make sure the connection was created:

```
$ mmcli --modem=/your/modem/location 
```

* For some cellular modules to be connected, please refer to [Cellular Modules](/nxp/imx6/sbc-platform/imx6-other-articles/cellular-modules.md) .

**GUI On Debian**

There is an option with the **Debian** image, up to the user, to work with a GUI like Weston, GNOME and etc.\
For applying this option do the following steps:

First, connect your device to a screen using the working output (HDMI / uHDMI).

For working with **Weston** GUI:

1. Install the Weston package.

```
sudo apt install weston
```

2. Set the XDG\_RUNTIME\_DIR env param.

```
cat << 'EOF' > /etc/profile.d/weston.sh
if test -z "$XDG_RUNTIME_DIR"; then
    export XDG_RUNTIME_DIR=/run/user/`id -u`
    if ! test -d "${XDG_RUNTIME_DIR}"; then
        # Make a directory for the output of the Weston GUI
        mkdir --parents "${XDG_RUNTIME_DIR}"
        chmod 0700 "${XDG_RUNTIME_DIR}"
    fi
fi
EOF
```

3. Restart the system

```
reboot
```

4. Start Weston (must be run from the **Dissplay Terminal**)

```
weston
```

{% hint style="info" %}
Run the `weston` command from the **Dissplay Terminal** using keyboard (PHYSICAL TERMINAL not serial session or remote connection)
{% endhint %}


For working with **GNOME** GUI on top of Xorg:

1. Install Xorg.

```
$ sudo apt install xorg
```

2. Install your desired gnome.

```
$ sudo apt install gnome-session
```

NOTE: ‘gnome-session’ is an example of gnome that we can work with, you can replace the ‘session' with another GNOME extention. 3. Start your GNOME GUI.

```
$ sudo systemctl start gdm
```

* For logging in you need a user on your device to log into it. You can create one before step 3 by this command (replace the ‘username’ with name that you want) :

```
$ sudo adduser username
```

* You can jump between GUIs that you install (like gnome-session) by the setting button that locates in the down right corner of the home screen.

#### List Of Supported OS

| **OS**                                                        |                                                                       |
| ------------------------------------------------------------- | --------------------------------------------------------------------- |
| ![](<../../../.gitbook/assets/image-20211024-150854 (2).png>) | [Debian](https://github.com/SolidRun/build_rzg2lc)                    |
| ![](<../../../.gitbook/assets/image-20211024-151110 (3).png>) | [RZ/G2LC Yocto](https://github.com/SolidRun/meta-solidrun-arm-rzg2lc) |
| ![](<../../../.gitbook/assets/image-20211024-150920 (2).png>) | [Buildroot](https://github.com/SolidRun/build_rzg2lc)                 |

## Build from source

* [https://github.com/SolidRun/build\_rzg2lc](https://github.com/SolidRun/build_rzg2lc)

[Buy a Sample Now](https://shop.solid-run.com/product/SRG2L-EVKHR-R00/)

## Documentation

|                                                                                                                                                                                                                                                                                                                                                                                                                                      | File                                                                                                                                      | Modified                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#section-5c40713c-9e48-4894-96fd-74067112dee3">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/411861047/HummingBoard-REV.2.5-pcb.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>          | ZIP Archive [HummingBoard-REV.2.5-pcb.zip](../../../wiki/download/attachments/411861047/HummingBoard-REV.2.5-pcb.zip)                     | Feb 28, 2023 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#section-958bf187-d67b-44b7-8cb9-d6eba003327d">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/411861047/HummingBoard+Mechanical+Drawings.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>  | ZIP Archive [HummingBoard Mechanical Drawings.zip](../../../wiki/download/attachments/411861047/HummingBoard%20Mechanical%20Drawings.zip) | Feb 28, 2023 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#section-3bff0940-25c3-48d5-9d20-d3cff825bb0f">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/411861047/HummingBoard-Part-Assembly.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>        | ZIP Archive [HummingBoard-Part-Assembly.zip](../../../wiki/download/attachments/411861047/HummingBoard-Part-Assembly.zip)                 | Feb 28, 2023 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#section-54fd271e-434e-42a3-a54f-73a94a9a05e3">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/411861047/HummingBoard+Gerbers.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>              | ZIP Archive [HummingBoard Gerbers.zip](../../../wiki/download/attachments/411861047/HummingBoard%20Gerbers.zip)                           | Feb 28, 2023 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2lc-som-quick-start-guide.md#section-f3eb9e47-0109-4d1d-bd3c-3e6566dad5db">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/411861047/hummingboard-v2.5-Full-schematics.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | PDF File [hummingboard-v2.5-Full-schematics.pdf](../../../wiki/download/attachments/411861047/hummingboard-v2.5-Full-schematics.pdf)      | Feb 28, 2023 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |

[Download All](../../../wiki/download/all_attachments)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
