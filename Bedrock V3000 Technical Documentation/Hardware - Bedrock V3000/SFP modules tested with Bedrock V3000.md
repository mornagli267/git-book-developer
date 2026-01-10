
[Bedrock PC](../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../Bedrock%20V3000%20Technical%20Documentation.md) > [Hardware - Bedrock V3000](../Hardware%20-%20Bedrock%20V3000.md)

# SFP modules tested with Bedrock V3000

## Introduction

This page lists the SFP modules that have been tested on Bedrock PC by SolidRun.

## Testing methodology

- Running iperf between a clearfog LX2160 and bedrock.
- Pass criteria, completing iperf without any errors or losses.

## 10GBASE-T SFP+ Modules (RJ45)

|  Manufacturer    |  Part number    |  Passed    |  speed         |  Notes    |
|:-----------------|:----------------|:-----------|:---------------|:----------|
| Ubiquiti         | UACC-CM-RJ45-MG | V          | 9.41 Gbits/sec |           |
| FS               | SFP-10G-T       | V          | 9.45 Gbits/sec |           |
| Walsun           | HXSX-ATRI-1     | V          | 9.42 Gbits/sec |           |

## DAC 10 GbE SFP+ Modules

|  Manufacturer    |  Part number    |  Passed    |  speed         |  Notes    |
|:-----------------|:----------------|:-----------|:---------------|:----------|
| FS               | SFPP-PC005      | V          | 8.63 Gbits/sec |           |

## Fiber optic 10 GbE SFP+ Modules

|  Manufacturer    |  Part number    |  Passed    |  speed         |  Notes                                                     |
|:-----------------|:----------------|:-----------|:---------------|:-----------------------------------------------------------|
| solid-optics     | SFP-10G-LR-SO   | V          | 8.91 Gbits/sec | Dual fiber                                                 |
| solid-optics     | SFP-10G-ER+-SO  | V          |                | Dual fiber                                                 |
| sandstone        | GLC-SX-MMD-ST   | X          |                | Dual fiber No link (had only 1 module not sure test valid) |
| Axcen Photonics  | AXGD-1354-0531  | X          |                | Dual fiber No link (had only 1 module not sure test valid) |
| FS               | SFP-10GSR-85    | V          | 8.76 Gbits/sec | Dual fiber                                                 |
| sandstone        | GLC-BX-D20-ST   | X          |                | Single fiber No link                                       |

## 1 GbE SFP modules

|  Manufacturer    |  Part number    |  Passed    |  speed        |  Notes    |
|:-----------------|:----------------|:-----------|:--------------|:----------|
| Source           | SPGBTXCNFC      | V          | 941 Mbits/sec |           |
| Jabil            | SF01S1RJC000T   | V          | 940 Mbits/sec |           |
| Asahi Net        | ASA-SFP-RJ45    | V          | 940 Mbits/sec |           |
| OEM              | SPT-PE-T2       | V          | 941 Mbits/sec |           |
| FS               | SFP-GB-GE-T     | V          | 940 Mbits/sec |           |

> [!IMPORTANT]
> List will be updated as soon as SolidRun tests more SFP modules on bedrock PC.
