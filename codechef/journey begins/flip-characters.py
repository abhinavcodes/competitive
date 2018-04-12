# https://www.codechef.com/JOBE2018/problems/FLC

inp_string = raw_input()

li = []
for i in inp_string:
    if i.isupper():
        li.append(i.lower())
    else:
        li.append(i.upper())

print ''.join(i for i in li)
