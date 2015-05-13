#!/usr/bin/python

from netaddr import *
import pprint
import sys

networkaddr = []

def usedMask(number):
    for i in xrange(16):
        if 2**i >= number+2:
            cider = 2**i
            break
        else:
            2**i
    # cidr = host
    return 32-i

def firstSubnet(ip, number):
    cidr = usedMask(number)
    temp_ip = str(ip.ip) + "/" + str(cidr)
    ip = IPNetwork(temp_ip)
    networkaddr.append(ip)
    print networkaddr

def main():
    amount = []
    ip = IPNetwork(raw_input("Enter IP Address with subnet mask: "))
    subnet_amount = input("Enter amount of subnet: ")
    for i in xrange(subnet_amount):
        amount.append(input("Enter amount of hosts: "))
    for i in xrange(subnet_amount):
        firstSubnet(ip, amount[i])

if __name__ == "__main__":
    main()
