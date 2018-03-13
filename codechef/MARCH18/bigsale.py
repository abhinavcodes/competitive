# https://www.codechef.com/MARCH18B/problems/BIGSALE

t = int(raw_input().strip())

for i in xrange(t):
    n = int(raw_input().strip())
    li = list()
    for j in xrange(n):
        li.append(map(float, raw_input().strip().split()))
    loss = 0
    for z in xrange(n):
        a = li[z][0] * li[z][1]
        b = (1 + (li[z][2] / 100))
        c = (1 - (li[z][2] / 100))
        d = a - (a * b * c)
        if d > 0:
            loss += abs(d)
        else:
            loss -= d
    print loss
