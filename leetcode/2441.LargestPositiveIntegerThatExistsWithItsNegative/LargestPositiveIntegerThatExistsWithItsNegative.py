def findMaxK(nums):
    nums.sort()
    l = 0
    if nums[l] >= 0 or max(nums) < 0 or len(nums) < 2:
        return -1
    while nums[l] < 0:
        if -nums[l] in nums:
            return -nums[l]
        else:
            l += 1
    return -1


if __name__ == '__main__':
    nums = [-956, -831, -707]

    print(findMaxK(nums))
