
[Bedrock PC](../../Bedrock%20PC.md) > [Bedrock Mechanical documentation](../Bedrock%20Mechanical%20documentation.md)

# Installing and upgrading RAM, storage and devices in Bedrock

## Required tools

Cross screwdriver (Phillips) #1

Cross screwdriver (Phillips) #0

Flat-head screwdriver

Thermal paste (MX-4 or similar) and spudger

## Open enclosure

### Bedrock with Stand

Use Philips screwdriver #1 to remove two stand screws and remove stand.

![](../../../attachments/e12fef81-de10-4f98-8151-580c78056806.png)![](../../../attachments/51cfd855-8763-467d-aaa0-b59bf71b7c15.png)

### Bedrock without stand

Remove the flat-head screw using Philips #1.

![](../../../attachments/64ee28cc-e267-4a38-99b7-e89c8d6c9fe0.png)![](../../../attachments/9dfa747a-fbf0-49d7-b702-2eca8ac52dca.png)

## Remove opposite wall

Use flat-head screwdriver in the marked slot to pry open the enclosure

![](../../../attachments/38119ee7-8723-4abd-855b-fabb762a3469.png)

Slide out the opposite wall.

![](../../../attachments/0bb68b9c-d639-4843-ad63-f2ec0e297339.png)

## Installing devices on SX (2x NVME, WiFi, Modem)

Use Philips #0 to remove the M.2 fastening screw

![](../../../attachments/3c51c79d-f143-453d-a7d8-889e8accb20e.png)

Install the M.2 device.

> [!IMPORTANT]
> If uninstalling WiFi or modem, make sure to disconnect MHF4 cables before removing.  
> When installing WiFi / modem, remember to connect MHF4 connectors after installing.

![](../../../attachments/77d665ec-bd14-4eed-869d-649cb98dd28a.png)
> [!IMPORTANT]
> The M.2 screw is mounted onto a removable standoff. The standoff can be positioned for NVME M.2 2280/2260/2242 and for modem M.2 3042/3052.
>
> If not installing a device at a slot make sure to remove the standoff.

> [!IMPORTANT]
> Apply 1mm thermal pad on NVME devices.
>
> Apply 0.5mm thermal pad on WiFi and modem.

> [!IMPORTANT]
> For installing RAM and NVME on SoM please proceed as described below.

## Remove Frame

> [!WARNING]
> If Bedrock has SIM trays, remove them before proceeding.

Remove 5 posts using Philips #0

![](../../../attachments/c20698a8-dc55-4bdf-a71e-5a7e04d12745.png)![](../../../attachments/c31ce15a-8e50-476a-a7c9-e69db61ae365.png)

Pull out panels.

![](../../../attachments/54c127ca-7a24-47f2-a278-31e8539ff02a.png)

## Remove Deck

> [!WARNING]
> The 4 screws on the bottom of the skirt tighten the heatplate against the CPU.   
> Make sure **not to open them**!
>
> ![image-20240613-121750.png](../../../attachments/71c4d9f5-b93e-4062-8e6b-6479dac16af9.png)

Remove 3 screws holding stacked electronic boards “deck” to main wall using Philips #0.

![](../../../attachments/50e32079-df91-4122-a0b8-f2657ff94eed.png)

Pull out deck from main wall.

Note that there is thermal paste between heatplate and main wall, so some force is required.

![](../../../attachments/cb4b1f96-4111-4150-bece-725d720b31d5.png)

## Installing RAM

First, release SX board as follows:

Remove 4 SX screws using Philips #0.

![](../../../attachments/42bddc01-8aee-4104-8cf3-39c54fadaf02.png)![](../../../attachments/09cc4e04-b204-4f20-9c0b-84dbd7f01c06.png)

Lift SX board. Do not release the flex side.

![](../../../attachments/fa308465-69e8-475d-a049-72ded3475178.png)

Release two screws holding RAM cover using Philips #0.

![](../../../attachments/4d795db7-5dcb-4448-b4fa-957d3769c9fd.png)

Slide out RAM cover

![](../../../attachments/939d4d53-81be-4e18-bfbd-6619938c82bb.png)

Install RAM (SODIMM DDR5)

![](../../../attachments/f6a422e3-8e89-4e7a-95c7-339d6bf6a5cb.png)

## Installing NVME on SoM

Use Philips #0 to remove M.2 screw of NVME.

![](../../../attachments/93755f2a-81bb-4503-9b2c-ebedcb215d0e.png)

Install NVME module.

![](../../../attachments/6fbab3c3-96cb-40a1-8e38-1d58dcedd6a3.png)
> [!IMPORTANT]
> Apply 1mm thermal pad on NVME.

# Re-assembling Bedrock

Re-assemble in reverse order.

> [!IMPORTANT]
> For best thermal performance it is advised to re-apply thermal paste in the two thermal joints:
>
> 1. Between heat-plate and main wall
> 2. Between heatpipes of main-wall and opposite wall
