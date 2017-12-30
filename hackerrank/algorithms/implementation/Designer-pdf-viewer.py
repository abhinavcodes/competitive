# https://www.hackerrank.com/challenges/designer-pdf-viewer


#!/bin/python
import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
max = -1
for i in word:
    if h[ord(i) - 97] > max:
        max = h[ord(i) - 97]
print max * len(word)
