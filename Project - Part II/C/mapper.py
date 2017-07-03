#!/usr/bin/python

import sys
import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity, username, time, zone, commmand, filename, protocol, status, size = data
		path = urlparse.urlparse(filename).scheme + urlparse.urlparse(filename).path
        print "{0}\t{1}".format(path, 1)

