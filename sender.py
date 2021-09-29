import network
from esp import espnow
from time import sleep

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)

e = espnow.ESPNow()
e.init()
# sender 50:02:91:a1:a1:70
# receive 50:02:91:a1:9f:90
peer = b'\x50\x02\x91\xa1\xa1\x70'   # MAC address of peer's wifi interface
try:
    e.add_peer(peer)
except OSError as err:
    if len(err.args) < 2:
        raise err
    if err.args[1] == 'ESP_ERR_ESPNOW_EXIST':
        print("Peer already exists")

peer = b'\x50\x02\x91\xa1\x9f\x90'   # MAC address of peer's wifi interface
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
    print("poll: ", e.poll())
    print("stats: ", e.stats())
    sendVal = str(i)*20
    e.send(sendVal)
    print("Sent: ", sendVal)
    sleep(1)
    e.send(b'end')