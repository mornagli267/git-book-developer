# Enabling Quectel EM05-G LTE Modem R7000

<a id="introduction"></a>

## Introduction

This documentation provides a comprehensive guide on enabling the Quectel EM05-G LTE Modem.  
With this guide, users can seamlessly set up the modem in their environment.

<a id="prerequisites"></a>

## Prerequisites

- Hardware requirements: Bedrock V3000 with Quectel EM05-G Modem
- Software requirements: Linux Environment

<a id="configuration"></a>

## Configuration

- Boot into your Linux environmment
- Run the following Commands:

```
modprobe option
echo "2c7c 030e" > /sys/bus/usb-serial/drivers/option1/new_id
modprobe cdc_mbim
```

- It might take a few seconds for the Modem and required services to start working

<a id="testing-and-verification"></a>

## Testing and Verification

- Run:

```
mmcli -L
```

- This will list Your modem, Example:

```
/org/freedesktop/ModemManager1/Modem/0 [Quectel] Quectel EM05-G
```

<a id="references"></a>

## References

1. [Quectel Official Website](http://www.example.com/)
2. [EM05-G AT-commands](https://forums.quectel.com/uploads/short-url/cBnrTmjnCg7OGnqRsk8dIpbHuVX.pdf)