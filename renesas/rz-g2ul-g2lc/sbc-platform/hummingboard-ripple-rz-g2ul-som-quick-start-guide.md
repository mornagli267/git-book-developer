# HummingBoard Ripple & RZ/G2UL SOM Quick Start Guide

![hb-ripple-rzg2lc.png](../../../.gitbook/assets/hb-ripple-rzg2lc.png)

## Introduction

The following quick start guide provides background information about the HummingBoard RZ/G2UL.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Revision** | **Notes**       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| Feb 5, 2024       | Shahar Fridman                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1.0          | Initial release |
| Table of Contents | <p>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#introduction">Introduction</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#revision-and-notes">Revision and Notes</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#hardware-setup">Hardware Setup</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#product-specifications">Product specifications</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#block-diagram">Block Diagram</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#visual-features-overview">Visual features overview</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#software-setup">Software Setup</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#boot-select">Boot Select</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#generating-yocto-buildroot-and-debian-image">Generating Yocto, Buildroot and Debian image</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#booting-from-sd-card">Booting from SD card</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#more-features">More Features</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#list-of-supported-os">List Of Supported OS</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#build-from-source">Build from source</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#documentation">Documentation</a><br>- <a href="https://solidrun.atlassian.net/wiki/spaces/developer/pages/411861047/HummingBoard+Ripple+RZ+G2LC+SOM+Quick+Start+Guide#related-articles">Related Articles</a></p> |              |                 |

## Hardware Setup

#### Product specifications

|                                  | HUMMINGBOARD RZ/G2UL                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| I/Os                             | <p>2 x USB 2.0<br><br>1 x MIPI-CSI-2</p>                                                |
| Networking                       | <p>1 x Ethernet 100BASE-T<br><br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4 GHz)</p> |
| Processor                        | Renesas RZ/G2UL Single MPcore Arm Cortex A55 up to 1.0GHz + Cortex M33 200MHz           |
| Memory & Storage                 | <p>Up to 2 GB DDR4<br>8GB eMMC up to 64 GB<br>MicroSD</p>                               |
| Display                          | None                                                                                    |
| Misc.                            | <p>1 x Reset button<br>1 x Configurable button<br>3 x LED indicators<br>RTC</p>         |
| Development and Debug interfaces | Micro USB                                                                               |
| Power                            | 7V – 36V                                                                                |
| Expansion card I/Os              | <p>mikroBUS header<br>Mini Pcie with SIM holder</p>                                     |
| Temperature                      | <p>Commercial: 0°C to 70°C<br>Industrial: -40°C to 85°C</p>                             |
| Dimensions                       | <p>PCBA: 100 x 70mm<br>Enclosure: 120 x 80 x 30mm</p>                                   |
| Enclosure                        | Extruded aluminium                                                                      |
|                                  | [Buy Now](https://shop.solid-run.com/product/SRG2L-EVKHBPRO-R01/)                       |

#### Block Diagram

The following figure describes the RZ/G2UL Block Diagram.

![image-20240205-113315.png](../../../.gitbook/assets/image-20240205-113315.png)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard Ripple & RZ/G2UL.

![image-20240319-091912.png](../../../.gitbook/assets/image-20240319-091912.png)

Print side connector overview of the HummingBoard Ripple & RZ/G2UL.

![image-20211104-110340.png](<../../../.gitbook/assets/image-20211104-110340 (1).png>)

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard Ripple with RZ/G2UL SOM (HummingBoard RZ/G2UL)
* 12V Power adapter (HummingBoard Ripple has wide range input of 7V-36V, it is recommended to use 12V power adapter).
* Micro USB to USB for console, the HummingBoard Ripple has an onboard FTDI chip.
* IP router or IP switch
* USB Disk and SD Card

## Boot Select

Before powering up the board for the first time it is recommended to select the boot media. In order to configure the boot media, please refer to [HummingBoard RZ/G2UL Boot Select](rz-g2-other-articles/hummingboard-rz-g2lc-g2ul-g2l-v2l-boot-select.md#when-using-hummingboard-ripple-rz-g2lc-or-rz-g2ul-som) .

{% hint style="info" %}
eMMC and SD connect to the same SDIO signals via MUX so we can’t have access to the SD & eMMC at the same time, select eMMC/SD by setting switch **S3**{6} → off : eMMC , on : SD
{% endhint %}


## Generating Yocto, Buildroot and Debian image

**Buildroot/Debian**

1. Clone the repository [rz-g2ul\_build](https://github.com/SolidRun/build_rzg2lc/tree/rzg2ul-rc1) and move your terminal to this directory.
2. In this stage you can modify your image configs as you want, you can find more info about it the the repository.
3. Build your own image by this command

```
$ MACHINE=rzg2ul-hummingboard Distro=<Buildroot/Debian> ./runme.sh
```

**Yocto \<TBD - Comig Soon>**

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
$ MACHINE=rzg2ul-hummingboard bitbake <target>
```

* NOTE: Choose your relevant target, for example:\
  -core-image-bsp: cli image.\
  -core-image-weston: graphical image.\
  -core-image-qt: graphical image including qt.

## Booting from SD card

The following shows how to set the switches on the boot source selector:

![image-20221123-220813.png](../../../.gitbook/assets/image-20221123-220813.png)

{% hint style="info" %}
Please Note: The black rectangle represents the switch position.
{% endhint %}


Once you set the switches, you can apply the following for booting from SD card:

1. **Downloading the image**\
   Download the image (for example Debian) by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/RZ/rzg2lc_build/20231122-6391518/rzg2lc-solidrun-sd-debian-6391518.img.xz
```

* For more Debian releases, please visit [Debian Releases for RZ/G2UL](https://images.solid-run.com/RZ/rzg2lc_build).

2. **Writing the image to the SD card**\
   Use the following commands for writing the image to an SD card:

```
xz -dc rzg2ul-solidrun-sd-debian-6391518.img.xz | dd of=/dev/sdX bs=4k conv=fdatasync 
```

* For more information, please visit [Flashing an SD Card](/other-articles/flashing-an-sd-card.md) .
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
   Hold on the **On/Off** Power button - **SW1** (as shown in the figure below)![image-20230228-151346.png](../../../.gitbook/assets/image-20230228-151346.png)

* **Note:** The system should turn on by default when the power is connected (without pressing the button).

6. **Serial Connection**\
   Please insert the micro USB into your device, then you can refer to [Serial Connection](/other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.\
   Once you installed the necessary serial connection software, you should be able to see the following:

![image-20231127-133436.png](../../../.gitbook/assets/image-20231127-133436.png)

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

![image-20231206-093535.png](../../../.gitbook/assets/image-20231206-093535.png)

After those steps you should end the process in this way (step 4 to the end):

![image-20231206-094407.png](../../../.gitbook/assets/image-20231206-094407.png)

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

{% hint style="info" %}
RZ/G2UL SOM **does not** support a Display port interface, so Debian GUI is not relevant for this product.
{% endhint %}


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
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2ul-som-quick-start-guide.md#section-914ef429-48cf-4c1b-88f5-eda67a86a1d9">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/598212944/HummingBoard-REV.2.5-pcb.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>          | ZIP Archive [HummingBoard-REV.2.5-pcb.zip](../../../wiki/download/attachments/598212944/HummingBoard-REV.2.5-pcb.zip)                     | Mar 19, 2024 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2ul-som-quick-start-guide.md#section-9e4afd9c-28b6-49ed-afd9-4174bd5481b1">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/598212944/HummingBoard+Mechanical+Drawings.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>  | ZIP Archive [HummingBoard Mechanical Drawings.zip](../../../wiki/download/attachments/598212944/HummingBoard%20Mechanical%20Drawings.zip) | Mar 19, 2024 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2ul-som-quick-start-guide.md#section-b8b84a17-a9f4-4a1c-b9c0-719fd470bbf4">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/598212944/HummingBoard-Part-Assembly.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>        | ZIP Archive [HummingBoard-Part-Assembly.zip](../../../wiki/download/attachments/598212944/HummingBoard-Part-Assembly.zip)                 | Mar 19, 2024 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2ul-som-quick-start-guide.md#section-663d4635-77c0-44a5-9baf-cebca903568a">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/598212944/HummingBoard+Gerbers.zip">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p>              | ZIP Archive [HummingBoard Gerbers.zip](../../../wiki/download/attachments/598212944/HummingBoard%20Gerbers.zip)                           | Mar 19, 2024 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |
| <p>Labels<br><br>- No labels<br>- <a href="hummingboard-ripple-rz-g2ul-som-quick-start-guide.md#section-08e86e93-c6d0-4dec-afdd-74ca2b64c97f">Edit Labels</a><br><br>[Preview] <a href="../../../wiki/download/attachments/598212944/hummingboard-v2.5-Full-schematics.pdf">View</a> <a href="../../../wiki/pages/editattachment.action">Properties</a> <a href="../../../wiki/pages/confirmattachmentremoval.action">Delete</a></p> | PDF File [hummingboard-v2.5-Full-schematics.pdf](../../../wiki/download/attachments/598212944/hummingboard-v2.5-Full-schematics.pdf)      | Mar 19, 2024 by [Yazan Shhady](../../../wiki/people/5f67bce9ed55c7006abc6319/) |

* Drag and drop to upload or \[browse for files]&#x20;

Upload file

File description

[Download All](../../../wiki/download/all/_attachments)

## Related Articles <a href="#hummingboardripple-and-rz-g2ulsomquickstartguide-relatedarticles" id="hummingboardripple-and-rz-g2ulsomquickstartguide-relatedarticles"></a>

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
