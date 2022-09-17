import pyfiglet
import sys
import socket
import os
import nmap
from requests import get
from datetime import datetime
  
ascii_banner = pyfiglet.figlet_format("Holy Eye")
print(ascii_banner)
target = input("Enter the host: ")  

 
# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)
  
try:
     
    # will scan ports between 1 to 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

os.system("arp -a") 
hostname = socket.gethostname()   
print("Hostname: " + hostname)

#ipify; will fail if no internet connection
ip = get('https://api.ipify.org').content.decode('utf8')
print('Public IP: {}'.format(ip))
