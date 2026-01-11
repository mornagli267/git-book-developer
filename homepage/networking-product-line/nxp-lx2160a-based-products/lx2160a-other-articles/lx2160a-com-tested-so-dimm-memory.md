# LX2160A COM Tested SO-DIMM Memory

<a id="introduction"></a>

## Introduction

The intention of this page is to describe what has been tested on the [LX2160A COM express type 7](https://www.solid-run.com/embedded-networking/nxp-lx2160a-family/cex7-lx2160/) module; what has passed and what has failed.

<a id="testing-methodology"></a>

## Testing Methodology

The testing methodology is mainly focused on running multiple instances of Linux memtester tool (as the core count) with variable buffer size where the buffer size is at least L3 cache in size.

The initial condition varies where one time the DDR training is conducted while all devices after power off; so room temperature is the die junction and then using different tools we reach with processor junction temperature into it’s max (105c in case of LX2160A SoC).

<a id="tested-memory-table"></a>

## Tested Memory Table

All SO-DIMMs that are tested are SO-DIMM DDR4 type with different sizes, speeds, with/without ECC and industrial temperature support.

The table is first published around when the LX2160A module started shipping to customers; it is expected to grow slightly in case all memory devices passes as in the current state and will update only the failed cases.

> [!INFO]
> The list is sorted alphabetical.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **SO-DIMM part number** | **Description** | **Passed** | **Failed** | **Notes** |
| ADATA AD4S3200732G22-BGN | 32GByte 3200Mtps | V   |     | Two SO-DIMMs reaches 64GByte system memory and reaches max bus speed 3200 Mtps |
| ADATA AD4S3200716G22-BGN | 16GByte 3200Mtps | V   |     |     |
| ADATA AD4S320038G22-BGN | 8GByte 3200Mtps | V   |     |     |
| Kingston KVR32S22S6/4 | 4GByte 3200 Mtps | V   |     |     |
| [Kingston Hyper-X HX432S20IBK2/32](https://shop.solid-run.com/product/SO-DIMM216/) | 16GByte 3200 Mtps | V   |     |     |
| Kingston Hyper-X KF432S20IBK2/32 | 16GByte 3200 Mtps | V   |     |     |
| Kingston Hyper-X HX432S0IB2/8 | 8GByte 3200 Mtps | V   |     |     |
| Micron MTA4ATF1G64HZ-3G2E2 | 8GByte 3200 Mtps | V   |     |     |
| Micron MTA18ASF4G72HZ | 32 GByte 3200 Mtps + ECC | V   |     | Two SO-DIMMs reaches 64GByte system memory and reaches max bus speed 3200 Mtps. with ECC. Has onboard temperature sensor |
| Samsung M471A1K43EB1-CWE | 8 GByte 3200 Mtps | V   |     |     |
| Samsung M474A4G43AB1-CWEQ | 32 GByte 3200 Mtps + ECC | V   |     | Two SO-DIMMs reaches 64GByte system memory and reaches max bus speed 3200 Mtps with ECC |
| Samsung M471A2K43CB1-CRC | 16GByte 2400 Mtps | V   |     |     |
| Samsung M471A4G43MB1-CTD | 32GByte 2666 Mtps | V   |     | Two SO-DIMMs reaches 64GByte system memory |
| Samsung M471A4G43AB1-CWE | 32 GByte 3200 Mtps | V   |     | Two SO-DIMMs reaches 64GByte system memory and reaches max bus speed 3200 Mtps |
| Samsung M471A1K43CB1-CRC | 8GByte 2400 Mtps | V   |     |     |
| SKHynix HMA82GSA6AFR8N-UH | 16GByte 2400 Mtps | V   |     |     |
| TeamGroup TE8GHSEV3BH | 8GByte 3200 Mtps with ECC industrial | V   |     |     |
| TeamGroup TE16GHSEV3BH | 16GByte 3200 Mtps with ECC industrial | V   |     |     |
| Virtium VL47A1H36B-C3SD | 8GByte 3200 Mtps | V   |     |     |
| Virtium VL41A2G63A-N8SC-S1 | 16GByte 2666 Mtps + ECC Industrial temp | V   |     |     |

> [!INFO]
> Notice that the above tests were performed when LX2160A COM express type 7 module core VDD was set to 780mV; which is the default setting when shipping the module.