# Serial-Console USB->UART

Our IMX6 Products have the ability to boot a system with a dumb terminal on a serial port as a console. This configuration is useful for developers who want to debug the kernel or device drivers.

The UART is 3.3V, so the USB→UART cable needs to be compatible with 3.3V, not 5V. Adapter cable only needed with HummingBoard.&#x20;

CuBox-i1 and CuBox-i2 do not have serial port support, CuBox-i2exW, Cubox-i2ex and CubBox-i4Pro come with a FTDI FT230X adapter, vendor ID = 1027 (0x403), productID = 24597 (0x6015).

Using a microUSB cable, it is possible to make serial connection. With a serial connection, the [i.MX6 U-Boot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179374)  command can be changed. It is also possible to log into a Linux environment using terminal emulation.

The serial connection is based on a self powered USB with FTDI. Connect the microUSB cable to a computer, set-up the serial connection, and power-on the CuBox-i. The default configuration is 115200 bps, 8bits, no-stop bit and any flow control disabled.

### Enabling serial console in U-Boot

Before making a serial connection, output to the serial console must be enabled in [i.MX6 U-Boot](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179374) . The following arguments must be passed to U-Boot to enable the serial console:

```
console=ttymxc0,115200n8
```

### Making a connection

With the power cable to the CuBox-i not connected, plug-in the microUSB cable. Now start the application of your choice. It will make a connection, even if the CuBox-i is not yet powered on. Once you connect the power to the CuBox-i, output will be shown.

### Drivers

Drivers can be downloaded from [FTDI](http://www.ftdichip.com/Drivers/VCP.htm).

### Linux

Once you connect the microUSB cable, the kernel should load the usbserial module.

```
dmesg | grep ttyUSB
```

The above command prints the name of the device, usually _/dev/ttyUSB0_, if it is the first of this type. Connect to the CuBox-i using a terminal application of choice.

**Screen**

```
screen /dev/ttyUSB0 115200
```

**Putty**

```
putty -serial -sercfg 115200,8,n,1 /dev/ttyUSB0
```

You can download PuTTY [here](http://www.putty.org/).

**Minicom**

```
minicom -s
```

Choose ‘Serial port setup’

* Click A, and fill in serial device – for example /dev/ttyUSB0
* Click E, and choose 115200 8N1 by click E,Q, then enter
* Click F to disable Hardware Flow Control
* If needed, click G to disable Software Flow Control, then enter
* Select ‘Save setup as dfl’. Next time you run minicom without the ‘-s’ flag, the saved parameters will be used
* Press exit, leaving configuration and enter console

### OSX

First, download and install the [FTDI VCP drivers](http://www.ftdichip.com/Drivers/VCP.htm)

Once you connect the cable, the kernel should load the usbserial module. Look for the device.

```
ls -l /dev/*usbserial*
```

**Screen**

OS X ships with screen by default. Open a terminal and type

```
screen /dev/tty.usbserial-DB008OZL 115200
```

**ZTerm**

You can also download [ZTerm](http://www.macupdate.com/app/mac/6888/zterm-x).

```
Open Settings, Connection and set the values to 115200 8 N 1 (uncheck Local Echo).
Open File, Transfer Convert and set Binary Data.
```

### Windows

First, download and install the [FTDI VCP drivers](http://www.ftdichip.com/Drivers/VCP.htm)

**PuTTY**

1. Download, install, and launch
2. In the main screen, select the radio button Serial for Connection type
3. Change Speed to 115200
4. If you connect the cable, and the correct driver is installed, a popup balloon will display the COM port CuBox is connected to. If no popup is displayed, just try the different COM ports, starting at COM1.
5. Try to connect by pressing Open
6. If nothing happens, change the Serial line to the next COM port (e.g. COM2) until it connects.
7. Once you know the correct port, save the session. Later open a connection by double-clicking on the session name.

**TeraTerm**

1. Download, install, and launch
2. On the initial screen, select the Serial option. Select the COM port the cubox is connected to. Press OK
3. Using the top menu, select Setup → Serial port…
4. Configure the baud rate to be 115200. Press OK
