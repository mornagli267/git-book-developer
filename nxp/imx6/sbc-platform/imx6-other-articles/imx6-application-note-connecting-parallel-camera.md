# i.MX6 Application Note – Connecting Parallel Camera

<a id="introduction"></a>

#### Introduction

The SolidRun i.MX6 SOM is a high performance micro system on module that is based on the highly integrated NXP i.MX6 family of products.

This application note provides information on signal mux and pinout to be used when integrating i.MX6 SOM with a parallel camera sensor.

Please refer to the i.MX6 SOM Reference Manual for detailed hardware integration manual.

It is highly recommended to refer to the NXP io-mux utility and NXP i.MX6 reference manual for more details.

The design of the i.MX6 SOM incorporates 3 board to board headers that expose to a carrier board most of the functions of the different flavors of the NXP i.MX6 family of SoC.

Besides the dedicated MIPI CSI-2 serial interface, there is an option to connect a camera with parallel interface. Internally in the i.MX6 device it connects to the –

1. **IPU1 CSI1** when using the solo or dual lite versions of the
2. **IPU2 CSI1** when using the dual or quad versions of the

In the pinout table below, when referring to the IPUx\_CSI1\_DATA00, it should be referred as IPU1\_CSI1\_DATA00 on the solo or dual lite versions, and as IPU2\_CSI1\_DATA00 on the dual or quad versions.

<a id="pinout-description"></a>

#### Pinout Description

The pinout that is exposed on the i.MX6 SOM board to board headers are as follows:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Signal Name** | **Board To Board Header Name** | **Pin Number** | **Orcad Port Signal Name** | **i.MX6 Ball Number** |
| IPUx\_CSI1\_DATA00 | Main | 66  | DISP1\_DATA00 | M21 |
| IPUx\_CSI1\_DATA01 | Main | 60  | DISP1\_DATA01 | L24 |
| IPUx\_CSI1\_DATA02 | Main | 56  | DISP1\_DATA02 | L25 |
| IPUx\_CSI1\_DATA03 | Main | 54  | DISP1\_DATA03 | K25 |
| IPUx\_CSI1\_DATA04 | Main | 64  | DISP1\_DATA04 | L23 |
| IPUx\_CSI1\_DATA05 | Main | 62  | DISP1\_DATA05 | L22 |
| IPUx\_CSI1\_DATA06 | Main | 58  | DISP1\_DATA06 | K24 |
| IPUx\_CSI1\_DATA07 | Third | 70  | DISP1\_DATA07 | L21 |
| IPUx\_CSI1\_DATA08 | Third | 55  | DISP1\_DATA08 | J25 |
| IPUx\_CSI1\_DATA09 | Third | 60  | DISP1\_DATA09 | L20 |
| IPUx\_CSI1\_DATA10 | Third | 57  | DISP1\_DATA10 | K23 |
| IPUx\_CSI1\_DATA11 | Third | 68  | DISP1\_DATA11 | K21 |
| IPUx\_CSI1\_DATA12 | Third | 59  | DISP1\_DATA12 | G24 |
| IPUx\_CSI1\_DATA13 | Third | 64  | DISP1\_DATA13 | J22 |
| IPUx\_CSI1\_DATA14 | Third | 63  | DISP1\_DATA14 | G25 |
| IPUx\_CSI1\_DATA15 | Third | 62  | DISP1\_DATA15 | H22 |
| IPUx\_CSI1\_DATA16 | Third | 66  | DISP1\_DATA16 | H23 |
| IPUx\_CSI1\_DATA17 | Third | 69  | DISP1\_DATA17 | F24 |
| IPUx\_CSI1\_DATA18 | Third | 56  | DISP1\_DATA18 | J21 |
| IPUx\_CSI1\_DATA19 | Third | 67  | DISP1\_DATA19 | F25 |
| IPUx\_CSI1\_DATA\_EN | Third | 43  | DI1\_PIN15 | M22 |
| IPUx\_CSI1\_HSYNC | Third | 41  | DI1\_PIN02 | M20 |
| IPUx\_CSI1\_PIXCLK | Third | 54  | DI1\_DISP\_CLK | H25 |
| IPUx\_CSI1\_VSYNC | Third | 51  | DI1\_PIN03 | M24 |