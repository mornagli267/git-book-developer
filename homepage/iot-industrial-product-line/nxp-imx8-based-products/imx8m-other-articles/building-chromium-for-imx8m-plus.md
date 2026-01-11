# Building Chromium for i.MX8M Plus

In order to compile an i.MX8M Plus image with chromium, please follow these steps. Please notice that building Yocto takes around **300GByte of disk storage and requires 64GByte system memory** or 32GByte with a tweak to build first rust-native as described below.

> [!INFO]
> These steps were tested on a Ubuntu 22.04 build machine.

<a id="install-required-packages"></a>

#### Install required packages

```
sudo apt install flex bison gperf build-essential zlib1g-dev lib32ncurses5-dev \
x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev tofrodos libxml2-utils \
openssh-server openssh-client uuid uuid-dev zlib1g-dev liblz-dev lzop liblzo2-2 \
liblzo2-dev git-core curl python3 python3-pip python3-pexpect python3-git \
python3-jinja2 u-boot-tools mtd-utils openjdk-8-jdk device-tree-compiler aptitude \
libcurl4-openssl-dev nss-updatedb chrpath texinfo gawk cpio diffstat \
libncursesw5-dev libssl-dev libegl1-mesa net-tools libsdl1.2-dev xterm socat \
icedtea-netx-common icedtea-netx python3-markdown android-sdk-libsparse-utils \
xsltproc gcc-multilib g++-multilib subversion libc++-dev libstdc++6 \
libstdc++-12-dev python-is-python3 lz4;

pip3 install pylint
```

<a id="building-from-sources"></a>

#### Building from sources

- Make sure your git username and email is configured; and then clone the ‘repo’ tool and initialize the sources tree -

```
mkdir imx-yocto
cd imx-yocto
wget https://storage.googleapis.com/git-repo-downloads/repo
chmod +x repo
./repo init -u https://github.com/SolidRun/meta-solidrun-arm-imx8 -b kirkstone-imx8m -m sr-imx-5.15.71-2.2.0.xml
./repo sync
DISTRO=fsl-imx-xwayland MACHINE=imx8mpsolidrun EULA=1 source imx-setup-release.sh -b build-xwayland-imx8mpsolidrun
```

- Accept the EULA license agreement by
- Now edit the file **conf/bblayers.conf** and append the following to the end -

```
BBLAYERS += "${BSPDIR}/sources/meta-solidrun-arm-imx8"
```

- edit the file **conf/local.conf** and append to it Chromium sources and NXP new github repo sources -

```
CORE_IMAGE_EXTRA_INSTALL += "chromium-ozone-wayland"
MIRRORS += " \
    git://source.codeaurora.org/external/imx/ git://github.com/nxp-imx/;protocol=https \n \
    https://source.codeaurora.org/external/imx/ https://github.com/nxp-imx/ \n \
    http://source.codeaurora.org/external/imx/ http://github.com/nxp-imx/ \n \
    gitsm://source.codeaurora.org/external/imx/ gitsm://github.com/nxp-imx/;protocol=https \n \
"
BB_NUMBER_THREADS = "4"
```

First build rust-native and then imx-image-full. The reason that rust-native is built first since it might fail on systems with less than 64GByte system memory.

If your machine does have available 64GByte system memory you can skip building rust-native and go ahead built imx-image-full directly.

```
bitbake -C compile rust-native
bitbake imx-image-full
```

<a id="using-chromium"></a>

#### Using Chromium

Once the image was compiled and deployed, you can start the browser simply by running:

```
chromium --no-sandbox
```