from typing import Counter, List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times. 
        You may assume that the majority element always exists in the array.
        """
        counter = Counter(nums)
        print(counter)
        print(len(nums))
        for k, v in counter.items():
            if v > len(nums) / 2:
                return k

        # Sort the array in ascending order
        # nums.sort()
        # Return the element at the middle index, which is guaranteed to be the majority element
        # return nums[len(nums) // 2]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2, 1, 2, 3, 3, 1, 1, 1]
    print(s.majorityElement(nums))