def maxScore(s):
    score = 0
    for i in range(1, len(s)):
        score = max(score, s[:i].count('0') + s[i:].count('1'))
    return score


if __name__ == '__main__':
    s = "011101"
    print(maxScore(s))
