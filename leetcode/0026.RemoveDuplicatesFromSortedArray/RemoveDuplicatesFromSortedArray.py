from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
        The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
            The remaining elements of nums are not important as well as the size of nums.
        2. Return k.
        """
        k = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[k] = nums[r]
                k += 1
        return k

        # k, p =1, 1
        # while p < len(nums):
        #     if nums[p] != nums[p-1]:
        #         nums[k] = nums[p]
        #         k += 1
        #     p += 1
        # return k

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))