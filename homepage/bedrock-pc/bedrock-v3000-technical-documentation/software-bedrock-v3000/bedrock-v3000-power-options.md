# Bedrock V3000 Power options

Bedrock provides a wide range of power management options, this guide will go over the basic power limit setting in BIOS as well as controling the power from the bedrockpower utility (experimantal).

<a id="bios"></a>

## BIOS

- Plug power to device
- Press 'DEL' repetitively to go to BIOS setup menu
- In BIOS, go to the power tab

![image-20240702-124825.png](./attachments/image-20240702-124825.png)

- Select cpu power limit enabled

![image-20240702-124858.png](./attachments/image-20240702-124858.png)

- In the CPU power limit (W) option select a value between 8W-54W (default is 45W)

![image-20240702-124959.png](./attachments/image-20240702-124959.png)

- Go to the ‘Save & Exit’ tab

![image-20240702-125154.png](./attachments/image-20240702-125154.png)

- Select 'Save Changes and Reset'
- Confirm saving configuration and exiting

![image-20240702-125255.png](./attachments/image-20240702-125255.png)

<a id="bedrockpower"></a>

## BedrockPower

Clone the [bedrockpower github repository](https://github.com/SolidRun/BedrockPower) and follow the repositories instructions.

Support is experimental and might not work for all devices, This is a great option to test your bedrock with different power configurations and then go to BIOS and set it persistently.

> [!NOTE]
> BedrockPower changes **DO NOT** persist over reboots