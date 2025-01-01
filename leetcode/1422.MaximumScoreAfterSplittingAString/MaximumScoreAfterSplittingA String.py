class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score = max(score, s[:i].count('0') + s[i:].count('1'))
        return score
    

if __name__ == '__main__':
    # Test the function
    s = "011101"
    sol = Solution()
    print(sol.maxScore(s))
    # Expected output: 5
