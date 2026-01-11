# Bedrock R8000 | R7000 Front panel LEDs documentation

This Page Includes the Front panel LEDs naming and behavior documentation:

1. **POWER LED:**![image-20251019-052500.png](./attachments/image-20251019-052500.png)
This LED indicates that the Device is powered on.  
When device is powered on the White LED is turned on during the early stages of BIOS initialization.  
**NOTE:** This LED is controlled By a GPIO pin, and therefore it will have some delay from the moment the power plug is inserted.
2. **S (Status) LED:**![image-20251019-050842.png](./attachments/image-20251019-050842.png)
This LED shows the POST status of the device. When device is in PRE-POST status LED will have yellow color (up to 40 seconds)  
After POST, color changes to green indicating the device successfully posted (Exiting BIOS menu or booting an OS).  
**NOTE:** During the DDR training stage the LED with have the yellow color, for more verbose info during the process connect a serial console: [Using serial console with Bedrock](../../../bedrock-pc/bedrock-v3000-technical-documentation/software-bedrock-v3000/using-serial-console-with-bedrock.md)
3. **Storage LED:**![image-20251019-050710.png](./attachments/image-20251019-050710.png)
This LED indicates activity on the main NVME device (NVME0).
4. **WI-FI / Bluetooth LED:**![image-20251019-051313.png](./attachments/image-20251019-051313.png)
This LED Indicates WIFI / Bluetooth is ON (works only on Windows due to driver compatibility).
5. **LTE LED:**![image-20251019-052129.png](./attachments/image-20251019-052129.png)
This LED Indicates LTE is ON (works only on Windows due to driver compatibility).