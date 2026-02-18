# Bedrock Disabling EEE on Intel I226 NICs

By default EEE should be disabled, if not you can disable it using ethtool using the following commands:

To check the status of the intel nic:

```
ethtool --show-eee <INTERFACE_NAME>
```

To disable EEE on a NIC:

```
ethtool --set-eee <INTERFACE_NAME> eee off
```

{% hint style="info" %}
When using ethtool, every reboot will reset the setting so you will need to do it each time you reboot the system.
{% endhint %}


EEE could also be disabled in the NICs settings using Intels Lanfonf tool if you have access to it.