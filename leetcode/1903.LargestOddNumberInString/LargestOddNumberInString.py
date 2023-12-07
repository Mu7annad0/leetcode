def largestOddNumber(num: str):
    num_reversed = num[::-1]

    for i in range(len(num)):
        if int(num_reversed[i]) % 2 == 0:
            continue
        else:
            return num_reversed[i:][::-1]

    return ""


if __name__ == "__main__":
    num = "35427"
    print(largestOddNumber(num))
    # 35427
