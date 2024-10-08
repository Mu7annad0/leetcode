from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        """
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit = max((prices[i] - buy), profit)
            else:
                buy = prices[i]
                
        return profit
    

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))