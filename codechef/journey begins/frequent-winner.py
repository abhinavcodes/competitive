# https://www.codechef.com/JOBE2018/problems/FRW

from collections import defaultdict

a = int(raw_input().strip())
n = raw_input().strip().split()
dict_names = defaultdict()
for item in set(n):
    dict_names.setdefault(item, n.count(item))
max_val = max(dict_names.values())
names = [key for key, value in dict_names.items() if value == max_val]
names.sort(reverse=True)
print names[0]
