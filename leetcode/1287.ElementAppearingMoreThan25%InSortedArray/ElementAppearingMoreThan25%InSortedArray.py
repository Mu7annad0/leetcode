def findSpecialInteger(arr):
    """
    This function takes a list of integers 'arr' and iterates through it to find and return any integer
    that occurs more than 25% of the time in the list; if none is found, it returns -1.
    """
    for i in range(len(arr)):
        if (arr.count(arr[i]) / len(arr)) * 100 > 25:
            return arr[i]

    return -1


if __name__ == '__main__':
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(findSpecialInteger(arr))
    # 6
