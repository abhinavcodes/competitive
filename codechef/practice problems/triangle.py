# https://www.codechef.com/problems/AVNRTRI

n = int(raw_input().strip())

iso = []
for i in xrange(n):
    x, y, z = map(int, raw_input().strip().split())

    if x + y > z and x + z > y and y + z > x:
        if x == y == z:
            print "equilateral"
        elif x != y != z:
            print "scalene"
        else:
            print "isosceles"
            iso.append('yes')
    else:
        print "not triangle"
print len(iso)
