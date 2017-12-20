#https://www.hackerrank.com/challenges/bon-appetit/problem

n, k = map(int, raw_input().strip().split(' '))
li = map(int, raw_input().strip().split(' '))
b = input()
a = sum(li) - li[k]
a = a / 2
if a == b:
    print "Bon Appetit"
else:
    print b - a
