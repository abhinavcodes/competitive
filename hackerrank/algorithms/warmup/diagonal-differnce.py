# https://www.hackerrank.com/challenges/diagonal-difference

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)
max = n - 1
sum = 0
sum1 = 0
for i in xrange(n):
    sum += a[i][i]
    sum1 += a[i][max]
    max -= 1
print abs(sum - sum1)
