# https://www.hackerrank.com/challenges/plus-minus

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
count = 0.0
count1 = 0.0
count2 = 0.0
for i in xrange(n):
    if arr[i] == 0:
        count += 1
    elif arr[i] > 0:
        count1 += 1
    else:
        count2 += 1
print count1 / len(arr)
print count2 / len(arr)
print count / len(arr)
