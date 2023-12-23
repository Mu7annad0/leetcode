def twoSum(nums, target):
    hashma = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashma:
            return [hashma[diff], i]
        hashma[n] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
    # [0, 1]
