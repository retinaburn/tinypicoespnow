import network
from esp import espnow
import ubinascii

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
    print("poll: ",e.poll())
    print("stats:",e.stats())
    print("Receving....")
    host, msg = e.irecv(1000)     # Available on ESP32 and ESP8266
    print("....")
    if msg:             # msg == None if timeout in irecv()
        print(ubinascii.hexlify(host,':').decode(), msg.decode("utf-8"))
        #
    else:
        print("Nothing")