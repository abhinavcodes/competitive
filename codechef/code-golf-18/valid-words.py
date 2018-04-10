# https://www.codechef.com/COLF2018/problems/APR103

inp = raw_input().strip().split()
results = list()

for item in inp:
    if not item[0].isdigit() and item[1] in ('a', 'e', 'i', 'o', 'u'):
        results.append(item)

print ''.join(item[0] for item in sorted(results, key=lambda x: x[0]))
