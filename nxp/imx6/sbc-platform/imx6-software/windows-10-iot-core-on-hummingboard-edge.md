# Windows 10 IoT Core on HummingBoard Edge

<a id="background"></a>

#### Background

Windows 10 IoT Core is a version of Windows 10 that is optimized for embedded devices including ARM and x86/x64 devices. IoT Core is requires less resources, while offering a wide range of Microsoft IoT services and solutions, which makes it perfect for embedded systems. For more information about this OS please visit Microsoft’s developer page [here](https://developer.microsoft.com/en-us/windows/iot). This platform is also [Azure](https://azure.microsoft.com/en-us/services/iot-hub/) certified.

<a id="supported-platforms"></a>

#### Supported Platforms

The supported platforms are the HummingBoard Gate/Edge which are based on the NXP i.MX6 SoC. SolidRun ships a dedicated part number pre-loaded with Windows 10 IoT core on the SD card, customers who want to order this platform can use the following link [here](https://www.solid-run.com/product/MSMX6QDW00D02GE008E00CH).

<a id="supported-features"></a>

###### Supported Features

|     |     |
| --- | --- |
|     | NXP i.MX6 |
| Audio | V   |
| GPIO | V   |
| I2C | V   |
| Ethernet | V   |
| SPI | V   |
| Display | V   |
| UART | V   |
| USB | V   |
| PCIe | V   |
| MIPI-CSI | N/A |
| Graphics/Video | Software-rendered |
| GPS | N/A |
| Wi-Fi/BT | N/A |
| Trusted I/O | V   |
| Processor power management | V   |
| TPM | V   |
| Secure Boot | Under development |
| PWM | V   |
| JTAG | V   |
| eMMC | V   |
| SDHC | V   |

{% hint style="warning" %}
**Please Note**
This OS is not being maintained by SolidRun directly and SolidRun does not offer technical support for it.
{% endhint %}


<a id="download"></a>

#### Download

Below you can find the pre-built images for the specific HummingBoard configuration.

{% hint style="warning" %}
**Please Note**
The provided Windows 10 IoT Core images is for pre-production/development use only. For more information and production options please see:
1. NXP resources:
[https://www.nxp.com/design/software/embedded-software/i-mx-software/windows-10-iot-core-for-i-mx-applications-processors:IMXWIN10IOT](https://www.nxp.com/design/software/embedded-software/i-mx-software/windows-10-iot-core-for-i-mx-applications-processors:IMXWIN10IOT)
1. Microsoft resources:
[https://docs.microsoft.com/en-us/windows/iot-core/learn-about-hardware/iotnxp](https://docs.microsoft.com/en-us/windows/iot-core/learn-about-hardware/iotnxp)
{% endhint %}


|     |     |
| --- | --- |
| **Product** | **Link** |
| NXP i.MX6 Solo | [Download](https://solid-run-images.sos-de-fra-1.exo.io/IMX6/Windows-10-IoT/HB_Edge_Solo.ffu) |
| NXP i.MX6 Dual-lite | [Download](https://solid-run-images.sos-de-fra-1.exo.io/IMX6/Windows-10-IoT/HB_Edge_Dual-Lite.ffu) |
| NXP i.MX6 Quad | [Download](https://solid-run-images.sos-de-fra-1.exo.io/IMX6/Windows-10-IoT/HB_Edge_Quad.ffu) |