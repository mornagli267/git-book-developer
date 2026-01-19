# SolidSense OEM software image

## SolidSense OEM software image

{% hint style="warning" %}
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.\
[Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.
{% endhint %}


## Introduction

The SolidSense OEM software image is the easiest solution to start a development on the SolidSense hardware. This is allowing to freely use all Debian Linux resources. The image comes with all SolidSense interfaces declared in the device tree as well all associated drivers.

The resulting development can then be directly used or re-package to run on top of the SolidSense IoT production platform that is providing key production features like read-only rootfs for safety and remote software management.

### Installation

**Step-By-Step**

* Download the image and flash on a USB stick with a tool like Etcher.

[https://images.solidsense.io/SolidSense/SolidSense-OEM-debian-buster.img.xz](https://images.solidsense.io/SolidSense/SolidSense-OEM-debian-buster.img.xz)

* Open the top cover of your device by removing the 6 x screws.
* Connect a TTL UART cable and open a serial connection console. You can refer to [serial connection](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287801409) for installing the necessary serial connection software.
* Stop booting in U-Boot and run the commands below - only at the first boot :

`setenv bootcmd "env run findfdt; usb start; ls usb 0:1; run bootcmd_usb0; run bootcmd_mmc0; $bootcmd"; saveenv; boot`

{% hint style="info" %}
You can always run `env default -a -f; saveenv; reset` to recover the default status.
{% endhint %}


{% hint style="info" %}
**Please Note:** The boot priority is:
1. &#x20;USB (if any compatible image is found)
2. &#x20;SD (if any compatible image is found)
3. &#x20;emmc (booting the default Solidsense SW)
{% endhint %}


Then you’ll see the following:

![](../../../../.gitbook/assets/image-20220405-215122.png)

* In order to be able to log in, please insert `solidsense` as a username and password as follows:

![](../../../../.gitbook/assets/image-20220405-215636.png)
