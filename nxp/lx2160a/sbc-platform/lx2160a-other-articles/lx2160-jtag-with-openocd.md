# LX2160 JTAG with OpenOCD

The LX2160A SoC features a standard ARM CoreSight Debug Interfaces, which can be used with OpenOCD and generic debug probes in place of NXP's own CodeWarrior Tap and Software.

A range of quirks are needed to accomplish this, most of which deserves thanks to the general community.

## SolidRun Boards JTAG Connectors

- [LX2160A CEX-7 JTAG](lx2160a-cex-7-jtag.md)
- [LX2162A SoM JTAG](../../../lx2162a/sbc-platform/lx2162a-other-articles/lx2162a-som-jtag.md)

## JTAG Adapters

General purpose JTAG Adapters should be usable, this section lists those that were actually tested.

### J-Link

SEGGER J-Link can connect to SolidRun LX2160 & LX2162 boards by using any of two adapters:

- [50mm 10-Pin Patch Adapter](https://www.segger.com/products/debug-probes/j-link/accessories/adapters/segger-50-mil-10-pin-patch-adapter/)
- [9-Pin Cortex-M Adapter](https://www.segger.com/products/debug-probes/j-link/accessories/adapters/9-pin-cortex-m-adapter/)

See the [OpenOCD Configuration File](#openocd-configuration-file) section below for connecting to an LX2160 board with OpenOCD and J-Link.

On Linux this is as simple as:

```
sudo openocd -f openocd_jlink_lx2160a.cfg
```

On Windows the WinUSB driver may be necessary, see [SEGGER Documentation](https://kb.segger.com/OpenOCD) for details.

## Enable Debugging Fused (Secure-Boot) SoCs

If LX2160/LX2162 eFuses were blown to enable secure boot, debugging through JTAG is disabled by default.

This can be overridden by setting SDBGEN bit in RCW to `1`, requiring installation of a special signed debug image. See [this patch](https://github.com/SolidRun/lx2160a_build/blob/8d9a0054661f39002463ea14bba55a9f69dfb200/patches/rcw/0023-add-explicit-setting-for-SDBGEN-disabled-by-default.patch) for pointers on where this bit can be set.

## Halt Cortex-A72 Core 0

Once connected to the OpenOCD command-line (telnet), the core can be stopped by a set of direct commands sent to the DAP. At the time of writing the "halt" command did not operate as intended:

```
poll off
lx2160a.dap apreg 0 0 0x23000002
lx2160a.dap apreg 0 4 0x01010310
lx2160a.dap apreg 0 0xc 0x00000009
lx2160a.dap apreg 0 4 0x01010FB0
lx2160a.dap apreg 0 0xc 0xC5ACCE55
lx2160a.dap apreg 0 4 0x01010300
lx2160a.dap apreg 0 0xc 0x00000000
lx2160a.dap apreg 0 4 0x01010088
lx2160a.dap apreg 0 0xc 0x00004000

lx2160a.dap apreg 0 4 0x01020FB0
lx2160a.dap apreg 0 0xc 0xC5ACCE55
lx2160a.dap apreg 0 4 0x01020000
lx2160a.dap apreg 0 0xc 0x00000001

lx2160a.dap apreg 0 4 0x010200A0
lx2160a.dap apreg 0 0xc 0x00000001
lx2160a.dap apreg 0 4 0x0102001C
lx2160a.dap apreg 0 0xc 0x00000001

lx2160a.dap apreg 0 4 0x01010088
lx2160a.dap apreg 0 0xc
```

The final command should print a value similar to `0x03007f13`. Here the least significant bit indicates whether the core is halted (bit set), or still running (bit cleared).

Now automatic control of dap can be re-activated:

```
poll on
```

```
lx2160a.cpu0 cluster 0 core 0 multi core
lx2160a.cpu0 halted in AArch64 state due to debug-request, current mode: EL3H
cpsr: 0x800003cd pc: 0x1800d000
MMU: disabled, D-Cache: disabled, I-Cache: enabled
```

OpenOCD has detected the halted state, and other commands may be used to inspect all state, e.g. to print all registers:

```
reg
```

Or to print memory at the program counter to find where execution halted:

```
mdw [dict get [get_reg pc] pc] 4
```

```
0x1800d000: 14000000 aa0003f4 aa0103f5 aa0203f6
```

Here it was halted at an infinite loop, a branch with offset 0.

**Note: The halt sequence above has been included in the example OpenOCD config file below as `lx2160_halt_core0` command.**

## References

- [OpenOCD Patches implementing LX2160 Quirks (abandoned)](https://review.openocd.org/c/openocd/+/6624)

## OpenOCD Configuration File

Example OpenOCD configuration file for connecting to an LX2160 board with J-Link (`openocd_jlink_lx2160a.cfg`):

```tcl
# SPDX-License-Identifier: GPL-2.0-or-later

# 1. Hardware Interface: SEGGER J-Link
source [find interface/jlink.cfg]
transport select jtag
adapter speed 4000

# BEGIN target/lx2160a.cfg
# This block was copied from openocd gerrit,
# originally submitted by David Lamparter:
# https://review.openocd.org/c/openocd/+/6624
if { [info exists CHIPNAME] } {
	set _CHIPNAME $CHIPNAME
} else {
	set _CHIPNAME lx2160a
}

if { [info exists NUMCORES] } {
	set _NUMCORES $NUMCORES
} else {
	set _NUMCORES 16
}

if { [info exists DAP_TAPID] } {
	set _DAP_TAPID $DAP_TAPID
} else {
	set _DAP_TAPID 0x6ba00477
}

jtag newtap $_CHIPNAME dap -irlen 4 -expected-id $_DAP_TAPID
dap create $_CHIPNAME.dap -chain-position $_CHIPNAME.dap

set _TARGETNAME $_CHIPNAME.cpu
set _smp "target smp"

# implementation has 2 cores in each core complex
for {set cc 0} {$cc < $_NUMCORES / 2} {incr cc} {
	set core0 [format %x [expr {$cc * 2 + 0}]]
	set core1 [format %x [expr {$cc * 2 + 1}]]

	cti    create $_CHIPNAME.cti.$core0         -dap $_CHIPNAME.dap -ap-num 0 -baseaddr [expr {0x1020000 + $cc * 0x400000}]
	target create $_CHIPNAME.cpu.$core0 aarch64 -dap $_CHIPNAME.dap -ap-num 0 -dbgbase  [expr {0x1010000 + $cc * 0x400000}] -cti $_CHIPNAME.cti.$core0
	cti    create $_CHIPNAME.cti.$core1         -dap $_CHIPNAME.dap -ap-num 0 -baseaddr [expr {0x1120000 + $cc * 0x400000}]
	target create $_CHIPNAME.cpu.$core1 aarch64 -dap $_CHIPNAME.dap -ap-num 0 -dbgbase  [expr {0x1110000 + $cc * 0x400000}] -cti $_CHIPNAME.cti.$core1

	set _smp "$_smp $_CHIPNAME.cpu.$core0 $_CHIPNAME.cpu.$core1"

	unset core0
	unset core1
}

eval $_smp
targets lx2160a.cpu.0

# datasheet value, tested @ 15MHz
adapter speed 25000
# END target/lx2160a.cfg

# custom halt script by direct dap commands
# Copyright 2026 Josua Mayer <josua@solid-run.com>
proc lx2160_halt_core0 {} {
    # stop background polling preventing bus collisions
    poll off

    # set CSW
    lx2160a.dap apreg 0 0 0x23000002
    lx2160a.dap apreg 0 4 0x01010310
    lx2160a.dap apreg 0 0xc 0x00000009

    # unlock LAR & OSLAR
    lx2160a.dap apreg 0 4 0x01010FB0
    lx2160a.dap apreg 0 0xc 0xC5ACCE55
    lx2160a.dap apreg 0 4 0x01010300
    lx2160a.dap apreg 0 0xc 0x00000000

    # set HDE
    lx2160a.dap apreg 0 4 0x01010088
    lx2160a.dap apreg 0 0xc 0x00004000

    # unlock cti
    lx2160a.dap apreg 0 4 0x01020FB0
    lx2160a.dap apreg 0 0xc 0xC5ACCE55
    lx2160a.dap apreg 0 4 0x01020000
    lx2160a.dap apreg 0 0xc 0x00000001

    # route cti pulse
    lx2160a.dap apreg 0 4 0x010200A0
    lx2160a.dap apreg 0 0xc 0x00000001
    lx2160a.dap apreg 0 4 0x0102001C
    lx2160a.dap apreg 0 0xc 0x00000001

    # verify halt state in EDSCR
    lx2160a.dap apreg 0 4 0x01010088
    set edscr [lx2160a.dap apreg 0 0xc]
    if {[expr {$edscr & 0x1}] == 0} {
        echo [format "ERROR: Core 0 failed to halt! (EDSCR = 0x%08X)" $edscr]
    }

    # continue background polling
    poll on
}
```
