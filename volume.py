import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
duty_cycle = 10 #default value, 0-100
#duty cycle is the same as the volume percentage

print("Press Ctrl+C to exit the program")

if (len(sys.argv) > 1):
    try:
        duty_cycle = int(sys.argv[1])
        print(f"Duty Cycle: {sys.argv[1]}")
    except ValueError:
        print("Invalid input")
else:
    print("no args entered, using default value")

try:
    #pin number, frequency
    pwm = GPIO.pwm(7, 400)
    pwm.start(duty_cycle)
    time.sleep(10)
except KeyboardInterrupt:
    print("interrupted")
except ValueError:
    print("invalid input")

print("cleaning up")
GPIO.cleanup()