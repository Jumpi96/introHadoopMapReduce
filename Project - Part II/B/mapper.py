#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, time, zone, commmand, filename, protocol, status, size = data
        print "{0}\t{1}".format(ip, 1)

