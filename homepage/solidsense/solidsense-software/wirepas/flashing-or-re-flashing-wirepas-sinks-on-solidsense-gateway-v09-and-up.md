# Flashing or Re-flashing Wirepas sinks on SolidSense gateway (V0.9 and up)

{% hint style="warning" %}
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.\
[Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.
{% endhint %}


#### Foreword

This article describe the procedure to flash the Wirepas stack on one or both of the of the Nordic chip available for that purpose on the gateway. This procedure is provided only for Wirepas licensees (having a full development license) that are flashing the sinks part of their license. For user not having a Wirepas development license they shall buy the gateways with the Wirepas stack installed by SolidRun.

For reference versus the picture below (N6 Indoor):

* Sink1 is the lower antenna corresponding to the device /dev/ttymxc1
* Sink2 is the left antenna corresponding to the device /dev/ttymxc2

![](../../../../.gitbook/assets/SolidSense-Indoor-Layout-v2.png)

#### Prerequisite

The first task is to generate your Wirepas binary (hex file) that is compatible with the SolidSense gateway internal wiring. To generate this firmware file you need to be a Wirepas licensee and have the Nordic development environment installed on your system. SolidRun does not provide any support concerning that development.

**The Wirepas application to be used is the standard dual MCU application unless some specific features have to be installed in the sink.**

Here is the table of the pin assignment to be used in the firmware

| Model/Chip                     | Direction | Pin |
| ------------------------------ | --------- | --- |
| Indoor/Nina B1                 | TX        | 6   |
| Indoor/Nina B1                 | RX        | 5   |
| Outdoor or Industrial /Nina B3 | TX        | 45  |
| Outdoor or Industrial /Nina B3 | RX        | 29  |

Baud rate used for connection is : 125000. This is to match with the Sink Service

For N6 Indoor and Outdoor versions here is the schematic if needed:&#x20;

[ublox-pinout-solidsense-v20.pdf](attachments/ublox-pinout-solidsense-v20.pdf)

The gateway firmware level must be at least solidsense-V0.9-2019111100 (This can be verified by checking the Device page in Kura). If you are not in that revision or up please ask Solid Run support for assistance.

{% hint style="warning" %}
**Warning: Flashing a Nordic chip with the Wirepas stack is erasing the MAC address of the chip. The chip can then be reprogrammed when needed but a specific process is to be applied (contact support).**
{% endhint %}


All operations require to access the gateway via ssh. ([SSH / FTP access to SolidSense gateway](../other-software-articles/ssh-ftp-access-to-solidsense-gateway.md) )

#### Flashing the Nordic chip with Wirepas stack

This paragraph is dedicated to customers having a Wirepas license to flash the Wirepas stack into the Nordic chips. The Wirepas subsystem is not activated on the gateway when the provisioning subsystem does not find a valid stack on at least one sink. By consequence, the flashing operation can directly start.

```
cd /opt/scripts
# Copy locally the firmware hex file - this is an example 
wget '<Your URL for the Wirepas hex file>' -O /tmp/wp_fw.hex
# flashing the FW to sink1 
sudo /opt/scripts/flash_ublox --sink 1 --type wirepas /tmp/wp_fw.hex 
# flashing the FW to sink2 
sudo /opt/scripts/flash_ublox --sink 2 --type wirepas /tmp/wp_fw.hex
```

Here is a example of a successful flash operation:

```
root@BS191400648:/opt/scripts# /opt/scripts/flash_ublox --sink 1 --type wirepas /tmp/wp_fw.hex 
Checking chip state
Chip is running, halting...
Chip is protected state!
Programming flash of type <wirepas> with file <wp_fw.hex>.
wrote 121312 bytes from file /tmp/wp_fw.hex in 21.538822s (5.500 KiB/s)
```

After flashing the simplest solution to enable Wirepas is to use the [Configuring and testing the Wirepas gateway software | Prerequisite-and-installation](configuring-and-testing-the-wirepas-gateway-software.md#prerequisite-and-installation) .

#### Flashing the Wirepas sink for upgrade

The procedure is valid for performing a hard upgrade of the chip.

Then perform the following commands while in the **/opt/scripts** directory.

```
cd /opt/scripts
# sudo chmod +x /opt/scripts/flash # only in case of execution error
# If the Wirepas service is already installed the transport (Data) service needs to be stopped as well
sudo systemctl stop wirepasTransport1
# sudo systemctl stop wirepasTransport2 (only if activated)
# Stop the Wirepas sink service during the firmware upgrade
sudo systemctl stop wirepasSink1
sudo systemctl stop wirepasSink2
# Copy locally the firmware hex file - this is an example 
wget '<Your URL for the Wirepas hex file>' -O /tmp/wp_fw.hex 
# flashing the FW to sink1 
sudo /opt/scripts/flash_ublox --sink 1 --type wirepas /tmp/wp_fw.hex 
# flashing the FW to sink2 
sudo /opt/scripts/flash_ublox --sink 2 --type wirepas /tmp/wp_fw.hex
# restart the Wirepas sink services 
sudo systemctl start wirepasSink1 
sudo systemctl start wirepasSink2
# checking if the services are running 
sudo systemctl status wirepasSink1 
sudo systemctl status wirepasSink2
```

After that operations it is necessary to re-configure the sink with the right values and re-start the transport (data) service. This needs to be done via the web interface: [Configuring and testing the Wirepas gateway software | Configuring-the-sink-service-with-Kura](configuring-and-testing-the-wirepas-gateway-software.md#configuring-the-sink-service-with-kura) .

Once the sink(s) have been configured, then the transport service can be restarted either via the web interface, Or directly via  the systemctl command.
