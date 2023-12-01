def arrayStringsAreEqual(word1, word2):

    # "easy answer"
    # first_word = ""
    # second_word = ""
    # for i in range(len(word1)):
    #     first_word += word1[i]
    # for j in range(len(word2)):
    #     second_word += word2[j]
    #
    # if first_word == second_word:
    #     return True
    # return False

    w1 = w2 = 0 # pointers for words
    c1 = c2 = 0 # pointers for char

    while w1 < len(word1) and w2 < len(word2):
        if word1[w1][c1] != word2[w2][c2]:
            return False

        c1, c2 = c1 + 1, c2 + 1
        if c1 == len(word1[w1]):
            w1 += 1
            c1 = 0
        if c2 == len(word2[w2]):
            w2 += 1
            c2 = 0

    if w1 != len(word1) or w2 != len(word2):
        return False

    return True

if __name__ == "__main__":
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(arrayStringsAreEqual(word1, word2))
    # True