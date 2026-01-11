# HummingBoard IIOT & RZ/V2N SOM Quick Start Guide

![IIOT Sideways.png](<../../../.gitbook/assets/IIOT Sideways (1).png>)

## Introduction

The following quick start guide provides background information about the HummingBoard IIOT.

The guide will give a technical overview about the product and by the end of it you should be able to boot an operating system and begin testing your application.

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Revision** | **Notes**       |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 20 Nov 2025       | Yazan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1.0          | Initial release |
| Table of Contents | <p>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#hardware-setup">Hardware Setup</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#product-specifications">Product specifications</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#block-diagram">Block Diagram</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#visual-features-overview">Visual features overview</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#booting-from-spi-and-loading-yocto-from-usd-card">Booting from SPI and loading Yocto from uSD card</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#boot-select">Boot Select</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#streaming-usb-webcam-video-from-rz-v2n-yocto-to-a-pc">Streaming USB Webcam Video from RZ/V2N Yocto to a PC</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#1-yocto-image-requirements">1. Yocto Image Requirements</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#2-installing-gstreamer-on-the-pc">2. Installing GStreamer on the PC</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#3-verifying-webcam-detection-on-rz-v2n-yocto-before-streaming-verify-that-the-usb-webcam-is-detected">3. Verifying Webcam Detection on RZ/V2N (Yocto) Before streaming, verify that the USB webcam is detected.</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#check-usb-enumeration">Check USB enumeration</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#check-video-devices">Check video devices</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#if-no-dev-video0-found">If no /dev/video0 found</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#check-supported-formats">Check supported formats</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#4-network-streaming-overview">4. Network Streaming Overview</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#5-gstreamer-commands">5. GStreamer Commands</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#51-on-the-rz-v2n-sender-yocto">5.1 On the RZ/V2N (Sender – Yocto)</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#52-on-the-pc-receiver">5.2 On the PC (Receiver)</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#linux-ubuntu-fedora-debian-etc">Linux (Ubuntu, Fedora, Debian, etc.)</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#windows-powershell">Windows (PowerShell)</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#tlv-eeprom-support">TLV EEPROM Support</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#list-of-supported-os">List Of Supported OS</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#build-from-source">Build from source</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#documentation">Documentation</a><br>- <a href="hummingboard-iiot-rz-v2n-som-quick-start-guide.md#related-articles">Related Articles</a></p> |              |                 |

## Hardware Setup

#### Product specifications

| **Model**               | HummingBoard RZ/V2N IIOT SBC                                                                                                                                                  |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Processor**           | <p><a href="https://www.solid-run.com/embedded-industrial-iot/renesas-rz-family/rz-v2n-som/">Renesas RZ/V2N SOM</a> 4 x Arm Cortex-A55<br>1 x Cortex-M33<br>Up to 1.8 GHz</p> |
| **Memory & Storage**    | <p>Up to 8GB LPDDR4<br>Up to 128GB eMMC<br>MicroSD</p>                                                                                                                        |
| **AI Accelerator**      | DRP-AI3 (15 Sparse TOPS / 4 Dense TOPS)                                                                                                                                       |
| **Display**             | MIPI-DSI                                                                                                                                                                      |
| **I/Os**                | <p>2 x RS232, 2 x RS485, or RS232 + RS485<br>2 x CAN-FD<br>2 x USB2.0<br>1 x USB3.2<br>1 x MIPI-CSI 4 lanes</p>                                                               |
| **Networking**          | <p>2 x Ethernet RJ45 10/100/1000<br>1 x 802.11 a/b/g/n/ac WiFi and Bluetooth (2.4/5 GHz)</p>                                                                                  |
| **Misc.**               | <p>GPIO<br>RTC<br>EEPROM</p>                                                                                                                                                  |
| **Power**               | <p>7V – 32V<br>PoE sink support 802.3at<br>Reverse polarity support</p>                                                                                                       |
| **Expansion card I/Os** | <p>M.2 B-Key LTE modem<br>(eSIM, NanoSim)</p>                                                                                                                                 |
| **Temperature**         | Industrial: -40°C to 85°C                                                                                                                                                     |
| **Dimensions**          | <p>PCBA: 88 x 135 mm<br>Enclosure (Optional): 150 x 145 x 40mm</p>                                                                                                            |
| **Enclosure**           | Extruded aluminum                                                                                                                                                             |
|                         | [Buy Now](https://www.solid-run.com/contact-us/)                                                                                                                              |

> \[!INFO] Supported with RZ/V2N SOM. For more detailed information about our SOM RZ/V2N series please visit this user manual : RZ/V2N SOM Hardware User Manual .

#### Block Diagram

The following figure describes the RZ/V2N Block Diagram.

![image-20251120-123530.png](../../../.gitbook/assets/image-20251120-123530.png)

#### Visual features overview

Please see below the features overview of the connector side of the HummingBoard IIOT & RZ/V2N SOM.

![image-20251120-123507.png](../../../.gitbook/assets/image-20251120-123507.png)

Print side connector overview of the HummingBoard IIOT & RZ/V2N SOM.

![image-20240929-120103.png](<../../../.gitbook/assets/image-20240929-120103 (1).png>)

![image-20241215-105449.png](../../../.gitbook/assets/image-20241215-105449.png)

**Power Input Polarity \[J1]:**

* **Connector Type**: Green two-terminal connector \[J1].
* **Voltage Range**: 7V to 32V.
* **Polarity**:
  * **+ (Positive)**: Left terminal (as marked in the image).
  * **- (Negative)**: Right terminal (as marked in the image).

> \[!NOTE] Plug for connector **J1** : 2 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm).

**J5004** {2x RS485, 2x CAN-FD, 2x RS232, DIG\_IN, DIG\_OUT}

![image-20241013-104136.png](../../../.gitbook/assets/image-20241013-104136.png)

![image-20241121-134703.png](<../../../.gitbook/assets/image-20241121-134703 (1).png>)

> \[!NOTE] Plug for connector **J5004** : 20 Position Terminal Block Plug, Female Sockets 0.138" (3.50mm) like [this](https://www.digikey.com/en/products/detail/phoenix-contact/1738885/3606115).

## Software Setup

#### Cable setup and prerequisites

Here is what you will need to power up and use the board:

* Linux or Windows PC
* HummingBoard IIOT with SOM
* 12V Power adapter (HummingBoard IIOT has wide range input of 7V-28V), alternatively you can use a PoE injector to power on the device.
* Type-C to USB for console, the HummingBoard IIOT has an onboard FTDI chip.
* IP router or IP switch

## Boot Select

![image-20240901-112851.png](<../../../.gitbook/assets/image-20240901-112851 (1).png>)

Before powering up the board for the first time it is recommended to select the boot media using onboard DIP switch **S5**:

| **Switch**            | <p><strong>1</strong><br>(MD0)</p> | <p><strong>2</strong><br>(MD1)</p> | <p><strong>3</strong><br>N/A</p> | <p><strong>4</strong><br>N/A</p> | <p><strong>5</strong><br>(VDD_1.8V)</p> | <p><strong>6</strong><br>(VDD_3.3V)</p> |
| --------------------- | ---------------------------------- | ---------------------------------- | -------------------------------- | -------------------------------- | --------------------------------------- | --------------------------------------- |
| **SPI**               | OFF                                | **ON**                             | X                                | X                                | OFF                                     | **ON**                                  |
| **eMMC**              | **ON**                             | OFF                                | X                                | X                                | OFF                                     | **ON**                                  |
| **Serial Dowanloder** | **ON**                             | **ON**                             | X                                | X                                | OFF                                     | **ON**                                  |

> \[!INFO] **MDx = BOOT\_MODEx.**\
> **VDD\_BOOT** can be either **1.8V** or **3.3V** (selectable via **S5\[5]** or **S5\[6]**).
>
> * **BOOT\_MODE2 = ‘1’** → fixed to **1.8V** at the SOM level
> * **BOOT\_MODE3** and **BOOT\_MODE4** → fixed to **GND** at the SOM level **Note:** MD1 and MD0 are swapped between **PCB version 1.1** and **PCB version 1.0**.

## Booting from SPI and loading Yocto from uSD card

## Boot Select

Here is the correct DIP switch position for SPI boot:

![image-20251120-125321.png](../../../.gitbook/assets/image-20251120-125321.png)

> \[!INFO] Note: The black rectangle represents the switch position. The unit comes with a pre-programmed bootloader on the SPI NOR flash.

Once you set the switches, you can apply the following for booting from an SPI card.

1. **Downloading the Yocto image**

Download the Debian image by running the following command on your Linux/Windows PC:

```
wget https://solid-run-images.sos-de-fra-1.exo.io/renesas/rzv2n/core-image-weston-rzv2n-evk.rootfs-20251224162903.wic.gz
```

* For more Debian releases, please visit [https://images.solid-run.com/renesas/rzv2n](https://images.solid-run.com/renesas/rzv2n).

2. **Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
gunzip -dc core-image-weston-rzv2n-evk.rootfs-20251224162903.wic.gz | dd of=/dev/sdX bs=4k conv=fdatasync 
```

* For more information, please visit [Flashing an SD Card](../../other-articles/flashing-an-sd-card.md) .

> \[!NOTE] Note: Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

3. **SD card insertion**

Please Insert the SD card into your device.

4. **Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

5. **Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, you should be able to see the following:

![image-20251120-160133.png](../../../.gitbook/assets/image-20251120-160133.png)

* In order to be able to log in, please insert “**root**” as a username and password.

## Streaming USB Webcam Video from RZ/V2N Yocto to a PC

This section describes how to stream live video from a USB webcam connected to a **SolidRun RZ/V2N** board running **Yocto Linux**, and display the video on a **remote PC** (Linux or Windows) over the network using **GStreamer**.\
The streaming pipeline uses **MJPEG over RTP**, which is supported by most USB webcams and does not require hardware H.264 encoding on the device.

GStreamer provides command-line tools for capturing, encoding, sending, receiving, and displaying video streams.

### **1. Yocto Image Requirements**

* v4l2 support
* GStreamer core + good/bad/ugly plugins
* v4l-utils (recommended)

Suggested additions to `local.conf` if missing:

```
IMAGE_INSTALL:append = " gstreamer1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly v4l-utils "
```

### **2. Installing GStreamer on the PC**

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

### **3. Verifying Webcam Detection on RZ/V2N (Yocto)**

Before streaming, verify that the USB webcam is detected.

#### **Check USB enumeration**

```
lsusb
```

Example:

```
Bus 001 Device 004: ID 046d:085c Logitech, Inc. C922 Pro Stream Webcam
```

#### **Check video devices**

```
ls /dev/video*
```

Expected:

```
/dev/video0
```

> \[!NOTE]
>
> #### **If no /dev/video0 found**
>
> Enable UVC driver:
>
> ```
> modprobe uvcvideo
> ```

#### **Check supported formats**

```
v4l2-ctl --list-formats -d /dev/video0
```

Typical output:

```
YUYV 4:2:2
MJPG
```

_**Note**:_ The Logitech C922 supports MJPEG, so MJPEG-over-RTP streaming is used.

### **4. Network Streaming Overview**

1. The RZ/V2N board captures MJPEG frames from the USB webcam (`/dev/video0`).
2. Frames are packetized into **RTP** and sent via **UDP** to the PC on port **5000**.
3. The PC receives the RTP stream, extracts the MJPEG frames, decodes them, and displays the video.

### **5. GStreamer Commands**

#### **5.1 On the RZ/V2N (Sender – Yocto)**

Replace `<LAPTOP_IP>` with the IP address of the PC receiving the video.\
Example: `192.168.33.17`

```
gst-launch-1.0 -v \
  v4l2src device=/dev/video0 ! \
  image/jpeg,width=1280,height=720,framerate=30/1 ! \
  rtpjpegpay ! \
  udpsink host=<LAPTOP_IP> port=5000 sync=false async=false
```

**Pipeline explanation**

* **v4l2src** – captures video from the webcam
* **image/jpeg** – requests MJPEG format
* **rtpjpegpay** – packetizes JPEG frames into RTP
* **udpsink** – sends RTP stream to the PC

***

#### **5.2 On the PC (Receiver)**

**Linux (Ubuntu, Fedora, Debian, etc.)**

```
gst-launch-1.0 -v \
  udpsrc port=5000 caps="application/x-rtp,encoding-name=JPEG,payload=26" ! \
  rtpjpegdepay ! \
  jpegdec ! \
  videoconvert ! \
  autovideosink sync=false
```

**Windows (PowerShell)**

```
gst-launch-1.0 -v `
  udpsrc port=5000 caps="application/x-rtp,encoding-name=JPEG,payload=26" ! `
  rtpjpegdepay ! `
  jpegdec ! `
  videoconvert ! `
  autovideosink sync=false
```

**Pipeline explanation**

* **udpsrc** – receives RTP packets
* **rtpjpegdepay** – extracts MJPEG frames
* **jpegdec** – decodes JPEG video
* **autovideosink** – displays the video on the PC

## TLV EEPROM Support

RZ/V2N SoMs are being programmed with identifying information such as the product name, MAC Address and SKUs to allow for programmatic identification of hardware.

## List Of Supported OS

| **OS**                                                        |   |
| ------------------------------------------------------------- | - |
| ![](<../../../.gitbook/assets/image-20211024-150854 (2).png>) |   |
| ![](<../../../.gitbook/assets/image-20211024-151110 (3).png>) |   |
| ![](<../../../.gitbook/assets/image-20211024-150920 (2).png>) |   |

## Build from source

* [GitHub - SolidRun](https://github.com/SolidRun/)

## Documentation

|   | File | Modified |
| - | ---- | -------- |

No files shared here yet.

* Drag and drop to upload or \[browse for files]&#x20;

Upload file

File description

[Buy a Sample Now](https://shop.solid-run.com/?s=%22HummingBoard+Pulse%22\&post_type=product&_ga=2.156269240.2016484779.1641802897-2012112798.1622706355)

## Related Articles

Error rendering macro 'contentbylabel' : CQL was parsed but the search manager was unable to execute the search. Error message: com.atlassian.confluence.api.service.exceptions.scale.SSStatusCodeException: There was an illegal request passed to XP-Search Aggregator API : HTTP/1.1 403 Forbidden
