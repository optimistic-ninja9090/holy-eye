#!/bin/bash

read IPADDR

echo "Scanning $IPADDR"

nmap -sV -sC -oA $IPADDR $IPADDR

echo "Scan complete"
