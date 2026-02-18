# iMX8MP EEPROM Programming - TLV

<a id="revisions-and-notes"></a>

## Revisions and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 11 Apr 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revisions and Notes](#revisions-and-notes)<br>- [Introduction](#introduction)<br>- [Carrier](#carrier)<br>  - [Example](#example)<br>  - [Programming from U-Boot](#programming-from-u-boot)<br>- [SoM](#som)<br>  - [Example](#example)<br>  - [Programming from U-Boot](#programming-from-u-boot)<br>  - [Progammring MAC Address](#progammring-mac-address) |     |     |

<a id="introduction"></a>

## Introduction

Starting from April 01. 2022, the EEPROMs on Carriers, i.MX8M Plus SoMs are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. The data is structured according to the [ONIE TLV Standard](https://opencomputeproject.github.io/onie/design-spec/hw_requirements.html#board-eeprom-information-format).

<a id="carrier"></a>

## Carrier

The EEPROM on Clearfog Base and Pro on i2c-3 at 0x57 is programmed with the following TLV entries:

- TLV\_CODE\_PRODUCT\_NAME (mandatory) Human-readable name of the Product.
- TLV\_CODE\_PART\_NUMBER (mandatory) Identifying part number from ordering system (SKU) without BOM suffix (/0).
- TLV\_CODE\_SERIAL\_NUMBER (mandatory)
- TLV\_CODE\_MANUF\_DATE (mandatory) Manufacturing Date (MM/DD/YYYY HH:MM:SS)
- TLV\_CODE\_DEVICE\_VERSION (mandatory) Board Revision, incremented when parts or layout changes; MAJOR.MINOR revisions are encoded by storing MAJOR in the four most significant bits, MINOR in the four least significant bits.
- TLV\_CODE\_MANUF\_NAME (mandatory)
- TLV\_CODE\_MANUF\_COUNTRY (mandatory)
- TLV\_CODE\_VENDOR\_NAME (mandatory) Name of Vendor, typically SolidRun.
- TLV\_CODE\_VENDOR\_EXT (optional): This is a custom entry using the following structure:
  1. 4 byte IANA enterprise number in network byte order (we use 0xFFFFFFFF for now)
  2. 1 byte solidrun tlv code
  - SR\_TLV\_CODE\_KIT\_NUMBER (0x10): Identifying part number (SKU) when sold as a Kit.
  1. up to 250 byte of binary data

<a id="example"></a>

### Example

- TLV\_CODE\_PRODUCT\_NAME: HummingBoard Ripple
- TLV\_CODE\_PART\_NUMBER: SRHBCRE000CV25
- TLV\_CODE\_SERIAL\_NUMBER: NG01829212000006
- TLV\_CODE\_MANUF\_DATE: 12/24/2022 07:35:59
- TLV\_CODE\_DEVICE\_VERSION: 0x25 (2.5)
- TLV\_CODE\_MANUF\_NAME: IMI
- TLV\_CODE\_MANUF\_COUNTRY: PH
- TLV\_CODE\_VENDOR\_NAME: SolidRun
- TLV\_CODE\_VENDOR\_EXT: 0xFFFFFFFF 0x10 SRMP8QDW00D01GE008R02CH

<a id="programming-from-u-boot"></a>

### Programming from U-Boot

The EEPROM can be programmed from the U-Boot cli accordingly by the following commands:

```
tlv_eeprom dev 1
tlv_eeprom erase
tlv_eeprom set 0x21 'HummingBoard Ripple'
tlv_eeprom set 0x22 'SRHBCRE000CV25'
tlv_eeprom set 0x23 'NG01829212000006'
tlv_eeprom set 0x25 '12/24/2022 07:35:59'
tlv_eeprom set 0x26 '0x25'
tlv_eeprom set 0x2b 'IMI'
tlv_eeprom set 0x2c 'PH'
tlv_eeprom set 0x2d 'SolidRun'
tlv_eeprom set 0xfd '0xff 0xff 0xff 0xff 0x10 0x53 0x52 0x4d 0x50 0x38 0x51 0x44 0x57 0x30 0x30 0x44 0x30 0x31 0x47 0x45 0x30 0x30 0x38 0x52 0x30 0x32 0x43 0x48'
tlv_eeprom write

```

<a id="som"></a>

## SoM

The EEPROM on i.MX8M Plus SoMs on i2c-1 at 0x50 is programmed with the following TLV entries:

- TLV\_CODE\_PRODUCT\_NAME (mandatory) Human-readable name of the Product.
- TLV\_CODE\_PART\_NUMBER (mandatory) Identifying part number from ordering system (long SKU) without BOM suffix (/0).
- TLV\_CODE\_SERIAL\_NUMBER (mandatory)
- TLV\_CODE\_MAC\_BASE (optional) First MAC Address for the on-COM (SoC) network interface(s)
- TLV\_CODE\_MANUF\_DATE (mandatory) Manufacturing Date (MM/DD/YYYY HH:MM:SS)
- TLV\_CODE\_DEVICE\_VERSION (mandatory) Board Revision, incremented when parts or layout changes; MAJOR.MINOR revisions are encoded by storing MAJOR in the four most significant bits, MINOR in the four least significant bits.
- TLV\_CODE\_PLATFORM\_NAME Family name for the SoC.
- TLV\_CODE\_MAC\_SIZE (optional) Number of consecutive MAC Addresses starting from TLV\_CODE\_MAC\_BASE. Usually 1.
- TLV\_CODE\_MANUF\_NAME (mandatory)
- TLV\_CODE\_MANUF\_COUNTRY (mandatory)
- TLV\_CODE\_VENDOR\_NAME (mandatory) Name of Vendor, typically SolidRun.
- TLV\_CODE\_VENDOR\_EXT (optional): This is a custom entry using the following structure:
  1. 4 byte IANA enterprise number in network byte order (we use 0xFFFFFFFF for now)
  2. 1 byte solidrun tlv code
  - SR\_TLV\_CODE\_KIT\_NUMBER (0x10): Identifying part number (SKU) when sold as a Kit.
  1. up to 250 byte of binary data

<a id="example"></a>

### Example

- TLV\_CODE\_PRODUCT\_NAME: i.MX8M Plus System on Module
- TLV\_CODE\_PART\_NUMBER: S8DN18C11/1
- TLV\_CODE\_SERIAL\_NUMBER: NG01865214200061
- TLV\_CODE\_MANUF\_DATE: 12/24/2022 07:35:59
- TLV\_CODE\_DEVICE\_VERSION: 0x11 (1.1)
- TLV\_CODE\_PLATFORM\_NAME: i.MX8M Plus
- TLV\_CODE\_MANUF\_NAME: Nistec
- TLV\_CODE\_MANUF\_COUNTRY: IL
- TLV\_CODE\_VENDOR\_NAME: SolidRun
- TLV\_CODE\_VENDOR\_EXT: 0xFFFFFFFF 0x10 SRMP8QDW00D01GE008X01CE

<a id="programming-from-u-boot"></a>

### Programming from U-Boot

The EEPROM can be programmed from the U-Boot cli accordingly by the following commands:

```
tlv_eeprom dev 0
tlv_eeprom erase
tlv_eeprom set 0x21 'i.MX8M Plus System on Module'
tlv_eeprom set 0x22 'SRMP8QDW00D01GE008V12C0'
tlv_eeprom set 0x23 'NG01873214300067'
tlv_eeprom set 0x25 '12/24/2022 07:35:59'
tlv_eeprom set 0x26 '0x12'
tlv_eeprom set 0x28 'i.MX8M Plus'
tlv_eeprom set 0x2b 'Nistec'
tlv_eeprom set 0x2c 'IL'
tlv_eeprom set 0x2d 'SolidRun'
tlv_eeprom set 0x24 '12:34:56:78:9a:bc'
tlv_eeprom set 0x2a '1'
tlv_eeprom set 0xfd '0xff 0xff 0xff 0xff 0x10 0x53 0x52 0x4d 0x50 0x38 0x51 0x44 0x57 0x30 0x30 0x44 0x30 0x31 0x47 0x45 0x30 0x30 0x38 0x55 0x30 0x32 0x43 0x48' # HBp
tlv_eeprom set 0xfd '0xff 0xff 0xff 0xff 0x10 0x53 0x52 0x4d 0x50 0x38 0x51 0x44 0x57 0x30 0x30 0x44 0x30 0x31 0x47 0x45 0x30 0x30 0x38 0x58 0x30 0x30 0x43 0x45' # CBp
tlv_eeprom write
```

<a id="progammring-mac-address"></a>

### Progammring MAC Address

There are two options for storing MAC addresses on the i.MX8MP platform:

1. **Store the MAC address in OTP eFuses**
  - This is a **non-reversible action**, as the eFuse is permanently programmed.
2. **Store the MAC address in EEPROM using TLV format** (Recommended)
  - This method allows flexibility and is the preferred approach.

* * *

**Default Configuration**

- By default, the MAC address is stored in the SOM's TLV EEPROM.
- All SOMs are pre-flashed with SolidRun's default MAC address range in the TLV EEPROM.

* * *

**Custom MAC Address Option**

- There is an option to provide a custom MAC address range.
- SolidRun can program the custom MAC addresses into the TLV EEPROM upon request.

**Programming MAC Address in TLV Format**

- Using the following U-Boot commands:
```
#load eeprom
tlv_eeprom read
#set MAC address (example: 'D0:63:B4:06:1B:D4')
tlv_eeprom set 0x24 'd0:63:b4:06:1b:d4'
#set number of mac addresses (example 2 x MAC per unit)
tlv_eeprom set 0x2a 2
#save data on eeprom
tlv_eeprom write
```

- By default, the bootloader will automatically read the `TLV_MAC` value during initialization and apply it to the corresponding network interface.