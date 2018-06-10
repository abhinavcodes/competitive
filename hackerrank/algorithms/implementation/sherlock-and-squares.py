# https://www.hackerrank.com/challenges/sherlock-and-squares/problem


import math


def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

n = int(raw_input().strip())
for i in xrange(n):
    a, b = map(int, raw_input().strip().split())
    print int(CountSquares(a, b))
