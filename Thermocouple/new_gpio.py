import pigpio
from time import sleep

#initializiation code
pi = pigpio.pi()

if not pi.connected:
    exit(0)

pin = 4
pi.set_mode(pin, pigpio.OUTPUT)

while True:
    try:
        #pin number : int , state : bool 
        pi.write(pin, False)
        print("turned on")
        sleep(1)
        pi.write(pin, True)
        print("turned off")
        sleep(1)
    except KeyboardInterrupt:
        print("Manually Exited.")
        break


print("I'm done")
