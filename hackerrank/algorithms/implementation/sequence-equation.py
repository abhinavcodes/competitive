# https://www.hackerrank.com/challenges/permutation-equation


def permutationEquation(n, p):
    for i in xrange(n):
        print p.index((p.index(i + 1) + 1)) + 1

if __name__ == "__main__":
    n = int(raw_input().strip())
    p = map(int, raw_input().strip().split(' '))
    permutationEquation(n, p)
