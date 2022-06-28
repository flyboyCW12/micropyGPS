from machine import Pin
from machine import UART

p18 = Pin(18, Pin.IN) #Rx
P19 = Pin(19, Pin.OUT) #Tx

uart2 = UART(2, baudrate = 9600, tx =19, rx = 18, bits = 8, parity = None, stop = 1)
print('UART2 Initialised')

while True:
    data = uart2.read(1) # Reads one byte

    if data is not None:
        # Show the byte as 2 hex digits then in the default way
        print("%02x " % (data[0]), end='')
        print(data)
        
        ''' These two lines attempt to decode the data but always generate
a unicode error.
        # output = data.decode()
        # print(output)'''
        
        