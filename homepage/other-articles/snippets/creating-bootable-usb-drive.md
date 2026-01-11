# Creating Bootable USB drive

This step requires a host PC running Linux.

- Download the required disk image file
- Connect a USB thumb drive to your pc
- Run command:   
`lsblk`
- Identify your drive (usually /dev/sdX, X can be different for each system) 
  - NOTE: SATA HDDs & SSDs also identify as sdX so be careful not to corrupt your data.
- Unmount your drive from the system if mounted using `umount`
- Run command:  
`sudo dd if=${path/to/image/file} of=/dev/sdX bs=1M status=progress; sync`
- Wait until dd finishes and you get a prompt again, safely eject the USB drive.