# https://www.hackerrank.com/challenges/service-lane


def serviceLane(n, cases, width):
    for i in cases:
        print min(width[i[0]:(i[1] + 1)])

if __name__ == "__main__":
    n, t = raw_input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = map(int, raw_input().strip().split(' '))
    cases = []
    for cases_i in xrange(t):
        cases_temp = map(int, raw_input().strip().split(' '))
        cases.append(cases_temp)
    serviceLane(n, cases, width)
