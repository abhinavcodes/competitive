#!/bin/python

q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    count = 0
    for a in xrange(1, x):
        if a ^ x > x:
            count += 1

    print count

