# Using Remote.it to access SolidSense gateway

{% hint style="warning" %}
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.
[Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.
{% endhint %}


When a gateway is in operation, it is seldom directly accessible because it own IP address is local to the sub-network it is hooked on and behind NAT routers and firewalls. A gateway can access a remote application crossing the routers (if the port is open), but the reverse is not true.

Using Kapua, it is possible to launch some commands on the gateway using the command service, but this is limited and can be tedious for complex operations and debugging.

One solution is to setup a VPN, but although this is bring some benefits by improving security and allowing 2 way communications on the VPN address space, it is also complex to setup and manage.

There is a solution on the market that has been developed to allow remote access to devices in a lightweight manner: [Remote.it.](https://remote.it/)

That service is very simple to setup and use:

1. Create an account on the service, there is a free plan to test then you can upgrade to commercial plans.
2. Install the client on the gateway (see additional information below)
3. Configure the client (see below)
4. From the web page of the service, you can then open a Kura web interface or get a proxy url to open an SSH session.

In the future release of the SolidSense platform, there will be a full integration of the [Remote.it](http://Remote.it) service to allow seamless navigation towards the gateways as well as a simplified installation process.

<a id="installing-the-remoteithttp-remoteit-client-on-the-gateway"></a>

### Installing the [Remote.it](http://Remote.it) client on the gateway

In the home (/data/solidsense) directory follow the instructions while the gateway is connected on the Internet

```
mkdir remote
cd remote
curl -LkO https://raw.githubusercontent.com/remoteit/installer/master/scripts/auto-install.sh
chmod +x ./auto-install.sh
sudo ./auto-install.sh
```

If no warning the connectd service is ready to to be configured

<a id="configuring-the-connectd-client-on-the-gateway"></a>

### Configuring the connectd client on the gateway

To perform that operation you need to have created your [Remote.it](http://Remote.it) account and the gateway need to be connected to the Internet.

We recommend to use the same device ID for this service as the one we use for Kura/Kapua as we will integrate the services in the future.

Also the recommendation is to create 2 local services:

1. Kura (http on port 80) with the naming <device id>-kura
2. ssh (on port 22 by default) with the naming <device id>-ssh

To make it simple you can run the interactive configuration: connectd\_installer. For more installation options please refer to the [Remote.it](http://Remote.it) documentation.

<a id="connecting-to-a-gateway-from-the-web"></a>

### Connecting to a gateway from the web

That is the simplest part: connect to your [Remote.it](http://Remote.it) account and you shall see all your gateways. Then you need to click on the line with the device ID you want to connect to and you will have a popup window appearing with the available services (kura and ssh as indicated above).

Clicking on <device id>-kura allow a direct access with a Kura page opening in your browser, while for ssh, you will have to copy the proxy address to open the ssh session.