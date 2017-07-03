import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 10:
        ip, identity, username, time, zone, commmand, file, protocol, status, size = data
        print "{0}\t{1}".format(file, 1)

