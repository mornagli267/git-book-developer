---
tags:
  - '#bedrock-r8000'
  - '#linux'
  - '#howto'
---

[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../../Software%20-%20Bedrock%20R8000.md) > [HowTo Guides - Bedrock R8000 | R7000](../HowTo%20Guides%20-%20Bedrock%20R8000%20_%20R7000.md)

# Enabling Watchdog in Ubuntu

##### Step 1 - Remove the watchdog module from modprobe blacklists:

```java
grep -r sp5100_tco /lib/modprobe.d/c
```

And comment out every "blacklist sp5100\_tco".

##### Step 2 - Create a new modprobe.d entry:

```java
echo "options sp5100_tco heartbeat=30 nowayout=1" > /etc/modprobe.d/sp5100_tco.conf
```

##### Step 3 - Install the watchdog package

```java
apt install -y watchdog
```

##### Step 4 - Update the watchdog config

Open the /etc/watchdog.conf file.

Uncomment the following line:

#watchdog-device         = /dev/watchdog

Uncomment and replace the following line:

#watchdog-timeout = 60

With:

watchdog-timeout = 30

##### Step 5 - reboot the system

```java
reboot
```

That’s it, it can be tested by triggering a kernel crash with the following command:

```java
echo c > /proc/sysrq-trigger
```

The kernel will crash, and the system will reboot after up to 30 seconds.
