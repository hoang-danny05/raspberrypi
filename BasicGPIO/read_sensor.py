#demo class to read from our vacuum sensor. #sudo rpigpiod
import RPi.GPIO as GPIO

class VacuumSensor():
    def __init__(self, pin = 7):
        GPIO.setmode(GPIO.board)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_sensor(self):
        return(GPIO.input(self.pin))
    
    def __del__(self):
        del self
        GPIO.cleanup()
        print("cleaning up")


