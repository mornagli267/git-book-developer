# i.MX6 Archlinux

<a id="description"></a>

## Description

This page is aimed at guiding you through a quick and simple installation of ArchLinux on you HummingBoard/Cubox-i. The result is a minimal installation with a very fast boot time (about 12 seconds to desktop on the HummingBoard, single core). The preparation of the SD card requires an existing linux box. However, once the SD card is ready, your Cubox-i does not need to be connected to a mouse, monitor or keyboard to complete the installation.

<a id="installation"></a>

## Installation

<a id="manual-installation"></a>

#### **Manual installation**

This installation method produces a SD card with the official ArchLinuxARM installation. The only difference is the use of a script to prepare the SD card. It simply performs all the steps described on the ArchLinuxARM pages for you.

1. Download the official ArchLinux rootfs
2. Downloadthe installation script (a slightly modified GeexBox script) \[2\]
3. Insert your SD card in your linux box, check (using dmesg) the name of the device (something like /dev/sdX) and run the following as root

```
chmod +x make-sdcard
./make-sdcard /dev/sdX ArchLinuxARM-imx6-cubox-latest.tar.gz
```

<a id="examples"></a>

#### **Examples:**

```
./make-sdcard /dev/mmcblk0 ArchLinuxARM-imx6-cubox-latest.tar.gz
./make-sdcard /dev/sdd ArchLinuxARM-imx6-cubox-latest.tar.gz
```

<a id="post-installation"></a>

#### Post Installation

Now you should have a SD card with a (very) basic ArchLinux. Insert it into your Cubox-i (connected to wired ethernet) and boot into ArchLinux, then login as root (password root) and run this to update

```
pacman -Syu
```

This will synchronize the package databases, upgrade to most recent packages.

<a id="installing-kodi-xbmc"></a>

#### Installing Kodi/xbmc

To install Kodi/xbmc:

```
pacman -S xbmc-imx-git
```

To run

```
systemctl start xbmc
```

Do not run xbmc within X

<a id="creating-a-desktop-environment"></a>

## Creating A Desktop Environment

To install an X environment (eg lxde)

```
pacman -S lxde xf86-video-fbdev xorg-xinit gpu-viv-bin-mx6q-fb
```

You will need a symlink

```
ln -sf /opt/fsl/lib/libGL.so /usr/lib/libGL.so.1
```

Add a user, running X is bad as root, this will create a user called alarm

```
groupadd alarm
useradd -m -d /home/alarm -g alarm alarm
usermod -a -G alarm,audio,video,power,network,optical,storage,disk alarm
passwd alarm
#you will be asked to choose a password
```

Add this to bottom of /home/alarm/.xinitrc

```
exec dbus-launch startlxde
```

You could now start lxde logged in as alarm by running

```
startx
```

<a id="make-logging-in-as-user-alarm-launch-lxde-automatically"></a>

#### Make logging in as user alarm launch lxde automatically

Add this to bottom of */home/alarm/.bash\_profile*

```
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx
```

To automatically go straight into lxde, logged in as alarm, from boot

```
mkdir /etc/systemd/system/getty@tty1.service.d
```

Now create this file

```
nano /etc/systemd/system/getty@tty1.service.d/autologin.conf
```

and paste these contents in

```
[Service]
ExecStart=
ExecStart=-/usr/bin/agetty --autologin alarm --noclear %I 38400 Linux
```

<a id="make-hdmi-default-sound-source-for-alsa"></a>

#### Make hdmi default sound source for alsa

Paste this into either /etc/asound.conf (affects all users) or ~/.asoundrc of the user

```
pcm.!default {
  type plug
  slave {
    pcm "hw:1,0"
  }
}
ctl.!default {
  type hw
  card 1
}
```

Complete the setup of the system by following the Archlinux wiki pages. You can start [here](https://wiki.archlinux.org/index.php/Beginners%27_Guide#post-installation).

<a id="installing-wifi-drivers"></a>

## **Installing WIFI drivers**

In order to install binary firmware for wireless network cards with the Broadcom BCM4313, BCM43224 or BCM43225 chip on ArchLinux run the following as root

```
pacman -Sy firmware-brcm43xx  wpa_actiond dialog
```

This will install bluetooth firmware and also 2 files, needed by wifi firmware

After installing the config files, you will need to reboot device or reload module and then you can configure wifi access with command

```
wifi-menu
```

To start on boot

```
systemctl enable netctl-auto@wlan0
```

<a id="alternative-installation-methods"></a>

## Alternative Installation Methods

Other options to get ArchLinux installed on your SD card:

- Official ArchLinux [installation instructions](http://archlinuxarm.org/platforms/armv7/freescale/cubox-i#qt-platform_tabs-ui-tabs2)