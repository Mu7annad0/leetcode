def largestGoodInteger(num):
    """
    This function iterates through each triple-digit sequence in the input 'num' string,
    checking if all three digits are equal. It keeps track of the largest such sequence and returns it.
    If no consecutive triple-digit sequence with equal digits is found, the function returns an empty string.
    """
    num_good = "0"

    for i in range(len(num) - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            num_good = max(num_good, num[i: i + 3])

    return "" if num_good == "0" else num_good


if __name__ == "__main__":
    num = "6777133339"
    print(largestGoodInteger(num))
    # 777
