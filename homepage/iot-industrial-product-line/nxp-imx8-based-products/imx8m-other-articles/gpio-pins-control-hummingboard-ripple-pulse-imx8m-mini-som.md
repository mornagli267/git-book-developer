# GPIO Pins Control - HummingBoard Ripple/Pulse & i.MX8M Mini SOM

**To control on the GPIO pins:**

- The external GPIOs are available under the /sys/class/gpio folder in Linux.

- To control on the GPIO pins you need to calculate the GPIO number XX (\*) and run the commands below:

```
# Export GPIO XX
echo XX > /sys/class/gpio/export

# Set GPIO pin Direction
echo "out" > /sys/class/gpio/gpioXX/direction
or
echo "in" > /sys/class/gpio/gpioXX/direction

# Set the value of an output pin
echo 1 > /sys/class/gpio/gpioXX/value
or
echo 0 > /sys/class/gpio/gpioXX/value

# Get the value of an input pin
cat > /sys/class/gpio/gpioXX/value

# Unexport GPIO XX
echo XX > /sys/class/gpio/unexport
```

**(\*) from the schematics you can find the name of the pin/pad (find the pad name of the imx8mm processor side) and from here** [pins-imx8mm.h](https://github.com/SolidRun/linux-stable/blob/linux-5.4.y-imx8/arch/arm64/boot/dts/freescale/imx8mm-hummingboard-pulse.dts) **can find the GPIO define name of the pin/pad with the GPIO option like (MX8MM\_IOMUXC\_SAI2\_RXD0\_GPIO4\_IO23), then you can calculate the GPIO number XX**  

  
**XX** = linux gpio number = (gpio\_bank - 1) \* 32 + gpio\_bit

**Example: to calculate the GPIO number of mikroBus J8 \[pin 2\]**   
**Pad Name:** SAI2\_RXD

**Pin Define:** MX8MM\_IOMUXC\_**SAI2\_RXD0\_GPIO4\_IO23**  
GPIO Bank= 4

GPIO bit = 23  
  

**XX** = ( 4 - 1) \* 32 + 23 = 119  
  

**Attached here the MikroBus schematics:**  

![](./attachments/hb-ripple-imx8mm-mikroBus.png)

|     |     |     |     |
| --- | --- | --- | --- |
| MikroBus Pin | Pad Name (SOM side) | GPIO name | Linux GPIO number |
| J8 \[pin 2\] | SAI2\_RXD | GPIO4\_IO23 | 119 |
| J8 \[pin 3\] | ECSPI2\_SS0 | GPIO5\_IO13 | 141 |
| J8 \[pin 4\] | ECSPI2\_SCLK | GPIO5\_IO10 | 138 |
| J8 \[pin 5\] | ECSPI2\_MISO | GPIO5\_IO12 | 140 |
| J8 \[pin 6\] | ECSPI2\_MOSI | GPIO5\_IO11 | 139 |
| J10 \[pin 1\] | UART3\_CTS -> UART3\_RXD | GPIO5\_IO26 | 154 |
| J10 \[pin 2\] | UART3\_RTS -> UART3\_TXD | GPIO5\_IO27 | 155 |
| J10 \[pin 3\] | UART3\_RXD -> UART1\_RXD | GPIO5\_IO22 | 150 |
| J10 \[pin 4\] | UART3\_TXD -> UART1\_TXD | GPIO5\_IO23 | 151 |
| J10 \[pin 5\] | I2C3\_SCL | GPIO5\_IO18 | 146 |
| J10 \[pin 6\] | I2C3\_SDA | GPIO5\_IO19 | 147 |

  

**Note:** from here [**pins-imx8mm.h**](https://github.com/SolidRun/linux-stable/blob/linux-5.4.y-imx8/arch/arm64/boot/dts/freescale/imx8mm-pinfunc.h) can find the all supported functions of the pin (IOMUX options), from the Define names of same PAD name  
for example, this pad **ECSPI2\_SS0** can support 5 functions (UART RTC, UART CTS, SPI SS, GPIO, TPSMP\_HDATA) 

Define format MX8MM\_IOMUX (for more information can see NXP documentations)  

![](./attachments/image-20211104-142924.png)

To use the SPI of the MikroBus you need to configure the SPI signals in the device tree & generate new Linux kernel + device tree  

- You can this repo to generate the kerenl - 

[https://github.com/SolidRun/linux-stable/tree/linux-5.4.y-imx8](https://github.com/SolidRun/linux-stable/tree/linux-5.4.y-imx8)  

- Here can find the imx8mm device  

[https://github.com/SolidRun/linux-stable/blob/linux-5.4.y-imx8/arch/arm64/boot/dts/freescale/imx8mm-hummingboard-pulse.dts](https://github.com/SolidRun/linux-stable/blob/linux-5.4.y-imx8/arch/arm64/boot/dts/freescale/imx8mm-hummingboard-pulse.dts)  

You can see an example here - [https://community.nxp.com/t5/i-MX-Processors/Problem-with-jedec-spi-nor-on-IMX8M-Mini-EVK/m-p/963020](https://community.nxp.com/t5/i-MX-Processors/Problem-with-jedec-spi-nor-on-IMX8M-Mini-EVK/m-p/963020)