# ARMADA A388 SOM U-Boot ODT Update

<a id="summary"></a>

## Summary

Old versions of U-Boot did not configure correctly the ODT on data signals of DDR RAM on ARMADA A388 SOMs. This article provides information about the affected hardware and U-Boot versions.

<a id="impact"></a>

## Impact

Incorrect ODT configuration might cause data corruption on write to RAM due to electric reflection of data signal.

<a id="affected-hardware"></a>

## Affected Hardware

All systems with ARMADA A388 SOM are affected. Actual corruption has only been observed on SOM rev 2.1.

<a id="fixed-u-boot-versions"></a>

## Fixed U-Boot Versions

U-Boot versions older than version 2018.03 are affected. Upstream U-Boot versions 2018.03 and newer are fixed, but only for SOMs with 1GB RAM. The mainline U-Boot fix is in commit `dbaf09590df9ad`.

SolidRun [U-Boot for ARMADA A388](https://github.com/SolidRun/u-boot/tree/v2018.01-solidrun-a38x) based on upstream version 2018.01 is fixed since commit `ab15b2d5b6ee`.

SolidRun U-Boot for ARMADA A388 based on Marvell provided source tree [version 2013.01-15t1](https://github.com/SolidRun/u-boot-armada38x/tree/u-boot-2013.01-15t1-clearfog) is fixed since commit `aba763a611e69f.`

<a id="solution"></a>

## Solution

To make sure Armada A38x RAM ODT is configured correctly on your system, do one of the following:

- Update U-Boot on your system to a fixed version
- Apply the applicable fix commit to your U-Boot source tree