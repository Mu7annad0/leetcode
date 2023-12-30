def minDifficulty(jobDifficulty, d):
    if len(jobDifficulty) < d:
        return -1
    total_sum = sum(jobDifficulty)
    if total_sum == 0:
        return 0
    memo = [[0] * len(jobDifficulty) for _ in range(d + 1)]
    helper(jobDifficulty, d, 0, memo)

    return memo[d][0]


def helper(jd, daysLeft, idx, memo):
    length = len(jd)
    if memo[daysLeft][idx] != 0:
        return
    if daysLeft == 1:
        num = max(jd[idx:])
        memo[daysLeft][idx] = num
        return
    max_difficulty = jd[idx]
    daysLeft -= 1
    stop = length - idx - daysLeft + 1

    res = float('inf')
    for i in range(1, stop):
        max_difficulty = max(max_difficulty, jd[idx + i - 1])
        other = memo[daysLeft][idx + i]
        if other == 0:
            helper(jd, daysLeft, idx + i, memo)
            other = memo[daysLeft][idx + i]
        res = min(res, other + max_difficulty)
    memo[daysLeft + 1][idx] = res


if __name__ == '__main__':
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    print(minDifficulty(jobDifficulty, d))
    # 7
