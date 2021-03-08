#! /usr/bin/python3

import NMAP_scanner()

scanner = NMAP_scanner.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)



