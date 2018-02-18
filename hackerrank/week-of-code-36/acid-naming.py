# https://www.hackerrank.com/contests/w36/challenges/acid-naming


def acidNaming(acid_name):
    first_char = acid_name[:5]
    last_char = acid_name[(len(acid_name) - 2):]
    if first_char == "hydro" and last_char == "ic":
        return "non-metal acid"
    elif last_char == "ic":
        return "polyatomic acid"
    else:
        return "not an acid"

if __name__ == "__main__":
    n = int(raw_input().strip())
    for a0 in xrange(n):
        acid_name = raw_input().strip()
        result = acidNaming(acid_name)
        print result
