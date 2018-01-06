# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

#!/bin/python

import sys


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
sum = 0
for i in xrange(0, n, k):
    sum += 1 + 2 * c[i]
print 100 - sum
