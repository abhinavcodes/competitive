# https://www.hackerrank.com/challenges/funny-string
#!/bin/python

import sys


def funnyString(s):
    rev_string = s[::-1]
    len_string = len(s)
    count = 1
    while count < (len_string - 1):
        a = abs(ord(s[count]) - ord(s[count - 1]))
        b = abs(ord(rev_string[count]) - ord(rev_string[count - 1]))
        if a != b:
            return "Not Funny"
        count += 1
    return "Funny"


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)
