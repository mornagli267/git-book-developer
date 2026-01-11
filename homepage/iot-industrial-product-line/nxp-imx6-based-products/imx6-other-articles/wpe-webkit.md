# WPE Webkit

WebKit is a cross-platform web browser engine.

<a id="description"></a>

### Description

This is a quick step by step guide for building wpe-webkit with yocto. It takes a few shortcuts here and there and is meant to serve as an example of how yocto can be used for a specific piece of software.

<a id="preparation"></a>

### Preparation

As of August 29 2018 30GB of disk space were used by the build tree and all source files. So this is the minimum of free space to go with! There are also quite a few build dependencies required such as a c compiler, and several tools. Yocto will list those requirements in the build step when they are missing. It is advised to use a dedicated folder for working on this, especially to clone all the repositories to!

<a id="download"></a>

### Download

```
git clone --branch master git://git.openembedded.org/bitbake
git clone --branch sumo git://git.openembedded.org/openembedded-core
git clone --branch sumo git://git.yoctoproject.org/meta-freescale
git clone --branch sumo https://github.com/SolidRun/meta-solidrun-arm-imx6.git
git clone --branch sumo git://git.yoctoproject.org/poky
git clone --branch sumo https://github.com/Freescale/meta-freescale-distro.git
git clone --branch master https://github.com/Igalia/meta-webkit.git
```

> [!INFO]
> This list refers to a fork of meta-solidrun-arm-imx6 adding support for the sumo release. Double-Check if upstream [meta-solidrun-arm-imx6](https://github.com/SolidRun/meta-solidrun-arm-imx6.git) has meanwhile added a sumo branch!

<a id="configure"></a>

### Configure

<a id="create-build-directory-in-current-folder"></a>

#### create build directory in current folder

```
source ./openembedded-core/oe-init-build-env
```

<a id="list-all-required-meta-layers-in-conf-bblayersconf"></a>

#### List all required meta layers in conf/bblayers.conf:

```
BBLAYERS ?= " \
  /opt/workspace/SolidRun/yocto/openembedded-core/meta \
  /opt/workspace/SolidRun/yocto/meta-freescale \
  /opt/workspace/SolidRun/yocto/meta-solidrun-arm-imx6 \
  /opt/workspace/SolidRun/yocto/poky/meta-poky \
  /opt/workspace/SolidRun/yocto/meta-freescale-distro \
  /opt/workspace/SolidRun/yocto/meta-webkit \
  "
```

<a id="select-target-machine-and-features-in-conf-localconf-by-appending-at-the-end"></a>

#### Select target machine and features in conf/local.conf (by appending at the end):

```
# target SolidRun i.MX6 based on the Freescale Wayland Distro
MACHINE = "solidrun-imx6"
DISTRO = "fslc-wayland"

# include wpewebkit in images
IMAGE_INSTALL_append = " gstreamer1.0-plugins-imx gstreamer1.0-plugins-imx-meta"
IMAGE_INSTALL_append = " wpewebkit cog"

# use rdk backend on wayland
PREFERRED_PROVIDER_virtual/wpebackend = "wpebackend-rdk"
PACKAGECONFIG_pn-wpebackend-rdk = "wayland"

# accept meta-freescale/EULA
ACCEPT_FSL_EULA = "1"
```

<a id="build"></a>

### Build

```
bitbake core-image-weston
```

<a id="deploy"></a>

### Deploy

```
gzip -cd tmp/deploy/images/solidrun-imx6/core-image-weston-solidrun-imx6.wic.gz | sudo tee /dev/sdX >/dev/null
```

<a id="run"></a>

### Run

From a terminal, or the serial console:

```
ifup eth0

export WPE_INIT_VIEW_WIDTH=1920
export WPE_INIT_VIEW_HEIGHT=1080
cog http://www.solid-run.com/
```

<a id="references"></a>

### References

- [Yocto for i.MX6](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287277558)
- [https://github.com/Igalia/meta-webkit/wiki](https://github.com/Igalia/meta-webkit/wiki)