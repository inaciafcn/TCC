
import socket
#import Adafruit_BBIO.ADC as ADC
import time
#from decimal import *
import struct
import serial
MCAST_GRP = '225.0.0.37'
MCAST_PORT = 1406
#ADC.setup()
#getcontext().prec = 6
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
serTen = serial.Serial("/dev/ttyUSB0", 9600)

def trunc(num, digits):
   sp = str(num).split('.')
   return '.'.join([sp[0], sp[:digits]])

while(1):
   # pot1 = Decimal(ADC.read("P9_40"))
    #pot2 = Decimal(ADC.read("P9_39"))
    #pot3 = Decimal(ADC.read("P9_37"))
    #pot4 = Decimal(ADC.read("P9_35"))
    respostaTen = serTen.readline() 
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    message = ['t',float(respostaTen)]
    print len(message)
    sock.sendto(struct.pack('cf', *message), (MCAST_GRP, MCAST_PORT))
    time.sleep(0.5)




