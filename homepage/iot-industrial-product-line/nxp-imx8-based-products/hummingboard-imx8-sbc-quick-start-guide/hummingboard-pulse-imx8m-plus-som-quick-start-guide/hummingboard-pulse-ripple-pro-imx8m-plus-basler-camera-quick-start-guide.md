# HummingBoard Pulse/Ripple/Pro & i.MX8M Plus - Basler Camera Quick Start Guide

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Revision** | **Notes**          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------ |
| 17 Feb 2022       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1.0          | Initial release    |
| 08 Jun 2025       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1.1          | Update for new BSP |
| Table of Contents | <p>- <a href="hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md#revision-and-notes">Revision and Notes</a><br>- <a href="hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md#introduction">Introduction</a><br>- <a href="hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md#software-setup">Software Setup</a><br>- <a href="hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md#cable-setup-and-prerequisites">Cable setup and prerequisites</a><br>- <a href="hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md#image-download-and-sd-card-preparation">Image download and SD card preparation</a><br>- <a href="hummingboard-pulse-ripple-pro-imx8m-plus-basler-camera-quick-start-guide.md#camera-test">Camera Test</a></p> |              |                    |

## Introduction

The following provides a quick guide to start using the Camera Module on your HummingBoard Pulse and i.MX8M Plus SOM.

* For more information, please visit [i.MX8M PLUS SOM](https://www.solid-run.com/embedded-industrial-iot/nxp-i-mx8-family/imx8m-plus-som/).

## Software Setup

#### Cable setup and prerequisites

Here are the additional cables and prerequisites you will need for being able to get started with your Camera:

* HDMI / micro - HDMI cable.
* Camera kit ( see our [i.MX8M Plus - Camera Kit](https://www.solid-run.com/blog/articles/i-mx8m-plus-som-camera-kit/) ).

## Image download and SD card preparation

**1. Downloading the Yocto image:**

Find the latest `imx-image-full-*.wic.{zst,bmap}` targeting the i.MX8M Plus SoM at [images.solid-run.com](https://images.solid-run.com/IMX8/meta-solidrun-arm-imx8) - e.g. at the time of writing:

```
wget https://images.solid-run.com/IMX8/meta-solidrun-arm-imx8/scarthgap-lf-6.6.52-2.2.0/2025-06-08_24a365b/imx8mp-sr-som/imx-image-full-imx8mp-sr-som.rootfs.wic.zst
wget https://images.solid-run.com/IMX8/meta-solidrun-arm-imx8/scarthgap-lf-6.6.52-2.2.0/2025-06-08_24a365b/imx8mp-sr-som/imx-image-full-imx8mp-sr-som.rootfs.wic.bmap
```

**2. Writing the image to the SD card**

Use the following commands for writing the image to an SD card:

```
# Either with bmaptool (faster)
sudo bmaptool copy imx-image-full-imx8mp-sr-som.rootfs.wic.zst /dev/sdX
# Or with dd (slower)
zstdcat imx-image-full-imx8mp-sr-som.rootfs.wic.zst | sudo dd of=/dev/sdX bs=4M conv=fsync
```

* For more information, please visit [Flashing an SD Card](../../../../other-articles/flashing-an-sd-card.md) .

{% hint style="info" %}
**Note:** Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.
{% endhint %}


**3. SD card insertion**

Please Insert the SD card into your device.

**4. Power connection**

Connect your power adaptor to the DC jack, and then connect the adaptor to mains supply.

**5. Serial Connection**

Please insert the micro USB into your device, then you can refer to [Serial Connection](../../../../other-articles/serial-connection.md) for installing necessary serial connection software in Linux/Windows.

Once you installed the necessary serial connection software, reboot your device and you should be able to see the following:

![](../../../../../.gitbook/assets/image-20220217-161316.png)

* Please inset ‘root’ as a username for being able to log in as shown in the above picture.

## Camera Test

1. **Enable Basler Cameras in Software:**\
   Edit file `extlinux.conf` on the first partition of the board adding the line starting with “FDTOVERLAYS” - either from a PC, or from the device serial console, **then reboot**. The resulting file should look similar to the example below (line 5 is the important addition):

```
default Yocto
label Yocto
   kernel /Image
   fdtdir /
   FDTOVERLAYS ../freescale/imx8mp-sr-som-basler.dtbo ../freescale/imx8mp-hummingboard-pulse-basler.dtbo
append root=PARTUUID=076c4a2a-02 rootwait
```

For editing on device can use `nano` text editor:

```
mount /dev/mmcblk1p1 /boot
nano /boot/extlinux/extlinux.conf
# save with ctrl+o, exit with ctrl+x
sync
reboot
```

2. **Connect your HDMI cable.**

{% hint style="info" %}
**Note:** The camera preview only works when a monitor is connected to your Board.
{% endhint %}


3. **Connect your Camera to the CSI 2.0 of the carrier as shown in the picture below:**![](../../../../../.gitbook/assets/image-20220217-160655.png)

{% hint style="success" %}
A green LED will light up at the back panel of your camera. This is an indication of Camera is operating. See the following figure:
{% endhint %}


![](../../../../../.gitbook/assets/image-20220222-092818.png)

4. **Check available devices by running the following on your monitor:**

```
v4l2-ctl --list-devices
# Example Output:
 ():
        /dev/v4l-subdev0
        /dev/v4l-subdev4
        /dev/v4l-subdev5
 ():
        /dev/v4l-subdev1
        /dev/v4l-subdev6
        /dev/v4l-subdev7
 (csi0):
        /dev/v4l-subdev3
 (csi1):
        /dev/v4l-subdev2
FSL Capture Media Device (platform:32c00000.bus:camera):
        /dev/media0
mxc-isi-m2m_v1 (platform:32e00000.isi:m2m_devic):
        /dev/video2
VIV (platform:viv0):
        /dev/video3
VIV (platform:viv1):
        /dev/video4
vsi_v4l2dec (platform:vsi_v4l2dec):
        /dev/video1
vsi_v4l2enc (platform:vsi_v4l2enc):
        /dev/video0
viv_media (platform:vvcam-video.0):
        /dev/media1
```

The relevant capture devices associated with the cameras are the ones named “VIV (platform:vivX)”:\
\- “VIV (platform:viv0)” (`/dev/video3`): Camera Connector on HummingBoard\
\- “VIV (platform:viv1)” (`/dev/video4`): Camera Connector on System on Module\
If the numbering changed, substitute the video device numbers (3,4) accordingly in the following steps. 5. **Render from Camera to HDMI Display with gstreamer:**

```
# for HummingBoard Camera Connector
gst-launch-1.0 -v v4l2src device=/dev/video3 ! "video/x-raw,format=YUY2,width=1920,height=1080" ! queue ! imxvideoconvert_g2d ! waylandsink
# for System on Module Camera Connector
gst-launch-1.0 -v v4l2src device=/dev/video4 ! "video/x-raw,format=YUY2,width=1920,height=1080" ! queue ! imxvideoconvert_g2d ! waylandsink
```

6. **Run NXP Video Demo to render from Camera to HDMI Display:**

```
systemctl stop weston weston.socket
cd /opt/imx8-isp/bin
# for HummingBoard Camera Connector
./video_test -w 1920 -h 1080 -f YUYV -t drm -m 0 -d 3
# for System on Module Camera Connector
./video_test -w 1920 -h 1080 -f YUYV -t drm -m 0 -d 4
```

Once you run the previous commands, you can direct your camera to an object and start monitoring as shown in the following figure:

![](<../../../../../.gitbook/assets/unnamed (1)-20220223-084738.jpg>)

The following is an implementation of what the camera displays on the monitor screen.

![](../../../../../.gitbook/assets/IMG-2338-20220217-150818.jpg)
