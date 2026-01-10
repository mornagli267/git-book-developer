
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Windows - Bedrock V3000](../Windows%20-%20Bedrock%20V3000.md)

# Bedrock V3000 drivers

### **LTE / 5G Modem Drivers**

- [![](https://developer.resources.solid-run.com/wiki/download/thumbnails/537001992/Quectel_LTE_Windows_USB_Driver_For_MBIM_V1.0.exe?version=1&modificationDate=1700643482735&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/537001992/Quectel_LTE_Windows_USB_Driver_For_MBIM_V1.0.exe?version=1&modificationDate=1700643482735&cacheVersion=1&api=v2)
- [![](https://developer.resources.solid-run.com/wiki/download/thumbnails/537001992/Quectel_Windows_USB_Driver(Q)_NDIS_V2.2.exe?version=1&modificationDate=1700643482743&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/537001992/Quectel_Windows_USB_Driver(Q)_NDIS_V2.2.exe?version=1&modificationDate=1700643482743&cacheVersion=1&api=v2)
- [![](https://developer.resources.solid-run.com/wiki/download/thumbnails/537001992/Quectel_Windows_USB_Driver(Q)_RNDIS_V1.1.4.zip?version=1&modificationDate=1700643473698&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/537001992/Quectel_Windows_USB_Driver(Q)_RNDIS_V1.1.4.zip?version=1&modificationDate=1700643473698&cacheVersion=1&api=v2)

### Intel Ethernet drivers

[![](https://developer.resources.solid-run.com/wiki/download/thumbnails/537001992/PRO2500.zip?version=1&modificationDate=1700643482750&cacheVersion=1&api=v2&viewType=fileMacro)](/wiki/download/attachments/537001992/PRO2500.zip?version=1&modificationDate=1700643482750&cacheVersion=1&api=v2)

While Intel's i226-TI drivers are typically auto-installed during a Windows update, there might be instances where they aren't.  
If that's the case, please follow the installation instructions below.

### **Installation Instructions for Intel Ethernet Drivers**:

1. **Access the Device Manager**:

   - Right-click on the Windows taskbar menu.
   - Select "Device Manager" from the dropdown.
2. **Identify if driver is missing**:

   - If the drivers are **not installed**, an "Ethernet Controller" entry will appear under the "Other Devices" tab.
3. **Install the Drivers**:

   - Click on the "Action" tab at the top.
   - Select "Add drivers" from the dropdown.
   - Navigate to the extracted `PRO2500` directory and choose the appropriate sub-directory corresponding to your Windows version.
   - Click "OK."
4. **Finalize the Installation**:

   - Windows will automatically detect and install the required drivers for the NICs.
   - It might be necessary to reboot or power cycle your system to ensure the NICs function correctly.
