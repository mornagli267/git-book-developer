# Increase VRAM for iGPU

**Introduction:** This guide provides detailed instructions for increasing Video RAM (VRAM) on Bedrock systems.

**Increasing VRAM: Step-by-Step**

1. **Enter BIOS:**
  - Restart your computer.
  - Repeatedly press the “DEL” key until the BIOS menu appears.
2. **Navigate to Advanced Settings:**
  - Once in the BIOS menu, select the 'Advanced' tab.
3. **Select AMD CBS:**
  - Find and select the 'AMD CBS' option from the list.
4. **Access NBIO Common Options:**
  - Within AMD CBS, navigate to 'NBIO Common Options'.
5. **Open GFX Configuration:**
  - In NBIO Common Options, select 'GFX Configuration'.
6. **Change iGPU Configuration:**
  - Set 'iGPU Configuration' to 'UMA\_SPECIFIED'.
  - This setting allows manual specification of VRAM.
7. **Adjust UMA Frame Buffer Size:**
  - Upon selecting 'UMA\_SPECIFIED', the 'UMA Frame Buffer Size' option will become available.
  - Here, you can set the VRAM to your desired size.
8. **VRAM Size Options:**
  - Choose from various sizes:
    - Auto
    - 64M
    - 128M
    - 256M
    - 284M
    - 512M
    - 80M
    - 96M
    - 768M
    - 1G
    - 2G
    - 3G
    - 4G
    - 8G
    - 16G
9. **Save and Exit:**
  - After setting the desired VRAM size, save your changes.
  - Exit the BIOS and restart your computer for the changes to take effect

{% hint style="warning" %}
**Troubleshooting:**
- If your system fails to boot or displays graphics issues after changing VRAM settings, use the BIOS reset button loacted near the console port to reset the BIOS settings to default.
{% endhint %}

