import sys
from max6675 import Max6675
from time import sleep
bus, spi = 0, 0

def updateTemp(event = None):
    sensor = Max6675(bus, spi)
    print(sensor.temperature)

if len(sys.argv) >= 2:
    bus = int(sys.argv[1])
if len(sys.argv) >= 3:
    spi = int(sys.argv[2])

while True:
    try:
        updateTemp()
        sleep(1)
    except KeyboardInterrupt:
        break

print("\nprogram exited")
