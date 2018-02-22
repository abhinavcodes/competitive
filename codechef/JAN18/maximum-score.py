# https://www.codechef.com/JAN18/problems/MAXSC

t = int(raw_input())

for i in xrange(t):
    final_sum = 0
    n = int(raw_input())
    li = list()
    for j in xrange(n):
        li.append(sorted(map(int, raw_input().split(' ')), reverse=True))
    z = n - 2
    a = max(li[n - 1])
    final_sum += a
    flag1 = 0
    while z >= 0 and flag1 == 0:
        i = 0
        flag = 0
        while i < n and flag == 0:
            b = li[z][i]
            if b < a:
                a = b
                flag = 1
            i += 1
        if flag == 0:
            final_sum = -1
            flag1 = 1
        else:
            final_sum += b
        z -= 1
    print final_sum
