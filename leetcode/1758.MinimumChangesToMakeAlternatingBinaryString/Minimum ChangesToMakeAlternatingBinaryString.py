def minOperations(s):
    # another solution
    """def count(s, c):
        count = 0

        for i in range(1, len(s)):
            current = s[i]
            if c == current:
                count += 1
                c = '0' if c == '1' else '1'
            else:
                c = current
        return count

    c = s[0]
    count1 = count(s, c)
    count2 = count(s, '0' if c == '1' else '1') + 1

    return min(count1, count2)"""

    count = 0

    for i in range(len(s)):
        if i % 2 != 0:
            count += 1 if s[i] == '0' else 0
        else:
            count += 1 if s[i] == '1' else 0

    return min(count, len(s) - count)


if __name__ == '__main__':
    s = "1111"
    print(minOperations(s))
    # 2
