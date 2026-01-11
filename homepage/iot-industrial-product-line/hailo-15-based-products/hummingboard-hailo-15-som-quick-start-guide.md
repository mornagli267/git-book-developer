# HummingBoard & Hailo 15 SOM Quick Start Guide

## HummingBoard & Hailo 15 SOM Quick Start Guide

### Introduction

The following quick start guide provides background information about the [SolidRun Hailo 15 SOM](https://www.solid-run.com/hailo-15-som/).

The guide will give a technical overview of the product. By the end of it, you should be able to boot an operating system and run a demo application.

### Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Revision** | **Notes**                                |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------------------------------- |
| 12 May 2024       | Mikhail Anikin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.0          | Initial release                          |
| 12 Aug 2024       | Mikhail Anikin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.1          | Update flashing process                  |
| 06 Nov 2024       | Mikhail Anikin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.2          | Add IIoT support                         |
| 16 Dec 2024       | Mikhail Anikin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.3          | Update flashing process                  |
| 22 Dec 2024       | Mikhail Anikin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1.4          | Introducing SW update                    |
| 11 Dec 2025       | Yazan Shhady                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1.5          | Correct DC input voltage range to 7V–18V |
| Table of Contents | <p>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#product-specifications">Product specifications</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#visual-features-overview">Visual Features Overview</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#boot-select-and-boot-options">Boot select and boot options</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#generating-yocto-image">Generating Yocto image</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#understanding-boot-artifacts">Understanding boot artifacts</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#booting-the-board">Booting the board:</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#running-the-demo-applications">Running the demo applications</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#using-gstreamer">Using GStreamer</a><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#using-vlc">Using VLC</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#hummingboardhailo15somquickstartguide-firmwareupdateprocess">Firmware update process</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#updating-firmware-with-swupdate-recommended">Updating firmware with SWUpdate (recommended)</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#manual-firmware-reflashing">Manual firmware reflashing</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#flashing-qspi-flash">Flashing QSPI flash</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#sending-u-boot-over-uart">Sending u-boot over uart</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#restoring-emmc-content">Restoring eMMC content.</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br><br>- <a href="hummingboard-hailo-15-som-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                                          |

### Hardware Setup

**Product specifications**

|                                  | Hailo 15 SOM with HummingBoard                                               |
| -------------------------------- | ---------------------------------------------------------------------------- |
| I/Os                             | 1 x MIPI-CSI on SOM                                                          |
| Networking                       | 1 x Ethernet RJ45 10/100/1000                                                |
| Processor                        | <p>Hailo 15 Quad-core Arm Cortex A53 1.3GHz<br><br>2 x Cortex M4, 200MHz</p> |
| Memory & Storage                 | <p>up to 8GB DDR4 RAM<br>Starting from 16GB eMMC</p>                         |
| Development and Debug interfaces | Micro USB                                                                    |
| Power                            | 7V – 18V                                                                     |
| Expansion card I/Os              | mikroBUS header                                                              |
| Temperature                      | <p>Commercial: 0°C to 70°C<br><br>Industrial: -40°C to 85°C</p>              |
| Dimensions                       | <p>PCBA: 100 x 70mm<br><br>Enclosure 120 x 80 x 30mm</p>                     |
| Enclosure                        | Extruded aluminium                                                           |

> \[!INFO] For more detailed information about Hailo 15 SOM, please visit the hardware user manual: [HAILO 15 SOM Hardware User Manual](hailo-15-som-hardware-user-manual.md)

**Visual Features Overview**

Please see below the features overview of the connector side of the HummingBoard Pro & Hailo 15

![image-20240513-080933.png](../../../.gitbook/assets/image-20240513-080933.png)

### Software Setup

**Cable setup and prerequisites**

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard with Hailo 15 SOM
* 12V Power adapter (HummingBoard has wide range input of 7V-36V, it is recommended to use 12V power adapter).
* The micro USB to USB for the console (the HummingBoard has an onboard FTDI chip).
* IP router or IP switch

### Boot select and boot options

You should select the boot source before powering up the board for the first time.

Hailo 15 with HummingBoard has two boot options: serial boot (for recovery) and eMMC boot (the main option). To select a boot option, the DIP switch needs to be modified.

For more information, see [HummingBoard Hailo 15 Boot Select](hailo-15-other-articles/hummingboard-hailo-15-boot-select.md)

### Generating Yocto image

The prebuilt artifacts are available [here](https://images.solid-run.com/Hailo/hailo15/meta-solidrun-arm-hailo).

Navigate to the meta layer repo for the build instructions: [meta-solidrun-arm-hailo](https://github.com/SolidRun/meta-solidrun-arm-hailo).

### Understanding boot artifacts

The following artifacts are generated by yocto build:

| **Artifact**                             | **Purpose**                                                                                           | **Target location** |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------- |
| hailo15\_scu\_bl.bin                     | SCU Bootloader                                                                                        | QSPI Flash          |
| hailo15\_scu\_fw.bin                     | SCU Firmware                                                                                          | QSPI Flash          |
| scu\_bl\_cfg\_a.bin, scu\_bl\_cfg\_b.bin | SCU Configuration                                                                                     | QSPI Flash          |
| customer\_certificate.bin                | Customer key certificate                                                                              | QSPI Flash          |
| u-boot.dtb.signed                        | U-Boot device tree                                                                                    | QSPI Flash          |
| u-boot-initial-env                       | U-Boot environment                                                                                    | QSPI Flash          |
| u-boot-spl.bin                           | U-Boot SPL                                                                                            | QSPI Flash          |
| u-boot-tfa.itb                           | TF-A and U-Boot                                                                                       | eMMC Boot partition |
| fitImage                                 | Linux kernel and device tree                                                                          | eMMC Boot partition |
| core-image-minimal-hailo15-solidrun.ext4 | RootFS                                                                                                | eMMC Root partition |
| core-image-minimal-hailo15-solidrun.wic  | Full eMMC image that contains both partitions. It can be flashed with bmap-tools using the .bmap file | eMMC                |
| hailo15\_uart\_recovery\_fw.bin          | Recovery firmware for reflashing QSPI                                                                 |                     |

### Booting the board:

The board is pre-flashed with a basic yocto image and AI demos.

1. **Serial connection**\
   Please insert the micro USB into your device. Then, you can refer to [Serial Connection](../../other-articles/serial-connection.md) to install the necessary serial connection software in Linux/Windows.
2. **Network connection**\
   The prebuilt image has a preset network configuration with a static IP `10.0.0.1`. Connect your PC to the board with a 1GbE RJ45 patch cord and set the static IP of your PC interface to `10.0.0.2`.
3. **Optional: Camera connection**\
   To evaluate the demo application, connect the MIPI-CSI camera to the Hailo 15 SOM MIPI-CSI interface before starting the boot.
4. **Power the board**\
   Plug in a power supply, and the board will start booting. You will see the boot log in the serial terminal:

> Poky (Yocto Project Reference Distro) 4.0.2 hailo15 ttyS1
>
> hailo15 login:

Use the following default credentials:

* Login: root
* Password: root

### Running the demo applications

#### Using GStreamer

Gstreamer is a CLI application that allows you to send, receive, and convert video streams.

1. Install gstreamer

For Ubuntu/Debian distros:

```
sudo apt install gstreamer1.0-plugins-ugly gstreamer1.0-plugins-bad gstreamer1.0-libav
```

For Fedora/RHEL distros:

```
sudo dnf install gstreamer1 gstreamer1-plugins-base gstreamer1-plugins-good gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free-gtk
```

For Windows:

* **Download the Installer**: Go to the [GStreamer official website](https://gstreamer.freedesktop.org/download/) and download the appropriate installer for your Windows version.
* **Run the Installer**: Execute the downloaded file. During installation, **select "Complete Installation"** to install all basic plugins.
* **Set Environment Variables**: To use GStreamer from the command line, add GStreamer to your system's PATH as described [here](https://gstreamer.freedesktop.org/documentation/installing/on-windows.html?gi-language=c).

> \[!INFO] For Windows, you might need to configure the Firewall to allow the stream. Make sure that `10.0.0.2` is a private network.

2. Run the gstreamer pipeline to start receiving a stream.

On **your pc** In a bash terminal or Windows cmd run:

```
gst-launch-1.0 -v udpsrc port=5000 address=0.0.0.0 ! application/x-rtp,encoding-name=H264 ! queue ! rtph264depay ! queue ! h264parse ! avdec_h264 ! queue ! videoconvert ! fpsdisplaysink video-sink=autovideosink text-overlay=false sync=false
```

3. Run the demo application on the **Hailo15 EVK**:

```
root@hailo15:~# ./apps/detection/detection.sh
```

#### Using VLC

Another option is to receive a stream using VLC media player.\\

1. Install VLCFor Ubuntu/Debian distros:

```
sudo apt install vlc
```

For Fedora/RHEL distros:

```
sudo dnf install vlc
```

For Windows:

* **Download the Installer**: Go to the [VLC official website](https://www.videolan.org/) and download the appropriate installer for your Windows version.
* **Run the Installer**: Execute the downloaded file. During installation, **select "Complete Installation"** to install all basic plugins.

> \[!INFO] For Windows, you might need to configure the Firewall to allow the stream. Make sure that `10.0.0.2` is a private network.

2. Create a stream configuration file `stream.sdp` with the following content:

![](https://developer.resources.solid-run.com/wiki/images/icons/grey_arrow_down.png)

stream.sdp

v=0\
o=- 0 0 IN IP4 127.0.0.1\
s=No Name\
c=IN IP4 10.0.0.2\
t=0 0\
a=tool:libavformat 58.20.100\
m=video 5000 RTP/AVP 96\
a=rtpmap:96 H264/90000

3. Open the `stream.sdp` in the vlc using the `Media -> Open File` tab.
4. Run the demo application on the **target**:

```
root@hailo15:~# ./apps/detection/detection.sh
```

> \[!NOTE] Note: VLC inserts its own 1s latency into the stream during the network cashing. You can decrease this latency in the settings.
>
> * Go to Tools > Preferences.
> * Show settings: select All at the bottom left to switch to the advanced preferences.
> * Under Input / Codecs, find Network.
> * Locate Network caching (ms) and reduce its value. The default is typically around 1000 ms (1 second). You might try lowering it to 100-300 ms, but be aware that too low a value can lead to stream instability or increased packet loss.

## Firmware update process

### Updating firmware with SWUpdate (recommended)

A part of the yocto build is a software update package (.swu). This image contains a full rootfs image, bootloaders, and qSPI content and will automatically flash all the artifacts in places.

1. Run an HTTP server on port 80 in the directory with the update image (.swu)

```
sudo python3 -m http.server 80
```

2. Reset the board. In the u-boot menu, select `SWUpdate`

```
  *** U-Boot Boot Menu ***

     Boot from eMMC
     Boot to flashing ramdisk
*    SWUpdate
     U-Boot console


  Press UP/DOWN to move, ENTER to select, ESC/CTRL+C to quit
```

> \[!INFO] If there is no SWUpdate item in the menu or an update was unsuccessful for any reason, please proceed to the next chapter “Manual firmware reflashing“.

> \[!INFO] A/B updates will be added in future firmware releases.

3. The board will boot, load the update image from IP 10.0.0.2, port 80 and update all the firmware components.

### Manual firmware reflashing

#### Flashing QSPI flash

Reflashing QSPI is only possible under Linux.

> \[!WARNING] Please make sure that u-boot-tools are installed in your system:
>
> * For Ubuntu/Debian: `sudo apt-get install u-boot-tools`
> * For Fedora/RHEL: `sudo dnf install uboot-tools`

1. Download the flashing tool and install it into your system.

```
python3 -m pip install hailo15_board_tools-x.x.x-py3-none-any.whl
```

2. Set the DIP switch to the [Serial download mode](hailo-15-other-articles/hummingboard-hailo-15-boot-select.md).
3. **Close the serial terminal on your PC**.
4. Reset the board.
5. Upload the uart flashing firmware into the SOM:

```
uart_boot_fw_loader --serial-device-name /dev/ttyUSB0 --firmware hailo15_uart_recovery_fw.bin 
```

6. Reflash QSPI content:

```
hailo15_spi_flash_program --serial-device-name /dev/ttyUSB0 --uart-load --scu-bootloader ./hailo15_scu_bl.bin --scu-bootloader-config scu_bl_cfg_a.bin --scu-firmware ./hailo15_scu_fw.bin --uboot-device-tree ./u-boot.dtb.signed --bootloader ./u-boot-spl.bin --bootloader-env ./u-boot-initial-env --customer-certificate ./customer_certificate.bin
```

> \[!INFO] Note: `hailo15_spi_flash_program` also allows to reflash selected parts of the QSPI Flash:
>
> * `hailo15_spi_flash_program --serial-device-name /dev/ttyUSB0 --uart-load --bootloader ./u-boot-spl.bin --bootloader-env ./u-boot-initial-env--scu-bootloader ./hailo15_scu_bl.bin`
> * `hailo15_spi_flash_program --serial-device-name /dev/ttyUSB0 --uart-load --uboot-device-tree ./u-boot.dtb.signed`
> * etc.

> \[!WARNING] This guide assumes that your serial terminal is `/dev/ttyUSB0`. Replace it with the proper device for your system.

#### Sending u-boot over uart

Hailo FW expects a firmware version match between proprietary firmware, SPL, u-boot, and kernel. After qSPI firmware was reflashed with uart boot mode, u-boot with the same fw version should be loaded. SPL uses the UART Y-Modem mode to load the `u-boot-tfa.itb` file over the serial connection.

1. Set the DIP switch to the [qSPI boot with Y-modem u-boot load](hailo-15-other-articles/hummingboard-hailo-15-boot-select.md).
2. Reset the board. You will see the board booted to SPL and expects u-boot to be sent with Y-modem:

> U-Boot SPL 2022.01 (Feb 04 2024 - 18:42:25 +0000)\
> Loading Environment from SPIFlash... OK\
> U-Boot SPL boot source uart\
> CCCCCCCCCC

The SPL waits for the Y-modem transfer to upload the u-boot into the RAM. The latest minicom already has a built-in Y-modem transfer function. With minicom, press Ctrl+A, then S, select `ymodem`, and then choose file `u-boot-tfa.itb`. Note: the transfer can take a few minutes. As soon as the u-boot is completely transferred, you will see the same u-boot entries as usual Proceed to the restoring eMMC with ramdisk.

#### Restoring eMMC content.

The u-boot menu has a special entry that allows you to load a ramdisk from an HTTP server and boot to it.

1. Run an HTTP server on port 80 in the directory with the image

```
sudo python3 -m http.server 80
```

2. In the u-boot menu, select `Boot to flashing ramdisk`
3. The Board will grub a ramdisk from the HTTP server on IP 10.0.0.2, port 80, and boot to it.
4. Once the board is booted to the ramdisk, flash eMMC:

```
bmaptool copy http://10.0.0.2/core-image-minimal-hailo15-solidrun.wic.zst /dev/mmcblk1
```

5. Reboot the board and restore the DIP switch to the [qSPI boot](hailo-15-other-articles/hummingboard-hailo-15-boot-select.md).

### List Of Supported OS

| **OS**                                                  |                                                                       |
| ------------------------------------------------------- | --------------------------------------------------------------------- |
| ![](../../../.gitbook/assets/image-20211024-151110.png) | [Hailo 15 Yocto](https://github.com/SolidRun/meta-solidrun-arm-hailo) |

### Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
