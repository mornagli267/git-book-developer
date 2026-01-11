# GPIO Pins Control - HummingBoard Pulse/Mate & i.MX8M Plus SOM

**To control on the GPIO pins:**

- The external GPIOs are available under the /sys/class/gpio folder in Linux.

- To control on the GPIO pins you need to calculate the GPIO number XX (\*) and run the commands below:

```
===================================================
# Export GPIO XX 
===================================================
XX=<GPIO-Linux-Number>
echo ${XX} > /sys/class/gpio/export

# Set GPIO pin Direction Output/Input
===================================================
# 1- Output -> 
===================================================
echo "out" > /sys/class/gpio/gpio${XX}/direction
# Set the output value
# High
echo 1 > /sys/class/gpio/gpio${XX}/value
# or LOW
echo 0 > /sys/class/gpio/gpio${XX}/value

===================================================
# 2- Input -> 
===================================================
echo "in" > /sys/class/gpio/gpio${XX}/direction
# Get the input value
cat /sys/class/gpio/gpio${XX}/value

===================================================
# Unexport GPIO XX
===================================================
echo ${XX} > /sys/class/gpio/unexport
```

**(\*) from the schematics you can find the name of the pin/pad (find the pad name of the imx8mp processor side) and from here** [pins-imx8mp.h](https://github.com/SolidRun/linux-stable/blob/linux-5.4.y-imx8/arch/arm64/boot/dts/freescale/imx8mp-pinfunc.h) **can find the GPIO define name of the pin/pad with the GPIO option like (MX8MP\_IOMUXC\_SAI2\_RXD0\_\_GPIO4\_IO23), then you can calculate the GPIO number XX**  

  
**XX** = linux gpio number = (gpio\_bank - 1) \* 32 + gpio\_bit

**Example: to calculate the GPIO number of mikroBus J8 \[pin 2\]**   
**Pad Name:** SAI2\_RXD

**Pin Define:** MX8MP\_IOMUXC**\_SAI2\_RXD0\_\_\_GPIO4\_IO23**  
GPIO Bank= 4

GPIO bit = 23  
  

**XX** = ( 4 - 1) \* 32 + 23 = 119  
  

**Attached here the MikroBus schematics:**  

![](./attachments/hb-ripple-imx8mm-mikroBus.png)

|     |     |     |     |
| --- | --- | --- | --- |
| MikroBus Pin | Pad Name (SOM side) | GPIO name | Linux GPIO number |
| J8 \[pin 2\] | SAI3\_RXD | GPIO4\_IO30 | 126 |
| J8 \[pin 3\] | ECSPI2\_SS0 | GPIO5\_IO13 | 141 |
| J8 \[pin 4\] | ECSPI2\_SCLK | GPIO5\_IO10 | 138 |
| J8 \[pin 5\] | ECSPI2\_MISO | GPIO5\_IO12 | 140 |
| J8 \[pin 6\] | ECSPI2\_MOSI | GPIO5\_IO11 | 139 |
| J10 \[pin 1\] | UART3\_CTS -> **ECSPI1\_MISO** | GPIO5\_IO08 | 136 |
| J10 \[pin 2\] | UART3\_RTS -> **ECSPI1\_SS0** | GPIO5\_IO09 | 137 |
| J10 \[pin 3\] | UART3\_RXD -> **ECSPI1\_SCLK** | GPIO5\_IO06 | 134 |
| J10 \[pin 4\] | UART3\_TXD -> **ECSPI1\_MOSI** | GPIO5\_IO07 | 135 |
| J10 \[pin 5\] | I2C3\_SCL (reserved) | GPIO5\_IO18 | 146 |
| J10 \[pin 6\] | I2C3\_SDA (reserved) | GPIO5\_IO19 | 147 |

  

**Note:** from here [**pins-imx8mp.h**](https://github.com/SolidRun/linux-stable/blob/lf-5.15-sr-imx8/arch/arm64/boot/dts/freescale/imx8mp-pinfunc.h) can find the all supported functions of the pin (IOMUX options), from the Define names of same PAD name  
for example, this pad **ECSPI2\_SS0** can support 5 functions (UART RTC, UART CTS, SPI SS, GPIO, TPSMP\_HDATA) 

Define format MX8MP\_IOMUX (for more information can see NXP documentations)  

![](./attachments/image-20221009-131116.png)

To use the SPI of the MikroBus you need to configure the SPI signals in the device tree & generate new Linux kernel + device tree  

- You can use this repo to generate the kerenl - 

[https://github.com/SolidRun/linux-stable/tree/lf-5.15-sr-imx8](https://github.com/SolidRun/linux-stable/tree/lf-5.15-sr-imx8)  

- Here can find the imx8mp device  tree  
[https://github.com/SolidRun/linux-stable/blob/lf-5.15-sr-imx8/arch/arm64/boot/dts/freescale/imx8mp-hummingboard-pulse.dts](https://github.com/SolidRun/linux-stable/blob/lf-5.15-sr-imx8/arch/arm64/boot/dts/freescale/imx8mp-hummingboard-pulse.dts)