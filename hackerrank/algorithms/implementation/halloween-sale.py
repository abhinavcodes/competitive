# https://www.hackerrank.com/challenges/halloween-sale


def howManyGames(p, d, m, s):
    count_of_games = 0
    while s > 0:
        if p >= m:
            s -= p
            p -= d
        else:
            s -= m
        if s >= 0:
            count_of_games += 1
    return count_of_games

if __name__ == "__main__":
    p, d, m, s = raw_input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print answer
