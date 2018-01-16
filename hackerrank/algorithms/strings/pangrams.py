# https://www.hackerrank.com/challenges/pangrams 


from string import ascii_lowercase
s = raw_input().strip().lower()
if len([item for item in ascii_lowercase if item in s]) == 26:
    print "pangram"
else:
    print "not pangram"
