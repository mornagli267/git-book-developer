# SFP modules tested with Bedrock V3000

<a id="introduction"></a>

## Introduction

This page lists the SFP modules that have been tested on Bedrock PC by SolidRun.

<a id="testing-methodology"></a>

## Testing methodology

- Running iperf between a clearfog LX2160 and bedrock.
- Pass criteria, completing iperf without any errors or losses.

<a id="10gbase-t-sfp-modules-rj45"></a>

## 10GBASE-T SFP+ Modules (RJ45)

| Manufacturer | Part number | Passed | speed | Notes |
| --- | --- | --- | --- | --- |
| Ubiquiti | UACC-CM-RJ45-MG | V   | 9.41 Gbits/sec |     |
| FS  | SFP-10G-T | V   | 9.45 Gbits/sec |     |
| Walsun | HXSX-ATRI-1 | V   | 9.42 Gbits/sec |     |

<a id="dac-10-gbe-sfp-modules"></a>

## DAC 10 GbE SFP+ Modules

| Manufacturer | Part number | Passed | speed | Notes |
| --- | --- | --- | --- | --- |
| FS  | SFPP-PC005 | V   | 8.63 Gbits/sec |     |

<a id="fiber-optic-10-gbe-sfp-modules"></a>

## Fiber optic 10 GbE SFP+ Modules

| Manufacturer | Part number | Passed | speed | Notes |
| --- | --- | --- | --- | --- |
| solid-optics | SFP-10G-LR-SO | V   | 8.91 Gbits/sec | Dual fiber |
| solid-optics | SFP-10G-ER+-SO | V   |     | Dual fiber |
| sandstone | GLC-SX-MMD-ST | X   |     | Dual fiber  <br>No link  <br>(had only 1 module not sure test valid) |
| Axcen Photonics | AXGD-1354-0531 | X   |     | Dual fiber  <br>No link  <br>(had only 1 module not sure test valid) |
| FS  | SFP-10GSR-85 | V   | 8.76 Gbits/sec | Dual fiber |
| sandstone | GLC-BX-D20-ST | X   |     | Single fiber  <br>No link |

<a id="1-gbe-sfp-modules"></a>

## 1 GbE SFP modules

| Manufacturer | Part number | Passed | speed | Notes |
| --- | --- | --- | --- | --- |
| Source | SPGBTXCNFC | V   | 941 Mbits/sec |     |
| Jabil | SF01S1RJC000T | V   | 940 Mbits/sec |     |
| Asahi Net | ASA-SFP-RJ45 | V   | 940 Mbits/sec |     |
| OEM | SPT-PE-T2 | V   | 941 Mbits/sec |     |
| FS  | SFP-GB-GE-T | V   | 940 Mbits/sec |     |

> [!INFO]
> List will be updated as soon as SolidRun tests more SFP modules on bedrock PC.