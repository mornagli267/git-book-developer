
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Linux - Bedrock V3000](../Linux%20-%20Bedrock%20V3000.md)

# Enable RAID 0 on Bedrock in Linux

Bedrock V3000 provides up to 3 NVME x4 slots which support RAID 0 configuration

This guide provides step-by-step instructions for setting up a RAID array with two ADATA 256 NVME gen 3.0 drives on Ubuntu Server 23.04.

## **Table of Contents**

- [Test setup](#test-setup)
- [RAID configuration steps](#raid-configuration-steps)

  - [Create RAID partitions](#create-raid-partitions)
  - [Create RAID device](#create-raid-device)
  - [Format RAID device](#format-raid-device)
  - [Retrieve UUID of RAID partition](#retrieve-uuid-of-raid-partition)
  - [Edit fstab](#edit-fstab)
  - [Testing the configuration](#testing-the-configuration)

## **Test setup**

- 2x A-data legend 710 NVMEs
- Ubuntu Server 23.04 ([Bedrock Images & info](../../../../Other%20Articles/Snippets/Bedrock%20Images%20&%20info.md))

Performance Test Results

With RAID :

- Command: dd if=/dev/md0 of=/dev/null bs=4M status=progress; sync
- Result: 510 GB copied in 149 seconds at a rate of 3.4 GB/s.

Without RAID (Single Disk)

- Command: sudo dd if=/dev/nvme0n1 of=/dev/null bs=4M status=progress; sync
- Result: 255 GB copied in 111 seconds at a rate of 2.3 GB/s.

## **RAID Configuration Steps**

## Create RAID Partitions

For each disk you want to include in the RAID configuration:

- Run: `parted /dev/sdX mklabel gpt` to create a new GPT label
- Create a primary partition with: `parted /dev/sdX mkpart primary ext4 0% 100%`
- Set the RAID flag with: `parted /dev/sdX set 1 raid on`

### Create RAID Device

- Use mdadm to create the RAID array:

  - `mdadm --create --verbose /dev/md0 --raid-devices=<number of disks> --level=0 /dev/<partition of first disk> /dev/<partition of second disk> <more disks>`

> [!IMPORTANT]
> - Replace <number of disks>, <partition of first disk>, <partition of second disk>, <more disks>  
>   with the appropriate values.
> - The RAID device will be named /dev/md0

### Format RAID Device

- Format RAID device with: `mkfs.ext4 /dev/md0`

> [!IMPORTANT]
> /dev/md0 is used because in the previous command we created it with the name /dev/md0

### Retrieve UUID of the RAID Partition

- Run `blkid` to ge the UUID of the /dev/md0 partition

  - Example: `UUID="2ff3d24d-c123c-43d5-41ed-627bcdf54154"`

### Edit fstab File

- Open /etc/fstab using `vi /etc/fstab`
- Add the Line `<Your UUID> /home ext4 defaults 0 1`

  - Replace <>Your UUID> with the actual UUID from the previous step
  - You can also change /home which is the destination point to mount the RAID disk

### Test the Configuration

- Run `mount -a` to mount all filesystems
- Verify with `df -h` to see if the filesystem got mounted

> [!WARNING]
> Always ensure you have a backup of your data before making changes to disk or configurations.  
> RAID 0 offers improved performance but no redundancy, meaning if one disk fails, all data is lost.
