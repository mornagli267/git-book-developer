# OV5640/OV5642 Camera Sensor

<a id="overview"></a>

#### Overview

The HummingBoard Gate and Edge models feature a MIPI CSI connector onboard and both models support OV5640/OV5642 camera sensors. For more information on the implementation please see the schematics here.

**Installing the cable incorrectly on the HB Edge/Gate can result in the Camera module being damaged!**

The compatible cameras can be found in the following article: [http://linuxgizmos.com/wandboard-sbc-gains-camera-add-ons/](http://linuxgizmos.com/wandboard-sbc-gains-camera-add-ons/)

<a id="device-tree-changes"></a>

## Device Tree changes

Below are the device tree changes we used successfully to enable support for the OV5642 cameras.

```
--- a/arch/arm/boot/dts/imx6dl-hummingboard2.dts
+++ b/arch/arm/boot/dts/imx6dl-hummingboard2.dts
@@ -50,3 +50,44 @@
model = "SolidRun HummingBoard2 Solo/DualLite";
compatible = "solidrun,hummingboard2/dl", "fsl,imx6dl";
};
+
+&iomuxc {
+ hummingboard2 {
+ pinctrl_hummingboard2_parallel: hummingboard2_parallel {
+ fsl,pins = <
+ MX6QDL_PAD_EIM_A24__IPU1_CSI1_DATA19 0x0b0b1
+ MX6QDL_PAD_EIM_A23__IPU1_CSI1_DATA18 0x0b0b1
+ MX6QDL_PAD_EIM_A22__IPU1_CSI1_DATA17 0x0b0b1
+ MX6QDL_PAD_EIM_A21__IPU1_CSI1_DATA16 0x0b0b1
+ MX6QDL_PAD_EIM_A20__IPU1_CSI1_DATA15 0x0b0b1
+ MX6QDL_PAD_EIM_A19__IPU1_CSI1_DATA14 0x0b0b1
+ MX6QDL_PAD_EIM_A18__IPU1_CSI1_DATA13 0x0b0b1
+ MX6QDL_PAD_EIM_A17__IPU1_CSI1_DATA12 0x0b0b1
+ MX6QDL_PAD_EIM_DA11__IPU1_CSI1_HSYNC 0x0b0b1
+ MX6QDL_PAD_EIM_DA12__IPU1_CSI1_VSYNC 0x0b0b1
+ MX6QDL_PAD_EIM_A16__IPU1_CSI1_PIXCLK 0x0b0b1
+
+ MX6QDL_PAD_EIM_DA10__GPIO3_IO10 0x400130b1
+ >;
+ };
+ };
+};
+
+&i2c3 {
+ ov5642: ov5642@3c {
+ compatible = "ovti,ov5642";
+ reg = <0x3c>;
+ clocks = <&clks IMX6QDL_CLK_CKO2>;
+ clock-names = "csi_mclk";
+
+ pwn-gpios = <&gpio3 10 GPIO_ACTIVE_HIGH>;
+
+ ipu_id = <0>;
+ csi_id = <1>;
+ mclk = <24000000>;
+ mclk_source = <0>;
+
+ pinctrl-names = "default";
+ pinctrl-0 = <&pinctrl_hummingboard2_parallel>;
+ };
+};
```