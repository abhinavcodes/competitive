# https://www.codechef.com/JOBE2018/problems/GBP

n, m = map(int, raw_input().strip().split())

if bin(n).count('0') == bin(m).count('0') and bin(n).count('1') == bin(m).count('1'):
    print "good"
else:
    print "bad"
