# https://www.hackerrank.com/challenges/the-time-in-words

#!/bin/python

import sys

def timeInWords(h, m):
    hour = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    minutes = ["zero",
               "one minute",
               "two minutes",
               "three minutes",
               "four minutes",
               "five minutes",
               "six minutes",
               "seven minutes",
               "eight minutes",
               "nine minutes",
               "ten minutes",
               "eleven minutes",
               "twelve minutes",
               "thirteen minutes",
               "fourteen minutes",
               "quarter",
               "sixteen minutes",
               "seventeen minutes",
               "eighteen minutes",
               "nineteen minutes",
               "twenty minutes",
               "twenty one minutes",
               "twenty two minutes",
               "twenty three minutes",
               "twenty four minutes",
               "twenty five minutes",
               "twenty six minutes",
               "twenty seven minutes",
               "twenty eight minutes",
               "twenty nine minutes"
               ]
    if m == 0:
        print hour[h - 1] + " o' clock"
    elif m <= 29:
        print minutes[m] + " past " + hour[h - 1]
    elif m == 30:
        print "half past " + hour[h - 1]
    elif m >= 31 and m <= 59:
        print minutes[60 - m] + " to " + hour[h]


if __name__ == "__main__":
    h = int(raw_input().strip())
    m = int(raw_input().strip())
    timeInWords(h, m)
