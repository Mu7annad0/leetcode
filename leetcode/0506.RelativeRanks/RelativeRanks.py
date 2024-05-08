from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_scores = sorted(score, reverse=True)

        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)

        output = [rank_map[score[i]] for i in range(len(score))]

        return output


if __name__ == '__main__':

    scores = [10, 3, 8, 9, 4]
    solution = Solution()
    result = solution.findRelativeRanks(scores)
    print(result)
    # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]