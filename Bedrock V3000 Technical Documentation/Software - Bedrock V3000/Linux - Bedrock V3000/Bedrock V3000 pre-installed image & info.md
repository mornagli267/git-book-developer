
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Linux - Bedrock V3000](../Linux%20-%20Bedrock%20V3000.md)

# Bedrock V3000 pre-installed image & info

Below, you will find a list of available images, each with a unique MD5 checksum to ensure integrity and security.  
Please verify the MD5 checksum after downloading to ensure the file has not been tampered with or corrupted during the download process.

## Available Images

### Image 1: Ubuntu Desktop 22.04.3

- **Description:** Ubuntu Desktop 22.04.3 with enabled ttyS4 shell on startup.
- **Version:** 1.0
- **File Size:** 12G
- **Release Date:** 30-Nov-2023
- **MD5 Sum:** 93428a1ca97a521c1495e6932d1107c7
- **Download Link**  
  [Download Ubuntu\_Desktop\_22.04.3.img.gz](https://solidrn-my.sharepoint.com/:u:/g/personal/lior_jigalo_solid-run_com/ESRdybdJO79ArPhp-o0zEbMB4yFAx9aZ5YMNdrrT1PdYTQ?e=PsOtbU)

### Image 2: Ubuntu Server 23.04

- **Description:** Ubuntu server 23.04 pre installed image.
- **Version:** 2
- **File Size:** 2 GB.
- **Release Date:** 10-JUL-2024
- **MD5 Sum:** ac2727ef63b194435d7ebc3dc8dda2ec
- **Download Link**  
  **Temporarily unavailable**

> [!IMPORTANT]
> Early Bedrock V3000 samples shipped before 06-Sep-2023 have Ubuntu server 22.04 without the AMD kernel, it is recommended to upgrade to the newer version.

## How to Verify MD5 Checksums

To ensure the integrity of your download, please use the following instructions to verify the MD5 checksum on your platform:

- **Windows:** Use a utility like `certUtil` - Command example: `certUtil -hashfile path-to-your-file MD5`
- **Linux/macOS:** Use the `md5` or `md5sum` command from a terminal - Command example: `md5sum path-to-your-file`
