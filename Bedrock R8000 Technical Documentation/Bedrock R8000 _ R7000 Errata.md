
[Bedrock PC](../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../Bedrock%20R8000%20Technical%20Documentation.md)

# Bedrock R8000 | R7000 Errata

# Full size Display Port does not work in Bedrock R7000 Basic (resolved)

### Status

As of 23-Jan-2025 issue is resolved.

### Symptom

Bedrock R7000 Basic has four display outputs (1x HDMI, 2x mini-DP, 1x full size DP).

The full size DP does not function with BIOS older than Jan-2025.

### Solution

Update BIOS

### Root cause

Internal port configuration issue involving the SoC firmware and BIOS.

# 10G USB Hot plug doesn't work

Due to some power management issues, the USB ports hot plug is disabled.  
You can prevent the OS from using the ACPI power management policies by using this workaround.  
[Bedrock Troubleshooting](../Bedrock%20Troubleshooting.md)

# Older Bedrock with Ryzen HS do not support DDR5 4800

### Symptom

Bedrock does not boot if DDR5 is set to 4800 MT/s or lower. Works with DDR5 set to 5600 MT/s.  
If BIOS default is set to 4800 MT/s on an old Bedrock with Ryzen HS **Bedrock is bricked** and should be returned by RMA.

### Applies to

Bedrock R7840HS | R8845HS with SN earlier than B7D-241101-000

### Root cause

Reducing DDR5 frequency results in unsupported DDR voltage setting

### Solution

DDR5 voltage circuit is revised for all units starting from B7D-241101-000

### Work around

Install [BIOS for Ryzen HS](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/530546703#BIOS-for-Ryzen-HS-CPUs) that defaults to DDR5 5600 MT/s.

If DDR5 setting was changed and Bedrock does not boot, then [Bedrock R8000 | R7000 BIOS reset](Software%20-%20Bedrock%20R8000/BIOS%20-%20Bedrock%20R8000%20_%20R7000/Bedrock%20R8000%20_%20R7000%20BIOS%20reset.md).
