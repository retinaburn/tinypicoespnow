# ESP32 Reminders


## Rebuild:

1. Open Git Bash
2. cd ~/Downloads/build-GENERIC
3. esptool.py -p COM6 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 bootloader/bootloader.bin 0x8000 partition_table/partition-table.bin 0x10000 micropython.bin

## To Flash the TinyPico Stuff
1. Open Git Bash
2. cd ~/Downloads
3. Erase Flash
esptool.py --chip esp32 --port COM4 erase_flash
3. esptool.py --chip esp32 --port COM4 --baud 912600 write_flash -z 0x1000 tinypico-20220117-v1.18.bin



## Trying out ulab
1. Open Git Bash
2. cd ~/Downloads/build-GENERIC-ulab
3. esptool.py --chip esp32 --port COM6 --baud 460800 write_flash -z 0x10000 micropython.bin

## ESPNOW MicroPython from https://github.com/glenn20/micropython-espnow-images
1. esptool.py --chip esp32 --port COM4 --baud 912600 write_flash -z 0x1000 ~/Downloads/firmware-esp32-UM_TINYPICO.bin
2. esptool.py --chip esp32 --port COM7 --baud 912600 write_flash -z 0x1000 ~/Downloads/firmware-esp32-UM_TINYPICO.bin

b'0\x83\x98\xc8\xad\xec' 30:83:98:c8:ad:ec
# old 50:02:91:a1:a1:70
# new receiver 50:02:91:a1:9f:90

## Development
1. pip3 install adafruit-ampy
2. ampy -p COM4 put main.py