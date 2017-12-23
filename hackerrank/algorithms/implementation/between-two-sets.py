# https://www.hackerrank.com/challenges/between-two-sets

def getTotalX(a, b):
    start = a[len(a) - 1]
    end = b[0]
    total = 0
    while start <= end:
        flag = 0
        flag1 = 0
        for i in xrange(len(a)):
            if start % a[i] != 0:
                flag = 1
                break
        for i in xrange(len(b)):
            if b[i] % start != 0:
                flag1 = 1
                break
        if flag == 0 and flag1 == 0:
            total += 1
        start += 1
    return total

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total
