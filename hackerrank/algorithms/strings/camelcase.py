# https://www.hackerrank.com/challenges/camelcase
#!/bin/python
import sys


s = raw_input().strip()
count = 0
for i in s:
    if i.isupper():
        count += 1
count += 1
print count
