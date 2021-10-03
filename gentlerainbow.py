import machine, neopixel
from machine import Pin
import time

from uasyncio import sleep_ms

pin = 25
number = 60

np = neopixel.NeoPixel(Pin(pin), number, 4)

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3, 0)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(number):
            rc_index = (i * 256 // number) + j
            np[i] = wheel(rc_index & 255)
        np.write()
        #time.sleep_ms(wait)

for i in range(100):
    rainbow_cycle(1)

