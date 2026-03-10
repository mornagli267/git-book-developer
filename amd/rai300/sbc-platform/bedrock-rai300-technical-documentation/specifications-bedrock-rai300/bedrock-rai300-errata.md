# Bedrock RAI300 Errata

## Device fails to Boot after it is powered off and power button is pressed

### Symptom

After powering off the device and powering it on using the power button / remote power button, the device fails to boot.
In console you will see:

```
ABL BP[80000000]
```

### Solution

Disconnect power and connect it back to the unit.

### Root cause

Unknown

## Device fails to boot Memtest86

### Symptom

The device will not boot Memtest86 with an error saying: "failed to calibrate CPU frequencies".

### Solution

None

### Root cause

HPET is disabled in order to allow Linux to boot. (temporary)
