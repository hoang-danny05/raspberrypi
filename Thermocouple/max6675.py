from time import sleep
import pigpio

# class to represent the reader for the max6675

pi = pigpio.pi()

#spi_channel, baud: 32K-30M, spi_flags: 22 bits
# MAX6675    RPI PIN
# GND  <----> GND  (6)
# VCC  <----> 3v3  (1)
# SCLK <----> SCLK (23)
# CS   <----> CE0  (24)
# SO   <----> MISO (21)

class MAX6675:
    def __init__(self):
        #initialize special things
        self.pi = pigpio.pi()
        self.h1 = pi.spi_open(0, 100_000, 0)

    def temp(self):
        b, d = self.pi.spi_read(self.h1, 2) #reads two bytes from h1
        data = (d[0] << 8) | d[1] #condense 2 bytes into a variable
        if b != 2:
            print("ERROR, DATA NOT RECIEVED")
        if (data & 0x8006 > 0):
            print("ERROR, INVALID DATA")
        return ((data >> 3) / 4.0)


    def output(self):
        b, d = self.pi.spi_read(self.h1, 2) #reads two bytes from h1
        data = (d[0] << 8) | d[1] #condense 2 bytes into a variable
        if b != 2:
            print("ERROR, DATA NOT RECIEVED")
        if (data & 0x8006 > 0):
            print("ERROR, INVALID DATA")
        self.print_temp(data)


    def print_temp(self, bytes):
        temp = (bytes >> 3) / 4.0
        print(f"{temp:.2f} C")

    def print_int(self, bytes):
        num = (bytes >> 3) #shift 3 right, easy to convert to int
        print((bytes))

    def print_binary(self, bytes):
        print("{:>16}".format(bin(bytes)))

    def cleanup(self):
        self.pi.stop()

    def __del__(self):
        self.cleanup()
        print("cleaning up")
