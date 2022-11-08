import pyfiglet
import sys
import socket
import os
import nmap
from requests import get
from datetime import datetime
  
# ipaddr = input("Enter the IP address: ")

# optports = input(" 1. Scan all ports \n 2. Scan specific ports")

# optscan = input(" 1. Vulnerability Scan \n 2. Quick Scan")

def vulnerability_scan():
        scan = os.system("nmap -sV --script vulners --script-args mincvss=5.0 192.168.0.106")
        return scan

def quick_scan():
        quick = os.system("nmap -sS -sV -Pn -T4 192.168.0.106")
        return quick


# def main():
#      if optscan == "1":
#         vulnerability_scan()
#      elif optscan == "2":
#         quick_scan()
#      else:
#         print("Invalid option")
#         main()



# def option():
#     if optports == "1":
#         print("Scanning all ports")
#         scanall()
#     elif optports == "2":
#         print("Scanning specific ports")
#         scanports()
#     else:
#         print("Invalid option")
#         option()