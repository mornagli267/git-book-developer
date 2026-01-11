# Changing the IR protocol under Linux

The Linux gpio-ir-recv driver defaults to the rc6 decoder.  This can be changed in two ways.

1. Change the protocol at runtime using sysfs
```
echo rc-5 > /sys/class/rc/rc0/protocols
```
2. Make the change in the device tree for the ir-receiver node.
```
diff --git a/arch/arm/boot/dts/imx6qdl-hummingboard.dtsi b/arch/arm/boot/dts/imx6qdl-hummingboard.dtsi
index d3b0b20aa05b..eda351f44d31 100644
--- a/arch/arm/boot/dts/imx6qdl-hummingboard.dtsi
+++ b/arch/arm/boot/dts/imx6qdl-hummingboard.dtsi
@@ -57,6 +57,7 @@
                 gpios = <&gpio3 5 GPIO_ACTIVE_LOW>;
                 pinctrl-names = "default";
                 pinctrl-0 = <&pinctrl_hummingboard_gpio3_5>;
+                linux,rc-map-name = "rc-rc5-mce";
         };
 
         regulators {
```

Previously this had defaulted to the rc5 decoder, this change was made as an alignment with the mainline device-tree.