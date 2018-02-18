# https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette

#!/bin/python

import sys


def revisedRussianRoulette(doors):
    locked = 0
    doors_len = len(doors)
    i = 0
    while i < doors_len:
        if doors[i] == 1:
            locked += 1
            i += 2
        else:
            i += 1
    print locked,
    print doors.count(1)

if __name__ == "__main__":
    n = int(raw_input().strip())
    doors = map(int, raw_input().strip().split(' '))
    revisedRussianRoulette(doors)
