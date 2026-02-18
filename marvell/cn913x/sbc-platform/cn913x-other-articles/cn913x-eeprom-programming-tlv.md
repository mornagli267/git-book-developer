# CN913x EEPROM Programming - TLV

<a id="revisions-and-notes"></a>

## Revisions and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 03 Apr 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revisions and Notes](#revisions-and-notes)<br>- [Introduction](#introduction)<br>- [Carrier](#carrier)<br>  - [Example](#example)<br>  - [Programming from U-Boot](#programming-from-u-boot)<br>- [COM Express](#com-express)<br>  - [Example](#example)<br>  - [Programming from U-Boot](#programming-from-u-boot)<br>- [SoM](#som)<br>  - [Example](#example)<br>  - [Programming from U-Boot](#programming-from-u-boot) |     |     |

<a id="introduction"></a>

## Introduction

Starting from April 01. 2022, the EEPROMs on Carriers, SoMs and COM-Express Modules are being programmed with identifying information such as the product name and SKUs to allow for programmatic identification of hardware. The data is is structured according to the [ONIE TLV Standard](https://opencomputeproject.github.io/onie/design-spec/hw_requirements.html#board-eeprom-information-format).

<a id="carrier"></a>

## Carrier

The EEPROM on Clearfog Base and Pro on i2c-0 at 0x52 is programmed with the following TLV entries:

- TLV\_CODE\_PRODUCT\_NAME (mandatory) Human-readable name of the Product.
- TLV\_CODE\_PART\_NUMBER (mandatory) Identifying part number from ordering system (SKU) without BOM suffix (/0).
- TLV\_CODE\_SERIAL\_NUMBER (mandatory)
- TLV\_CODE\_MANUF\_DATE (mandatory) Manufacturing Date (MM/DD/YYYY HH:MM:SS)
- TLV\_CODE\_DEVICE\_VERSION (mandatory) Board Revision, incremented when parts or layout changes; MAJOR.MINOR revisions are encoded by storing MAJOR in the four most significant bits, MINOR in the four least significant bits.
- TLV\_CODE\_MANUF\_NAME (mandatory)
- TLV\_CODE\_MANUF\_COUNTRY (mandatory)
- TLV\_CODE\_VENDOR\_NAME (mandatory) Name of Vendor, typically SolidRun.

<a id="example"></a>

### Example

- TLV\_CODE\_PRODUCT\_NAME: Clearfog Base
- TLV\_CODE\_PART\_NUMBER: SRCFCB9130IV14
- TLV\_CODE\_SERIAL\_NUMBER: NG01725204200060
- TLV\_CODE\_MANUF\_DATE: 12/24/2022 07:35:59
- TLV\_CODE\_DEVICE\_VERSION: 0x14 (1.4)
- TLV\_CODE\_MANUF\_NAME: IMI
- TLV\_CODE\_MANUF\_COUNTRY: PH
- TLV\_CODE\_VENDOR\_NAME: SolidRun

<a id="programming-from-u-boot"></a>

### Programming from U-Boot

The EEPROM can be programmed from the U-Boot cli accordingly by the following commands:

```
tlv_eeprom dev 0
tlv_eeprom erase
tlv_eeprom set 0x21 'Clearfog Base'
tlv_eeprom set 0x22 'SRCFCB9130IV14'
tlv_eeprom set 0x23 'NG01725204200060'
tlv_eeprom set 0x25 '12/24/2022 07:35:59'
tlv_eeprom set 0x26 '0x14'
tlv_eeprom set 0x2b 'IMI'
tlv_eeprom set 0x2c 'PH'
tlv_eeprom set 0x2d 'SolidRun'
tlv_eeprom write

```

<a id="com-express"></a>

## COM Express

The EEPROM on CN913x CEX-7 Modules on i2c-0 at 0x50 is programmed with the following TLV entries:

- TLV\_CODE\_PRODUCT\_NAME (mandatory) Human-readable name of the Product.
- TLV\_CODE\_PART\_NUMBER (mandatory) Identifying part number from ordering system (SKU) without BOM suffix (/0).
- TLV\_CODE\_SERIAL\_NUMBER (mandatory)
- TLV\_CODE\_MAC\_BASE (optional) First MAC Address for the on-COM (SoC) network interface(s)
- TLV\_CODE\_MANUF\_DATE (mandatory) Manufacturing Date (MM/DD/YYYY HH:MM:SS)
- TLV\_CODE\_DEVICE\_VERSION (mandatory) Board Revision, incremented when parts or layout changes; MAJOR.MINOR revisions are encoded by storing MAJOR in the four most significant bits, MINOR in the four least significant bits.
- TLV\_CODE\_PLATFORM\_NAME Family name for the SoC.
- TLV\_CODE\_MAC\_SIZE (optional) Number of consecutive MAC Addresses starting from TLV\_CODE\_MAC\_BASE. Usually 1.
- TLV\_CODE\_MANUF\_NAME (mandatory)
- TLV\_CODE\_MANUF\_COUNTRY (mandatory)
- TLV\_CODE\_VENDOR\_NAME (mandatory) Name of Vendor, typically SolidRun.

<a id="example"></a>

### Example

- TLV\_CODE\_PRODUCT\_NAME: CN9132 COM Express 7 Module
- TLV\_CODE\_PART\_NUMBER: SRC9132S64D00GE008V12
- TLV\_CODE\_SERIAL\_NUMBER: NG01848213000015
- TLV\_CODE\_MANUF\_DATE: 12/24/2022 07:35:59
- TLV\_CODE\_DEVICE\_VERSION: 0x12 (1.2)
- TLV\_CODE\_PLATFORM\_NAME: Octeon TX2
- TLV\_CODE\_MANUF\_NAME: Nistec
- TLV\_CODE\_MANUF\_COUNTRY: IL
- TLV\_CODE\_VENDOR\_NAME: SolidRun

<a id="programming-from-u-boot"></a>

### Programming from U-Boot

The EEPROM can be programmed from the U-Boot cli accordingly by the following commands:

```
tlv_eeprom dev 0
tlv_eeprom erase
tlv_eeprom set 0x21 'CN9132 COM Express 7 Module'
tlv_eeprom set 0x22 'SRC9132S64D00GE008V12'
tlv_eeprom set 0x23 'NG01848213000015'
tlv_eeprom set 0x25 '12/24/2022 07:35:59'
tlv_eeprom set 0x26 '0x12'
tlv_eeprom set 0x28 'Octeon TX2'
tlv_eeprom set 0x2b 'IMI'
tlv_eeprom set 0x2c 'PH'
tlv_eeprom set 0x2d 'SolidRun'
tlv_eeprom write

```

<a id="som"></a>

## SoM

The EEPROM on CN913x SoMs on i2c-0 at 0x53 is programmed with the following TLV entries:

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

<a id="example"></a>

### Example

- TLV\_CODE\_PRODUCT\_NAME: CN9130 System on Module
- TLV\_CODE\_PART\_NUMBER: SRS9130S64D04GE008V11C0
- TLV\_CODE\_SERIAL\_NUMBER: NG01862214200020
- TLV\_CODE\_MANUF\_DATE: 12/24/2022 07:35:59
- TLV\_CODE\_DEVICE\_VERSION: 0x11 (1.1)
- TLV\_CODE\_PLATFORM\_NAME: Octeon TX2
- TLV\_CODE\_MANUF\_NAME: Nistec
- TLV\_CODE\_MANUF\_COUNTRY: IL
- TLV\_CODE\_VENDOR\_NAME: SolidRun

<a id="programming-from-u-boot"></a>

### Programming from U-Boot

The EEPROM can be programmed from the U-Boot cli accordingly by the following commands:

```
tlv_eeprom dev 1
tlv_eeprom erase
tlv_eeprom set 0x21 'CN9130 System on Module'
tlv_eeprom set 0x22 'SRS9130S64D04GE008V11C0'
tlv_eeprom set 0x23 'NG01862214200020'
tlv_eeprom set 0x25 '12/24/2022 07:35:59'
tlv_eeprom set 0x26 '0x11'
tlv_eeprom set 0x28 'Octeon TX2'
tlv_eeprom set 0x2b 'Nistec'
tlv_eeprom set 0x2c 'IL'
tlv_eeprom set 0x2d 'SolidRun'
tlv_eeprom write
```