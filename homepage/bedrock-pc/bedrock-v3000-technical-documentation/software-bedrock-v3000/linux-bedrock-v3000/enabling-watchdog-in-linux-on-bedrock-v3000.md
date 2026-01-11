# Enabling Watchdog in Linux on Bedrock V3000

This guide outlines the steps to configure and test the `sp5100_tco` watchdog on your system.

<a id="step-1-remove-the-watchdog-module-from-modprobe-blacklists"></a>

## Step 1: Remove the Watchdog Module from Modprobe Blacklists

1. Search for the `sp5100_tco` entry in the modprobe configuration:
```
grep -r sp5100_tco /lib/modprobe.d/
```
2. For each returned result, open the file and comment out lines containing "blacklist sp5100\_tco".

<a id="step-2-create-a-new-modprobe-entry"></a>

## Step 2: Create a New Modprobe Entry

Enter the following command to add a new configuration for `sp5100_tco`:

```
echo "options sp5100_tco heartbeat=30 nowayout=1" > /etc/modprobe.d/sp5100_tco.conf
```

<a id="step-3-install-the-watchdog-package"></a>

## Step 3: Install the Watchdog Package

Use the package manager to install the watchdog package:

```
apt install -y watchdog
```

<a id="step-4-update-the-watchdog-configuration"></a>

## Step 4: Update the Watchdog Configuration

1. Open the watchdog configuration file:
```
nano /etc/watchdog.conf
```
2. Locate and uncomment the line:
```
#watchdog-device = /dev/watchdog
```
3. Find the line:
```
#watchdog-timeout = 60
```
Uncomment it and change its value to `30`:
```
watchdog-timeout = 30
```

<a id="step-5-reboot-the-system"></a>

## Step 5: Reboot the System

To apply the changes, reboot your system:

```
reboot
```

<a id="testing-the-configuration"></a>

## Testing the Configuration

To test if the watchdog is working correctly, you can intentionally trigger a kernel crash:

After executing the above command, the kernel will crash. If the watchdog is correctly configured, the system should reboot automatically within 30 seconds.

> [!WARNING]
> **Warning**: The test command will cause system instability and an immediate reboot. Ensure you've saved all your work before executing the test command.