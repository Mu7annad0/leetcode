from collections import Counter, defaultdict


def countCharacters(words, chars):
    """
    The function takes two arguments: a list of words (words) and a  string of characters (chars).
    It returns an integer representing the total number of characters in the words
    that do not contain any character exceeding its frequency limit as specified in the chars dictionary.
    The function uses a nested loop to iterate over each word in the input list
    and check whether it contains any character that violates the frequency limit.
    If a word is found to have no such characters, its length is added to the total count returned by the function.
    Otherwise, the inner loop breaks and the word is skipped.
    """

    counter = Counter(chars)
    result = 0

    for word in words:
        curr_word = defaultdict(int)
        flag = True

        for char in word:
            curr_word[char] += 1

            if char not in chars or curr_word[char] > counter[char]:
                flag = False
                break

        if flag:
            result += len(word)

    return result


if __name__ == "__main__":
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"

    print(countCharacters(words, chars))
    # 6
