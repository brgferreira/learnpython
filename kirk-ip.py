#!/usr/bin/env python

ipaddr = '192.168.1.1'
octets = ipaddr.split('.')
print("\n")
print("-" * 80)
print("{:10}{:10}{:10}{:10}".format(*octets))
print("-" * 80)
print("\n")
