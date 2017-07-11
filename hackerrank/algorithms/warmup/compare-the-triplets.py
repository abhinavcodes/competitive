#https://www.hackerrank.com/challenges/compare-the-triplets

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
count = 0
count1 = 0
if a0 > b0:
    count += 1
elif a0 < b0:
    count1 += 1
if a1 > b1:
    count += 1
elif a1 < b1:
    count1 += 1
if a2 > b2:
    count += 1
elif a2 < b2:
    count1 += 1
print count, count1
