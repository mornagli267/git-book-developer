# CPU Frequency and DVFS - i.MX6 and i.MX8M

## Revision and Notes

| **Date**          | **Owner**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Revision** | **Notes**       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- |
| 28 Feb 2022       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1.0          | Initial release |
| Table of Contents | <p>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#revision-and-notes">Revision and Notes</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#introduction">Introduction</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#maximum-frequency-by-soms">Maximum Frequency by SoMs</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#cpu-frequency">CPU Frequency</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#changing-the-scaling-governor">Changing the scaling governor</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#changing-cpu-frequency">Changing CPU frequency</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#cpufreq-userspace-tools">CPUFreq Userspace Tools</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#enable-disable-cpu">Enable/Disable CPU</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#disable-cpu">Disable CPU</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#enable-cpu">Enable CPU</a><br>- <a href="cpu-frequency-and-dvfs-imx6-and-imx8m.md#gpu-clock-information-and-debugging">GPU clock information and debugging</a></p> |              |                 |

## Introduction

The Linux Kernel supports dynamic voltage and frequency switching (DVFS) in order to minimize power usage. Generally, the feature should remain enabled, however, if power consumption and heat dissipation aren't an issue and low latency is required, it might make sense to disable frequency scaling.

## Maximum Frequency by SoMs

The maximum frequency to be used depends on the SoC present in the module, see the table below:

| **Module**                    | **Maximum frequency (Hz)** |
| ----------------------------- | -------------------------- |
| i.mx6                         | 792000                     |
| i.mx8m plus/mini (Industrial) | 1600000                    |
| i.mx8m plus/mini (Commercial) | 1800000                    |

## CPU Frequency

{% hint style="info" %}
**Please Note:** The operation below requires root access.
{% endhint %}


CPU frequency can be changed by using one of the following methods:

### Changing the scaling governor

CPU governors can be viewed as preconfigured power settings for the CPU, for detailed information about governors consult [this](https://wiki.archlinux.org/title/CPU_frequency_scaling#scaling_governors) article.

Available governors can be seen through "scaling\_available\_governors" file:

```
root@sr-imx8:/home/debian# cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
conservative powersave userspace ondemand performance schedutil
```

Execute the following command to see current scaling governor:

```
root@sr-imx8:/home/debian# cat /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
ondemand
```

Execute the following command to change the scaling governor:

```
echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
```

Where **performance** is the name of the scaling governor.

### Changing CPU frequency

{% hint style="info" %}
**Please Note:** CPU frequency can be changed only when the scaling governor is set to userspace.
{% endhint %}


Available frequencies values can be seen through "scaling\_available\_frequencies" file:

```
root@sr-imx8:/home/debian# cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
1200000 1600000 1800000
```

Execute the following command to see current CPU frequency:

```
root@sr-imx8:/home/debian# cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq
1200000
```

Execute the following command to set CPU frequency:

```
echo frequency > /sys/devices/system/cpu/cpufreq/policy0/scaling_setspeed
```

Where **frequency** is one of the available CPU frequencies.

{% hint style="info" %}
**Note:** The userspace governor must be set to change the frequency value.
{% endhint %}


The system will adjust to an appropriate voltage according to frequency. Please note that depending on the board/die temperature, thermal throttling might limit the current frequency in use.

## CPUFreq Userspace Tools

The cpufreq userspace tools can be used to achieve the same results as above.

Check the current frequency information:

```
debian@sr-imx8:~$ cpufreq-info
cpufrequtils 008: cpufreq-info (C) Dominik Brodowski 2004-2009
Report errors and bugs to cpufreq@vger.kernel.org, please.
analyzing CPU 0:
  driver: cpufreq-dt
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 150 us.
  hardware limits: 1.20 GHz - 1.80 GHz
  available frequency steps: 1.20 GHz, 1.60 GHz, 1.80 GHz
  available cpufreq governors: conservative, powersave, userspace, ondemand, performance, schedutil
  current policy: frequency should be within 1.20 GHz and 1.80 GHz.
                  The governor "ondemand" may decide which speed to use
                  within this range.
  current CPU frequency is 1.20 GHz (asserted by call to hardware).
  cpufreq stats: 1.20 GHz:98.03%, 1.60 GHz:0.63%, 1.80 GHz:1.34%  (394)
analyzing CPU 1:
  driver: cpufreq-dt
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 150 us.
  hardware limits: 1.20 GHz - 1.80 GHz
  available frequency steps: 1.20 GHz, 1.60 GHz, 1.80 GHz
  available cpufreq governors: conservative, powersave, userspace, ondemand, performance, schedutil
  current policy: frequency should be within 1.20 GHz and 1.80 GHz.
                  The governor "ondemand" may decide which speed to use
                  within this range.
  current CPU frequency is 1.20 GHz (asserted by call to hardware).
  cpufreq stats: 1.20 GHz:98.03%, 1.60 GHz:0.63%, 1.80 GHz:1.34%  (394)
analyzing CPU 2:
  driver: cpufreq-dt
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 150 us.
  hardware limits: 1.20 GHz - 1.80 GHz
  available frequency steps: 1.20 GHz, 1.60 GHz, 1.80 GHz
  available cpufreq governors: conservative, powersave, userspace, ondemand, performance, schedutil
  current policy: frequency should be within 1.20 GHz and 1.80 GHz.
                  The governor "ondemand" may decide which speed to use
                  within this range.
  current CPU frequency is 1.20 GHz (asserted by call to hardware).
  cpufreq stats: 1.20 GHz:98.03%, 1.60 GHz:0.63%, 1.80 GHz:1.34%  (394)
analyzing CPU 3:
  driver: cpufreq-dt
  CPUs which run at the same hardware frequency: 0 1 2 3
  CPUs which need to have their frequency coordinated by software: 0 1 2 3
  maximum transition latency: 150 us.
  hardware limits: 1.20 GHz - 1.80 GHz
  available frequency steps: 1.20 GHz, 1.60 GHz, 1.80 GHz
  available cpufreq governors: conservative, powersave, userspace, ondemand, performance, schedutil
  current policy: frequency should be within 1.20 GHz and 1.80 GHz.
                  The governor "ondemand" may decide which speed to use
                  within this range.
  current CPU frequency is 1.20 GHz (asserted by call to hardware).
  cpufreq stats: 1.20 GHz:98.03%, 1.60 GHz:0.63%, 1.80 GHz:1.34%  (394)
```

Change CPU frequency behavior to userspace:

```
cpufreq-set -g userspace
```

Change CPU frequency value by setting the CPU frequency explicitly:

```
cpufreq-set -f frequency
```

Where **frequency** is the desired frequency.

## Enable/Disable CPU

Check the number of available CPUs/cores by simply running the following command and hit '1':

```
root@sr-imx8:/home/debian# top
top - 08:57:45 up 18 min,  1 user,  load average: 0.00, 0.00, 0.00
Tasks: 127 total,   1 running, 126 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.1 us,  0.1 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   2942.0 total,   2416.9 free,    338.5 used,    186.6 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   2530.3 avail Mem
```

### Disable CPU

Directory path to see available CPU devices : `/sys/devices/system/cpu`

To disable CPU core, execute the following command:

```
echo 0 > /sys/devices/system/cpu/cpu3/online
```

* Verify whether CPU has been disabled or not by executing TOP utility.
* Choose on which one to work when using the previous command by checking the CPU core number:

```
debian@sr-imx8:~$ ls /sys/devices/system/cpu/
consumers  cpu2     hotplug     modalias  possible  smt        vulnerabilities
cpu0       cpu3     isolated    offline   power     suppliers
cpu1       cpufreq  kernel_max  online    present   uevent
```

### Enable CPU

To enable CPU which have been disabled above, execute the following:

```
echo 1 > /sys/devices/system/cpu/cpu3/online
```

* Check the status of enable CPUs by executing TOP utility.

### GPU clock information and debugging

![](../../../.gitbook/assets/image-20221222-113545.png)

go to section 14.3 of [https://www.nxp.com/docs/en/user-guide/i.MX\_AA\_Graphics\_User's\_Guide.pdf](https://www.nxp.com/docs/en/user-guide/i.MX_AA_Graphics_User's_Guide.pdf)
