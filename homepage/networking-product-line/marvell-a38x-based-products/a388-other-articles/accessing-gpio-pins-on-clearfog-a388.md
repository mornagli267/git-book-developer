# Accessing GPIO Pins on ClearFog A388

**To control on the GPIO pins:**

- The external GPIOs are available under the /sys/class/gpio folder in Linux.
- To control on the GPIO pins you need to calculate the GPIO number XX and run the commands below:

```
# Export GPIO XX
echo XX > /sys/class/gpio/export

# Set GPIO pin Direction
echo "out" > /sys/class/gpio/gpioXX/direction
or
echo "in" > /sys/class/gpio/gpioXX/direction

# Set the value of an output pin
echo 1 > /sys/class/gpio/gpioXX/value
or
echo 0 > /sys/class/gpio/gpioXX/value

# Get the value of an input pin
cat > /sys/class/gpio/gpioXX/value

# Unexport GPIO XX
echo XX > /sys/class/gpio/unexport
```

This is an example code for accessing the GPIOs on the ClearFog Base/Pro:

```
#An example for gpio 22

# Export GPIO XX
cd /sys/class/gpio/ 
echo 22 > export 

cd gpio22/ 

# Set GPIO pin Direction
echo out > direction 

# Set the value of an output pin
echo 0 > value
```