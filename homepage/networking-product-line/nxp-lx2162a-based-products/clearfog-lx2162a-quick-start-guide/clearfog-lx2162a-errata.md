# ClearFog LX2162A Errata

<a id="revisions-and-notes"></a>

## Revisions and Notes

|     |     |     |     |
| --- | --- | --- | --- |
| **Date** | **Owner** | **Revision** | **Notes** |
| 27/04/2023 |     | 1   | Production Release |
| 27/05/2023 |     | 2   | Resolved MAC addresses + DPMAC11 |
| 23/07/2023 |     | 3   | HW bugs workaround |

> [!INFO]
> No warranty of accuracy is given concerning the contents of the information contained in this publication. To the extent permitted by law no liability (including liability to any person by reason of negligence) will be accepted by SolidRun Ltd., its subsidiaries or employees for any direct or indirect loss or damage caused by omissions from or inaccuracies in this document. SolidRun Ltd. reserves the right to change details in this publication without prior notice. Product and company names herein may be the trademarks of their respective owners.

<a id="introduction"></a>

## Introduction

|     |     |     |     |
| --- | --- | --- | --- |
| **Short Description** | **Errata** | **Affected PCB rev** | **Fix or workaround** |
| upper 10Gbps SFP+ Port can not link up | It appears that the upper 10Gbps SFP+ port transmits a signal, but does not receive. Consequently the interface never detects a link.<br><br>This could be either SW or HW issue, to be determined. | Any | SoM revision 1.0 had a short on the rx line. Fixed by upgrading to revision 1.1 or later.  <br>All units shipped have SoM 1.1 or later. |
| 2x 2.5Gbps RJ45 not supported | 2 of the 8 RJ45 ports can from the hardware support 2.5Gbps ethernet. Software support for this configuration is incomplete. | Any | Limit to 1Gbps. |
| 1x RJ45 port can’t receive or transmit. | The second RJ45 port on the left, in bottom row while looking from the front currently can neither transmit nor receive.<br><br>Likely cause is a bug in NXPs networking firmware for the SoC. | Any | Resolved by [Software Update](https://github.com/SolidRun/lx2160a_build/commit/143b0ba3ed1a885f885e71f9cf11879fd9a90e07): SoC DEVDISR2 register had wrongly disabled dpmac11, causing tx/rx failure. |
| MAC addresses randomised | Random MAC addresses are assigned to network interface after booting Linux, even though specific ones are stored on EEPROM. | Any | Resolved by [Software Update](https://github.com/SolidRun/lx2160a_build/commit/92bef239332fdfedcbdcc4740c6261b3ad99607a). |
| SFP+ MOD\_ABS signal fail to detect module | HW bug - missing PU resistors to MOD\_ABS signal | REV 1.1 | Added 10K resistors to each of the buffers - U1706, U1707, U1708 and U3003 from pin #1 to pin #5<br><br>**\*see attached instructions** |
| 3.3V has a low voltage around 2.7V | HW bug - voltage drop on O-Ring diodes due to low current rating of the component | REV 1.1 | Remove D48 and assemble 0ohm 1/2W 0603 resistor from pin #1 to pin #3<br><br>**\*see attached instructions** |
| SFP+ fail to link up on optics module | HW bug - TX\_DIS is floating causing optic transceiver to shut Tx laser due to module internal PU | REV 1.1 | Stitching of TX\_DIS to GND<br><br>**\*see attached instructions** |

     

|     | File | Modified |
| --- | --- | --- |
| Labels<br><br>- No labels<br>- [Edit Labels](#section-0ffc757e-f980-4ad6-8a11-c757b1b28fb7)<br><br>[Preview] [View](/wiki/download/attachments/199491605/ECO++-+Clearfog+LX2162A_SFP_PU_3V3_ORING_and_SFP_Tx_Dis_.pdf?version=1) [Properties](/wiki/pages/editattachment.action?pageId=199491605&fileName=ECO++-+Clearfog+LX2162A_SFP_PU_3V3_ORING_and_SFP_Tx_Dis_.pdf&isFromPageView=true) [Delete](/wiki/pages/confirmattachmentremoval.action?pageId=199491605&fileName=ECO++-+Clearfog+LX2162A_SFP_PU_3V3_ORING_and_SFP_Tx_Dis_.pdf) | PDF File [ECO - Clearfog LX2162A\_SFP\_PU\_3V3\_ORING\_and\_SFP\_Tx\_Dis\_.pdf](/wiki/download/attachments/199491605/ECO%20%20-%20Clearfog%20LX2162A_SFP_PU_3V3_ORING_and_SFP_Tx_Dis_.pdf?api=v2) | Jul 23, 2023 by [Ilan Braun](/wiki/people/6231e3991f014e0069cd4610) |

- Drag and drop to upload or [browse for files] ![](/wiki/images/icons/wait.gif)

Upload file 

File description