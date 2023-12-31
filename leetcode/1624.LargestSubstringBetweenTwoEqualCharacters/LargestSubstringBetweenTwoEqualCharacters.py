def maxLengthBetweenEqualCharacters(s):

    # another solution
    """res = -1

    for l in range(len(s) - 1):
        print(f"s[l]: {s[l]}")
        for r in range(l+1, len(s)):
            print(f"s[r]: {s[r]}")
            if s[l] == s[r]:
                res = max(res, len(s[l:r - 1]))
                print(f"res: {res}")
    return res"""

    charIndex = {}
    res = -1

    for i, c in enumerate(s):

        if c in charIndex:
            res = max(res, i - charIndex[c] - 1)
        else:
            charIndex[c] = i

    return res


if __name__ == '__main__':
    s = "abckdjana"
    print(maxLengthBetweenEqualCharacters(s))
    # 7