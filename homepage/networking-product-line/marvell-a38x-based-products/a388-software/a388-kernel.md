# A388 Kernel

{% hint style="warning" %}
**Please Note**
This article contains outdated information and A388 support is linux kernel mainlined.
{% endhint %}


<a id="description"></a>

#### Description

Official release of the Clearfog board is with Linux kernel 3.10.70 which is supplied by Marvell.

Most of the support for the chip and the platform is already upstreamed mainline and future releases will be based on LTS kernels that are almost identical to the mainline kernel.

The main differences between Marvell kernel and mainline are in the network drivers, noticeably –

- Interrupts spreading to SMP
- RSS support
- Hardware buffer management

As of writing this page, patches to support first item are already queued to LK 4.4, and patches are ready to be submitted for the second and third features.

<a id="build-instructions-mainline-49y"></a>

#### Build Instructions Mainline (>= 4.9.y)

To build the kernel perform the following on a Linux PC –

- git clone –branch linux-4.9.y [https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/linux-stable.git](https://kernel.googlesource.com/pub/scm/linux/kernel/git/stable/linux-stable.git)
- export ARCH=arm CROSS\_COMPILE=<External ARM toolchain prefix>
- make mvebu\_v7\_defconfig
- \# optionally modify the default configuration
- make zImage dtbs modules

{% hint style="warning" %}
The standard configuration is very minimal, you will want to add additional features such as file systems, PCI device drivers and Control-Group support for systemd!
{% endhint %}


<a id="build-instructions-310y-legacy"></a>

#### Build Instructions 3.10.y (Legacy)

To build the kernel perform the following on a Linux PC –

- git clone [https://github.com/SolidRun/linux-armada38x.git](https://github.com/SolidRun/linux-armada38x.git)
- export CROSS\_COMPILE=<External ARM toolchain prefix>
- export ARCH=arm
- make mvebu\_lsp\_defconfig
- \# optionally modify the default configuration
- make zImage dtbs modules

{% hint style="warning" %}
The standard configuration is very minimal, you will want to add additional features such as file systems, PCI device drivers and Control-Group support for systemd!
{% endhint %}


If extended kernel features is requested to be included by the build then you can replace

- make mvebu\_lsp\_defconfig

by

- ./scripts/kconfig/merge\_config.sh -m arch/arm/configs/mvebu\_lsp\_defconfig arch/arm/configs/mvebu\_extra\_defconfig
- make olddefconfig

The merge\_config.sh is a Linux kernel tool that combines different defconfig fragments into a single .config. In this case it combines mvebu\_lsp\_defconfig and mvebu\_extra\_defconfig

<a id="systemd-requirements-debian-fedora-opensuse"></a>

#### systemd requirements (Debian, Fedora, openSUSE, …)

Many recent Linux distributions are using systemd, which requires these additional configuration options:

```
CONFIG_CGROUPS=y
CONFIG_FHANDLE=y
CONFIG_EXPERT=y
CONFIG_EPOLL=y
CONFIG_SIGNALFD=y
CONFIG_TIMERFD=y
CONFIG_NET=y
CONFIG_DEVTMPFS=y
CONFIG_INOTIFY_USER=y
CONFIG_PROC_FS=y
CONFIG_SYSFS=y
```

{% hint style="success" %}
For additional information on systemd requirements, inlcuding where exactly to find these options, see this helpful wiki page of the Gentoo project: [https://wiki.gentoo.org/wiki/Systemd#Kernel](https://wiki.gentoo.org/wiki/Systemd#kernel)
{% endhint %}

