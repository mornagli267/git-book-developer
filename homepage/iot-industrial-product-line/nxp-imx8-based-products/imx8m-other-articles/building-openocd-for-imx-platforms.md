# Building OpenOCD for i.MX Platforms

<a id="compiling-openocd-for-solidrun-imx-based-products"></a>

### Compiling OpenOCD For SolidRun iMX\* Based Products

The purpose of this document is to cover compiling OpenOCD directly on the developer board specifically for using OpenOCD to flash connected devices via the imx\_gpio interface. We will use Debian as the base for the instructions, however the general procedure should work with slight modification on most distributions. Cross-compiling is possible but is currently not in the scope of this document.

<a id="prepare-debian-for-compiling"></a>

### Prepare Debian for compiling

Start by making sure Debian is updated to the latest version.

Next, run the following command to install all the tools needed to build OpenOCD from source

```
sudo apt install build-essential git autoconf libtool make pkg-config libusb-1.0-0 libusb-1.0-0-dev
```

<a id="get-the-source-and-compile-openocd"></a>

### Get the Source and Compile OpenOCD

Once that has finished clone the SolidRun github repository, as it has patches to mainline OpenOCD specifically for the new iMX8M AARCH64 architecture. Then bootstrap, configure and build the source.

```
git clone https://github.com/SolidRun/openocd.git
cd openocd
./bootstrap
./configure --prefix=/usr --sysconfdir=/etc --enable-imx_gpio --enable-sysfsgpio --disable-stlink --disable-ti-icdi --disable-ulink --disable-usb-blaster-2 --disable-vsllink --disable-xds110 --disable-osbdm --disable-opendous --disable-aice --disable-usbprog --disable-rlink --disable-armjtagew --disable-cmsis-dap --disable-kitprog --disable-usb-blaster --disable-presto --disable-openjtag --disable-jlink
make
```

This configures and builds OpenOCD for a very limited purpose built build mainly targeted at using the imx\_gpio interface.

Finally install the source

```
sudo make install
```

Great now OpenOCD is ready to use.