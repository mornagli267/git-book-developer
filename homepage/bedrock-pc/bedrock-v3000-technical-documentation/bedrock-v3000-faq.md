# Bedrock V3000 FAQ

<a id="can-nvme-drives-be-configured-in-a-raid-array"></a>

### Can NVME drives be configured in a RAID array?

Bedrock has 3 PCIe4x4 NVME devices.  
SolidRun evaluated hardware RAID controllers for Bedrock and decided not to incorporate it. To the best of our judgement, current SSD technology provides adequate performance, capacity and reliability and therefore hardware RAID does not make sense for Bedrock form factor.

Please note that Bedrock is offered with enterprise grade Micron 7450 NVME SSD which has built-in power loss protection. This SSD makes a good choice for critical data.

The modular architecture of Bedrock allows developing an integrated RAID controller, either by SolidRun or by a 3rd party.

<a id="which-software-raid-solution-can-be-used"></a>

### Which software RAID solution can be used?

Linux has several software RAID options, including mdadm, Btrfs and ZFS.

Worth noting that Bedrock has high CPU performance and high NVME performance which may make software RAID an effective solution.

<a id="what-are-the-dimensions-of-bedrock-package-and-its-weight"></a>

### What are the dimensions of Bedrock package and its weight?

Bedrock V3000 package measures 24 x 18 x 11 cm (4.7 liter)

Weight varies according to Bedrock configuration between 1.5 Kg and 4 Kg.

> [!INFO]
> PSU, cables and accessories are not included in the box and are shipped in a separate box.

<a id="what-is-the-maximum-current-of-the-usb-ports"></a>

### What is the maximum current of the USB ports?

Each USB port supports up to 2A.