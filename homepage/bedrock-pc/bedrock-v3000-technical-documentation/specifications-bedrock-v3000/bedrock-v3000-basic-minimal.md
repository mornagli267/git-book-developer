# Bedrock V3000 Basic / Minimal

The only technical difference between Bedrock V3000 Basic and Bedrock V3000 Minimal is that Basic includes 4x 2.5 GbE ports (Intel i226 NICs, RJ45) which are not included in Minimal.

![](./attachments/basic%20and%20minimal.jpg)

<a id="hardware-implementation"></a>

## Hardware implementation

Both Basic and Minimal hardware is comprised of SoM, NIO and optional SX and PM.

- Bedrock V3000 Basic is using **NIO V3000 Basic**.
- Bedrock V3000 Minimal is using **NIO V3000 Minimal**.  
It is the same PCB as NIO V3000 Basic, assembled without the 2.5 GbE related components and connector.
- All other boards are identical for Basic and Minimal.

Dual 10 GbE ports are present in both Basic and Minimal.

<a id="see-also"></a>

### See also:

- [Bedrock V3000 Basic block diagram](https://drive.google.com/file/d/1bgjY0bzk7xiONxsBhrf3vpstDtXHDJUl/view?usp=share_link)
- [Bedrock V3000 Minimal block diagram](https://drive.google.com/file/d/1gaiv6PfVrkQYSuAmSQe3LVbpXx-s2_EB/view?usp=share_link)

<a id="software"></a>

## Software

Bedrock V3000 Basic and Bedrock V3000 Minimal use the same BIOS and support the same operating systems.

> [!INFO]
> 10 GbE is currently **not** supported in Windows.
> Therefore, Bedrock V3000 Minimal is not recommended for running Windows due to lack of wired networking.

<a id="mechanical"></a>

## Mechanical

Basic and Minimal have identical mechanical design.

- Bedrock V3000 Basic has 1x4 RJ45 on the front panel
- Bedrock V3000 Minimal does not have those RJ45 ports

<a id="pricing"></a>

## Pricing

Bedrock V3000 Minimal is priced lower than Bedrock V3000 Basic.

> [!INFO]
> Please contact [SolidRun](https://www.solid-run.com/fanless-computers/industrial-embedded-computers/bedrock-v3000-basic/#evaluate-bedrock) or [Bedrock resellers](https://www.solid-run.com/fanless-computers/industrial-embedded-computers/bedrock-v3000-basic/#bedrock-resellers) for a quotation.