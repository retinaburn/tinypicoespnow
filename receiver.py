import network
from esp import espnow

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)

e = espnow.ESPNow()
e.init()
# sender 50:02:91:a1:a1:70
# receive 50:02:91:a1:9f:90
peer = b'\x50\x02\x91\xa1\x9f\x90'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
        print(host, msg)
        if msg == b'end':
            break