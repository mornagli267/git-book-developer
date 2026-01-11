# Temperature Sensor - i.MX6 and i.MX8M

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 28 Feb 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Introduction](#introduction)<br>- [Maximum and Minimum Temperatures by SoMs](#maximum-and-minimum-temperatures-by-soms)<br>- [i.MX6 Based Modules](#imx6-based-modules)<br>- [i.MX8M Mini/Plus Based Modules](#imx8m-mini-plus-based-modules)<br>- [Trip Points](#trip-points)<br>  - [Passive trip point](#passive-trip-point)<br>  - [Critical trip point](#critical-trip-point) |     |     |

<a id="introduction"></a>

## Introduction

The SoCs often have one or more internal temperature sensors. From Linux userspace, it is possible to read the temperature values on `/sys`.

- To better understand how things work, you can read section *2.7 - Thermal* of the [i.MX Reference Manual](https://www.nxp.com/docs/en/reference-manual/i.MX_Reference_Manual_Linux.pdf) .

<a id="maximum-and-minimum-temperatures-by-soms"></a>

## Maximum and Minimum Temperatures by SoMs

The maximum frequency to be used depends on the SoC present in the module, see the table below:

| **Module** | **Minimum Temperature (°C)** | **Maximum Temperature (°C)** |
| --- | --- | --- |
| i.mx6 (Industrial) | \-40 | 105 |
| i.mx6 (Commercial) | 0   | 95  |
| i.mx8m plus/mini (Industrial) | \-40 | 85  |
| i.mx8m plus/mini (Commercial) | 0   | 70  |

<a id="imx6-based-modules"></a>

## i.MX6 Based Modules

The i.MX6 provides a temperature reading of the SoC's internal temperature plus the board temperature is available via ADC/touch chip albeit with much worse accuracy. The output is in millidegrees Celsius aka 1000ths of degrees Celsius. Therefore it must be divided by 1000 to obtain regular degrees.

Execute the following to read the current CPU temperature:

```
cat /sys/class/thermal/thermal_zone0/temp
```

<a id="imx8m-mini-plus-based-modules"></a>

## i.MX8M Mini/Plus Based Modules

The internal temperature sensors of i.MX8M Mini and i.MX8M Plus are split into zones, accessible through `/sys/devices/virtual/thermal/thermal_zoneX`:

```
root@imx8mpsolidrun:~# ls /sys/devices/virtual/thermal/
cooling_device0  cooling_device1  thermal_zone0  thermal_zone1
```

You can read the temperature from a thermal zone as follows:

```
root@imx8mpsolidrun:~# cat /sys/devices/virtual/thermal/thermal_zone0/temp
40000
```

The zones are described as follows for i.mx8m Mini:

- zone 0 represents the temperature of the A53 CPU cores.

And for i.MX8M Plus:

- zone 0 represents the temperature of the A53 CPU cores.
- zone 1 represents the temperature of the SoC near the ANAMIX.

<a id="trip-points"></a>

## Trip Points

A trip point describes a point in the temperature domain at which the system takes an action. This node describes just the point, not the action.

<a id="passive-trip-point"></a>

### Passive trip point

When the temperature in the SOC reaches the passive trip point temperature, the SOC generates an interrupt and the driver sends a notification. Other drivers may subscribe to such notifications in order to trigger cooling actions, such as reducing their clock frequency.

> [!INFO]
> On the current BSP, the GPU driver subscribes to the temperature monitor to lower the GPU frequency when the passive trip point is reached. Expect a performance impact on graphical applications when this happens.

The passive trip point has a hysteresis of 10 °C. This means that only when the die temperature has gone 10 °C below the passive trip point, the system is considered within normal parameters and the cooling actions can be cancelled.

To read the passive trip point parameters:

```
# cat /sys/class/thermal/thermal_zone0/trip_point_0_type
passive

# debian@sr-imx8:~$ cat /sys/class/thermal/thermal_zone0/trip_point_0_temp
85000
```

To set a different temperature for the passive trip point, write the new temperature (in millicelsius) to the trip point temperature descriptor:

```
# echo 65000 > /sys/class/thermal/thermal_zone0/trip_point_0_temp
```

<a id="critical-trip-point"></a>

### Critical trip point

When the SOC temperature reaches the critical trip point temperature, the SOC generates an interrupt and the driver resets the system to avoid damaging the SoC.

To read the critical trip point parameters:

```
debian@sr-imx8:~$ cat /sys/class/thermal/thermal_zone0/trip_point_1_type
critical

# debian@sr-imx8:~$ cat /sys/class/thermal/thermal_zone0/trip_point_1_temp
95000
```

To set a different temperature for the critical trip point, write the new temperature (in millicelsius) to the trip point temperature descriptor:

```
# echo 90000 > /sys/class/thermal/thermal_zone0/trip_point_1_temperature
```

> [!NOTE]
> **Note:**
> Modifying the temperature is not necessary for i.mx6 as the driver checks the temperature grade and adapts temperatures automatically.