# https://www.codechef.com/problems/ADI

n = int(raw_input().strip())

for i in xrange(n):
    x = raw_input().strip()

    if 'a' in x and 'e' in x and 'i' in x and 'o' in x and 'u' in x:
        print x
