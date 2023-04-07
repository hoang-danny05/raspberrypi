import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    try:
        if GPIO.input(pin):
            print("PRESSED")
            time.sleep(.5)
        else:
            print("NOT PRESSED")
            time.sleep(.5)
    except KeyboardInterrupt:
        print("\n exited")
        break
