#!/usr/bin/python

import sys

countHits = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", countHits
        oldKey = thisKey;
        countHits = 0

    oldKey = thisKey
    countHits += int(thisHit)

if oldKey != None:
    print oldKey, "\t", countHits

