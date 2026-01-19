# Flashing an SD Card

<a id="description"></a>

## Description

There are many distributions for CuBox-i & Hummingboard. Before a distribution can be used, it must be flashed to an SD card. How this works depends on your operating system. Below are general instructions for flashing an image to an SD card. A distribution might have specific instructions, or a script that will do all these steps for you. As a general rule, it is easiest to flash a distributions on a Linux PC, especially if more advanced configuration is needed. However, you can use Windows or OS X as well. Many distributions are available as an .img.xz file. This .img extension indicates that this is a full disk image. The .xz extension indicates that the file is compressed using xz. There is no need to format the SD card before you begin. It is also not needed to create any partitions manually.

{% hint style="warning" %}
**Flashing an image will erase all files and partitions of the target device. Make sure you choose the SD card as the target device, or you can seriously damage your existing operating system.**
{% endhint %}


You do not need to format the SD card before use. Images fully overwrite the card’s contents, including the boot loader and the partition table.

<a id="windows"></a>

## Windows

<a id="flash-the-img-file"></a>

#### Flash the .img file

**Short verions:**

Download the operation system/image file. extract it with [7zip](http://www.7-zip.org/). use [win32diskimager](http://sourceforge.net/projects/win32diskimager/) to flash the .img file onto your sd card.

**Long version:**

Windows does not include any program by default to extract the compressed file or flash images to an SD card. Some extra tools must be installed first.

First, the file needs to be extracted. [7zip](http://www.7-zip.org/) is a good program to extract files in Windows. After the program is installed, start 7-Zip File Manager. Browse to the .img.xz file. 7-Zip File Manager can open the file and display its content. There will be just one file with the extension .img. Click on the button Extract and select a location where you want to extract the file.

To connect the micro SD card, use an SD card adapter and insert it in the SD card reader. Or use an USB converter. If there is already a Linux distribution on the SD card, Windows might not be able to read the SD card. Windows will display a message that the drive must be formatted first. You can ignore this message safely. The card will be formatted once it will be flashed.

Open [Win32 Diskimager](http://sourceforge.net/projects/win32diskimager/). Click the Browse button and select the .img file. Select the drive letter of the SD card. **Make sure you select the correct drive, because all content on the drive will be erased!** Click Write to flash the distribution to the SD card.

<a id="extend-image-size-to-whole-sd-card"></a>

#### Extend image size to whole SD card

- Download [GParted LIVE CD](http://gparted.org/livecd.php)
- Download and install [VirtualBox](https://www.virtualbox.org/)
- Insert SD card with flashed image
- Find DeviceID of your SD card reader

```
C:\Users\>wmic diskdrive list brief
Caption                      DeviceID            Model                        Partitions  Size
WDC WD7500BPKT-75PK4T0       \\.\PHYSICALDRIVE0  WDC WD7500BPKT-75PK4T0       3           750153761280
O2Micro SD SCSI Disk Device  \\.\PHYSICALDRIVE1  O2Micro SD SCSI Disk Device  1           3964584960
```

- Create .vmdk file (will be used as disk in VirtualBox)

```
C:\Program Files\Oracle\VirtualBox\VBoxManage internalcommands createrawvmdk -filename "%HOMEPATH%/Desktop/sdcard.vmdk" -rawdisk "\\.\PHYSICALDRIVE1"
```

- Configure VirtualBox to use GParted and sdcard.vmdk file (located at desktop)
- Boot the VirtualBox and edit partitions on SD Card

Note: original blogpost [here](http://www.sandyscott.net/2013/08/14/virtualbox-direct-drive-access/)

Refer [here](http://forum.solid-run.com/your-first-steps-beginners-corner-f17/gparted-and-flashing-an-image-to-sd-t1223.html) for a worked example posted on the forum.

<a id="mac-osx"></a>

## Mac OSX

<a id="flash-the-img-file"></a>

#### Flash the .img file

**Update:** You can use the [OSX DD Tool](https://www.thefanclub.co.za/how-to/dd-utility-write-and-backup-operating-system-img-files-memory-card-mac-os-x) to flash .img files onto your sd card:

OS X includes the program to flash the image to an SD card, but not the program to extract the .xz file. Flashing must be done using command line tools.

To extract the .xz file, install [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver). This can be installed directly from the App Store, or can be downloaded from the site and installed manually. Open The Unarchiver from Launchpad. A preference window will open, but that can be ignored. On the menu bar, click File > Unarchive to Current Folder. Select the .img.xz file and press Unarchive. The file will now be extracted to the same folder as the .img.xz file.

You can also install a command line program to handle .xz compressed files. See the [XZ home page](http://tukaani.org/xz/) which points you to the [Mac OS X Packages sourceforge](http://macpkg.sourceforge.net/) project. It’s an unsigned package, so you’ll need to right-click and select Open rather than just double-click. If you have the XCode compiler tools installed you can also compile it yourself from source.

Next, start the Terminal app. Open Launchpad, click on the Other folder, and select Terminal (or simply type Terminal in the search box). Now, go to the folder where the distribution is extracted. If you downloaded it using your browser, this will most likely be the downloads folder. **On the terminal and type:**

```
cd Downloads
```

**and press enter. Now type**

```
ls -lh *.img
```

**and press enter. The output will look like**

```
-rw-r--r--@ 1 user  staff   2.0G Jan 25 15:33 <image name>.img
```

The 2.0G part is the size of the file. This is also the minimal size of the SD card you need. It is not a problem if the SD card is larger. Connect the SD card. Use a microSD to SD card adapter and insert the SD card in the SD slot. Or use a microSD to USB converter. If the content can be read, a new icon for the SD card will appear on the desktop (or multiple icons if there are multiple partitions on the card). However, this is the mount point of the SD card. To flash the image you need the device name of the SD card. Note the name of the icon on the desktop. On the terminal type

```
mount
```

**and press enter. Most likely, the last line will look something like**

```
/dev/disk2s1 on /Volumes/SYSTEM (msdos, local, nodev, nosuid, noowners)
```

The part behind /Volumes should be the same name as the icon on the desktop. Note the name of the SD card at the beginning of the line (/dev/disk2s1). In this case, it means the first partition of the second disk. Thus, the device name is /dev/disk2. Unmount the existing partitions. **On the terminal, type** (change the device name to the correct one)

```
sudo diskutil unmountDisk /dev/disk2*
```

and press enter. Now type your OS X password. The icon(s) will now disappear from the desktop. Now the image can be flashed to the SD card. It should be flashed to the whole SD card, not to a partition. If, in the previous step the mount point was /dev/disk2s1, you need to flash it to /dev/rdisk2 (without the s1 and with an r in front, so it will use the much faster raw mode). **On the terminal, type** (change the device name to the correct one)

```
sudo dd if=<image name>.img of=/dev/rdisk2 bs=4096
```

and wait! Before you press enter, double check that the device name is correct. An incorrect device could erase everything on your hard disk. Press enter if everything correct. There will be no visual confirmation that anything is going on, but you can press Ctrl+T to send SIGINFO to the dd process and it will output its progress. Depending on the write speed of the SD card, and the size of the image, it can take a long time. Once the flash is complete, a new icon will appear automatically on the desktop. Make sure to properly eject the image before removing the SD card.

<a id="extend-image-size-to-whole-sd-card"></a>

#### Extend image size to whole SD card

Use Virtualbox on MacOSX with Gparted Image.

<a id="linux"></a>

## Linux

All Linux distributions include all the program to extract and flash the image to an SD card. Everything will be done from the command line. Starting a command line (also called terminal) depends on the desktop environment you use (or, if you don’t use a desktop environment, you are already at the command line.)

Go the the folder where the file .img.xz file is downloaded. If this is the downloads folder, type

```
cd downloads
```

and press enter. To extract the .xz file, run

```
xz -d <image name>.img.xz
```

if it does not work please install the unxz program and run

```
unxz <image name>.img.xz
```

to decompress it. The image will now be extracted. Now type

```
ls -lh *.img
```

and press enter. The output will look like

```
-rw-r--r-- 1 user  group   2.0G Jan 25 15:33 <image name>.img
```

The 2.0G part is the size of the file. This is also the minimal size of the SD card you need. It is not a problem if the SD card is larger. Connect the SD card. Use a microSD to SD card adapter and insert the SD card in the SD slot. Or use a microSD to USB converter. Depending on the distribution, the SD card might be mounted automatically. Before it can be flashed, it must be unmounted. Type

```
mount
```

and press enter to check if the SD card is mounted. It can appear as /dev/mmcblk0p1 or /dev/sdb1 or similar. If partitions are mounted, unmount them first. Type

```
umount <mount point>
```

and press enter. If you get a message about permissions, type the same command preceded by sudo and press enter. You must type your password to give permission to execute the command. Now the image can be flashed to the SD card. It should be flashed to the whole SD card, not to a partition. If, in the previous step the mount point was /dev/sdb1, you need to flash it to /dev/sdb (without the 1). On the terminal, type (change the device name to the correct one, for example /dev/mmcblk0 or /dev/sdb)

```
dd bs=4k conv=fsync if=<image name>.img of=/dev/sdb
```

and wait. Before you press enter, double check that the device is correct. An incorrect device could erase everything on your hard disk. Press enter if everything is correct. If the previous command required sudo, also precede this command with sudo. There will be no visual confirmation that anything is going on. Depending on the write speed of the SD card, and the size of the image, it can take a long time.

<a id="extend-image-size-to-whole-sd-card"></a>

#### Extend image size to whole SD card

Command line steps can be found on [How To Forge](http://www.howtoforge.com/linux_resizing_ext3_partitions_p2) For a much simplier method is to use [GParted](http://gparted.org/). It can be downloaded in Ubuntu/Debian with the following command sudo apt-get install gparted

- Insert SD Card into your Linux based PC
- Start GParted
- Select the SD Card from the drop down in the upper right
- If the partition is mounted you will need to Unmount it under the partition menu
- Choose Partition→Resize/Move
- Fill out the requested information and click Resize/Move button
- Click the green Apply checkbox
- Screenshots and steps can be found on How To Forge