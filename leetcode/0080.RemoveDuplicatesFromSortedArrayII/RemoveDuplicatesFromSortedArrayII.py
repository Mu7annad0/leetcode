from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
        The relative order of the elements should be kept the same.

        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
        More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
        It does not matter what you leave beyond the first k elements.

        Return k after placing the final result in the first k slots of nums.

        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
        """
        k, i = 1, 1
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1]:
                i += 1
                if i <=2:
                    nums[k] = nums[r]
                    k += 1
            else:
                i = 1
                nums[k] = nums[r]
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
