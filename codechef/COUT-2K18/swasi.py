# https://www.codechef.com/problems/SWASI

from collections import Counter

t = int(raw_input().strip())

for i in xrange(t):
    x = raw_input().strip()
    c = Counter(x)
    a = c['a'] + c['e'] + c['i'] + c['o'] + c['u']
    b = sum(c.values()) - a
    print a,
    print b
