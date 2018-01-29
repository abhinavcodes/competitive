# https://www.hackerrank.com/challenges/quicksort1
#!/bin/python


def partition(ar): 
    left = []
    right = []
    equal = []
    equal.append(ar[0])
    for i in xrange(1, len(ar)):
        if ar[i] > equal[0]:
            right.append(ar[i])
        elif ar[i] < equal[0]:
            left.append(ar[i])
        else:
            equal.append(ar[i])
    print " ".join('%d'%x for x in left),
    print " ".join('%d'%x for x in equal),
    print " ".join('%d'%x for x in right),

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
