# https://www.codechef.com/COOK92B/problems/CO92SUBW

n = int(raw_input().strip())

for i in xrange(n):
    x = int(raw_input().strip())
    i = 1
    j = 2
    time = 1
    flag = 0
    while flag == 0:
        if i + j <= x:
            i += j
            time += 1
            j += 1
        else:
            flag = 1
    if x == 1:
        time = 1
    elif x == 2:
        time = 2
    elif ((i + j) - x) < (x - i):
        time = time + (i + j - x) + 1
    else:
        time = time + (x - i)
    print time
