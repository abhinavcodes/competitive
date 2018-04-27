# https://www.codechef.com/problems/RECIPE


def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

n = int(raw_input().strip())

for i in xrange(n):
    li = map(int, raw_input().strip().split())
    li = li[1:]
    result = li[0]
    for i in xrange(len(li)):
        result = find_gcd(li[i], result)
    for i in xrange(len(li)):
        print li[i] / result,
    print ""
