# Blink LED when a button is pressed - GPIO/LED/Button Example

To create a bash script for an i.MX8MP that makes an LED blink when a button is pressed, you'll need to use the GPIO (General Purpose Input/Output) pins on the i.MX8MP. Here's a simple example using a button connected to GPIO5\_IO08 and an LED connected to GPIO5\_IO09:

* GPIO5\_IO08 (GPIO number **136** in Linux)
* GPIO5\_IO09 (GPIO number **137** in Linux)

[Here](gpio-pins-control-hummingboard-pulse-mate-imx8m-plus-som.md) can find more information about how to control on the i.MX8MP GPIOs&#x20;

1. Connect a button to GPIO5\_IO08 and ground (GND), and connect an LED to GPIO5\_IO09 and a current-limiting resistor, then to ground (GND).\
   \- for simple test you can use the GPIOs of the [HummingBoard-Pulse/Ripple imx8mp](../hummingboard-imx8-sbc-quick-start-guide/hummingboard-pulse-imx8m-plus-som-quick-start-guide.md); [MikroBus](gpio-pins-control-hummingboard-pulse-mate-imx8m-plus-som.md) (J10\[1] and J10\[2])
2. Create a bash script using a text editor. For example, use the following command to create a script named `blink_button.sh`

```
#!/bin/bash
# Define GPIO pin numbers
BUTTON_PIN=136
LED_PIN=137
# Set up GPIO pins
echo "$BUTTON_PIN" > /sys/class/gpio/export
echo "$LED_PIN" > /sys/class/gpio/export
echo "in" > "/sys/class/gpio/gpio$BUTTON_PIN/direction"
echo "out" > "/sys/class/gpio/gpio$LED_PIN/direction"
# Function to turn on the LED
turn_on_led() {
   echo 1 > "/sys/class/gpio/gpio$LED_PIN/value"
}
# Function to turn off the LED
turn_off_led() {
   echo 0 > "/sys/class/gpio/gpio$LED_PIN/value"
}
# Main loop
while true; do
   # Check the state of the button
   button_state=$(cat "/sys/class/gpio/gpio$BUTTON_PIN/value")
   # If the button is pressed (value is 0), turn on the LED
   if [ "$button_state" -eq 0 ]; then
       turn_on_led
   else
       turn_off_led
   fi
   # Sleep for a short duration to avoid high CPU usage
   sleep 0.1
done
```

Your LED should blink when the button is pressed.

**Note** that this script continuously checks the state of the button in a loop. You can stop the script by pressing `Ctrl + C`.
