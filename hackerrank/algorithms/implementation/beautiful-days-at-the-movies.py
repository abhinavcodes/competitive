# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

i, j, k = raw_input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]
count = 0
for z in xrange(i, j + 1):
    rev = int(str(z)[::-1])
    if (z - rev) % k == 0:
        count += 1
print count
