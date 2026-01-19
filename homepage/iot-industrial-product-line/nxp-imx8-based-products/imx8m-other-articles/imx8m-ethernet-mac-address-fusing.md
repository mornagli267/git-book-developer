# i.MX8M Ethernet MAC Address Fusing

<a id="mac-fusing"></a>

#### MAC Fusing

Use these U-Boot commands to store the example MAC address `02:03:04:05:06:07` on i.MX8M SOM:

```
fuse prog -y 9 0 04050607
fuse prog -y 9 1 0203
```

{% hint style="warning" %}
**Please Note**
Fuse programming is irreversible.
{% endhint %}

