#!/usr/bin/python
# -*- coding: utf-8 -*-

from netaddr import *
from bisect import bisect_left, bisect_right
import os

def usedMask(number):
    i = 1
    while(2**i < number+2):
        i = i +1
    return 32-i

def calculateSubnet(number):
    cidr = usedMask(number)
    subnets = list(ip.subnet(cidr))
    subnets.sort()
    if len(networkaddr):
        for i in xrange(len(subnets)):
            net = [networkaddr[-1], subnets[i]] # check overlap between last used subnet and possible subnet
            # print 'Compare [Last used, Possible]:', net
            if not(subnets_overlap(net)) and (networkaddr[-1] < subnets[i]): # if not overlap and current subnet less than possible subnet
                # print 'Add to subnet table:', subnets[i]
                networkaddr.append(subnets[i]) # put  possible subnet to subnet table
                break
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
    global networkaddr
    networkaddr = []
    amount = []
    ip = IPNetwork(raw_input("Enter IP Address with subnet mask: "))
    subnet_amount = input("Enter amount of subnet: ")
    for i in xrange(subnet_amount):
        amount.append(input("Enter amount of hosts: "))
    for i in xrange(subnet_amount):
        calculateSubnet(amount[i])
    # show subnet table
    print 'Network address\t\tBroadcast address\tSubnet mask\t\tCIDR'
    for result in networkaddr:
        # print '========== Subnet table =========='
        print '%s\t\t%s\t\t%s\t\t%s' % (result.network, result.broadcast, result.netmask, result.prefixlen)
        # print '=================================='
    os.system('pause')

if __name__ == "__main__":
    main()
