# https://www.hackerrank.com/challenges/equality-in-a-array

n = int(input())
a = list(map(int, raw_input().strip().split(' ')))
print(n - max([a.count(t)for t in set(a)]))
