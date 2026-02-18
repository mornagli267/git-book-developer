# HummingBoard Hailo 15 Boot Select

<a id="boot-select"></a>

#### Boot Select

Before powering up the board for the first time it is recommended to select the boot media. Hailo 15 SOM has two boot options: qSPI boot (main option) and UART firmware update mode. In the qSPI boot mode SPL uses GPIO1 to select if it needs to boot from eMMC or use Y-modem protocol to load u-boot with UART.

<a id="using-hummingboard-iiot"></a>

## Using HummingBoard IIoT

S5 DIP switch should be modified.

qSPI boot:

| **Switch #** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| Position | Off | Off | Off | Off | Off | **On** |

UART boot:

| **Switch #** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| Position | **On** | Off | Off | Off | Off | **On** |

qSPI boot with Y-modem u-boot load:

| **Switch #** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| Position | Off | Off | **On** | Off | Off | **On** |

<a id="using-hummingboard-ripple-pulse-pro"></a>

## Using HummingBoard Ripple/Pulse/Pro

S3 DIP switch should be modified.

qSPI boot:

| **Switch #** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| Position | Off | Off | Off | Off | Off | Off |

UART boot:

| **Switch #** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| Position | Off | **On** | Off | Off | Off | Off |

qSPI boot with Y-modem u-boot load:

| **Switch #** | **1** | **2** | **3** | **4** | **5** | **6** |
| --- | --- | --- | --- | --- | --- | --- |
| Position | Off | Off | **On** | Off | Off | Off |