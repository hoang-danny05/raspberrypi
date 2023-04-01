from time import sleep
import pigpio

pi = pigpio.pi()

#spi_channel, baud: 32K-30M, spi_flags: 22 bits
h1 = pi.spi_open(0, 100_000, 0)

def output():
    b, d = pi.spi_read(h1, 2) #reads two bytes from h1
    data = (d[0] << 8) | d[1] #condense 2 bytes into a variable
    #print(b, data) # debug
    #print(f"{b:0>4}", d[0], d[1]) #shows how to format
    if (data & 0x8006 > 0):
        print("ERROR")
    print_temp(data)


def print_temp(bytes):
    temp = (bytes >> 3) / 4.0
    print(f"{temp:.2f} C")

def print_int(bytes):
    num = (bytes >> 3) #shift 3 right, easy to convert to int
    print(int(bytes))

def print_binary(bytes):
    print("{:>16}".format(bin(bytes)))

while True:
    try:
        output()
        sleep(1)
    except KeyboardInterrupt:
        print("exited manually")
        break

pi.stop()
