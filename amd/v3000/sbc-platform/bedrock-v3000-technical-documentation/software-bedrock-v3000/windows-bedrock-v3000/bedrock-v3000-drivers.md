# Bedrock V3000 drivers

<a id="lte-5g-modem-drivers"></a>

### **LTE / 5G Modem Drivers**

- [Quectel_LTE_Windows_USB_Driver_For_MBIM_V1.0.exe](./attachments/Quectel_LTE_Windows_USB_Driver_For_MBIM_V1.0.exe)
- [Quectel_Windows_USB_Driver(Q)_NDIS_V2.2.exe](./attachments/Quectel_Windows_USB_Driver(Q)_NDIS_V2.2.exe)
- [Quectel_Windows_USB_Driver(Q)_RNDIS_V1.1.4.zip](./attachments/Quectel_Windows_USB_Driver(Q)_RNDIS_V1.1.4.zip)

<a id="intel-ethernet-drivers"></a>

### Intel Ethernet drivers

[PRO2500.zip](./attachments/PRO2500.zip)

While Intel's i226-TI drivers are typically auto-installed during a Windows update, there might be instances where they aren't.  
If that's the case, please follow the installation instructions below.

<a id="installation-instructions-for-intel-ethernet-drivers"></a>

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