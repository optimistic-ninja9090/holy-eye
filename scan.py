#!/usr/bin/python

import nmap
scann = nmap.PortScanner()

ip_addr= input("Enter the IP address: ")
type(ip_addr)

resp = input("""\n Please enter the type of scan you want to run
1. SYN ACK Scan
2. UDP Scan
3. Comprehensive Scan \n""")
print("You have selected option: ", resp)

if resp == '1':
    print('Nmap Version: ', scann.nmap_version())
    scann.scan(ip_addr, '1-10024', '-v -sS')
    print(scann.scaninfo())
    print("IP Status: ", scann[ip_addr].state())
    print(scann[ip_addr].all_protocols())
    print("Open Ports: ", scann[ip_addr]['tcp'].keys())
elif resp == '2':
    print('Nmap Version: ', scann.nmap_version())
    scann.scan(ip_addr, '1-65535', '-v -sU')
    print(scann.scaninfo())
    print("IP Status: ", scann[ip_addr].state())
    print(scann[ip_addr].all_protocols())
    print("Open Ports: ", scann[ip_addr]['udp'].keys())
elif resp == '3':
    print('Nmap Version: ', scann.nmap_version())
    scann.scan(ip_addr, '1-65535', '-v -sU')
    print(scann.scaninfo())
    print("IP Status: ", scann[ip_addr].state())
    print(scann[ip_addr].all_protocols())
    print("Open Ports: ", scann[ip_addr]['udp'].keys())

