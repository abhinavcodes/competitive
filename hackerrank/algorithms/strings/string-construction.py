# https://www.hackerrank.com/challenges/string-construction
#!/bin/python

import sys


def stringConstruction(s):
    cost = 0
    p = ''
    for i in s:
        if i not in p:
            p += i
            cost += 1
    return cost

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = stringConstruction(s)
        print result
