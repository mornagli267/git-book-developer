# Renesas RZ Features

<a id="internet"></a>

#### Internet

Connect an Ethernet cable to your HummingBoard Pulse (for internet access during boot-up).  
Models HummingBoard with WiFi, can be connected via [WiFi](../../nxp-imx8-based-products/cubox-m-quick-start-guide.md#wifi) or wired Ethernet.

- Please check you Ethernet connection.
- Use the following commands in order to keep your system up-to-date:

```
apt-get update 
apt-get upgrade 
reboot
```

- For more detailed information, please refer to [RZ/G2LC Debian](https://github.com/SolidRun/documentation/blob/bsp/imx8/debian-11_sr8.md) .

<a id="wifi"></a>

##### WiFi

- You can connect to WiFi using any application, such as : [connmanctl](https://manpages.debian.org/testing/connman/connmanctl.1.en.html) or [wpa\_spplicant](https://wiki.archlinux.org/title/wpa_supplicant).

An example for connecting to WiFi using wpa\_supplicant:

1. To bring a WiFi interface up, run the following :

```
$ ifconfig wlan0 up 
```

> [!NOTE]
> To discover your wireless network interface name, see [Network Interfaces](https://wiki.archlinux.org/title/Network_configuration#network_interfaces).

2. Install the wpa\_supplicant package:

```
$ apt-get install wpasupplicant 
```

3. Edit network interfaces file :

At the bottom of the file, add the following lines to allow wlan as a network connection:

```
cat <<EOF > /etc/network/interfaces.d/wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
EOF

```

4. Create a configuration file with the relevant ssid:

```
cat <<EOF > /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=/run/wpa_supplicant
update_config=1
network={
    ssid="MYSSID"
    psk="passphrase" 
}
EOF

```

> [!NOTE]
> Check your personal ssids by running : ‘iw dev wlan0 scan’

5. Make sure it works:

Restart your device and it should connect to the wireless network. You can check it by running the command `$ iwconfig` . If it doesn't, repeat above steps or get help from an adult.

- For more information about using wpa\_supplicant , you can refer to [wpa\_supplicant](https://www.linuxbabe.com/command-line/ubuntu-server-16-04-wifi-wpa-supplicant) or [wpa\_supplicant](https://blog.nelhage.com/2008/08/using-wpa_supplicant-on-debianubuntu/).

<a id="bluetooth"></a>

#### Bluetooth

1. For showing all Bluetooth devices, run the following:

```
$ apt-get install bluez
$ bluetoothctl
```

2. Turn the device on:

```
[bluetooth]# power on
```

3. Make your Bluetooth detectable by other devices:

```
[bluetooth]# discoverable on
```

4. If you want to connect to other devices:

- Start by scanning for other Bluetooth devices:

```
[bluetooth]# scan on
```

- Choose a MAC address and connect :

```
[bluetooth]# pair $MAC 
```

- You can check the pairing list between the devices by writing :

```
[bluetooth]# paired-devices
```

<a id="cellular-modem"></a>

#### Cellular Modem

The cellular modem is a more fully featured extension of which contains a cellular module with additional hardware interfaces and a SIM card slot.

You can connect your cellular modem to the mPCIe, and insert a SIM card.

- How to connect to the network:  
1\. Install “modemmanager” package on your debian.
```
 $ sudo apt install modemmanager
```
2\. Search for your modem location:
```
$ mmcli -L
```
3\. Connect to your modem:
```
$ mmcli --modem=/your/modem/location
```
4\. Enable the modem:
```
$ mmcli --modem=/your/modem/location -e
```
5\. Scan for networks:
```
$ mmcli --modem=/your/modem/location --3gpp-scan
```
6\. connect to 3gpp network:
```
$ mmcli --modem=/your/modem/location --3gpp-register-in-operator=<network ID>
```
7\. Make sure the connection was created:
```
$ mmcli --modem=/your/modem/location 
```
- For some cellular modules to be connected, please refer to [Cellular Modules](https://solidrun.atlassian.net/wiki/spaces/developer/pages/274661454) .

**GUI On Debian**

There is an option with the **Debian** image, up to the user, to work with a GUI like Weston, GNOME and etc.  
For applying this option do the following steps:

First, connect your device to a screen using the working output (HDMI / uHDMI).

For working with **Weston** GUI:

1. Install the Weston package.
```
sudo apt install weston
```
2. Set the XDG\_RUNTIME\_DIR env param.
```
cat << 'EOF' > /etc/profile.d/weston.sh
if test -z "$XDG_RUNTIME_DIR"; then
    export XDG_RUNTIME_DIR=/run/user/`id -u`
    if ! test -d "${XDG_RUNTIME_DIR}"; then
        # Make a directory for the output of the Weston GUI
        mkdir --parents "${XDG_RUNTIME_DIR}"
        chmod 0700 "${XDG_RUNTIME_DIR}"
    fi
fi
EOF
```
3. Restart the system
```
reboot
```
4. Start Weston (must be run from the **Dissplay Terminal**)
```
weston
```

> [!NOTE]
> Run the `weston` command from the **Dissplay Terminal** using keyboard (PHYSICAL TERMINAL not serial session or remote connection)

For working with **GNOME** GUI on top of Xorg:

1. Install Xorg.
```
$ sudo apt install xorg
```
2. Install your desired gnome.
```
$ sudo apt install gnome-session
```
NOTE: ‘gnome-session’ is an example of gnome that we can work with, you can replace the ‘session' with another GNOME extention.
3. Start your GNOME GUI.
```
$ sudo systemctl start gdm
```
  - For logging in you need a user on your device to log into it. You can create one before step 3 by this command (replace the ‘username’ with name that you want) :
```
$ sudo adduser username
```
  - You can jump between GUIs that you install (like gnome-session) by the setting button that locates in the down right corner of the home screen.