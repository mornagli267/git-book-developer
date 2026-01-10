
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [HowTo Guides - Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000.md)

# How to disable DRTM in Windows

To Disable DRTM in Windows follow these steps:

Open the **Group Policy Editor** (press `Win + R`, type `gpedit.msc`, and press Enter).

- Navigate to **Computer Configuration** > **Administrative Templates** > **System** > **Device Installation** > **Device Installation Restrictions**.
- Double-click **Prevent installation of devices that match any of these device IDs**.
- Set this policy to **Enabled** and then click **Show**.
- In the box that appears, enter the **Device Instance ID** or **Hardware ID** of the device you wish to block.

> [!IMPORTANT]
> You can get the device ID by right-clicking the device in Device Manager, selecting **Properties**, and going to the **Details** tab. From the dropdown menu, select **Device Instance Path** or **Hardware Ids**.
