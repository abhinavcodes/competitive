# https://www.hackerrank.com/challenges/breaking-best-and-worst-records


def getrecord(s):
    max = s[0]
    min = s[0]
    count = 0
    count1 = 0
    for i in xrange(len(s)):
        if s[i] > max:
            count += 1
            max = s[i]
        if s[i] < min:
            count1 += 1
            min = s[i]
    print count, count1

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
getrecord(s)
