# Configuration provisioning of the SolidSense gateways

{% hint style="warning" %}
**Please Note**
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.
[Here](https://github.com/solidsense-connect/solidsense-connect-gateway/wiki) is the Solidsense-Connect WiKi documentation page.
{% endhint %}


The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.

<a id="introduction"></a>

## Introduction

Configuring the gateway with the customized configuration can become a burden if many gateways have to be configured. To address this problem a provisioning service has been develop and allow to define any configuration from a YAML definition file. There is a generic minimum configuration part of the factory (read-only) image that allows a basic start of the system allowing further configurations via Kura. On top, a custom configuration can be defined that will override and/or augment the basic configuration to create the operational configuration needed for the application. With that service we can have gateways that start and go into service without any on site provisioning activities.

The SolidSense provisioning is taking Yaml files as input (factory basic configuration + custom configuration) and generates the key system configuration files:

- Kura configurations files and mainly the snapshot\_0.xml
- WiFi configuration files
- ppp configuration files
- SolidSense configuration files

**Having your SolidSense provisioning file allows to commission all your gateways without any manual entry so with efficiency and reliability.**

<a id="factory-configuration-read-only"></a>

## Factory configuration (read-only)

The factory configuration includes 2 files that shall be located in /opt/SolidSense/config

1. SolidSense-conf-base.yml => Generic standard configuration
2. SolidSense-HW-configurations => Definition of HW configuration description

The provisioning process also make use of files located in /opt/SolidSense/template

<a id="default-configuration"></a>

### Default configuration

Network:  
Ethernet (eth0): WAN DHCP client  
WiFi (wlan0) : LAN Access Point (WPA2) DHCP Server SSID=Serial Number  
Cellular (ppp0) : Not configured

Services:  
MQTT Client for Kura: enabled  
modem\_gps: enabled if the modem is present

<a id="defining-a-custom-startup-configuration"></a>

## Defining a custom startup configuration

Here are some examples that can be pasted into your own SolidSense-conf-custom.yml file. And an example file that includes Wirepas parameters and ppp [SolidSense-conf-custom.yml](https://images.solidsense.io/SolidSense/config/SolidSense-conf-custom.yml)

<a id="structure-of-the-yaml-configuration-file"></a>

### Structure of the Yaml configuration file

The file includes two main sections:

The ‘gateway’ section in which global variables can be defined

```
gateway:

    snapshot_0: snapshot_0.xml #this is the template snapshot do not change it unless full test
    #
    # set of global variables (for convenience and example)
    #
    MQTT_BROKER: YOUR_MQTT_URL
    MQTT_PORT: 1883
    MQTT_USER: YOUR_USER
    MQTT_PASSWORD: YOUR_PASSWORD
```

The ‘services’ section that is a list of ‘service’ that have the following structure

```
- service:
    type: WirepasSink
    name: sink1
    state: active
    parameters:
        configuration: WirepasSinkConfigurationService
        plugin: WirepasConfigurationService.dp
        plugin_name: WirepasConfigurationService
        system: wirepasSink1
        port: ttymxc1 # physical port
        start: true

    variables:
        NETWORK_ID: $WP_TEST_ID
        NETWORK_CHANNEL: $WP_TEST_CHANNEL
        ADDRESS: $UNIQUE_ADDRESS0
    properties:
        sinkAddress: $ADDRESS
        networkChannel: $NETWORK_CHANNEL
        networkAddress: $NETWORK_ID
        sinkName: $service_name
```

<a id="services-definition"></a>

#### Services definition

Each ‘service’ has the following possible parameters

- ‘type’: the service class as defined by the SolidSense provisioning system
- ‘name’: the internal name of the service. For network interfaces it shall be identical to the device name
- ‘state’: the state of the service after provisioning
```
#   disabled    the service will not be configured and and started
#   auto        the service is configured but the start and activation is done by another process or context dependant
#   interactive the service configuration is to be done via Kura
#   active      the service is configured and activared during provisioning
```
- ‘override’: If *true*, then the existing default configuration is ignored and the service is refined from scratch, if *false* then all existing configuration is kept and only the parameters specified in the file are modified.
- ‘parameters’. This is a set of values that are used to configure the service.
- ‘variables’. List of local variable definitions
- ‘properties’: This is the list of the Kura properties that are set during the provisioning stage and written in the snapshot\_0.xml file. Only modified or additional properties needs to be defined in the file otherwise default values from the baseline snapshot\_0.xml file are used.

Among parameters some a class specific but some others are generic, in particular for all services from the *KuraService* class and subclasses.

- ‘configuration’ : Name of the ‘configuration’ XML block in Snapshot\_0 file. It can be prefixed by “org.eclipse.kura.<service>.” This prefix is to be ignored.
- ‘plugin’ : when the service requires a dynamic plugin add-on in Kura, this is the file name of the compiled dp. (shall be in: /opt/eclipse/kura/packages). Versions suffix are not taken into account.
- ‘plugin\_name’ : As a dynamic plugin file can include several services, this is the name of the class (in Java) associated with the service
- ‘prefix’ : this is the prefix used for properties. If no prefix is defined, then the full property name is to be explicitly given for the property
- ‘system’: systemd service associated with the service

<a id="solidsense-provisioning-classes-hierarchy"></a>

### SolidSense provisioning classes hierarchy

```
SolidSenseService                              # global abstract super class
    KuraService                                # default class for Kura ConfigurationService each 
        NetworkService                         # default class for network interfaces (Ethernet)
            WiFiService                        # class supporting WiFi configuration
            PppService                         # Class supporting ppp configuration
        WirepasSink                            # Class supporting sink configuration
        WirepasTransport                       # Class supporting data transport configuration
        WirepasMicroService
        MQTTService                            # Class supporting SolidSense MQTT service configuration
        FirewallService                        # class supporting Firewall configuration
    BluetoothService                           # class supporting ble activation on hc1 hc2
    BLEClientService                           # class supporting BLE Client internal configuration (no screens)
    ModemGPS                                   # class supporting Modem internal configuration
```

<a id="example-1-cellular-as-wan-and-ethernet-as-lan"></a>

### Example 1: cellular as WAN and Ethernet as LAN

```
#
#   state is used for activable services (pure data services don't need one)
#   disabled    the service will not be configured and and started
#   auto        the service is configured but the start and activation is done by another process or context dependant
#   interactive the service configuration is to be done via Kura
#   active      the service is configured and activared during provisioning
#
#   override    (true by default) replace the default service definition, false, combine both definitions
#
# Global variable definition
#
#######################################################
#                Services definition
#######################################################
services:        
#
#
#   Variables are here for reference and example and are not used in interactive mode
#
- service:
    # MQTT connection to Kapua
    type: KuraService
    name: KapuaMQTT
    state: active
    override: false
 
    properties:
# These are the factory default parameters and this is to be modified
        topic.context.account-name: SOLIDSENSE-NURSERY
        username: newborn-gw
        password: ^$SolidSense2019$
        client-id: $SERIAL-NUMBER
        
#
#  ppp0 configuration
# 
- service:
    type: PppService
    name: ppp0
    state: disabled
    parameters:
        configuration: NetworkConfigurationService
        prefix: net.interface.$service_name
    variables:
        APN: orange
        APN_AUTH: CHAP # PAP/CHAP/Auto/None
        APN_USER: orange # If not None
        APN_PASSWORD: orange # if Not None
        DIAL_STRING: atd*99***1#
    properties:
        config.pppNum: 0
        config.apn: $APN
        config.authType: $APN_AUTH
        config.identifier: $MODEM_MODEL
        config.username: $APN_USER
        config.password: $APN_PASSWORD
        config.dialString: $DIAL_STRING
        config.ip4.status: netIPv4StatusEnabledWAN
        config.dhcpClient4.enabled: true
        config.enabled: true
        config.autoconnect: true
        usb.product.name: $MODEM_MODEL
        usb.vendor.name: $MODEM_MFG
        model: $MODEM_MODEL
        manufacturer: $MODEM_MFG
        
#
#  Eth0 as LAN when ppp0 is WAN
#
- service:
    # Ethernet port
    type: NetworkService
    name: eth0
    state: active
    override: false
    properties:
        config.ip4.status: netIPv4StatusEnabledWAN
```

To be edited:

- Cellular connection parameters: APN
- Kapua connection parameters

<a id="example-2-starting-the-solidsense-mqtt-service-automatically"></a>

### Example 2: Starting the SolidSense MQTT service automatically

<a id="applying-the-custom-configuration"></a>

#### Applying the custom configuration

Step 1: copy the YAML configuration on the gateway in the directory **/data/solidsense/config/SolidSense-conf-custom.yml**. Note that this is not affected by software upgrade or factory reset.

Step 2: restart the gateway with a factory reset. As a new configuration is applied, it shall be understood that any previous configuration will be lost. **All content of the /data partition is left untouched**.

Restart command. This command can be applied from a local shell (ssh) or from Kapua.

```
/opt/SolidSense/bin/restart --help
restart:
-h|--help :display this help
-c|--config :whether to erase kura user snapshots
-s|--sleep :default is <5>
-w|--wipe :whether to erase overlay

# to restart with a complete new configuration (as user solidsense)
sudo --login /opt/SolidSense/bin/restart --wipe

# to restart with only changes to the system done by Kura (as user solidsense)
sudo --login /opt/SolidSense/bin/restart --config
```

At that point the overlay file system is wiped out and the system reboots. Then the provision configuration is applied.