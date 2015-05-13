#!/usr/bin/python
# -*- coding: utf-8 -*-

from netaddr import *
from bisect import *
import pprint
import sys

networkaddr = []

def usedMask(number):
    for i in xrange(16):
        if 2**i >= number+2: #include network address and broadcast address
            cider = 2**i
            break
        else:
            2**i
    # cidr = host
    return 32-i

def firstSubnet(number):
    cidr = usedMask(number)
    subnets = list(ip.subnet(cidr))
    subnets.sort()
    possibleList = []
    if len(networkaddr):
        for i in xrange(len(subnets)):
            net = [networkaddr[-1], subnets[i]] # check overlap between last used subnet and possible subnet
            # print 'Compare [Last used, Possible]:', net
            if not(subnets_overlap(net)) and (networkaddr[-1] < subnets[i]): # if not overlap and current subnet less than possible subnet
                possibleList.append(subnets[i]) # add possible subnet to list
                # print 'Add possible subnet to list:', subnets[i]
        # print '============= Show possible subnet ============='
        # print possibleList
        # print '================================================'
        networkaddr.append(possibleList[0]) # put lowest possible subnet to subnet table
        # print 'Add possible subnet to subnet table:', possibleList[0]
    else:
        networkaddr.append(subnets[0]) # put first subnet to subnet table

def subnets_overlap(subnets):
    # ranges will be a sorted list of alternating start and end addresses
    ranges = []
    for subnet in subnets:
        # find indices to insert start and end addresses
        first = bisect_left(ranges, subnet.first)
        last = bisect_right(ranges, subnet.last)
        # check the overlap conditions and return if one is met
        if first != last or first % 2 == 1:
            return True
        ranges[first:first] = [subnet.first, subnet.last]
    return False

def main():
    global ip
    amount = []
    ip = IPNetwork(raw_input("Enter IP Address with subnet mask: "))
    subnet_amount = input("Enter amount of subnet: ")
    for i in xrange(subnet_amount):
        amount.append(input("Enter amount of hosts: "))
    for i in xrange(subnet_amount):
        firstSubnet(amount[i])
    # show subnet table
    for result in networkaddr:
        # print '========== Subnet table =========='
        print result, result.netmask
        # print '=================================='

if __name__ == "__main__":
    main()
