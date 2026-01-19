# i.MX6 Application Note – Thermal Analysis

## Introduction

This Application Note notes the thermal grades of SolidRun i.MX6 products.

## i.MX6 SOM

|                         |                  |               |          |                                                              |             |                |               |
| ----------------------- | ---------------- | ------------- | -------- | ------------------------------------------------------------ | ----------- | -------------- | ------------- |
| **Grade**               | **SolidRun SKU** | **i.MX6 CPU** | **DDR3** | <p><strong>Ethernet</strong><br><br><strong>PHY</strong></p> | **Crystal** | **PWR Mngmnt** | **WiFi (\*)** |
| **Commercial**          | SRMX6SO\*V15C0   | Cj            | C        | I                                                            | I           | I              | E             |
|                         | SRMX6DL\*V15C0   | Cj            | C        | I                                                            | I           | I              | E             |
|                         | SRMX6DU\*V15C0   | Ej            | C        | I                                                            | I           | I              | E             |
|                         | SRMX6QD\*V15C0   | Ej            | C        | I                                                            | I           | I              | E             |
|                         |                  |               |          |                                                              |             |                |               |
| **Extended**            | SRMX6SO\*V15E0   | Ej            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6DL\*V15E0   | Ej            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6DU\*V15C0   | Ej            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6QD\*V15C0   | Ej            | I        | I                                                            | I           | I              | E             |
|                         |                  |               |          |                                                              |             |                |               |
| **Industrial**          | SRMX6SO\*V15I0   | Ij            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6DL\*V15I0   | Ij            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6DU\*V15I0   | Ij            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6QD\*V15I0   | Ij            | I        | I                                                            | I           | I              | E             |
|                         |                  |               |          |                                                              |             |                |               |
| **Industrial Extended** | SRMX6SO\*V15A0   | Aj            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6DL\*V15A0   | Aj            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6DU\*V15A0   | Aj            | I        | I                                                            | I           | I              | E             |
|                         | SRMX6QD\*V15A0   | Aj            | I        | I                                                            | I           | I              | E             |

{% hint style="info" %}
**Please note** By default the i.MX6 Dual and Quad core CPU are “commercial extended” by default (\*) For WiFi there is an industrial ordering option – Please contact SolidRun for additional information
{% endhint %}


**Comments**

The temperatures below are for the junction of the CPU and the ambient of the rest of the components.

The number indicating the minimum in CPU junction are typically the boot temperatures, and the max (i.e. 95/105/125) are the maximum temperatures of the die inside the CPU package, that can be measured by the OS (for instance Linux ‘sensors’ command) –

C= Commercial – Ambient 0C-70C

E= Extended – Ambient -20C-70C

I=  Industrial – Ambient -40C-85C

Cj= Commercial – Junction Temperature 0C-95C

Ej= Extended – Junction Temperature -20C-105C

Ij=  Industrial – Junction Temperature -40C-105C

Aj= Automotive – Junction Temperature -40C- 125C

NXP i.MX6 Order-able CPUs options (Solo and Dual-lite):

![](../../../../.gitbook/assets/image-20211104-093559.png)

NXP i.MX6 Order-able CPUs options (Dual and Quad):

![](../../../../.gitbook/assets/image-20211104-093616.png)

## HummingBoard Base/Pro

|                |                                               |             |                  |         |
| -------------- | --------------------------------------------- | ----------- | ---------------- | ------- |
| **Grade**      | **SolidRun SKU**                              | **USB HUB** | **Analog Audio** | **RTC** |
| **Commercial** | SRHBCBE000CV35 – HummingBoard Base\|Com. Temp | C           | –                | –       |
|                | SRHBCPE000CV35 – HummingBoard Pro\|Com. Temp  | C           | C                | C       |
| **Industrial** | SRHBCBE000IV35 – HummingBoard Base\|Ind. Temp | I           | –                | –       |
|                | SRHBCPE000IV35 – HummingBoard Pro\|Ind. Temp  | I           | I                | I       |

## HummingBoard Gate/Edge

|                |                                                |             |         |
| -------------- | ---------------------------------------------- | ----------- | ------- |
| **Grade**      | **SolidRun SKU**                               | **USB HUB** | **RTC** |
| **Commercial** | SRHBCGE000CV14 – HummingBoard Gate\|Com. Temp  | I           | C       |
|                | SRHBCEE000CV14 – HummingBoard Edge \|Com. Temp | I           | C       |
| **Industrial** | SRHBCGE000IV14 – HummingBoard Gate \|Ind. Temp | I           | Removed |
|                | SRHBCEE000IV14 – HummingBoard Edge \|Ind. Temp | I           | Removed |

{% hint style="warning" %}
**Comments** The temperatures of the components are Operating Ta (ambient): Commercial: 0C-70C Industrial: -40C-85C
{% endhint %}


## CuBox-i

The ambient temperatures that the CuBox-i supports are 0C-40C.
