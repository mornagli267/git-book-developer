# SolidSense N8 Compact - redpesk

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Revision** | **Notes**       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 06 Mar 2022       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 1.0          | Initial release |
| Table of Contents | <p>- <a href="solidsense-n8-compact-redpesk.md#revision-and-notes">Revision and Notes</a><br>- <a href="solidsense-n8-compact-redpesk.md#introduction">Introduction</a><br>- <a href="solidsense-n8-compact-redpesk.md#what-is-redpesk">What is redpesk?</a><br>- <a href="solidsense-n8-compact-redpesk.md#redpesk-image-download">redpesk Image Download</a><br>- <a href="solidsense-n8-compact-redpesk.md#writing-the-image-to-your-sd-card">Writing the image to your SD card</a><br>- <a href="solidsense-n8-compact-redpesk.md#connect-to-the-solidsense-n8-iot-compact">Connect to the SolidSense N8 IoT Compact</a><br>- <a href="solidsense-n8-compact-redpesk.md#solidsense-n8-iot-compact-block-diagram">SolidSense N8 IoT Compact Block Diagram</a><br>- <a href="solidsense-n8-compact-redpesk.md#hardware-interfaces">Hardware interfaces</a><br>- <a href="solidsense-n8-compact-redpesk.md#step-by-step">Step-By-Step</a></p> |              |                 |

## Introduction

### What is redpesk?

![](../../../../.gitbook/assets/image-20220307-090739.png)

redpesk is a secure embedded all-in-one Linux software platform dedicated to Industrial IoT. It offers an easy-to-use pre-integrated CI/CD factory with more than 2,500 binary packages and a set of basic “ready-to-go” components that nearly every system requires.

* For more information, please visit [redpesk](https://docs.redpesk.bzh/docs/en/master/getting_started/docs/overview.html).

## redpesk Image Download

Create a directory for downloading image:

```
mkdir ~/redpeskimage
cd ~/redpeskimage
```

Download the image by using:

```
wget -r -nd -nc --no-parent -A "redpesk*smack*" 'https://download.redpesk.bzh/redpesk-lts/arz-1.0-update/images/smack/minimal/aarch64/solidrun-edge-gateways/latest'
```

* For more images releases, please visit [redpesk images](https://docs.redpesk.bzh/docs/en/master/redpesk-os/boards/docs/boards/download-images.html).

## Writing the image to your SD card

To flash your SD card, unxz the compressed file and use dd:

```
unxz redpesk*.raw.xz
IMAGE=$(ls redpesk*.raw)
sudo dd if=$IMAGE of=/dev/sdX bs=4M status=progress
```

> \[!NOTE] **Note:** Plug a micro SD into your Linux PC, the following assumes that the micro SD is added as /dev/sdX and all it’s partitions are unmounted.

## Connect to the SolidSense N8 IoT Compact

### **SolidSense N8 IoT Compact Block Diagram**

![](<../../../../.gitbook/assets/image-20211219-084606 (1).png>)

### Hardware interfaces

![](<../../../../.gitbook/assets/image-20211219-085810 (1).png>)

* You can visit our [guide](../solidsense-n8-compact-quick-start-guide.md) to get more information about the SolidSense N8 IoT Compact.

### Step-By-Step

* Plug in the SD Card into the board.
* Power on the board.
* Before powering up the board, make sure you have configured the boot media to microSD by setting the S1 switch on the boot source selector to **ON**:

|          |              |              |
| -------- | ------------ | ------------ |
|          | **Switch 1** | **Switch 2** |
| **SD**   | ON           | ON           |
| **eMMC** | OFF          | ON           |

* Connect the USB-UART cable following the three pins beside the SD card socket

![](<../../../../.gitbook/assets/image-20211219-165131 (1).png>)

Open your serial console, restart your device and you should be able to see the following.

![](../../../../.gitbook/assets/image-20220310-133343.png)

* In order to be able to log in , please insert “root” as a username and password.
* use `dmesg` to see the name of the USB plugged

```
[    4.514489] usb 1-6: FTDI USB Serial Device converter now attached to ttyUSB0 
```

* use picocom

```
 sudo picocom  -b 115200 /dev/ttyUSB0
```

* Getting the address of the board to be able to use a ssh connectionConnect an Ethernet cable between computer and SolidSense

```
 #on board
 ip -c a
 # on computer
 ssh root@<ip_board>
```
