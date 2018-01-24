# https://www.hackerrank.com/challenges/insertionsort1
#!/bin/python


def insertionSort(ar):
    a = len(ar)
    i = a - 1
    b = ar[i]
    i -= 1
    while i >= 0:
        if ar[i] > b:
            ar[i + 1] = ar[i]
        elif ar[i] < b:
            ar[i + 1] = b
            print " ".join(map(str, ar))
            return
        print " ".join(map(str, ar))
        i -= 1
    ar[0] = b
    print " ".join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
