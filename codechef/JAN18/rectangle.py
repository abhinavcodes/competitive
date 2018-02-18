# https://www.codechef.com/JAN18/problems/RECTANGL

n = int(raw_input())

for i in xrange(n):
    li = map(int, raw_input().strip().split())
    li.sort()
    if li[0] == li[1] and li[2] == li[3]:
        a = li[0] ** 2 + li[2] ** 2
        b = li[1] ** 2 + li[3] ** 2
        if a == b:
            print "YES"
        else:
            print "NO"
    else:
        print "NO"
