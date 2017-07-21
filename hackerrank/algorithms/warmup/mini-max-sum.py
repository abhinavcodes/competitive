# https://www.hackerrank.com/challenges/mini-max-sum

a, b, c, d, e = raw_input().strip().split(' ')
a, b, c, d, e = [int(a), int(b), int(c), int(d), int(e)]
arr = list([a, b, c, d, e])
arr.sort()
print sum(arr[:4]), sum(arr[1:])
