# CN9132 COM EVK Errata Lista List

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 27/05/2024 | Josua Mayer | 1   | Added Ethernet PHY Firmware Note |

{% hint style="info" %}
No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.
{% endhint %}


<a id="introduction"></a>

## Introduction

|     |     |     |     |
| --- | --- | --- | --- |
| **Short Description** | **Errata** | **Affected PCB rev** | **Fix or workaround** |
| 5Gbps RJ45 Ports have no link | Development samples may have been sent without firmware programmed.<br><br>During activation of the interfaces, Linux loads a generic driver that can not establish a link. | 1.3.2 and earlier | Existing customers can contact SolidRun Support for firmware download instructions. |
| Secondary 5Gbps RJ45 Port does not activate | The second 5Gbps Ethernet port fails to activate (“ifconfig up”) with error message "eth4: could not attach PHY (-19)".<br><br>In default assembly two resistors are routing the mdio signals to the bus of first phy where it has an address conflict. | 1.3.2 | Reroute the mdio signals from phy to the intended mdio bus on CP2:<br><br>Move the 0-Ohm resistors R9300 and R9303 to the places of R9301 and R9302.  <br>They are located on the bottom side of the carrier board within the area of M.2 port “CON1” near screw socket “J13”, and clearly labeled. |