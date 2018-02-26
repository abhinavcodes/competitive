# https://www.hackerrank.com/challenges/lisa-workbook/problem

n, k = map(int, raw_input().split())
t = map(int, raw_input().split())

speical = 0
i = 0
page_no = 1
m = 1

while i < n:
    if m <= page_no and page_no <= min(m + k - 1, t[i]):
        speical += 1
    page_no += 1
    m += k
    if m > t[i]:
        i += 1
        m = 1
print speical
