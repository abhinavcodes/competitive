# https://www.codechef.com/problems/INTEST

x, y = map(int, raw_input().split())
li = []
for i in xrange(x):
    q = input()
    li.append(q)
cnt = 0
for i in li:
    if (i % y == 0):
        cnt = cnt + 1
print cnt
