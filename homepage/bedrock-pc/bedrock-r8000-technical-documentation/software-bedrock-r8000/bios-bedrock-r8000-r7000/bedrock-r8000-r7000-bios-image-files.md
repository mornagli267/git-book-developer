# Bedrock R8000 | R7000 BIOS Image Files

{% hint style="info" %}
Please follow [BIOS update procedure](../../../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/bios-bedrock-v3000/bios-update-procedure.md) carefully.
Incorrect BIOS update might lead to BIOS corruption that cannot be recovered and would require an RMA.
{% endhint %}


{% hint style="info" %}
Before updating BIOS, you are advised to [check current BIOS version](../../../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/bios-bedrock-v3000/bedrock-v3000-bios-settings.md#how-to-check-bios-version)
{% endhint %}


<a id="table-fo-contents"></a>

## **Table fo contents:**

<a id="current-bios-version"></a>

# Current BIOS version

{% hint style="success" %}
Recommended version
{% endhint %}


<a id="bios-v106-release-for-bedrock-r8000-r7000"></a>

## BIOS V1.06 Release for Bedrock R8000 | R7000

| <a id="bios-for-ryzen-hs-cpus"></a><br><br>## **BIOS for Ryzen HS CPUs** | <a id="bios-for-ryzen-u-cpus"></a><br><br>## **BIOS for Ryzen U CPUs** |
| --- | --- |
| **File name**:  <br>BIOS\_BDR7K\_V1\_06\_FOR\_HS\_CPUS.rom.gz<br><br>**Release date**: 26-NOV-2025<br><br>**MD5:** bd32ff694210ba22ea024bf617d71758<br><br>[BIOS_BDR7K_V1_06_FOR_HS_CPUS.rom.gz](./attachments/BIOS_BDR7K_V1_06_FOR_HS_CPUS.rom.gz)<br><br>**To be used with**:<br><br>- Bedrock R7840HS<br>- Bedrock R8845HS<br>- Bedrock R8945HS | **File name**:  <br>BIOS\_BDR7K\_V1\_06.rom.gz<br><br>**Release date**: 26-NOV-2025<br><br>**MD5**: 7cce17d2e600fc8afa324ac635e23a22<br><br>[BIOS_BDR7K_V1_06.rom.gz](./attachments/BIOS_BDR7K_V1_06.rom.gz)<br><br>**To be used with**:<br><br>- Bedrock R7440U<br>- Bedrock R7840U<br>- Bedrock R8840U<br><br>> [!WARNING]<br>> This BIOS for Ryzen U might **brick** Bedrock with Ryzen HS CPU and **require an RMA**.<br>> Update to [**BIOS for Ryzen HS CPUs**](/homepage/bedrock-pc/bedrock-r8000-technical-documentation/software-bedrock-r8000/bios-bedrock-r8000-r7000/bedrock-r8000-r7000-bios-image-files.md#bios-for-ryzen-hs-cpus) instead.<br>> [Learn more](../../../bedrock-r8000-technical-documentation/bedrock-r8000-r7000-errata.md#older-bedrock-with-ryzen-hs-do-not-support-ddr5-4800) |

<a id="revision-notes"></a>

### Revision notes

- Enabled A/B recovery mechanism
- Enabled early ABL (AGESA boot loader) messages
- Fixed Power LED not working on NIO 4x25 rev 1.2
- Fixed AMD I2C Driver issue with checking transaction status
- Updated splash screen to R8000
  - In AFU use /L to update the LOGO ROM hole
- Fixed DMI information sometimes showing extra characters.

* * *

<a id="older-bios-versions"></a>

# Older BIOS versions

<a id="bios-v104-release-for-bedrock-r8000-r7000"></a>

## BIOS V1.04 Release for Bedrock R8000 | R7000

| <a id="bios-for-ryzen-hs-cpus"></a><br><br>## **BIOS for Ryzen HS CPUs** | <a id="bios-for-ryzen-u-cpus"></a><br><br>## **BIOS for Ryzen U CPUs** |
| --- | --- |
| **File name**:  <br>BIOS\_BDR7K\_V1\_04\_FOR\_HS\_CPUS.rom.gz<br><br>**Release date**: 05-JUN-2025<br><br>**MD5:** adb7b3c78b708c91d869ca4d450d3188<br><br>[BIOS_BDR7K_V1_04_FOR_HS_CPUS.rom.gz](./attachments/BIOS_BDR7K_V1_04_FOR_HS_CPUS.rom.gz)<br><br>**To be used with**:<br><br>- Bedrock R7840HS<br>- Bedrock R8845HS<br>- Bedrock R8945HS | **File name**:  <br>BIOS\_BDR7K\_V1\_04.rom.gz<br><br>**Release date**: 05-JUN-2025<br><br>**MD5**: bd1a5669db871185c92d071008c5bfa3<br><br>[BIOS_BDR7K_V1_04.rom.gz](./attachments/BIOS_BDR7K_V1_04.rom.gz)<br><br>**To be used with**:<br><br>- Bedrock R7440U<br>- Bedrock R7840U<br>- Bedrock R8840U<br><br>> [!WARNING]<br>> This BIOS for Ryzen U might **brick** Bedrock with Ryzen HS CPU and **require an RMA**.<br>> Update to [**BIOS for Ryzen HS CPUs**](/homepage/bedrock-pc/bedrock-r8000-technical-documentation/software-bedrock-r8000/bios-bedrock-r8000-r7000/bedrock-r8000-r7000-bios-image-files.md#bios-for-ryzen-hs-cpus) instead.<br>> [Learn more](../../../bedrock-r8000-technical-documentation/bedrock-r8000-r7000-errata.md#older-bedrock-with-ryzen-hs-do-not-support-ddr5-4800) |

<a id="revision-notes"></a>

### Revision notes

- Fixed AMD I2C Driver issue where Busses were powering off and not visible in Linux
- Fixed Power Tab not showing
  - Fixed System Management Unit (SMU) in power tab not opening the SMU menu
- Added Automatic switching between Full size DisplayPort & USB-C Thunderbolt.
- Added option to change SMBIOS tables 1, 2 & 3 from on boardEEprom.
  - see: [TLV Writer Documentation](../../../../../homepage/other-articles/snippets/tlv-writer-documentation.md)
- Added SMBIOS tables 8 & 9

<a id="bios-v101-release-for-bedrock-r8000-r7000"></a>

## BIOS V1.01 Release for Bedrock R8000 | R7000

| <a id="bios-for-ryzen-hs-cpus"></a><br><br>## **BIOS for Ryzen HS CPUs** | <a id="bios-for-ryzen-u-cpus"></a><br><br>## **BIOS for Ryzen U CPUs** |
| --- | --- |
| **File name**:  <br>BIOS\_BDR7K\_REL\_V1\_1\_FOR\_HS\_CPUS.rom.gz<br><br>**Release date**: 17-FEB-2025<br><br>**MD5:** db76f6434ed6fae258ef8b12beb01521<br><br>[BIOS_BDR7K_REL_V1_1_FOR_HS_CPUS.rom.gz](./attachments/BIOS_BDR7K_REL_V1_1_FOR_HS_CPUS.rom.gz)<br><br>**To be used with**:<br><br>- Bedrock R7840HS<br>- Bedrock R8845HS<br>- Bedrock R8945HS | **File name**:  <br>BIOS\_BDR7K\_REL\_V1\_1.rom.gz<br><br>**Release date**: 17-FEB-2025<br><br>**MD5**: 9d03ef7a73220ee1ec38e8ff4c815c7c<br><br>[BIOS_BDR7K_REL_V1_1.rom.gz](./attachments/BIOS_BDR7K_REL_V1_1.rom.gz)<br><br>**To be used with**:<br><br>- Bedrock R7440U<br>- Bedrock R7840U<br>- Bedrock R8840U<br><br>> [!WARNING]<br>> This BIOS for Ryzen U might **brick** Bedrock with Ryzen HS CPU and **require an RMA**.<br>> Update to [**BIOS for Ryzen HS CPUs**](/homepage/bedrock-pc/bedrock-r8000-technical-documentation/software-bedrock-r8000/bios-bedrock-r8000-r7000/bedrock-r8000-r7000-bios-image-files.md#bios-for-ryzen-hs-cpus) instead.<br>> [Learn more](../../../bedrock-r8000-technical-documentation/bedrock-r8000-r7000-errata.md#older-bedrock-with-ryzen-hs-do-not-support-ddr5-4800) |

<a id="revision-notes"></a>

### Revision notes

- Updated to new AGESA 1.2.0.0a
- Fixed 10G USB hot-plug issue under Linux
- Introduced support for USB-C Thunderbolt on NIO 4x25 (Can be [changed in BIOS menu](../../software-bedrock-r8000/howto-guides-bedrock-r8000-r7000/switching-between-displayport-usb-c-thunderbolt-full-size-displayport.md))
- Fixed non-functional Full-size DisplayPort on NIO Basic (Can be [changed in BIOS menu](../../software-bedrock-r8000/howto-guides-bedrock-r8000-r7000/switching-between-displayport-usb-c-thunderbolt-full-size-displayport.md))
- Disabled DRTM support which was breaking some Windows installations
- Default memory speed set as follows:
  - BIOS for Ryzen U: 4800MT/s (Can be [changed in BIOS menu](../../software-bedrock-r8000/howto-guides-bedrock-r8000-r7000/setting-ddr-memory-frequency-on-bedrock-r8000-r7000.md))
  - BIOS for Ryzen HS: 5600MT/s (Can be [changed in BIOS menu](../../software-bedrock-r8000/howto-guides-bedrock-r8000-r7000/setting-ddr-memory-frequency-on-bedrock-r8000-r7000.md))
- Added visual feedback on BIOS settings reset saved in SPI flash [BIOS reset instructions](../../../../../homepage/other-articles/snippets/bedrock-bios-reset-button.md)
- Fixed splash screen not showing up

<a id="bios-v33-eval-for-bedrock-r8000-r7000"></a>

## BIOS V33 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7K\_EV\_V33.signed

**Release date**: 12-JUN-2024

**MD5**: 60db00923bfab1ddcdc62292ff1c4746

[BIOS_BDR7K_EV_V33.signed](./attachments/BIOS_BDR7K_EV_V33.signed)

<a id="revision-notes"></a>

### Revision notes

- Fixed issue of [connected HDMI leading to reboot](../../../../bedrock-pc/bedrock-troubleshooting.md#system-reboots-under-certain-conditions-while-hdmi-is-connected)
- Fixed issue where some USB devices were rebooting the system

<a id="bios-v30-eval-for-bedrock-r8000-r7000"></a>

## BIOS V30 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7K\_EV\_V30.signed

**Release date**: 09-APR-2024

**MD5**: e8952b3f53159f7c1e7c71c75d81f60a

[BIOS_BDR7K_EV_V30.signed](./attachments/BIOS_BDR7K_EV_V30.signed)

<a id="known-issues"></a>

### Known Issues

- Constant reboots when using HDMI on windows: [connected HDMI leading to reboot](../../../../bedrock-pc/bedrock-troubleshooting.md#system-reboots-under-certain-conditions-while-hdmi-is-connected)
- System might reboot when accessing some USB devices

<a id="revision-notes"></a>

### Revision notes

- Updated to new AGESA v1.1.0.2c

<a id="bios-v29-eval-for-bedrock-r8000-r7000"></a>

## BIOS V29 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7000\_EVAL\_V29.signed

**Release date**: 26-MAR-2024

**MD5**: d4795bd80360de55c35645b5ea8dae0e

[BIOS_BDR7000_EVAL_V29.signed](./attachments/BIOS_BDR7000_EVAL_V29.signed)

<a id="known-issues"></a>

### Known Issues

- Constant reboots when using HDMI on windows: [connected HDMI leading to reboot](../../../../bedrock-pc/bedrock-troubleshooting.md#system-reboots-under-certain-conditions-while-hdmi-is-connected)
- System might reboot when accessing some USB devices

<a id="revision-notes"></a>

### Revision notes

- Disabled ASPM for all PCI devices

<a id="bios-v28-eval-for-bedrock-r8000-r7000"></a>

## BIOS V28 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7000\_EVAL\_V28.signed

**Release date**: 15-Feb-2024

**MD5**: f267cb0c0ef32ca1f447b5990c1cd7d6

[BIOS_BDR7000_EVAL_V28.signed](./attachments/BIOS_BDR7000_EVAL_V28.signed)

<a id="revision-notes"></a>

### Revision notes

- Fixed issue where power button ACPI event was not registered.
- Fixed ACPI error boot messages.

<a id="bios-v25-eval-for-bedrock-r8000-r7000"></a>

## BIOS V25 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7000\_EVAL\_V25.signed

**Release date**: 06-Jan-2024

**MD5**: 39d600bbf77ae02cdeee516c7f369a87

[BIOS_BDR7000_EVAL_V25.signed](./attachments/BIOS_BDR7000_EVAL_V25.signed)

<a id="revision-notes"></a>

### Revision notes

- Disabled DDR power down which greatly improved system stability.
- Disabled ASPM for wifi module.