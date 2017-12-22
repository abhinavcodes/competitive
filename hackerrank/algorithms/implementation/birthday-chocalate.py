# https://www.hackerrank.com/challenges/the-birthday-bar
#!/bin/python
import sys


def solve(n, s, d, m):
    b = 0
    count = 0
    while b < n:
        c = sum(s[b:(m+b)])
        if c == d:
            count += 1
        b += 1
    return count
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
