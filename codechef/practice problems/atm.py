# https://www.codechef.com/problems/HS08TEST
x, y = map(float, raw_input().split())

if (x % 5 != 0 or (x + 0.50) > y):
    print y
else:
    print y - (x + 0.50)
