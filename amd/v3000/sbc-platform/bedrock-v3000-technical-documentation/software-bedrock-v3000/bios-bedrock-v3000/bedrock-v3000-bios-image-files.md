# Bedrock V3000 BIOS Image Files

{% hint style="info" %}
Please follow [BIOS update procedure](../bios-bedrock-v3000/bios-update-procedure.md) carefully.
Incorrect BIOS update might lead to BIOS corruption that cannot be recovered and would require an RMA.
{% endhint %}


{% hint style="info" %}
Before updating BIOS, you are advised to [check current BIOS version](/amd/v3000/sbc-platform/bedrock-v3000-technical-documentation/software-bedrock-v3000/bios-bedrock-v3000/bedrock-v3000-bios-image-files.md#how-to-check-bios-version)
{% endhint %}


<a id="current-bios-version"></a>

# Current BIOS version

<a id="bios-v103-release-for-bedrock-v3000"></a>

## BIOS V1.03 Release for Bedrock V3000

**File name**: BIOS\_BDV3000\_RELEASE\_V1.03\_SIGNED.BIN

**Release date**: 26-MAR-2024

**MD5**: 64ce5d561001dda950843c0af03af243

[BIOS_BDV3000_RELEASE_V1.03_SIGNED.BIN](./attachments/BIOS_BDV3000_RELEASE_V1.03_SIGNED.BIN)

<a id="revision-notes"></a>

### Revision notes

- Disable ASPM for all PCI devices

<a id="older-bios-versions"></a>

# Older BIOS versions

<a id="bios-v101-release-for-bedrock-v3000"></a>

## BIOS V1.01 Release for Bedrock V3000

**File name**: BIOS\_BDV3000\_RELEASE\_V1.01\_SIGNED.BIN

**Release date**: 15-Feb-2024

**MD5**: ee49a250859b8e36fe138efff553d746

[BIOS_BDV3000_RELEASE_V1.01_SIGNED.BIN](./attachments/BIOS_BDV3000_RELEASE_V1.01_SIGNED.BIN)

<a id="revision-notes"></a>

### Revision notes

- Fix V3000 CPUs boot failures with ECC memory

<a id="bios-v10-release-for-bedrock-v3000"></a>

## BIOS V1.0 Release for Bedrock V3000

**File name**: BIOS\_BDV3000\_RELEASE\_V1\_SIGNED.BIN

**Release date**: 15-OCT-2023

**MD5**: 68f94b371618e942a529187b19ebbfbc

[BIOS_BDV3000_RELEASE_V1_SIGNED.BIN](./attachments/BIOS_BDV3000_RELEASE_V1_SIGNED.BIN)

<a id="revision-notes"></a>

### Revision notes

- AGESA 1.0.0.5
- Console encoding was set to VT-UTF8

{% hint style="info" %}
Early Bedrock V3000 samples shipped before 25-Aug-2023 (serial number B3D-230825 or smaller) may have an issue with BIOS update due to signature incompatibility.
If you have such a Bedrock V3000 sample and need to update BIOS please contact SolidRun.
{% endhint %}

