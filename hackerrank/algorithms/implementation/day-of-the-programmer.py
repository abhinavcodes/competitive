# https://www.hackerrank.com/challenges/day-of-the-programmer
#!/bin/python
import sys


def solve(year):
    if year < 1918:
        if year % 4 == 0:
            print "12.09." + str(year)
        else:
            print "13.09." + str(year)
    elif year == 1918:
            print "26.09." + str(year)
    elif year >= 1919:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print "12.09." + str(year)
        else:
            print "13.09." + str(year)
year = int(raw_input().strip())
solve(year)
