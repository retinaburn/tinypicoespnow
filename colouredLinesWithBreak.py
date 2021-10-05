import neopixel
from machine import Pin
import time
#from ulab import numpy as nd
from collections import deque

pin = 25
leds = 60
darkWidth = 10


def drawLine():
    d = deque((),darkWidth, True)
    np.fill( elemOn )
    np.write()

    iter = 0
    for i in range(darkWidth):
        d.append(iter)
        iter -= 1


    for iter in range(leds):
        np.fill(elemOn)
        for i in range(darkWidth):
            
            try:
                x = d.popleft()
            except IndexError:
                x = leds
            if x < leds and x >= 0:
                np[x] = elemOff
            if x < leds:
                d.append(x+1)                
        np.write()
        time.sleep(sleepS)
    return

np = neopixel.NeoPixel(Pin(pin), leds, 4)


sleepS = 0.10
elemOff  = (0, 0, 0, 0)

while True:
    elemOn = (0, 0, 255, 0)
    drawLine()
    elemOn = (0, 255, 0, 0)
    drawLine()
    elemOn = (255, 0, 0, 0)
    drawLine()
    elemOn = (0, 0, 0, 255)
    drawLine()

