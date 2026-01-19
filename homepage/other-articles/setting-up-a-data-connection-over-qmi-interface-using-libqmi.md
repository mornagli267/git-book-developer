# Setting up a data connection over QMI interface using libqmi

<a id="revision-and-notes"></a>

## Revision and Notes

| **Date** | **Owner** | **Revision** | **Notes** |
| --- | --- | --- | --- |
| 08 Mar 2022 |     | 1.0 | Initial release |
| Table of Contents | - [Revision and Notes](#revision-and-notes)<br>- [Introduction](#introduction)<br>- [Step-By-Step](#step-by-step)<br>- [Checking the Connection](#checking-the-connection) |     |     |

<a id="introduction"></a>

## Introduction

Cellular modules that are based on the Qualcomm chipsets support the QMI interface. The libqmi can be used to establish QMI interface for mini PCIe modules

<a id="step-by-step"></a>

## Step-By-Step

1\. Install the libqmi Linux library e.g. by using your system package manager like apt or preferably latest version from source on the Freedesktop pages for libqmi project: [https://www.freedesktop.org/wiki/Software/libqmi/](https://www.freedesktop.org/wiki/Software/libqmi/)

2\. Verify that you have the Linux in-kernel qmi\_wwan driver installed and attached for the cellular modules QMI interface over USB using:

```
lsusb -t
```

Should return driver information, it can look e.g like this:

```
        |__ Port 3: Dev 3, If 4, Class=Vendor Specific Class, Driver=qmi_wwan, 480M
```

- You can load the qmi\_wwan kernel module by running:
```
root@sr-imx8:/home/debian# modprobe qmi_wwan
[ 3342.100394] usbcore: registered new interface driver cdc_wdm
[ 3342.109771] usbcore: registered new interface driver qmi_wwan
```
- The cellular modules QMI control interface are usually named cdc-wdm\* e.g.:
```
qmicli --device=/dev/cdc-wdm0
```

{% hint style="info" %}
**Note:**
If the driver is not correctly loaded, please verify that the module is set to expose the correct USB endpoints configuration toward the host system and that you have followed the provided guides from the cellular module vendors, regarding how to implement the module in Linux.
{% endhint %}


3.Install the required packages

```
sudo apt-get update 
sudo apt-get install libqmi-utils udhcpc
sudo reboot
```

4\. Use the following command to make sure module is ready:

```
root@sr-imx8:/home/debian# sudo qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
[/dev/cdc-wdm0] Operating mode retrieved:
        Mode: 'online'
        HW restricted: 'no'
```

Should return `'online'`. If not, try :

```
sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode='online'
```

5\. Configure the network interface for the raw-ip protocol

```
sudo ip link set wwan0 down
```

6\. Set the wwan0 interface to raw mode

```
echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip
```

7\. Restart the interface

```
sudo ip link set wwan0 up 
```

8\. Once the wwan0 is up, gather the APN information for your SIM card and start the qui network by changing the `apn='YOUR_APN',username='YOUR_USERNAME',password='YOUR_PASSWORD'` part of the line according to the information of your SIM & operator. If username and password are not required, delete those parameters.

```
sudo qmicli -p -d /dev/cdc-wdm0 --device-open-net='net-raw-ip|net-no-qos-header' --wds-start-network="apn='YOUR_APN',username='YOUR_USERNAME',password='YOUR_PASSWORD',ip-type=4" --client-no-release-cid
```

{% hint style="info" %}
**Note:**
Your APN information will vary according to the card you have.
{% endhint %}


You will get something similar to this:

```
[/dev/cdc-wdm0] Network started
Packet data handle: '3781840224'
[/dev/cdc-wdm0] Client ID not released:
Service: 'wds'
CID: '20'
```

Once “Network started” is displayed, you can send a DHCP request on the network interface.

9\. Acquire an IP number from your provider

```
 sudo udhcpc -q -f -i wwan0
```

You will get something similar to this:

```
udhcpc: started, v1.30.1
No resolv.conf for interface wwan0.udhcpc
udhcpc: sending discover
udhcpc: sending select for 10.165.xx.xx
udhcpc: lease of 10.165.xx.xx obtained, lease time 7200
Too few arguments.
Too few arguments.
```

<a id="checking-the-connection"></a>

## Checking the Connection

Now check the assigned IP address and test the connection

```
ifconfig
```

You will get something like this:

```
...
wwan0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST> mtu 1500
inet 10.165.xx.xx netmask 255.255.255.252 destination 10.165.xx.xx
unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00 txqueuelen 1000 (UNSPEC)
RX packets 2 bytes 612 (612.0 B)
RX errors 0 dropped 0 overruns 0 frame 0
TX packets 75 bytes 12478 (12.1 KiB)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
```

Test network connectivity:

```
ping -I wwan0 -c 5 sixfab.com
```

You will get something similar to this:

```
PING sixfab.com (172.67.75.126) from 100.67.114.164 wwan0: 56(84) bytes of data.
64 bytes from 172.67.75.126 (172.67.75.126): icmp_seq=1 ttl=29 time=247 ms
64 bytes from 172.67.75.126 (172.67.75.126): icmp_seq=2 ttl=29 time=205 ms
64 bytes from 172.67.75.126 (172.67.75.126): icmp_seq=3 ttl=29 time=207 ms
64 bytes from 172.67.75.126 (172.67.75.126): icmp_seq=4 ttl=29 time=204 ms
64 bytes from 172.67.75.126 (172.67.75.126): icmp_seq=5 ttl=29 time=216 ms

--- sixfab.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 8ms
rtt min/avg/max/mdev = 204.050/215.839/247.004/16.201 ms
```

Enjoy your internet connection !