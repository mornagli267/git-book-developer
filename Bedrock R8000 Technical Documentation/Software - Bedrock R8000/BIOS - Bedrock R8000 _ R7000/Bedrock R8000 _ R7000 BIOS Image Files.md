---
tags:
  - '#bios'
  - '#bedrock-r8000'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [BIOS - Bedrock R8000 | R7000](../BIOS%20-%20Bedrock%20R8000%20_%20R7000.md)

# Bedrock R8000 | R7000 BIOS Image Files

> [!NOTE]
> Please follow [BIOS Update procedure](../../../Bedrock%20V3000%20Technical%20Documentation/Software%20-%20Bedrock%20V3000/BIOS%20-%20Bedrock%20V3000/BIOS%20Update%20procedure.md) carefully.
>
> Incorrect BIOS update might lead to BIOS corruption that cannot be recovered and would require an RMA.

> [!IMPORTANT]
> Before updating BIOS, you are advised to [Bedrock V3000 BIOS Settings](../../../Bedrock%20V3000%20Technical%20Documentation/Software%20-%20Bedrock%20V3000/BIOS%20-%20Bedrock%20V3000/Bedrock%20V3000%20BIOS%20Settings.md)

## **Table fo contents:**

# Current BIOS version

> [!TIP]
> Recommended version

## BIOS V1.06 Release for Bedrock R8000 | R7000

| **BIOS for Ryzen HS CPUs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **BIOS for Ryzen U CPUs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **File name**: BIOS\_BDR7K\_V1\_06\_FOR\_HS\_CPUS.rom.gz <br/> **Release date**: 26-NOV-2025 <br/> **MD5:** bd32ff694210ba22ea024bf617d71758 <br/> [BIOS_BDR7K_V1_06_FOR_HS_CPUS.rom.gz](../../../../../attachments/201fd734-ba42-439a-abc3-0433cd65d8c2.gz) <br/>  <br/> **To be used with**: <br/><ul local-id="92d34bd2-ae79-469d-9589-628568addd2d"><li local-id="cd05d13a-dce6-4072-8f26-b8cf15a4913f"><p local-id="c0f6dd54-2912-4380-b3c6-4bece4ed2520">Bedrock R7840HS</p></li><li local-id="f07f329d-b5d1-4691-8694-da7e18ca98e4"><p local-id="1a2a3b14-254f-4c9a-947b-3ad271afdb35">Bedrock R8845HS</p></li><li local-id="0ac2ca09-56fc-4e91-8b42-82fec19c0313"><p local-id="683cf322-ecf2-46d8-9f7b-56a7ecdb0484">Bedrock R8945HS</p></li></ul> | **File name**:  BIOS\_BDR7K\_V1\_06.rom.gz <br/> **Release date**: 26-NOV-2025 <br/> **MD5**: 7cce17d2e600fc8afa324ac635e23a22 <br/> [BIOS_BDR7K_V1_06.rom.gz](../../../../../attachments/ca7856dc-ebd6-4c14-8a42-42595ddb42cf.gz) <br/>  <br/> **To be used with**: <br/><ul local-id="02e0dbc0-44f7-4756-843c-d0f236e443d3"><li local-id="c612d79f-2262-466e-8025-8c14e2105fce"><p local-id="6198ff58-6adc-4508-9e19-269698d77ee1">Bedrock R7440U</p></li><li local-id="c04f11de-5b54-47c9-91d7-28fa0e2cd17b"><p local-id="64e11124-88cb-4fc9-8852-4b9723b3d1f6">Bedrock R7840U</p></li><li local-id="67167092-9de1-408c-95ca-8a3ba9c36110"><p local-id="5c10c1e4-d75b-4680-8bdd-305a9f01ef32">Bedrock R8840U</p></li></ul><br/>> [!WARNING] This BIOS for Ryzen U might **brick** Bedrock with Ryzen HS CPU and **require an RMA**. <br/> Update to [**BIOS for Ryzen HS CPUs**](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/530546703#BIOS-for-Ryzen-HS-CPUs) instead. <br/> [Bedrock R8000 | R7000 Errata](../../Bedrock%20R8000%20_%20R7000%20Errata.md) <br/> |

### Revision notes

- Enabled A/B recovery mechanism
- Enabled early ABL (AGESA boot loader) messages
- Fixed Power LED not working on NIO 4x25 rev 1.2
- Fixed AMD I2C Driver issue with checking transaction status
- Updated splash screen to R8000

  - In AFU use /L to update the LOGO ROM hole
- Fixed DMI information sometimes showing extra characters.

---

# Older BIOS versions

## BIOS V1.04 Release for Bedrock R8000 | R7000

| **BIOS for Ryzen HS CPUs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **BIOS for Ryzen U CPUs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **File name**: BIOS\_BDR7K\_V1\_04\_FOR\_HS\_CPUS.rom.gz <br/> **Release date**: 05-JUN-2025 <br/> **MD5:** adb7b3c78b708c91d869ca4d450d3188 <br/> [BIOS_BDR7K_V1_04_FOR_HS_CPUS.rom.gz](../../../../../attachments/40eef483-5e5c-4516-a295-b4a553a8e9a9.gz) <br/>  <br/> **To be used with**: <br/><ul local-id="5c30c7c6-20ec-470a-bcfc-9a68b0efccca"><li local-id="fdfc0feb-1078-4ed8-9cff-1fcc3181f5c2"><p local-id="bd816c9a-5d11-46c7-9dfa-cdd23e348097">Bedrock R7840HS</p></li><li local-id="8c10b5a2-0dff-4d73-b3b9-c5c769b207a7"><p local-id="ba9fa72b-f13a-4ebd-8708-43c1affd25bd">Bedrock R8845HS</p></li><li local-id="b3452b34-ca11-448a-98c5-2fd16ce90384"><p local-id="ea045f3f-c50d-4451-baa6-021a2225493b">Bedrock R8945HS</p></li></ul> | **File name**:  BIOS\_BDR7K\_V1\_04.rom.gz <br/> **Release date**: 05-JUN-2025 <br/> **MD5**: bd1a5669db871185c92d071008c5bfa3 <br/> [BIOS_BDR7K_V1_04.rom.gz](../../../../../attachments/53de0365-4922-426a-9312-5eb8518c8a54.gz) <br/> **To be used with**: <br/><ul local-id="f42892d3-e5b8-4368-96f4-71adfb0fa2cc"><li local-id="e3964c2a-59c6-4673-8bf2-719c65fc6fdb"><p local-id="c6a1fb72-67d6-4e1c-b983-b94fc424ce15">Bedrock R7440U</p></li><li local-id="9265354e-1b1e-4f7a-ae24-8bfb39ac10de"><p local-id="b8146112-4b63-4f4c-8465-e1adc155d405">Bedrock R7840U</p></li><li local-id="b904e35b-ae6d-48ac-86ef-d79fb5d6fe94"><p local-id="18b2b5af-5bf0-4cc8-a836-d4e71c7870f2">Bedrock R8840U</p></li></ul><br/>> [!WARNING] This BIOS for Ryzen U might **brick** Bedrock with Ryzen HS CPU and **require an RMA**. <br/> Update to [**BIOS for Ryzen HS CPUs**](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/530546703#BIOS-for-Ryzen-HS-CPUs) instead. <br/> [Bedrock R8000 | R7000 Errata](../../Bedrock%20R8000%20_%20R7000%20Errata.md) <br/> |

### Revision notes

- Fixed AMD I2C Driver issue where Busses were powering off and not visible in Linux
- Fixed Power Tab not showing

  - Fixed System Management Unit (SMU) in power tab not opening the SMU menu
- Added Automatic switching between Full size DisplayPort & USB-C Thunderbolt.
- Added option to change SMBIOS tables 1, 2 & 3 from on boardEEprom.

  - see: [TLV Writer Documentation](../../../../Other%20Articles/Snippets/TLV%20Writer%20Documentation.md)
- Added SMBIOS tables 8 & 9

## BIOS V1.01 Release for Bedrock R8000 | R7000

| **BIOS for Ryzen HS CPUs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **BIOS for Ryzen U CPUs**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **File name**: BIOS\_BDR7K\_REL\_V1\_1\_FOR\_HS\_CPUS.rom.gz <br/> **Release date**: 17-FEB-2025 <br/> **MD5:** db76f6434ed6fae258ef8b12beb01521 <br/> [BIOS_BDR7K_REL_V1_1_FOR_HS_CPUS.rom.gz](../../../../../attachments/6900a998-fa95-466f-9aea-4369a88ea878.gz) <br/> **To be used with**: <br/><ul local-id="36fa26d7-141f-4f4f-99ad-9af2c643c94f"><li local-id="d2a42929-d0de-4fa8-8f77-805b4823e247"><p local-id="45b9da5c-e13d-4254-bbbf-20dfa8f052eb">Bedrock R7840HS</p></li><li local-id="4311ab7f-c23d-4110-a4bb-673fef8cb341"><p local-id="12cfd4d3-f295-43c4-b563-0a005c88c0b6">Bedrock R8845HS</p></li><li local-id="29b9203b-a9b6-4a08-b194-65ff969a66e9"><p local-id="5fa7a661-150d-4b06-8b30-471d98ea44d1">Bedrock R8945HS</p></li></ul> | **File name**:  BIOS\_BDR7K\_REL\_V1\_1.rom.gz <br/> **Release date**: 17-FEB-2025 <br/> **MD5**: 9d03ef7a73220ee1ec38e8ff4c815c7c <br/> [BIOS_BDR7K_REL_V1_1.rom.gz](../../../../../attachments/6892b63e-fd82-4426-93b2-c1e410638e31.gz) <br/> **To be used with**: <br/><ul local-id="0dff5a7f-5d71-478f-970c-1a499f389bdb"><li local-id="b4654409-754d-4048-a0ba-1be898d9ba3b"><p local-id="ee209b2b-8bfa-4214-a965-937ca66d41d8">Bedrock R7440U</p></li><li local-id="55b4f948-b325-4810-82c8-7b16a4efad6c"><p local-id="86a213f5-0941-45b4-9cbb-d6422cddd338">Bedrock R7840U</p></li><li local-id="3fd8b918-ea93-4816-9b30-b0cf98086889"><p local-id="05ff89ce-dbf3-46a8-99f6-485ec7d88ade">Bedrock R8840U</p></li></ul><br/>> [!WARNING] This BIOS for Ryzen U might **brick** Bedrock with Ryzen HS CPU and **require an RMA**. <br/> Update to [**BIOS for Ryzen HS CPUs**](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/530546703#BIOS-for-Ryzen-HS-CPUs) instead. <br/> [Bedrock R8000 | R7000 Errata](../../Bedrock%20R8000%20_%20R7000%20Errata.md) <br/> |

### Revision notes

- Updated to new AGESA 1.2.0.0a
- Fixed 10G USB hot-plug issue under Linux
- Introduced support for USB-C Thunderbolt on NIO 4x25 (Can be [Switching between DisplayPort (USB-C Thunderbolt / Full-size DisplayPort )](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000/Switching%20between%20DisplayPort%20(USB-C%20Thunderbolt%20_%20Full-size%20DisplayPort%20).md))
- Fixed non-functional Full-size DisplayPort on NIO Basic (Can be [Switching between DisplayPort (USB-C Thunderbolt / Full-size DisplayPort )](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000/Switching%20between%20DisplayPort%20(USB-C%20Thunderbolt%20_%20Full-size%20DisplayPort%20).md))
- Disabled DRTM support which was breaking some Windows installations
- Default memory speed set as follows:

  - BIOS for Ryzen U: 4800MT/s (Can be [Setting DDR memory frequency on Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000/Setting%20DDR%20memory%20frequency%20on%20Bedrock%20R8000%20_%20R7000.md))
  - BIOS for Ryzen HS: 5600MT/s (Can be [Setting DDR memory frequency on Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000/Setting%20DDR%20memory%20frequency%20on%20Bedrock%20R8000%20_%20R7000.md))
- Added visual feedback on BIOS settings reset saved in SPI flash [Bedrock BIOS reset button](../../../../Other%20Articles/Snippets/Bedrock%20BIOS%20reset%20button.md)
- Fixed splash screen not showing up

## BIOS V33 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7K\_EV\_V33.signed

**Release date**: 12-JUN-2024

**MD5**: 60db00923bfab1ddcdc62292ff1c4746

[BIOS_BDR7K_EV_V33.signed](../../../../../attachments/53af2d07-8462-4e3d-a343-c9d2423490ea)

### Revision notes

- Fixed issue of [Bedrock Troubleshooting](../../../Bedrock%20Troubleshooting.md)
- Fixed issue where some USB devices were rebooting the system

## BIOS V30 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7K\_EV\_V30.signed

**Release date**: 09-APR-2024

**MD5**: e8952b3f53159f7c1e7c71c75d81f60a

[BIOS_BDR7K_EV_V30.signed](../../../../../attachments/f70de3aa-8e1e-46b9-aae7-fb9ad0aeff63)

### Known Issues

- Constant reboots when using HDMI on windows: [Bedrock Troubleshooting](../../../Bedrock%20Troubleshooting.md)
- System might reboot when accessing some USB devices

### Revision notes

- Updated to new AGESA v1.1.0.2c

## BIOS V29 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7000\_EVAL\_V29.signed

**Release date**: 26-MAR-2024

**MD5**: d4795bd80360de55c35645b5ea8dae0e

[BIOS_BDR7000_EVAL_V29.signed](../../../../../attachments/c740e4b6-5af9-4290-82a2-feabe849bd08)

### Known Issues

- Constant reboots when using HDMI on windows: [Bedrock Troubleshooting](../../../Bedrock%20Troubleshooting.md)
- System might reboot when accessing some USB devices

### Revision notes

- Disabled ASPM for all PCI devices

## BIOS V28 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7000\_EVAL\_V28.signed

**Release date**: 15-Feb-2024

**MD5**: f267cb0c0ef32ca1f447b5990c1cd7d6

[BIOS_BDR7000_EVAL_V28.signed](../../../../../attachments/7e7d67f3-a85a-424e-9108-56da8ca65cf9)

### Revision notes

- Fixed issue where power button ACPI event was not registered.
- Fixed ACPI error boot messages.

## BIOS V25 EVAL for Bedrock R8000 | R7000

**File name**: BIOS\_BDR7000\_EVAL\_V25.signed

**Release date**: 06-Jan-2024

**MD5**: 39d600bbf77ae02cdeee516c7f369a87

[BIOS_BDR7000_EVAL_V25.signed](../../../../../attachments/a6b4d899-f677-45ea-940c-84bf3fb46a6b)

### Revision notes

- Disabled DDR power down which greatly improved system stability.
- Disabled ASPM for wifi module.
