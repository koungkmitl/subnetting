#!/usr/bin/python

'''
Wildcard mask is 32-bit filter that used to specify range of interesting IP address when

- 0 bit means must be interesting, should be the same as network ID
- 1 bit means ignore, can be 0 or 1

For example 192.168.0.0 with 0.0.0.255 wildcard mask:

- 192.168.0.0 is 11000000.10101000.0000000.00000000
- 0.0.0.255   is 00000000.00000000.0000000.11111111

As you can see from wildcard mask, there are eight "1" at the last segment of wildcard mask that shoul be ignored and can be 0 or 1.
So, the translation of 192.168.0.0 with 0.0.0.255 wildcard mask is the IP range between 192.168.0.0 - 192.168.0.255

Another example, 192.168.0.0 with 0.0.0.127 wildcard mask:

- 192.168.0.0 is 11000000.10101000.00000000.0000000
- 0.0.0.127   is 00000000.00000000.00000000.0111111
- ???         is 11000000.10101000.00000000.0xxxxxx

From ???, "x" can be 0 or 1. So, the ??? is the IP range between 192.168.0.0 ("x" is all 0) - 192.168.0.127 ("x" is all 1)

Wildcard mask is inverse of subnet mask, it can be find more easily by using wildcard mask = 255 - subnet mask

Wildcard mask calculator: http://www.subnetonline.com/pages/subnet-calculators/ipv4-wildcard-calculator.php
'''
