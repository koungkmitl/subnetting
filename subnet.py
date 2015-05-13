#!/usr/bin/python

import sys
import re

def checkIP(ip):
    matchIP = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return matchIP.match(ip)

def maskToCIDR(string):
    counter = 0
    number_list = []
    if checkIP(string):
        temp_list = string.split(".")
        for number in temp_list:
            number_list.append(bin(int(number)))
        for element in number_list:
            counter += element.count("1")
        return string + " is " + "/" + str(counter)
    else:
        sys.exit("Wrong enterred!")

def CIDRToMask(string):
    string = string.strip("/")
    mask = ('1'*int(string))+('0'*(32-int(string)))
    mask_list = ""
    temp = []
    for i in xrange(32):        
        if i%8 == 0 and i != 0:
            mask_list += "."
            mask_list += mask[i]
        else:
            mask_list += mask[i]

    mask_list = mask_list.split(".")
    for element in mask_list:
        temp.append(int(element, 2))
    return temp

def subnetFromAmount(amount):
    for i in xrange(16):
        if 2**i >= amount+2:
            cidr = 2**i
            break
        else:
            2**i
    # cidr = host
    mask = 32-i

def main():
    amount = []
    ip = raw_input("Enter IP address: ")
    subnet = raw_input("Enter subnet mask or CIDR: ")
    temp = input("Enter amount of subnetting: ")
    for i in xrange(0, temp):
        amount.append(input("Subnet " + str(i+1) + ": "))

if __name__ == '__main__':
    # main()
    subnetFromAmount(30)
