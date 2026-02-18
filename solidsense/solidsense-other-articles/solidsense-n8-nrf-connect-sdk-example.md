# SolidSense N8 nRF Connect SDK Example

This document gives instructions for using Nordic [nRF Connect SDK](https://www.nordicsemi.com/Products/Development-software/nRF-Connect-SDK) for programming the 802.15.1 radio on SolidSense N8.

Instructions herein were tested on [SolidRun Yocto BSP for i.MX8, Scarthgap release](https://github.com/SolidRun/meta-solidrun-arm-imx8/tree/scarthgap-imx8m).

<a id="installing-nrf-connect-sdk"></a>

## Installing nRF Connect SDK

Carefully read the [nRF Connect SDK Documentation](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/installation/install_ncs.html) for installation instructions. At a bare minimum on a Linux host they boil down to the following steps:

- Install `nrfutil` cli application
- Install Toolchain using `nrfutil`
- Download SDK Sources using `nrfutil`
- Generate CMake Target

```
install -v -m755 -o root -g root ~/Downloads/nrfutil /usr/local/bin/
nrfutil install sdk-manager
nrfutil sdk-manager toolchain install --ncs-version v2.9.1

nrfutil sdk-manager toolchain launch --ncs-version v2.9.1  --shell
west init -m <https://github.com/nrfconnect/sdk-nrf> --mr v2.9.1 v2.9.1
cd ~/ncs/v2.9.1
west update
west zephyr-export
```

<a id="enter-development-environment"></a>

## Enter Development Environment

This step should be repeated when launching a new terminal session:

```
nrfutil sdk-manager toolchain launch --ncs-version v2.9.1  --shell
cd ~/ncs/v2.9.1
source zephyr/zephyr-env.sh

cd <your-workspace>
```

<a id="define-custom-board"></a>

## Define Custom Board

Ultimately defining the SolidSense N8 as a board in Zephyr would be nice but is left as an exercise for the future.

Instead it is possible to reuse the already supported "nrf52833dk" board which is similar enough.

A device-tree overlay should be added to the application process with customer- and SolidRun-specific changes: `<app-source>/boards/nrf52833dk_nrf52833.overlay`:

```
/*
 * Copyright (c) 2025 Josua Mayer <josua@solid-run.com>
 */

&button0 {
        /* remap to GPIO18 (BT_RST#) from application processor */
	gpios = <&gpio1 2 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
};

&uart0 {
	/* Note: Flow-Control should be disabled: hw-flow-control; */
};
```

<a id="thread-cli-sample"></a>

## Thread CLI Sample

nRF Connect SDK provides a [Thread example](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/samples/openthread/cli/README.html) application with CLI interface on the MCU UART.  
It can be ported to the SolidSense N8 as follows:

1. Copy example from nRF Connect SDK:
```
cd <your-workspace>
cp -r ~/ncs/v2.9.1/nrf/samples/openthread/cli ./ot-cli-app
cd ot-cli-app
# optionally initialise version control
git init .
git add .
git commit
```
2. Add Board configuration:Create a new device-tree overlay at `boards/nrf52833dk_nrf52833.overlay` with the content described above.
3. Compile
```
west build -b nrf52833dk/nrf52833
```
The resulting application binary is found at `build/ot-cli-app/zephyr/zephyr.bin`:
```
ls -ln ./build/ot-cli-app/zephyr/zephyr.bin
-rwxr-xr-x 1 1001 100 461524  7. Apr 18:38 ./build/ot-cli-app/zephyr/zephyr.bin
```

<a id="program-application"></a>

## Program Application

The generated `zephyr.bin` file comes without separate bootloader and can be installed at offset 0 to the MCU flash.  
The programming procedure utilizes SWD interface with [OpenOCD](https://openocd.org/).

OpenOCD uses a server-client architecture, it is therefore recommended to operate at least two concurrent terminals to the board, e.g. one UART Console and one SSH, or 2x SSH.  
Open a third console for interactive debugging to monitor the UART between MCU and Linux.

<a id="take-mcu-out-of-reset"></a>

### Take MCU out of reset

The MCU may be kept in reset by GPIO1\_IO5 of the Host. Release it:

```
# check status of control gpios (reset, power)
gpioget -c /dev/gpiochip0 5 6
"5"=inactive "6"=active

# release reset
gpioset -c /dev/gpiochip0 5=1
```

<a id="start-openocd"></a>

### Start OpenOCD

A suitable configuration file for SolidSense N8 with FWM7BLZ22W MCU is provided below:

```
source [find interface/imx-native.cfg]
transport select swd
set WORKAREASIZE 0
source [find target/nrf52.cfg]
imx_gpio_peripheral_base 0x30200000
imx_gpio_speed_coeffs 50000 50
imx_gpio_swd_nums 14 15
```

The above is included by default in our Yocto BSP at `/etc/openocd.cfg`, but can be created on the fly as needed.

On the first console start the openocd server:

```
root@solidsense-n8:~# openocd --file /etc/openocd.cfg
Open On-Chip Debugger 0.12.0+dev-00150-g91bd43134-dirty (2025-04-07-18:00)
Licensed under GNU GPL v2
For bug reports, read
        <http://openocd.org/doc/doxygen/bugs.html>
imx_gpio GPIO nums: swclk = 14, swdio = 15
Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
Info : imx_gpio GPIO JTAG/SWD bitbang driver
Info : imx_gpio mmap: pagesize: 4096, regionsize: 131072
Info : clock speed 1000 kHz
Info : SWD DPIDR 0x2ba01477
Info : [nrf52.cpu] Cortex-M4 r0p1 processor detected
Info : [nrf52.cpu] target has 6 breakpoints, 4 watchpoints
Info : starting gdb server for nrf52.cpu on 3333
Info : Listening on port 3333 for gdb connections
```

<a id="program-mcu-flash"></a>

### Program MCU Flash

First the generated `zephyr.bin` file must be copied to the SolidSense N8 filesystem, e.g. at `/root/zephyr.bin`.

While openocd is running on the first console, use the second console for connecting with telnet:

```
root@solidsense-n8:~# telnet 127.0.0.1 4444
Connected to 127.0.0.1

Entering character mode
Escape character is '^]'.

Open On-Chip Debugger
> targets
    TargetName         Type       Endian TapName            State
--  ------------------ ---------- ------ ------------------ ------------
 0* nrf52.cpu          cortex_m   little nrf52.cpu          running
```

Halt the processor, erase flash and program `zephyr.bin`:

```
> halt
[nrf52.cpu] halted due to debug-request, current mode: Thread
xPSR: 0x41000000 pc: 0x0002083e psp: 0x20007e20
> nrf5 mass_erase
Mass erase completed.
> program /root/zephyr.bin 0x0000
[nrf52.cpu] halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0xfffffffe msp: 0xfffffffc
** Programming Started **
Adding extra erase range, 0x00070ad4 .. 0x00070fff
not enough working area available(requested 34)
no working area available, falling back to slow memory writes
** Programming Finished **
```

Programming may take a minute without progress indication.

Finally the MCU can be reset to restart execution.  
It is however recommended to open `/dev/ttymsxc3` and monitor the MCU UART before reset:

```
> reset
shutdown command invoked
```

<a id="open-mcu-uart-console"></a>

## Open MCU UART Console

This example provides a CLI on the UART that can be accessed from Linux running on the N8:

```
root@solidsense-n8:~# microcom -s 115200 /dev/ttymxc3

uart:~$ *** Booting nRF Connect SDK v2.9.1-60d0d6c8d42d ***
*** Using Zephyr OS v3.7.99-ca954a6216c9 ***
help
Please press the <Tab> button to see all available commands.
You can also use the <Tab> button to prompt or auto-complete all commands or its subcommands.
You can try to call commands with <-h> or <--help> parameter for more information.

Shell supports following meta-keys:
  Ctrl + (a key from: abcdefklnpuw)
  Alt  + (a key from: bf)
Please refer to shell documentation for more details.

Available commands:
  clear    : Clear screen.
  device   : Device commands
  devmem   : Read/write physical memory
             Usage:
             Read memory at address with optional width:
             devmem <address> [<width>]
             Write memory at address with mandatory width and value:
             devmem <address> <width> <value>
  gpio     : GPIO commands
  help     : Prints the help message.
  history  : Command history.
  kernel   : Kernel commands
  ot       : OpenThread subcommands
             Use "ot help" to get the list of subcommands
  rem      : Ignore lines beginning with 'rem '
  resize   : Console gets terminal screen size or assumes default in case the
             readout fails. It must be executed after each terminal width change
             to ensure correct text display.
  retval   : Print return value of most recent command
  shell    : Useful, not Unix-like shell commands.
uart:~$
```

`microcom` can be exited pressing ctrl+x.

> Note: The MCU may be kept in reset by GPIO1\_IO5 of the Host. Release it if needed: `gpioset -c /dev/gpiochip0 5=1`

<a id="recovery-after-bad-programming"></a>

## Recovery after bad programming

It is possible to get the mcu into a locked state where openocd reports an “unknown” state, see lines 13 following:

```
root@solidsense-n8:~# openocd -f /etc/openocd.cfg 
Open On-Chip Debugger 0.12.0+dev-00150-g91bd43134-dirty (2025-04-07-18:10)
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
imx_gpio GPIO nums: swclk = 14, swdio = 15
Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
Info : imx_gpio GPIO JTAG/SWD bitbang driver
Info : imx_gpio mmap: pagesize: 4096, regionsize: 131072
Info : clock speed 1000 kHz
Info : SWD DPIDR 0x2ba01477
Error: [nrf52.cpu] Could not find MEM-AP to control the core
****** WARNING ******
nRF52 device has AP lock engaged (see UICR APPROTECT register).
Debug access is denied.
Use 'nrf52_recover' to erase and unlock the device.

Warn : target nrf52.cpu examination failed
Info : starting gdb server for nrf52.cpu on 3333
Info : Listening on port 3333 for gdb connections
```

Recovery from this state is possible by `nrf52_recover` command:

```
Open On-Chip Debugger
> targets
    TargetName         Type       Endian TapName            State       
--  ------------------ ---------- ------ ------------------ ------------
 0* nrf52.cpu          cortex_m   little nrf52.cpu          unknown
> nrf52_recover
Waiting for chip erase...
nrf52.cpu device has been successfully erased and unlocked.
[nrf52.cpu] Cortex-M4 r0p1 processor detected
[nrf52.cpu] target has 6 breakpoints, 4 watchpoints
[nrf52.cpu] clearing lockup after double fault
Polling target nrf52.cpu failed, trying to reexamine
[nrf52.cpu] Cortex-M4 r0p1 processor detected
[nrf52.cpu] target has 6 breakpoints, 4 watchpoints
> targets
    TargetName         Type       Endian TapName            State       
--  ------------------ ---------- ------ ------------------ ------------
 0* nrf52.cpu          cortex_m   little nrf52.cpu          halted
> nrf5 mass_erase
nRF52833-xxAA(build code: A0) 512kB Flash, 128kB RAM
Mass erase completed.
> exit
```