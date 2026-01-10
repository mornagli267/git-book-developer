
[Bedrock PC](../../../Bedrock%20PC.md) > [Bedrock V3000 Technical Documentation](../../Bedrock%20V3000%20Technical%20Documentation.md) > [Software - Bedrock V3000](../Software%20-%20Bedrock%20V3000.md)

# Disabling EEE on Intel I226 NICs V3000

By default EEE should be disabled, if not you can disable it using ethtool using the following commands:

To check the status of the intel nic:

```java
ethtool --show-eee <INTERFACE_NAME>
```

To disable EEE on a NIC:

```java
ethtool --set-eee <INTERFACE_NAME> eee off
```

> [!IMPORTANT]
> When using ethtool, every reboot will reset the setting so you will need to do it each time you reboot the system.

EEE could also be disabled in the NICs settings using Intels Lanfonf tool if you have access to it.
