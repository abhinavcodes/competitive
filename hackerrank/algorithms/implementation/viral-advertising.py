# https://www.hackerrank.com/challenges/strange-advertising
n = int(raw_input())

count = 2
people = 5 / 2
for i in xrange(1, n):
    people = (people * 3)
    people = people / 2
    count += people
print count
