import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
endBanner = pyfiglet.figlet_format("END OF SCAN 07")
print(ascii_banner)

target = input(str('Target ip: '))
portStart = 0
portEnd = 0
rawInput = 0

# Ensures only valid port numbers are entered
while rawInput < 1 or rawInput > 65535:
    portStart = input(str('PORT RANGE Starting Port# (Min 1, Max 65535): '))
    rawInput = int(portStart)
    if rawInput >= 1 and rawInput <= 65535:
        portStart = rawInput
        rawInput = 0
        break

# Ensures only valid port numbers are entered
while rawInput < portStart  or rawInput > 65535:
    portEnd = input(str('PORT RANGE Ending Port# (Min ' + str(portStart) + ', Max 65535): '))
    rawInput = int(portEnd)
    if rawInput >= portStart and rawInput <= 65535:
        portEnd = rawInput + 1
        rawInput = 0
        break

##Banner##
print("*" * 50)
print("Scan start @: " + str(datetime.now()))
print("*" * 50)

try:

    #Scan every port#
    for port in range(int(portStart),int(portEnd)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        ##Return open port##
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

        #Return closed port#
        if result != 0:
            print("   Port {} is closed".format(port))
            s.close()


except KeyboardInterrupt:
    print("\n Exitting ;-;")
    sys.exit()

except socket.error:
    print("\Host not responding ;-;")
    sys.exit()

else:
    #print("End of scan 07")##
    print(endBanner)