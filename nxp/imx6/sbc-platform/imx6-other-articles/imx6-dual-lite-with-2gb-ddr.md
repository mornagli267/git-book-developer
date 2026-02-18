# i.MX6 Dual-lite with 2GB DDR

For  SOM iMX6 Dual-lite with **2GB** DDR requires a special U-Boot change to support the **2GB** DDR with imx6 Dual-lite...

By default the general iMX6 U-Boot configured to support **1GB** DDR when detected imx6 Dual-liteSOM version, so you need to rebuild your U-Boot with applying the attached patch to support the **2GB** DDR with SOM iMX6 Dual-lite (the attached patch should replace the default settings of the imx6 Dual-lite from 1GB to 2GB and adding the DDR calibration for the 2GB DDR).

```
diff --git a/board/solidrun/mx6cuboxi/mx6cuboxi.c b/board/solidrun/mx6cuboxi/mx6cuboxi.c
index 8fad3febf9..450399088d 100644
--- a/board/solidrun/mx6cuboxi/mx6cuboxi.c
+++ b/board/solidrun/mx6cuboxi/mx6cuboxi.c
@@ -936,6 +936,22 @@ static const struct mx6_mmdc_calibration mx6dl_1g_mmcd_calib = {
    .p1_mpwrdlctl =    0x36363430,
 };
 
+/* microSOM with Dual lite processor and 2GB memory */
+static const struct mx6_mmdc_calibration mx6dl_2g_mmcd_calib = {
+   .p0_mpwldectrl0 =  0x00450052,
+   .p0_mpwldectrl1 =  0x003C0046,
+   .p1_mpwldectrl0 =  0x00230025,
+   .p1_mpwldectrl1 =  0x00280036,
+   .p0_mpdgctrl0 =    0x4230022C,
+   .p0_mpdgctrl1 =    0x02180224,
+   .p1_mpdgctrl0 =    0x421C0220,
+   .p1_mpdgctrl1 =    0x020C0218,
+   .p0_mprddlctl =    0x3C3E4440,
+   .p1_mprddlctl =    0x44464A3E,
+   .p0_mpwrdlctl =    0x38302E2E,
+   .p1_mpwrdlctl =    0x3C363632,
+};
+
 static struct mx6_ddr3_cfg mem_ddr_2g = {
    .mem_speed = 1600,
    .density   = 2,
@@ -1007,7 +1023,7 @@ static void spl_dram_init(int width)
    else if (is_cpu_type(MXC_CPU_MX6Q))
        mx6_dram_cfg(&sysinfo, &mx6q_2g_mmcd_calib, &mem_ddr_4g);
    else if (is_cpu_type(MXC_CPU_MX6DL))
-       mx6_dram_cfg(&sysinfo, &mx6dl_1g_mmcd_calib, &mem_ddr_2g);
+       mx6_dram_cfg(&sysinfo, &mx6dl_2g_mmcd_calib, &mem_ddr_4g);
    else if (is_cpu_type(MXC_CPU_MX6SOLO))
        mx6_dram_cfg(&sysinfo, &mx6dl_512m_mmcd_calib, &mem_ddr_2g);
 }
-- 
2.25.1
```

you can follow the [i.MX6 U-Boot](../imx6-software/imx6-u-boot.md) guide to generate a new U-Boot for imx6 SOM.

The quick test can be:

1- install general i.MX6 image from Solidrun web ([sr-imx6-debian-buster-20220731-cli.img.xz](https://solid-run-images.sos-de-fra-1.exo.io/IMX6/Debian/sr-imx6-debian-buster-20220731-cli.img.xz)) & uncompress & flash it on SD Card

2- override the bootloader (U-Boot & SPL) of the SD card using the commands below:&#x20;

```
dd if=SPL of=/dev/sdX bs=1k seek=1 conv=sync
dd if=u-boot.img of=/dev/sdX bs=1k seek=69 conv=sync
```

Attached here is a pre-built U-Boot and SPL with the above changes applied.

[u-boot.img](attachments/u-boot.img) [SPL](attachments/SPL/) [0001-add-imx6dl\_2g\_mmcd\_calib.patch](attachments/0001-add-imx6dl_2g_mmcd_calib.patch)
