# https://www.codechef.com/problems/TEST

number = input()
li = []
while number != 42:
    li.append(number)
    number = input()
else:
    for num in li:
        print num
