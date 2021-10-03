import machine, neopixel
from machine import Pin
import time

from uasyncio import sleep_ms

pin = 25
number = 60

np = neopixel.NeoPixel(Pin(pin), number, 4)
np.fill( (0, 0, 0, 0) )
np.write()

