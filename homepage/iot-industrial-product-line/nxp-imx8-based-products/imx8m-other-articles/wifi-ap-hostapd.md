# WiFi AP - HostApd

Creating a WiFi hotspot on a device running Linux involves configuring the built-in wireless adapter to act as an access point. Below are general steps to achieve this using the hostapd software:

<a id="prerequisites"></a>

### Prerequisites:

1. Ensure that your device has a compatible wireless adapter. You may need an external USB WiFi dongle if the built-in WiFi doesn't support the necessary features.
2. Make sure your device is running a Linux distribution with package management. Debian is a popular choice.

**Step 1: Install hostapd and dnsmasq**

```
sudo apt-get update
sudo apt-get upgrade -y 
sudo apt-get install hostapd dnsmasq
```

**Stop Services:**

```
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

**Configure Static IP for the Access Point:**

**Edit /etc/dhcpcd.conf and add the following lines at the end:**

```
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
```

**Configure dnsmasq:**

**Create a new configuration file /etc/dnsmasq.conf and add:**

```
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```

**Configure Hostapd:**

**Create a new configuration file /etc/hostapd/hostapd.conf :**

```
cat <<EOF > /etc/hostapd/hostapd.conf

interface=wlan0
ssid=YourHotspotName
hw_mode=g
channel=7
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=YourPassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP

EOF
```

> [!NOTE]
> Here can find more information about the hostapd configuration
> [https://web.mit.edu/freebsd/head/contrib/wpa/hostapd/hostapd.conf](https://web.mit.edu/freebsd/head/contrib/wpa/hostapd/hostapd.conf)
> The `hw_mode` parameter can take one of the following values:
> - `a`: Specifies 5 GHz (802.11a)
> - `b`: Specifies 2.4 GHz (802.11b)
> - `g`: Specifies 2.4 GHz (802.11g)
> - `ad`: Specifies 60 GHz (802.11ad)
> - `n`: Specifies 2.4 GHz or 5 GHz (802.11n)
> - `ac`: Specifies 5 GHz (802.11ac)

**Update Hostapd Configuration:**

**Edit /etc/default/hostapd and update the line:**

```
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

**Start Services:**

```
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```

**Enable Services to Start on Boot:**

```
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
```

**Reboot:**

```
sudo reboot
```

After rebooting, your device should be broadcasting a WiFi hotspot with the specified SSID and password. You can connect to it using a device and should be able to access the internet through the device.

Adjust the configurations (SSID, password, IP range, etc.) according to your preferences.

Please note that these steps provide a basic setup, and additional configurations may be needed depending on your specific requirements and the Linux distribution you are using.