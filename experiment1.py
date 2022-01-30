import neopixel
from machine import Pin, SoftSPI, TouchPad
import time
#from ulab import numpy as nd
from collections import deque
import math
import tinypico

pin = 25
leds = 60

spi = SoftSPI(sck=Pin( tinypico.DOTSTAR_CLK ), mosi=Pin( tinypico.DOTSTAR_DATA ), miso=Pin( tinypico.SPI_MISO) )
dotstar = tinypico.DotStar(spi, 1, brightness = 0.5 ) # Just one DotStar, half brightness
tinypico.set_dotstar_power(True)

np = neopixel.NeoPixel(Pin(pin), leds, 4)
d = deque((), leds, True)

def getSinVal(amplitude, phaseShift, degrees, period):
    sinVal = abs(math.sin(math.radians(period * degrees) + phaseShift))
    roundedSinVal = round (sinVal * amplitude)
    #print ("sin(",degrees,") = ",sinVal," -> ", roundedSinVal)
    return roundedSinVal

period = 1.0
for i in range(leds):
    d.append( (getSinVal(32,0,i * 3, period), 0, 0, getSinVal(255,0,i * 3, period) ) )

t = TouchPad(Pin(27))

mode = 0
while True:
    if (mode == 0):
        while t.read() > 800:
            for i in range(leds):
                np[i] = d.popleft()
                d.append(np[i])        
            np.write()
            dotstar[0] = (64, 32, 32, np[0][3]/255)
            d.append(d.popleft())
        mode = 1
    else:
        while t.read() > 800:
            np.fill( (32, 0, 0, 128) )
            np.write()
        mode = 0