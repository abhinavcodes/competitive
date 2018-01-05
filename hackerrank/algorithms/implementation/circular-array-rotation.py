# https://www.hackerrank.com/challenges/circular-array-rotation

#!/bin/python

import sys


n, k, q = raw_input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = map(int, raw_input().strip().split(' '))
k = k % n
a = a[(n - k):] + a[:(n - k)]
for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[m]
