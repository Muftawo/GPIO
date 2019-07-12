from gpiozero import LED, Button
from signal import pause

led_red = LED(17)
led= LED(16)
button = Button(2)

button.when_pressed = led_red.on
button.when_released = led.on

pause()