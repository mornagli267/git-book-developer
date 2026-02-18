# Enabling Watchdog in Ubuntu

**Step 1 - Remove the watchdog module from modprobe blacklists:**

```
grep -r sp5100_tco /lib/modprobe.d/c
```

And comment out every "blacklist sp5100\_tco".

**Step 2 - Create a new modprobe.d entry:**

```
echo "options sp5100_tco heartbeat=30 nowayout=1" > /etc/modprobe.d/sp5100_tco.conf
```

**Step 3 - Install the watchdog package**

```
apt install -y watchdog
```

**Step 4 - Update the watchdog config**

Open the /etc/watchdog.conf file.

Uncomment the following line:

\#watchdog-device         = /dev/watchdog

Uncomment and replace the following line:

\#watchdog-timeout = 60

With:

watchdog-timeout = 30

**Step 5 - reboot the system**

```
reboot
```

That’s it, it can be tested by triggering a kernel crash with the following command:

```
echo c > /proc/sysrq-trigger
```

The kernel will crash, and the system will reboot after up to 30 seconds.
