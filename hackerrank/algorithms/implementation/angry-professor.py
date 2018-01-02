# https://www.hackerrank.com/challenges/angry-professor

t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))
    a.sort()
    if a[k - 1] <= 0:
        print "NO"
    else:
        print "YES"
