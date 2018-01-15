# https://www.hackerrank.com/challenges/jumping-on-the-clouds
#!/bin/python
import sys


def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < (len(c)):
        try:
            if c[i + 2] == 0:
                i += 2
            else:
                i += 1
            count += 1
        except:
            if i < (len(c) - 1):
                count += 1
            i = len(c) + 1

    return count

if __name__ == "__main__":
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))
    result = jumpingOnClouds(c)
    print result
