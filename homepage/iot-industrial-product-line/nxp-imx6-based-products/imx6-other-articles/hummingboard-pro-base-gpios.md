# HummingBoard Pro/Base GPIOs

### Description

![](https://developer.solid-run.com/wp-content/uploads/2018/10/hb_gpio.png)

\[HB GPIO] GPIO, or General-Purpose Input/Output is a mechanism that allows a computing board to provide electrical contacts for signalling to a wide range of external devices. These pins allow commerical and hobbyist projects to do things like communicate with a “breakout board”, or individual physical modules – like a motor.

GPIO interfaces are different than other capabilities on a circuit board (like LVDS or the RTC integration) in that they provide a non-specific electrical interface. While these other interfaces have a set specification and set capability for an intended use (connecting to an LCD panel or a real-time clock, in the cited examples respectively) GPIO pins are used at the developer’s discretion. You could connect a motor. Or a temperature sensor. Or a lock solenoid. Or any one of millions of other device combinations for bringing information into the system – or sending information out from the HummingBoard device.

### **Pin header schematics**

26 pin header

![](../../../../.gitbook/assets/image-20211118-150548.png)

### GPIO Header Pinout

| **Header Pin** | **Signal**  | **Pad Name** | **GPIO Name** | **Linux GPIO Number (\*)** |
| -------------- | ----------- | ------------ | ------------- | -------------------------- |
| J2 \[pin 1]    | 3.3V        | -            | -             | -                          |
| J2 \[pin 2]    | 5V          | -            | -             | -                          |
| J2 \[pin 3]    | I2C\_SDA    | EIM\_D18     | GPIO3\_IO18   | 82                         |
| J2 \[pin 4]    | 5V          | -            | -             | -                          |
| J2 \[pin 5]    | I2C\_SCL    | EIM\_D17     | GPIO3\_IO17   | 81                         |
| J2 \[pin 6]    | GND         | -            | -             | -                          |
| J2 \[pin 7]    | GPIO 1      | GPIO\_1      | GPIO1\_IO01   | 1                          |
| J2 \[pin 8]    | UART TX     | -            | -             | -                          |
| J2 \[pin 9]    | GND         | -            | -             | -                          |
| J2 \[pin 10]   | UART RX     | -            | -             | -                          |
| J2 \[pin 11]   | GPIO 73     | EIM\_DA9     | GPIO3\_IO09   | 73                         |
| J2 \[pin 12]   | GPIO 72     | EIM\_DA8     | GPIO3\_IO08   | 72                         |
| J2 \[pin 13]   | GPIO 71     | EIM\_DA7     | GPIO3\_IO07   | 71                         |
| J2 \[pin 14]   | GND         | -            | -             | -                          |
| J2 \[pin 15]   | GPIO 70     | EIM\_DA6     | GPIO3\_IO06   | 70                         |
| J2 \[pin 16]   | GPIO 194    | SD3\_CMD     | GPIO7\_IO02   | 194                        |
| J2 \[pin 17]   | 3.3V        | -            | -             | -                          |
| J2 \[pin 18]   | GPIO 195    | SD3\_CLK     | GPIO7\_IO03   | 195                        |
| J2 \[pin 19]   | SPI\_MOSI   | EIM\_CS1     | GPIO2\_IO24   | 56                         |
| J2 \[pin 20]   | GND         | -            | -             | -                          |
| J2 \[pin 21]   | SPI\_MISO   | EIM\_OE      | GPIO2\_IO25   | 57                         |
| J2 \[pin 22]   | GPIO 67     | EIM\_DA3     | GPIO3\_IO03   | 67                         |
| J2 \[pin 23]   | SPI\_SCLK   | EIM\_CS0     | GPIO2\_IO23   | 55                         |
| J2 \[pin 24]   | ECSPI2\_SS0 | EIM\_RW      | GPIO2\_IO26   | 58                         |
| J2 \[pin 25]   | GND         | -            | -             | -                          |
| J2 \[pin 26]   | ECSPI2\_SS1 | EIM\_LBA     | GPIO2\_IO27   | 59                         |

> \[!NOTE] Pins 16 and 18 are actually SD3\_CMD and SD3\_CLK signals that can be muxed to support flex can TX/RX interface (i.e. those can be connected to an external CAN).\
> (\*) SPI and I2C can also be muxed to be GPIO

### Serial UART port access

![](https://developer.solid-run.com/wp-content/uploads/2018/10/26pin-header.jpg)

The UART port for debug can be accessed on the 26 pin header as follows –

Pin 6/9/14/20/25 GND\
Pin 1 3.3V\
Pin 8 buffered i.MX6 UART TX – pulled up to 3.3v\
Pin 10 buffered i.MX6 UART RX – pulled up to 3.3v\
Notice that the pin number starts as pin #1 on the edge of the board, towards the micro-USB connector; then number #2 is the one towards the corner of the board.\
Accessing GPIO from Linux user space

#### General

Please have a look at WiringX, which also supports the Hummingboard:

[http://wiringx.org/](http://wiringx.org/)

#### **Manual**

* The external GPIOs are available under the /sys/class/gpio folder in Linux.
* To control on the GPIO pins you need to calculate the GPIO number XX (\*) and run the commands below:

**Get the current list of reserved GPIO**

```
mount -t debugfs none /sys/kernel/debug
cat /sys/kernel/debug/gpio
```

**Reserve GPIO pin**

```
# Export GPIO XX
echo XX > /sys/class/gpio/export
```

**Set GPIO pin Direction**

```
echo "out" > /sys/class/gpio/gpioXX/direction
# or
echo "in" > /sys/class/gpio/gpioXX/direction
```

**Set the value of an output pin**

```
echo 1 > /sys/class/gpio/gpioXX/value
# or
echo 0 > /sys/class/gpio/gpioXX/value
```

**Get the value of an input pin**

```
cat > /sys/class/gpio/gpioXX/value
```

**Free GPIO pin**

```
# Unexport GPIO XX
echo XX > /sys/class/gpio/unexport
```

To calculate the GPIO number **XX:**\
**XX** = linux gpio number = (gpio\_bank - 1) \* 32 + gpio\_bit

**Example:** To calculate the GPIO number of pin header J2 \[pin 12] Pad Name **GPIO3\_IO08**

GPIO Bank = 3, GPIO bit = 8

**XX** = (3 - 1) \* 32 + 8 = 72

> \[!NOTE] You can take the GPIO Number from the above table (\*)

### External Links and References

* IMX6 Software Development/Drivers
* IMX6 Som Documents
* wiringHB
* [http://wiringx.org/](http://wiringx.org/)
