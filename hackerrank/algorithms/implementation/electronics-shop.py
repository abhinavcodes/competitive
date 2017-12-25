# https://www.hackerrank.com/challenges/electronics-shop
#!/bin/python

import sys


def getMoneySpent(keyboards, drives, s):
    if (min(keyboards) + min(drives)) > s:
        return -1
    else:
        max_cost = -1
        for i in keyboards:
            for j in drives:
                if (j + i) > max_cost and (j + i) <= s:
                    max_cost = j + i
        return max_cost

s, n, m = raw_input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
