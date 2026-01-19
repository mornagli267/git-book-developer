# Using Kura gateway application framework

{% hint style="warning" %}
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.
{% endhint %}


## Introduction

The SolidSense gateways are delivered equipped with the [Eclipse IoT framework Kura](https://www.eclipse.org/kura/index.php). This framework is used by the SolidSense solution for configuration purpose but nothing prevents to go further and build application on top of Kura.

Kura is a Java/OSGi framework that provides a comprehensive foundation to build an IoT gateway and SolidRun has selected it to provide an open source extensible basis for its customers. Not all applications need to be mapped inside the Kura structure and SolidSense is also providing independent micro services for those who prefer developing their application in other languages than Java.

This article is not intended to provide a full documentation for Kura as this is already existing [here](https://wiki.eclipse.org/Kura). It shall be noted that Solid Run is providing a limited support on Kura operations and no support on Kura development.

SolidSense is using the framework as is except the cellular modem interface to allow the native support of the modems supported by the gateway configurations. Users who would like to develop their own packages can start from the existing public repository. All existing Kura add-ons from the marketplace shall work as documented, but Solid Run is not giving any support for that, all problems needs to be reported to the add-on publisher.

## Kura menus

![](../../../../.gitbook/assets/image-20211226-130038.png)

The Kura left menu is divided in 2 parts:

* The system menu, that is common to all Kura instances
* The service menu, that can be configured as services can be added or removed

### The Kura system menu

#### Status

This page summarize the status of the gateway for the following aspects:

* Connection to Kapua
* Network configuration
* Position => the position is the one from the Position Service and refer to the corresponding section

#### Device

This page is giving the configuration and running status of the Kura system running on the JVM, not the underlying Linux system configuration and status.

The command tab allow to execute Linux commands if the Command service is enabled.

#### Network

The page allows the configuration of the 3 network interfaces Ethernet, WiFi and Cellular. The basic configuration principles are explained in the [Configuring and testing the Wirepas gateway software](https://solidrun.atlassian.net/wiki/spaces/developer/pages/263946241) . For gateways that are remote, an extreme care needs to be taken when re-configuring the network as it can result in communication loss requiring to send someone locally for recovery.

The Ethernet and WiFi interfaces can be configured as LAN or WAN interfaces and obviously the Cellular interface only as WAN. Only ONE WAN interface can be configured at a given time, so to switch from one WAN interface to another, the initial interface must be either disabled or configured as LAN.

#### Firewall

The firewall is also a key element to be configured in particular for security purpose as every open port is a possible backdoor entry point. We recommend to remove all non required open port for the production machines.

#### Cloud connection

The page is used to configure the connection between Kura and cloud applications. By default, only the connection between Kura and Kapua for device management is used. It include 3 tabs, but only the 3rd one “MQTT Data Transport” is to be configured.

![](../../../../.gitbook/assets/image-20211226-130100.png)

The field values depends on the Kapua instance to which the gateway is to be connected:

1. Broker URL:Kapua instance URL or IP and port
2. Account-Name: the child account ([Using Eclipse Kapua to supervise and configure SolidSense gateways | Managing-Kapua-account](../kapua/using-eclipse-kapua-to-supervise-and-configure-solidsense-gateways.md#managing-kapua-account) ) used to access the gateway data
3. Username and password as defined in Kapua for the gateway connection (Thing role)

We recommend not to modify the other fields, without having a good knowledge of the Kura/Kapua features.

#### Drivers and assets

These are the main Kura objects to build local programming using Wire graphs. Drivers are implementing a specific protocol over a physical interface while Assets represent specific devices communicating over a Driver. Assets can have associated Channels.

Developing Drivers requires to write Java code and is well documented in the Kura documentation. There is a set of already existing drivers on the [Eclipse marketplace](https://marketplace.eclipse.org/) (note that you need an Eclipse account to access the add-ons).

There is today no specific SolidSense drivers, but if some particular needs are raised, Solid Run will look into possible joint or co-development.

#### Wire Graph

The Wire Graph page allow visual programming on the gateway. This is useful if you have Drivers and Assets defined. Some computing components are available on the Eclipse Marketplace.

#### Packages

This page allow to add new optional packages or to remove some of them. In the SolidSense solution there is only one optional package: wirepasConfiguration. Other packages can be either found on the Marketplace (see above) or develop by the users.

#### Settings

The key feature here is the snapshot management. The snapshots store the state of Kura configuration after each configuration change. The first snapshot “snapshot 0” is the one with the initial configuration of the gateway. Rolling back to snapshot 0 is erasing all configuration steps made after the initial Kura boot. The snapshots are stored encrypted on the gateway hard disk but can be downloaded via the Kura interface in plain XML.

The snapshot 0 can be replaced un-encrypted, but will be encrypted automatically upon Kura start. It is possible to use a particular snapshot and to use it as snapshot 0, but these snapshot are not generic and the XML will have to be edited to replace gateway specific data like hostname. The snapshot 0 is taken into account only when it is the only file in the directory.

### The Kura Services menu

Here is described the main additional services and their usage in the context of SolidSense. Services that have no use in the SolidSense context are not described.

#### Artemis MQTT Broker

Simple local MQTT Broker. Useful when a local broker is needed.

#### Clock service

Parameters for the NTP clock service to keep the local clock synchronized.

#### Command service

Enable the capacity to send command via the Web interface or Kapua

#### Webconsole

Credentials settings for Kura web login

#### Position service

This service allow to set a position or to retrieve it from the GPS. There is no permanent publication of the position via MQTT and this this cannot be used to track the gateway position. This is a static indication.

On SolidSense with LTE/GPS module integrated the GPS must be manually enabled to allow this feature to work.

#### Watchdog service

Allow automatic reboot if the system hangs.
