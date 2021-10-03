import machine, neopixel
from machine import Pin
import time

from uasyncio import sleep_ms

pin = 25
number = 60
brightness = 0.1

np = neopixel.NeoPixel(Pin(pin), number, 4)

def wheel(pos):
    #print("S: ",valStraight,", I: ",valInvert)
    
    if pos < 0 or pos > 255:
        return (0, 0, 0, 0)
    if pos < 85:
        red = round(255 - pos * 3)
        green = round(pos * 3)        
        blue = 0        
    elif pos < 170:
        pos -= 85
        red = 0
        green = round(255 - pos * 3)
        blue = round(pos * 3)        
    else:
        pos -= 170
        red = round(pos * 3)
        green = 0
        blue = round(255 - pos * 3)
    return (int(red * brightness), int(green * brightness), int(blue * brightness), 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(number):
            rc_index = (i * 256 // number) + j
            np[i] = wheel(rc_index & 255)
        np.write()
        time.sleep_ms(wait)

for i in range(100):
    rainbow_cycle(1)

