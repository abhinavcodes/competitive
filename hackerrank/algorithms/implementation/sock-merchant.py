#https://www.hackerrank.com/challenges/sock-merchant/problem

from collections import Counter

n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' '))
cnt = Counter(c)
count = 0
for key, value in cnt.items():
    val = value / 2
    count += val
print count
