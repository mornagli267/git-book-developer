# Gateway secure communication and VPN

> [!WARNING]
> The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.

<a id="included-communication-security-features"></a>

#### Included communication security features

SolidSense system comes with **openssl** to establish encrypted communication channels and **openvpn** to connect to virtual private networks.

To be able to rejoin networks or to connect to specific servers, it can be necessary to change the root certificate of the gateway

<a id="installing-new-certificates-on-the-gateway"></a>

#### Installing new certificates on the gateway

New certificates to be installed must be copied  in: /usr/local/share/ca-certificates . If that directory does not exist it shall be created: `mkdir -p /usr/local/share/ca-certificates`.

After having copied the new certificates please run:

```
sudo /usr/sbin/update-ca-certificates
```

To remove, the command to run is ‘`sudo /usr/sbin/update-ca-certificates --fresh`‘ after removing the cert from /usr/local/share/ca-certificates.