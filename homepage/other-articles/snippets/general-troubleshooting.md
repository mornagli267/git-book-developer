# General troubleshooting

- [Bedrock 'hangs' after system update or on new installation](#bedrock-hangs-after-system-update-or-on-new-installation)
  - [Status](#status)
  - [Symptom](#symptom)
  - [Fix](#fix)
    - [Wait for the system to boot](#wait-for-the-system-to-boot)
- [USB Hotplug does not work after pulling out and plugging in](#usb-hotplug-does-not-work-after-pulling-out-and-plugging-in)
  - [Status](#status)
  - [Symptom](#symptom)
  - [Fix](#fix)
    - [Linux](#linux)
    - [Windows](#windows)
- [Bedrock overheats when positioned flat or without a stand](#bedrock-overheats-when-positioned-flat-or-without-a-stand)

<a id="bedrock-hangs-after-system-update-or-on-new-installation"></a>

# Bedrock 'hangs' after system update or on new installation

<a id="status"></a>

### Status

Closed

<a id="symptom"></a>

### Symptom

![image-20240703-104108.png](./attachments/image-20240703-104108.png)

System 'hangs' on the systemd-networkd-wait-online service start during the boot process.  
It looks like a bug in the service file since it waits for ALL interfaces to get an ip and unless this happens, it will 'hang'.

However, the system does not hang, it will be like this for about 3 minutes, then the service will time out.

<a id="fix"></a>

### Fix

<a id="wait-for-the-system-to-boot"></a>

#### Wait for the system to boot

- run
  - sudo systemctl edit systemd-networkd-wait-online.service
- Uncomment the line where there is the execstart="..." and to the end of the command add "--any"
  - Should look line this:`ExecStart=/usr/lib/systemd/systemd-networkd-wait-online --any`
- Save the file
- run
  - Systemctl daemon-reload
  - sudo systemctl restart systemd-networkd-wait-online.service

<a id="usb-hotplug-does-not-work-after-pulling-out-and-plugging-in"></a>

# USB Hotplug does not work after pulling out and plugging in

<a id="status"></a>

### Status

Closed

<a id="symptom"></a>

### Symptom

USB works when booting the system with it plugged, when unplugged and plugged again it stops working.

<a id="fix"></a>

### Fix

<a id="linux"></a>

#### Linux

- Run:
  - nano /etc/default/grub
- on the line that starts with: GRUB\_CMDLINE\_LINUX\_DEFAULT change to:
  - GRUB\_CMDLINE\_LINUX\_DEFAULT="quiet splash **usbcore.autosuspend=-1**"
- Run:
  - update-grub
- Reboot

<a id="windows"></a>

#### Windows

<a id="bedrock-overheats-when-positioned-flat-or-without-a-stand"></a>

# Bedrock overheats when positioned flat or without a stand

Bedrock convection cooling works by the chimney effect which requires

1. Bedrock to be positioned vertically
2. Having space below the Bedrock body for cool air to enter heatsink

Convection cooling does not work effectively in the following cases

1. Bedrock is positioned horizontally rather than vertically
2. Bedrock is positioned on a flat surface without the stand
3. Bedrock is placed in a small closed cabinet with no ventilation which results in elevated temperature of ambient air

See [Bedrock Mounting options](../../../homepage/bedrock-pc/bedrock-mechanical-documentation/bedrock-mounting-options.md) for proper positioning of Bedrock.