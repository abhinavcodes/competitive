# https://www.hackerrank.com/challenges/minimum-distances
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def minimumDistances(a):
    li1 = set([x for x in a if a.count(x) > 1])
    if not li1:
        return -1
    min_val = 10000
    for item in li1:
        b = duplicates(a, item)
        sub = abs(b[1] - b[0])
        if sub < min_val:
            min_val = sub
    return min_val

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = minimumDistances(a)
    print result
