# CN913x COM Tested SO-DIMM Memory

<a id="introduction"></a>

## Introduction

The intention of this page is to describe what has been tested on the [CN913x COM express type 7](https://www.solid-run.com/embedded-networking/marvell-octeon-tx2-family/) module; what has passed and what has failed.

<a id="testing-methodology"></a>

## Testing Methodology

The testing methodology is mainly focused on running multiple instances of Linux memtester tool (as the core count) with variable buffer size where the buffer size is at least L3 cache in size.

The initial condition varies where one time the DDR training is conducted while all devices after power off; so room temperature is the die junction and then using different tools we reach with processor junction temperature into it’s max (105c in case of CN913x SoC).

<a id="tested-memory-table"></a>

## Tested Memory Table

All SO-DIMMs that are tested are SO-DIMM DDR4 type with different sizes, speeds, with/without ECC and industrial temperature support.

The table is based on modules that SolidRun have tested and on modules that are being used and were validated by customers.  

> [!INFO]
> The list is sorted alphabetical.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **SO-DIMM part number** | **Description** | **Passed** | **Failed** | **Notes** |
| ADATA AD4B2400316G17-BSSB | 16GByte 2400Mtps | V   |     |     |
| ADATA AD4S320038G22-BGN | 8GByte 3200Mtps | V   |     |     |
| ADATA AD4B3200716G22-BSSA | 16GByte 3200Mtps + ECC |     |     |     |
| Kingston KVR32S22S6/4 | 4GByte 3200 Mtps | V   |     |     |
| Kingston Hyper-X HX432S20IBK2/32 | 16GByte 3200 Mtps | V   |     |     |
| Kingston Hyper-X KF432S20IBK2/32 | 16GByte 3200 Mtps | V   |     |     |
| Kingston Hyper-X HX432S0IB2/8 | 8GByte 3200 Mtps | V   |     |     |
| Micron MTA4ATF1G64HZ-3G2E2 | 8GByte 3200 Mtps | V   |     |     |
| Micron MTA18ASF2G72HZ-2G6E1 / 3G2E1 | 16GByte 2666Mtps + ECC | V   |     |     |
| Samsung M471A1K43EB1-CWE | 8 GByte 3200 Mtps | V   |     |     |
| Samsung M471A2K43CB1-CRC | 16GByte 2400 Mtps | V   |     |     |
| Samsung M471A1K43CB1-CRC | 8GByte 2400 Mtps | V   |     |     |
| SKHynix HMA82GSA6AFR8N-UH | 16GByte 2400 Mtps | V   |     |     |
| Virtium VL41A2G63A-N8SC-S1 | 16GByte 2666 Mtps + ECC | V   |     | Industrial temp |