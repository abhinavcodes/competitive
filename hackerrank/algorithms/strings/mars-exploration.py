# https://www.hackerrank.com/challenges/mars-exploration
#!/bin/python

import sys


radio = raw_input().strip()
count = 0
for start in xrange(0, len(radio), 3):
    now = radio[start:start + 3]
    if now[0] != 'S':
        count += 1
    if now[1] != 'O':
        count += 1
    if now[2] != 'S':
        count += 1
print count
