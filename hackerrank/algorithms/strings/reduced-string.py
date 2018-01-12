# https://www.hackerrank.com/challenges/reduced-string


def super_reduced_string(s):
    list_string = list(s)
    count = 0
    while count < len(list_string) - 1:
        if list_string[count] == list_string[count + 1]:
            del list_string[count]
            del list_string[count]
            count = 0
        else:
            count += 1

    if len(list_string) == 0:
        return 'Empty String'

    return ''.join(list_string)

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
