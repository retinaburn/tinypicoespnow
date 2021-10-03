from collections import deque
import machine, neopixel
from machine import Pin
import time
import math

from uasyncio import sleep_ms

pin = 25
number = 60

np = neopixel.NeoPixel(Pin(pin), number, 4)

on = 16         #the maximum brightness 
white = 0
sleepS = 0.0

numElem = 8
B = 1

a = []

def getSinVal(phaseShift):
    sinVal = abs(math.sin( B * math.radians(degrees) + phaseShift))
    roundedSinVal = round (sinVal * on)
    print ("sin(",degrees,") = ",sinVal," -> ", roundedSinVal)
    return roundedSinVal

for i in range(numElem):
    degrees = 180 / numElem * i
    redVal = getSinVal(0)
    blueVal = 0
    greenVal = 0
    a.append( (redVal, blueVal, greenVal, white) )
print("a = ",a)
# a = [
#     (0, 0, 0, 0) , #0 / 180
#     (int(0.3746 * on), 0, 0, 0) , # 22
#     (int(0.7071 * on), 0, 0, 0) , # 45
#     (int(0.9272 * on), 0, 0, 0) , # 67
#     (int(1.0 * on), 0, 0, 0) , # 90
#     (int(0.9272 * on), 0, 0, 0) , # 113
#     (int(0.7071 * on), 0, 0, 0) , # 135
#     (int(0.3746 * on), 0, 0, 0) , # 157
# ]

d = deque((), len(a), True)
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
    d.append(d.popleft()) #rotate one element to offset
    d.append(d.popleft()) #rotate one element to offset
    time.sleep(sleepS)
