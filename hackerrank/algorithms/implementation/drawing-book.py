# https://www.hackerrank.com/challenges/drawing-book
#!/bin/python

import sys


def solve(n, p):
    a = p / 2
    b = n / 2 - p / 2
    return min(a, b)

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
