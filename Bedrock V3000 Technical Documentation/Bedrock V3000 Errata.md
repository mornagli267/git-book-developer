
[Bedrock PC](../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../Bedrock%20V3000%20Technical%20Documentation.md)

# Bedrock V3000 Errata

## Ubuntu kernel version

Ubuntu Server 22.04.3 has kernel 5.15 which does not include the AMD\_XGBE driver versionrequired for V3000 SFP modules.

## Bluetooth LED

Bluetooth LED does not work.

## RJ45 LEDs

Swapped RJ45 LEDs in ports 3,4.

> [!IMPORTANT]
> Applies to Bedrock V3000 units earlier than 16-Oct-2023 with SN smaller than **B3D-231016-001**

## PMIC programming

Random crashes due to incorrect PMIC programming.

> [!IMPORTANT]
> Applies to some Bedrock V3000 units earlier than 5-Sep-2023 with SN smaller than **B3D-230905-001**

To verify PMIC programming please follow the instructions below:

1. download the RyzenAdj utility to Bedrock: [Download RyzenAdj utility](https://solidrn-my.sharepoint.com/:u:/g/personal/lior_jigalo_solid-run_com/EZ7s9GJ6wFJHhOc-M6SLWMoBavwX9VfqdZFkUo6aOIdfqw?e=WTjgFQ)
2. run: ./ryzenadj -i | grep "TDC VALUE VDD"

Expected value is greater than 2.8 when Bedrock is in idle.
