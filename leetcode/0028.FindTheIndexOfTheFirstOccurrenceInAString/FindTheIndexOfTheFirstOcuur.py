def strStr(haystack, needle):

    """

    The function checks if the input string needle is empty and returns 0 if it is.
    This is because an empty string cannot be found within another string.
    If needle is not empty, the function iterates through each character of haystack starting from the first character,
    and compares a slice of haystack (of length len(needle)) to needle. If the slice matches needle,
     the function returns the index i where the match occurred. If no match is found, the function returns -1.
    """
    
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1


    # Another way:

    # for i in range(len(haystack) - len(needle) + 1):
    #     for j in range(len(needle)):
    #         if haystack[i + j] != needle[j]:
    #             break
    #         if j == len(needle) - 1:
    #             return i
    # return -1

if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    print(strStr(haystack, needle))
    # 0