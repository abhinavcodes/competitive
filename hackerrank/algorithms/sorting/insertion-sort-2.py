# https://www.hackerrank.com/challenges/insertionsort2
#!/bin/python


def insertionSort(ar):
    for i in xrange(1, len(ar)):
        val = ar[i]
        j = i - 1
        while (j >= 0) and (ar[j] > val):
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = val
        print " ".join(map(str, ar))


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
