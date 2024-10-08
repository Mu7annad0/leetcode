from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)
    print(nums)
    # [5, 6, 7, 1, 2, 3, 4]