from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        output = 0
        happiness.sort(reverse=True)
        for i, n in enumerate(happiness[:k]):
            output += max(n - i, 0)
        return output


if __name__ == '__main__':
    happiness = [2, 3, 4, 5]
    k = 1
    solution = Solution()
    result = solution.maximumHappinessSum(happiness, k)
    print(result)
