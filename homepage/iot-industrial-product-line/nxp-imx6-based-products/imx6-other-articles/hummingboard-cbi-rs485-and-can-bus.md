# HummingBoard CBi RS485 and CAN bus

## Test CAN bus communication

**1. Enable device can0 (for ex):**

```
ip link set can0 up type can bitrate xxxxxx
```

* (ex: 125000)

**2. Bring the CAN interface up:**

```
ifconfig can0 up
```

> \[!NOTE] To discover your CAN bus interface name, please run ‘ ip link show ’.

**3. To start testing the CanBUS, you have to install the can-utils package by running:**

```
sudo apt-get install -y can-utils 
```

* For more information, please follow the  [CAN-Utils](https://github.com/linux-can/can-utils), which are available for Debain/Ubuntu etc.

**4. Print all data received by CAN interface to “can\_test” file (for ex):**

```
candump can0 >> /tmp/can_test &
```

**5. Send data to the bus by executing (for ex):**

```
cansend can0 "123#1234"
```

**6. Check received data by opening “can\_test” file:**

```
cat /tmp/can_test
```

## Test RS-485 communication

An example for testing RS485 communication:

**1. Open a test file “rs485\_test”**

```
rs485conf -e 1 /dev/ttymxc1
touch /tmp/rs485_test
stty -F /dev/ttymxc1 raw -echo -echoe -echok
```

**2. Print received data to “rs485\_test” file:**

```
cat /dev/ttymxc1 > /tmp/rs485_test &
echo "rs485" > /dev/ttymxc1
```

* For more information, please refer to [HummingBoard CBi RS485 and CANBus pin mapping](https://solidrun.atlassian.net/wiki/spaces/developer/pages/287178867) .
