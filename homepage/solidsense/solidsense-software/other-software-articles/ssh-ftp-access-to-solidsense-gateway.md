# SSH / FTP access to SolidSense gateway

> [!WARNING]
> The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.  
> [Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.

<a id="ssh-access"></a>

#### SSH Access

For specific operations it can be useful to have a direct SSH to the gateway. This is also the case for users that wants to add their specific applications or configuration. In most of the case SSH access can be possible only through LAN access. WAN are generally using firewalls and NAT that are making the direct SSH login on the gateway impossible. However, there are some possibilities that are explained here [Using Remote.it to access SolidSense gateway](https://solidrun.atlassian.net/wiki/spaces/developer/pages/265027593)

The first step is to know your network configuration, the simplest is to get it via Kura ([Configuring SolidSense networking with Kura](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287179294) )

With the default gateway configuration the simplest is to use the WiFi access point:

- SSID => gateway serial number
- passphrase => ‘testKEYS’
- IP => 172.16.1.1

Then you need to have the SSH credentials to access to the gateway that can requested to [SolidRun support](mailto:solidsense-support@solid-run.com). Then you have the access to the gateway via SSH . There is no root access, but the default user is an sudoer.

<a id="ftp-access"></a>

#### FTP access

**it shall be noted the sftp is also available from version 0.911 on. So you can use tools like FileZilla to transfer files from and to the gateway.**  

Warning only the sftp protocol is supported by the default configuration so the host shall be specified as for instance sftp://172.16.1.1