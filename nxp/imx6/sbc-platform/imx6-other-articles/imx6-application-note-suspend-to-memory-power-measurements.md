# i.MX6 Application Note – Suspend to Memory Power Measurements

<a id="introduction"></a>

## Introduction

The SolidRun i.MX6 SOM is a high performance system on module that is based on the highly integrated NXP i.MX6 family of products.

This application note provides information on power consumption of the i.MX6 SOM suspend to memory feature.

Suspend to memory is a feature that enables putting the whole system in memory retention mode where waking up the whole system back again is very fast. In this case the DDR memories are put in self-refresh-mode where its content is preserved and used when the system is awakened.

As a preparation for the measurement the following components were selected –

1. HummingBoard Base with the below modifications
2. SOM i.MX6 solo with 512Mbyte memory
3. SOM i.MX6 solo with 512Mbyte memory and AR8035 Gigabit Ethernet PHY
4. SOM i.MX6 solo with 512Mbyte memory, AR8035 Gigabit Ethernet PHY and BCM4330 WiFi/BT SiP
5. SOM i.MX6 dual lite with 1GByte of memory and AR8035 Gigabit Ethernet PHY
6. SOM i.MX6 dual with 1GByte of memory and AR8035 Gigabit Ethernet PHY
7. SOM i.MX6 quad with 2GByte of memory, AR8035 Gigabit Ethernet PHY and BCM4330 WiFi/BT SiP

The modifications to the HummingBoard Base were done in order to have a PCB that has only the 5v and 3.3v power rails coming from an external power supply where the HummingBoard itself will consume almost no power when the SOM i.MX6 is disconnected (i.e. to really test the power consumption of the SOM alone).

The following modifications were done on HummingBoard Base configuration –

1. Remove Red LED – Remove D3
2. Remove PWM audio – Removed R7, C7 and D4
3. uSD is power directly from 3.2v – Remove R24, Q1, R3013 and short R3
4. Remove 5v to 3.2v LDO and supply 3.2v from external power supply – Remove U8, R22, C64 and R21
5. Remove USB current limiter – Remove U9

With the previous modifications the following was achieved while measuring the currents on the 5V and 3.2V power rails while the SOM i.MX6 is **NOT inserted**; i.e. measure leakages only on HummingBoard itself –

|     |     |     |
| --- | --- | --- |
| **HummingBoard carrier without SOM** | **Current on 5V rail (mA)** | **Current on 3.2v rail (mA)** |
| uSD inserted | 0.6 | 1   |
| uSD not inserted | 0.6 | 0.2 |

The conclusion is that the uSD card that was used consumes 0.8mA in idle mode.

<a id="som-imx6-power-measurements"></a>

## **SOM i.MX6 Power Measurements**

The following measurements are on the 5V and 3.2V rails while running Linux kernel 3.0.35.

In Linux we run the following two commands where the first set the debug console as an interface to wake the system from (by pressing any key) and second line puts the system in suspend to memory state.

```
echo enabled > /sys/devices/platform/imx-uart.0/tty/ttymxc0/power/wakeup echo mem > /sys/power/state
```

Pressing any key on the console awakens the system. The wakeup time for the system is reported to be 168 msec. Notice that external peripherals on USB for example are awakened later on.

Following is the power consumption of 3 different configurations of the SOM i.MX6 –

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **SOM name** | **SOM Details** | **5V rail (mA)** | **3.2v rail (mA) (\*)** | **Total power (mW)** |
| Solo without gig phy | SOM i.MX6 solo with 512Mbyte memory without Gigabit phy | 6.83 | 1.23 | 38  |
| Solo | SOM i.MX6 solo with 512Mbyte memory with Gigabit phy | 6.92 | 6.21 | 54  |
| Solo wifh Wifi | SOM i.MX6 solo with 512Mbyte memory, Gigabit phy and wifi/bt SiP (\*\*) | 10.7 | 6.78 | 75  |
| Dual-lite | SOM i.MX6 dual lite with 1GByte memory and Gigabit phy | 8.79 | 6.19 | 64  |
| Dual | SOM i.MX6 dual with 1GByte memory and Gigabit phy | 8.7 | 6.15 | 63  |
| Quad | SOM i.MX6 quad with 2GByte memory, Gigabit phy and wifi/bt SiP (\*\*) | 14.2 | 7.05 | 93.5 |

(\*) When the current is measured the uSD card was removed in order to measure the current that is consumed by the SOM.

(\*\*) WiFi/B T are put into reset by setting the GPIO that controls the regulator to 0 (gpio3, bit 19) – devmem 0x020a4000 32 0x00400000.

<a id="conclusion"></a>

## Conclusion

A system using the SOM can use the suspend to memory feature and consume, depending on the configuration, down to **38mW to 93.5mW** power.

<a id="som-imx6-quad-power-measurements"></a>

## **SOM i.MX6 Quad Power Measurements**

These are the numbers for the iMX6 Quad on the [HummingBoard Edge](../../nxp-imx6-based-products/hummingboard-imx6-sbc-quick-start-guide/hummingboard-edge-quick-start-guide.md), which is the worst case scenario **without taking into account external peripherals**.

**SOM Details** : SOM i.MX6 quad with 2GByte memory, Gigabit phy and wifi/bt SiP .

Values are additional to the idle no display number

|     |     |     |
| --- | --- | --- |
| **State** | **Current (mA)** | **Power (W)** |
| sleep | 35  | 0.4 |
| idle no display | 70-75 | 0.85-0.95 |
| 1080p display | +45 | +0.55 |
| WiFi active | +10 | +0.12 |
| Bluetooth active | +5  | +0.06 |
| Ethernet gigabit link idle | +30 | +0.36 |
| Ethernet gigabit link idle with smartEEE | +7  | +0.085 |
| 4 cores 1Ghz running cpuburn with neon | +330 | +4  |
| low load cpu + full GPU | +200 | 2.4 |
| fully loaded cpu + gpu + display | 656 | 8   |

The average active workload is 1W-2.5W depending on the task .