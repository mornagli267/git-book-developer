---
tags:
  - '#bedrock-r8000'
  - '#howto'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [HowTo Guides - Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000.md)

# Enabling Quectel EM05-G LTE Modem R7000

## Introduction

This documentation provides a comprehensive guide on enabling the Quectel EM05-G LTE Modem.   
With this guide, users can seamlessly set up the modem in their environment.

## Prerequisites

- Hardware requirements: Bedrock V3000 with Quectel EM05-G Modem
- Software requirements: Linux Environment

## Configuration

- Boot into your Linux environmment
- Run the following Commands:

```java
modprobe option
echo "2c7c 030e" > /sys/bus/usb-serial/drivers/option1/new_id
modprobe cdc_mbim
```

- It might take a few seconds for the Modem and required services to start working

## Testing and Verification

- Run:

```java
mmcli -L
```

- This will list Your modem, Example:

```java
/org/freedesktop/ModemManager1/Modem/0 [Quectel] Quectel EM05-G
```

## References

1. [Quectel Official Website](http://www.example.com/)
2. [EM05-G AT-commands](https://forums.quectel.com/uploads/short-url/cBnrTmjnCg7OGnqRsk8dIpbHuVX.pdf)
