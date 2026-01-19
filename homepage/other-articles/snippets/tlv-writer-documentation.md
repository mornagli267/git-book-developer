# TLV Writer Documentation

***

## **Table of Contents**

* [Table of Contents](tlv-writer-documentation.md#table-of-contents)
  * [where to get](tlv-writer-documentation.md#where-to-get)
  * [Overview](tlv-writer-documentation.md#overview)
* [Dependencies](tlv-writer-documentation.md#dependencies)
* [Usage](tlv-writer-documentation.md#usage)
  * [Arguments](tlv-writer-documentation.md#arguments)
  * [Example Usage](tlv-writer-documentation.md#example-usage)
  * [Finding the I2C Bus Number](tlv-writer-documentation.md#finding-the-i2c-bus-number)
* [Supported TLV Keys](tlv-writer-documentation.md#supported-tlv-keys)
  * [System Information (SMBIOS Type 1)](tlv-writer-documentation.md#system-information-smbios-type-1)
  * [NIO Information (SMBIOS Type 2)](tlv-writer-documentation.md#nio-information-smbios-type-2)
  * [Chassis Information (SMBIOS Type 3)](tlv-writer-documentation.md#chassis-information-smbios-type-3)
* [Error Handling](tlv-writer-documentation.md#error-handling)
  * [Possible Errors](tlv-writer-documentation.md#possible-errors)

***

### where to get

[https://github.com/SolidRun/PyTLVWriter](https://github.com/SolidRun/PyTLVWriter)

### **Overview**

This script writes **TLV (Type-Length-Value)** structured data into an **I2C EEPROM**. It supports a variety of system-specific keys that define metadata for the device.

The script:

* Builds **TLV-formatted** payloads.
* Writes the data into an **EEPROM via I2C**.
* Supports **custom-defined keys**.
* Calculates and appends a **CRC checksum** to ensure data integrity.

***

## Dependencies

To ensure all required dependencies are installed, run:

```
sudo apt update
sudo apt install python3 python3-smbus
```

this will:

* Install Python 3 if it is not already installed.
* Install smbus for I2C communication.

***

## **Usage**

```
python3 TLV_write.py <i2c_bus> <eeprom_address> [--yes] [-b] <key> <value> <key> <value> ...
```

### **Arguments**

| **Argument**                  | **Description**                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| i2c\_bus                      | The I2C bus number.                                                                                                                     |
| eeprom\_address               | The EEPROM address (hex or decimal).                                                                                                    |
| <p>--yes<br>-y<br>--force</p> | Automatically confirms the operation (skips user confirmation).                                                                         |
| -b                            | Writes the TLV data to a binary file (`/tmp/eeprom_tlv.bin`) without writing to the EEPROM. You can later write it manually using `dd`. |
|                               | One or more key-value pairs to write to EEPROM.                                                                                         |

### **Example Usage**

For example if we want the following data to appear in DMI:

```
Handle 0xXXXX, DMI type 1, XX bytes
System Information
	Manufacturer: XXXXX
	Product Name: MySystem
	Version: 1.0
	Serial Number: XXXXXX
	UUID: XXXXXX-XXXXX-XXXXX-XXXXX-XXXXX
	Wake-up Type: XXXXXXXXXXXX
	SKU Number: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	Family: XXXXXXXXXXXXXXXXXXXXXXX
```

We want to run the following command (Note that bus 3 address 0X50 is used in this example):

```
python3 TLVwriter.py 3 0x50 TLV_CODE_SYS_NAME "MySystem" TLV_CODE_SYS_VERSION "1.0"
```

{% hint style="info" %}
**eeprom example for this :**
```
python3 TLVwriter.py 3 0x50 TLV_CODE_SYS_NAME "EmbeddedDevice" \
TLV_CODE_SYS_SKU "ED-2024" \
TLV_CODE_SYS_SERIAL_NUMBER "SN123456789" \
TLV_CODE_SYS_VERSION "01.02" \
TLV_CODE_FAMILY "Industrial" \
TLV_CODE_MANUF_NAME "Solid-Run" \
TLV_CODE_MANUF_DATE "2024-03-11" \
TLV_CODE_PLATFORM_NAME "Bedrock-IPC"
```
00: 54 6c 76 49 6e 66 6f 00 01 65 00 30 0e 45 6d 62 TlvInfo.?e.0?Emb\
10: 65 64 64 65 64 44 65 76 69 63 65 31 07 45 44 2d eddedDevice1?ED-\
20: 32 30 32 34 32 0b 53 4e 31 32 33 34 35 36 37 38 20242?SN12345678\
30: 39 33 05 30 31 2E 30 32 20 0a 49 6e 64 75 73 74 93?01.02 ?Indust\
40: 72 69 61 6c 25 09 73 6f 6c 69 64 2d 72 75 6e 23 rial%.solid-run#\
50: 0a 32 30 32 34 2d 30 33 2d 31 31 24 0b 42 65 64 .2024-03-11$.Bed\
60: 72 6f 63 6b 2d 49 50 43 fe 04 6e 7e c0 fd 00 00 rock-IPC??n\~??\
70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................\
80: …… header version Total Payload Length (little endian) Type Length Value crc checksum TLV
{% endhint %}


{% hint style="info" %}
#### **Finding the I2C Bus Number**
To determine the correct I2C bus number, run the following command:
```
sudo i2cdetect -y 1
```
If no EEPROM device is found, repeat the command with different bus numbers (e.g., 3, 4, 5 etc.) until you detect an address 0x50 or 0x56. Once found, use the corresponding bus number in the script. **Example:**
```
sudo i2cdetect -y 3
```
If the output shows:
```
0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: 50 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
```
Then bus 3 and address 0x50 should be used in the script.
{% endhint %}


{% hint style="warning" %}
Bus 2 or 5 usually has the memory SPD on addresses 0x50 & 0x51, **do not write to them!**
{% endhint %}


***

## **Supported TLV Keys**

Each TLV Key has a Hex Code, Max Length, and belongs to a DMIDecode Type.

### **System Information (SMBIOS Type 1)**

|                                |                        |                                                   |
| ------------------------------ | ---------------------- | ------------------------------------------------- |
| **TLV Key**                    | **Max Length (bytes)** | **BIOS path**                                     |
| TLV\_CODE\_FAMILY              | 20                     | -                                                 |
| TLV\_CODE\_MANUF\_DATE         | 10                     | -                                                 |
| TLV\_CODE\_PLATFORM\_NAME      | 20                     | -                                                 |
| TLV\_CODE\_MANUF\_NAME         | 20                     | -                                                 |
| TLV\_CODE\_VENDOR\_NAME        | 20                     | -                                                 |
| TLV\_CODE\_SYS\_NAME           | 20                     | Main → Detailed Configuration Information → Model |
| TLV\_CODE\_SYS\_SKU            | 20                     | Main screen                                       |
| TLV\_CODE\_SYS\_SERIAL\_NUMBER | 24                     | Main screen                                       |
| TLV\_CODE\_SYS\_VERSION        | 5                      | -                                                 |

### **NIO Information (SMBIOS Type 2)**

|                                |                        |
| ------------------------------ | ---------------------- |
| **TLV Key**                    | **Max Length (bytes)** |
| TLV\_CODE\_NIO\_NAME           | 20                     |
| TLV\_CODE\_NIO\_SERIAL\_NUMBER | 24                     |
| TLV\_CODE\_NIO\_VERSION        | 5                      |

### **Chassis Information (SMBIOS Type 3)**

|                                |                        |
| ------------------------------ | ---------------------- |
| **TLV Key**                    | **Max Length (bytes)** |
| TLV\_CODE\_CHS\_SERIAL\_NUMBER | 24                     |
| TLV\_CODE\_CHS\_VERSION        | 5                      |

|                         |                        |                                                                  |
| ----------------------- | ---------------------- | ---------------------------------------------------------------- |
| **TLV Key**             | **Max Length (bytes)** | **BIOS path**                                                    |
| TLV\_CODE\_CONFIG\_CODE | 200                    | Main → Detailed Configuration Information → Configuration String |

***

## **Error Handling**

If invalid input is provided, the script will:

* Print an **error message**.
* **Exit** without modifying EEPROM contents.

### **Possible Errors**

|                                                        |                                                |
| ------------------------------------------------------ | ---------------------------------------------- |
| **Error Message**                                      | **Cause**                                      |
| `Error: Unknown key`                                   | Provided TLV key is not in the supported list. |
| `Error: Value for key 'X' is too long`                 | Input exceeds the maximum allowed length.      |
| `Error: MAC address must have 6 parts`                 | Incorrect MAC format.                          |
| `Error: I2C write error`                               | I2C communication issue during EEPROM write.   |
| `Error: Total TLV data length exceeds EEPROM capacity` | Data is too large for EEPROM storage.          |

***
