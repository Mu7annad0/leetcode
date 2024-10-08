from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
        representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

        Do not return anything, modify nums1 in-place instead.
        """

        # 1. we will use two pointers to compare the elements of the two arrays
        p1 = m -1
        p2 = n -1

        # 2. we will use a third pointer to store the elements of the merged array
        p = m + n - 1

        # 3. we will use a loop to compare the elements of the two arrays
        while p1 >= 0:
            if p2 >= 0 and nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1


if __name__ == "__main__":

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    s = Solution()
    print(s.merge(nums1, m, nums2, n))