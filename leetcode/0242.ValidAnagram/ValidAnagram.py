def isAnagram(s, t):
    # first solution
    """
    flag = True
    if len(s) != len(t):
        flag = False
    for i in range(len(s)):
        if s[i] not in t or s.count(s[i]) != t.count(s[i]):
            flag = False
    return flag
    """

    # second solution
    # return Counter(s) == Counter(t)

    if len(s) != len(t):
        return False
    dictS, dictT = {}, {}
    for i in range(len(s)):
        dictS[s[i]] = 1 + dictS.get(s[i], 0)
        dictT[t[i]] = 1 + dictT.get(t[i], 0)
    return dictS == dictT


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    # True
