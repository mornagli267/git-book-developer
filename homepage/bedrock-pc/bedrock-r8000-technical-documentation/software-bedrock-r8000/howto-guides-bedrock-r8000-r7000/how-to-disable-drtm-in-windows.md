# How to disable DRTM in Windows

To Disable DRTM in Windows follow these steps:

Open the **Group Policy Editor** (press `Win + R`, type `gpedit.msc`, and press Enter).

- Navigate to **Computer Configuration** > **Administrative Templates** > **System** > **Device Installation** > **Device Installation Restrictions**.
- Double-click **Prevent installation of devices that match any of these device IDs**.
- Set this policy to **Enabled** and then click **Show**.
- In the box that appears, enter the **Device Instance ID** or **Hardware ID** of the device you wish to block.

{% hint style="info" %}
You can get the device ID by right-clicking the device in Device Manager, selecting **Properties**, and going to the **Details** tab. From the dropdown menu, select **Device Instance Path** or **Hardware Ids**.
{% endhint %}

