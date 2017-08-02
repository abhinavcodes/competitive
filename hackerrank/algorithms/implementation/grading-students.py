# https://www.hackerrank.com/challenges/grading


def solve(grades):
    li = []
    for i in xrange(len(grades)):
        if grades[i] < 38:
            li.append(grades[i])
        elif (grades[i] + 1) % 5 == 0:
            li.append(grades[i] + 1)
        elif (grades[i] + 2) % 5 == 0:
            li.append(grades[i] + 2)
        else:
            li.append(grades[i])
    return li

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
for i in xrange(len(result)):
    print result
