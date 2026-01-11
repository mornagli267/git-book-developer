# List of SO-DIMM RAM modules tested with Ryzen V3000 CoM7

<a id="introduction"></a>

## Introduction

This page lists DDR5 SO-DIMM RAM modules tested on Ryzen V3000 CoM7 by SolidRun.

<a id="testing-methodology"></a>

## Testing Methodology

- DDR training right after power-up, Tjunction close to room temperature
- Multiple instances of Linux Memtester utility (one instance per core) with variable buffer size where the buffer size is greater than the size of L3 cache
- System is stressed until Tjunction approaches 105ºC while Memtester instances keep running

Pass criteria is completing the test above with no memory errors.

<a id="list-of-tested-so-dimm-ram-modules"></a>

## List of tested SO-DIMM RAM modules

Tested SO-DIMM modules are DDR5 with different capacity, rate, ECC support and temperature rating.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Manufacturer** | **Part number** | **Capacity \| type \| Rate \| ECC** | **Validated** | **Notes** |
| Kingston | CBD48S40BS6MA-8 | 8 GB DDR5 4800 | V   |     |
| Kingston | CBD48S40BS8MA-16 | 16 GB DDR5 4800 | V   |     |
| Micron | MTC8C1084S1SC48BA1 | 16 GB DDR5 4800 | V   |     |
| Kingston | KSM48T40BS8KM-16HM | 16 GB DDR5 4800 with ECC | V   |     |
| Kingston | CBD48S40BD8MA-32 | 32 GB DDR5 4800 | V   |     |
| Micron | MTC16C2085S1SC48BA1 | 32 GB DDR5 4800 | V   |     |
| Micron | MTC10C1084S1TC48BA1 | 16 GB DDR5 4800 ECC | V   |     |
| Micron | MTC20C2085S1TC48BA1 | 32 GB DDR5 4800 ECC | V   |     |
| ADATA | AD5S48008G-S | 8 GB DDR5 4800 | V   |     |
| ADATA | AD5S480016G-S | 16 GB DDR5 4800 | V   |     |
| ADATA | AD5S480032G-S | 32 GB DDR5 4800 | V   | Based on K4RAH086VB-BCQK. |
| ADATA | ADS56008G-S | 8GB DDR5 5600 | V   |     |
| ADATA | ADS560016G-S | 16GB DDR5 5600 | V   |     |
| ADATA | ADS560032G-S | 32GB DDR5 5600 | V   |     |
| Crucial | CT16G56C46S5 | 16GB DDR5 5600 |     |     |
| Mushkin | MRA5S560LKKD48GX2 | 2x48GB - 96GByte DDR5 5600 |     |     |
|     |     |     |     |     |