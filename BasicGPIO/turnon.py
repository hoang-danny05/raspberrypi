#this turns on GPIO4 for 10 seconds
import RPi.GPIO as GPIO
import time

#initialize stuff
GPIO.setmode(GPIO.BOARD) #use the board pin numbers
GPIO.setup(7, GPIO.OUT)


#turn on, CTRL+C to CANCEL/exit
try: 
    GPIO.output(7, True)
    print("Turned ON")
    time.sleep(10)
except KeyboardInterrupt:
    print("Ended Early")

print("Cleaning up")
GPIO.cleanup()
