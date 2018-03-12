# https://www.codechef.com/MARCH18B/problems/CHEGLOVE

t = int(raw_input().strip())

for i in xrange(t):
    n = int(raw_input().strip())
    finger_len = map(int, raw_input().strip().split())
    glove_len = map(int, raw_input().strip().split())
    flag = 0
    flag1 = 0
    for i in xrange(n):
        if finger_len[i] > glove_len[i]:
            flag = 1
            break
    glove_len = glove_len[::-1]
    for i in xrange(n):
        if finger_len[i] > glove_len[i]:
            flag1 = 1
            break
    if flag == 0 and flag1 == 0:
        print "both"
    elif flag == 0:
        print "front"
    elif flag1 == 0:
        print "back"
    else:
        print "none"
