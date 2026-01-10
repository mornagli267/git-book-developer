
[Bedrock PC](../Bedrock%20PC.md)

# Bedrock Troubleshooting

## Table of contents

- [Full size Display Port does not work in Bedrock R7000 Basic](#full-size-display-port-does-not-work-in-bedrock-r7000-basic)
  - [See R7000 Basic Full-size DP Erratum](#see-r7000-basic-full-size-dp-erratum)
- [System reboots under certain conditions while HDMI is connected](#system-reboots-under-certain-conditions-while-hdmi-is-connected)
  - [Status](#status)
  - [Symptom](#symptom)
  - [Solution](#solution)
- [USB 10G (Closest to console port) hotplug doesn't work](#usb-10g-closest-to-console-port-hotplug-doesn-t-work)
  - [Symptom](#symptom)
  - [Solution](#solution)
- [Bedrock reboots once when booting to OS after power loss](#bedrock-reboots-once-when-booting-to-os-after-power-loss)
  - [Symptom](#symptom)
  - [Workaround](#workaround)
- [After re-assembly Bedrock does not power up / some features do not function properly](#after-re-assembly-bedrock-does-not-power-up-some-features-do-not-function-properly)
  - [Symptom](#symptom)
  - [Possible Cause](#possible-cause)
  - [Solution](#solution)

# Full size Display Port does not work in Bedrock R7000 Basic

### See[Bedrock R8000 | R7000 Errata](Bedrock%20R8000%20Technical%20Documentation/Bedrock%20R8000%20_%20R7000%20Errata.md)

# System reboots under certain conditions while HDMI is connected

### Status

resolved

### Symptom

Bedrock R7000 reboots when HDMI display is connected in the following scenarios:

- Running lspci and accessing device 08:00.03
- Running some programs that are opening a GUI
- Installing AMD GPU Windows drivers
- Booting Windows installer

### Solution

[Bedrock R8000 | R7000 BIOS Image Files](Bedrock%20R8000%20Technical%20Documentation/Software%20-%20Bedrock%20R8000/BIOS%20-%20Bedrock%20R8000%20_%20R7000/Bedrock%20R8000%20_%20R7000%20BIOS%20Image%20Files.md)

# USB 10G (Closest to console port) hotplug doesn't work

### Symptom

When unplugging and plugging a USB device to the 10G USB port (closest one to the console port) the USB device has power but no data.

SolidRun R&D is working on solving the issue.

### Solution

**Windows**: Disable USB *Power Managment* for USB Host Controller in Device Manager.

**Linux**: Add usbcore.autosuspend=-1 to grub command line

```java
sudo nano /etc/default/grub
```

Find the line that starts with: `GRUB_CMDLINE_LINUX_DEFAULT`

Add the `usbcore.autosuspend=-1` argument

```java
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash usbcore.autosuspend=-1"
```

Save the new configuration

```java
update-grub
```

# Bedrock reboots once when booting to OS after power loss

### Symptom

When device loses power, before booting to OS it reboots one time then boots to OS normally.

### Workaround

Let the device reboot, after which it will continue working normally, until the next power loss.

# After re-assembly Bedrock does not power up / some features do not function properly

### **Symptom**

- Bedrock was fully disassembled for installing RAM / NVME on SoM.   
  After re-assembly Bedrock does not power up / some features do not function properly

### **Possible Cause**

- There are four high density B2B connectors between SoM and NIO. Connectors may not be fully connected.

### **Solution**

- Disassemble and separate NIO from SoM.
- Observe the B2B connectors and their position. Ensure they are clean on both sides.
- Seat the NIO and apply pressure on the connectors to ensure the NIO is seated properly.
- Tighten NIO screws.
- Complete assembly and test power up and functionality.

Error rendering macro 'include' : com.atlassian.renderer.v2.macro.MacroException: No title provided.
