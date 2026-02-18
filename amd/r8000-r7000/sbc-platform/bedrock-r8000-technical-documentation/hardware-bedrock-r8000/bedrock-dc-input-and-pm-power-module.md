# Bedrock DC Input and PM (Power Module)

Bedrock can be ordered with an optional power module - an internal DC to DC converter with the following features

- Voltage regulation
- Reverse polarity protection
- Extended voltage range
- Overvoltage protection

For operating Bedrock using the standard PSU SRBD-PSU90, a PM is not required.

For operating Bedrock from a DC source, the PM (either PM1248 or PM1260) are highly recommended.

{% hint style="warning" %}
Without the PM, DC is fed directly into the Bedrock SoM which has no overvoltage protection and no reverse polarity protection. SoM may be damaged by voltage spikes.
If powering Bedrock with no PM, nominal voltage should not exceed 24V. Peak voltage should not exceed 28V.
{% endhint %}

