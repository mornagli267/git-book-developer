# SPI from Linux with spidev

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 24 Feb 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Introduction](#introduction)<br>- [SPI hardware tests (loopback MOSI / MISO)](#spi-hardware-tests-loopback-mosi-miso)<br>- [DT and kernel configuration](#dt-and-kernel-configuration)<br>- [SPI unitary tests using spidev\_test](#spi-unitary-tests-using-spidev_test)<br>  - [Source code](#source-code)<br>  - [List of spidev options](#list-of-spidev-options)<br>  - [Example of 32-byte transfer in Full-duplex with loopback](#example-of-32-byte-transfer-in-full-duplex-with-loopback) |     |     |

<a id="introduction"></a>

## Introduction

Linux® SPI framework offers several ways to access SPI peripherals. Among them, the spidev framework enables to easily control an SPI peripheral straight from Linux® user space. The following provides a guide for testing the SPI bus with spidev.

<a id="spi-hardware-tests-loopback-mosi-miso"></a>

## SPI hardware tests (loopback MOSI / MISO)

Short-circuit the SPI bus MISO and MOSI lines to create a loopback enables the bus to receive the same data it is sending. This is an interesting solution to quickly perform basic tests as well as performance tests.

**Attached here the MikroBus schematics:**

![](./attachments/image-20220227-142813.png)

> [!NOTE]
> **Note:**
> To be able to control the SPI1 device, the DT must be customized accordingly. See the above schematics to get the SPI1 Som side Pad Names.

<a id="dt-and-kernel-configuration"></a>

## DT and kernel configuration

In our example of MOSI/MISO loopback, the DT must be customized as follows:

- Activate the SPI controller by setting its status to *okay*.
- Add a spidev child node.
  - Enable spidev by adding a compatible *spidev*.
  - Add a **reg** property, required for the SPI framework but not meaningful in this case since chip select is not defined and loopback is used.
  - Configure the bus speed for SPI communications by setting the **spi-max-frequency** property.

```
&spi4 {
    pinctrl-names = "default", "sleep";
    pinctrl-0 = <&spi4_pins_a>;
    pinctrl-1 = <&spi4_sleep_pins_a>;
    status = "okay";
 
    spidev@0{
        compatible = "spidev";
        reg = <0>;
        spi-max-frequency = <4000000>;
    };
}
```

<a id="spi-unitary-tests-using-spidev_test"></a>

## SPI unitary tests using spidev\_test

spidev\_test, available within the Linux® kernel, is a test tool enabling to perform tests via the spidev interface.

<a id="source-code"></a>

### **Source code**

The Linux® kernel spidev\_test tool source code can be found under tools/spi\[2\] directory:

- [tools/spi/spidev\_test.c](https://github.com/STMicroelectronics/linux/blob/v5.10-stm32mp/tools/spi/spidev_test.c)

<a id="list-of-spidev-options"></a>

### List of spidev options

The spidev\_test tool has the following options:

```
Usage: spidev_test [-DsbdlHOLC3vpNR24SI]
  -D --device   device to use (default /dev/spidev1.1)
  -s --speed    max speed (Hz)
  -d --delay    delay (usec)
  -b --bpw      bits per word
  -i --input    input data from a file (e.g. "test.bin")
  -o --output   output data to a file (e.g. "results.bin")
  -l --loop     loopback
  -H --cpha     clock phase
  -O --cpol     clock polarity
  -L --lsb      least significant bit first
  -C --cs-high  chip select active high
  -3 --3wire    SI/SO signals shared
  -v --verbose  Verbose (show tx buffer)
  -p            Send data (e.g. "1234\xde\xad")
  -N --no-cs    no chip select
  -R --ready    slave pulls low to pause
  -2 --dual     dual transfer
  -4 --quad     quad transfer
  -8 --octal    octal transfer
  -S --size     transfer size
  -I --iter     iterations
```

<a id="example-of-32-byte-transfer-in-full-duplex-with-loopback"></a>

### Example of 32-byte transfer in Full-duplex with loopback

```
root@imx8mpsolidrun:~# spidev_test -D /dev/spidev1.0 -v
spi mode: 0x4
bits per word: 8
max speed: 500000 Hz (500 kHz)
TX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.... .................. .
RX | FF FF FF FF FF FF 40 00 00 00 00 95 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF F0 0D  | ......@.... .................. .
```

- To make sure you can detect your SPI devices, use the following:

```
ls /dev/spi*
```

Two available SPI devices are detected:

![](./attachments/image-20220227-140328.png)