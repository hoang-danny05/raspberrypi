#script to test RPi.GPIO's digital input
#intended to read a vacuum switch

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.IN) #4 is the pin number

while True:
    print(GPIO.input(4)) #Reads the input from the pi
