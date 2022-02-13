import network
from esp import espnow
from time import sleep
from machine import Pin
import ubinascii
import uasyncio
import _thread

sendPin = Pin(5, Pin.OUT)
receivedPin = Pin(22, Pin.OUT)
button = Pin(23, Pin.IN, Pin.PULL_UP)

BACKGROUND_THREAD = True

def sendThread():
    while BACKGROUND_THREAD:
        if not button.value():
            e.send(peer, b'END')
            print("Sent: ", "END")
            sendPin.on()
            sleep(1)
            sendPin.off()



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
peer = b'\xff\xff\xff\xff\xff\xff'   # broadcast mac address
try:
    e.add_peer(peer)
except OSError as err:
    if len(err.args) < 2:
        raise err
    if err.args[1] == 'ESP_ERR_ESPNOW_EXIST':
        print("Peer already exists")

_thread.start_new_thread(sendThread, ())

while True:
    print("poll: ", e.poll(),", stats: ",e.stats())
    while e.poll():
        host, msg = e.irecv(0)     # Available on ESP32 and ESP8266
        if msg:             # msg == None if timeout in irecv()
            message = msg.decode("utf-8")
            print(ubinascii.hexlify(host,':').decode(), message)
            if (message == "END"):
                receivedPin.on()
                sleep(10)
                receivedPin.off()
    sleep(1)
