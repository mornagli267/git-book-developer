# i.MX6 Reset Button

<a id="program-the-reset-button"></a>

### Program the reset button

That is exposed to linux as a GPIO key. You can see it in the device-tree here:

```
arch/arm/boot/dts/imx6qdl-cubox-i.dtsi
pinctrl_gpio_key: gpio-key {
                       fsl,pins = <
                               MX6QDL_PAD_EIM_DA8__GPIO3_IO08  0x17059
                       >;
               };
```

If you want you can customize this to look like a custom button. [https://github.com/SolidRun/linux-stable/blob/linux-4.9.y-imx6/Documentation/devicetree/bindings/input/gpio-keys.txt](https://github.com/SolidRun/linux-stable/blob/linux-4.9.y-imx6/Documentation/devicetree/bindings/input/gpio-keys.txt)

Then you would need to write a userspace daemon to listen for the key event and then perform whatever action you wanted depending on the length it was held down for.