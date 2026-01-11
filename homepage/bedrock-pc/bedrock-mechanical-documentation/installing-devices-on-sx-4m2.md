# Installing devices on SX 4M2

SX 4M2 has four M.2 sockets.  
Below is a guide about the fastening mechanism of M.2 cards on SX 4M2:

<a id="general-description"></a>

# General description

![](./attachments/image-20230707-085806.png)

The locking mechanism has two parts

|     |     |
| --- | --- |
| Standoff | ![](./attachments/image-20230707-090045.png) |
| Screw | ![](./attachments/image-20230707-090111.png) |

SX 4M2 has multiple key-hole shaped openings for supporting different M.2 sizes.

![](./attachments/image-20230707-090419.png)

<a id="installation-guide"></a>

# Installation guide

1. Insert standoff in keyhole, groove down.![](./attachments/image-20230707-092055.png)
2. Push standoff to the narrow end of the keyhole.![](./attachments/image-20230707-092434.png)
**Tip:** If pushing the standoff in place is difficult, consider using a 4mm hex socket for pushing the standoff in place.
3. Install M.2 card in the M.2 slot and tighten the screw onto the standoff![](./attachments/image-20230707-092858.png)

<a id="thermal-coupling-of-ssd"></a>

### Thermal coupling of SSD

Most of the power is generated in the flash controller which in nearly all NVME SSDs is located close to the M.2 edge connector, on the component side. A 0.5mm/1mm 20x20 mm positioned as depicted would be effective in keeping the NVME SSD cool.

![](./attachments/image-20230728-073801.png)

Additional such pad can be placed further away from the M.2 connector. This would extract heat from the flash chips.