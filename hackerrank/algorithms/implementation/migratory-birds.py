# https://www.hackerrank.com/challenges/migratory-birds

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
li = [0] * (n)
# your code goes here
for i in xrange(n):
    li[types[i] - 1] = li[types[i] - 1] + 1
print li.index(max(li)) + 1
