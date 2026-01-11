# Bedrock R8000 | R7000 Errata

<a id="full-size-display-port-does-not-work-in-bedrock-r7000-basic-resolved"></a>

# Full size Display Port does not work in Bedrock R7000 Basic (resolved)

<a id="status"></a>

### Status

As of 23-Jan-2025 issue is resolved.

<a id="symptom"></a>

### Symptom

Bedrock R7000 Basic has four display outputs (1x HDMI, 2x mini-DP, 1x full size DP).

The full size DP does not function with BIOS older than Jan-2025.

<a id="solution"></a>

### Solution

Update BIOS

<a id="root-cause"></a>

### Root cause

Internal port configuration issue involving the SoC firmware and BIOS.

<a id="10g-usb-hot-plug-doesnt-work"></a>

# 10G USB Hot plug doesn't work

Due to some power management issues, the USB ports hot plug is disabled.  
You can prevent the OS from using the ACPI power management policies by using this workaround.  
[https://solidrun.atlassian.net/wiki/spaces/developer/pages/666370082/Bedrock+Troubleshooting#USB-10G-(Closest-to-console-port)-hotplug-doesn't-work](../bedrock-troubleshooting.md#usb-10g-closest-to-console-port-hotplug-doesnt-work)

<a id="older-bedrock-with-ryzen-hs-do-not-support-ddr5-4800"></a>

# Older Bedrock with Ryzen HS do not support DDR5 4800

<a id="symptom"></a>

### Symptom

Bedrock does not boot if DDR5 is set to 4800 MT/s or lower. Works with DDR5 set to 5600 MT/s.  
If BIOS default is set to 4800 MT/s on an old Bedrock with Ryzen HS **Bedrock is bricked** and should be returned by RMA.

<a id="applies-to"></a>

### Applies to

Bedrock R7840HS | R8845HS with SN earlier than B7D-241101-000

<a id="root-cause"></a>

### Root cause

Reducing DDR5 frequency results in unsupported DDR voltage setting

<a id="solution"></a>

### Solution

DDR5 voltage circuit is revised for all units starting from B7D-241101-000

<a id="work-around"></a>

### Work around

Install [BIOS for Ryzen HS](https://solidrun.atlassian.net/wiki/spaces/developer/pages/edit-v2/530546703#bios-for-ryzen-hs-cpus) that defaults to DDR5 5600 MT/s.

If DDR5 setting was changed and Bedrock does not boot, then [reset BIOS](../bedrock-r8000-technical-documentation/software-bedrock-r8000/bios-bedrock-r8000-r7000/bedrock-r8000-r7000-bios-reset.md).