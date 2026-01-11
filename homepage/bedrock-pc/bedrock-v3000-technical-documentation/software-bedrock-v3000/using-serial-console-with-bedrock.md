# Using serial console with Bedrock

## Setting terminal on host

### **Putty Linux:**

* Download putty to your linux or windows pc
* Open putty gui
* Choose **Serial** from the 3 bullet choices
* In the **serial line** type /dev/ttyUSBX
* Where X is the number assigned to your serial adapter, you can view it by running

```
sudo dmesg | grep ttyUSB*
```

* **Speed** should be 115200
* You can click on save to save the current configuration for faster connection in the future
* Click on **open**
* A terminal will appear

### **Putty Windows:**

* Download putty to your linux or windows pc
* Open putty gui
* Choose **Serial** from the 3 bullet choices
* In the **serial line** type COMX
* Where X is the number assigned to your serial adapter in the device manager
  * Open device manager, and look for serial adapters, look for the COMX that corresponds to your serial connection:![image-20240617-110508.png](../../../../.gitbook/assets/image-20240617-110508.png)
* **Speed** should be 115200
* You can click on save to save the current configuration for faster connection in the future
* Click on **open**
* A terminal will appear

### **Tio (Linux):**

* Install the tio package on your linux pc
* Run the command

```
tio /dev/ttyUSBX
```

* Where X is the number assigned to your serial adapter, you can view it by running

```
sudo dmesg | grep ttyUSB*
```

NOTE: when using TIO in BIOS, the currently selected setting could be invisible due to TIO displaying the selected text and background in the same color.

## Connecting Bedrock to host PC

* Use a mini-USB to USB-A cable to connect Bedrock console port to an available USB port on your host PC.

![](../../../../.gitbook/assets/image-20230604-084319.png)

* Start Terminal utility on your host

## Entering BIOS settings on Bedrock

* Turn on Bedrock
* Repetitively press the DEL / ESC key in Terminal on your host to enter the BIOS setup on Bedrock

BIOS settings screen should appear in the terminal window on your host.
