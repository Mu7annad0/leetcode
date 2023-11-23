def reverseWords(s):

    """
    The function takes a string s as input and splits it into individual words using the split() method with a parameter of [::-1].
    This will split the string into a list of words in reverse order.
    The function then uses the join() method to join the list of words back together into a single string, separated by spaces.
    The resulting string will be the original sentence with the words in reverse order.
    """
    words = s.split()[::-1]  # splitting the sentence and reverse the words
    return " ".join(words)


# another way to do the inverse
"""
def reverseWords(s):

        s = s.split()
        the_output = ""

        for idx, word in enumerate(reversed(s)):

            if (idx+1) == len(s):
                the_output += word
            else:
                the_output += word + " "
        return the_output
"""
if __name__ == "__main__":

    s = "the sky is blue"
    print(reverseWords(s))
    # blue is sky the