# Yocto for i.MX6

> [!WARNING]
> Documentation for SolidRun Yocto Releases has been moved to the [SolidRun GitHub](https://github.com/SolidRun/meta-solidrun-arm-imx6/tree/develop).

<a id="yocto-for-imx6-31-and-earlier"></a>

# Yocto for i.MX6 (3.1 and earlier)

> [!WARNING]
> The documentation below is covers unmaintained versions of Yocto, please upgrade to 4.0 or later under the link above.

<a id="description"></a>

## Description

he Yocto Project is an open source collaboration project that provides templates, tools and methods to help you create custom Linux-based systems for embedded products regardless of the hardware architecture. It was founded in 2010 as a collaboration among many hardware manufacturers, open-source operating systems vendors, and electronics companies to bring some order to the chaos of embedded Linux development.

<a id="introduction"></a>

## Introduction

<a id="openembedded"></a>

#### **OpenEmbedded**

[OpenEmbedded (OE)](http://www.openembedded.org/) is a framework for cross compilation. It uses the BitBake build tool, and consists of a large number of BitBake scripts, called “recipes”. A recipe describes how a certain package is to be built. Recipe filenames use the .bb extension. Note that OpenEmbedded is not Linux distribution. The names of generated packages usually equal the names of the corresponding recipes, though in some cases, the names may differ.

In the past, OpenEmbedded was a monolithic system. For third parties such as BSP makers it was not straightforward to add OE support for their platforms. Also, other projects which developed recipes had to be merged into OE. For this reason, OE was redesigned to use a layered approach (the old, monolithic OE, is now called “OE classic”). An OE layer contains a set of recipes, machine configurations etc. the union of all layers registered in the local OE installation is the set of all recipes that can be used for building packages. A new layer, called [meta-openembedded](http://cgit.openembedded.org/meta-openembedded/), was also created, to house a vast set of recipes previously contained in the monolithic OE that do not belong in the core.

The fundamental layer is called [openembedded core](http://cgit.openembedded.org/openembedded-core/). Layers are divided into the following types:

- base layer – only two layers qualify: meta-openembedded and openembedded-core
- BSP layer – provides support for platforms and machines
- software layer – adds recipes for software packages
- distribution layer – adds recipes for an OE distribution; distributions contain a set of OE policy definitions as well as some distribution specific recipes, and are often based on OpenEmbedded core (some distributions like Poky in fact contain OpenEmbedded core)
- miscellaneous layer

A complete list of known layers is available at [layers.openembedded.org](http://layers.openembedded.org/) .

A special type of recipe are the “image” recipes. They build an entire root filesystem, and somehow contain it, for example as a tarball, or a SD card image. meta-fsl-arm has hooks that produce images that can be directly copied with the dd tool to SD cards.

<a id="yocto"></a>

#### **Yocto**

For a long time, several projects for embedded development were being carried out without proper inter-project coordination. Distributions moved along at their own pace as well OpenEmbedded itself and BitBake. To introduce better coordination between these projects, the Yocto Project was created. It can be understood as an umbrella project, coordinating and synchronizing the other projects which depend on each other. BitBake and OpenEmbedded are developed to work properly together, are tested together. Distributions are tested to ensure they work well with Yocto etc. Yocto selected one distribution as its “main” one: the distribution called [Poky](http://www.yoctoproject.org/tools-resources/projects/poky). For the remainder of this document, Yocto and Poky are used.

Yocto releases have a name. At time of writing, the current version is 1.6 , called “daisy”. Other layers (especially BSP layers) tend to offer several variants for each release. Since most layers are stored in Git repositories, this translates to one branch per release.

It is also possible to use the current development version of Yocto. This means that master branches of Poky and the layers are used. Note that this is not recommended for production. In this document, daisy is used.

<a id="setting-up-yocto-for-the-cubox-i-hummingboard"></a>

## Setting up Yocto for the CuBox-i/Hummingboard

<a id="hardware-requirements"></a>

#### **Hardware requirements**

Building root filesystems and images with Yocto is very demanding. A quad core processor is strongly recommended. So are at least 8 GB RAM and 50 GB free disk space. Parallelization can quickly require even more RAM; with the right configuration, dozens of compiler instances may run at the same time.

<a id="necessary-layers"></a>

## **Necessary layers**

The CuBox-i uses the Freescale i.MX6 System-on-a-Chip. The BSP layer for this SoC is [meta-fsl-arm](http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/). It is actively maintained, supports several i.MX6 based systems, and contains recipes for Freescale specific software, like the GPU and VPU libraries, u-boot and Linux kernel forks etc. Support for additional platforms is contained in an additional layer, called [meta-solidrun-arm-imx6](https://github.com/SolidRun/meta-solidrun-arm-imx6).

To use Yocto, the minimum set of layers and packages is:

1. Poky Linux
2. meta-fsl-arm
3. meta-solidrun-arm-imx6

<a id="first-setup-steps"></a>

## First setup steps

<a id="first-get-poky"></a>

## First, get Poky:

```
git clone -b fido git://git.yoctoproject.org/poky.git
```

This can take a while.

Afterwards, there will be a “poky” directory, containing several subdirectories: meta, meta-skelenton, meta-yocto etc. as well as several files. Go into this directory. Then get the Freescale layers:

```
cd poky
git clone -b fido git://git.yoctoproject.org/meta-fsl-arm
git clone -b fido git://github.com/SolidRun/meta-solidrun-arm-imx6.git
```

And run:

```
source oe-init-build-env
```

This will create a directory called “build”, set up the environment, and create two configuration files, *conf/local.conf* and *conf/bblayers.conf* .

<a id="editing-localconf"></a>

## Editing local.conf

local.conf is the “local” (= locally for this build) configuration. It contains many options for tweaking OE’s behavior. The most important settings to use/modify are:

```
PARALLEL_MAKE ?= "-j 4"
```

This will pass the parameter in the quotes to the build systems. Most of them understand the “-j” convention, which is how make is instructed to build several source files in parallel. The line above would instruct the build systems to build four source files in parallel. The default sets the number to the number of CPU cores.

```
BB_NUMBER_THREADS ?= "4"
```

Similar to PARALLEL\_MAKE, this option defines how many BitBake tasks can run in parallel. BitBake splits the package building into many tasks. Unpacking is a task. Fetching another etc. As with PARALLEL\_MAKE, the default sets the number to the number of CPU cores.

These two values should be chosen carefully. On systems with less than 8 GB RAM it may be dangerous to set both to 4 or higher. The two numbers should be viewed with a multiplicative relationship: compiling one package is one task, and each compilation task is passed the PARALLEL\_MAKE parameter. In a worst case scenario, BitBake would run four compilation tasks at the same time, and each task would run with -j 4 , thus starting a total of 4\*4 = 16 simultaneously running compiler instances. Broadly speaking, PARALLEL\_MAKE = “-j 4” and BB\_NUMBER\_THREADS = “4” is a good idea when building on a host with 16 GB RAM. For 8 GB hosts should use BB\_NUMBER\_THREADS = “2” instead.

```
MACHINE ??= "qemux86"
```

The machine to build packages for. Machines are specific platforms. For the CuBox-i , the appropiate MACHINE value is “solidrun-imx6”. (choose for the hummingboard “solidrun-imx6” too)

```
DL_DIR ?= "${TOPDIR}/downloads"
```

DL\_DIR defines where downloaded packages and cloned repositories are stored. It is generally a good idea to define one central spot where downloaded packages are to be stored, since OpenEmbedded will not try to download a package if it is already present. Furthermore, when building a root filesystem, many packages could be downloaded. It is recommended to make sure the place DL\_DIR refers to has at least 20 GB of free space. Note that this directory path should be an absolute one.

```
PACKAGE_CLASSES ?= "package_rpm"
```

Built packages are written as either RPM, IPK, of DEB packages. Which one to pick is a matter of taste. For a long time, IPK was the standard.

```
EXTRA_IMAGE_FEATURES = "debug-tweaks"
```

For developer builds it is strongly recommended to add these two values to the string in the quotes: package-management and ssh-server-dropbear. This adds SSH support and the ability to install packages on the target. This is a whitespace separated list. Example: EXTRA\_IMAGE\_FEATURES = “debug-tweaks ssh-server-dropbear package-management”

```
INHERIT += "rm_work"
```

This line is not included in the local.conf that is generated the first time oe-init-build-env is ran, but it is recommended to add it. It ensures that after building a package, all temporary files (including unpacked sources but \*not\* the downloaded tarballs or repositories) are deleted, thus saving a lot of space.

```
ACCEPT_FSL_EULA = "1"
```

meta-fsl-arm requires this setting. With this line, you declare that you have read and accepted the terms of the Freescale EULA. meta-fsl-arm packages will not build without this set.

```
LICENSE_FLAGS_WHITELIST = "commercial"
```

Also a line not present in the generated local.conf , this enables certain restricted recipes, which are subject to licenses and/or royalties. Examples are LAME and mp3 decoder recipes. Note that this should not be used for production unless the legal situation with these restricted recipes is cleared.

<a id="editing-bblayersconf"></a>

## Editing bblayers.conf

bblayers.conf contains a list of layers to use. Only layers mentioned in this list are looked at. The union of these layers makes up the set of available recipes, configurations etc. Note that the order matters; each layer has a defined priority value, and if this value is the same for two or more layers, the order in which they are present in the list decides which layer “wins” in case of conflicts. The paths to the layers \*must\* be absolute.

The default bblayers.conf content looks like this:

```
# LAYER_CONF_VERSION is increased each time build/conf/bblayers.conf
# changes incompatibly
LCONF_VERSION = "6"

BBPATH = "${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \
  /home/test/poky/meta \
  /home/test/poky/meta-yocto \
  /home/test/poky/meta-yocto-bsp \
  "
BBLAYERS_NON_REMOVABLE ?= " \
  /home/test/poky/meta \
  /home/test/poky/meta-yocto \
  "
```

Notice that /home/test/ directory above is an example and should be replaced by the directory on your build machine.

It is recommended to leave these lines in as they are, and just add extra layers. In this case, the meta-fsl-arm and meta-solidrun-arm-imx6 recipes are added like this (don’t forget the trailing backslash!):

```
# LAYER_CONF_VERSION is increased each time build/conf/bblayers.conf
# changes incompatibly
LCONF_VERSION = "6"

BBPATH = "${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \
  /home/test/poky/meta \
  /home/test/poky/meta-fsl-arm \
  /home/test/poky/meta-solidrun-arm-imx6 \
  /home/test/poky/meta-yocto \
  /home/test/poky/meta-yocto-bsp \
  "
BBLAYERS_NON_REMOVABLE ?= " \
  /home/test/poky/meta \
  /home/test/poky/meta-yocto \
  "
```

meta contains openembedded core, and it is generally a good idea to make sure it always has priority. meta-yocto and meta-yocto-bsp contain Yocto specific recipes that may need to be overriden by BSP specific recipes, so they are placed behind the Freescale layers.

This concludes the setup steps. For more in-depth information about the OE details, consulting the [Yocto Project manual](http://www.yoctoproject.org/docs/current/ref-manual/ref-manual.html) is recommended.

<a id="customizing-images"></a>

## Customizing images

As mentioned before, image recipes – or just “images” – assemble a set of packages, and create a root filesystem out of them that can be used with the target machine. There are two ways to define what is contained in an image:

1. Define a new image recipe. This is the “clean” solution, and the one that should be used for production. How to write an image recipe is described in the Yocto Project manual.
2. Set the IMAGE\_INSTALL\_append variable in local.conf . This is more useful during development. It is a whitespace-separated list containing package names (not recipe names!)

For example, to make sure “strace” is added to generated images, it is possible to add this line to local.conf:

```
IMAGE_INSTALL_append = "strace"
```

<a id="building-packages"></a>

## Building packages

Before a package can be built, the environment must be set up with the oe-init-build-env script. If not already done, run:

```
source oe-init-build-env
```

this must be called every time a shell is opened for building. (For longer builds, it is recommended to first start a GNU screen session, and run the source line above in there, as well as bitbake itself.)

After the environment has been set up, bitbake can be called. The syntax is simple: bitbake <recipe name>. Example:

```
nice bitbake strace
```

This downloads the strace tarball (if not already downloaded), unpacks it, builds the package, and stores the result in an RPM,IPK, or DEB file (depending on the value of PACKAGE\_CLASSES in local.conf). It also builds any other recipes the specified recipe depends on. (It is a good idea to call bitbake with nice, to make the host more responsive while building.)

Note that OE builds everything, including the cross compiler. (There are ways to use an external cross compilation toolchain, but this goes beyond the scope of this document.) Building can take a long time, depending on how many sources were downloaded and how many packages were built already.

There are several predefined images that can be used as starting points. Examples are: core-image-base, core-image-x11, core-image-sato . BSP layers sometimes also contain image recipes. For a quick start, build core-image-x11:

```
nice bitbake core-image-x11
```

For building gstreamer-1.0 packages with gst-1.0 imx acceleration run:

```
bitbake gstreamer1.0 gstreamer1.0-plugins-base-meta gstreamer1.0-plugins-good-meta gstreamer1.0-plugins-bad-meta gstreamer1.0-plugins-ugly-meta gstreamer1.0-libav gstreamer1.0-plugins-imx
```

<a id="installing-images"></a>

## Installing images

The hooks introduced by meta-fsl-arm make this step easy. Assuming the core-image-x11 was built, a .sdcard file will be generated, and stored at: build/tmp/deploy/images/cubox-i/core-image-x11-cubox-i.sdcard (this is usually a symlink; the actual file has a longer name containing timestamps etc.)

To run the image with the CuBox-i , a MicroSD card is required. Insert the SD card, but do not mount it. Check what the device name of the card is (the entire card, not just a partition). If for example the device name is /dev/sdg (again: sdg, not sdg1 or sdg2 etc.), dd is called this way:

```
dd if=build/tmp/deploy/images/cubox-i/core-image-cubox-i-x11.sdcard of=/dev/sdg bs=4M conv=fsync
```

**Warning: All contents on the MicroSD card will be gone, including the partition table. Be absolutely sure the device name is correct, otherwise you may destroy the data on a local volume, like the host’s system hard disk! This cannot be undone! dd will not emit any warnings!**

It may be necessary to run dd with root privileges. “sudo dd” is usually enough.

Once the dd call completes, the SD card can be removed, and inserted into the CuBox-i . After plugging in the power supply, the system should start.

<a id="adding-gpu-support"></a>

## Adding GPU Support

Following code must be added to the local.conf

```
DISTRO_FEATURES_append += "x11 opengl"
```

<a id="web-browser-support"></a>

## Web Browser Support

**For adding a browser to Yocto, please have a look at WPE Webkit**

<a id="kodi-specific-notes"></a>

## Kodi specific notes

<a id="installation"></a>

#### **Installation**

Installation is done on a computer, not on the CuBox-i. Make sure the SD card is mounted.

1. Download the script from first post in the forum thread.
2. Run the script with the SD card as an argument, e.g.

```
./mk_xbmc_hb.sh /dev/mmcblk0
```

This will guide you through the installation process. Choose the correct version of the CuBox-i, and the desired resolution. The script will download the distribution, format the SD card, and perform the installation.

<a id="external-links"></a>

#### External links

- [http://yoctoproject.org](http://yoctoproject.org)
- OpenEmbedded (OE)
- meta-openembedded
- openembedded core
- [http://layers.openembedded.org](http://layers.openembedded.org)
- Poky
- meta-fsl-arm
- meta-solidrun-arm-imx6
- Yocto Project manual