# KGDB Kernel Debugger

This page describes how to use in-kernel KGDB to debug the Linux Kernel running on LX2162A Clearfog Board.

<a id="requirements"></a>

## Requirements

On the Target (LX2162A Clearfog) a native UART from the SoC must be used. UART1 (`ttyAMA0`) is normally used for console access (mini-USB connector).

Additionally UART2 (`ttyAMA1`) is available on pin header J19.

The host may connect to the target by any suitable usb-to-uart adapters, usually showing up as `/dev/ttyUSB0` or similar.

Further the kernel must be recompiled adding support for KGDB and additional symbol information:

```
CONFIG_KGDB=y
CONFIG_DEBUG_INFO=y
# CONFIG_DEBUG_INFO_REDUCED is not set
```

Finally the target must disable its watchdog functionality to avoid unintended reset while debugging.

<a id="configure-host"></a>

## Configure Host

<a id="dedicated-uart"></a>

### Dedicated UART

Debugging Linux using the LX2162A Clearfog UART2 exposed on J19 pin header at 3.3V logic level.

**Note: This method currently is not functional during the author’s testing …**

<a id="share-console"></a>

### Share Console

Debugging Linux using the LX2162A Clearfog UART1 that is already in use for console.

Kernel developers provide a proxy tool for multiplexing between KGDB commands and the regular console from a single UART: [https://git.kernel.org/pub/scm/utils/kernel/kgdb/agent-proxy.git/tree/README.TXT](https://git.kernel.org/pub/scm/utils/kernel/kgdb/agent-proxy.git/tree/README.TXT)

It reads from the Host (PC) Serial POrt that is connected to the Target, and exposes KGDB and Console on two local network ports for access from gdb and telnet.

If on the Host side the console uart is `/dev/ttyUSB0`, then the agent-proxy is started as follows:

```
./agent-proxy 5550^5551 0 /dev/ttyUSB0,115200
Agent Proxy 1.97 Started with: 5550^5551 0 /dev/ttyUSB0,115200
Agent Proxy running. pid: 855222
```

**Note: Ensure no other process is opening the serial device, in particular no other terminal emulator.**

Console is now available using telnet:

```
telnet localhost 5550
```

Note: When configuring the target, choose `ttyAMA0` for KGDB.

Note: When configuring the target, choose `ttyAMA0` for KGDB.

**Note: When configuring the target, choose** `ttyAMA0`**for KGDB instead of dedicated** `ttyAMA1`**.**

<a id="configure-debugger-on-target"></a>

## Configure Debugger on Target

<a id="disable-watchdog"></a>

### Disable Watchdog

1. In Linux edit systemd config file to disable watchdog configuration:
```
sed -i "s;^\(RuntimeWatchdogSec=.*\)$;#\1;g" /etc/systemd/system.conf
```
2. In boot-loader during every boot, break to u-boot console during the timeout and stop the watchdog:
```
Hit any key to stop autoboot:  0 
=> wdt list
watchdog@23a0000 (sbsa_gwdt)
=> wdt dev watchdog@23a0000
=> wdt stop
=> boot
```

<a id="at-boot-time"></a>

### At Boot-Time

Kernel debugger can be configured using kernel cmdline passed from bootloader.

Edit extlinux.conf `APPEND` line and add `kgdboc=ttyAMA1,115200` - e.g.:

```
  timeout 30
  default linux
  menu title linux-lx2160a boot options
  label primary
    menu label primary kernel
    linux /boot/Image.gz
    fdtdir /boot/
    APPEND console=ttyAMA0,115200 earlycon=pl011,mmio32,0x21c0000 default_hugepagesz=1024m hugepagesz=1024m hugepages=2 pci=pcie_bus_perf root=PARTUUID=30303030-01 rw rootwait kgdboc=ttyAMA1,115200 kgdbwait
```

<a id="at-run-time"></a>

### At Run-Time

Kernel debugger can be enabled at run-time by setting the `kgdboc` parameter through sysfs:

```
echo ttyAMA1,115200 > /sys/module/kgdboc/parameters/kgdboc
[   42.920363] KGDB: Registered I/O driver kgdboc
```

<a id="start-debugging"></a>

## Start Debugging

To start a debug session requires coordinated steps on both the Host (PC) and the Target (LX2162A Clearfog). Extra complication is added by system watchdog if it wasn’t disabled properly.

<a id="target"></a>

### Target

A debug session on the Target is started by issuing magic sysrq - which will halt the kernel and start KGDB:

```
echo g > /proc/sysrq-trigger
[  907.508271] sysrq: DEBUG
[  907.510809] KGDB: Entering KGDB
```

<a id="host"></a>

### Host

The Host should connect to the Target immediately after sysrq was issued. It is recommended to first start gdb and wait while it loads `vmlinux` file - then issue sysrq and connect (`target` command).

```
gdb-multiarch vmlinux -tui
GNU gdb (Debian 13.1-3) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from vmlinux...
(gdb) # for dedicated UART
(gdb) set serial baud 115200
(gdb) target remote /dev/ttyUSB1
(gdb) # for Console UART
(gdb) target remote localhost:5551
Remote debugging using localhost:5551
```