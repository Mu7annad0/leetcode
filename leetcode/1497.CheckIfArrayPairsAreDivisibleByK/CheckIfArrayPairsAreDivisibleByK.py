from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        Given an array of integers arr of even length n and an integer k.

        We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

        Return true If you can find a way to do that or false otherwise.
        """
        
        # Initialize a frequency array to count the occurrences of each remainder when divided by k
        freq = [0] * k
        for num in arr:
            # Calculate the remainder of the number when divided by k, ensuring it's always positive
            rem = ((num % k)+k)%k
            # Increment the frequency of the remainder
            freq[rem] += 1

        # If the frequency of remainder 0 is odd, it's impossible to pair them up, so return False
        if freq[0] % 2 != 0:
            return False
        
        # Check if the frequencies of complementary remainders are equal
        for i in range(1, (k//2) + 1):
            if freq[i] != freq[k-i]:
                return False

        return True
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,10,6,7,8,9]
    k = 5
    s = Solution()
    print(s.canArrange(arr, k))