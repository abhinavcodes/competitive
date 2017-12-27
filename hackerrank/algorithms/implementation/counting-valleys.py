# https://www.hackerrank.com/challenges/counting-valleys

n = input()
arr = raw_input()
up = 0
count = 0
for item in arr:
    if item == 'U':
        up += 1
        if up == 0:
            count += 1
    elif item == 'D':
        up -= 1
print count
