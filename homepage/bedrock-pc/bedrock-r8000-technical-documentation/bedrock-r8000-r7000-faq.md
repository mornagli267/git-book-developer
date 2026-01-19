# Bedrock R8000 | R7000 FAQ

### What is the longevity of Bedrock R7000?

For longevity, it is advised to consider [Bedrock R8000](https://www.solid-run.com/industrial-computers/bedrock-r8000/) which has 10 years guaranteed longevity.\
Bedrock R8000 is fully compatible to Bedrock R7000.

### Does Bedrock R7000 include AMD Ryzen™ AI?

Ryzen 7840HS and 7840U include Ryzen AI IPU. Ryzen 7440U does not.\
Also, [Bedrock R7000 Edge AI](https://www.solid-run.com/fanless-computers/bedrock-r7000-edgeai/) can be fitted with up to 3 Hailo-8™ AI accelerators, for AI inferencing performance of up to 78 TOPS.

### Where is Bedrock manufactured and where is it shipped from?

Bedrock PCBAs are manufactured by [IMI Philippines](https://www.global-imi.com/)\
Mechanical assembly and testing for Bedrock samples and small volume orders takes place at SolidRun facility in Israel. In that case shipping is from Israel.\
For large volume orders, assembly and testing takes place at IMI, supervised by SolidRun. In that case shipping is done directly from the Philippines to the customer.

### Can NVME drives be configured in a RAID array?

Bedrock has 3 PCIe4x4 NVME devices.\
SolidRun evaluated hardware RAID controllers for Bedrock and decided not to incorporate it. To the best of our judgement, current SSD technology provides adequate performance, capacity and reliability and therefore hardware RAID does not make sense for Bedrock form factor.

Please note that Bedrock is offered with enterprise grade Micron 7450 NVME SSD which has built-in power loss protection. This SSD makes a good choice for critical data.

The modular architecture of Bedrock allows developing an integrated RAID controller, either by SolidRun or by a 3rd party.

### Which software RAID solution can be used?

Linux has several software RAID options, including mdadm, Btrfs and ZFS.

Worth noting that Bedrock has high CPU performance and high NVME performance which may make software RAID an effective solution.

### What are the dimensions of Bedrock package and its weight?

The standard Bedrock package measures 24 x 18 x 11 cm (4.7 liter)

Weight varies according to Bedrock configuration between 1.5 Kg and 4 Kg.

{% hint style="info" %}
PSU, cables and accessories are not included in the box and are shipped in a separate box.
{% endhint %}


### What is the difference between industrial temperature Bedrock and commercial temperature one?

Industrial temperature Bedrock undergoes power-on testing below -40ºC and full system stress-testing at +85ºC. This ensures that all devices and the system as a whole withstands the extreme temperatures.

Worth noting that full system testing is more reliable than relying on the temperature rating of individual components and devices. In fact, industrial temperature Bedrock may include components that are not originally rated for industrial temperature and are qualified within the industrial temperature Bedrock system.

### What metrics should be used to determine if Bedrock is thermally fine?

1. Monitor CPU die temperature in software.\
   Temperature should not exceed 100ºC
2. Measure enclosure temperature using a thermo-coupler or IR thermometer.\
   Temperature should not exceed ambient+40ºC
3. Measure power used by Bedrock.\
   If measuring AC “at the wall” assume power consumed by Bedrock is 90% of the measured value\
   Bedrock temperature above ambient is proportional to power

Notes:

* To verify that Bedrock is assembled properly and does not have thermal conduction failures, check these guidelines
  * DeltaT die to enclosure should not exceed 20ºC
  * DeltaT between two sides of Bedrock should not exceed 15ºC
* It is advised to limit CPU power in BIOS to the minimum power that meets performance goals, in order to reduce temperatures
* All secondary devices (RAM, SSD, NICs, power FETs) are conduction cooled and are not expected to overheat

### How do I check the CPU clocks?

To see the clocks of the CPU you can use the following command: `lscpu -e=mhz`

&#x20;To probe continuously you can use the command: `watch -n 0.5 lscpu -e=mhz`\
This command will probe the CPU clocks every 0.5 seconds; you can change the probing time as you wish.
