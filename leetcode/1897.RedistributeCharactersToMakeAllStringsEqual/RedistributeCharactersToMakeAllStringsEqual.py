from collections import defaultdict


def makeEqual(words):
    charCount = defaultdict(int)

    for w in words:
        for c in w:
            charCount[c] += 1

    for c in charCount:
        if charCount[c] % len(words):
            return False

    return True


if __name__ == '__main__':
    words = ["abc", "aabc", "bc"]
    print(makeEqual(words))
    # True
