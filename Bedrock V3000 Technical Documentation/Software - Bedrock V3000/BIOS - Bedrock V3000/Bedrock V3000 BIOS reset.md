
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [BIOS - Bedrock V3000](../BIOS%20-%20Bedrock%20V3000.md)

# Bedrock V3000 BIOS reset

If your Bedrock device is not booting due to changes in the BIOS menus, you can reset the BIOS to its default settings by following these steps:

1. Unplug the power supply from the device.
2. Take a SIM extractor pin (or a similar small tool) and insert it into the hole beside the console port until you feel the button click, on R7000 with USB-C the button is at the top of the device near the console connector.

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/830308356/image-20240730-085832.png?version=1&modificationDate=1722329913764&cacheVersion=1&api=v2&width=571&height=238)

3. While holding the button down, reconnect the power supply to the device.
4. Wait for checkpoints to appear in the serial console, ~20-40 seconds.

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/830308356/image-20240730-092734.png?version=1&modificationDate=1722331656520&cacheVersion=1&api=v2&width=608&height=319)

On **R7000** platforms, with BIOS V1.1 ([0ACTF10](https://eip.ami.com/eip/accessAttachment.do?task=get&iid=816769&aid=2511089)1) the S LED will blink, switching between green and orange, after this, you can release the sim extractor pin.

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/830308356/image-20250217-185030.png?version=1&modificationDate=1739818232323&cacheVersion=1&api=v2&width=594&height=185)
> [!IMPORTANT]
> You can hold the button indefinitely, however as long as you hold it, the device will keep rebooting this is expected behavior.

5. Release the button and allow the device to boot up.

> [!NOTE]
> First boot, might take some time for the device to boot up due to DDR training.

By following these steps, you should be able to reset the Bedrock BIOS to its default settings and restore normal operation.
