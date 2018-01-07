# https://www.hackerrank.com/challenges/find-digits

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n1 = str(n)
    count = 0
    for i in n1:
        if int(i) != 0:
            if n % int(i) == 0:
                count += 1
    print count
