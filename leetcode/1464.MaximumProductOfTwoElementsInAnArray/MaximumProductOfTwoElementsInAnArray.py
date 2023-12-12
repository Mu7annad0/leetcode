def maxProduct(nums):
    """
    res = 0

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            res = max(res, (nums[i] - 1) * (nums[j] - 1))

    return res"""

    largest, second_largest = 0, 0
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        else:
            second_largest = max(second_largest, nums[i])

    return (largest - 1) * (second_largest - 1)


if __name__ == '__main__':
    nums = [1, 5, 4, 5]
    print(maxProduct(nums))
    # 16
