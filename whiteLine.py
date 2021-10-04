from collections import deque
import machine, neopixel
from machine import Pin
import time
import math
from uasyncio import sleep_ms


pin = 25
leds = 60

np = neopixel.NeoPixel(Pin(pin), leds, 4)

white = 255
sleepS = 0.05

np.fill( (0,0,0,white) )
np.write()

while True:
    for i in range(leds):
        np[i] = (0,0,0,0)
        np.write()
        time.sleep(sleepS)

    for i in range(leds):
        np[i] = (0,0,0,white)
        np.write()
        time.sleep(sleepS)
