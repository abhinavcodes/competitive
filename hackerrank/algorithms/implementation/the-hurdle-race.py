# https://www.hackerrank.com/challenges/the-hurdle-race
#!/bin/python
import sys


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
height = map(int, raw_input().strip().split(' '))
a = max(height)
if k > a:
    print "0"
else:
    print a - k
