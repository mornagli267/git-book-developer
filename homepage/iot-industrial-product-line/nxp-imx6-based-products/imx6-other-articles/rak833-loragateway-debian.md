# RAK833 – LoRaGateway – Debian

<a id="rak833-loragateway-solidrun-debian"></a>

# RAK833-LoRaGateway-SolidRun-Debian

Verified on HummingBoard Gate/Edge rev 1.4 and SOM rev 1.5

<a id="installation-procedure"></a>

## Installation procedure

step1 : Download and install [sr-imx6-debian-stretch-cli-20180916.img.xz](https://images.solid-build.xyz/IMX6/Debian/)

step2 : flashing image to SD card([Flashing an SD Card](../../../../homepage/other-articles/flashing-an-sd-card.md))

step3 : Clone the installer and start the installation

```
  $ git clone https://github.com/RAKWireless/RAK833-LoRaGateway-SolidRun-Debian.git ~/rak833-solidrun
  $ cd ~/rak833-solidrun
  $ sudo ./install.sh
```

step4 : make sure the mini-pcie PERST# signal(pin 22) pulled down (default high will cause rak833 function error)

step5 : Start the packet-forwarder application

```
  $ cd /opt/packet_forwarder/lora_pkt_fwd
  $ sudo ./lora_pkt_fwd
```

Now you have a running gateway.