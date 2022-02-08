import network
from esp import espnow
from time import sleep
from machine import Pin
import ubinascii
import uasyncio

redPin = Pin(5, Pin.OUT)

async def blink():
    redPin.on()
    #await uasyncio.sleep_ms(1000)
    await uasyncio.sleep(0.5)
    #sleep(0.3)
    redPin.off()
    

async def createBlink():
    uasyncio.create_task(blink())

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)
mac = w0.config('mac')
print("MAC: ",mac, ubinascii.hexlify(mac, ':').decode())

e = espnow.ESPNow()
e.init()
# old 50:02:91:a1:a1:70
# new receiver 50:02:91:a1:9f:90
#peer = b'\x50\x02\x91\xa1\x9f\x90'   # MAC address of peer's wifi interface
peer = b'\xff\xff\xff\xff\xff\xff'   # MAC address of peer's wifi interface
try:
    e.add_peer(peer)
except OSError as err:
    if len(err.args) < 2:
        raise err
    if err.args[1] == 'ESP_ERR_ESPNOW_EXIST':
        print("Peer already exists")

print("Starting")
try:
    e.send("Starting...")       # Send to all peers
except OSError as err:
    if err.args[1] == 'ESP_ERR_ESPNOW_NOT_FOUND':
        print("Ok.... adding Peer")
        e.add_peer(peer)
for i in range(100):
    print("poll: ", e.poll(),", stats: ",e.stats())
    sendVal = str(i)*20
    e.send(sendVal)
    e.send(b'END')
    print("Sent: ", sendVal)
    uasyncio.run(createBlink())
    sleep(1)