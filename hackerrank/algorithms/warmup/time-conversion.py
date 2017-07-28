# https://www.hackerrank.com/challenges/time-conversion

time = raw_input().strip()
a = len(time)
if time[a - 2:] == "AM":
    z = int(time[:2])
    if z == 12:
        z = 0
        time = str(z) + str(z) + time[2:a - 2]
        print time
    else:
        print time[:-2]
else:
    z = int(time[:2])
    if z < 12:
        z = z + 12
    time = str(z) + time[2:a - 2]
    print time
