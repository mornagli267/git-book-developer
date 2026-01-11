# SolidPC Testpoints

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 19 Apr 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Description](#description)<br>- [Carrierboard (Silk)](#carrierboard-silk)<br>- [Testpoints](#testpoints)<br>- [Detect all I2C busses](#detect-all-i2c-busses) |     |     |

<a id="description"></a>

## Description

Testpoints are designed to provide a secure anchoring point on a printed circuit board for j-hooks and miniature test leads.

<a id="carrierboard-silk"></a>

## Carrierboard (Silk)

[![](./attachments/image-20220419-145927.png)

](https://developer.solid-run.com/wp-content/uploads/2018/10/sr-ibx-solidpc-rev1.2-component-side-silk.pdf)[![](./attachments/image-20220419-150010.png)

](https://developer.solid-run.com/wp-content/uploads/2018/10/sr-ibx-solidpc-rev1.2-print-side-silk.pdf)

<a id="testpoints"></a>

## Testpoints

**Power management**

![](./attachments/image-20220419-150239.png)

**GPIOs and misc**

![](./attachments/image-20220419-150313.png)

[**MCU: STM32**](https://developer.solid-run.com/knowledge-base/ib8000-drivers/)**PA1..PA4 pins**

![](./attachments/image-20220419-150325.png)

> [!TIP]
> **Missing TP-names on PCB:**

Few TP points are not named on the pcb:

- TP27
- TP21
- TP6
- TP7
- TP8
- TP3
- TP4
- TP5

Please see the pictures below:

![](./attachments/image-20220419-150406.png)

![](./attachments/image-20220419-150414.png)

<a id="detect-all-i2c-busses"></a>

## Detect all I2C busses

This patch can be used if not all I2C busses are detected:

```
--- drivers/i2c/busses/i2c-designware-baytrail.c	2016-10-22 12:41:00.000000000 +0200
+++ /tmp/i2c-designware-baytrail.c	2016-10-26 15:05:42.936807731 +0200
@@ -22,7 +22,7 @@
 #include "i2c-designware-core.h"
 
 #define SEMAPHORE_TIMEOUT	100
-#define PUNIT_SEMAPHORE		0x7
+#define PUNIT_SEMAPHORE		0x10e
 #define PUNIT_SEMAPHORE_BIT	BIT(0)
 #define PUNIT_SEMAPHORE_ACQUIRE	BIT(1)
```