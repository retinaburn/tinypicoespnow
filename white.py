import neopixel
from machine import Pin
import time
import math

pin = 25
leds = 60
darkWidth = 10

np = neopixel.NeoPixel(Pin(pin), leds, 4)


white = 255
sleepS = 0.05
bottomSinLevel = 60

elemOff  = (0, 0, 0, 0)
elemOn = (64, 0, 0, white)

np.fill( elemOn )
np.write()