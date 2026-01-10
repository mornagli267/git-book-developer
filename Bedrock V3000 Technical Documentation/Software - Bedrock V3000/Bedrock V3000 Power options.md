
[Bedrock PC](../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../Software%20-%20Bedrock%20V3000.md)

# Bedrock V3000 Power options

Bedrock provides a wide range of power management options, this guide will go over the basic power limit setting in BIOS as well as controling the power from the bedrockpower utility (experimantal).

## BIOS

- Plug power to device
- Press 'DEL' repetitively to go to BIOS setup menu
- In BIOS, go to the power tab

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/799080449/image-20240702-124825.png?version=1&modificationDate=1719924508891&cacheVersion=1&api=v2&width=760&height=490)

- Select cpu power limit enabled

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/799080449/image-20240702-124858.png?version=1&modificationDate=1719924539980&cacheVersion=1&api=v2&width=760&height=490)

- In the CPU power limit (W) option select a value between 8W-54W (default is 45W)

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/799080449/image-20240702-124959.png?version=1&modificationDate=1719924600568&cacheVersion=1&api=v2&width=760&height=490)

- Go to the ‘Save & Exit’ tab

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/799080449/image-20240702-125154.png?version=1&modificationDate=1719924716232&cacheVersion=1&api=v2&width=760&height=490)

- Select 'Save Changes and Reset'
- Confirm saving configuration and exiting

![](https://developer.resources.solid-run.com/wiki/download/thumbnails/799080449/image-20240702-125255.png?version=1&modificationDate=1719924777173&cacheVersion=1&api=v2&width=760&height=490)

## BedrockPower

Clone the [bedrockpower github repository](https://github.com/SolidRun/BedrockPower) and follow the repositories instructions.

Support is experimental and might not work for all devices, This is a great option to test your bedrock with different power configurations and then go to BIOS and set it persistently.

> [!NOTE]
> BedrockPower changes **DO NOT** persist over reboots
