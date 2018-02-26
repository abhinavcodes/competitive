# https://www.hackerrank.com/challenges/manasa-and-stones


def stones(n, a, b):
    print ' '.join(map(str, sorted({x * a + (n - 1 - x) * b for x in xrange(n)})))


if __name__ == "__main__":
    T = int(raw_input().strip())
    for a0 in xrange(T):
        n = int(raw_input().strip())
        a = int(raw_input().strip())
        b = int(raw_input().strip())
        stones(n, a, b)
