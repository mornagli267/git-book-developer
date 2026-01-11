# List of SO-DIMM RAM modules tested with Bedrock V3000

<a id="introduction"></a>

## Introduction

This page lists DDR5 SO-DIMM RAM modules tested in Bedrock PC by SolidRun.

<a id="testing-methodology"></a>

## Testing Methodology

- DDR training right after power-up, Tjunction close to room temperature
- Multiple instances of Linux Memtester utility (one instance per core) with variable buffer size where the buffer size is greater than the size of L3 cache
- System is stressed until Tjunction approaches 105ºC while Memtester instances keep running

Pass criteria is completing the test above with no memory errors.

<a id="list-of-non-ecc-so-dimm-ram-modules"></a>

## List of non-ECC SO-DIMM RAM modules

Tested SO-DIMM modules are DDR5 with different capacity, rate, and temperature rating.

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **Manufacturer** | **Part number** | **Capacity \| Rate** | **Validated for V3000** | **Validated for R7000** | **Validated for R8000** | **Notes** |
| Kingston | CBD48S40BS6MA-8 | 8 GB DDR5 4800 | V   |     |     |     |
| Kingston | CBD48S40BS8MA-16 | 16 GB DDR5 4800 | V   |     |     |     |
| Kingston | CBD48S40BD8MA-32 | 32 GB DDR5 4800 | V   |     |     |     |
| Micron | MTC8C1084S1SC48BA1 | 16 GB DDR5 4800 | V   |     |     |     |
| Micron | MTC16C2085S1SC48BA1 | 32 GB DDR5 4800 | V   |     |     |     |
| A-DATA | AD5S48008G-S | 8 GB DDR5 4800 | V   |     |     |     |
| A-DATA | AD5S480016G-S | 16 GB DDR5 4800 | V   |     |     |     |
| A-DATA | AD5S480032G-S | 32 GB DDR5 4800 | V   |     |     | Based on K4RAH086VB-BCQK. |
| A-DATA | AD5S56008G-S | 8GB DDR5 5600 | V   |     | V   |     |
| A-DATA | AD5S560016G-B | 16GB DDR5 5600 | V   | V   | V   |     |
| A-DATA | AD5S560032G-S | 32GB DDR5 5600 | V   | V   | V   |     |
| Crucial | CT16G56C46S5 | 16GB DDR5 5600 |     | V   |     |     |
| Mushkin | MRA5S560LKKD48GX2 | 2x48GB - 96GByte DDR5 5600 |     | V   | V   |     |

<a id="list-of-ecc-so-dimm-ram-modules"></a>

## List of ECC SO-DIMM RAM modules

Tested ECC SO-DIMM modules are DDR5 with different capacity, rate, and temperature rating.

> [!INFO]
> Bedrock R7000 does **not** support ECC RAM and is therefore not listed

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Manufacturer** | **Part number** | **Capacity \| Rate** | **Validated for V3000** | **Validated for R8000** | **Notes** |
| Kingston | KSM48T40BS8KM-16HM | 16 GB DDR5 4800 ECC | V   |     |     |
| Kingston | KSM56T46BS8KM-16HA | 16 GB DDR5 5600 ECC |     | V   |     |
| Micron | MTC10C1084S1TC48BA1 | 16 GB DDR5 4800 ECC | V   | V   |     |
| Micron | MTC20C2085S1TC48BA1 | 32 GB DDR5 4800 ECC | V   |     |     |