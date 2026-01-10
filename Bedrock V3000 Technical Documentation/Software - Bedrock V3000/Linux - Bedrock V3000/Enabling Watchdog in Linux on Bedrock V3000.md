
[Bedrock PC](../../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../../Software%20-%20Bedrock%20V3000.md) > [Linux - Bedrock V3000](../Linux%20-%20Bedrock%20V3000.md)

# Enabling Watchdog in Linux on Bedrock V3000

This guide outlines the steps to configure and test the `sp5100_tco` watchdog on your system.

## Step 1: Remove the Watchdog Module from Modprobe Blacklists

1. Search for the `sp5100_tco` entry in the modprobe configuration:

   ```java
   grep -r sp5100_tco /lib/modprobe.d/
   ```
2. For each returned result, open the file and comment out lines containing "blacklist sp5100\_tco".

## Step 2: Create a New Modprobe Entry

Enter the following command to add a new configuration for `sp5100_tco`:

```java
echo "options sp5100_tco heartbeat=30 nowayout=1" > /etc/modprobe.d/sp5100_tco.conf
```

## Step 3: Install the Watchdog Package

Use the package manager to install the watchdog package:

```java
apt install -y watchdog
```

## Step 4: Update the Watchdog Configuration

1. Open the watchdog configuration file:

   ```java
   nano /etc/watchdog.conf
   ```
2. Locate and uncomment the line:

   ```java
   #watchdog-device = /dev/watchdog
   ```
3. Find the line:

   ```java
   #watchdog-timeout = 60
   ```

   Uncomment it and change its value to `30`:

   ```java
   watchdog-timeout = 30
   ```

## Step 5: Reboot the System

To apply the changes, reboot your system:

```java
reboot
```

## Testing the Configuration

To test if the watchdog is working correctly, you can intentionally trigger a kernel crash:

After executing the above command, the kernel will crash. If the watchdog is correctly configured, the system should reboot automatically within 30 seconds.

> [!WARNING]
> **Warning**: The test command will cause system instability and an immediate reboot. Ensure you've saved all your work before executing the test command.
