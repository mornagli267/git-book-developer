# HummingBoard Edge/Gate/CBi GPIO Pins Control

**To control on the GPIO pins:**

* The external GPIOs are available under the /sys/class/gpio folder in Linux.
* To control on the GPIO pins you need to calculate the GPIO number XX (\*) and run the commands below:

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
cat /sys/class/gpio/gpioXX/value

# Unexport GPIO XX
echo XX > /sys/class/gpio/unexport
```

You can calculate the GPIO number XX:\
**XX** = linux gpio number = (gpio\_bank - 1) \* 32 + gpio\_bit

**Example: to calculate the GPIO number of pin header J1 \[pin 3]**&#x20;

**Pad Name :** DISP1\_DATA0

GPIO Bank = 3

GPIO bit = 9

**XX** = linux gpio number = (3 - 1)\*32 + 9 = 73

**Attached here the headers schematics**

36 pin header implemented using 4 headers

![](../../../../.gitbook/assets/image-20211118-123626.png)

| **Header Pin** | **Pad Name**   | **GPIO name** | **Linux GPIO number** |
| -------------- | -------------- | ------------- | --------------------- |
| J21 \[pin 1]   | 3.2V           |               |                       |
| J21 \[pin 2]   | 5V             |               |                       |
| J21 \[pin 3]   | DISP1\_DATA00  | GPIO3\_IO09   | 73                    |
| J21 \[pin 4]   | DISP1\_DATA01  | GPIO3\_IO08   | 72                    |
| J21 \[pin 5]   | DISP1\_DATA04  | GPIO3\_IO05   | 69                    |
| J21 \[pin 6]   | DISP1\_DATA05  | GPIO3\_IO04   | 68                    |
| J23 \[pin 1]   | DI1\_D0\_CS    | GPIO3\_IO13   | 77                    |
| J23 \[pin 2]   | DI1\_D1\_CS    | GPIO3\_IO14   | 78                    |
| J23 \[pin 3]   | DISP1\_DAT08   | GPIO3\_IO01   | 65                    |
| J23 \[pin 4]   | DISP1\_DAT09   | GPIO3\_IO00   | 64                    |
| J23 \[pin 5]   | DISP1\_DAT12   | GPIO2\_IO21   | 53                    |
| J23 \[pin 6]   | DISP1\_DAT13   | GPIO2\_IO20   | 52                    |
| J23 \[pin 7]   | DISP1\_DAT16   | GPIO2\_IO17   | 49                    |
| J23 \[pin 8]   | DISP1\_DAT17   | GPIO2\_IO16   | 48                    |
| J23 \[pin 9]   | DISP1\_DAT20   | GPIO3\_IO31   | 95                    |
| J23 \[pin 10]  | DISP1\_DAT21   | GPIO3\_IO30   | 94                    |
| J23 \[pin 11]  | GND            |               |                       |
| J23 \[pin 12]  | DI1\_DISP\_CLK | GPIO2\_IO22   | 54                    |
| J22 \[pin 1]   | DI1\_PIN15     | GPIO3\_IO10   | 74                    |
| J22 \[pin 2]   | DISP1\_DATA03  | GPIO3\_IO11   | 75                    |
| J22 \[pin 3]   | DISP1\_DATA02  | GPIO3\_IO07   | 71                    |
| J22 \[pin 4]   | DISP1\_DATA03  | GPIO3\_IO06   | 70                    |
| J22 \[pin 5]   | DISP1\_DATA06  | GPIO3\_IO03   | 67                    |
| J22 \[pin 6]   | DISP1\_DATA07  | GPIO3\_IO02   | 66                    |
| J24 \[pin 1]   | DI1\_PIN01     | GPIO3\_IO15   | 79                    |
| J24 \[pin 2]   | DI1\_PIN03     | GPIO3\_IO12   | 76                    |
| J24 \[pin 3]   | DISP1\_DATA10  | GPIO2\_IO29   | 61                    |
| J24 \[pin 4]   | DISP1\_DATA11  | GPIO2\_IO28   | 60                    |
| J24 \[pin 5]   | DISP1\_DATA14  | GPIO2\_IO19   | 51                    |
| J24 \[pin 6]   | DISP1\_DATA15  | GPIO2\_IO18   | 50                    |
| J24 \[pin 7]   | DISP1\_DATA18  | GPIO6\_IO06   | 166                   |
| J24 \[pin 8]   | DISP1\_DATA19  | GPIO5\_IO04   | 132                   |
| J24 \[pin 9]   | DISP1\_DATA22  | GPIO3\_IO26   | 90                    |
| J24 \[pin 10]  | DISP1\_DATA23  | GPIO3\_IO27   | 91                    |
| J24 \[pin 11]  | SPDIF\_IN      | GPIO1\_IO24   | 24                    |
| J24 \[pin 12]  | SPDIF\_OUT     | GPIO7\_IO12   | 204                   |
