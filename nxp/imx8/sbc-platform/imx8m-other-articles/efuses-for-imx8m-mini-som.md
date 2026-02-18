# eFuses for i.MX8M Mini SOM

The intention of this page is to provide developers the utilities to boot SolidRun based i.MX8M mini boards (by default HummingBoard Pulse) that can boot from Micro SD and eMMC.

In this tutorial you will learn how to boot a standalone minimal kernel with buildroot based image.

Once the prompt is there you can blow fuses, download files (wget) and perform other tasks for the sake of evaluating the boot process.

<a id="setting-up-the-environment"></a>

#### Setting up the environment

1. HummingBoard Pulse + IMX8M mini.
2. PC that runs Linux
3. Terminal emulation (putty, minicom etc..) that are connected to HummingBoard Pulse serial terminal 115200bps 8N1 via USB to microusb cable.
4. Download and build buildroot image for IMX8M mini and flashing it to SD card.

<a id="booting-through-usb-otg"></a>

#### Booting through USB OTG

Clone the following git repository: [https://github.com/SolidRun/imx8mm\_build.git](https://github.com/SolidRun/imx8mm_build.git)

Run the “runme.sh” script to start the build, the output is presented in the “Image” directory as “microsd.img”, Flash the “microsd.img” to SD card and insert it into the hummingboard pulse.

<a id="blowing-fuses-to-program-the-unit-mac-address"></a>

#### Blowing fuses to program the unit MAC address

{% hint style="warning" %}
**Blowing fuses is an irreversible act. If you set a bit from ‘0’ to ‘1’ you can not set it back to ‘0’.**
{% endhint %}


echo <high 16 bit of the MAC address> > /sys/fsl\_otp/HW\_OCOTP\_MAC\_ADDR1

echo <lower 32bit of the MAC address> > /sys/fsl\_otp/HW\_OCOTP\_MAC\_ADDR0

**For example –** use the following command in order to fuse “d0:63:12:34:56:78” MAC address

**In Linux:**

```
echo 0xd063 > /sys/fsl_otp/HW_OCOTP_MAC_ADDR1
echo 0x12345678 > /sys/fsl_otp/HW_OCOTP_MAC_ADDR0
```

**In order to blow high 16 bit of MAC address in u-boot; run –**

```
fuse prog -y 9 1 0xd063
```

**and for the low 32bit run –**

```
fuse prog -y 9 0 0x12345678
```

**In order to read the low 32bit; run –**

```
fuse read 9 0
```

**and for the high 16bit run –**

```
fuse read 9 1
```

<a id="blowing-fuses-to-boot-from-chosen-device"></a>

#### Blowing fuses to boot from chosen device

For this we blow fuse set that marks the boot device as we choose, this action instructs i.MX8M mini to ignore the boot from GPIO and use the eFuses for the boot device settings.

**From Micro SD:**

**Under Linux –**

```
echo 0x10001400 > /sys/fsl_otp/HW_OCOTP_BOOT_CFG0
```

**Under U-Boot –**

```
fuse prog -y 1 3 0x10001400
```

<a id="from-emmc"></a>

### **From eMMC**

{% hint style="warning" %}
Booting from eMMC is trickier than MicroSD since the device is soldered on the board and can’t be modified by simply taking it out and flashing it on a PC. So when flashing u-boot to the eMMC device, make sure you use a u-boot image that you can get into it’s console in case you need to modify it afterwards.
{% endhint %}


**Under Linux –**

```
echo 0x10002800 > /sys/fsl_otp/HW_OCOTP_BOOT_CFG0
```

**Under U-Boot –**

```
fuse prog -y 1 3 0x10002800
```

**As an example of flashing u-boot on eMMC –**

```
wget <URL>/flash.bin
dd if=flash.bin of=/dev/mmcblk2 bs=1K seek=33
```

{% hint style="success" %}
When finished and want to restart the system, you need to either power cycle the unit or click the reset button. Running the ‘reboot’ command will not work since new fuses values will not be activated.
{% endhint %}

