import network
from esp import espnow
import ubinascii
import uasyncio

from machine import Pin
from time import sleep

bluePin = Pin(5, Pin.OUT)

async def blink():
    bluePin.on()
    #await uasyncio.sleep_ms(1000)
    #await uasyncio.sleep(0.5)
    sleep(0.3)
    bluePin.off()
    

async def createBlink():
    uasyncio.create_task(blink())
    
# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

e = espnow.ESPNow()
e.init()
# sender 50:02:91:a1:a1:70
# receive 50:02:91:a1:9f:90
peer = b'\x50\x02\x91\xa1\x9f\x90'   # MAC address of peer's wifi interface
try:
    e.add_peer(peer)
except OSError as err:
    if len(err.args) < 2:
        raise err
    if err.args[1] == 'ESP_ERR_ESPNOW_EXIST':
        print("Peer already exists")

while True:
    print("poll: ",e.poll(),", ",e.stats())
    host, msg = e.irecv(1000)     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        message = msg.decode("utf-8")
        if (message == "END"):
            uasyncio.run(createBlink())
        print(ubinascii.hexlify(host,':').decode(), message)
        #
    else:
        print("Nothing")