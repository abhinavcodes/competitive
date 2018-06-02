# https://www.hackerrank.com/challenges/library-fine/problem


def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 >= y2:
        if y1 > y2:
            return 10000
        elif m1 > m2:
            return ((m1 - m2) * 500)
        elif d1 > d2 and m1 >= m2:
            return ((d1 - d2) * 15)
        else:
            return 0
    else:
        return 0

if __name__ == "__main__":
    d1, m1, y1 = raw_input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = raw_input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print result
