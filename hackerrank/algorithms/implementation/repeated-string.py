# https://www.hackerrank.com/challenges/repeated-string
#!/bin/python
import sys


s = raw_input().strip()
n = long(raw_input().strip())
b = s.count('a')
a = len(s)
c = n / a
b = b * c
n = n - (c * a)
s = s[:n]
c = s.count('a')
b = b + c
print b
