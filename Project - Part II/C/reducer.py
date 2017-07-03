#!/usr/bin/python

import sys

countHits = 0
maxCount = 0
maxKey = None
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        if countHits > maxCount:
			maxKey = oldKey
			maxCount = countHits
        oldKey = thisKey;
        countHits = 0

    oldKey = thisKey
    countHits += thisHit

if oldKey != None:
    if countHits > maxCount:
			maxKey = oldKey
			maxCount = countHits

print maxKey, "\t", maxCount

