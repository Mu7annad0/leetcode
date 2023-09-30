def mergeAlternately(word1, word2):
    """
        It takes two strings, word1 and word2, as input and returns a new string that is the result of merging the two strings alternately,
        starting with word1. If one string is longer than the other, the remaining letters of the longer string are appended to the end of the merged string.
    """

    new_word = ""
    length = min(len(word1), len(word2))

    for i in range(length):
        new_word += word1[i] + word2[i]

    return new_word + word1[length:] + word2[length:]

if __name__ == "__main__":
    word1, word2 = "ab", "pqrs"
    print(mergeAlternately(word1, word2))
    # apbqrs

