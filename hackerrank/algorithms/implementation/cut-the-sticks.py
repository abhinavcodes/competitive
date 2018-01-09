# https://www.hackerrank.com/challenges/cut-the-sticks
#!/bin/python
import sys


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
arr.sort()
while len(arr)>0:
    a = arr[0]
    print len(arr)
    arr = list(map(lambda x: x - a, arr))
    while arr[0] == 0:
        arr.remove(0)
