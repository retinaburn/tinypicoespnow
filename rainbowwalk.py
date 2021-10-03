from collections import deque
import machine, neopixel
from machine import Pin
import time

from uasyncio import sleep_ms

pin = 25
number = 60

np = neopixel.NeoPixel(Pin(pin), number, 4)

on = 32
white = 0
a = [ (on, 0, 0, white), (0, on, 0, white), (0, 0, on, white)]

d = deque((), 3, True)
for iter in range(len(a)):
    d.append(a[iter])


np.fill( (0,0,0,0) )
np.write()

for iter in range(1000):
    for i in range(number):        
        np[i] = d.popleft()
        #print("np[",i,"] = [",np[i],"]")
        d.append(np[i])        
    np.write()
    d.append(d.popleft()) #rotate one element to offset
    time.sleep(0.25)
