
[Bedrock PC](../../../Bedrock%20PC.md) > [Bedrock R8000 Technical Documentation](../../Bedrock%20R8000%20Technical%20Documentation.md) > [Software - Bedrock R8000](../Software%20-%20Bedrock%20R8000.md)

# Bedrock R8000 | R7000 Front panel LEDs documentation

This Page Includes the Front panel LEDs naming and behavior documentation:

1. **POWER LED:**

   ![image-20251019-052500.png](../../../../attachments/7877374d-6ea0-4a48-8633-90f30ebd790c.png)

   This LED indicates that the Device is powered on.  
   When device is powered on the White LED is turned on during the early stages of BIOS initialization.  
   **NOTE:** This LED is controlled By a GPIO pin, and therefore it will have some delay from the moment the power plug is inserted.
2. **S (Status) LED:**

   ![image-20251019-050842.png](../../../../attachments/14310290-53fd-41d3-b00e-7a12cd539910.png)

   This LED shows the POST status of the device. When device is in PRE-POST status LED will have yellow color (up to 40 seconds)  
   After POST, color changes to green indicating the device successfully posted (Exiting BIOS menu or booting an OS).  
   **NOTE:** During the DDR training stage the LED with have the yellow color, for more verbose info during the process connect a serial console: [Using serial console with Bedrock](../../Bedrock%20V3000%20Technical%20Documentation/Software%20-%20Bedrock%20V3000/Using%20serial%20console%20with%20Bedrock.md)
3. **Storage LED:**

   ![image-20251019-050710.png](../../../../attachments/5100ee6a-5b69-4791-9e67-49a0ec638243.png)

   This LED indicates activity on the main NVME device (NVME0).
4. **WI-FI / Bluetooth LED:**

   ![image-20251019-051313.png](../../../../attachments/0112fff8-f3e8-42b1-a9be-ab0a6c86107e.png)

   This LED Indicates WIFI / Bluetooth is ON (works only on Windows due to driver compatibility).
5. **LTE LED:**

   ![image-20251019-052129.png](../../../../attachments/f9078537-1ea8-4b40-a324-799df45faef3.png)

   This LED Indicates LTE is ON (works only on Windows due to driver compatibility).
