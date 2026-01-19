# Hailo-8 in Bedrock R8000 | R7000

## Hailo-8 in Bedrock R8000 | R7000

This guide explains how to install Hailo’s hailo\_pci driver, hailortcli and tappas.\
It was tested on

### **Table of Contents**

* [Required packages](../../../../other-articles/snippets/hailo-8-driver-hailortcli-tappas-installation.md#required_packages)
* [Driver compilation & installation](../../../../other-articles/snippets/hailo-8-driver-hailortcli-tappas-installation.md#driver_compilation)
  * [Method 1 (Host)](../../../../other-articles/snippets/hailo-8-driver-hailortcli-tappas-installation.md#method1)
  * [Method 2 (Docker)](../../../../other-articles/snippets/hailo-8-driver-hailortcli-tappas-installation.md#method2)
* [Testing using hailortcli benchmark](../../../../other-articles/snippets/hailo-8-driver-hailortcli-tappas-installation.md#testing)

### Required packages

```
sudo apt-get update
sudo apt-get upgrade
```

```
sudo apt-get install -y rsync ffmpeg g++-12 x11-utils python3-dev python3-pip python3-setuptools python3-virtualenv python-gi-dev libgirepository1.0-dev gcc-9 g++-9 cmake git libzmq3-dev unzip 
```

```
sudo apt-get install -y libopencv-dev python3-opencv 
```

```
sudo apt-get install -y libcairo2-dev libgirepository1.0-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio gcc-9 g++-9 python-gi-dev 
```

```
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 
```

### Driver compilation and installation

**Clone the driver repository**&#x20;

```
# If using Host, clone:
git clone https://github.com/hailo-ai/hailort-drivers.git 
git checkout hailo8

# If using Docker (driver V4.15 is required), download:
wget https://github.com/hailo-ai/hailort-drivers/archive/refs/tags/v4.15.0.zip
```

&#x20;**Compile the driver**&#x20;

```
cd hailort-drivers/linux/pcie 
make all
```

&#x20;**Install the driver**&#x20;

```
sudo make install
```

&#x20;**Check installation**&#x20;

```
sudo modprobe hailo_pci
```

&#x20;**Download firmware**&#x20;

```
cd ../..
./download_firmware.sh 
mkdir /lib/firmware/hailo 
sudo mv hailo8_fw.<VERSION>.bin /lib/firmware/hailo/hailo8_fw.bin
```

**Optional (set udev rules and reload the rules)**&#x20;

```
sudo cp ./linux/pcie/51-hailo-udev.rules /etc/udev/rules.d/ 
sudo udevadm control --reload-rules && sudo udevadm trigger
```

## Method 1 Host

### Installing HailortCli

**Clone the Hailort repository**&#x20;

```
git clone https://github.com/hailo-ai/hailort.git
git checkout hailort-v4.22.0
```

**Compile sources**&#x20;

```
cd hailort
cmake . -Bbuild -DCMAKE_BUILD_TYPE=Release -DHAILO_BUILD_GSTREAMER=1 -DCMAKE_INSTALL_PREFIX=/usr
sudo cmake --build build --target install
```

**Testing**

Run:

```
sudo hailortcli fw-control identify
```

If for some reason the –target install does not install hailortcli to the machine run the following line and try retesting:&#x20;

```
cp build/hailort/hailortcli/hailortcli /usr/bin/
```

Output will look something like this:

```
Output will look somewhat like this: 
# hailortcli fw-control identify 
Executing on device: 0000:01:00.0 
Identifying board 
Control Protocol Version: 2 
Firmware Version: 4.16.2 (release,app,extended context switch buffer) 
Logger Version: 0 
Board Name: Hailo-8 
Device Architecture: HAILO8 
Serial Number: xxxxxxxxxxxxxxx
Part Number: xxxxxxxxxxx 
Product Name: HAILO-8 AI ACC M.2 M KEY MODULE EXT TEMP 
```

### Installing TAPPAS

**Clone & set-up tappas repostitory**&#x20;

```
git clone https://github.com/hailo-ai/tappas.git 
cd tappas 
```

```
# Use this only on ubuntu 23.04
cp tools/run_app/requirements_20_04.txt tools/run_app/requirements_23_04.txt 
```

```
sudo ln -s /usr/lib/x86_64-linux-gnu/libhailort.so.<version> /usr/lib/libhailort.so 
sudo ln -s /usr/lib/x86_64-linux-gnu/libgsthailo.so /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgsthailo.so
```

{% hint style="info" %}
Ubuntu 23.04 requires to change pybind version from 2.9 to 2.10 in:\
hailo-ai/tappas/scripts/build\_scripts/clone\_external\_packages.sh\
To change version, use this command from tappas source directory:
```
sed -i 's|v2.9.0 https://github.com/pybind/pybind11.git|v2.10.0 https://github.com/pybind/pybind11.git -b v2.10.0|' scripts/build_scripts/clone_external_packages.sh
```
{% endhint %}


**Install**

```
./install.sh --skip-hailort
```

## Method 2 Docker

**Download TAPPAS container**

* Go to: hailo website → developer zone → software downloads
* Download the Tappas docker container:

Move it to your machine and unzip the file using:

```
unzip tappas_<VERSION>_ubuntu22_docker_x86_64.zip
```

Install and run the image

```
./run_tappas_docker.sh --tappas-image TAPPAS_IMAGE_PATH
```

To resume the image after exiting you can use

```
./run_tappas_docker.sh --resume
```

### Testing using hailortcli benchmark

{% hint style="info" %}
Running hailortcli requires the use of sudo
{% endhint %}


To test we will benchmark the models:

```
cd apps/h8/gstreamer/general/detection/resources
sudo hailortcli benchmark yolov5m_wo_spp_60p.hef
```

After the benchmark will run you will see something like this:

```
root@bedrock:~/tappas/apps/h8/gstreamer/general/detection/resources# hailortcli benchmark yolov5m_wo_spp_60p.hef
Starting Measurements...
Measuring FPS in hw_only mode
Network yolov5m_wo_spp_60p/yolov5m_wo_spp_60p: 100% | 3271 | FPS: 217.97 | ETA: 00:00:00
Measuring FPS and Power in streaming mode
[HailoRT] [warning] Using the overcurrent protection dvm for power measurement will disable the overcurrent protection.
If only taking one measurement, the protection will resume automatically.
If doing continuous measurement, to enable overcurrent protection again you have to stop the power measurement on this dvm.
Network yolov5m_wo_spp_60p/yolov5m_wo_spp_60p: 100% | 3270 | FPS: 217.91 | ETA: 00:00:00
Measuring HW Latency
Network yolov5m_wo_spp_60p/yolov5m_wo_spp_60p: 100% | 972 | HW Latency: 13.13 ms | ETA: 00:00:00

=======
Summary
=======
FPS     (hw_only)                 = 217.973
        (streaming)               = 217.911
Latency (hw)                      = 13.1348 ms
Device 0000:01:00.0:
  Power in streaming mode (average) = 5.22191 W
                          (max)     = 5.25619 W

```

{% hint style="info" %}
Numbers might be somewhat unrealistic since we are running a benchmark in a console environment without actual image processing calculations, hence the high FPS, etc…
{% endhint %}

