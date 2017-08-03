# https://www.hackerrank.com/challenges/apple-and-orange


s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))
count = 0
count1 = 0
for i in apple:
    if a + i >= s and a + i <= t:
        count += 1
for i in orange:
    if b + i >= s and b + i <= t:
        count1 += 1
print count
print count1
