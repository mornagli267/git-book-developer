# Installing and upgrading RAM, storage and devices in Bedrock

<a id="required-tools"></a>

## Required tools

Cross screwdriver (Phillips) #1

Cross screwdriver (Phillips) #0

Flat-head screwdriver

Thermal paste (MX-4 or similar) and spudger

<a id="open-enclosure"></a>

## Open enclosure

<a id="bedrock-with-stand"></a>

### Bedrock with Stand

Use Philips screwdriver #1 to remove two stand screws and remove stand.

![](./attachments/image-20231111-145420.png)

![](./attachments/image-20231111-145530.png)

<a id="bedrock-without-stand"></a>

### Bedrock without stand

Remove the flat-head screw using Philips #1.

![](./attachments/image-20231111-145612.png)

![](./attachments/image-20231111-145754.png)

<a id="remove-opposite-wall"></a>

## Remove opposite wall

Use flat-head screwdriver in the marked slot to pry open the enclosure

![](./attachments/image-20231111-150158.png)

Slide out the opposite wall.

![](./attachments/image-20231111-150411.png)

<a id="installing-devices-on-sx-2x-nvme-wifi-modem"></a>

## Installing devices on SX (2x NVME, WiFi, Modem)

Use Philips #0 to remove the M.2 fastening screw

![](./attachments/image-20231111-150601.png)

Install the M.2 device.

> [!INFO]
> If uninstalling WiFi or modem, make sure to disconnect MHF4 cables before removing.  
> When installing WiFi / modem, remember to connect MHF4 connectors after installing.

![](./attachments/image-20231111-150717.png)

> [!INFO]
> The M.2 screw is mounted onto a removable standoff. The standoff can be positioned for NVME M.2 2280/2260/2242 and for modem M.2 3042/3052.
> If not installing a device at a slot make sure to remove the standoff.

> [!INFO]
> Apply 1mm thermal pad on NVME devices.
> Apply 0.5mm thermal pad on WiFi and modem.

> [!INFO]
> For installing RAM and NVME on SoM please proceed as described below.

<a id="remove-frame"></a>

## Remove Frame

> [!WARNING]
> If Bedrock has SIM trays, remove them before proceeding.

Remove 5 posts using Philips #0

![](./attachments/image-20231111-151428.png)

![](./attachments/image-20231111-151504.png)

Pull out panels.

![](./attachments/image-20231111-151542.png)

<a id="remove-deck"></a>

## Remove Deck

> [!WARNING]
> The 4 screws on the bottom of the skirt tighten the heatplate against the CPU.  
> Make sure **not to open them**!
> ![image-20240613-121750.png](./attachments/image-20240613-121750.png)

Remove 3 screws holding stacked electronic boards “deck” to main wall using Philips #0.

![](./attachments/image-20231111-152529.png)

Pull out deck from main wall.

Note that there is thermal paste between heatplate and main wall, so some force is required.

![](./attachments/image-20231111-152157.png)

<a id="installing-ram"></a>

## Installing RAM

First, release SX board as follows:

Remove 4 SX screws using Philips #0.

![](./attachments/image-20231111-152657.png)

![](./attachments/image-20231111-152728.png)

Lift SX board. Do not release the flex side.

![](./attachments/image-20231111-152837.png)

Release two screws holding RAM cover using Philips #0.

![](./attachments/image-20231111-153000.png)

Slide out RAM cover

![](./attachments/image-20231111-153052.png)

Install RAM (SODIMM DDR5)

![](./attachments/image-20231111-153121.png)

<a id="installing-nvme-on-som"></a>

## Installing NVME on SoM

Use Philips #0 to remove M.2 screw of NVME.

![](./attachments/image-20231111-153755.png)

Install NVME module.

![](./attachments/image-20231111-153816.png)

> [!INFO]
> Apply 1mm thermal pad on NVME.

<a id="re-assembling-bedrock"></a>

# Re-assembling Bedrock

Re-assemble in reverse order.

> [!INFO]
> For best thermal performance it is advised to re-apply thermal paste in the two thermal joints:
> 1. Between heat-plate and main wall
> 2. Between heatpipes of main-wall and opposite wall