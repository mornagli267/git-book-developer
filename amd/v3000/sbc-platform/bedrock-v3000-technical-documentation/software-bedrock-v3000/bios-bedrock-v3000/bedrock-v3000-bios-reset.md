# Bedrock V3000 BIOS reset

If your Bedrock device is not booting due to changes in the BIOS menus, you can reset the BIOS to its default settings by following these steps:

1. Unplug the power supply from the device.
2. Take a SIM extractor pin (or a similar small tool) and insert it into the hole beside the console port until you feel the button click, on R7000 with USB-C the button is at the top of the device near the console connector.
3. While holding the button down, reconnect the power supply to the device.
4. Wait for checkpoints to appear in the serial console, \~20-40 seconds.

On **R7000** platforms, with BIOS V1.1 ([0ACTF10](https://eip.ami.com/eip/accessAttachment.do?task=get\&iid=816769\&aid=2511089)1) the S LED will blink, switching between green and orange, after this, you can release the sim extractor pin.

{% hint style="info" %}
You can hold the button indefinitely, however as long as you hold it, the device will keep rebooting this is expected behavior.
{% endhint %}


5. Release the button and allow the device to boot up.

{% hint style="info" %}
First boot, might take some time for the device to boot up due to DDR training.
{% endhint %}


By following these steps, you should be able to reset the Bedrock BIOS to its default settings and restore normal operation.
