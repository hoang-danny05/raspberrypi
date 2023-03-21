import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.OUT)

#blink
try:
    for i in range(10):
        gpio.output(pin, False)
        print("off")
        time.sleep(1)
        gpio.output(pin, True)
        print("on")
        time.sleep(1)
    print("loop naturally exited")
except KeyboardInterrupt:
    print("Exited.")

print("Cleaning Up")
GPIO.cleanup()
