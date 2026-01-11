# Bedrock Troubleshooting

<a id="table-of-contents"></a>

## Table of contents

- [Full size Display Port does not work in Bedrock R7000 Basic](#full-size-display-port-does-not-work-in-bedrock-r7000-basic)
  - [See R7000 Basic Full-size DP Erratum](#see-r7000-basic-full-size-dp-erratum)
- [System reboots under certain conditions while HDMI is connected](#system-reboots-under-certain-conditions-while-hdmi-is-connected)
  - [Status](#status)
  - [Symptom](#symptom)
  - [Solution](#solution)
- [USB 10G (Closest to console port) hotplug doesn't work](#usb-10g-closest-to-console-port-hotplug-doesnt-work)
  - [Symptom](#symptom)
  - [Solution](#solution)
- [Bedrock reboots once when booting to OS after power loss](#bedrock-reboots-once-when-booting-to-os-after-power-loss)
  - [Symptom](#symptom)
  - [Workaround](#workaround)
- [After re-assembly Bedrock does not power up / some features do not function properly](#after-re-assembly-bedrock-does-not-power-up-some-features-do-not-function-properly)
  - [Symptom](#symptom)
  - [Possible Cause](#possible-cause)
  - [Solution](#solution)

<a id="full-size-display-port-does-not-work-in-bedrock-r7000-basic"></a>

# Full size Display Port does not work in Bedrock R7000 Basic

<a id="see-r7000-basic-full-size-dp-erratumhttps-solidrunatlassiannet-wiki-spaces-developer-pages-923271175-bedrockr8000r7000erratafull-size-display-port-does-not-work-in-bedrock-r7000-basic-resolved"></a>

### See [R7000 Basic Full-size DP Erratum](https://solidrun.atlassian.net/wiki/spaces/developer/pages/923271175/Bedrock+R8000+R7000+Errata#full-size-display-port-does-not-work-in-bedrock-r7000-basic-resolved)

<a id="system-reboots-under-certain-conditions-while-hdmi-is-connected"></a>

# System reboots under certain conditions while HDMI is connected

<a id="status"></a>

### Status

resolved

<a id="symptom"></a>

### Symptom

Bedrock R7000 reboots when HDMI display is connected in the following scenarios:

- Running lspci and accessing device 08:00.03
- Running some programs that are opening a GUI
- Installing AMD GPU Windows drivers
- Booting Windows installer

<a id="solution"></a>

### Solution

[Update to BIOS V33](../bedrock-pc/bedrock-r8000-technical-documentation/software-bedrock-r8000/bios-bedrock-r8000-r7000/bedrock-r8000-r7000-bios-image-files.md)

<a id="usb-10g-closest-to-console-port-hotplug-doesnt-work"></a>

# USB 10G (Closest to console port) hotplug doesn't work

<a id="symptom"></a>

### Symptom

When unplugging and plugging a USB device to the 10G USB port (closest one to the console port) the USB device has power but no data.

SolidRun R&D is working on solving the issue.

<a id="solution"></a>

### Solution

**Windows**: Disable USB *Power Managment* for USB Host Controller in Device Manager.

**Linux**: Add usbcore.autosuspend=-1 to grub command line

```
sudo nano /etc/default/grub
```

Find the line that starts with: `GRUB_CMDLINE_LINUX_DEFAULT`

Add the `usbcore.autosuspend=-1` argument

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash usbcore.autosuspend=-1"
```

Save the new configuration

```
update-grub
```

<a id="bedrock-reboots-once-when-booting-to-os-after-power-loss"></a>

# Bedrock reboots once when booting to OS after power loss

<a id="symptom"></a>

### Symptom

When device loses power, before booting to OS it reboots one time then boots to OS normally.

<a id="workaround"></a>

### Workaround

Let the device reboot, after which it will continue working normally, until the next power loss.

<a id="after-re-assembly-bedrock-does-not-power-up-some-features-do-not-function-properly"></a>

# After re-assembly Bedrock does not power up / some features do not function properly

<a id="symptom"></a>

### **Symptom**

- Bedrock was fully disassembled for installing RAM / NVME on SoM.  
After re-assembly Bedrock does not power up / some features do not function properly

<a id="possible-cause"></a>

### **Possible Cause**

- There are four high density B2B connectors between SoM and NIO. Connectors may not be fully connected.

<a id="solution"></a>

### **Solution**

- Disassemble and separate NIO from SoM.
- Observe the B2B connectors and their position. Ensure they are clean on both sides.
- Seat the NIO and apply pressure on the connectors to ensure the NIO is seated properly.
- Tighten NIO screws.
- Complete assembly and test power up and functionality.

Error rendering macro 'include' : com.atlassian.renderer.v2.macro.MacroException: No title provided.