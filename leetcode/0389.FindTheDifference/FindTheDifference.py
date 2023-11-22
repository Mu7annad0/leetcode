"""
The function takes two strings, s and t, as input and returns a single character that appears in either string but not both.
It does this by iterating through each character in the longer string (either s or t) and checking its count in the other string.
If a character is found to have a different count in the two strings, it is returned immediately.
"""

def find_the_difference(s, t):

    if len(s) > len(t):
        for char in s:
            if s.count(char) > t.count(char):
                return char
    if len(s) < len(t):
        for char in t:
            if s.count(char) < t.count(char):
                return char


if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(find_the_difference(s, t))
    # e