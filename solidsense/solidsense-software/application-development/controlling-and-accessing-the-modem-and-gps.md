# Controlling and accessing the modem and GPS

{% hint style="warning" %}
The documentation for SolidSense software is not maintained by SolidRun and the information herein is not actual with the latest version of the software, please contact our partner [SolidSense Connect](https://solidsense-connect.com/) who is now developing the SolidSense software.
{% endhint %}


## Purpose

The SolidSense platform includes a cellular modem with GNSS function in most of its configuration. In order to easily control the modem and access the GNSS data, a specific service with gRPC access is provided.

Here are the main features:

1. Initializing the modem with programming of the PIN code on startup
2. Constant monitoring of the modem in system logs
3. Capability to access the modem status remotely at any time via gRPC
4. Capability to access GNSS position and quality data remotely via gRPC
5. Configuring and resetting the modem
6. Sending and receiving SMS

## Installation and introduction

The modem and GPS management service and SW is directly installed in SolidSense V1.0 images (from 0.9 on), no action needed here.

A systemd service ‘modem\_gps’ is automatically enabled and started by the provisioning system if the gateway is equipped with a combined modem/GNSS receiver module. This service is performing the following tasks:

1. Initialization of the modem at startup
2. Constant supervision
3. gRPC server for modem status information and GPS information

## Controlling the modem and GPS status interactively

A convenience script is installed for accesing the modem status and control: ‘modem\_status’.

That script is looking for the local instance of the gRPC server on default port. If the server is not active (start\_gps\_service is false) the command is ineffective except some direct access commands.

```
modem_status --help
    -h|--help                     :display this help
    -l|--list                     :list available networks
    -t|--test arg1 arg2           :test the modem and attachment (as sudo). arg1 and arg2 are optional
    -n|--network                  :select an network
    -r|--rat                      :select a RAT (GSM/UTRAN/LTE)
    -R|--reset                    :reset the modem (as sudo)
    -F|--factory_reset            :reset the modem to factory default(as sudo)
    -c|--check                    :check modem presence (as sudo)
    no arguments                  :print the modem status
```

All commands mentioned ‘as sudo’ are directly accessing the modem and not the modem\_gps service, by consequence the service is stopped and needs to be restarted afterwards.

Additional arguments for modem\_status -t

|      |            |                                                                                               |
| ---- | ---------- | --------------------------------------------------------------------------------------------- |
| arg1 | arg2       | signification                                                                                 |
| cmd  | AT command | send the corresponding AT command to the modem. The command must not include the leading ‘AT’ |
| scan |            | Restart networks scan                                                                         |
| init |            | Perform a flight mode /non flight mode cycle                                                  |
| sms  |            | check SMS parameters                                                                          |
| gps  |            | check the GPS                                                                                 |

Example of status print

```
modem_status
====GPS Server : 127.0.0.1:20231
modem command: status
model: EC25 Revision: EC25EFAR06A03M4G IMEI: 866758042319323 GPS ON: True  SIM: READY
IMSI: 208019601320228
On: HOME  PLMNID: 20801  Network: 20801  Radio: FDD LTE  Band: LTE BAND 3  LAC: 14497 CI: 14308869 RSSI: -51 dBm
GPS FIXED date: 27/03/20 time: 14:59:05.000000
LAT: 48.104156494140625 LONG: -1.6879802942276 SOG: 0.0 COG: 331.79998779296875
```

## Configuration

The configuration file (parameters.json) resides /data/solidsense/modem\_gps directory. A default version is generated based on provisioning service directive and can be edited to tailor the micro-service to your needs.

```
{
 "operatorsDB": "operatorsDB",
 "trace": "debug",
 "start_gps": false,
 "start_gps_service": true,
 "modem_ctrl": "/dev/ttyUSB2",
 "address": "0.0.0.0",
 "nmea_tty": "/dev/ttyUSB1",
 "PIN": "0000",
 "port": 20231,
 "roaming": true,
 "timer" : 60,
 "nb_retry" : 3,
 "log_at": false
}
```

Explanation and values for each parameters by order of importance:

**start\_gps\_service**: if false, only the modem configuration and in particular PIN code entry is done. After that phase the service stops. In that case it run only once at gateway startup. If true, the gRPC server is started after the modem configuration phase.

**start\_gps**: if true the GNSS feature is enabled, if false nothing is done, but in case the GNSS was started before, it remains running (GNSS state is permanently stored on the modem).

**address**: IP address used for listening. This parameter can be used to restrict the scope of listening. 0.0.0.0 means listening on all external interfaces while localhost is listening only for internal connections.

**port**: TCP port used by the service. In case the service can be reached from outside, then that port is to be open on the firewall.

**PIN**: PIN code to be entered to enable the SIM card. If no PIN code is requested by the SIM card, that parameter is not used.

**trace**: level of traces. Possible values: debug, info, error. We recommend to use “info”.

**roaming**: To allow roaming attachment of the modem.

**timer**: Interval in seconds for the logging of the modem and GPS status

**nb\_retry**: This parameter is used to perform a soft reset of the modem if it does not find a network after timer interval

**log\_at**: If true all AT commends and responses with the modem are logged into the file /data/solidsense/atcmd.log. To be used only for debugging purpose.

{% hint style="warning" %}
**Please note** Changing the SIM requires to reset the modem or even restart the gateway to be taken into account.
{% endhint %}


## Using the modem GPS micro-service in application

To use the micro-service writing a gRPC client to access it is mandatory. Use [protobuf](https://developers.google.com/protocol-buffers/) and [gRPC](https://www.grpc.io/)  to generate your client stubs and serialization routines. This is existing for most of the programming language. The interface definition file is available in the installation directory (GPS\_Service.proto).

2 example files in Python3 are provided:

GPS\_Service\_client.py: accessing the GPS (GNSS) data

Modem\_Service\_client.py: send commands to the modem

SMS\_Client.py: send or receive SMS

Accessing the GPS and modem via MQTT

From the SolidSense version (1.1) on the GPS and Modem can be remotely monitored via MQTT using the SolidSense MQTT client integrated with the SolidSense platform.

## Troubleshooting

If the ppp connection does not come up, first check the status with ‘modem\_status’ to verify that the SIM is well recognized and a network is attached. If everything is OK here, then the APN parameters have to be verified.

#### Getting the modem logs

Logs are retrieved via journalctl. The simplest is: sudo journalctl -u modem\_gps -f (-b)

#### Modem is not attaching to any network

When this situation happens, the only solution is to perform a modem\_reset.

First try:sudo modem\_status -R

If it does not solve the problem: sudo modem\_status -F

After performing any reset, make a quick check: sudo modem\_status -c
