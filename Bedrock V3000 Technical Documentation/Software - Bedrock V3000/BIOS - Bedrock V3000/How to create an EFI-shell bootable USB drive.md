
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [BIOS - Bedrock V3000](../BIOS%20-%20Bedrock%20V3000.md)

# How to create an EFI-shell bootable USB drive

- [Download the UEFI Shell ISO](#download-the-uefi-shell-iso)
- [Guide for UBUNTU](#guide-for-ubuntu)
  - [Step 1: Format the USB Drive to FAT32](#step-1-format-the-usb-drive-to-fat32)
  - [Step 2: Create a FAT32 Partition on the USB (After Disk Format)](#step-2-create-a-fat32-partition-on-the-usb-after-disk-format)
  - [Step 3: Mount the UEFI Shell ISO and Copy the EFI Folder](#step-3-mount-the-uefi-shell-iso-and-copy-the-efi-folder)
- [Guide for WINDOWS](#guide-for-windows)
  - [Step 1: Format the USB Drive to FAT32](#step-1-format-the-usb-drive-to-fat32)
  - [Step 2: Mount the ISO and Copy the Files](#step-2-mount-the-iso-and-copy-the-files)

# Download the UEFI Shell ISO

1. Open your browser Go to: <https://github.com/pbatard/UEFI-Shell/releases>
2. Scroll to the latest release and download `UEFI-Shell…RELEASE.iso`

![image-20250513-085352.png](../../../../../attachments/61ad68b4-a7e4-4698-89f5-f4007df10091.png)

# Guide for UBUNTU

### Step 1: Format the USB Drive to FAT32

1. Press the **Super (Windows)** key and type `Disks` in the search.  
   Open **“Disks”** (aka **GNOME Disks**).
2. On the left panel, select your **USB drive**.

> [!WARNING]
> Double-check it’s not your system drive!

![image-20250513-090015.png](../../../../../attachments/91aebda9-93e1-4d9f-a065-78025bbebfdd.png)

3. Click the **three dots.**
4. Choose **“Format Disk…”**:

   ![image-20250513-090237.png](../../../../../attachments/d8a04981-5c3b-4d25-992c-a903c73f8518.png)

![image-20250513-090527.png](../../../../../attachments/dc2ff3a0-45d0-4364-b856-142c4df55f85.png)

5. Click **Format** . (if its ask you are you sure you want to format the disk you can click format..)

### **Step 2: Create a FAT32 Partition on the USB (After Disk Format)**

**What you should see now:**

One big block of “Free Space”

![image-20250513-091231.png](../../../../../attachments/6bee053f-c493-4864-a440-b89a46f0bea1.png)

**Now create the partition:**

1. **Select the USB drive** (make sure it's still highlighted).
2. Click the `+` **(plus)** button below the free space area.

**In the "Create Partition" window:**

1. **Size**: Leave it as default (use the full free space) and click next
2. **Name**: Call it something like `EFI-USB`
3. **Type**: choose “For use with all systems and devices (FAT)“
4. click **Create**.

![image-20250513-091702.png](../../../../../attachments/cf0fbdc3-decf-4f2a-bd8c-1e731295101e.png)

**after clicking create:**

1. Wait for the partition to finish creating.
2. Click the  **Play** button (in Disks) to **mount** the new partition (if it didn’t mount automatically).
3. Your USB will now appear in the **Files app** as a mounted drive.

   ![image-20250513-091841.png](../../../../../attachments/62121b0c-8de7-425c-9d0e-e4e05baf989c.png)

### Step 3: Mount the UEFI Shell ISO and Copy the EFI Folder

Now that your USB is formatted and mounted, you’ll copy the necessary boot files from the ISO into the USB.

1. Locate the ISO file (shoud be in the downloads folder)
2. mount the iso by right click and choose "Open With Disk Image Mounter"

   ![image-20250513-092206.png](../../../../../attachments/e6635798-0823-44d0-9355-ed14e9a10a43.png)
3. click the mounted ISO
4. copy the efi folder (right click and then copy)
5. navigate to your mounted USB drive (mine is the EFI-USB)
6. Paste the efi folder in the **root** of the USB

   ![image-20250513-092519.png](../../../../../attachments/8aa924d1-5567-46c1-9608-02cb8a19dd66.png)

> [!TIP]
> **Your USB drive is now ready**
>
> You can **safely unmount it** **(important)** from Ubuntu and **plug it into any computer** that supports UEFI.  
> After booting from the USB, the system will launch directly into the **UEFI Shell environment**.

> [!IMPORTANT]
> You can put EFI programs such as AFUEFI in the root directory of the usb drive and use these commands in the EFI shell.

# Guide for WINDOWS

## Step 1: Format the USB Drive to FAT32

1. Plug in your USB drive.
2. Open **File Explorer**, right-click your USB, and select **Format**.

   ![image-20250513-094818.png](../../../../../attachments/beec915f-2e14-4411-bb26-45ec46baca68.png)
3. In the Format window, choose:

   - **File system:** `FAT32`
   - **Volume label:** `EFI-USB` (or any name)
   - ✅ Check “Quick Format”

     - Click **Start** → then confirm the warning.

       ![image-20250513-095032.png](../../../../../attachments/9cb97532-383c-4360-95a2-828cec4e3c4d.png)![image-20250513-095119.png](../../../../../attachments/1030207b-c60b-45a0-8549-903dd2520d47.png)

## Step 2: Mount the ISO and Copy the Files

1. **Double-click** the downloaded ISO file (UEFI-Shell…RELEASE.iso)  
    It will **automatically mount** as a virtual DVD drive in File Explorer.

   ![image-20250513-101812.png](../../../../../attachments/656590cc-2a3c-4d8f-a5f7-8962fa2b1f6e.png)
2. Open the mounted ISO from the **sidebar** in File Explorer if not open automatic (it looks like a CD/DVD drive).
3. Copy all contents.

   ![image-20250513-101909.png](../../../../../attachments/a33fec77-2fd3-4640-957d-d3b0f089d875.png)
4. Navigate to your **formatted USB drive**.
5. **Paste** the copied files into the **root** of the USB (not inside any other folder).

> [!TIP]
> **Your USB drive is now ready**
>
> You can **safely unmount it** **(important)** from Ubuntu and **plug it into any computer** that supports UEFI.  
> After booting from the USB, the system will launch directly into the **UEFI Shell environment**.

> [!IMPORTANT]
> You can put EFI programs such as AFUEFI in the root directory of the usb drive and use these commands in the EFI shell.
