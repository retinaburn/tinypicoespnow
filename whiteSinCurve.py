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
elemOn = (32, 0, 0, white)

def getSinVal(amplitude, phaseShift, degrees):
    sinVal = abs(math.sin(math.radians(degrees) + phaseShift))
    roundedSinVal = round (sinVal * amplitude)
    #print ("sin(",degrees,") = ",sinVal," -> ", roundedSinVal)
    return roundedSinVal

while True:
    for i in range(180):
        redSin = getSinVal(32, 0, i)
        whiteSin = getSinVal(255, 0, i)
        whiteSin = whiteSin if whiteSin > bottomSinLevel else bottomSinLevel
        np.fill( (redSin, 0, 0, whiteSin) )
        np.write()
        time.sleep(0.05)
