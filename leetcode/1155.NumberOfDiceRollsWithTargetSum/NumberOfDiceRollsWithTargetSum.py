def numRollsToTarget(n, k, target):


    dp = [[0] * (target+1) for _ in range(n+1)]
    dp[0][0] = 1

    for dice in range(1, n+1):
        for tgt in range(target+1):
            dp[dice][tgt] = sum(dp[dice-1][tgt-roll] for roll in range(1, min(tgt, k)+1))

    return dp[n][target]

if __name__ == "__main__":
    target = 7
    n = 2
    k = 6
    #dp = [[0] * (target + 1) for _ in range(n + 1)]
    print(numRollsToTarget(n, k, target))