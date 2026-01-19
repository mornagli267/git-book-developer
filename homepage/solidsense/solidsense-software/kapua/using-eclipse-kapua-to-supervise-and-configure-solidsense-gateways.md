# Using Eclipse Kapua to supervise and configure SolidSense gateways

{% hint style="warning" %}
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.\
[Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.
{% endhint %}


## Foreword

Kapua is an Open Source cloud IoT platform managed by the Eclipse IoT group under the Eclipse foundation. It is made available to SolidSense users under the Eclipse license for test. The system can be used during Proof of Concept phase but is not intended to be used for production. There is no service warranty associated with the SolidSense Kapua instance.

Full Kapua documentation can be found on: [https://www.eclipse.org/kapua/documentation.php](https://www.eclipse.org/kapua/documentation.php)

It is recommended for customer intending to use Kapua for their production environment to install their own instance in their production environment.

## Connecting to Kapua

The current URL to access the SolidSense Kapua is [https://kapua.solidsense.io](https://kapua.solidsense.io/)

To connect to Kapua you need the username and password that have been assigned to you for your account by Solid-Run. This is allowing you to access Kapua a see all gateways assigned to your organization and only these ones.

This article is just a quick start guide for Kapua and does not by far describe all the available features.

![](../../../../.gitbook/assets/Kapua-Login.png)

Then select **Devices** on the left to see all the gateways of your account

## Managing devices

![](../../../../.gitbook/assets/Kapua-Devices.png)

Devices with a green plug are connected while those with a yellow plug are not yet reachable and no action can be performed on these gateways. By clicking on 1 gateway connected there several information actions that can be done using the series of tabs below.

If a device that is expected to be seen is not appearing, this is most of the case a problem with the gateway MQTT credentials (account/username/password). Please re-check these parameters.

![](../../../../.gitbook/assets/Kapua-Devices-Actions.png)

### Possible actions/information available

* Description: access to the device/Kura main parameters
* Tags => feature not described here
* Events: list of all events related to the device. Allow to see when the device has been connected or disconnected. Events are available even if the device is not connected
* Packages: list of optional packages (like the Wirepas configuration package) installed in Kura on the gateway. New package can also be added here.
* Bundles: list of all software bundles (Java components) installed on the gateway. Linked to the OSGi framework.
* Configuration: access to the configuration off all services running on the gateway and also to the configuration snapshots that can be downloaded for examination and uploaded to force a configuration change. Rollback to previous state can also be triggered here.
* Commands: capability to send Linux command line commands to be executed on the gateway. The working directory in /tmp. Some files can be uploaded on the gateway (and will be stored in /tmp) in .zip format and will be unzipped automatically after download. Non zipped file will NOT be downloaded. This service (Command Service) needs to be enabled either on Kura or on Kapua before use.

![](../../../../.gitbook/assets/Kapua-Devices-Configuration.png)

{% hint style="warning" %}
**Please note** Changing the MQTT data transport parameters allow to re-parent a gateway to another account or another cloud, but if any parameter is wrong a direct connection to the gateway (via Kura web) will be needed to recover.
{% endhint %}


![](../../../../.gitbook/assets/Kapua-Devices-Commands.png)

{% hint style="warning" %}
**Please note** Commands are executed as root and there is no control nor security mechanism. So to use with great care to avoid to put the gateway in a non reachable state to will force a field operation to recover it.
{% endhint %}


## Managing Kapua account

### Adding user(s) to your account

It is always possible to add new users to your account using the Users screen

![](../../../../.gitbook/assets/Kapua-Users.png)

Click on the +add button and a pop-up window will open asking for the user name and password. Warning password rule is enforced and you need to follow the indications.

After the user as been created you need to assign to him a role and permissions otherwise it will not be able to perform any task. This is done using the bottom part of the screen with the Roles and Permissions tab.

### Adding Child Accounts

This is a powerful feature of Kapua. You can create a hierarchy of accounts to which user and gateways will be attached. Users belonging to an account at one particular level of the hierarchy will have access to all gateway that account and all child accounts. This is mainly used to create multi-tenant schemes where you can create child accounts per customer (or site or whatever) and then create accounts for gateways and users in that specific account.

![](../../../../.gitbook/assets/Kapua-Child-account.png)

After creating a child account you need to adjust the following settings:

* Account service: to allow child accounts to be created from that account, so one more level in the herarchy
* Device Registry service: to allow devices (gateways) to connect to this Kapua instance
* User service: to allow creation of users associated with that account

Then we recommend to create 2 users associated with the new account:

* One for the Kapua login with the admin role
* One for the gateways with the thing role
