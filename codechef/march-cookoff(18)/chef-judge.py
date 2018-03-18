# https://www.codechef.com/COOK92B/problems/CO92JUDG

t = int(raw_input().strip())

for i in xrange(t):
    n = int(raw_input().strip())
    li = map(int, raw_input().strip().split())
    li1 = map(int, raw_input().strip().split())
    sum_1 = sum(li) - max(li)
    sum_2 = sum(li1) - max(li1)
    if sum_1 == sum_2:
        print "Draw"
    elif sum_1 < sum_2:
        print "Alice"
    else:
        print "Bob"
