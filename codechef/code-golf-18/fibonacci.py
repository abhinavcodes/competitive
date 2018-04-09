# https://www.codechef.com/COLF2018/problems/APR102

MAX = 1000
f = [0] * MAX


def fib(n):
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])
    if (f[n]):
        return f[n]
    if(n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2
    if((n & 1)):
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]

a, b = map(int, raw_input().strip().split())
C = fib(b - 1)
e = C - (C % a)
d = a - (C % a) + C

if (C - e) > (d - C):
    print d
else:
    print e
