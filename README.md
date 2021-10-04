# ESP32 Reminders


## Rebuild:

1. Open Git Bash
2. cd ~/Downloads/build-GENERIC
3. esptool.py -p COM6 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 bootloader/bootloader.bin 0x8000 partition_table/partition-table.bin 0x10000 micropython.bin

## To Flash the TinyPico Stuff
1. Open Git Bash
2. cd ~/Downloads
3. esptool.py --chip esp32 --port COM6 --baud 460800 write_flash -z 0x1000 tinypico-20210902-v1.17.bin
the above seems to do a complete image from 1000 .... what the


## Trying out ulab
1. Open Git Bash
2. cd ~/Downloads/build-GENERIC-ulab
3. esptool.py --chip esp32 --port COM6 --baud 460800 write_flash -z 0x10000 micropython.bin
