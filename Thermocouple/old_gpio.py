import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while True:
    try:
        GPIO.output(7, True)
        print("ON")
        sleep(1)
        GPIO.output(7, False)
        print("OFF")
        sleep(1)
    except KeyboardInterrupt:
        print("exiting")
        break

GPIO.cleanup()
