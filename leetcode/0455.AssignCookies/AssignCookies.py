def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = j = 0

    while j < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1

    return i


if __name__ == "__main__":
    g = [1, 2]
    s = [1, 2, 3]
    print(findContentChildren(g, s))
    # 2
