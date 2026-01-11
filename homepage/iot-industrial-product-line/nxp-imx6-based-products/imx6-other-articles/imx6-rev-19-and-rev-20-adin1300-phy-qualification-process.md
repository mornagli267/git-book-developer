# i.MX6 Rev 1.9 and Rev 2.0 ADIN1300 PHY Qualification Process

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 21 Feb 2022 | Alvaro Karsz | 1.0 |     |
| Table of Contents | - [Background](#background)<br>- [Auto negotiation (A/N) test](#auto-negotiation-a-n-test)<br>  - [1Gbps](#1gbps)<br>  - [100Mbps](#100mbps)<br>  - [10Mbps](#10mbps)<br>- [Stress test](#stress-test)<br>  - [Retries for 100M cable iperf](#retries-for-100m-cable-iperf)<br>- [Thermal](#thermal)<br>- [Conclusion](#conclusion) |     |     |

<a id="background"></a>

## **Background**

Following SolidRun’s PCN on i.MX6 SOM Rev 1.5 migrating to Rev 1.9 and Rev 2.0, this article explains the qualification procedure that SolidRun performed to make sure the performance of Analog Devices ADIN1300 PHY is adequate and no performance / quality / stability issues are affecting any customer.

<a id="auto-negotiation-a-n-test"></a>

## Auto negotiation (A/N) test

ethtool was used to select the speed with A/N on.

<a id="1gbps"></a>

#### **1Gbps**

```
$ ethtool -s eth0 speed 1000 duplex full autoneg on
[ 8548.041399] fec 2188000.ethernet eth0: Link is Down
[ 8551.757596] fec 2188000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
```

<a id="100mbps"></a>

#### **100Mbps**

```
$ ethtool -s eth0 speed 100 duplex full autoneg on
[ 8617.585894] fec 2188000.ethernet eth0: Link is Down
[ 8620.397596] fec 2188000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx
```

<a id="10mbps"></a>

#### **10Mbps**

```
$ ethtool -s eth0 speed 10 duplex full autoneg on
[ 8648.151779] fec 2188000.ethernet eth0: Link is Down
[ 8650.557544] fec 2188000.ethernet eth0: Link is Up - 10Mbps/Full - flow control rx/tx
```

<a id="stress-test"></a>

## Stress test

Stress test using iperf for 30 minutes.

```
$ iperf3 -c <iperf server IP> -t 1800
```

|     |     |     |
| --- | --- | --- |
| **Cable length \[m\]** | **Speed \[Mpbs\]** | **Number of retries** |
| 3   | 1000 | 0   |
| 50  | 1000 | 0   |
| 100 | 1000 | 49  |

<a id="retries-for-100m-cable-iperf"></a>

#### Retries for 100M cable iperf

```
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-1800.00 sec  80.6 GBytes   385 Mbits/sec   49             sender
[  5]   0.00-1800.11 sec  80.6 GBytes   384 Mbits/sec                  receiver
```

<a id="thermal"></a>

## Thermal

![](./attachments/Screenshot%20from%202022-02-21%2013-19-13.png)

Max. temperature in PHY (Poly 1): ~71 °C.

Max. temperature in the SOM (Poly 3): ~75°C in SoC.

> [!NOTE]
> Thermal snapshot was taken after a weekend long iperf, without a heat-sink.

<a id="conclusion"></a>

## Conclusion

Based on SolidRun’s short and long term tests, we find that Analog Devices ADIN1300 ethernet PHY meets the requirements of the datasheet and SolidRun did not observe any stability, reliability or thermal problems.