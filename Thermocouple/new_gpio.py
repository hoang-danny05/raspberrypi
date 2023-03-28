import pigpio
from time import sleep

#initializiation code
pi = pigpio.pi

if not pi.connected:
    exit(0)

while True:
    try:
        #pin number : int , state : bool 
        pi.write(4, 0)
        sleep(1)
        pi.write(4, 1)
        sleep(1)
    except KeyboardInterrupt:
        print("Manually Exited.")
        break
        

