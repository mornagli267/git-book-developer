
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Windows - Bedrock V3000](../Windows%20-%20Bedrock%20V3000.md)

# Connecting to Windows 11 RDP (Remote desktop connection)

Bedrock V3000 lacks an integrated display adapter. Consequently, it cannot be used with a regular monitor setup, users must connect to the windows host using RDP.

This document describesthe RDP connection process on Bedrock V3000.

## **Table of Contents**

- [Connection process](#connection-process)
- [Identifying Bedrock IP on your LAN](#identifying-bedrock-ip-on-your-lan)

  - [Method 1](#method-1)
  - [Method 2](#method-2)
- [Connecting to RDP](#connecting-to-rdp)
- [Windows](#windows)
- [Linux](#linux)

# Connection process

## Identifying Bedrock IP on your LAN

> [!IMPORTANT]
> For easier identifrication you can check the label on the back side of the Bedrock to check the mac units addresses.

### Method 1

- Connect in the Bedrock Unit to your router and wait for about 30 seconds for it to compeletely boot, get an IP and enable the RDP functionality.
- Open your routers web interface
- Find the active DHCP leases and see what is the IP of your unit  
  example: (your routers web interface will probably look different)

  ![image-20240417-135558.png](../../../../../attachments/466be255-1eb2-4537-afce-3e724194ba6c.png)

### Method 2

- Connect in the Bedrock Unit to your router and wait for about 30 seconds for it to compeletely boot, get an IP and enable the RDP functionality.
- On your pc run:

  ```java
  arp -a
  ```
- You will see something like this:

  ```java
  arp -a
  ? (192.168.XXX.XXX) at XX:XX:XX:00:00:00 [ether] on enxb04f13d1835f
  OpenWrt.lan (192.168.XXX.XXX) at XX:XX:XX:XX:XX:XX [ether] on enxb04f13d1835f
  DESKTOP-450BDI5.lan (192.168.XXX.XXX) at 94:c6:91:a9:67:0f [ether] on enxb04f13d1835f
  ? (192.168.XXX.XXX) at <incomplete> on enxb04f13d1835f
  my.firewall (192.168.1.1) at XX:XX:XX:XX:XX:XX [ether] on wlp3s0
  DESKTOP-S57BJI2.lan (192.168.17.182) at d0:63:b4:05:b3:63 [ether] on enxb04f13d1835f
  ```
- Identify the ip address of your Bedrock unit

## Connecting to RDP

> [!NOTE]
> **Default credentials:**
>
> Username: bedrock  
> password: root

### Windows

From another Windows device:

- search for remote desktop connection in your search bar.

![image-20240417-140405.png](../../../../../attachments/0780f607-63b5-4534-9ce9-011f11d7244b.png)

- Open the app and type the IP you found in the previous step

![image-20240417-140604.png](../../../../../attachments/5f562aa3-4793-4e83-b2f8-ca0f1d71b90c.png)

- Enter your devices credentials and click OK

![image-20240417-141014.png](../../../../../attachments/92e39c2a-4595-4448-aa20-58b23b861125.png)

### Linux

- instal Remmina

```java
sudo apt-add-repository ppa:remmina-ppa-team/remmina-next
sudo apt update
sudo apt install remmina remmina-plugin-rdp remmina-plugin-secret
```

- Open remmina

![image-20240417-141838.png](../../../../../attachments/63db299b-c517-45f7-9348-4aa271104cf9.png)

- Click on a new connection in the upper left corner

  ![image-20240417-142005.png](../../../../../attachments/e50263e6-25db-4e42-bc50-0aaa18155461.png)

- In the server and domain enter the IP address you found in the previous step
- Enter the username and password
- Click save and connect

> [!IMPORTANT]
> Note:  
> You can also cnhange the connection connection name in the upper part.
>
> You can also share a folder with the windows machine you are connecting to.
