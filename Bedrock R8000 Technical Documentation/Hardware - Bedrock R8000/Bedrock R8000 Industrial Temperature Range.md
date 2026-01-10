
[Bedrock PC](../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../Bedrock%20R8000%20Technical%20Documentation.md) > [Hardware - Bedrock R8000](../Hardware%20-%20Bedrock%20R8000.md)

# Bedrock R8000 Industrial Temperature Range

Bedrock R8000 is available with optional industrial temperature range.  
Each industrial temperature Bedrock undergoes full functional test at the extreme low and high temperatures, including stress text at the max temperature.

## Specific devices not qualified for industrial temperature range

If a Bedrock unit fails the industrial temperature range, it disqualified, hardware is changed and retested until it passes successfully.

The following devices are not supported for industrial temperature range due to low yield (high failure rate)

- PM1248  
  **How to address**: Choose PM1260
- NVME Micron 7450 Pro  
  **How to address**: Choose another NVME, or order Bedrock with no NVME and purchase industrial grade NVME separately

The list above may change in the future subject to SolidRun industrial temperature test statistics.

## RTC battery

Industrial temperature Bedrock has industrial temperature RTC battery installed.
