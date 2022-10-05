#!/bin/bash



echo "Type of scan (1-5)
1. Vulnerability
2. Quick
3. TCP
4. UDP
5. SYN"
read SCAN

echo "Enter IP address"
read IPADDR


echo "1 - Scan all ports
2 - Scan ports in custom range"
read PORTS

PORT1=0
PORT2=0

if [$PORTS = 1]
then
    echo "Enter port range start"
    read PORT1
    echo "Enter port range end"
    read PORT2
elif [$PORTS = 2]
then
    PORT1=1 
    PORT2=65535
else
    echo "Invalid option"
    
fi





# case $PORTS in
# 1) echo "Enter port range start" 
# read PORT1
# echo "Enter port range end"
# read PORT2;;
# 2) PORT1=1 PORT2=65535;;
# esac

case $SCAN in
#VULNERABILITY SCAN
1) nmap -sV --script vulners --script-args mincvss=5.0 -p$PORT1-$PORT2 $IPADDR 
;;
#QUICK SCAN
2) nmap -sS -sV -Pn -T4 -p$PORT1-$PORT2 $IPADDR
;;
#TCP SCAN
3) nmap -sS -sV -Pn -p$PORT1-$PORT2 $IPADDR
;;
#UDP SCAN
4) nmap -sS -sV -Pn -p$PORT1-$PORT2 $IPADDR
;;
#SYN SCAN
5) nmap -sS -sV -Pn -p$PORT1-$PORT2 $IPADDR
;;
esac

echo "Scanning $IPADDR"

    nmap -sV -sC -oA $IPADDR $IPADDR

echo "Scan complete"
