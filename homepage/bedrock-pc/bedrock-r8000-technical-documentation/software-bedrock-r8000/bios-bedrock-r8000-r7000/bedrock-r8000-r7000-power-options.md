# Bedrock R8000 | R7000 power options

Bedrock provides a wide range of power management options, this guide will go over the basic power limit setting in BIOS as well as controling the power from the bedrockpower utility (experimantal).

## BIOS

* Plug power to device
* Press 'DEL' repetitively to go to BIOS setup menu
* In BIOS, go to the power tab
* Select cpu power limit enabled
* In the CPU power limit (W) option select a value between 8W-54W (default is 45W)
* Go to the ‘Save & Exit’ tab
* Select 'Save Changes and Reset'
* Confirm saving configuration and exiting

## BedrockPower

Clone the [bedrockpower github repository](https://github.com/SolidRun/BedrockPower) and follow the repositories instructions.

Support is experimental and might not work for all devices, This is a great option to test your bedrock with different power configurations and then go to BIOS and set it persistently.

> \[!NOTE] BedrockPower changes **DO NOT** persist over reboots
