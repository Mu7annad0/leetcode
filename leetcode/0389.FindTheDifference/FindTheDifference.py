def find_the_difference(s, t):
    for char in t:
        if s.count(char) < t.count(char):
            return char


if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(find_the_difference(s, t))
    # e
