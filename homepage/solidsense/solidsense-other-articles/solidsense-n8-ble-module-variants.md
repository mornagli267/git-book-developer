# SolidSense N8 BLE Module Variants

* [Intro](solidsense-n8-ble-module-variants.md#intro)
* [Hardware Variants & PCB Revisions](solidsense-n8-ble-module-variants.md#hardware-variants-pcb-revisions)
* [SKU-to-Module Mapping](solidsense-n8-ble-module-variants.md#sku-to-module-mapping)
* [Firmware Options & Defaults](solidsense-n8-ble-module-variants.md#firmware-options-defaults)
* [UART Pinout Differences (Developer Critical)](solidsense-n8-ble-module-variants.md#uart-pinout-differences-developer-critical)
* [Schematics & Hardware Resources](solidsense-n8-ble-module-variants.md#schematics-hardware-resources)

## **Intro**

This page documents the two BLE module options used across SolidSense N8 hardware revisions, how they map to SKUs, and the key UART pin differences developers must consider. It also links to the module schematics and provides migration notes between PCB revisions.

***

## Hardware Variants & PCB Revisions

* **Legacy N8 (PCB ≤ v1.3):** populated with **u-blox NINA-B1**.
* **Current N8 (PCB v1.4+):** populated with **Fujitsu FWM7BLZ22**.

Both variants are functionally compatible at the system level but differ in BLE module and UART pin mapping.

***

## SKU-to-Module Mapping

* **SRG40x.01SD** (x ∈ {1, 2, 5, 6, 7}) → **u-blox NINA-B1**
* **SRG40x.02SD** (x ∈ {1, 2, 5, 6, 7}) → **Fujitsu FWM7BLZ22**
* Example:
  * **SRG0405.01SD** — N8 Compact with Wi-Fi, BLE-**u-blox**, LTE, RS485, CAN, ETH-Atheros
  * **SRG0405.02SD** — N8 Compact with Wi-Fi, BLE-**FWM7BLZ22**, LTE, PoE, RS485, CAN, ETH-ADIN

{% hint style="info" %}
**Note:** **“.02SD”** SKUs ship FWM7BLZ22 with **BLE firmware** by default. **“.02SW”** SKUs (e.g., `SRG40x.02SW`) ship with **Wirepas** firmware.
{% endhint %}


***

## Firmware Options & Defaults

* **NINA-B1:** BLE stack as per u-blox defaults.
* **FWM7BLZ22:**
  * **.02SD** → BLE firmware by default.
  * **.02SW** → Wirepas firmware preloaded.\
    If a different firmware load is required, specify at order time.

***

## UART Pinout Differences (Developer Critical)

| Module            | UART\_0\_TX | UART\_0\_RX | UART\_0\_RTS | UART\_0\_CTS |
| ----------------- | ----------- | ----------- | ------------ | ------------ |
| u-blox NINA-B1    | 6           | 5           | N.C.         | PD           |
| Fujitsu FWM7BLZ22 | 6           | 8           | N.C.         | PD           |

**Legend:** N.C. = Not Connected, PD = Pulled Down.\
**Impact:** If migrating from NINA-B1 to FWM7BLZ22, update any pin mappings that reference UART0 RX (pin 5 → pin 8).

***

## Schematics & Hardware Resources

* **NINA-B1 Module Schematic**

![image-20250814-103121.png](../../../.gitbook/assets/image-20250814-103121.png)

TX/RX Nordic pin number

**UART\_TX** on pin **6** and **UART\_RX** on pin **5**

![image-20250814-103414.png](../../../.gitbook/assets/image-20250814-103414.png)

* **Fujitsu** **FWM7BLZ022W Module Schematic**\
  ![image-20250814-103035.png](../../../.gitbook/assets/image-20250814-103035.png)

TX/RX Nordic pin number

**UART\_TX** on pin **6** and **UART\_RX** on pin **8**

![image-20250814-093728.png](../../../.gitbook/assets/image-20250814-093728.png)
