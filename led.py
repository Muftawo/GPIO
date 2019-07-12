from gpiozero import LED
from time import sleep

led_red = LED(17)
led_green = LED(27)
led_yellow = LED(21)

while True:
    led_red.on()
    sleep(1)
    led_red.off()
    sleep(1)
    
    led_yellow.on()
    sleep(1)
    led_yellow.off()
    sleep(1)
    
    led_green.on()
    sleep(1)
    led_green.off()
    sleep(1)